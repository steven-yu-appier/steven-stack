#!/usr/bin/env python3
"""Post GitHub PR review comments as pending draft review threads."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


FINDING_TITLE = re.compile(r"^\[(P[0-3])\] (.+)$")


def run_json(args: list[str]) -> Any:
    result = run(args)
    return json.loads(result.stdout)


def run_text(args: list[str]) -> str:
    result = run(args)
    return result.stdout.strip()


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, text=True, capture_output=True)
    if result.returncode != 0:
        command = " ".join(args)
        message = result.stderr.strip() or result.stdout.strip() or "command failed"
        raise SystemExit(f"{command}\n{message}")
    return result


def parse_repo(remote_url: str) -> str:
    if remote_url.startswith("git@github.com:"):
        path = remote_url.removeprefix("git@github.com:").removesuffix(".git")
        return path
    parsed = urlparse(remote_url)
    path = parsed.path.strip("/").removesuffix(".git")
    if parsed.netloc == "github.com" and path.count("/") == 1:
        return path
    raise SystemExit(f"Could not infer OWNER/REPO from origin URL: {remote_url}")


def load_comments(path: Path) -> tuple[list[dict[str, Any]], str | None, str | None]:
    data = json.loads(path.read_text())
    comments = data["comments"] if isinstance(data, dict) else data
    if not isinstance(comments, list):
        raise SystemExit("Comments input must be a JSON array or an object with a comments array.")
    if not comments:
        raise SystemExit("Comments input must include at least one comment.")
    normalized: list[dict[str, Any]] = []
    for index, comment in enumerate(comments, start=1):
        if not isinstance(comment, dict):
            raise SystemExit(f"Comment {index} is not an object.")
        missing = {"path", "line", "body"} - set(comment)
        if missing:
            raise SystemExit(f"Comment {index} is missing: {', '.join(sorted(missing))}")
        body = str(comment["body"])
        lines = body.splitlines()
        title_match = FINDING_TITLE.fullmatch(lines[0] if lines else "")
        if title_match is None:
            raise SystemExit(
                f"Comment {index} must start with '[P0]' through '[P3]' followed by a title."
            )
        severity, title = title_match.groups()
        non_blocking = title.startswith("Non-blocking: ") and bool(
            title.removeprefix("Non-blocking: ").strip()
        )
        if severity == "P3" and not non_blocking:
            raise SystemExit(
                f"Comment {index} must format P3 as '[P3] Non-blocking: <title>'."
            )
        if severity != "P3" and title.startswith("Non-blocking"):
            raise SystemExit(f"Comment {index} cannot mark {severity} as non-blocking.")
        if len(lines) < 3 or lines[1] != "" or not "\n".join(lines[2:]).strip():
            raise SystemExit(
                f"Comment {index} must include one blank line and actionable feedback after its title."
            )
        normalized.append(
            {
                "path": str(comment["path"]),
                "line": int(comment["line"]),
                "side": str(comment.get("side", "RIGHT")),
                "body": body,
            }
        )
    manifest_pr = str(data["pr"]) if isinstance(data, dict) and data.get("pr") is not None else None
    manifest_head = str(data["head_sha"]) if isinstance(data, dict) and data.get("head_sha") is not None else None
    return normalized, manifest_pr, manifest_head


def gh_pr_view(pr: str | None) -> dict[str, Any]:
    cmd = ["gh", "pr", "view"]
    if pr:
        cmd.append(pr)
    cmd.extend(["--json", "number,url,headRefOid"])
    return run_json(cmd)


def current_login() -> str:
    data = run_json(["gh", "api", "user"])
    return str(data["login"])


def pr_node_and_pending_review(repo: str, number: int, login: str) -> tuple[str, dict[str, Any] | None]:
    owner, name = repo.split("/", 1)
    query = """
