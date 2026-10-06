#!/usr/bin/env python3
"""Focused tests for the author-context publisher."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import post_author_context_comments as subject


HEAD = "0123456789abcdef0123456789abcdef01234567"


def write_manifest(directory: str, comments: list[dict[str, object]]) -> Path:
    path = Path(directory) / "comments.json"
    path.write_text(json.dumps({"pr": "150", "head_sha": HEAD, "comments": comments}))
    return path


class ManifestTests(unittest.TestCase):
    def test_accepts_multiline_context_body(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            manifest = write_manifest(
                directory,
                [
                    {
                        "path": "src/navigation.ts",
                        "line": 84,
                        "body": "Context for reviewers: chosen behavior.\n\nThe rejected alternative adds coupling.",
                    }
                ],
            )

            comments, pr, head = subject.load_manifest(manifest)

        self.assertEqual(pr, "150")
        self.assertEqual(head, HEAD)
        self.assertEqual(comments[0].side, "RIGHT")

    def test_rejects_finding_body(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            manifest = write_manifest(
                directory,
                [{"path": "src/navigation.ts", "line": 84, "body": "[P3] Non-blocking: note"}],
            )

            with self.assertRaises(SystemExit):
                subject.load_manifest(manifest)

    def test_rejects_two_comments_at_the_same_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            manifest = write_manifest(
                directory,
                [
                    {
                        "path": "src/navigation.ts",
                        "line": 84,
                        "body": "Context for reviewers: first explanation.",
                    },
                    {
                        "path": "src/navigation.ts",
                        "line": 84,
                        "body": "Context for reviewers: second explanation.",
                    },
                ],
            )

            with self.assertRaises(SystemExit):
                subject.load_manifest(manifest)


class PatchTests(unittest.TestCase):
    def test_maps_added_deleted_and_context_lines(self) -> None:
        patch_text = """@@ -10,3 +10,4 @@
 unchanged
-removed
+added
+another
 unchanged again
"""

        self.assertEqual(
            subject.valid_patch_lines(patch_text),
            {(10, "RIGHT"), (11, "LEFT"), (11, "RIGHT"), (12, "RIGHT"), (13, "RIGHT")},
        )


class WorkflowTests(unittest.TestCase):
    def base_comment(self) -> dict[str, object]:
        return {
            "path": "src/navigation.ts",
            "line": 84,
            "side": "RIGHT",
            "body": "Context for reviewers: this stays here because the provider does not own navigation.",
        }

    def run_main(self, manifest: Path, *, publish: bool = False) -> int:
        arguments = ["post_author_context_comments.py", "--comments", str(manifest)]
        if publish:
            arguments.append("--publish")
        with (
            patch.object(sys, "argv", arguments),
            patch.object(subject, "parse_repo", return_value="owner/repo"),
            patch.object(subject, "run_text", return_value="git@github.com:owner/repo.git"),
            patch.object(
                subject,
                "gh_pr_view",
                return_value={"number": 150, "headRefOid": HEAD, "author": {"login": "author"}},
            ),
            patch.object(subject, "current_login", return_value="author"),
            patch.object(subject, "load_diff_anchors", return_value={"src/navigation.ts": {(84, "RIGHT")}}),
            patch.object(subject, "existing_comments", return_value=[]),
        ):
            return subject.main()

    def test_preview_does_not_publish(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            manifest = write_manifest(directory, [self.base_comment()])
            with patch.object(subject, "post_comment") as post_comment:
                exit_code = self.run_main(manifest)

        self.assertEqual(exit_code, 0)
        post_comment.assert_not_called()

    def test_publish_posts_direct_comment(self) -> None:
        posted = {
            **self.base_comment(),
            "user": {"login": "author"},
            "html_url": "https://github.com/owner/repo/pull/150#discussion_r1",
        }
        with tempfile.TemporaryDirectory() as directory:
            manifest = write_manifest(directory, [self.base_comment()])
            with patch.object(
                subject,
                "post_comment",
                return_value=posted,
            ) as post_comment:
                exit_code = self.run_main(manifest, publish=True)

        self.assertEqual(exit_code, 0)
        post_comment.assert_called_once()

    def test_invalid_anchor_blocks_all_publication(self) -> None:
        comments = [self.base_comment(), {**self.base_comment(), "path": "src/other.ts"}]
        with tempfile.TemporaryDirectory() as directory:
            manifest = write_manifest(directory, comments)
            with patch.object(subject, "post_comment") as post_comment:
                exit_code = self.run_main(manifest, publish=True)

        self.assertEqual(exit_code, 1)
        post_comment.assert_not_called()

    def test_repo_override_is_used_for_pr_resolution(self) -> None:
        response = {"number": 150, "headRefOid": HEAD, "author": {"login": "author"}}
        with patch.object(subject, "run_json", return_value=response) as run_json:
            self.assertEqual(subject.gh_pr_view("150", "owner/repo"), response)

        run_json.assert_called_once_with(
            [
                "gh",
                "pr",
                "view",
                "150",
                "--repo",
                "owner/repo",
                "--json",
                "number,url,headRefOid,author",
            ]
        )

    def test_successful_post_missing_from_readback_fails(self) -> None:
        posted = {**self.base_comment(), "html_url": "https://example.test/comment"}
        with tempfile.TemporaryDirectory() as directory:
            manifest = write_manifest(directory, [self.base_comment()])
            with patch.object(subject, "post_comment", return_value=posted):
                exit_code = self.run_main(manifest, publish=True)

        self.assertEqual(exit_code, 1)


if __name__ == "__main__":
    unittest.main()
