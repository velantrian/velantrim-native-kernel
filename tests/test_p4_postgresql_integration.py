from __future__ import annotations

import json
import os
import sys
import unittest
from pathlib import Path

from native_kernel.postgresql_profile.conformance import build_report, render_report

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools" / "conformance"
sys.path.insert(0, str(TOOLS))

import runner  # noqa: E402
import validate_p4_report  # noqa: E402

DSN = os.environ.get("NK_TEST_POSTGRES_DSN")


@unittest.skipUnless(DSN, "NK_TEST_POSTGRES_DSN is required for P4 integration tests")
class P4PostgreSQLIntegrationTests(unittest.TestCase):
    def test_c1_report_executes_all_checks_and_round_trips(self) -> None:
        report = build_report(
            ROOT / "contracts" / "fixture-pack.json",
            dsn=DSN or "",
            conformance_level="C1",
            evidence_level="LOCALLY_TESTED",
            evidence_commit="integration-test",
            evidence_run_id="integration-test",
            python_version=f"{sys.version_info.major}.{sys.version_info.minor}",
            postgresql_version="integration-service",
        )
        runner.validate_evidence_report(report)
        validate_p4_report.validate(report, require_c2=False)
        reparsed = json.loads(render_report(report))
        self.assertEqual(reparsed, report)
        self.assertEqual(report["support_state"], "PARTIAL")
        self.assertEqual(report["kernel_runtime_conformance"], "C1")
        self.assertEqual(len(report["assertion_results"]), 72)
        self.assertTrue(all(check["status"] == "PASS" for check in report["checks"]))
        counts = {
            status: sum(
                1
                for item in report["assertion_results"]
                if item["status"] == status
            )
            for status in ("SUPPORTED", "PARTIAL", "UNSUPPORTED", "FAILED")
        }
        self.assertEqual(
            counts,
            {
                "SUPPORTED": 41,
                "PARTIAL": 13,
                "UNSUPPORTED": 18,
                "FAILED": 0,
            },
        )


if __name__ == "__main__":
    unittest.main()
