from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "docs" / "A5_IDENTITY_TIME_AND_CHANGE.md"
RU_PATH = ROOT / "docs" / "A5_IDENTITY_TIME_AND_CHANGE.ru.md"
VALIDATOR_PATH = ROOT / "tools" / "docs" / "validate_bilingual_parity.py"

SPEC = importlib.util.spec_from_file_location("validate_bilingual_parity", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

IDENTITY_KINDS = (
    "REFERENT_IDENTITY",
    "SEMANTIC_CONTENT_IDENTITY",
    "CLAIM_POSITION_IDENTITY",
    "RECORD_IDENTITY",
    "LINEAGE_CONTINUITY_IDENTITY",
    "OCCURRENCE_IDENTITY",
    "SUBSTRATE_LOCAL_IDENTITY",
)

IDENTITY_OUTCOMES = (
    "SAME",
    "DISTINCT",
    "CONTINUATION_OF",
    "VERSION_OF",
    "ALIAS_OF",
    "MIGRATED_FROM",
    "UNRESOLVED",
)

TEMPORAL_DIMENSIONS = (
    "OCCURRENCE_TIME",
    "VALID_TIME",
    "OBSERVATION_TIME",
    "ASSERTION_TIME",
    "RECORD_TIME",
    "DECISION_TIME",
    "EFFECTIVE_TIME",
    "WRITE_COMMIT_TIME",
)

ORDER_RELATIONS = (
    "OCCURRENCE_ORDER",
    "OBSERVATION_ORDER",
    "CAUSAL_DEPENDENCY_ORDER",
    "LINEAGE_ORDER",
    "AUTHORITY_DECISION_ORDER",
    "LOCAL_WRITE_COMMIT_ORDER",
    "MIGRATION_SYNCHRONIZATION_ORDER",
    "CONCURRENT / INCOMPARABLE / UNKNOWN_ORDER",
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


class A5IdentityTimeChangeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.en = EN_PATH.read_text(encoding="utf-8")
        cls.ru = RU_PATH.read_text(encoding="utf-8")

    def test_language_selectors_and_heading_parity(self) -> None:
        for literal in (
            "(./A5_IDENTITY_TIME_AND_CHANGE.md)",
            "(./A5_IDENTITY_TIME_AND_CHANGE.ru.md)",
        ):
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)
        self.assertEqual(validator.heading_levels(self.en), validator.heading_levels(self.ru))
        self.assertEqual(1, validator.heading_levels(self.en).count(1))
        self.assertEqual(1, validator.heading_levels(self.ru).count(1))

    def test_model_identity_status_and_next_slice_are_bilingual(self) -> None:
        required = (
            "model_id: nk-identity-time-change/A5-draft-1",
            "state: DRAFTED",
            "classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL",
            "next_content_slice: A6_KNOWLEDGE_LIFECYCLE",
            "runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED",
            "Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED",
        )
        for literal in required:
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)

    def test_exact_identity_kind_inventory_is_bilingual(self) -> None:
        self.assertEqual(
            IDENTITY_KINDS,
            _table_first_column(self.en, "## 3. Identity kinds"),
        )
        self.assertEqual(
            IDENTITY_KINDS,
            _table_first_column(self.ru, "## 3. Identity kinds"),
        )

    def test_identity_relation_outcomes_are_explicit(self) -> None:
        for outcome in IDENTITY_OUTCOMES:
            self.assertIn(outcome, self.en)
            self.assertIn(outcome, self.ru)
        for markdown in (self.en, self.ru):
            self.assertIn("same **under the named identity relation**", markdown)
            self.assertIn("UNRESOLVED", markdown)

    def test_temporal_dimensions_are_exact_and_bilingual(self) -> None:
        self.assertEqual(
            TEMPORAL_DIMENSIONS,
            _table_first_column(self.en, "## 6. Temporal dimensions"),
        )
        self.assertEqual(
            TEMPORAL_DIMENSIONS,
            _table_first_column(self.ru, "## 6. Temporal dimensions"),
        )

    def test_order_relations_and_write_causality_boundary_exist(self) -> None:
        for relation in ORDER_RELATIONS:
            self.assertIn(relation, self.en)
            self.assertIn(relation, self.ru)
        for markdown in (self.en, self.ru):
            self.assertIn("A <write B", markdown)
            self.assertIn("A <causal B", markdown)

    def test_change_matrix_keeps_key_non_equivalences(self) -> None:
        required = (
            "storage relocation / backend replacement",
            "exact copy",
            "translation",
            "semantic correction",
            "Revision",
            "Supersession",
            "restriction",
            "logical erasure",
            "physical/cryptographic erasure",
            "forgetting/loss",
            "represented-world change",
        )
        for literal in required:
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)

    def test_existing_contracts_are_reconciled_without_silent_supersession(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in (
                "nk-id/1.0",
                "global_seq",
                "stream_seq",
                "Issue #14",
                "Issue #15",
                "Issue #16",
                "Issue #74 / ADR-0024",
                "Issue #18",
                "No ADR status changes here.",
            ):
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

    def test_a5_defers_later_blueprint_and_runtime_work(self) -> None:
        for markdown in (self.en, self.ru):
            deferred = markdown.split("## 15.", 1)[1]
            for literal in (
                "A6",
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