query($owner:String!, $name:String!, $number:Int!) {
  repository(owner:$owner, name:$name) {
    pullRequest(number:$number) {
      id
      reviews(first:50, states:PENDING) {
        nodes {
          id
          databaseId
          state
          author { login }
          commit { oid }
        }
      }
    }
  }
}
"""
    data = run_json(
        [
            "gh",
            "api",
            "graphql",
            "-f",
            f"query={query}",
            "-f",
            f"owner={owner}",
            "-f",
            f"name={name}",
            "-F",
            f"number={number}",
        ]
    )
    pr = data["data"]["repository"]["pullRequest"]
    pending = None
    for review in pr["reviews"]["nodes"]:
        if review.get("author", {}).get("login") == login:
            pending = review
            break
    return str(pr["id"]), pending


def create_pending_review(repo: str, number: int, commit_id: str, comments: list[dict[str, Any]]) -> dict[str, Any]:
    payload = {"commit_id": commit_id, "threads": comments}
    temp_path = Path("/tmp/post-pending-review-comments.json")
    temp_path.write_text(json.dumps(payload))
    return run_json(
        [
            "gh",
            "api",
            f"repos/{repo}/pulls/{number}/reviews",
            "-X",
            "POST",
            "--input",
            str(temp_path),
        ]
    )


def add_thread(review_id: str, comment: dict[str, Any]) -> dict[str, Any]:
    query = """
mutation($reviewId: ID!, $path: String!, $line: Int!, $side: DiffSide!, $body: String!) {
  addPullRequestReviewThread(input: {
    pullRequestReviewId: $reviewId,
    path: $path,
    line: $line,
    side: $side,
    body: $body
  }) {
    thread { id path line }
  }
}
"""
    return run_json(
        [
            "gh",
            "api",
            "graphql",
            "-f",
            f"query={query}",
            "-f",
            f"reviewId={review_id}",
            "-f",
            f"path={comment['path']}",
            "-F",
            f"line={comment['line']}",
            "-f",
            f"side={comment['side']}",
            "-f",
            f"body={comment['body']}",
        ]
    )


def review_comment_count(repo: str, number: int, review_database_id: int) -> int:
    comments = run_json(["gh", "api", f"repos/{repo}/pulls/{number}/reviews/{review_database_id}/comments"])
    return len(comments)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comments", required=True, type=Path)
    parser.add_argument("--pr", help="PR number or URL. Defaults to current branch PR.")
    parser.add_argument("--repo", help="OWNER/REPO. Defaults to origin remote.")
    parser.add_argument("--expected-head", help="Fail unless the current PR head SHA matches this value.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    comments, manifest_pr, manifest_head = load_comments(args.comments)
    repo = args.repo or parse_repo(run_text(["git", "remote", "get-url", "origin"]))
    pr = gh_pr_view(args.pr or manifest_pr)
    number = int(pr["number"])
    head_oid = str(pr["headRefOid"])
    expected_head = args.expected_head or manifest_head
    if expected_head and expected_head != head_oid:
        raise SystemExit(
            f"PR head changed: expected {expected_head}, found {head_oid}. Refusing to post stale comments."
        )
    login = current_login()
    _pr_node_id, pending = pr_node_and_pending_review(repo, number, login)

    summary = {
      "repo": repo,
      "pr": number,
      "headRefOid": head_oid,
      "existingPendingReview": pending,
      "commentCountToAdd": len(comments),
    }
    if args.dry_run:
        print(json.dumps(summary, indent=2))
        return 0

    if pending:
        for comment in comments:
            add_thread(str(pending["id"]), comment)
        review_id = int(pending["databaseId"])
        state = pending["state"]
    else:
        created = create_pending_review(repo, number, head_oid, comments)
        review_id = int(created["id"])
        state = str(created["state"])

    total = review_comment_count(repo, number, review_id)
    print(
        json.dumps(
            {
                "repo": repo,
                "pr": number,
                "reviewId": review_id,
                "state": state,
                "added": len(comments),
                "draftCommentsInReview": total,
                "submitted": False,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
