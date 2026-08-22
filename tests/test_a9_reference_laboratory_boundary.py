from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "docs" / "A9_REFERENCE_LABORATORY_BOUNDARY.md"
RU_PATH = ROOT / "docs" / "A9_REFERENCE_LABORATORY_BOUNDARY.ru.md"
STATE_PATH = ROOT / "project-state.json"
REGISTRY_PATH = ROOT / "tools" / "docs" / "bilingual-pairs-v1.json"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "ai-context.yml"

ROLE_LABELS = (
    "ARCHITECTURE_PRESERVING_EVIDENCE",
    "PROFILE_SPECIFIC_REALIZATION",
    "PARTIAL_ARCHITECTURE_COVERAGE",
    "FALSIFICATION_INSTRUMENT",
    "LABORATORY_ONLY_CONSTRAINT",
    "NOT_ARCHITECTURE_EVIDENCE",
)


class A9ReferenceLaboratoryBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.en = EN_PATH.read_text(encoding="utf-8")
        cls.ru = RU_PATH.read_text(encoding="utf-8")
        cls.state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        cls.registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        cls.workflow = WORKFLOW_PATH.read_text(encoding="utf-8")

    def test_documents_model_and_next_slice(self) -> None:
        for markdown in (self.en, self.ru):
            self.assertIn("nk-reference-laboratory-boundary/A9-draft-1", markdown)
            self.assertIn("DRAFTED / PROVISIONAL", markdown)
            self.assertIn("A10_OPEN_QUESTIONS_AND_FALSIFICATION", markdown)
            self.assertIn("FROZEN", markdown)

    def test_classification_vocabulary_is_bilingual(self) -> None:
        for markdown in (self.en, self.ru):
            for label in ROLE_LABELS:
                self.assertIn(label, markdown)

    def test_all_laboratory_phases_are_explicitly_classified(self) -> None:
        headings = ("## 5. P1", "## 6. P2", "## 7. P3", "## 8. P4", "## 9. P5", "## 10. C4", "## 11. C5")
        for markdown in (self.en, self.ru):
            for heading in headings:
                self.assertIn(heading, markdown)

    def test_storage_profile_evidence_is_bounded(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in ("PostgreSQL ↔ SQLite C3", "independent-language equivalence", "independent-computation-model equivalence", "arbitrary-substrate portability proof", "Python"):
                self.assertIn(literal, markdown)
        self.assertIn("shared", self.en)
        self.assertTrue("разделяют" in self.ru or "общей language lineage" in self.ru)

    def test_mechanisms_do_not_capture_canon(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in ("profile-specific", "Event sourcing", "reducer", "PostgreSQL", "SQLite", "SHA-256", "global"):
                self.assertIn(literal, markdown)
        self.assertIn("existing mechanism", self.en)
        self.assertIn("architecture requirement", self.en)
        self.assertIn("существующий механизм", self.ru)
        self.assertIn("архитектурное требование", self.ru)

    def test_preservation_rule_and_overclaim_cases_exist(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in ("reproducibility", "silent Canon promotion", "profile-specific", "C5", "production security", "independent custody", "assertion arithmetic"):
                self.assertIn(literal, markdown)
        self.assertIn("preserve reproducibility", self.en)
        self.assertIn("сохранить reproducibility", self.ru)

    def test_operator_boundaries_are_unchanged(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in ("Issue #18", "Issue #74 / ADR-0024", "ADR-0003", "Track H", "reducer-v2"):
                self.assertIn(literal, markdown)

    def test_project_state_preserves_a9_through_blocked_h11_admission(self) -> None:
        research = self.state["tracks"]["long_horizon_research"]
        refoundation = research["architecture_refoundation"]
        validation = research["post_blueprint_validation"]
        self.assertIn("A9_REFERENCE_LABORATORY_BOUNDARY", refoundation["completed_deliverables"])
        self.assertIn("A10_OPEN_QUESTIONS_AND_FALSIFICATION", refoundation["completed_deliverables"])
        self.assertEqual("A10_H11_EXECUTION_ADMISSION", refoundation["next_content_slice"])
        self.assertEqual("ADR-0026", validation["decision"])
        self.assertEqual("QUALIFYING_REVIEW_COMPLETE", validation["independent_review_status"])
        self.assertEqual("COMPLETE / H11_EXECUTION_ADMISSION_BLOCKED / NO_AUTOMATIC_PROMOTION", validation["status"])
        self.assertEqual("ADMITTED_FOR_EXPERIMENT_ONLY", validation["bpv1_status"])
        self.assertEqual("BPV1-001-cross-lineage-bounded-accountability-v1", validation["bpv1_plan"]["plan_id"])
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

        plan = validation["residual_a10_validation_plan"]
        self.assertEqual("RAVP-001-residual-a10-validation-plan-v1", plan["plan_id"])
        self.assertEqual("COMPLETE / MERGED / NOTION_7_OF_7_READ_BACK_VERIFIED", plan["status"])
        self.assertEqual("A10_H11_EXECUTION_ADMISSION", plan["next_gate"])
        self.assertEqual("EXECUTION_ADMISSION_ONLY", plan["next_gate_scope"])
        self.assertEqual("BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER", plan["execution_admission_state"])
        self.assertEqual("IMPLEMENT_ADR0028_POSITIVE_QUALIFICATION_PATH_THEN_ESTABLISH_GENUINELY_EXTERNAL_CANDIDATE", plan["next_dependency"])
        self.assertEqual("A10-H11", plan["selected_family"])
        self.assertEqual("RAVP-H11-LAB-CANON-SEPARATION", plan["selected_family_id"])
        self.assertTrue(plan["family_preregistration_authorized"])
        self.assertTrue(plan["family_preregistration_complete"])
        h11 = plan["h11_preregistration"]
        self.assertEqual("H11-001-c5-lab-canon-separation-v1", h11["plan_id"])
        self.assertEqual("native-kernel/c5/2026-08-08-adr0023", h11["frozen_laboratory_bundle"])
        self.assertEqual("INDEPENDENT_SEMANTIC_ORACLE", h11["required_oracle_class"])
        self.assertEqual("NOT_ESTABLISHED / MUST_BE_VERIFIED_AT_EXECUTION_ADMISSION", h11["qualifying_reviewer_reproducer"])
        self.assertEqual("NOT_TESTED", h11["current_a10_outcome"])
        self.assertFalse(h11["implementation_authorized"])
        self.assertFalse(h11["execution_authorized"])

        admission = plan["h11_execution_admission"]
        self.assertEqual("BLOCKED", admission["status"])
        self.assertEqual("f7d13fce0104a4c2ce67589e954b09365a82f36f", admission["admission_package_merge_sha"])
        self.assertEqual("BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER", admission["admission_result"])
        self.assertEqual("NOT_ESTABLISHED", admission["qualifying_reviewer_reproducer"])
        self.assertEqual("NOT_TESTED", admission["h11_outcome"])
        self.assertFalse(admission["implementation_authorized"])
        self.assertFalse(admission["execution_authorized"])
        self.assertFalse(admission["dependency_graph_execution_authorized"])
        self.assertFalse(admission["semantic_adjudication_authorized"])
        self.assertFalse(plan["experiment_implementation_authorized"])
        self.assertFalse(plan["experiment_execution_authorized"])
        self.assertFalse(plan["composition_federation_is_h11"])

        self.assertTrue(refoundation["runtime_expansion_frozen"])
        self.assertFalse(validation["product_runtime_thaw"])
        self.assertEqual("BOUNDED_REFERENCE_LABORATORY", self.state["tracks"]["clean_implementation"]["architecture_role"])
        self.assertFalse(self.state["status"]["production_authorized"])
        self.assertEqual({"supported": 45, "partial": 10, "unsupported": 17, "failed": 0, "total": 72}, self.state["assertion_map"])
        self.assertEqual((0, 0, 8, 0), tuple(self.state["nk_epi"][key] for key in ("supported", "partial", "unsupported", "failed")))

    def test_registry_and_workflow_include_a9(self) -> None:
        serialized = json.dumps(self.registry, ensure_ascii=False)
        self.assertIn("A9_REFERENCE_LABORATORY_BOUNDARY", serialized)
        self.assertIn("nk-reference-laboratory-boundary/A9-draft-1", serialized)
        self.assertIn("tests/test_a9_reference_laboratory_boundary.py", self.workflow)


if __name__ == "__main__":
    unittest.main()
