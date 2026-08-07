from __future__ import annotations

import copy
import unittest
from pathlib import Path

from native_kernel.shadow_evaluation import ShadowEvaluationError, evaluate, load_json, validate_report
from c4_test_support import make_c3_report

ROOT = Path(__file__).resolve().parents[1]


class C4ReportValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        dataset_path = ROOT / "contracts" / "shadow-workload-v1.json"
        cls.report = evaluate(load_json(dataset_path), make_c3_report(ROOT), dataset_text=dataset_path.read_text(encoding="utf-8"))

    def test_valid_report_passes(self) -> None:
        validate_report(copy.deepcopy(self.report))

    def test_missing_receipt_is_rejected(self) -> None:
        report = copy.deepcopy(self.report)
        report["receipts"].pop()
        with self.assertRaisesRegex(ShadowEvaluationError, "Receipts are incomplete"):
            validate_report(report)

    def test_promotion_decision_is_rejected(self) -> None:
        report = copy.deepcopy(self.report)
        report["promotion_decision"] = "APPROVED"
        with self.assertRaisesRegex(ShadowEvaluationError, "cannot authorize promotion"):
            validate_report(report)

    def test_supported_assertion_without_c4_is_rejected(self) -> None:
        report = copy.deepcopy(self.report)
        row = next(item for item in report["assertion_results"] if item["status"] == "SUPPORTED")
        row["shadow_level"] = "NOT_EVALUATED_C4"
        with self.assertRaisesRegex(ShadowEvaluationError, "every C3-supported"):
            validate_report(report)

    def test_nk_epi_promotion_is_rejected(self) -> None:
        report = copy.deepcopy(self.report)
        row = next(item for item in report["assertion_results"] if item["assertion_id"] == "NK-EPI-001")
        row["status"] = "SUPPORTED"
        row["shadow_level"] = "C4"
        row["case_ids"] = [report["case_results"][0]["case_id"]]
        report["metrics"]["assertion_counts"] = {"SUPPORTED": 46, "PARTIAL": 10, "UNSUPPORTED": 16, "FAILED": 0}
        with self.assertRaises(ShadowEvaluationError):
            validate_report(report)

    def test_truth_proof_overclaim_is_rejected(self) -> None:
        report = copy.deepcopy(self.report)
        report["receipts"][0]["proofs"]["truth_proven"] = True
        with self.assertRaisesRegex(ShadowEvaluationError, "overclaims proof"):
            validate_report(report)


if __name__ == "__main__":
    unittest.main()
