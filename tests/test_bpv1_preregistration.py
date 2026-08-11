from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "ai_context" / "validate_bpv1_preregistration.py"
SPEC = importlib.util.spec_from_file_location("validate_bpv1_preregistration", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)
PLAN = json.loads((ROOT / "docs" / "research" / "BPV1_PREREGISTRATION.json").read_text(encoding="utf-8"))
EN = (ROOT / "docs" / "research" / "BPV1_PREREGISTRATION.md").read_text(encoding="utf-8")
RU = (ROOT / "docs" / "research" / "BPV1_PREREGISTRATION.ru.md").read_text(encoding="utf-8")


class BPV1PreregistrationTests(unittest.TestCase):
    def validate(self, plan: dict | None = None) -> None:
        module.validate_plan(copy.deepcopy(PLAN) if plan is None else plan)

    def test_authoritative_plan_passes(self) -> None:
        digest = module.validate(ROOT)
        self.assertRegex(digest, r"^[0-9a-f]{64}$")

    def test_exact_twelve_preregistration_fields_exist(self) -> None:
        self.assertEqual(12, len(module.REQUIRED_FIELDS))
        self.assertEqual(module.REQUIRED_FIELDS, [field for field in module.REQUIRED_FIELDS if field in PLAN])

    def test_execution_is_not_authorized_by_plan(self) -> None:
        self.assertFalse(PLAN["execution_authorized"])
        self.assertTrue(PLAN["execution_admission_required"])
        self.assertFalse(PLAN["execution_boundary"]["plan_merge_authorizes_execution"])
        self.assertEqual("BPV1_EXECUTION_ADMISSION", PLAN["execution_boundary"]["next_gate"])
        self.assertEqual("BLOCKED_PENDING_EXECUTION_ADMISSION", PLAN["execution_boundary"]["execution_status_after_plan_merge"])
        self.assertFalse(PLAN["product_runtime_thaw"])
        self.assertFalse(PLAN["automatic_canon_promotion"])
        self.assertFalse(PLAN["automatic_runtime_promotion"])

    def test_instrument_is_cross_language_and_non_event_sourced(self) -> None:
        instrument = PLAN["implementation_instrument"]
        self.assertEqual("Rust", instrument["language"])
        self.assertEqual("EXPERIMENTAL_INSTRUMENT_NOT_CANON", instrument["language_role"])
        self.assertEqual("PROHIBITED_AS_AUTHORITATIVE_HISTORY_MODEL", instrument["event_sourcing"])
        self.assertEqual("PROHIBITED", instrument["current_native_kernel_dependency"])
        self.assertEqual("PROHIBITED", instrument["current_python_domain_model_translation"])
        self.assertFalse(instrument["exact_replay_requirement"])
        self.assertFalse(instrument["global_total_order_requirement"])

    def test_same_custody_and_computation_model_are_not_overclaimed(self) -> None:
        rules = PLAN["applicability_rules"]
        self.assertEqual("DECLARED_LIMITATION", rules["same_repository_custody"])
        self.assertEqual("NOT_ESTABLISHED", rules["independent_team"])
        self.assertEqual("NOT_ESTABLISHED / CONVENTIONAL_DIGITAL", rules["independent_computation_model"])

    def test_bounded_workload_is_exact(self) -> None:
        workload = PLAN["workload"]
        self.assertEqual(512, workload["scripted_mutations"])
        self.assertEqual([128, 256, 512], workload["checkpoints_after_mutations"])
        self.assertEqual(262144, workload["durable_state_byte_cap"])
        self.assertEqual(64, workload["retained_detailed_predecessor_cap"])
        self.assertEqual(32, workload["loss_witness_cap"])
        self.assertFalse(workload["authoritative_per_operation_append_log_allowed"])
        self.assertEqual(8, workload["bounded_crash_journal_max_entries"])
        self.assertFalse(workload["bounded_crash_journal_may_define_semantic_history"])

    def test_all_fixture_families_are_mandatory(self) -> None:
        self.assertEqual(module.FIXTURE_IDS, [item["id"] for item in PLAN["fixture_families"]])
        self.assertTrue(all(item["mandatory"] for item in PLAN["fixture_families"]))

    def test_hard_semantic_failures_are_zero_tolerance(self) -> None:
        thresholds = PLAN["failure_thresholds"]
        for key in (
            "semantic_hard_failures_allowed",
            "mandatory_fixture_failures_allowed",
            "silent_unknown_to_false_coercions_allowed",
            "silent_loss_inside_declared_retention_scope_allowed",
            "unauthorized_conflict_winner_selections_allowed",
            "material_role_collapses_allowed",
        ):
            self.assertEqual(0, thresholds[key])
        self.assertIn("no averaging", thresholds["aggregate_pass_rule"])

    def test_unknown_cannot_be_promoted_to_pass_when_unobservable(self) -> None:
        self.assertIn("INDETERMINATE", PLAN["failure_thresholds"]["indeterminate_rule"])
        self.assertIn("Unknown must remain distinct from False", "\n".join(PLAN["equivalence_predicates"]))

    def test_not_applicable_claims_have_preregistered_rationale(self) -> None:
        for key in ("physical_erasure", "cryptographic_erasure", "composition_federation"):
            value = PLAN["applicability_rules"][key]
            self.assertTrue(value.startswith("NOT_APPLICABLE / "))
            self.assertGreater(len(value), len("NOT_APPLICABLE / "))

    def test_oracle_is_external_to_implementation_under_test(self) -> None:
        oracle = PLAN["oracle_authority"]
        self.assertEqual("BPV1-ORACLE-001", oracle["authority_id"])
        self.assertFalse(oracle["implementation_under_test_may_modify_oracle"])
        self.assertFalse(oracle["implementation_under_test_may_define_expected_outcomes"])
        self.assertEqual(module.A10_OUTCOMES, oracle["result_vocabulary"])
        self.assertIn("separate BPV1_EXECUTION_ADMISSION checkpoint", oracle["execution_admission_requires"])

    def test_post_hoc_normative_change_requires_new_scenario(self) -> None:
        self.assertEqual(
            "INVALIDATES_RUN_FOR_CLAIMED_SCOPE_AND_REQUIRES_NEW_SCENARIO_ID",
            PLAN["applicability_rules"]["post_hoc_applicability_change"],
        )
        self.assertTrue(PLAN["execution_boundary"]["execution_cannot_change_preregistered_fields"])
        self.assertTrue(PLAN["execution_boundary"]["change_requires_new_scenario_id"])

    def test_event_log_threshold_cannot_be_enabled(self) -> None:
        plan = copy.deepcopy(PLAN)
        plan["failure_thresholds"]["authoritative_per_operation_append_log_allowed"] = True
        with self.assertRaisesRegex(module.BPV1PreregistrationError, "Event-log threshold drift"):
            self.validate(plan)

    def test_execution_cannot_be_enabled(self) -> None:
        plan = copy.deepcopy(PLAN)
        plan["execution_authorized"] = True
        with self.assertRaisesRegex(module.BPV1PreregistrationError, "must not authorize execution"):
            self.validate(plan)

    def test_runtime_thaw_cannot_be_enabled(self) -> None:
        plan = copy.deepcopy(PLAN)
        plan["product_runtime_thaw"] = True
        with self.assertRaisesRegex(module.BPV1PreregistrationError, "cannot thaw product runtime"):
            self.validate(plan)

    def test_mandatory_field_cannot_be_removed(self) -> None:
        plan = copy.deepcopy(PLAN)
        del plan["threat_model"]
        with self.assertRaisesRegex(module.BPV1PreregistrationError, "missing required preregistration fields"):
            self.validate(plan)

    def test_bounded_state_cap_cannot_drift(self) -> None:
        plan = copy.deepcopy(PLAN)
        plan["workload"]["durable_state_byte_cap"] = 999999
        with self.assertRaisesRegex(module.BPV1PreregistrationError, "bounded-memory workload drift"):
            self.validate(plan)

    def test_hard_refutation_cannot_be_removed(self) -> None:
        plan = copy.deepcopy(PLAN)
        plan["hard_refutation_observations"] = plan["hard_refutation_observations"][:-1]
        with self.assertRaisesRegex(module.BPV1PreregistrationError, "exactly ten hard refutation"):
            self.validate(plan)

    def test_independent_team_cannot_be_claimed(self) -> None:
        plan = copy.deepcopy(PLAN)
        plan["applicability_rules"]["independent_team"] = "ESTABLISHED"
        with self.assertRaisesRegex(module.BPV1PreregistrationError, "independent-team overclaim"):
            self.validate(plan)

    def test_physical_erasure_cannot_silently_become_applicable(self) -> None:
        plan = copy.deepcopy(PLAN)
        plan["applicability_rules"]["physical_erasure"] = "APPLICABLE"
        with self.assertRaisesRegex(module.BPV1PreregistrationError, "physical_erasure requires"):
            self.validate(plan)

    def test_bilingual_plan_preserves_execution_hard_stop(self) -> None:
        for markdown in (EN, RU):
            for literal in (
                "nk-bpv1-preregistration/1",
                "BPV1-001-cross-lineage-bounded-accountability-v1",
                "PREREGISTERED / EXECUTION_NOT_AUTHORIZED",
                "BPV1_EXECUTION_ADMISSION",
                "BLOCKED_PENDING_EXECUTION_ADMISSION",
                "FROZEN",
                "SUPPORTED_FOR_SCOPE",
                "WEAKENED",
                "REFUTED",
                "INDETERMINATE",
                "NOT_TESTED",
                "NOT_TESTED ≠ SUPPORTED",
            ):
                self.assertIn(literal, markdown)


if __name__ == "__main__":
    unittest.main()
