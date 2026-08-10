from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = (ROOT / "docs" / "INTEGRATED_A1_A10_REVIEW.md").read_text(encoding="utf-8")
RU = (ROOT / "docs" / "INTEGRATED_A1_A10_REVIEW.ru.md").read_text(encoding="utf-8")
STATE = json.loads((ROOT / "project-state.json").read_text(encoding="utf-8"))


class IntegratedA1A10ReviewTests(unittest.TestCase):
    def test_review_identity_and_next_gate_are_bilingual(self) -> None:
        for markdown in (EN, RU):
            self.assertIn("nk-integrated-blueprint-review/A1-A10-review-1", markdown)
            self.assertIn("COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING", markdown)
            self.assertIn("OPERATOR_POST_BLUEPRINT_DECISION", markdown)
            self.assertIn("Runtime expansion:** `FROZEN`", markdown)

    def test_all_integrated_findings_are_explicit(self) -> None:
        for markdown in (EN, RU):
            for index in range(1, 8):
                self.assertIn(f"IR-F{index:02d}", markdown)

    def test_integrated_closure_taxonomy_preserves_a5_distinctions(self) -> None:
        expected = (
            "LOGICALLY_ERASED",
            "PHYSICALLY_ERASED",
            "CRYPTOGRAPHICALLY_ERASED",
            "FORGOTTEN_OR_LOST",
        )
        for markdown in (EN, RU):
            for literal in expected:
                self.assertIn(literal, markdown)
            self.assertIn("physical", markdown.lower())
            self.assertIn("cryptographic", markdown.lower())
            self.assertIn("INDETERMINATE", markdown)

    def test_a10_outcome_protocol_is_normalized(self) -> None:
        outcomes = ("SUPPORTED_FOR_SCOPE", "WEAKENED", "REFUTED", "INDETERMINATE", "NOT_TESTED")
        for markdown in (EN, RU):
            for outcome in outcomes:
                self.assertIn(outcome, markdown)
            self.assertIn("A10-H03", markdown)
            self.assertIn("A10-H06", markdown)
            self.assertIn("A10-H10", markdown)
            self.assertIn("A10-H11", markdown)

    def test_review_does_not_claim_independence_or_runtime_authority(self) -> None:
        self.assertIn("not independent validation", EN.lower())
        self.assertIn("не является independent validation", RU.lower())
        for markdown in (EN, RU):
            self.assertIn("NOT ESTABLISHED", markdown)
            self.assertIn("runtime", markdown.lower())
            self.assertIn("operator", markdown.lower())

    def test_machine_state_moves_only_to_operator_gate(self) -> None:
        refoundation = STATE["tracks"]["long_horizon_research"]["architecture_refoundation"]
        self.assertEqual("OPERATOR_POST_BLUEPRINT_DECISION", refoundation["next_content_slice"])
        self.assertEqual(10, len(refoundation["completed_deliverables"]))
        self.assertNotIn("INTEGRATED_A1_A10_REVIEW", refoundation["completed_deliverables"])
        self.assertNotIn("OPERATOR_POST_BLUEPRINT_DECISION", refoundation["completed_deliverables"])
        self.assertTrue(refoundation["runtime_expansion_frozen"])
        self.assertFalse(STATE["status"]["production_authorized"])
        self.assertEqual("BOUNDED_REFERENCE_LABORATORY", STATE["tracks"]["clean_implementation"]["architecture_role"])


if __name__ == "__main__":
    unittest.main()
