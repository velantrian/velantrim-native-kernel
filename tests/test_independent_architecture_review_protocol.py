from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = (ROOT / "docs" / "INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md").read_text(encoding="utf-8")
RU = (ROOT / "docs" / "INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md").read_text(encoding="utf-8")
ADR = (ROOT / "docs" / "adr" / "0026-independent-challenge-before-bounded-cross-lineage-falsification.md").read_text(encoding="utf-8")
RESULT = json.loads((ROOT / "docs" / "reviews" / "IAR-1_RESULT.json").read_text(encoding="utf-8"))
RECONCILIATION = json.loads((ROOT / "docs" / "reviews" / "IAR-1_RECONCILIATION.json").read_text(encoding="utf-8"))
STATE = json.loads((ROOT / "project-state.json").read_text(encoding="utf-8"))


class IndependentArchitectureReviewProtocolTests(unittest.TestCase):
    def test_protocol_identity_and_runtime_boundary_are_bilingual(self) -> None:
        for markdown in (EN, RU):
            self.assertIn("nk-independent-architecture-review/1", markdown)
            self.assertIn("ADR-0026", markdown)
            self.assertIn("FROZEN", markdown)
            self.assertIn("BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION", markdown)

    def test_required_question_headings_are_exactly_q1_through_q12(self) -> None:
        for markdown in (EN, RU):
            headings = re.findall(r"^### Q(\d+) —", markdown, flags=re.MULTILINE)
            self.assertEqual([str(index) for index in range(1, 13)], headings)

    def test_required_input_packet_includes_ai_orientation_surfaces(self) -> None:
        for markdown in (EN, RU):
            self.assertIn("`docs/ai/README.md`", markdown)
            self.assertIn("`docs/ai/CURRENT_STATE.md`", markdown)
            self.assertIn("`docs/ai/KNOWN_RISKS.md`", markdown)

    def test_finding_schema_and_severity_are_explicit(self) -> None:
        for markdown in (EN, RU):
            self.assertIn("IAR-F01", markdown)
            self.assertIn("status: OPEN | RESOLVED", markdown)
            self.assertIn("reconciliation_record:", markdown)
            for severity in ("BLOCKING", "MATERIAL", "MODERATE", "MINOR"):
                self.assertIn(severity, markdown)
            for disposition in ("REMOVE", "WEAKEN", "SPLIT", "CLARIFY", "TEST", "RETAIN"):
                self.assertIn(disposition, markdown)

    def test_unresolved_blocking_finding_cannot_be_carried_into_bpv1(self) -> None:
        for markdown in (EN, RU):
            self.assertIn("bpv1_dependency: BLOCKS | SHOULD_INFORM | NONE", markdown)
            self.assertIn("status: RESOLVED", markdown)
            self.assertIn("bpv1_dependency: BLOCKS", markdown)
        self.assertIn("An unresolved `BLOCKING` finding **always blocks BPV-1**", EN)
        self.assertIn("There is no exception that allows an open `BLOCKING` finding", EN)
        self.assertIn("Неразрешённый `BLOCKING` finding **всегда блокирует BPV-1**", RU)
        self.assertIn("Нет исключения, позволяющего перенести open `BLOCKING` finding", RU)

    def test_review_process_cannot_be_confused_with_a10_outcomes(self) -> None:
        for markdown in (EN, RU):
            for process_outcome in (
                "QUALIFYING_REVIEW_COMPLETE",
                "BLOCKED_NO_QUALIFYING_REVIEWER",
                "INCOMPLETE_REVIEW",
                "REVIEW_INVALIDATED_BY_INDEPENDENCE_FAILURE",
            ):
                self.assertIn(process_outcome, markdown)

    def test_adr_records_option_d_without_runtime_thaw(self) -> None:
        self.assertIn("Option D", ADR)
        self.assertIn("INDEPENDENT_ARCHITECTURE_REVIEW", ADR)
        self.assertIn("BPV-1", ADR)
        self.assertIn("runtime_expansion: FROZEN", ADR)
        self.assertIn("product_runtime_thaw: NO", ADR)
        self.assertIn("automatic_canon_promotion: NO", ADR)
        self.assertIn("automatic_runtime_promotion: NO", ADR)

    def test_iar1_result_binds_reviewed_subject_and_complete_questions(self) -> None:
        self.assertEqual("QUALIFYING_REVIEW_COMPLETE", RESULT["process_outcome"])
        self.assertEqual("2dd51723e30d5f3c5e86268365bf4cf7639b5e9a", RESULT["reviewed_commit"])
        self.assertTrue(RESULT["q1_q12_complete"])
        self.assertEqual(10, RESULT["finding_count"])
        self.assertEqual(7, len(RESULT["blocking_findings"]))
        self.assertEqual(3, len(RESULT["material_findings"]))
        self.assertEqual("FROZEN", RESULT["product_runtime_status"])

    def test_reconciliation_covers_all_review_findings_without_runtime_promotion(self) -> None:
        source_ids = {finding["finding_id"] for finding in RESULT["findings"]}
        reconciled = {finding["finding_id"]: finding for finding in RECONCILIATION["findings"]}
        self.assertEqual(source_ids, set(reconciled))
        self.assertTrue(all(item["status"] == "RESOLVED" for item in reconciled.values()))
        self.assertTrue(all(item["reconciliation_record"].strip() for item in reconciled.values()))
        self.assertEqual([], RECONCILIATION["open_blocking_findings"])
        self.assertEqual([], RECONCILIATION["open_material_findings"])
        self.assertFalse(RECONCILIATION["automatic_canon_promotion"])
        self.assertFalse(RECONCILIATION["automatic_runtime_promotion"])

    def test_historical_reconciliation_gate_and_current_h11_gate_are_separate(self) -> None:
        research = STATE["tracks"]["long_horizon_research"]
        validation = research["post_blueprint_validation"]
        # Historical IAR-1-R1 remains bound to the gate that followed reconciliation.
        self.assertEqual("BPV1_PLAN_AND_PREREGISTRATION", RECONCILIATION["next_gate"])
        self.assertEqual("BLOCKED_PENDING_PREREGISTERED_PLAN", RECONCILIATION["bpv1_status_after_reconciliation"])

        # Current machine truth has advanced through RAVP and H11 preregistration only.
        self.assertEqual("A10_H11_EXECUTION_ADMISSION", research["architecture_refoundation"]["next_content_slice"])
        self.assertEqual("QUALIFYING_REVIEW_COMPLETE", validation["independent_review_status"])
        self.assertEqual("COMPLETE / H11_PREREGISTERED / EXECUTION_ADMISSION_NEXT", validation["status"])
        self.assertEqual("ADMITTED_FOR_EXPERIMENT_ONLY", validation["bpv1_status"])
        self.assertEqual("BPV1-001-cross-lineage-bounded-accountability-v1", validation["bpv1_plan"]["plan_id"])
        self.assertEqual("a538d7f1e28858a88b9ee777ac7d6e05b85943db", validation["bpv1_plan"]["authoritative_plan_merge_sha"])
        self.assertFalse(validation["bpv1_plan"]["execution_authorized"])
        result = validation["bpv1_execution_result"]
        self.assertEqual("COMPLETE", result["status"])
        self.assertEqual("QUALIFIED", result["qualification_status"])
        self.assertEqual("SUPPORTED_FOR_SCOPE", result["oracle_outcome"])
        self.assertEqual("RESIDUAL_A10_VALIDATION_PLAN", result["next_gate"])
        self.assertEqual("COMPLETE", result["d6_status"])
        self.assertEqual("COMPLETE", result["d7_status"])
        self.assertEqual("COMPLETE / READ_BACK_VERIFIED", result["d8_status"])
        self.assertEqual("COMPLETE", validation["d6_hypothesis_classification"]["status"])
        self.assertEqual("COMPLETE", validation["d7_integrated_rereview"]["status"])
        self.assertEqual("COMPLETE / READ_BACK_VERIFIED", validation["d8_consolidated_sync"]["status"])
        self.assertTrue(validation["d8_consolidated_sync"]["operator_decision_required"])
        self.assertFalse(validation["d8_consolidated_sync"]["next_gate_authorized_by_d8"])

        # ADR-0027 stays a historical planning authorization record.
        decision = validation["post_d8_operator_decision"]
        self.assertEqual("RESIDUAL_A10_VALIDATION_PLAN", decision["next_gate"])
        self.assertEqual("RESEARCH_PLANNING_ONLY", decision["next_gate_scope"])
        self.assertFalse(decision["experiment_execution_authorized"])

        plan = validation["residual_a10_validation_plan"]
        self.assertEqual("A10-H11", plan["selected_family"])
        self.assertTrue(plan["family_preregistration_authorized"])
        self.assertTrue(plan["family_preregistration_complete"])
        self.assertEqual("A10_H11_EXECUTION_ADMISSION", plan["next_gate"])
        self.assertEqual("EXECUTION_ADMISSION_ONLY", plan["next_gate_scope"])
        self.assertFalse(plan["experiment_implementation_authorized"])
        self.assertFalse(plan["experiment_execution_authorized"])

        h11 = plan["h11_preregistration"]
        self.assertEqual("H11-001-c5-lab-canon-separation-v1", h11["plan_id"])
        self.assertEqual("NOT_TESTED", h11["current_a10_outcome"])
        self.assertEqual("INDEPENDENT_SEMANTIC_ORACLE", h11["required_oracle_class"])
        self.assertEqual("NOT_ESTABLISHED / MUST_BE_VERIFIED_AT_EXECUTION_ADMISSION", h11["qualifying_reviewer_reproducer"])
        self.assertFalse(h11["implementation_authorized"])
        self.assertFalse(h11["execution_authorized"])

        self.assertFalse(validation["product_runtime_thaw"])
        self.assertFalse(validation["automatic_canon_promotion"])
        self.assertFalse(validation["automatic_runtime_promotion"])


if __name__ == "__main__":
    unittest.main()
