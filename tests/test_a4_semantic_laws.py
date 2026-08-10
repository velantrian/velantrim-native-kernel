from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "docs" / "A4_SEMANTIC_LAWS_AND_INVARIANTS.md"
RU_PATH = ROOT / "docs" / "A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md"
VALIDATOR_PATH = ROOT / "tools" / "docs" / "validate_bilingual_parity.py"

SPEC = importlib.util.spec_from_file_location("validate_bilingual_parity", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

LAW_IDS = tuple(f"A4-L{number:02d}" for number in range(1, 29))
LAW_MARKERS = (
    "**Statement:**",
    "**Rationale:**",
    "**Counterexample/falsifier:**",
    "**Failure mode:**",
    "**Observable obligation:**",
    "**Exception/open uncertainty:**",
)

REQUIRED_BOUNDARIES = (
    "representation is not represented reality",
    "Unknown, missing, unsupported, partial, and failed are not False",
    "Semantic identity is not storage or physical identity",
    "Revision is not silent overwrite",
    "Supersession is not deletion and is not falsity",
    "Conflict detection is not conflict resolution",
    "Derived views do not rewrite history or become universal State",
    "History visibility is required; Event sourcing, reducer replay, and global total order are not universal mechanisms",
    "Determinism and reproducibility are not truth or physical identity; equivalence is named",
    "conformance is not production authorization",
)


def _law_sections(markdown: str) -> dict[str, str]:
    matches = list(
        re.finditer(
            r"^###\s+(A4-L\d{2})\s+—\s+.*$",
            markdown,
            flags=re.MULTILINE,
        )
    )
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        sections[match.group(1)] = markdown[match.end() : end]
    return sections


class A4SemanticLawTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.en = EN_PATH.read_text(encoding="utf-8")
        cls.ru = RU_PATH.read_text(encoding="utf-8")

    def test_language_selectors_and_heading_parity(self) -> None:
        for literal in (
            "(./A4_SEMANTIC_LAWS_AND_INVARIANTS.md)",
            "(./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md)",
        ):
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)
        self.assertEqual(validator.heading_levels(self.en), validator.heading_levels(self.ru))
        self.assertEqual(1, validator.heading_levels(self.en).count(1))
        self.assertEqual(1, validator.heading_levels(self.ru).count(1))

    def test_exact_numbered_law_inventory_is_bilingual(self) -> None:
        self.assertEqual(LAW_IDS, tuple(_law_sections(self.en)))
        self.assertEqual(LAW_IDS, tuple(_law_sections(self.ru)))

    def test_every_law_has_required_semantic_fields(self) -> None:
        for language, markdown in (("en", self.en), ("ru", self.ru)):
            sections = _law_sections(markdown)
            for law_id in LAW_IDS:
                with self.subTest(language=language, law_id=law_id):
                    section = sections[law_id]
                    for marker in LAW_MARKERS:
                        self.assertIn(marker, section)

    def test_law_set_identity_and_status_are_bilingual(self) -> None:
        required = (
            "law_set: nk-semantic-laws/A4-draft-1",
            "law_count: 28",
            "state: DRAFTED",
            "classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL",
            "next_content_slice: A5_IDENTITY_TIME_AND_CHANGE",
            "runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED",
            "Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED",
        )
        for literal in required:
            with self.subTest(literal=literal):
                self.assertIn(literal, self.en)
                self.assertIn(literal, self.ru)

    def test_old_false_notion_law_set_identity_is_not_reused(self) -> None:
        for markdown in (self.en, self.ru):
            self.assertIn("previously erroneous Notion-only label", markdown)
            self.assertIn("nk-semantic-laws/0.1-draft", markdown)
            self.assertNotIn("law_set: nk-semantic-laws/0.1-draft", markdown)

    def test_core_boundaries_are_present(self) -> None:
        for literal in REQUIRED_BOUNDARIES:
            with self.subTest(literal=literal):
                self.assertIn(literal, self.en)

    def test_three_contrasting_substrate_mappings_exist(self) -> None:
        markers = (
            "Manual archival and review process",
            "Adaptive analog or neuromorphic substrate",
            "Conventional digital Event-sourced laboratory",
        )
        for marker in markers:
            self.assertIn(marker, self.en)
            self.assertIn(marker, self.ru)

    def test_a4_does_not_authorize_later_deliverables_or_runtime(self) -> None:
        for markdown in (self.en, self.ru):
            later = markdown.split("## 15.", 1)[1]
            for literal in (
                "A5",
                "A6",
                "A7",
                "A8",
                "A9",
                "A10",
                "Issue #74 / ADR-0024",
                "Issue #18",
                "runtime implementation",
                "new Event vocabulary",
                "new databases",
                "LLM/vector adapters",
                "production authorization",
            ):
                self.assertIn(literal, later)


if __name__ == "__main__":
    unittest.main()
