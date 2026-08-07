from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from native_kernel.sqlite_profile.conformance import build_report
from tools.conformance.validate_p5_report import validate_sqlite

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "contracts" / "fixtures" / "fixture-pack.json"


class P5SQLiteIntegrationTests(unittest.TestCase):
    def test_full_sqlite_c1_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            report = build_report(
                FIXTURES,
                database_path=str(Path(directory) / "p5.db"),
                conformance_level="C1",
                evidence_level="LOCALLY_TESTED",
            )
        validate_sqlite(report, require_c2=False)
        counts = {status: sum(item["status"] == status for item in report["assertion_results"])
                  for status in ("SUPPORTED", "PARTIAL", "UNSUPPORTED", "FAILED")}
        self.assertEqual(counts, {"SUPPORTED": 41, "PARTIAL": 13, "UNSUPPORTED": 18, "FAILED": 0})


if __name__ == "__main__":
    unittest.main()
