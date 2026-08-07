from __future__ import annotations

import copy
import json
import os
import tempfile
import unittest
from pathlib import Path

from native_kernel.shadow_evaluation import ShadowEvaluationError, evaluate, load_json, report_from_files, validate_dataset, validate_report
from c4_test_support import make_c3_report

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "contracts" / "shadow-workload-v1.json"


class C4ShadowEvaluationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.dataset = load_json(DATASET)
        self.c3 = make_c3_report(ROOT)

    def test_approved_dataset_passes_and_preserves_map(self) -> None:
        report = evaluate(self.dataset, self.c3, dataset_text=DATASET.read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["kernel_runtime_conformance"], "C4")
        self.assertEqual(report["metrics"]["assertion_counts"], {"SUPPORTED": 45, "PARTIAL": 10, "UNSUPPORTED": 17, "FAILED": 0})
        self.assertEqual(report["metrics"]["c4_shadow_evaluated_assertions"], 45)
        self.assertEqual(len(report["receipts"]), 15)
        self.assertTrue(all(not r["authority_promoted"] and not r["side_effects_executed"] for r in report["receipts"]))
        validate_report(report)

    def test_semantic_divergence_fails_closed(self) -> None:
        dataset = copy.deepcopy(self.dataset)
        dataset["cases"][0]["candidate_observation"]["semantic"]["identity_digest"] = "sha256:tampered"
        report = evaluate(dataset, self.c3)
        self.assertEqual(report["status"], "FAIL")
        self.assertEqual(report["kernel_runtime_conformance"], "C4_FAILED")
        self.assertEqual(report["metrics"]["critical_divergences"], 1)
        with self.assertRaises(ShadowEvaluationError):
            validate_report(report)

    def test_authority_promotion_is_rejected_before_evaluation(self) -> None:
        dataset = copy.deepcopy(self.dataset)
        dataset["authority_policy"]["authority_promotion"] = "ALLOWED"
        with self.assertRaisesRegex(ShadowEvaluationError, "forbid authority promotion"):
            validate_dataset(dataset, {r["assertion_id"]: r["status"] for r in self.c3["assertion_results"]})

    def test_non_supported_assertion_cannot_receive_c4(self) -> None:
        dataset = copy.deepcopy(self.dataset)
        dataset["cases"][0]["assertion_ids"].append("NK-EPI-001")
        with self.assertRaisesRegex(ShadowEvaluationError, "non-C3-supported"):
            evaluate(dataset, self.c3)

    def test_duplicate_case_and_assertion_coverage_are_rejected(self) -> None:
        dataset = copy.deepcopy(self.dataset)
        dataset["cases"].append(copy.deepcopy(dataset["cases"][0]))
        with self.assertRaisesRegex(ShadowEvaluationError, "duplicate C4 case_id"):
            evaluate(dataset, self.c3)

    def test_unapproved_dataset_is_rejected(self) -> None:
        dataset = copy.deepcopy(self.dataset)
        dataset["approval"]["state"] = "DRAFT"
        with self.assertRaisesRegex(ShadowEvaluationError, "explicitly approved"):
            evaluate(dataset, self.c3)

    def test_repository_metadata_is_required_when_requested(self) -> None:
        report = evaluate(self.dataset, self.c3)
        with self.assertRaisesRegex(ShadowEvaluationError, "wrong evidence level"):
            validate_report(report, require_repository=True)
        old = dict(os.environ)
        try:
            os.environ.update({
                "NK_EVIDENCE_COMMIT": "a" * 40,
                "NK_EVIDENCE_RUN_ID": "12345",
                "NK_PYTHON_VERSION": "3.11",
                "NK_POSTGRESQL_VERSION": "16",
                "NK_SQLITE_VERSION": "3.45.1",
            })
            report = evaluate(self.dataset, self.c3)
            validate_report(report, require_repository=True)
        finally:
            os.environ.clear(); os.environ.update(old)

    def test_report_from_files_binds_exact_dataset_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            c3_path = Path(tmp) / "c3.json"
            c3_path.write_text(json.dumps(self.c3), encoding="utf-8")
            report = report_from_files(DATASET, c3_path)
        self.assertTrue(report["dataset"]["sha256"].startswith("sha256:"))
        self.assertTrue(report["prerequisite"]["sha256"].startswith("sha256:"))


if __name__ == "__main__":
    unittest.main()
