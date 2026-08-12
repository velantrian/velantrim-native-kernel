from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = (ROOT / "docs" / "INTEGRATED_A1_A10_REVIEW.md").read_text(encoding="utf-8")
RU = (ROOT / "docs" / "INTEGRATED_A1_A10_REVIEW.ru.md").read_text(encoding="utf-8")
STATE = json.loads((ROOT / "project-state.json").read_text(encoding="utf-8"))


class IntegratedA1A10ReviewTests(unittest.TestCase):
    def test_review_identity_and_historical_next_gate_are_bilingual(self) -> None:
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
        expected = ("LOGICALLY_ERASED", "PHYSICALLY_ERASED", "CRYPTOGRAPHICALLY_ERASED", "FORGOTTEN_OR_LOST")
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

    def test_integrated_review_remains_historical_while_machine_state_advances(self) -> None:
        refoundation = STATE["tracks"]["long_horizon_research"]["architecture_refoundation"]
        validation = STATE["tracks"]["long_horizon_research"]["post_blueprint_validation"]
        self.assertEqual("A10_H11_EXECUTION_ADMISSION", refoundation["next_content_slice"])
        self.assertEqual(10, len(refoundation["completed_deliverables"]))
        self.assertNotIn("INTEGRATED_A1_A10_REVIEW", refoundation["completed_deliverables"])
        self.assertNotIn("OPERATOR_POST_BLUEPRINT_DECISION", refoundation["completed_deliverables"])
        self.assertTrue(refoundation["runtime_expansion_frozen"])
        self.assertEqual("ADR-0026", validation["decision"])
        self.assertEqual("QUALIFYING_REVIEW_COMPLETE", validation["independent_review_status"])
        self.assertEqual("COMPLETE / H11_PREREGISTERED / EXECUTION_ADMISSION_NEXT", validation["status"])
        self.assertEqual("ADMITTED_FOR_EXPERIMENT_ONLY", validation["bpv1_status"])
        self.assertEqual("BPV1-001-cross-lineage-bounded-accountability-v1", validation["bpv1_plan"]["plan_id"])
        self.assertFalse(validation["bpv1_plan"]["execution_authorized"])
        result = validation["bpv1_execution_result"]
        self.assertEqual("COMPLETE", result["status"])
        self.assertEqual("QUALIFIED", result["qualification_status"])
        self.assertEqual("SUPPORTED_FOR_SCOPE", result["oracle_outcome"])
        # Historical D5/D6/D7/D8 chain remains bound to the residual-planning gate.
        self.assertEqual("RESIDUAL_A10_VALIDATION_PLAN", result["next_gate"])
        self.assertEqual("COMPLETE", result["d6_status"])
        self.assertEqual("COMPLETE", result["d7_status"])
        self.assertEqual("COMPLETE / READ_BACK_VERIFIED", result["d8_status"])
        self.assertEqual("STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL", validation["d7_integrated_rereview"]["architecture_position"])
        self.assertEqual("COMPLETE / READ_BACK_VERIFIED", validation["d8_consolidated_sync"]["status"])
        self.assertTrue(validation["d8_consolidated_sync"]["operator_decision_required"])
        self.assertFalse(validation["d8_consolidated_sync"]["next_gate_authorized_by_d8"])

        # ADR-0027 remains historical authority for admitting RAVP planning only.
        decision = validation["post_d8_operator_decision"]
        self.assertEqual("RESIDUAL_A10_VALIDATION_PLAN", decision["next_gate"])
        self.assertEqual("RESEARCH_PLANNING_ONLY", decision["next_gate_scope"])
        self.assertFalse(decision["experiment_execution_authorized"])

        plan = validation["residual_a10_validation_plan"]
        self.assertEqual("RAVP-001-residual-a10-validation-plan-v1", plan["plan_id"])
        self.assertEqual("COMPLETE / MERGED / NOTION_7_OF_7_READ_BACK_VERIFIED", plan["status"])
        self.assertEqual("A10-H11", plan["selected_family"])
        self.assertEqual("RAVP-H11-LAB-CANON-SEPARATION", plan["selected_family_id"])
        self.assertTrue(plan["family_preregistration_authorized"])
        self.assertTrue(plan["family_preregistration_complete"])
        self.assertEqual("A10_H11_EXECUTION_ADMISSION", plan["next_gate"])
        self.assertEqual("EXECUTION_ADMISSION_ONLY", plan["next_gate_scope"])
        self.assertFalse(plan["experiment_implementation_authorized"])
        self.assertFalse(plan["experiment_execution_authorized"])
        self.assertFalse(plan["composition_federation_is_h11"])

        h11 = plan["h11_preregistration"]
        self.assertEqual("H11-001-c5-lab-canon-separation-v1", h11["plan_id"])
        self.assertEqual("PREREGISTERED / EXECUTION_NOT_AUTHORIZED", h11["status"])
        self.assertEqual("NOT_TESTED", h11["current_a10_outcome"])
        self.assertEqual("INDEPENDENT_SEMANTIC_ORACLE", h11["required_oracle_class"])
        self.assertEqual("NOT_ESTABLISHED / MUST_BE_VERIFIED_AT_EXECUTION_ADMISSION", h11["qualifying_reviewer_reproducer"])
        self.assertFalse(h11["implementation_authorized"])
        self.assertFalse(h11["execution_authorized"])

        self.assertFalse(validation["product_runtime_thaw"])
        self.assertFalse(STATE["status"]["production_authorized"])
        self.assertEqual("BOUNDED_REFERENCE_LABORATORY", STATE["tracks"]["clean_implementation"]["architecture_role"])


if __name__ == "__main__":
    unittest.main()
