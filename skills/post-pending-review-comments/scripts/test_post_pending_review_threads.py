from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import post_pending_review_threads as subject


class PendingReviewTransportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        root = Path(self.directory.name)
        gh = root / "gh"
        gh.write_text(
            f"#!{sys.executable}\n"
            "import json, os, pathlib, sys, time\n"
            "if os.environ.get('REVIEW_TEST_FAIL'):\n"
            "    print('request rejected', file=sys.stderr)\n"
            "    sys.exit(7)\n"
            "route = sys.argv[2]\n"
            "barrier = os.environ.get('REVIEW_TEST_BARRIER')\n"
            "if barrier:\n"
            "    root = pathlib.Path(barrier)\n"
            "    (root / route.split('/')[-2]).touch()\n"
            "    deadline = time.monotonic() + 5\n"
            "    while len(list(root.iterdir())) < 2:\n"
            "        if time.monotonic() > deadline:\n"
            "            sys.exit('concurrent request did not arrive')\n"
            "        time.sleep(0.01)\n"
            "source = sys.argv[sys.argv.index('--input') + 1]\n"
            "payload = json.load(sys.stdin) if source == '-' else json.loads(pathlib.Path(source).read_text())\n"
            "print(json.dumps({'route': route, 'payload': payload, 'state': 'PENDING'}))\n"
        )
        gh.chmod(0o700)
        self.environment = {
            "PATH": f"{root}{os.pathsep}{os.environ.get('PATH', '')}",
            "REVIEW_TEST_FAIL": "",
            "REVIEW_TEST_BARRIER": "",
        }
        self.barrier = root / "barrier"
        self.barrier.mkdir()

    def test_concurrent_reviews_keep_their_own_payloads(self) -> None:
        comments = [
            {"path": "src/a.py", "line": 4, "side": "RIGHT", "body": "[P2] 保留值\n\nKeep the original value."},
            {"path": "src/b.py", "line": 9, "side": "LEFT", "body": "[P1] Keep ordering\n\nWait before replacing the result."},
        ]
        with patch.dict(os.environ, {**self.environment, "REVIEW_TEST_BARRIER": str(self.barrier)}):
            with ThreadPoolExecutor(max_workers=2) as pool:
                first = pool.submit(subject.create_pending_review, "team/repo", 11, "head-a", [comments[0]])
                second = pool.submit(subject.create_pending_review, "team/repo", 12, "head-b", [comments[1]])
                results = [first.result(), second.result()]

        self.assertEqual(results, [
            {"route": "repos/team/repo/pulls/11/reviews", "payload": {"commit_id": "head-a", "threads": [comments[0]]}, "state": "PENDING"},
            {"route": "repos/team/repo/pulls/12/reviews", "payload": {"commit_id": "head-b", "threads": [comments[1]]}, "state": "PENDING"},
        ])

    def test_failed_request_reports_error_and_next_request_succeeds(self) -> None:
        comment = {"path": "src/a.py", "line": 4, "side": "RIGHT", "body": "[P2] Preserve data\n\nKeep the value."}
        with patch.dict(os.environ, {**self.environment, "REVIEW_TEST_FAIL": "1"}):
            with self.assertRaisesRegex(SystemExit, "request rejected"):
                subject.create_pending_review("team/repo", 11, "old-head", [comment])

        with patch.dict(os.environ, self.environment):
            result = subject.create_pending_review("team/repo", 12, "new-head", [comment])

        self.assertEqual(result, {
            "route": "repos/team/repo/pulls/12/reviews",
            "payload": {"commit_id": "new-head", "threads": [comment]},
            "state": "PENDING",
        })


if __name__ == "__main__":
    unittest.main()
