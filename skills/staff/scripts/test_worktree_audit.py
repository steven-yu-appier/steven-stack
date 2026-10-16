import csv
import io
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(os.environ.get("STAFF_AUDIT_SCRIPT", Path(__file__).with_name("worktree-audit.sh")))


class WorktreeAuditTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="staff-audit-", dir="/private/tmp")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.git("init", "-b", "main")
        (self.repo / ".gitignore").write_text("ignored.txt\n")
        (self.repo / "tracked.txt").write_text("saved\n")
        self.git("add", ".")
        self.git("commit", "-m", "fixture")
        self.git("update-ref", "refs/remotes/origin/main", "HEAD")
        self.git("symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")
        self.worktree = self.root / "candidate"
        self.git("worktree", "add", "-b", "candidate", str(self.worktree))
        self.bin = self.root / "bin"
        self.bin.mkdir()
        self.env = dict(os.environ, PATH=str(self.bin) + os.pathsep + os.environ["PATH"])
        self.stub("gh", "print('[{\"number\":1,\"state\":\"MERGED\",\"headRefName\":\"candidate\"}]')")
        self.stub("jq", """import json, sys
data = json.load(open(sys.argv[-1]))
if '-e' in sys.argv:
    sys.exit(0 if isinstance(data, list) else 1)
branch = sys.argv[sys.argv.index('--arg') + 2]
for item in data:
    if item['headRefName'] == branch:
        print('#' + str(item['number']) + '/' + item['state'])
""")
        self.stub("rg", f"from pathlib import Path\nPath({str(self.root / 'transcript-scan')!r}).touch()")

    def git(self, *args):
        return subprocess.run(
            ["git", "-c", "user.name=Staff Audit Test", "-c", "user.email=audit@example.invalid",
             "-c", "core.hooksPath=/dev/null", *args],
            cwd=self.repo, check=True, capture_output=True, text=True,
        ).stdout.strip()

    def stub(self, name, body):
        path = self.bin / name
        path.write_text(f"#!{sys.executable}\n{body}\n")
        path.chmod(0o755)

    def audit(self, github=True):
        args = ["bash", str(SCRIPT)]
        if github:
            args.append("--github")
        result = subprocess.run(args + [str(self.repo)], env=self.env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = list(csv.DictReader(io.StringIO(result.stdout), delimiter="\t"))
        self.assertEqual(len(rows), 1, result.stdout)
        return rows[0]

    def test_untracked_work_is_held_and_preserved(self):
        file = self.worktree / "unsaved.txt"
        file.write_text("user work\n")
        row = self.audit()
        self.assertTrue(row["DIRTY"].startswith("untracked:"), row)
        self.assertTrue(row["BUCKET"].startswith("hold-"), row)
        self.assertEqual(file.read_text(), "user work\n")

    def test_ignored_work_is_held_and_preserved(self):
        file = self.worktree / "ignored.txt"
        file.write_text("local data\n")
        row = self.audit()
        self.assertTrue(row["DIRTY"].startswith("ignored:"), row)
        self.assertEqual(row["BUCKET"], "hold-local-data")
        self.assertEqual(file.read_text(), "local data\n")

    def test_tracked_work_is_held(self):
        (self.worktree / "tracked.txt").write_text("not saved\n")
        row = self.audit()
        self.assertTrue(row["DIRTY"].startswith("wip:"), row)
        self.assertTrue(row["BUCKET"].startswith("hold-"), row)

    def test_status_failure_is_unknown(self):
        real_git = shutil.which("git")
        self.stub("git", f"""import os, sys
if 'status' in sys.argv[1:]:
    sys.stderr.write('fixture status failure\\n')
    sys.exit(42)
os.execv({real_git!r}, [{real_git!r}, *sys.argv[1:]])
""")
        row = self.audit()
        self.assertEqual(row["DIRTY"], "unknown")
        self.assertEqual(row["BUCKET"], "hold-unknown")

    def test_audit_does_not_search_chat_contents(self):
        self.audit()
        self.assertFalse((self.root / "transcript-scan").exists())

    def test_enumeration_failure_is_not_empty_success(self):
        real_git = shutil.which("git")
        self.stub("git", f"""import os, sys
if 'worktree' in sys.argv[1:] and 'list' in sys.argv[1:]:
    sys.exit(42)
os.execv({real_git!r}, [{real_git!r}, *sys.argv[1:]])
""")
        result = subprocess.run(
            ["bash", str(SCRIPT), str(self.repo)], env=self.env, capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)

    def test_clean_merged_worktree_still_needs_usage_check(self):
        row = self.audit()
        self.assertEqual(row["DIRTY"], "clean")
        self.assertEqual(row.get("USAGE"), "unknown")
        self.assertEqual(row["BUCKET"], "verify-usage")

    def test_paths_with_spaces_are_preserved(self):
        renamed = self.root / "candidate with spaces"
        self.git("worktree", "move", str(self.worktree), str(renamed))
        self.worktree = renamed
        row = self.audit()
        self.assertEqual(row["WORKTREE"], str(renamed))
        self.assertEqual(row["DIRTY"], "clean")

    def test_missing_pr_metadata_is_held(self):
        row = self.audit(github=False)
        self.assertEqual(row["PR"], "unknown")
        self.assertEqual(row["BUCKET"], "hold-unknown")


if __name__ == "__main__":
    unittest.main()
