from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D6 = ROOT / "docs" / "research" / "BPV1_D6_A10_CLASSIFICATION.json"
D7 = ROOT / "docs" / "research" / "BPV1_D7_INTEGRATED_REREVIEW.json"
EN = ROOT / "docs" / "research" / "BPV1_D7_INTEGRATED_REREVIEW.md"
RU = ROOT / "docs" / "research" / "BPV1_D7_INTEGRATED_REREVIEW.ru.md"

SUPPORTED = ["A10-H01", "A10-H02", "A10-H04", "A10-H05", "A10-H07", "A10-H12"]
NOT_TESTED = ["A10-H03", "A10-H06", "A10-H08", "A10-H09", "A10-H10", "A10-H11"]


class BPV1D7IntegratedRereviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.d6 = json.loads(D6.read_text(encoding="utf-8"))
        cls.d7 = json.loads(D7.read_text(encoding="utf-8"))
        cls.en = EN.read_text(encoding="utf-8")
        cls.ru = RU.read_text(encoding="utf-8")

    def test_identity_and_input_checkpoint(self) -> None:
        self.assertEqual(self.d7["protocol"], "nk-integrated-post-bpv1-rereview/1")
        self.assertEqual(self.d7["review_id"], "BPV1-001-D7-integrated-rereview-v1")
        self.assertEqual(self.d7["review_kind"], "INTEGRATED_RE_REVIEW / NOT_INDEPENDENT_VALIDATION")
        self.assertEqual(self.d7["input_checkpoint"], "030d0a0585bd061b27329a38e29708c11304701a")
        self.assertEqual(self.d7["inputs"]["d6_classification_merge_sha"], self.d7["input_checkpoint"])

    def test_d6_classification_is_preserved_exactly(self) -> None:
        self.assertEqual(self.d7["d6_summary"]["SUPPORTED_FOR_SCOPE"], SUPPORTED)
        self.assertEqual(self.d7["d6_summary"]["NOT_TESTED"], NOT_TESTED)
        self.assertEqual(self.d7["d6_summary"]["WEAKENED"], [])
        self.assertEqual(self.d7["d6_summary"]["REFUTED"], [])
        self.assertEqual(self.d7["d6_summary"]["INDETERMINATE"], [])
        d6_by_outcome: dict[str, list[str]] = {key: [] for key in ["SUPPORTED_FOR_SCOPE", "WEAKENED", "REFUTED", "INDETERMINATE", "NOT_TESTED"]}
        for row in self.d6["classifications"]:
            d6_by_outcome[row["outcome"]].append(row["hypothesis_id"])
        self.assertEqual(d6_by_outcome, self.d7["d6_summary"])

    def test_review_remains_provisional(self) -> None:
        self.assertEqual(self.d7["review_outcome"], "PROVISIONAL_VALIDATION_REVIEW_COMPLETE")
        self.assertEqual(self.d7["architecture_position"], "STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL")
        conclusions = self.d7["review_conclusions"]
        self.assertTrue(conclusions["tested_semantic_core_strengthened"])
        self.assertFalse(conclusions["a1_a10_final_canon"])
        self.assertFalse(conclusions["universal_substrate_independence_proven"])
        self.assertFalse(conclusions["independent_implementation_validation_established"])
        self.assertFalse(conclusions["independent_computation_model_established"])
        self.assertFalse(conclusions["runtime_thaw_authorized"])
        self.assertFalse(conclusions["production_authorized"])

    def test_open_research_findings_cover_all_not_tested_domains(self) -> None:
        text = json.dumps(self.d7["findings"], ensure_ascii=False)
        for hypothesis_id in NOT_TESTED:
            self.assertIn(hypothesis_id, text)
        for marker in ("representation migration", "Physical and cryptographic erasure", "Analog, neuromorphic and probabilistic", "Storage and computation independence", "Composition and federation"):
            self.assertIn(marker, text)

    def test_h07_limitation_is_preserved(self) -> None:
        finding = next(row for row in self.d7["findings"] if row["finding_id"] == "D7-F07")
        text = (finding["finding"] + " " + finding["architectural_effect"]).lower()
        self.assertIn("same-repository", text)
        self.assertIn("independent implementation", text)
        self.assertIn("conventional digital", text)
        self.assertIn("not_established", text)

    def test_no_local_to_federated_promotion(self) -> None:
        finding = next(row for row in self.d7["findings"] if row["finding_id"] == "D7-F08")
        self.assertIn("No local conformance result", finding["architectural_effect"])

    def test_scoped_substrate_statement_is_stronger_but_not_universal(self) -> None:
        finding = next(row for row in self.d7["findings"] if row["finding_id"] == "D7-F10")
        self.assertIn("one materially different bounded conventional-digital realization", finding["finding"])
        self.assertIn("arbitrary future-substrate support", finding["architectural_effect"])

    def test_next_gate_is_d8_and_runtime_remains_frozen(self) -> None:
        self.assertEqual(self.d7["next_gate"], "D8_CONSOLIDATED_AUTHORITATIVE_SYNC")
        self.assertTrue(self.d7["notion_sync_allowed_at_next_gate"])
        self.assertEqual(self.d7["operator_canon_runtime_decision_after_d8"], "SEPARATE / REQUIRED")
        self.assertEqual(self.d7["runtime_expansion"], "FROZEN")
        self.assertFalse(self.d7["product_runtime_thaw"])
        self.assertFalse(self.d7["production_authorized"])

    def test_bilingual_records_preserve_core_boundaries(self) -> None:
        for text in (self.en, self.ru):
            for marker in (
                "D8_CONSOLIDATED_AUTHORITATIVE_SYNC",
                "NOT_INDEPENDENT_VALIDATION",
                "SUPPORTED_FOR_SCOPE",
                "NOT_TESTED",
                "FROZEN",
                "Final Canon",
            ):
                self.assertIn(marker, text)
            for hypothesis_id in NOT_TESTED:
                self.assertIn(hypothesis_id, text)


if __name__ == "__main__":
    unittest.main()
