from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "docs" / "A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md"
RU_PATH = ROOT / "docs" / "A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md"
VALIDATOR_PATH = ROOT / "tools" / "docs" / "validate_bilingual_parity.py"

SPEC = importlib.util.spec_from_file_location("validate_bilingual_parity", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

PRESERVATION_STATES = (
    "PRESERVED",
    "PARTIAL",
    "UNSUPPORTED",
    "INDETERMINATE",
    "LOSSY",
)

CONFORMANCE_OUTCOMES = (
    "FULL_CONFORMANCE_FOR_SCOPE",
    "BOUNDED_CONFORMANCE",
    "NON_CONFORMANT_FOR_SCOPE",
    "INDETERMINATE_CONFORMANCE",
)

PRESERVATION_OBLIGATIONS = tuple(f"A8-P{i:02d}" for i in range(1, 11))


def _table_first_column(markdown: str, section_heading: str) -> tuple[str, ...]:
    section = markdown.split(section_heading, 1)[1]
    values: list[str] = []
    started = False
    for line in section.splitlines():
        if line.startswith("## ") and started:
            break
        if line.startswith("| `"):
            started = True
            values.append(line.split("`", 2)[1])
    return tuple(values)


class A8SubstrateIndependenceContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.en = EN_PATH.read_text(encoding="utf-8")
        cls.ru = RU_PATH.read_text(encoding="utf-8")

    def test_language_selectors_and_heading_parity(self) -> None:
        for literal in (
            "(./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md)",
            "(./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md)",
        ):
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)
        self.assertEqual(validator.heading_levels(self.en), validator.heading_levels(self.ru))
        self.assertEqual(1, validator.heading_levels(self.en).count(1))
        self.assertEqual(1, validator.heading_levels(self.ru).count(1))

    def test_model_identity_status_and_next_slice_are_bilingual(self) -> None:
        required = (
            "model_id: nk-substrate-independence/A8-draft-1",
            "state: DRAFTED",
            "classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL",
            "next_content_slice: A9_REFERENCE_LABORATORY_BOUNDARY",
            "runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED",
            "Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED",
        )
        for literal in required:
            self.assertIn(literal, self.en)
            self.assertIn(literal, self.ru)

    def test_preservation_state_vocabulary_is_exact(self) -> None:
        self.assertEqual(
            PRESERVATION_STATES,
            _table_first_column(self.en, "## 3. Architecture-preserving mapping"),
        )
        self.assertEqual(
            PRESERVATION_STATES,
            _table_first_column(self.ru, "## 3. Architecture-preserving mapping"),
        )

    def test_preservation_obligations_are_exact_and_bilingual(self) -> None:
        self.assertEqual(
            PRESERVATION_OBLIGATIONS,
            _table_first_column(self.en, "## 4. Mandatory preserved semantic obligations"),
        )
        self.assertEqual(
            PRESERVATION_OBLIGATIONS,
            _table_first_column(self.ru, "## 4. Обязательные semantic preservation obligations"),
        )

    def test_conformance_outcomes_are_exact(self) -> None:
        self.assertEqual(
            CONFORMANCE_OUTCOMES,
            _table_first_column(self.en, "## 14. Conformance outcomes"),
        )
        self.assertEqual(
            CONFORMANCE_OUTCOMES,
            _table_first_column(self.ru, "## 14. Conformance outcomes"),
        )

    def test_equivalence_is_multidimensional(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in (
                "PHYSICAL_IDENTITY",
                "REPRESENTATION_EQUIVALENCE",
                "SEMANTIC_OBLIGATION_EQUIVALENCE",
                "BEHAVIORAL_CONFORMANCE_FOR_SCOPE",
                "LINEAGE_CONTINUITY_EQUIVALENCE",
                "physical identity",
                "is neither necessary nor sufficient",
                "for semantic equivalence",
            ):
                self.assertIn(literal, markdown)

    def test_required_non_equivalences_survive(self) -> None:
        shared = (
            "Conflict ≠ necessarily Contradiction",
            "Detection ≠ Resolution",
            "Resolution-for-scope ≠ Objective Truth",
            "Uncertainty ≠ one universal confidence scalar",
            "Revision ≠ overwrite",
            "write/commit order",
            "≠ occurrence order",
            "≠ causal/dependency order",
            "≠ semantic precedence",
        )
        for markdown in (self.en, self.ru):
            for literal in shared:
                self.assertIn(literal, markdown)

    def test_current_technologies_are_not_canon_requirements(self) -> None:
        for markdown in (self.en, self.ru):
            nonrequirements = markdown.split("## 19.", 1)[1]
            for literal in (
                "binary representation",
                "von Neumann CPU",
                "silicon",
                "RAM",
                "JSON",
                "SHA-256",
                "SQL",
                "PostgreSQL",
                "SQLite",
                "Event sourcing",
                "reducer",
                "global_seq",
                "wall-clock timestamps",
                "LLM",
                "embeddings",
                "Python",
                "network",
                "cloud",
            ):
                self.assertIn(literal, nonrequirements)

    def test_universal_portability_overclaim_is_explicitly_rejected(self) -> None:
        for markdown in (self.en, self.ru):
            for literal in (
                "substrate-independent specification",
                "universal portability proof",
                "substrate independence ≠ proof that every substrate can conform",
                "future-facing architecture ≠ implemented neuromorphic/analog/quantum profile",
                "full conformance ≠ production authorization",
                "public repository ≠ open-source license",
            ):
                self.assertIn(literal, markdown)

    def test_counterexamples_cover_required_failure_surface(self) -> None:
        for markdown in (self.en, self.ru):
            for marker in (
                "Counterexample A",
                "Counterexample B",
                "Counterexample C",
                "Counterexample D",
                "Counterexample E",
                "Counterexample F",
                "Counterexample G",
            ):
                self.assertIn(marker, markdown)
            self.assertIn("Provenance", markdown)
            self.assertIn("UNRESOLVED", markdown)
            self.assertIn("Event sourcing", markdown)
            self.assertIn("newest record", markdown)

    def test_operator_runtime_and_next_slice_boundaries_are_preserved(self) -> None:
        for markdown in (self.en, self.ru):
            deferred = markdown.split("## 20.", 1)[1]
            for literal in (
                "Issue #18",
                "Issue #74 / ADR-0024",
                "Track H",
                "reducer-v2",
                "runtime expansion",
                "FROZEN",
                "A9",
                "P1–C5",
            ):
                self.assertIn(literal, deferred)


if __name__ == "__main__":
    unittest.main()
