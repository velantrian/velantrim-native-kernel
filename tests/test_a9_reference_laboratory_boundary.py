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
        for markdown in (self.en, self.ru):
            for phase in ("P1", "P2", "P3", "P4", "P5", "C4", "C5"):
                self.assertIn(f"## {5 + (('P1','P2','P3','P4','P5','C4','C5').index(phase))}. {phase}", markdown)

    def test_storage_profile_evidence_is_bounded(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in (
                "PostgreSQL ↔ SQLite C3",
                "independent-language equivalence",
                "independent-computation-model equivalence",
                "arbitrary-substrate portability proof",
                "shared",
                "Python",
            ):
                self.assertIn(literal, markdown)

    def test_mechanisms_do_not_capture_canon(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in (
                "existing mechanism",
                "architecture requirement",
                "profile-specific",
                "Event sourcing",
                "reducer",
                "PostgreSQL",
                "SQLite",
                "SHA-256",
                "global",
            ):
                self.assertIn(literal, markdown)

    def test_preservation_rule_and_overclaim_cases_exist(self) -> None:
        for markdown in (self.en, self.ru):
            self.assertIn("preserve reproducibility", markdown)
            self.assertIn("prevent silent Canon promotion", markdown)
            self.assertIn("profile-specific", markdown)
            self.assertIn("C5", markdown)
            self.assertIn("production security", markdown)
            self.assertIn("independent custody", markdown)
            self.assertIn("assertion arithmetic", markdown)

    def test_operator_boundaries_are_unchanged(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in (
                "Issue #18",
                "Issue #74 / ADR-0024",
                "ADR-0003",
                "Track H",
                "reducer-v2",
            ):
                self.assertIn(literal, markdown)

    def test_project_state_advances_only_to_a10(self) -> None:
        refoundation = self.state["tracks"]["long_horizon_research"]["architecture_refoundation"]
        self.assertEqual("A10_OPEN_QUESTIONS_AND_FALSIFICATION", refoundation["next_content_slice"])
        self.assertEqual(
            [
                "A1_KERNEL_PURPOSE_AND_NON_GOALS",
                "A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY",
                "A3_ABSTRACT_NATIVE_KERNEL_MACHINE",
                "A4_SEMANTIC_LAWS_AND_INVARIANTS",
                "A5_IDENTITY_TIME_AND_CHANGE",
                "A6_KNOWLEDGE_LIFECYCLE",
                "A7_CONFLICT_UNCERTAINTY_AND_REVISION",
                "A8_SUBSTRATE_INDEPENDENCE_CONTRACT",
                "A9_REFERENCE_LABORATORY_BOUNDARY",
            ],
            refoundation["completed_deliverables"],
        )
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
