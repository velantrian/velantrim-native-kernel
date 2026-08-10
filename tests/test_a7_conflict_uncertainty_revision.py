from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "docs" / "A7_CONFLICT_UNCERTAINTY_AND_REVISION.md"
RU_PATH = ROOT / "docs" / "A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md"
VALIDATOR_PATH = ROOT / "tools" / "docs" / "validate_bilingual_parity.py"

SPEC = importlib.util.spec_from_file_location("validate_bilingual_parity", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

ASSESSMENT_STATUSES = (
    "CANDIDATE",
    "ESTABLISHED",
    "NOT_A_CONFLICT",
    "UNRESOLVED_ASSESSMENT",
)

RESOLUTION_STATUSES = (
    "UNRESOLVED",
    "DEFERRED",
    "RESOLVED_FOR_SCOPE",
    "REOPENED",
)

TENSION_KINDS = (
    "DUPLICATE_DELIVERY",
    "WRITE_VERSION_RACE",
    "DIVERGENT_HISTORY",
    "SEMANTIC_CONTRADICTION",
    "TEMPORAL_MISMATCH",
    "SCOPE_MISMATCH",
    "PROVENANCE_CONFLICT",
    "MEASUREMENT_DISAGREEMENT",
    "AUTHORITY_CONFLICT",
    "POLICY_CONFLICT",
    "EPISTEMIC_DISAGREEMENT",
    "PROJECTION_DRIFT",
    "UNCLASSIFIED_TENSION",
)

UNCERTAINTY_KINDS = (
    "EVIDENCE_GAP",
    "PROVENANCE_GAP",
    "CONTEXT_GAP",
    "TEMPORAL_GAP",
    "IDENTITY_GAP",
    "INTERPRETATION_GAP",
    "AUTHORITY_GAP",
    "CAPABILITY_GAP",
    "DEPENDENCY_UNCERTAINTY",
    "MEASUREMENT_UNCERTAINTY",
    "UNCLASSIFIED_UNCERTAINTY",
)

RESOLUTION_MODES = (
    "DISSOLVE_BY_ALIGNMENT",
    "RETAIN_PLURALITY",
    "PREFER_FOR_SCOPE",
    "REVISE_POSITION",
    "SUPERSEDE_FOR_SCOPE",
    "DEFER_DECISION",
    "NO_AUTHORIZED_RESOLUTION",
)


def _table_first_column(markdown: str, section_heading: str) -> tuple[str, ...]:
    heading_level = len(section_heading) - len(section_heading.lstrip("#"))
    section = markdown.split(section_heading, 1)[1]
    values: list[str] = []
    for line in section.splitlines():
        heading = re.match(r"^(#{1,6})\s", line)
        if heading and len(heading.group(1)) <= heading_level:
            break
        match = re.match(r"^\| `([^`]+)` \|", line)
        if match:
            values.append(match.group(1))
    return tuple(values)


class A7ConflictUncertaintyRevisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.en = EN_PATH.read_text(encoding="utf-8")
        cls.ru = RU_PATH.read_text(encoding="utf-8")

    def test_language_selectors_and_heading_parity(self) -> None:
        for literal in (
            "(./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md)",
            "(./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md)",
        ):
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)
        self.assertEqual(validator.heading_levels(self.en), validator.heading_levels(self.ru))
        self.assertEqual(1, validator.heading_levels(self.en).count(1))
        self.assertEqual(1, validator.heading_levels(self.ru).count(1))

    def test_model_identity_status_and_next_slice_are_bilingual(self) -> None:
        required = (
            "model_id: nk-conflict-uncertainty-revision/A7-draft-1",
            "state: DRAFTED",
            "classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL",
            "next_content_slice: A8_SUBSTRATE_INDEPENDENCE_CONTRACT",
            "runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED",
            "ADR-0003 decision status: PROPOSED / UNCHANGED",
            "Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED",
        )
        for literal in required:
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)

    def test_assessment_and_resolution_axes_are_exact(self) -> None:
        self.assertEqual(
            ASSESSMENT_STATUSES,
            _table_first_column(self.en, "### 3.1 Assessment status"),
        )
        self.assertEqual(
            ASSESSMENT_STATUSES,
            _table_first_column(self.ru, "### 3.1 Статус установления"),
        )
        self.assertEqual(
            RESOLUTION_STATUSES,
            _table_first_column(self.en, "### 3.2 Resolution status"),
        )
        self.assertEqual(
            RESOLUTION_STATUSES,
            _table_first_column(self.ru, "### 3.2 Статус решения"),
        )

    def test_exact_tension_taxonomy_is_bilingual(self) -> None:
        self.assertEqual(
            TENSION_KINDS,
            _table_first_column(self.en, "## 4. Tension taxonomy"),
        )
        self.assertEqual(
            TENSION_KINDS,
            _table_first_column(self.ru, "## 4. Таксономия напряжений"),
        )

    def test_exact_uncertainty_inventory_is_bilingual(self) -> None:
        self.assertEqual(
            UNCERTAINTY_KINDS,
            _table_first_column(self.en, "## 6. Typed uncertainty positions"),
        )
        self.assertEqual(
            UNCERTAINTY_KINDS,
            _table_first_column(self.ru, "## 6. Typed uncertainty positions"),
        )

    def test_typed_relations_are_explicit(self) -> None:
        for markdown in (self.en, self.ru):
            self.assertIn("UNCERTAINTY_POSITION(", markdown)
            self.assertIn("TENSION_POSITION(", markdown)
            self.assertIn("EPISTEMIC_REVISION(", markdown)
            self.assertIn("dependency_information", markdown)
            self.assertIn("resolution_ref_or_none", markdown)
            self.assertIn("uncertainty_before_after", markdown)

    def test_exact_resolution_modes_are_bilingual(self) -> None:
        self.assertEqual(
            RESOLUTION_MODES,
            _table_first_column(self.en, "## 9. Resolution modes without a universal winner algorithm"),
        )
        self.assertEqual(
            RESOLUTION_MODES,
            _table_first_column(self.ru, "## 9. Режимы решения без универсального winner algorithm"),
        )

    def test_conflict_and_uncertainty_non_equivalences_are_explicit(self) -> None:
        shared = (
            "Conflict ≠ necessarily Contradiction",
            "candidate tension ≠ established tension",
            "detection ≠ resolution",
            "resolution-for-scope ≠ objective truth",
            "uncertainty ≠ one universal confidence scalar",
            "confidence score ≠ Evidence",
            "newer ≠ more correct",
            "majority ≠ truth",
            "write order ≠ semantic precedence",
            "unknown ≠ false",
        )
        for markdown in (self.en, self.ru):
            for literal in shared:
                self.assertIn(literal, markdown)

    def test_existing_contract_and_adr_boundaries_are_preserved(self) -> None:
        shared = (
            "NK-CFL-001",
            "NK-CFL-008",
            "ADR-0003",
            "PROPOSED / NOT_STARTED",
            "Issue #74 / ADR-0024",
            "PROPOSED / PENDING_OPERATOR",
            "nk-p1-reducer/1",
            "CONFLICT_OPENED",
            "CONFLICT_RESOLVED",
        )
        for markdown in (self.en, self.ru):
            for literal in shared:
                self.assertIn(literal, markdown)

    def test_a6_lifecycle_is_refined_not_replaced(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in (
                "IN_TENSION",
                "EPISTEMICALLY_WEIGHED",
                "RELATIONALLY_INTEGRATED",
                "REVISED_OR_SUPERSEDED",
                "DETECT_TENSION",
                "ACCOUNTED ≠ true/correct",
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

    def test_a7_defers_later_blueprint_and_runtime_work(self) -> None:
        for markdown in (self.en, self.ru):
            deferred = markdown.split("## 17.", 1)[1]
            for literal in (
                "A8",
                "A9",
                "A10",
                "ADR-0003",
                "Issue #14",
                "Issue #15",
                "Issue #16",
                "Issue #17",
                "Issue #74 / ADR-0024",
                "Issue #18",
                "Track H",
                "new Event vocabulary",
                "CRDT",
                "LLM/vector adapters",
                "runtime implementation",
                "production authorization",
            ):
                self.assertIn(literal, deferred)


if __name__ == "__main__":
    unittest.main()
