#!/usr/bin/env python3
"""Preview or publish author context comments on exact GitHub PR diff lines."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


SHA = re.compile(r"^[0-9a-f]{40}$")
CONTEXT_PREFIX = "Context for reviewers:"


class CommandError(RuntimeError):
    """A subprocess failed with compact diagnostic output."""


@dataclass(frozen=True)
class ContextComment:
    path: str
    line: int
    side: str
    body: str

    def anchor_key(self) -> tuple[str, int, str]:
        return self.path, self.line, self.side


def run(args: list[str], *, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, input=input_text, text=True, capture_output=True)
    if result.returncode != 0:
        command = " ".join(args)
        message = result.stderr.strip() or result.stdout.strip() or "command failed"
        raise CommandError(f"{command}\n{message}")
    return result


def run_json(args: list[str], *, input_value: Any | None = None) -> Any:
    input_text = None if input_value is None else json.dumps(input_value)
    output = run(args, input_text=input_text).stdout
    return json.loads(output)


def run_text(args: list[str]) -> str:
    return run(args).stdout.strip()


def parse_repo(remote_url: str) -> str:
    if remote_url.startswith("git@github.com:"):
        path = remote_url.removeprefix("git@github.com:").removesuffix(".git")
        if path.count("/") == 1:
            return path
    parsed = urlparse(remote_url)
    path = parsed.path.strip("/").removesuffix(".git")
    if parsed.netloc == "github.com" and path.count("/") == 1:
        return path
    raise SystemExit(f"Could not infer OWNER/REPO from origin URL: {remote_url}")


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SystemExit(f"{label} must be a non-empty string.")
    if "\n" in value or "\r" in value:
        raise SystemExit(f"{label} must not contain newlines.")
    return value


def require_body(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SystemExit(f"{label} must be a non-empty string.")
    return value


def load_manifest(path: Path) -> tuple[list[ContextComment], str | None, str]:
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Could not read comments manifest: {error}") from error
    if not isinstance(data, dict):
        raise SystemExit("Comments manifest must be a JSON object.")

    head_sha = require_string(data.get("head_sha"), "head_sha")
    if not SHA.fullmatch(head_sha):
        raise SystemExit("head_sha must be a full lowercase 40-character SHA.")
    manifest_pr = data.get("pr")
    if manifest_pr is not None:
        manifest_pr = require_string(str(manifest_pr), "pr")

    raw_comments = data.get("comments")
    if not isinstance(raw_comments, list) or not raw_comments:
        raise SystemExit("comments must be a non-empty array.")

    comments: list[ContextComment] = []
    seen_anchors: set[tuple[str, int, str]] = set()
    for index, raw_comment in enumerate(raw_comments, start=1):
        label = f"comments[{index}]"
        if not isinstance(raw_comment, dict):
            raise SystemExit(f"{label} must be an object.")
        path_value = require_string(raw_comment.get("path"), f"{label}.path")
        line = raw_comment.get("line")
        if isinstance(line, bool) or not isinstance(line, int) or line < 1:
            raise SystemExit(f"{label}.line must be a positive integer.")
        side = str(raw_comment.get("side", "RIGHT")).upper()
        if side not in {"LEFT", "RIGHT"}:
            raise SystemExit(f"{label}.side must be LEFT or RIGHT.")
        body = require_body(raw_comment.get("body"), f"{label}.body")
        if not body.startswith(CONTEXT_PREFIX):
            raise SystemExit(f"{label}.body must start with '{CONTEXT_PREFIX}'.")
        comment = ContextComment(path=path_value, line=line, side=side, body=body)
        if comment.anchor_key() in seen_anchors:
            raise SystemExit(f"{label} reuses an earlier path, line, and side.")
        seen_anchors.add(comment.anchor_key())
        comments.append(comment)
    return comments, manifest_pr, head_sha


def gh_pr_view(pr: str | None, repo: str) -> dict[str, Any]:
    command = ["gh", "pr", "view"]
    if pr:
        command.append(pr)
    command.extend(["--repo", repo, "--json", "number,url,headRefOid,author"])
    value = run_json(command)
    if not isinstance(value, dict):
        raise SystemExit("gh pr view returned an unexpected response.")
    return value


def paginated_array(endpoint: str) -> list[dict[str, Any]]:
    pages = run_json(["gh", "api", endpoint, "--paginate", "--slurp"])
    if not isinstance(pages, list):
        raise SystemExit(f"GitHub returned an unexpected response for {endpoint}.")
    items: list[dict[str, Any]] = []
    for page in pages:
        if not isinstance(page, list):
            raise SystemExit(f"GitHub returned an unexpected page for {endpoint}.")
        items.extend(item for item in page if isinstance(item, dict))
    return items


def valid_patch_lines(patch: str) -> set[tuple[int, str]]:
    anchors: set[tuple[int, str]] = set()
    old_line: int | None = None
    new_line: int | None = None
    for text in patch.splitlines():
        if text.startswith("@@"):
            match = re.match(r"@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@", text)
            if match is None:
                old_line = None
                new_line = None
                continue
            old_line, new_line = (int(value) for value in match.groups())
            continue
        if old_line is None or new_line is None or text.startswith("\\ No newline"):
            continue
        marker = text[:1]
        if marker == "+":
            anchors.add((new_line, "RIGHT"))
            new_line += 1
        elif marker == "-":
            anchors.add((old_line, "LEFT"))
            old_line += 1
        else:
            anchors.add((new_line, "RIGHT"))
            new_line += 1
            old_line += 1
    return anchors


def load_diff_anchors(repo: str, number: int) -> dict[str, set[tuple[int, str]]]:
    files = paginated_array(f"repos/{repo}/pulls/{number}/files")
    anchors: dict[str, set[tuple[int, str]]] = {}
    for file in files:
        filename = file.get("filename")
        patch = file.get("patch")
        if isinstance(filename, str) and isinstance(patch, str):
            anchors[filename] = valid_patch_lines(patch)
    return anchors


def current_login() -> str:
    value = run_json(["gh", "api", "user"])
    if not isinstance(value, dict) or not isinstance(value.get("login"), str):
        raise SystemExit("Could not determine the authenticated GitHub user.")
    return str(value["login"])


def comment_matches(existing: dict[str, Any], comment: ContextComment, login: str) -> bool:
    user = existing.get("user")
    if not isinstance(user, dict) or user.get("login") != login:
        return False
    existing_line = existing.get("line") or existing.get("original_line")
    existing_side = existing.get("side") or existing.get("original_side")
    return (
        existing.get("path") == comment.path
        and existing_line == comment.line
        and existing_side == comment.side
        and existing.get("body") == comment.body
    )


def existing_comments(repo: str, number: int) -> list[dict[str, Any]]:
    return paginated_array(f"repos/{repo}/pulls/{number}/comments")


def post_comment(repo: str, number: int, head_sha: str, comment: ContextComment) -> dict[str, Any]:
    payload = {
        "body": comment.body,
        "commit_id": head_sha,
        "path": comment.path,
        "line": comment.line,
        "side": comment.side,
    }
    value = run_json(
        [
            "gh",
            "api",
            f"repos/{repo}/pulls/{number}/comments",
            "-X",
            "POST",
            "--input",
            "-",
        ],
        input_value=payload,
    )
    if not isinstance(value, dict):
        raise CommandError("GitHub returned an unexpected response after posting a comment.")
    return value


def result_entry(comment: ContextComment, status: str, **extra: Any) -> dict[str, Any]:
    return {
        "path": comment.path,
        "line": comment.line,
        "side": comment.side,
        "status": status,
        **extra,
    }


def summarize(results: list[dict[str, Any]]) -> dict[str, int]:
    statuses = ("ready", "posted", "duplicate", "failed", "skipped")
    return {status: sum(item["status"] == status for item in results) for status in statuses}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comments", required=True, type=Path, help="Author-context manifest JSON.")
    parser.add_argument("--pr", help="PR number or URL. Defaults to the manifest or current branch PR.")
    parser.add_argument("--repo", help="OWNER/REPO. Defaults to the origin remote.")
    parser.add_argument("--publish", action="store_true", help="Publish comments. Omit for preview.")
    args = parser.parse_args()

    comments, manifest_pr, expected_head = load_manifest(args.comments)
    repo = args.repo or parse_repo(run_text(["git", "remote", "get-url", "origin"]))
    pr = gh_pr_view(args.pr or manifest_pr, repo)
    number = int(pr["number"])
    head_sha = str(pr["headRefOid"])
    if head_sha != expected_head:
        raise SystemExit(f"PR head changed: expected {expected_head}, found {head_sha}.")

    login = current_login()
    author = pr.get("author")
    author_login = author.get("login") if isinstance(author, dict) else None
    if author_login != login:
        raise SystemExit(f"Authenticated user {login} is not PR author {author_login}.")

    anchors = load_diff_anchors(repo, number)
    current_comments = existing_comments(repo, number)
    results: list[dict[str, Any]] = []
    ready: list[ContextComment] = []
    for comment in comments:
        if (comment.line, comment.side) not in anchors.get(comment.path, set()):
            results.append(result_entry(comment, "skipped", error="location is not in the current diff"))
        elif any(comment_matches(item, comment, login) for item in current_comments):
            match = next(item for item in current_comments if comment_matches(item, comment, login))
            results.append(result_entry(comment, "duplicate", url=match.get("html_url")))
        else:
            ready.append(comment)
            results.append(result_entry(comment, "ready", body=comment.body))

    if args.publish and any(item["status"] == "skipped" for item in results):
        output = {
            "repo": repo,
            "pr": number,
            "head_sha": expected_head,
            "mode": "publish",
            "summary": summarize(results),
            "comments": results,
        }
        print(json.dumps(output, indent=2))
        return 1

    if args.publish:
        result_by_key = {(item["path"], item["line"], item["side"]): item for item in results}
        for comment in ready:
            result = result_by_key[comment.anchor_key()]
            try:
                refreshed = gh_pr_view(args.pr or manifest_pr, repo)
            except CommandError as error:
                result.update(status="failed", error=f"could not refresh PR head: {error}")
                continue
            if str(refreshed["headRefOid"]) != expected_head:
                result.update(status="skipped", error="PR head changed before publication")
                continue
            try:
                posted = post_comment(repo, number, expected_head, comment)
                result.update(status="posted", url=posted.get("html_url"))
                current_comments.append(posted)
            except CommandError as error:
                try:
                    refreshed_comments = existing_comments(repo, number)
                except CommandError as readback_error:
                    result.update(
                        status="failed",
                        error=f"{error}\nReadback also failed: {readback_error}",
                    )
                    continue
                match = next(
                    (item for item in refreshed_comments if comment_matches(item, comment, login)),
                    None,
                )
                if match is not None:
                    result.update(status="posted", url=match.get("html_url"), recovered_after_error=True)
                    current_comments = refreshed_comments
                else:
                    result.update(status="failed", error=str(error))

        if any(item["status"] == "posted" for item in results):
            try:
                verified_comments = existing_comments(repo, number)
            except CommandError as error:
                for result in results:
                    if result["status"] == "posted":
                        result.update(
                            status="failed",
                            error=f"post returned success but readback failed: {error}",
                        )
            else:
                for comment in ready:
                    result = result_by_key[comment.anchor_key()]
                    if result["status"] != "posted":
                        continue
                    match = next(
                        (item for item in verified_comments if comment_matches(item, comment, login)),
                        None,
                    )
                    if match is None:
                        result.update(
                            status="failed",
                            error="post returned success but the comment was absent from readback",
                        )
                    else:
                        result.update(url=match.get("html_url"))

    output = {
        "repo": repo,
        "pr": number,
        "head_sha": expected_head,
        "mode": "publish" if args.publish else "preview",
        "summary": summarize(results),
        "comments": results,
    }
    print(json.dumps(output, indent=2))
    unsuccessful = {"failed", "skipped"}
    return 1 if any(item["status"] in unsuccessful for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
