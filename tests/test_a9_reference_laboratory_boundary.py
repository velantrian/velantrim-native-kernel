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

    def test_project_state_preserves_a9_through_d5_r1_qualification(self) -> None:
        research = self.state["tracks"]["long_horizon_research"]
        refoundation = research["architecture_refoundation"]
        validation = research["post_blueprint_validation"]
        self.assertIn("A9_REFERENCE_LABORATORY_BOUNDARY", refoundation["completed_deliverables"])
        self.assertIn("A10_OPEN_QUESTIONS_AND_FALSIFICATION", refoundation["completed_deliverables"])
        self.assertEqual("D6_A10_HYPOTHESIS_CLASSIFICATION", refoundation["next_content_slice"])
        self.assertEqual("ADR-0026", validation["decision"])
        self.assertEqual("QUALIFYING_REVIEW_COMPLETE", validation["independent_review_status"])
        self.assertEqual(
            "AUTHORIZED / REVIEW_COMPLETE / RECONCILIATION_COMPLETE / BPV1_PLAN_PREREGISTERED / EXECUTION_ADMITTED_FOR_EXPERIMENT_ONLY / D5_COMPLETE / D5_R1_QUALIFIED",
            validation["status"],
        )
        self.assertEqual("ADMITTED_FOR_EXPERIMENT_ONLY", validation["bpv1_status"])
        self.assertEqual("BPV1-001-cross-lineage-bounded-accountability-v1", validation["bpv1_plan"]["plan_id"])
        self.assertFalse(validation["bpv1_plan"]["execution_authorized"])
        result = validation["bpv1_execution_result"]
        self.assertEqual("COMPLETE", result["status"])
        self.assertEqual("QUALIFIED", result["qualification_status"])
        self.assertEqual("SUPPORTED_FOR_SCOPE", result["oracle_outcome"])
        self.assertEqual("D6_A10_HYPOTHESIS_CLASSIFICATION", result["next_gate"])
        self.assertEqual("NOT_STARTED", result["d6_status"])
        self.assertTrue(refoundation["runtime_expansion_frozen"])
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
