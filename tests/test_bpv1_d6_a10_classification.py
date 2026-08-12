from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSIFICATION = ROOT / "docs" / "research" / "BPV1_D6_A10_CLASSIFICATION.json"
PLAN = ROOT / "docs" / "research" / "BPV1_PREREGISTRATION.json"
EVALUATION = ROOT / "experiments" / "bpv1" / "BPV1-001" / "results" / "d5-r1" / "evaluation-report.json"
QUALIFICATION = ROOT / "experiments" / "bpv1" / "BPV1-001" / "results" / "d5-r1" / "qualification-report.json"
EN = ROOT / "docs" / "research" / "BPV1_D6_A10_CLASSIFICATION.md"
RU = ROOT / "docs" / "research" / "BPV1_D6_A10_CLASSIFICATION.ru.md"

EXPECTED_OUTCOMES = {
    "A10-H01": "SUPPORTED_FOR_SCOPE",
    "A10-H02": "SUPPORTED_FOR_SCOPE",
    "A10-H03": "NOT_TESTED",
    "A10-H04": "SUPPORTED_FOR_SCOPE",
    "A10-H05": "SUPPORTED_FOR_SCOPE",
    "A10-H06": "NOT_TESTED",
    "A10-H07": "SUPPORTED_FOR_SCOPE",
    "A10-H08": "NOT_TESTED",
    "A10-H09": "NOT_TESTED",
    "A10-H10": "NOT_TESTED",
    "A10-H11": "NOT_TESTED",
    "A10-H12": "SUPPORTED_FOR_SCOPE",
}
EXPECTED_TARGETS = {
    "primary": ["A10-H02", "A10-H05"],
    "secondary": ["A10-H01", "A10-H04", "A10-H07", "A10-H12"],
    "informative_not_adjudicated": ["A10-H03", "A10-H10"],
    "not_tested": ["A10-H06", "A10-H08", "A10-H09", "A10-H11"],
}
ALLOWED = ["SUPPORTED_FOR_SCOPE", "WEAKENED", "REFUTED", "INDETERMINATE", "NOT_TESTED"]


