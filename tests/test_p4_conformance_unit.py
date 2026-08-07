from __future__ import annotations

import json
import unittest
from pathlib import Path

from native_kernel.postgresql_profile import conformance
from native_kernel.postgresql_profile.conformance import (
    ConformanceCheck,
    ConformanceExecutionError,
)

ROOT = Path(__file__).resolve().parents[1]


class P4AssertionMappingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = json.loads(
            (ROOT / "contracts" / "registry.json").read_text(encoding="utf-8")
        )

    def test_mapping_covers_all_72_assertions_with_expected_counts(self) -> None:
        results = conformance._assertion_results(self.registry)
        self.assertEqual(len(results), 72)
        self.assertEqual(len({item["assertion_id"] for item in results}), 72)
        counts = {
            status: sum(1 for item in results if item["status"] == status)
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

    def test_proposed_epistemic_family_remains_unsupported(self) -> None:
        results = {
            item["assertion_id"]: item
            for item in conformance._assertion_results(self.registry)
        }
        for index in range(1, 9):
            item = results[f"NK-EPI-{index:03d}"]
            self.assertEqual(item["status"], "UNSUPPORTED")
            self.assertIn("PROPOSED", "\n".join(item["limitations"]))

    def test_supported_and_partial_results_are_traceable(self) -> None:
        results = conformance._assertion_results(self.registry)
        check_ids = {
            check_id
            for mapping in (conformance.SUPPORTED, conformance.PARTIAL)
            for evidence, _ in mapping.values()
            for check_id in evidence
        }
        checks = [
            ConformanceCheck(check_id, "PASS", "unit fixture")
            for check_id in sorted(check_ids)
        ]
        conformance._validate_traceability(results, checks)

    def test_missing_or_failed_evidence_is_rejected(self) -> None:
        results = conformance._assertion_results(self.registry)
        with self.assertRaisesRegex(ConformanceExecutionError, "unknown evidence check"):
            conformance._validate_traceability(results, [])
        check_ids = {
            check_id
            for mapping in (conformance.SUPPORTED, conformance.PARTIAL)
            for evidence, _ in mapping.values()
            for check_id in evidence
        }
        checks = [
            ConformanceCheck(
                check_id,
                "FAIL" if check_id == "p4.identity.golden" else "PASS",
                "unit fixture",
            )
            for check_id in sorted(check_ids)
        ]
        with self.assertRaisesRegex(ConformanceExecutionError, "did not pass"):
            conformance._validate_traceability(results, checks)

    def test_c2_requires_repository_evidence_level(self) -> None:
        with self.assertRaisesRegex(
            ConformanceExecutionError,
            "C2 requires REPOSITORY_REPRODUCED",
        ):
            conformance.build_report(
                ROOT / "contracts" / "fixture-pack.json",
                dsn="unused",
                conformance_level="C2",
                evidence_level="LOCALLY_TESTED",
            )


if __name__ == "__main__":
    unittest.main()
