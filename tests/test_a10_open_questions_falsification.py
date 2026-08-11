from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "docs" / "A10_OPEN_QUESTIONS_AND_FALSIFICATION.md"
RU_PATH = ROOT / "docs" / "A10_OPEN_QUESTIONS_AND_FALSIFICATION.ru.md"
STATE_PATH = ROOT / "project-state.json"
REGISTRY_PATH = ROOT / "tools" / "docs" / "bilingual-pairs-v1.json"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "ai-context.yml"

OUTCOMES = ("SUPPORTED_FOR_SCOPE", "WEAKENED", "REFUTED", "INDETERMINATE", "NOT_TESTED")


class A10OpenQuestionsFalsificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.en = EN_PATH.read_text(encoding="utf-8")
        cls.ru = RU_PATH.read_text(encoding="utf-8")
        cls.state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        cls.registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        cls.workflow = WORKFLOW_PATH.read_text(encoding="utf-8")

    def test_documents_preserve_a10_first_draft_identity(self) -> None:
        for markdown in (self.en, self.ru):
            self.assertIn("nk-open-questions-falsification/A10-draft-1", markdown)
            self.assertIn("DRAFTED / PROVISIONAL", markdown)
            self.assertIn("INTEGRATED_A1_A10_REVIEW", markdown)
            self.assertIn("FROZEN", markdown)

    def test_falsification_outcomes_are_bilingual(self) -> None:
        for markdown in (self.en, self.ru):
            for outcome in OUTCOMES:
                self.assertIn(outcome, markdown)
            self.assertIn("NOT_TESTED ≠ SUPPORTED", markdown)

    def test_major_hypotheses_have_falsifiers(self) -> None:
        for markdown in (self.en, self.ru):
            for index in range(1, 13):
                self.assertIn(f"A10-H{index:02d}", markdown)
            self.assertIn("independent-language", markdown)
            self.assertIn("analog", markdown.lower())
            self.assertIn("neuromorphic", markdown.lower())
            self.assertIn("probabilistic", markdown.lower())

    def test_open_question_registry_is_explicit(self) -> None:
        for markdown in (self.en, self.ru):
            for index in range(1, 19):
                self.assertIn(f"A10-Q{index:02d}", markdown)
            for literal in ("forgetting", "physical deletion", "global sequence", "decentralized", "quantum", "Evidence independence"):
                self.assertIn(literal.lower(), markdown.lower())

    def test_overclaim_falsifiers_and_stop_conditions_exist(self) -> None:
        for markdown in (self.en, self.ru):
            self.assertIn("Universal portability", markdown)
            self.assertIn("Semantic equivalence", markdown)
            self.assertIn("C5", markdown)
            self.assertIn("Stop conditions", markdown)
            self.assertIn("possible failure condition", markdown)
            self.assertIn("runtime", markdown)

    def test_thought_experiments_cover_distinct_substrate_classes(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in ("Eventless state-transition archive", "Distributed neuromorphic memory", "Lossy bounded-memory agent", "Probabilistic realization", "Independent-language digital profile"):
                self.assertIn(literal, markdown)

    def test_operator_and_runtime_boundaries_are_preserved(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in ("Issue #18", "Issue #74 / ADR-0024", "ADR-0003", "Track H", "reducer-v2"):
                self.assertIn(literal, markdown)
            self.assertIn("45/10/17/0", markdown)
            self.assertIn("0/0/8/0", markdown)

    def test_machine_state_preserves_a10_and_advances_to_execution_admission(self) -> None:
        research = self.state["tracks"]["long_horizon_research"]
        refoundation = research["architecture_refoundation"]
        validation = research["post_blueprint_validation"]
        expected = [
            "A1_KERNEL_PURPOSE_AND_NON_GOALS",
            "A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY",
            "A3_ABSTRACT_NATIVE_KERNEL_MACHINE",
            "A4_SEMANTIC_LAWS_AND_INVARIANTS",
            "A5_IDENTITY_TIME_AND_CHANGE",
            "A6_KNOWLEDGE_LIFECYCLE",
            "A7_CONFLICT_UNCERTAINTY_AND_REVISION",
            "A8_SUBSTRATE_INDEPENDENCE_CONTRACT",
            "A9_REFERENCE_LABORATORY_BOUNDARY",
            "A10_OPEN_QUESTIONS_AND_FALSIFICATION",
        ]
        self.assertEqual(expected, refoundation["completed_deliverables"])
        self.assertEqual("BPV1_EXECUTION_ADMISSION", refoundation["next_content_slice"])
        self.assertEqual("ADR-0026", validation["decision"])
        self.assertEqual("QUALIFYING_REVIEW_COMPLETE", validation["independent_review_status"])
        self.assertEqual("AUTHORIZED / REVIEW_COMPLETE / RECONCILIATION_COMPLETE / BPV1_PLAN_PREREGISTERED / EXECUTION_ADMISSION_NEXT", validation["status"])
        self.assertEqual("BLOCKED_PENDING_EXECUTION_ADMISSION", validation["bpv1_status"])
        self.assertEqual("a538d7f1e28858a88b9ee777ac7d6e05b85943db", validation["bpv1_plan"]["authoritative_plan_merge_sha"])
        self.assertFalse(validation["bpv1_plan"]["execution_authorized"])
        self.assertTrue(refoundation["runtime_expansion_frozen"])
        self.assertEqual("BOUNDED_REFERENCE_LABORATORY", self.state["tracks"]["clean_implementation"]["architecture_role"])
        self.assertFalse(self.state["status"]["production_authorized"])
        self.assertEqual({"supported": 45, "partial": 10, "unsupported": 17, "failed": 0, "total": 72}, self.state["assertion_map"])
        self.assertEqual((0, 0, 8, 0), tuple(self.state["nk_epi"][key] for key in ("supported", "partial", "unsupported", "failed")))

    def test_registry_and_workflow_include_a10(self) -> None:
        serialized = json.dumps(self.registry, ensure_ascii=False)
        self.assertIn("A10_OPEN_QUESTIONS_AND_FALSIFICATION", serialized)
        self.assertIn("nk-open-questions-falsification/A10-draft-1", serialized)
        self.assertIn("tests/test_a10_open_questions_falsification.py", self.workflow)


if __name__ == "__main__":
    unittest.main()