class BPV1D6ClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.record = json.loads(CLASSIFICATION.read_text(encoding="utf-8"))
        cls.plan = json.loads(PLAN.read_text(encoding="utf-8"))
        cls.evaluation = json.loads(EVALUATION.read_text(encoding="utf-8"))
        cls.qualification = json.loads(QUALIFICATION.read_text(encoding="utf-8"))
        cls.en = EN.read_text(encoding="utf-8")
        cls.ru = RU.read_text(encoding="utf-8")

    def test_identity_and_frozen_plan_binding(self) -> None:
        self.assertEqual(self.record["protocol"], "nk-a10-hypothesis-classification/1")
        self.assertEqual(self.record["classification_id"], "BPV1-001-D6-A10-classification-v1")
        self.assertEqual(self.record["scenario_id"], self.plan["scenario_id"])
        self.assertEqual(self.record["frozen_plan_merge_sha"], "a538d7f1e28858a88b9ee777ac7d6e05b85943db")
        self.assertEqual(self.record["frozen_plan_sha256"], "7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0")

    def test_target_map_matches_preregistration_exactly(self) -> None:
        self.assertEqual(self.plan["target_hypotheses"], EXPECTED_TARGETS)
        self.assertEqual(self.record["preregistered_target_map"], EXPECTED_TARGETS)

    def test_allowed_outcome_vocabulary_is_exact(self) -> None:
        self.assertEqual(self.record["allowed_outcomes"], ALLOWED)

    def test_all_twelve_hypotheses_are_classified_once(self) -> None:
        rows = self.record["classifications"]
        ids = [row["hypothesis_id"] for row in rows]
        self.assertEqual(ids, [f"A10-H{i:02d}" for i in range(1, 13)])
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual({row["hypothesis_id"]: row["outcome"] for row in rows}, EXPECTED_OUTCOMES)

    def test_informative_hypotheses_are_not_promoted(self) -> None:
        by_id = {row["hypothesis_id"]: row for row in self.record["classifications"]}
        for hypothesis_id in EXPECTED_TARGETS["informative_not_adjudicated"]:
            self.assertEqual(by_id[hypothesis_id]["outcome"], "NOT_TESTED")

    def test_preregistered_not_tested_hypotheses_remain_not_tested(self) -> None:
        by_id = {row["hypothesis_id"]: row for row in self.record["classifications"]}
        for hypothesis_id in EXPECTED_TARGETS["not_tested"]:
            self.assertEqual(by_id[hypothesis_id]["outcome"], "NOT_TESTED")

    def test_aggregate_evaluator_result_is_not_copied_to_every_hypothesis(self) -> None:
        self.assertEqual(self.evaluation["outcome"], "SUPPORTED_FOR_SCOPE")
        outcomes = [row["outcome"] for row in self.record["classifications"]]
        self.assertIn("NOT_TESTED", outcomes)
        self.assertNotEqual(set(outcomes), {"SUPPORTED_FOR_SCOPE"})

    def test_qualified_evidence_binding(self) -> None:
        self.assertEqual(self.qualification["status"], "QUALIFIED")
        self.assertFalse(self.qualification["subject_self_report_used_for_structural_oracle_fields"])
        self.assertFalse(self.qualification["oracle_fixture_expectations_read"])
        self.assertFalse(self.qualification["implementation_private_runtime_state_read"])
        evidence = self.record["qualified_evidence"]
        self.assertEqual(evidence["qualification_status"], "QUALIFIED")
        self.assertEqual(evidence["frozen_evaluator_outcome"], "SUPPORTED_FOR_SCOPE")
        self.assertEqual(evidence["mandatory_fixture_pass"], 12)
        self.assertEqual(evidence["mandatory_fixture_total"], 12)
        self.assertEqual(evidence["hr10_self_report_path"], "REMOVED_BY_EXTERNAL_QUALIFICATION")

    def test_primary_support_has_direct_fixture_basis(self) -> None:
        by_id = {row["hypothesis_id"]: row for row in self.record["classifications"]}
        self.assertIn("BPV1-FX11", " ".join(by_id["A10-H02"]["basis"]))
        h05_basis = " ".join(by_id["A10-H05"]["basis"])
        self.assertIn("BPV1-FX04", h05_basis)
        self.assertIn("BPV1-FX06", h05_basis)

    def test_h07_limitations_forbid_independence_overclaim(self) -> None:
        h07 = next(row for row in self.record["classifications"] if row["hypothesis_id"] == "A10-H07")
        limits = h07["limits"].lower()
        self.assertIn("same-repository", limits)
        self.assertIn("not independently authored", limits)
        self.assertIn("conventional-digital", limits)
        self.assertIn("not mean independent validation", limits)

    def test_summary_arithmetic(self) -> None:
        self.assertEqual(self.record["summary"], {
            "SUPPORTED_FOR_SCOPE": 6,
            "WEAKENED": 0,
            "REFUTED": 0,
            "INDETERMINATE": 0,
            "NOT_TESTED": 6,
            "total": 12,
        })

    def test_runtime_and_promotion_boundary(self) -> None:
        self.assertEqual(self.record["runtime_expansion"], "FROZEN")
        self.assertFalse(self.record["product_runtime_thaw"])
        self.assertFalse(self.record["production_authorized"])
        self.assertEqual(self.record["next_gate_after_authoritative_merge"], "D7_INTEGRATED_RE_REVIEW")
        non_claims = " ".join(self.record["non_claims"]).lower()
        self.assertIn("final canon", non_claims)
        self.assertIn("universal substrate portability", non_claims)
        self.assertIn("does not authorize product runtime integration", non_claims)

    def test_bilingual_hypothesis_outcomes_are_present(self) -> None:
        for hypothesis_id, outcome in EXPECTED_OUTCOMES.items():
            for text in (self.en, self.ru):
                self.assertIn(hypothesis_id, text)
                self.assertIn(outcome, text)
        self.assertIn("D7_INTEGRATED_RE_REVIEW", self.en)
        self.assertIn("D7_INTEGRATED_RE_REVIEW", self.ru)


if __name__ == "__main__":
    unittest.main()
