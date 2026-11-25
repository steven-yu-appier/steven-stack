import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CheckRecordTest(unittest.TestCase):
    def check_record(self, record):
        with tempfile.TemporaryDirectory() as scratch:
            path = Path(scratch) / "record.md"
            path.write_text(record)
            return subprocess.run(
                [sys.executable, Path(__file__).with_name("check-ac-record.py"), path, "1", "2"],
                capture_output=True, text=True,
            )

    def test_mixed_record_accepts_xml_error(self):
        result = self.check_record(
            "## AC 1\nVerdict: PASS\n## AC 2\nVerdict: BLOCK\n"
            "Attempt: open settings\nError: <Error><Code>AccessDenied</Code></Error>"
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_evidence_from_another_ac_does_not_count(self):
        result = self.check_record(
            "## AC 1\nVerdict: BLOCK\nError:   \n## AC 2\nVerdict: FAIL\n"
            "Attempt: open settings\nError: denied"
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("AC 1: missing Attempt", result.stderr)
        self.assertIn("AC 1: missing Error", result.stderr)

    def test_rejects_missing_duplicate_and_invalid_verdict(self):
        result = self.check_record("## AC 1\nVerdict: skipped\n## AC 1\nVerdict: PASS")
        self.assertNotEqual(result.returncode, 0)
        for message in ("expected one", "duplicate section", "AC 2: missing section"):
            self.assertIn(message, result.stderr)
