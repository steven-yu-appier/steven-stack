import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location(
    "task_artifacts", Path(__file__).with_name("task-artifacts.py")
)
artifacts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(artifacts)


class TaskArtifactsTest(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.base = Path(self.workspace.name).resolve()
        self.home = self.base / "account"
        self.temp = self.base / "temp"
        self.temp.mkdir()
        self.home_patch = patch.object(Path, "home", return_value=self.home)
        self.temp_patch = patch.object(tempfile, "tempdir", str(self.temp))
        self.home_patch.start()
        self.temp_patch.start()
        self.addCleanup(self.home_patch.stop)
        self.addCleanup(self.temp_patch.stop)

    def command(self, *args):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            artifacts.main(list(args))
        return json.loads(output.getvalue())

    def test_finish_deletes_logs_but_preserves_archive_and_other_runs(self):
        run = self.command("start", "--ticket", "CAMD-123")
        other = self.command("start", "--ticket", "CAMD-123")
        archive = Path(run["archive_dir"])
        self.assertEqual(archive.parent, self.home / ".local/share/plans/CAMD-123")
        self.assertNotEqual(run["archive_dir"], other["archive_dir"])
        (archive / "plan.md").write_text("approved plan")
        (archive / "screenshots").mkdir()
        (archive / "screenshots/after.png").write_bytes(b"retained screenshot")
        scratch = Path(run["scratch_dir"])
        (scratch / "test.log").write_text("disposable")
        (scratch / "raw.json").write_text("{}")
        (scratch / "archive-link").symlink_to(archive, target_is_directory=True)
        result = self.command("finish", "--scratch", str(scratch))
        self.assertTrue(result["removed"])
        self.assertFalse(scratch.exists())
        self.assertEqual((archive / "plan.md").read_text(), "approved plan")
        self.assertEqual((archive / "screenshots/after.png").read_bytes(), b"retained screenshot")
        self.assertTrue(Path(other["scratch_dir"]).is_dir())
        self.assertFalse(self.command("finish", "--scratch", str(scratch))["removed"])

    def test_adhoc_and_invalid_identity(self):
        run = self.command("start", "--task", "artifact-policy")
        self.assertEqual(Path(run["archive_dir"]).parent, self.home / ".local/share/plans/_adhoc/artifact-policy")
        for flag, value in (("--ticket", "../CAMD-1"), ("--task", "../../outside")):
            with self.subTest(value=value), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as failure:
                    self.command("start", flag, value)
                self.assertEqual(failure.exception.code, 1)
        self.assertFalse((self.base / "outside").exists())

    def test_cleanup_refuses_unmarked_directory_symlink_and_tampered_marker(self):
        unmarked = self.temp / "steven-stack-unmarked"
        unmarked.mkdir()
        run = self.command("start", "--task", "cleanup")
        scratch = Path(run["scratch_dir"])
        link = self.temp / "steven-stack-link"
        link.symlink_to(scratch, target_is_directory=True)
        marker = scratch / ".steven-stack-run.json"
        for target in (unmarked, link):
            with self.subTest(target=target.name), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit):
                    self.command("finish", "--scratch", str(target))
        tampered_records = [
            {**run, "scratch_dir": str(unmarked)},
            {**run, "temp_root": str(unmarked)},
            {key: value for key, value in run.items() if key != "temp_root"},
        ]
        for record in tampered_records:
            marker.write_text(json.dumps(record))
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                self.command("finish", "--scratch", str(scratch))
            self.assertTrue(scratch.is_dir())
        self.assertTrue(unmarked.is_dir())
        self.assertTrue(scratch.is_dir())
        self.assertTrue(link.is_symlink())

    def test_unavailable_archive_preserves_diagnostic_output(self):
        run = self.command("start", "--task", "save-failure")
        archive = Path(run["archive_dir"])
        scratch = Path(run["scratch_dir"])
        (scratch / "failure.log").write_text("needed diagnostic")
        archive.rmdir()
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.command("finish", "--scratch", str(scratch))
        self.assertEqual((scratch / "failure.log").read_text(), "needed diagnostic")

    def test_cleanup_survives_changed_temp_root(self):
        run = self.command("start", "--task", "resume-cleanup")
        scratch = Path(run["scratch_dir"])
        archive = Path(run["archive_dir"])
        (scratch / "test.log").write_text("disposable")
        (archive / "task.md").write_text("verified result")
        other_temp = self.base / "other-temp"
        other_temp.mkdir()
        unrelated = other_temp / "keep.log"
        unrelated.write_text("another task")
        with patch.object(tempfile, "tempdir", str(other_temp)):
            self.assertTrue(self.command("finish", "--scratch", str(scratch))["removed"])
            self.assertFalse(self.command("finish", "--scratch", str(scratch))["removed"])
        self.assertFalse(scratch.exists())
        self.assertEqual((archive / "task.md").read_text(), "verified result")
        self.assertEqual(unrelated.read_text(), "another task")


if __name__ == "__main__":
    unittest.main()
