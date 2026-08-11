from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = (ROOT / "docs" / "INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md").read_text(encoding="utf-8")
RU = (ROOT / "docs" / "INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md").read_text(encoding="utf-8")
ADR = (ROOT / "docs" / "adr" / "0026-independent-challenge-before-bounded-cross-lineage-falsification.md").read_text(encoding="utf-8")
STATE = json.loads((ROOT / "project-state.json").read_text(encoding="utf-8"))


class IndependentArchitectureReviewProtocolTests(unittest.TestCase):
    def test_protocol_identity_and_runtime_boundary_are_bilingual(self) -> None:
        for markdown in (EN, RU):
            self.assertIn("nk-independent-architecture-review/1", markdown)
            self.assertIn("ADR-0026", markdown)
            self.assertIn("FROZEN", markdown)
            self.assertIn("BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION", markdown)

    def test_required_questions_are_present(self) -> None:
        for markdown in (EN, RU):
            for index in range(1, 13):
                self.assertIn(f"Q{index}", markdown)

    def test_finding_schema_and_severity_are_explicit(self) -> None:
        for markdown in (EN, RU):
            self.assertIn("IAR-F01", markdown)
            for severity in ("BLOCKING", "MATERIAL", "MODERATE", "MINOR"):
                self.assertIn(severity, markdown)
            for disposition in ("REMOVE", "WEAKEN", "SPLIT", "CLARIFY", "TEST", "RETAIN"):
                self.assertIn(disposition, markdown)

    def test_review_process_cannot_be_confused_with_a10_outcomes(self) -> None:
        for markdown in (EN, RU):
            for process_outcome in (
                "QUALIFYING_REVIEW_COMPLETE",
                "BLOCKED_NO_QUALIFYING_REVIEWER",
                "INCOMPLETE_REVIEW",
                "REVIEW_INVALIDATED_BY_INDEPENDENCE_FAILURE",
            ):
                self.assertIn(process_outcome, markdown)

    def test_adr_records_option_d_without_runtime_thaw(self) -> None:
        self.assertIn("Option D", ADR)
        self.assertIn("INDEPENDENT_ARCHITECTURE_REVIEW", ADR)
        self.assertIn("BPV-1", ADR)
        self.assertIn("runtime_expansion: FROZEN", ADR)
        self.assertIn("product_runtime_thaw: NO", ADR)
        self.assertIn("automatic_canon_promotion: NO", ADR)
        self.assertIn("automatic_runtime_promotion: NO", ADR)

    def test_machine_state_starts_at_review_not_experiment(self) -> None:
        research = STATE["tracks"]["long_horizon_research"]
        validation = research["post_blueprint_validation"]
        self.assertEqual("INDEPENDENT_ARCHITECTURE_REVIEW", research["architecture_refoundation"]["next_content_slice"])
        self.assertEqual("NOT_ESTABLISHED", validation["independent_review_status"])
        self.assertEqual("BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION", validation["bpv1_status"])
        self.assertFalse(validation["product_runtime_thaw"])
        self.assertFalse(validation["automatic_canon_promotion"])
        self.assertFalse(validation["automatic_runtime_promotion"])


if __name__ == "__main__":
    unittest.main()