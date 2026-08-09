from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "docs" / "A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md"
RU_PATH = ROOT / "docs" / "A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md"
VALIDATOR_PATH = ROOT / "tools" / "docs" / "validate_bilingual_parity.py"

SPEC = importlib.util.spec_from_file_location("validate_bilingual_parity", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

TRANSITIONS = (
    "ENCOUNTER",
    "REGISTER",
    "IDENTIFY_OR_DISTINGUISH",
    "BIND_SCOPE_AND_ORIGIN",
    "INTERPRET_AND_CLASSIFY_ROLE",
    "ASSESS_EPISTEMIC_POSITION",
    "DECIDE_DISPOSITION",
    "RELATE",
    "DETECT_TENSION",
    "REVISE_OR_SUPERSEDE",
    "DERIVE_BOUNDED_VIEW",
    "SELECT_FOR_USE",
    "ACCOUNT",
)

FACETS = ("B", "R", "I", "C", "P", "E", "L", "U", "G", "V", "D", "A", "O")

OUTCOMES = (
    "APPLIED",
    "NO_CHANGE",
    "QUARANTINED",
    "REJECTED",
    "PARTIAL",
    "UNKNOWN",
    "UNSUPPORTED",
    "FAILED",
)

NON_EQUIVALENCES = (
    "abstract machine ≠ runtime implementation",
    "logical configuration K ≠ complete world State",
    "transition ≠ Event envelope",
    "transition relation ≠ reducer",
    "history visibility ≠ mandatory Event sourcing",
    "Record registration ≠ admission",
    "admission ≠ truth",
    "available ≠ Knowledge",
    "selected/relevant ≠ epistemically valid",
    "deterministic output ≠ true output",
    "reproducible ≠ physically identical",
    "Relation position ≠ represented relation reality",
    "conflict detection ≠ conflict resolution",
    "revision ≠ silent overwrite",
    "Supersession ≠ deletion",
    "Receipt ≠ proof of correctness",
    "unknown/unsupported/failed ≠ false",
    "Authority in one role ≠ authority in every role",
    "profile conformance ≠ production authorization",
)

EN_MARKERS = (
    "**Purpose:**",
    "**Preconditions:**",
    "**Postconditions:**",
    "**Allowed outcomes:**",
    "**Failure/counterexample:**",
)

RU_MARKERS = (
    "**Назначение:**",
    "**Preconditions:**",
    "**Postconditions:**",
    "**Allowed outcomes:**",
    "**Failure/counterexample:**",
)


def _transition_section(markdown: str, name: str) -> str:
    match = re.search(
        rf"^###\s+5\.\d+\s+`{re.escape(name)}`\s*$\n(?P<body>.*?)(?=^###\s+5\.\d+\s+|^##\s+|\Z)",
        markdown,
        flags=re.MULTILINE | re.DOTALL,
    )
    if match is None:
        raise AssertionError(f"missing transition section: {name}")
    return match.group("body")


class A3AbstractMachineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.en = EN_PATH.read_text(encoding="utf-8")
        cls.ru = RU_PATH.read_text(encoding="utf-8")

    def test_language_selectors_and_heading_parity(self) -> None:
        for literal in (
            "(./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md)",
            "(./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md)",
        ):
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)
        self.assertEqual(validator.heading_levels(self.en), validator.heading_levels(self.ru))
        self.assertEqual(1, validator.heading_levels(self.en).count(1))
        self.assertEqual(1, validator.heading_levels(self.ru).count(1))

    def test_configuration_notation_and_facets_are_bilingual(self) -> None:
        notation = "K = ⟨B, R, I, C, P, E, L, U, G, V, D, A, O⟩"
        transition = "τ : ⟨K, request, declared context, declared authority/policy⟩"
        for markdown in (self.en, self.ru):
            self.assertIn(notation, markdown)
            self.assertIn(transition, markdown)
            for facet in FACETS:
                self.assertRegex(markdown, rf"\| `{facet}` \|")

    def test_each_transition_has_required_obligations(self) -> None:
        for transition in TRANSITIONS:
            with self.subTest(language="en", transition=transition):
                section = _transition_section(self.en, transition)
                for marker in EN_MARKERS:
                    self.assertIn(marker, section)
            with self.subTest(language="ru", transition=transition):
                section = _transition_section(self.ru, transition)
                for marker in RU_MARKERS:
                    self.assertIn(marker, section)

    def test_outcome_inventory_is_bilingual(self) -> None:
        for outcome in OUTCOMES:
            with self.subTest(outcome=outcome):
                self.assertIn(f"`{outcome}`", self.en)
                self.assertIn(f"`{outcome}`", self.ru)

    def test_required_non_equivalences_are_bilingual_and_exact(self) -> None:
        for distinction in NON_EQUIVALENCES:
            with self.subTest(distinction=distinction):
                self.assertIn(distinction, self.en)
                self.assertIn(distinction, self.ru)

    def test_three_contrasting_substrate_mappings_exist(self) -> None:
        for marker in (
            "Manual archival",
            "Adaptive analog",
            "Conventional digital Event-sourced laboratory",
        ):
            self.assertIn(marker, self.en)
        for marker in (
            "Manual archival",
            "Adaptive analog",
            "Conventional digital Event-sourced laboratory",
        ):
            self.assertIn(marker, self.ru)

    def test_status_preserves_freeze_and_advances_to_a4(self) -> None:
        required = (
            "deliverable: A3_ABSTRACT_NATIVE_KERNEL_MACHINE",
            "state: DRAFTED",
            "classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL",
            "machine_form: SCOPED OBLIGATION-AND-TRANSITION SYSTEM",
            "next_content_slice: A4_SEMANTIC_LAWS_AND_INVARIANTS",
            "runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED",
            "Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED",
        )
        for literal in required:
            with self.subTest(literal=literal):
                self.assertIn(literal, self.en)
                self.assertIn(literal, self.ru)

    def test_non_goals_reject_runtime_capture(self) -> None:
        en_non_goals = self.en.split("## 18. Non-goals", 1)[1]
        ru_non_goals = self.ru.split("## 18. Non-goals", 1)[1]
        required = (
            "reducer v2",
            "Event sourcing",
            "global total order",
            "Issue #18",
            "ADR-0024",
            "A4",
            "A5",
            "A6",
            "A7",
            "A8",
            "runtime",
            "LLM",
            "embeddings",
            "SQL",
            "JSON",
            "Python",
        )
        for literal in required:
            with self.subTest(language="en", literal=literal):
                self.assertIn(literal, en_non_goals)
            with self.subTest(language="ru", literal=literal):
                self.assertIn(literal, ru_non_goals)


if __name__ == "__main__":
    unittest.main()
