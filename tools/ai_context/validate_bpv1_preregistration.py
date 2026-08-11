#!/usr/bin/env python3
"""Fail closed when the BPV1-001 preregistration or execution boundary drifts."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Mapping

PLAN_PATH = Path("docs/research/BPV1_PREREGISTRATION.json")
PROTOCOL = "nk-bpv1-preregistration/1"
PLAN_ID = "BPV1-001-cross-lineage-bounded-accountability-v1"
ARCHITECTURE_CHECKPOINT = "c5d76fe281606edc0053bd7fc65167ebdfa50992"
REQUIRED_FIELDS = [
    "scenario_id",
    "purpose_scope",
    "mandatory_obligations",
    "applicability_rules",
    "mandatory_observables",
    "equivalence_predicates",
    "allowed_declared_losses",
    "failure_thresholds",
    "hard_refutation_observations",
    "grounding_mode",
    "threat_model",
    "oracle_authority",
]
FIXTURE_IDS = [f"BPV1-FX{n:02d}-{suffix}" for n, suffix in [
    (1, "UNKNOWN-NOT-FALSE"),
    (2, "ROLE-NONCONFLATION"),
    (3, "CONTEXT-BINDING"),
    (4, "REVISION-SUPERSESSION"),
    (5, "UNRESOLVED-PLURALITY"),
    (6, "BOUNDED-COMPACTION"),
    (7, "TRUNCATION-ROLLBACK"),
    (8, "FORGED-AUTHORITY"),
    (9, "WITHHELD-COUNTEREVIDENCE"),
    (10, "DECLARED-LOSS-AND-UNSUPPORTED"),
    (11, "NON-EVENT-HISTORY"),
    (12, "HIDDEN-SEMANTIC-DIVERGENCE"),
]]
A10_OUTCOMES = ["SUPPORTED_FOR_SCOPE", "WEAKENED", "REFUTED", "INDETERMINATE", "NOT_TESTED"]
EXPECTED_PRIMARY = ["A10-H02", "A10-H05"]
EXPECTED_SECONDARY = ["A10-H01", "A10-H04", "A10-H07", "A10-H12"]
EXPECTED_OPEN_QUESTIONS = ["A10-Q01", "A10-Q02", "A10-Q04", "A10-Q10", "A10-Q13", "A10-Q14", "A10-Q18"]
EXPECTED_THREATS = [
    "forgery",
    "truncation",
    "rollback",
    "equivocation",
    "withheld counterevidence",
    "unavailable witness",
    "forged Authority/provenance",
]
EXPECTED_ADMISSION_REQUIREMENTS = [
    "authoritative merged preregistration",
    "frozen preregistration digest",
    "machine-readable fixture/oracle package derived only from this plan",
    "standalone evaluator tests passing before subject implementation execution",
    "pinned Rust toolchain and experimental source boundary",
    "static scope audit proving no product runtime/profile integration",
    "separate BPV1_EXECUTION_ADMISSION checkpoint",
]


class BPV1PreregistrationError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise BPV1PreregistrationError(message)


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BPV1PreregistrationError(f"cannot read BPV-1 preregistration: {exc}") from exc
    _require(isinstance(value, dict), "BPV-1 preregistration must be an object")
    return value


def semantic_projection_digest(plan: Mapping[str, Any]) -> str:
    projection = {field: plan[field] for field in REQUIRED_FIELDS}
    canonical = json.dumps(projection, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def validate_plan(plan: Mapping[str, Any]) -> None:
    _require(plan.get("protocol") == PROTOCOL, "BPV-1 protocol drift")
    _require(plan.get("plan_id") == PLAN_ID, "BPV-1 plan identity drift")
    _require(plan.get("status") == "PREREGISTERED / EXECUTION_NOT_AUTHORIZED", "BPV-1 preregistration status drift")
    _require(plan.get("architecture_checkpoint") == ARCHITECTURE_CHECKPOINT, "BPV-1 architecture checkpoint drift")
    _require(plan.get("decision") == "ADR-0026", "BPV-1 decision binding drift")
    _require(plan.get("review") == "IAR-1", "BPV-1 review binding drift")
    _require(plan.get("reconciliation") == "IAR-1-R1", "BPV-1 reconciliation binding drift")
    _require(plan.get("role") == "FALSIFICATION_INSTRUMENT_ONLY", "BPV-1 role drift")
    _require(plan.get("execution_authorized") is False, "BPV-1 plan must not authorize execution")
    _require(plan.get("execution_admission_required") is True, "BPV-1 execution admission must remain required")
    _require(plan.get("next_gate_after_plan_merge") == "BPV1_EXECUTION_ADMISSION", "BPV-1 next gate drift")
    _require(plan.get("product_runtime_thaw") is False, "BPV-1 plan cannot thaw product runtime")
    _require(plan.get("automatic_canon_promotion") is False, "BPV-1 plan cannot auto-promote Canon")
    _require(plan.get("automatic_runtime_promotion") is False, "BPV-1 plan cannot auto-promote runtime")

    missing = [field for field in REQUIRED_FIELDS if field not in plan]
    _require(not missing, f"missing required preregistration fields: {missing}")
    _require(plan.get("scenario_id") == PLAN_ID, "scenario_id must equal plan identity")

    instrument = plan.get("implementation_instrument")
    _require(isinstance(instrument, Mapping), "implementation instrument required")
    _require(instrument.get("language") == "Rust", "BPV-1 instrument language drift")
    _require(instrument.get("language_role") == "EXPERIMENTAL_INSTRUMENT_NOT_CANON", "Rust must remain experiment-only")
    _require(instrument.get("lineage_class") == "INDEPENDENT_LANGUAGE / SAME_REPOSITORY_CUSTODY / CONVENTIONAL_DIGITAL_COMPUTATION", "BPV-1 evidence class drift")
    _require(instrument.get("event_sourcing") == "PROHIBITED_AS_AUTHORITATIVE_HISTORY_MODEL", "authoritative Event sourcing must remain prohibited")
    for key in (
        "current_native_kernel_dependency",
        "current_python_domain_model_translation",
        "current_event_envelope_reuse",
        "current_reducer_reuse",
        "current_receipt_shape_as_oracle",
    ):
        _require(instrument.get(key) == "PROHIBITED", f"implementation-capture boundary drift: {key}")
    _require(instrument.get("exact_replay_requirement") is False, "exact replay cannot become a universal requirement")
    _require(instrument.get("global_total_order_requirement") is False, "global total order cannot become a universal requirement")
    _require(instrument.get("composition_or_federation") == "OUT_OF_SCOPE", "composition scope drift")

    targets = plan.get("target_hypotheses")
    _require(isinstance(targets, Mapping), "target hypotheses required")
    _require(targets.get("primary") == EXPECTED_PRIMARY, "primary A10 hypothesis inventory drift")
    _require(targets.get("secondary") == EXPECTED_SECONDARY, "secondary A10 hypothesis inventory drift")
    _require(plan.get("target_open_questions") == EXPECTED_OPEN_QUESTIONS, "A10 open-question inventory drift")

    workload = plan.get("workload")
    _require(isinstance(workload, Mapping), "bounded-memory workload required")
    expected_workload = {
        "active_claim_slots": 32,
        "revision_cycles": 16,
        "scripted_mutations": 512,
        "checkpoints_after_mutations": [128, 256, 512],
        "compaction_after_each_revision_cycle": True,
        "bounded_memory_definition": "BOUND_ON_RETAINED_DURABLE_EXPERIMENT_STATE_NOT_PROCESS_RSS",
        "durable_state_byte_cap": 262144,
        "retained_detailed_predecessor_cap": 64,
        "loss_witness_cap": 32,
        "growth_rule": "durable_bytes_at_512 <= durable_bytes_at_256 * 1.25 + 4096",
        "authoritative_per_operation_append_log_allowed": False,
        "bounded_crash_journal_allowed": True,
        "bounded_crash_journal_max_entries": 8,
        "bounded_crash_journal_may_define_semantic_history": False,
    }
    _require(dict(workload) == expected_workload, "bounded-memory workload drift")

    fixtures = plan.get("fixture_families")
    _require(isinstance(fixtures, list) and len(fixtures) == 12, "exactly twelve mandatory fixture families required")
    _require([item.get("id") for item in fixtures if isinstance(item, Mapping)] == FIXTURE_IDS, "fixture identity/order drift")
    _require(all(isinstance(item, Mapping) and item.get("mandatory") is True and str(item.get("purpose", "")).strip() for item in fixtures), "every fixture family must remain mandatory and purposeful")

    obligations = plan.get("mandatory_obligations")
    _require(isinstance(obligations, list) and len(obligations) == 10, "exactly ten mandatory obligations required")
    joined_obligations = "\n".join(str(item) for item in obligations)
    for marker in (
        "not be silently equated with reality or objective truth",
        "Unknown, uncertainty and unsupported",
        "CURRENT_ACCOUNTABILITY",
        "DECLARED_RETENTION_SCOPE",
        "LOSS_WITNESS",
        "without making a canonical per-operation Event log",
    ):
        _require(marker in joined_obligations, f"mandatory obligation marker missing: {marker}")

    applicability = plan.get("applicability_rules")
    _require(isinstance(applicability, Mapping), "applicability rules required")
    _require(applicability.get("independent_language") == "APPLICABLE / RUST", "independent-language applicability drift")
    _require(applicability.get("independent_team") == "NOT_ESTABLISHED", "independent-team overclaim")
    _require(applicability.get("independent_computation_model") == "NOT_ESTABLISHED / CONVENTIONAL_DIGITAL", "computation-model overclaim")
    for key in ("physical_erasure", "cryptographic_erasure", "composition_federation"):
        value = applicability.get(key)
        _require(isinstance(value, str) and value.startswith("NOT_APPLICABLE / ") and len(value) > len("NOT_APPLICABLE / "), f"{key} requires preregistered NOT_APPLICABLE rationale")
    _require(applicability.get("post_hoc_applicability_change") == "INVALIDATES_RUN_FOR_CLAIMED_SCOPE_AND_REQUIRES_NEW_SCENARIO_ID", "post-hoc applicability boundary drift")

    observables = plan.get("mandatory_observables")
    _require(isinstance(observables, list) and len(observables) == 12, "exactly twelve mandatory observables required")
    observables_text = "\n".join(str(item) for item in observables)
    for marker in ("Context binding", "LOSS_WITNESS", "128, 256 and 512", "authoritative per-operation append log", "evaluator"):
        _require(marker in observables_text, f"mandatory observable marker missing: {marker}")

    predicates = plan.get("equivalence_predicates")
    _require(isinstance(predicates, list) and len(predicates) == 10, "exactly ten equivalence predicates required")
    _require([str(item).split(":", 1)[0] for item in predicates] == [f"EQ{n:02d}" for n in range(1, 11)], "equivalence predicate identity drift")

    losses = plan.get("allowed_declared_losses")
    _require(isinstance(losses, list) and len(losses) == 9, "allowed declared loss inventory drift")
    _require(any("LOSS_WITNESS" in str(item) for item in losses), "compacted loss must require LOSS_WITNESS")

    thresholds = plan.get("failure_thresholds")
    _require(isinstance(thresholds, Mapping), "failure thresholds required")
    for key in (
        "semantic_hard_failures_allowed",
        "mandatory_fixture_failures_allowed",
        "silent_unknown_to_false_coercions_allowed",
        "silent_loss_inside_declared_retention_scope_allowed",
        "unauthorized_conflict_winner_selections_allowed",
        "material_role_collapses_allowed",
    ):
        _require(thresholds.get(key) == 0, f"hard semantic threshold drift: {key}")
    _require(thresholds.get("authoritative_per_operation_append_log_allowed") is False, "Event-log threshold drift")
    _require(thresholds.get("durable_state_byte_cap") == 262144, "durable-state cap drift")
    _require(thresholds.get("retained_detailed_predecessor_cap") == 64, "retained-predecessor cap drift")
    _require(thresholds.get("loss_witness_cap") == 32, "loss-witness cap drift")
    _require(thresholds.get("required_checkpoint_count") == 3, "checkpoint-count drift")
    _require(thresholds.get("required_mutation_count") == 512, "mutation-count drift")
    _require("INDETERMINATE" in str(thresholds.get("indeterminate_rule")), "indeterminate must not be counted as PASS")
    _require("no averaging" in str(thresholds.get("aggregate_pass_rule")), "hard failures cannot be averaged away")

    refutations = plan.get("hard_refutation_observations")
    _require(isinstance(refutations, list) and len(refutations) == 10, "exactly ten hard refutation observations required")
    _require([str(item).split(":", 1)[0] for item in refutations] == [f"HR{n:02d}" for n in range(1, 11)], "hard-refutation identity drift")
    refutation_text = "\n".join(str(item) for item in refutations)
    for marker in ("A10-H02", "A10-H05", "A10-H04", "A10-H01", "A10-H07", "INVALIDATED_FOR_CLAIMED_SCOPE"):
        _require(marker in refutation_text, f"hard-refutation marker missing: {marker}")

    grounding = plan.get("grounding_mode")
    _require(isinstance(grounding, Mapping), "grounding mode required")
    _require(grounding.get("mode") == "EXPLICIT_ASSUMED_ROOT", "grounding mode drift")
    _require(grounding.get("hidden_root_allowed") is False, "hidden grounding root cannot be allowed")
    _require("TERMINAL_UNKNOWN_OR_GAP" in str(grounding.get("recursion_rule")), "terminal unknown/gap grounding boundary missing")

    threat = plan.get("threat_model")
    _require(isinstance(threat, Mapping), "threat model required")
    _require(threat.get("mandatory_adversarial_cases") == EXPECTED_THREATS, "mandatory threat inventory drift")
    na = threat.get("not_applicable_with_rationale")
    _require(isinstance(na, Mapping), "threat-model NOT_APPLICABLE rationale map required")
    _require(set(na) == {"colluding_witness", "compromised_external_certifier", "physical_residue_after_erasure"}, "threat-model N/A inventory drift")
    _require(all(isinstance(value, str) and len(value.strip()) >= 40 for value in na.values()), "threat-model N/A rationale too weak")

    oracle = plan.get("oracle_authority")
    _require(isinstance(oracle, Mapping), "oracle Authority required")
    _require(oracle.get("authority_id") == "BPV1-ORACLE-001", "oracle identity drift")
    _require(oracle.get("normative_source_after_merge") == "docs/research/BPV1_PREREGISTRATION.json", "oracle source drift")
    _require(oracle.get("authority_scope") == "EXPERIMENTAL_CONFORMANCE_FOR_BPV1-001_ONLY", "oracle scope drift")
    _require(oracle.get("implementation_under_test_may_modify_oracle") is False, "implementation may not modify oracle")
    _require(oracle.get("implementation_under_test_may_define_expected_outcomes") is False, "implementation may not define expected outcomes")
    _require(oracle.get("execution_admission_requires") == EXPECTED_ADMISSION_REQUIREMENTS, "execution-admission requirement drift")
    _require(oracle.get("result_vocabulary") == A10_OUTCOMES, "A10 outcome vocabulary drift")

    execution = plan.get("execution_boundary")
    _require(isinstance(execution, Mapping), "execution boundary required")
    _require(execution.get("plan_merge_authorizes_execution") is False, "plan merge cannot authorize execution")
    _require(execution.get("next_gate") == "BPV1_EXECUTION_ADMISSION", "execution next gate drift")
    _require(execution.get("execution_status_after_plan_merge") == "BLOCKED_PENDING_EXECUTION_ADMISSION", "post-plan execution status drift")
    _require(execution.get("execution_branch_must_start_after_admission") is True, "execution branch must start after admission")
    _require(execution.get("execution_cannot_change_preregistered_fields") is True, "execution cannot rewrite preregistration")
    _require(execution.get("change_requires_new_scenario_id") is True, "preregistration changes require a new scenario id")


def validate(repo: Path) -> str:
    plan = _load(repo / PLAN_PATH)
    validate_plan(plan)
    return semantic_projection_digest(plan)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        digest = validate(args.repo.resolve())
    except BPV1PreregistrationError as exc:
        print(f"BPV-1 preregistration validation failed: {exc}", file=sys.stderr)
        return 1
    print(
        "BPV-1 preregistration validation passed; "
        f"scenario={PLAN_ID}; semantic_projection_sha256={digest}; "
        "execution=BLOCKED_PENDING_EXECUTION_ADMISSION; runtime_expansion_frozen=true"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
