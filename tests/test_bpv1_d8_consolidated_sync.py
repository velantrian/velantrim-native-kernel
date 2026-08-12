from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D6 = ROOT / "docs" / "research" / "BPV1_D6_A10_CLASSIFICATION.json"
D7 = ROOT / "docs" / "research" / "BPV1_D7_INTEGRATED_REREVIEW.json"
D8 = ROOT / "docs" / "research" / "BPV1_D8_CONSOLIDATED_SYNC.json"
EN = ROOT / "docs" / "research" / "BPV1_D8_CONSOLIDATED_SYNC.md"
RU = ROOT / "docs" / "research" / "BPV1_D8_CONSOLIDATED_SYNC.ru.md"

EXPECTED_PAGE_IDS = {
    "3a5ac84d-0547-8127-a289-c32763c5050d",
    "3a5ac84d-0547-81cc-920d-ef45a66fe953",
    "3a5ac84d-0547-815b-a58b-d2ed52771601",
    "3b7ac84d-0547-81ff-8f04-cf967ff80069",
    "3b4ac84d-0547-81d4-b9ce-df8b0f8616bc",
    "3b7ac84d-0547-8112-8595-ca44940cc242",
    "3b7ac84d-0547-8101-ada4-de9702b68eb3",
}


class BPV1D8ConsolidatedSyncTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.d6 = json.loads(D6.read_text(encoding="utf-8"))
        cls.d7 = json.loads(D7.read_text(encoding="utf-8"))
        cls.d8 = json.loads(D8.read_text(encoding="utf-8"))
        cls.en = EN.read_text(encoding="utf-8")
        cls.ru = RU.read_text(encoding="utf-8")

    def test_identity_and_source_checkpoint(self) -> None:
        self.assertEqual(self.d8["protocol"], "nk-option-d-consolidated-sync/1")
        self.assertEqual(self.d8["sync_id"], "BPV1-001-D8-consolidated-sync-v1")
        self.assertEqual(self.d8["source_checkpoint_sha"], "491ff7b229606d228ca04985b19b146878390e08")
        self.assertEqual(self.d8["d7_rereview_merge_sha"], self.d8["source_checkpoint_sha"])
        self.assertEqual(self.d8["d6_classification_merge_sha"], "030d0a0585bd061b27329a38e29708c11304701a")

    def test_seven_existing_notion_surfaces_were_read_back(self) -> None:
        sync = self.d8["notion_sync"]
        self.assertEqual(sync["status"], "COMPLETE / READ_BACK_VERIFIED")
        self.assertEqual(sync["surface_count"], 7)
        self.assertEqual(sync["read_back_verified_count"], 7)
        self.assertEqual(sync["new_pages_created"], 0)
        self.assertTrue(sync["historical_content_preserved"])
        surfaces = sync["surfaces"]
        self.assertEqual(len(surfaces), 7)
        self.assertEqual({item["page_id"] for item in surfaces}, EXPECTED_PAGE_IDS)
        self.assertTrue(all(item["read_back_verified"] for item in surfaces))

    def test_d6_classification_is_preserved(self) -> None:
        result = self.d8["synchronized_result"]
        supported = [row["hypothesis_id"] for row in self.d6["classifications"] if row["outcome"] == "SUPPORTED_FOR_SCOPE"]
        not_tested = [row["hypothesis_id"] for row in self.d6["classifications"] if row["outcome"] == "NOT_TESTED"]
        self.assertEqual(result["SUPPORTED_FOR_SCOPE"], supported)
        self.assertEqual(result["NOT_TESTED"], not_tested)
        self.assertEqual(len(supported), 6)
        self.assertEqual(len(not_tested), 6)
        self.assertEqual(result["WEAKENED"], [])
        self.assertEqual(result["REFUTED"], [])
        self.assertEqual(result["INDETERMINATE"], [])

    def test_d7_provisional_position_is_preserved(self) -> None:
        self.assertEqual(self.d8["synchronized_result"]["architecture_position"], self.d7["architecture_position"])
        self.assertFalse(self.d8["synchronized_result"]["universal_substrate_independence_proven"])
        self.assertFalse(self.d8["synchronized_result"]["final_canon_authorized"])
        self.assertFalse(self.d8["synchronized_result"]["independent_implementation_validation_established"])
        self.assertFalse(self.d8["synchronized_result"]["independent_custody_established"])
        self.assertFalse(self.d8["synchronized_result"]["independent_computation_model_established"])
        self.assertFalse(self.d8["synchronized_result"]["composition_federation_conformance_established"])

    def test_runtime_and_operator_boundaries_remain_closed(self) -> None:
        governance = self.d8["governance"]
        self.assertEqual(governance["runtime_expansion"], "FROZEN")
        self.assertFalse(governance["product_runtime_thaw"])
        self.assertFalse(governance["production_authorized"])
        self.assertEqual(governance["p1_c5_role"], "BOUNDED_REFERENCE_LABORATORY")
        self.assertEqual(governance["rust_subject_role"], "FALSIFICATION_INSTRUMENT_ONLY")
        self.assertIn("PENDING_OPERATOR", governance["issue_18"])
        self.assertIn("PENDING_OPERATOR", governance["issue_74_adr0024"])
        self.assertIn("OPERATOR_CONTROLLED", governance["track_h_source_admission"])

    def test_next_gate_is_required_but_not_authorized_by_d8(self) -> None:
        self.assertEqual(self.d8["next_gate"], "OPERATOR_CANON_RUNTIME_DECISION_REQUIRED")
        self.assertFalse(self.d8["next_gate_authorized_by_d8"])
        self.assertTrue(self.d8["operator_decision_required"])
        self.assertTrue(self.d8["github_remains_technical_authority"])

    def test_bilingual_records_preserve_final_boundaries(self) -> None:
        for text in (self.en, self.ru):
            for marker in (
                "7",
                "STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL",
                "OPERATOR_CANON_RUNTIME_DECISION_REQUIRED",
                "FROZEN",
                "Final Canon",
                "NOT_TESTED",
            ):
                self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
