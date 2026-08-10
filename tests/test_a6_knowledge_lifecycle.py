from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "docs" / "A6_KNOWLEDGE_LIFECYCLE.md"
RU_PATH = ROOT / "docs" / "A6_KNOWLEDGE_LIFECYCLE.ru.md"
VALIDATOR_PATH = ROOT / "tools" / "docs" / "validate_bilingual_parity.py"

SPEC = importlib.util.spec_from_file_location("validate_bilingual_parity", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

LIFECYCLE_PHASES = (
    "ENCOUNTERED",
    "RETAINED",
    "POSITIONED",
    "EPISTEMICALLY_WEIGHED",
    "RELATIONALLY_INTEGRATED",
    "IN_TENSION",
    "REVISED_OR_SUPERSEDED",
    "DISPOSED",
    "ACCOUNTED",
)

CLOSURE_KINDS = (
    "LOGICALLY_ERASED",
    "PHYSICALLY_OR_CRYPTOGRAPHICALLY_ERASED",
    "FORGOTTEN_OR_LOST",
)

TRANSITION_OUTCOMES = (
    "APPLIED",
    "NO_CHANGE",
    "QUARANTINED",
    "REJECTED",
    "PARTIAL",
    "UNKNOWN",
    "UNSUPPORTED",
    "FAILED",
)


def _table_first_column(markdown: str, section_heading: str) -> tuple[str, ...]:
    section = markdown.split(section_heading, 1)[1]
    section = section.split("\n## ", 1)[0]
    values: list[str] = []
    for line in section.splitlines():
        match = re.match(r"^\| `([^`]+)` \|", line)
        if match:
            values.append(match.group(1))
    return tuple(values)


class A6KnowledgeLifecycleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.en = EN_PATH.read_text(encoding="utf-8")
        cls.ru = RU_PATH.read_text(encoding="utf-8")

    def test_language_selectors_and_heading_parity(self) -> None:
        for literal in (
            "(./A6_KNOWLEDGE_LIFECYCLE.md)",
            "(./A6_KNOWLEDGE_LIFECYCLE.ru.md)",
        ):
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)
        self.assertEqual(validator.heading_levels(self.en), validator.heading_levels(self.ru))
        self.assertEqual(1, validator.heading_levels(self.en).count(1))
        self.assertEqual(1, validator.heading_levels(self.ru).count(1))

    def test_model_identity_status_and_next_slice_are_bilingual(self) -> None:
        required = (
            "model_id: nk-knowledge-lifecycle/A6-draft-1",
            "state: DRAFTED",
            "classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL",
            "next_content_slice: A7_CONFLICT_UNCERTAINTY_AND_REVISION",
            "runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED",
            "Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED",
        )
        for literal in required:
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)

    def test_exact_lifecycle_phase_inventory_is_bilingual(self) -> None:
        self.assertEqual(
            LIFECYCLE_PHASES,
            _table_first_column(self.en, "## 3. Lifecycle phases"),
        )
        self.assertEqual(
            LIFECYCLE_PHASES,
            _table_first_column(self.ru, "## 3. Lifecycle phases"),
        )

    def test_phase_referencing_families_are_explicit(self) -> None:
        for markdown in (self.en, self.ru):
            self.assertIn("DERIVE_BOUNDED_VIEW", markdown)
            self.assertIn("SELECT_FOR_USE", markdown)
            self.assertIn("phase-referencing", markdown)

    def test_transition_relation_and_outcomes_are_explicit(self) -> None:
        for markdown in (self.en, self.ru):
            self.assertIn("LIFECYCLE_TRANSITION(", markdown)
            self.assertIn("temporal_binding", markdown)
            self.assertIn("identity_effect", markdown)
            for outcome in TRANSITION_OUTCOMES:
                self.assertIn(outcome, markdown)

    def test_non_linearity_keywords_are_present(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in ("Looping", "Branching", "Concurrency", "Simultaneity across identity kinds"):
                self.assertIn(literal, markdown)

    def test_lifecycle_order_non_equivalences_are_explicit(self) -> None:
        for markdown in (self.en, self.ru):
            self.assertIn("LIFECYCLE_TRANSITION_ORDER", markdown)
            self.assertIn("OCCURRENCE_ORDER", markdown)
            self.assertIn("CAUSAL_DEPENDENCY_ORDER", markdown)

    def test_exact_closure_kind_inventory_is_bilingual(self) -> None:
        self.assertEqual(
            CLOSURE_KINDS,
            _table_first_column(self.en, "## 7. Disposition and closure kinds"),
        )
        self.assertEqual(
            CLOSURE_KINDS,
            _table_first_column(self.ru, "## 7. Disposition and closure kinds"),
        )

    def test_existing_contracts_are_reconciled_without_silent_supersession(self) -> None:
        shared = (
            "ADMIT",
            "LINK",
            "UTILIZED",
            "SUPERSEDED",
            "ERASED",
            "nk-p1-reducer/1",
            "Issue #74 / ADR-0024",
            "Issue #16",
            "global_seq",
            "stream_seq",
        )
        for markdown in (self.en, self.ru):
            for literal in shared:
                self.assertIn(literal, markdown)

    def test_three_contrasting_substrate_mappings_exist(self) -> None:
        markers = (
            "Manual archival and review process",
            "Adaptive analog or neuromorphic substrate",
            "Conventional digital Event-sourced laboratory",
        )
        for marker in markers:
            self.assertIn(marker, self.en)
            self.assertIn(marker, self.ru)

    def test_a6_defers_later_blueprint_and_runtime_work(self) -> None:
        for markdown in (self.en, self.ru):
            deferred = markdown.split("## 13.", 1)[1]
            for literal in (
                "A7",
                "A8",
                "A9",
                "A10",
                "Issue #14",
                "Issue #15",
                "Issue #16",
                "Issue #74 / ADR-0024",
                "Issue #18",
                "Track H",
                "runtime implementation",
                "new Event vocabulary",
                "new databases",
                "LLM/vector adapters",
                "production authorization",
            ):
                self.assertIn(literal, deferred)


if __name__ == "__main__":
    unittest.main()
