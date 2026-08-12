from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECISION_PATH = ROOT / "docs" / "research" / "POST_D8_OPERATOR_DECISION.json"
ADR_PATH = ROOT / "docs" / "adr" / "0027-retain-provisional-architecture-and-runtime-freeze-after-option-d.md"
EN_PATH = ROOT / "docs" / "research" / "POST_D8_OPERATOR_DECISION.md"
RU_PATH = ROOT / "docs" / "research" / "POST_D8_OPERATOR_DECISION.ru.md"
D6_PATH = ROOT / "docs" / "research" / "BPV1_D6_A10_CLASSIFICATION.json"
D7_PATH = ROOT / "docs" / "research" / "BPV1_D7_INTEGRATED_REREVIEW.json"
D8_PATH = ROOT / "docs" / "research" / "BPV1_D8_CONSOLIDATED_SYNC.json"

SUPPORTED = ["A10-H01", "A10-H02", "A10-H04", "A10-H05", "A10-H07", "A10-H12"]
NOT_TESTED = ["A10-H03", "A10-H06", "A10-H08", "A10-H09", "A10-H10", "A10-H11"]
SOURCE_CHECKPOINT = "ad459cd5301756936a26cab0997ba6c77c58191b"
D6_MERGE = "030d0a0585bd061b27329a38e29708c11304701a"
D7_MERGE = "491ff7b229606d228ca04985b19b146878390e08"
D8_MERGE = "9ecb2369edec17a0171b6e965bcb49f9526adf0b"


class PostD8OperatorDecisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.decision = json.loads(DECISION_PATH.read_text(encoding="utf-8"))
        cls.d6 = json.loads(D6_PATH.read_text(encoding="utf-8"))
        cls.d7 = json.loads(D7_PATH.read_text(encoding="utf-8"))
        cls.d8 = json.loads(D8_PATH.read_text(encoding="utf-8"))
        cls.adr = ADR_PATH.read_text(encoding="utf-8")
        cls.en = EN_PATH.read_text(encoding="utf-8")
        cls.ru = RU_PATH.read_text(encoding="utf-8")

    def test_decision_identity_and_governance_dimensions(self) -> None:
        self.assertEqual("nk-post-d8-operator-decision/1", self.decision["protocol"])
        self.assertEqual("OD-POST-D8-001", self.decision["decision_id"])
        self.assertEqual(SOURCE_CHECKPOINT, self.decision["source_checkpoint_sha"])
        self.assertEqual("ACCEPTED", self.decision["decision_status"])
        self.assertEqual("APPROVED", self.decision["operator_approval"])
        self.assertEqual("REPOSITORY_REPRODUCED", self.decision["evidence_level"])
        self.assertEqual("COMPLETE", self.decision["implementation_status"])

    def test_d6_evidence_is_not_overgeneralized(self) -> None:
        outcomes = {item["hypothesis_id"]: item["outcome"] for item in self.d6["classifications"]}
        self.assertEqual(SUPPORTED, [item for item in SUPPORTED if outcomes[item] == "SUPPORTED_FOR_SCOPE"])
        self.assertEqual(NOT_TESTED, [item for item in NOT_TESTED if outcomes[item] == "NOT_TESTED"])
        self.assertEqual(6, self.d6["summary"]["SUPPORTED_FOR_SCOPE"])
        self.assertEqual(6, self.d6["summary"]["NOT_TESTED"])
        self.assertEqual(SUPPORTED, self.decision["inputs"]["d6"]["supported_for_scope"])
        self.assertEqual(NOT_TESTED, self.decision["inputs"]["d6"]["not_tested"])
        self.assertEqual(NOT_TESTED, self.decision["residual_validation_targets"])
        self.assertEqual(D6_MERGE, self.decision["inputs"]["d6"]["merge_sha"])

    def test_d7_requires_provisional_architecture(self) -> None:
        expected = "STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL"
        self.assertEqual(expected, self.d7["architecture_position"])
        self.assertFalse(self.d7["review_conclusions"]["a1_a10_final_canon"])
        self.assertFalse(self.d7["review_conclusions"]["runtime_thaw_authorized"])
        self.assertEqual(expected, self.decision["decision"]["architecture_baseline"])
        self.assertEqual(D7_MERGE, self.decision["inputs"]["d7"]["merge_sha"])

    def test_d8_requires_separate_operator_decision(self) -> None:
        self.assertEqual("OPERATOR_CANON_RUNTIME_DECISION_REQUIRED", self.d8["next_gate"])
        self.assertFalse(self.d8["next_gate_authorized_by_d8"])
        self.assertTrue(self.d8["operator_decision_required"])
        self.assertEqual(7, self.d8["notion_sync"]["surface_count"])
        self.assertEqual(7, self.d8["notion_sync"]["read_back_verified_count"])
        self.assertEqual(0, self.d8["notion_sync"]["new_pages_created"])
        self.assertEqual(D8_MERGE, self.decision["inputs"]["d8"]["merge_sha"])

    def test_decision_defers_canon_and_keeps_runtime_frozen(self) -> None:
        result = self.decision["decision"]
        self.assertEqual("DEFERRED / NOT_AUTHORIZED_AT_THIS_CHECKPOINT", result["final_canon"])
        self.assertEqual("NOT_AUTHORIZED_AT_THIS_CHECKPOINT", result["product_runtime_thaw"])
        self.assertEqual("FROZEN", result["runtime_expansion"])
        self.assertFalse(result["production_authorized"])
        self.assertEqual("BOUNDED_REFERENCE_LABORATORY", result["p1_c5_role"])
        self.assertFalse(result["automatic_canon_promotion"])
        self.assertFalse(result["automatic_runtime_promotion"])

    def test_next_gate_is_planning_only(self) -> None:
        result = self.decision["decision"]
        self.assertEqual("RESIDUAL_A10_VALIDATION_PLAN", result["next_gate"])
        self.assertEqual("RESEARCH_PLANNING_ONLY", result["next_gate_scope"])
        self.assertFalse(result["experiment_execution_authorized"])

    def test_reserved_operator_boundaries_are_untouched(self) -> None:
        reserved = self.decision["operator_reserved_boundaries"]
        self.assertEqual("UNCHANGED / PENDING_OPERATOR", reserved["issue_18_license_publication"])
        self.assertEqual("UNCHANGED / PENDING_OPERATOR", reserved["issue_74_adr_0024_reducer_v2"])
        self.assertEqual("UNCHANGED / OPERATOR_CONTROLLED", reserved["track_h_source_admission"])

    def test_human_records_preserve_non_claims(self) -> None:
        for text in (self.adr, self.en, self.ru):
            self.assertIn("STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL", text)
            self.assertIn("RESIDUAL_A10_VALIDATION_PLAN", text)
            self.assertIn("FROZEN", text)
            for hypothesis in NOT_TESTED:
                self.assertIn(hypothesis, text)
        self.assertIn("does **not** promote A1–A10 to Final Canon", self.adr)
        self.assertIn("does **not** thaw product runtime", self.adr)


if __name__ == "__main__":
    unittest.main()
