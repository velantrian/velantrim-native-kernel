from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from native_kernel.sqlite_profile.equivalence import build_comparison_report
from tools.conformance.validate_p5_report import validate_c3

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "contracts" / "fixtures" / "fixture-pack.json"


@unittest.skipUnless(os.environ.get("NK_TEST_POSTGRES_DSN"), "PostgreSQL DSN required")
class P5CrossProfileIntegrationTests(unittest.TestCase):
    def test_full_assertion_scoped_c3_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            report = build_comparison_report(
                FIXTURES,
                dsn=os.environ["NK_TEST_POSTGRES_DSN"],
                sqlite_path=str(Path(directory) / "p5-c3.db"),
                evidence_level="LOCALLY_TESTED",
            )
        validate_c3(report, require_repository=False)
        counts = {status: sum(item["status"] == status for item in report["assertion_results"])
                  for status in ("SUPPORTED", "PARTIAL", "UNSUPPORTED", "FAILED")}
        self.assertEqual(counts, {"SUPPORTED": 45, "PARTIAL": 10, "UNSUPPORTED": 17, "FAILED": 0})


if __name__ == "__main__":
    unittest.main()
