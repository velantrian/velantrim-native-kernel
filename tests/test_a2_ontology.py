from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "docs" / "A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md"
RU_PATH = ROOT / "docs" / "A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md"
VALIDATOR_PATH = ROOT / "tools" / "docs" / "validate_bilingual_parity.py"

SPEC = importlib.util.spec_from_file_location("validate_bilingual_parity", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

CONCEPTS = (
    "Signal",
    "Observation",
    "Record",
    "Proposition",
    "Claim",
    "Interpretation",
    "Hypothesis",
    "Belief",
    "Knowledge",
    "Evidence",
    "Uncertainty",
    "Source",
    "Provenance",
    "Context",
    "Authority",
    "Memory",
    "State",
    "Change",
    "Event",
    "Revision",
    "Supersession",
    "Relation",
    "Conflict",
    "Contradiction",
    "Receipt",
)

CLASSIFICATIONS = (
    "CANDIDATE_PRIMITIVE",
    "DERIVED_CONCEPT",
    "OPEN_QUESTION",
)

NON_EQUIVALENCES = (
    "Observation ≠ Claim",
    "Claim ≠ Truth",
    "Evidence ≠ Source",
    "Repetition ≠ Evidence",
    "Belief ≠ Knowledge",
    "Memory ≠ merely a stored Record",
    "retrieval relevance ≠ epistemic validity",
    "Conflict ≠ necessarily Contradiction",
    "Unknown ≠ False",
    "Event usage in P1–C5 ≠ Event as universal primitive",
    "State ≠ necessarily reducer output",
    "Knowledge ≠ LLM / embeddings / SQL / JSON / specific processor",
)

EN_OBLIGATIONS = (
    "**Classification:**",
    "**Working definition:**",
    "**It is not:**",
    "**Neighbour distinction:**",
    "**Allowed relations:**",
    "**Identity and lifecycle note:**",
    "**Minimum semantic obligations:**",
    "**Unresolved questions:**",
    "**Falsification/counterexample:**",
)

RU_OBLIGATIONS = (
    "**Классификация:**",
    "**Рабочее определение:**",
    "**Чем не является:**",
    "**Отличие от соседних понятий:**",
    "**Допустимые связи:**",
    "**Identity и lifecycle:**",
    "**Минимальные semantic obligations:**",
    "**Открытые вопросы:**",
    "**Falsification/counterexample:**",
)


def _section(markdown: str, concept: str) -> str:
    match = re.search(
        rf"^###\s+\d+\.\d+\s+{re.escape(concept)}\s*$\n(?P<body>.*?)(?=^###\s+\d+\.\d+\s+|^##\s+|\Z)",
        markdown,
        flags=re.MULTILINE | re.DOTALL,
    )
    if match is None:
        raise AssertionError(f"missing concept section: {concept}")
    return match.group("body")


class A2OntologyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.en = EN_PATH.read_text(encoding="utf-8")
        cls.ru = RU_PATH.read_text(encoding="utf-8")

    def test_language_selectors_and_heading_parity(self) -> None:
        for literal in (
            "(./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md)",
            "(./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md)",
        ):
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)
        self.assertEqual(validator.heading_levels(self.en), validator.heading_levels(self.ru))
        self.assertEqual(1, validator.heading_levels(self.en).count(1))
        self.assertEqual(1, validator.heading_levels(self.ru).count(1))

    def test_each_concept_has_required_semantic_obligations(self) -> None:
        for concept in CONCEPTS:
            with self.subTest(language="en", concept=concept):
                section = _section(self.en, concept)
                for marker in EN_OBLIGATIONS:
                    self.assertIn(marker, section)
                self.assertTrue(any(f"`{value}`" in section for value in CLASSIFICATIONS))

            with self.subTest(language="ru", concept=concept):
                section = _section(self.ru, concept)
                for marker in RU_OBLIGATIONS:
                    self.assertIn(marker, section)
                self.assertTrue(any(f"`{value}`" in section for value in CLASSIFICATIONS))

    def test_required_non_equivalences_are_bilingual_and_exact(self) -> None:
        for distinction in NON_EQUIVALENCES:
            with self.subTest(distinction=distinction):
                self.assertIn(distinction, self.en)
                self.assertIn(distinction, self.ru)

    def test_event_state_and_memory_remain_open_questions(self) -> None:
        for concept in ("Memory", "State", "Event"):
            with self.subTest(language="en", concept=concept):
                self.assertIn("`OPEN_QUESTION`", _section(self.en, concept))
            with self.subTest(language="ru", concept=concept):
                self.assertIn("`OPEN_QUESTION`", _section(self.ru, concept))

    def test_a2_does_not_authorize_runtime_or_canon_promotion(self) -> None:
        required = (
            "state: DRAFTED",
            "classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL",
            "next_content_slice: A3_ABSTRACT_NATIVE_KERNEL_MACHINE",
            "runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED",
            "Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED",
        )
        for literal in required:
            with self.subTest(language="en", literal=literal):
                self.assertIn(literal, self.en)
            with self.subTest(language="ru", literal=literal):
                self.assertIn(literal, self.ru)

    def test_non_goals_reject_implementation_capture(self) -> None:
        en_non_goals = self.en.split("## 17. Non-goals", 1)[1]
        ru_non_goals = self.ru.split("## 17. Non-goals", 1)[1]
        required = (
            "reducer v2",
            "Event sourcing",
            "Titan, Crystal, Mentaury",
            "LLM",
            "embedding",
            "runtime",
            "Issue #18",
            "ADR-0024",
            "A3",
        )
        for literal in required:
            with self.subTest(language="en", literal=literal):
                self.assertIn(literal, en_non_goals)
            with self.subTest(language="ru", literal=literal):
                self.assertIn(literal, ru_non_goals)


if __name__ == "__main__":
    unittest.main()
