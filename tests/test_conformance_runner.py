from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools" / "conformance"
sys.path.insert(0, str(TOOLS))

import runner  # noqa: E402
from runner import (  # noqa: E402
    ContractError,
    canonical_json_bytes,
    content_hash,
    validate_evidence_report,
)


class CanonicalEncodingTests(unittest.TestCase):
    def test_key_order_is_deterministic(self) -> None:
        self.assertEqual(canonical_json_bytes({"b": 2, "a": 1}), b'{"a":1,"b":2}')

    def test_non_nfc_is_rejected(self) -> None:
        with self.assertRaises(ContractError):
            content_hash({"text": "e\u0301"})

    def test_float_is_rejected(self) -> None:
        with self.assertRaises(ContractError):
            content_hash({"value": 1.25})

    def test_null_is_rejected(self) -> None:
        with self.assertRaises(ContractError):
            content_hash({"value": None})


class FixtureRunnerTests(unittest.TestCase):
    def test_fixture_pack_passes(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(TOOLS / "runner.py"), "validate"],
            cwd=ROOT,
            check=False,
            text=True,
            capture_output=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        report = json.loads(completed.stdout)
        self.assertEqual(report["support_state"], "SUPPORTED")
        self.assertEqual(report["kernel_runtime_conformance"], "UNSUPPORTED")
        self.assertEqual(len(report["assertion_results"]), 72)
        self.assertTrue(all(item["status"] == "UNSUPPORTED" for item in report["assertion_results"]))

    def test_payload_hash_tampering_is_rejected(self) -> None:
        pack = json.loads((ROOT / "contracts" / "fixture-pack.json").read_text(encoding="utf-8"))
        pack["event_scenarios"]["scenarios"][0]["events"][0]["payload_hash"] = "nkp1:" + "0" * 64
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture-pack.json"
            path.write_text(json.dumps(pack), encoding="utf-8")
            with patch.object(runner, "PACK", path):
                with self.assertRaisesRegex(ContractError, "payload hash mismatch"):
                    runner.validate_events([])

    def test_incomplete_adapter_assertion_coverage_is_rejected(self) -> None:
        assertion_ids = sorted(runner._registry_assertion_ids())
        report = {
            "report_version": "nk-evidence-report/1",
            "profile_id": "test/incomplete",
            "support_state": "PARTIAL",
            "kernel_runtime_conformance": "C0",
            "evidence_level": "DOCUMENTED",
            "assertion_results": [
                {"assertion_id": assertion_id, "status": "UNSUPPORTED"}
                for assertion_id in assertion_ids[:-1]
            ],
            "checks": [],
            "limitations": ["test fixture"],
        }
        with self.assertRaisesRegex(ContractError, "assertion coverage mismatch"):
            validate_evidence_report(report)

    def test_duplicate_adapter_assertion_result_is_rejected(self) -> None:
        assertion_ids = sorted(runner._registry_assertion_ids())
        assertion_results = [
            {"assertion_id": assertion_id, "status": "UNSUPPORTED"}
            for assertion_id in assertion_ids
        ]
        assertion_results.append(assertion_results[0].copy())
        report = {
            "report_version": "nk-evidence-report/1",
            "profile_id": "test/duplicate",
            "support_state": "FAILED",
            "kernel_runtime_conformance": "UNSUPPORTED",
            "evidence_level": "LOCALLY_TESTED",
            "assertion_results": assertion_results,
            "checks": [],
            "limitations": ["test fixture"],
        }
        with self.assertRaisesRegex(ContractError, "duplicate assertion results"):
            validate_evidence_report(report)


if __name__ == "__main__":
    unittest.main()
