#!/usr/bin/env python3
"""Validate the planning-only Residual A10 Validation Plan.

This validator checks research-plan structure and authorization boundaries only.
It does not preregister, execute, or adjudicate any residual experiment.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping

PROTOCOL = "nk-residual-a10-validation-plan/1"
PLAN_ID = "RAVP-001-residual-a10-validation-plan-v1"
SOURCE_CHECKPOINT = "ec421410d6ea5df86adca3a962ad2c5ba699e297"
DECISION_MERGE = "57993f39906ae7266011f6146c9a485d0587d2bf"
PLAN_PATH = Path("docs/research/RESIDUAL_A10_VALIDATION_PLAN.json")
EN_PATH = Path("docs/research/RESIDUAL_A10_VALIDATION_PLAN.md")
RU_PATH = Path("docs/research/RESIDUAL_A10_VALIDATION_PLAN.ru.md")

ALLOWED_OUTCOMES = [
    "SUPPORTED_FOR_SCOPE",
    "WEAKENED",
    "REFUTED",
    "INDETERMINATE",
    "NOT_TESTED",
]
TARGETS = [
    "A10-H03",
    "A10-H06",
    "A10-H08",
    "A10-H09",
    "A10-H10",
    "A10-H11",
]
INDEPENDENCE_CLASSES = [
    "INDEPENDENT_LANGUAGE",
    "INDEPENDENT_IMPLEMENTATION_STRUCTURE",
    "INDEPENDENT_TEAM",
    "INDEPENDENT_CUSTODY",
    "INDEPENDENT_STORAGE_MODEL",
    "INDEPENDENT_COMPUTATION_MODEL",
    "INDEPENDENT_HARDWARE_FAMILY",
    "INDEPENDENT_SEMANTIC_ORACLE",
]
FAMILY_IDS = {
    "A10-H03": "RAVP-H03-REPRESENTATION-MIGRATION",
    "A10-H06": "RAVP-H06-DISPOSITION-ERASURE-EPISTEMICS",
    "A10-H08": "RAVP-H08-NON-ADDRESS-DYNAMICAL-CONTINUITY",
    "A10-H09": "RAVP-H09-PROBABILISTIC-CONFORMANCE",
    "A10-H10": "RAVP-H10-ORTHOGONAL-STORAGE-COMPUTATION",
    "A10-H11": "RAVP-H11-LAB-CANON-SEPARATION",
}
REQUIRED_FAMILY_FIELDS = {
    "hypothesis_id",
    "family_id",
    "hypothesis",
    "why_not_tested_by_bpv1",
    "target_semantic_obligations",
    "testable_question",
    "required_independence_axis",
    "strengthening_independence_axis",
    "candidate_realization_class",
    "observables",
    "equivalence_predicate",
    "allowed_losses",
    "failure_condition",
    "hard_refutation",
    "grounding_mode",
    "threat_trust_model",
    "oracle_authority",
    "reproduction_requirements",
    "expected_evidence",
}


class ResidualA10PlanError(ValueError):
    """Raised when residual planning truth drifts or overclaims authority."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ResidualA10PlanError(message)


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ResidualA10PlanError(f"plan file missing: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ResidualA10PlanError(f"plan JSON invalid: {exc}") from exc
    _require(isinstance(value, dict), "plan root must be an object")
    return value


def _nonempty_strings(value: Any, field: str) -> None:
    _require(isinstance(value, list) and bool(value), f"{field} must be a non-empty list")
    _require(
        all(isinstance(item, str) and item.strip() for item in value),
        f"{field} must contain non-empty strings",
    )


def _reject_execution_authority(value: Any, path: str = "root") -> None:
    """Reject any future drift that grants execution authority inside this plan."""
    if isinstance(value, Mapping):
        for key, item in value.items():
            child = f"{path}.{key}"
            normalized = key.lower()
            if "execution" in normalized and "authoriz" in normalized:
                _require(item is False, f"{child} must remain false in planning-only scope")
            _reject_execution_authority(item, child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _reject_execution_authority(item, f"{path}[{index}]")


def _family_map(plan: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    families = plan.get("families")
    _require(isinstance(families, list) and len(families) == 6, "plan must contain exactly six families")
    result: dict[str, Mapping[str, Any]] = {}
    seen_ids: set[str] = set()
    for index, raw in enumerate(families):
        _require(isinstance(raw, Mapping), f"families[{index}] must be an object")
        hypothesis_id = raw.get("hypothesis_id")
        family_id = raw.get("family_id")
        _require(hypothesis_id in TARGETS, f"families[{index}] unexpected hypothesis {hypothesis_id!r}")
        _require(hypothesis_id not in result, f"duplicate family for {hypothesis_id}")
        _require(family_id == FAMILY_IDS[hypothesis_id], f"{hypothesis_id} family_id drift")
        _require(family_id not in seen_ids, f"duplicate family_id {family_id}")
        seen_ids.add(str(family_id))
        missing = REQUIRED_FAMILY_FIELDS - set(raw)
        _require(not missing, f"{hypothesis_id} missing fields: {sorted(missing)}")
        _nonempty_strings(raw.get("target_semantic_obligations"), f"{hypothesis_id}.target_semantic_obligations")
        _nonempty_strings(raw.get("observables"), f"{hypothesis_id}.observables")
        _nonempty_strings(raw.get("failure_condition"), f"{hypothesis_id}.failure_condition")
        _nonempty_strings(raw.get("threat_trust_model"), f"{hypothesis_id}.threat_trust_model")
        _nonempty_strings(raw.get("reproduction_requirements"), f"{hypothesis_id}.reproduction_requirements")
        _nonempty_strings(raw.get("required_independence_axis"), f"{hypothesis_id}.required_independence_axis")
        for axis in raw["required_independence_axis"]:
            _require(axis in INDEPENDENCE_CLASSES, f"{hypothesis_id} unknown required independence axis {axis}")
        for axis in raw.get("strengthening_independence_axis", []):
            _require(axis in INDEPENDENCE_CLASSES, f"{hypothesis_id} unknown strengthening independence axis {axis}")
        result[str(hypothesis_id)] = raw
    _require(list(result) == TARGETS, "family order/target inventory drift")
    return result


def _validate_special_boundaries(plan: Mapping[str, Any], families: Mapping[str, Mapping[str, Any]]) -> None:
    h03 = families["A10-H03"]
    h03_question = str(h03["testable_question"]).lower()
    _require(
        "target representation" in h03_question
        and "substrate-local identity" in h03_question,
        "H03 must remain a representation-migration question",
    )
    _require("source-format physical identity" in str(h03["hard_refutation"]), "H03 hard refutation must guard source physical identity")

    h06 = families["A10-H06"]
    lanes = h06.get("evidence_lanes")
    _require(isinstance(lanes, list) and len(lanes) == 3, "H06 must contain exactly three evidence lanes")
    _require(
        [lane.get("lane") for lane in lanes if isinstance(lane, Mapping)]
        == ["LOGICAL_FORGETTING", "CRYPTOGRAPHIC_ERASURE", "PHYSICAL_ERASURE"],
        "H06 logical/cryptographic/physical lane inventory drift",
    )
    _require("INDETERMINATE" in json.dumps(h06, ensure_ascii=False), "H06 must preserve INDETERMINATE for unobservable erasure")
    _require("self-report" in json.dumps(h06, ensure_ascii=False).lower(), "H06 must reject self-report-only erasure evidence")

    h08 = families["A10-H08"]
    tiers08 = h08.get("qualification_tiers")
    _require(isinstance(tiers08, Mapping), "H08 qualification tiers required")
    _require(
        "CANNOT_SUPPORT_H08" in str(tiers08.get("SIMULATION_OR_EMULATION")),
        "H08 simulation/emulation must not support H08",
    )
    _require(
        "INDEPENDENT_HARDWARE_FAMILY" in h08["required_independence_axis"],
        "H08 requires independent hardware family",
    )
    _require("digital shadow" in json.dumps(h08, ensure_ascii=False).lower(), "H08 anti-shadow boundary required")

    h09 = families["A10-H09"]
    tiers09 = h09.get("qualification_tiers")
    _require(isinstance(tiers09, Mapping), "H09 qualification tiers required")
    _require(
        "CANNOT_SUPPORT_PHYSICAL_SUBSTRATE_CLAIM" in str(tiers09.get("SOFTWARE_STOCHASTIC_REHEARSAL")),
        "H09 software stochastic rehearsal cannot support substrate claim",
    )
    h09_text = json.dumps(h09, ensure_ascii=False).lower()
    _require("insufficient power" in h09_text and "indeterminate" in h09_text, "H09 insufficient-power boundary required")
    _require("post-hoc" in h09_text, "H09 post-hoc threshold rescue must be forbidden")

    h10 = families["A10-H10"]
    _require(
        h10.get("minimum_matrix") == ["C1/S1", "C1/S2", "C2/S1", "C2/S2"],
        "H10 must preserve the minimum 2x2 storage/computation matrix",
    )
    _require(
        "programming-language change alone does not qualify" in str(h10["equivalence_predicate"]).lower(),
        "H10 must distinguish language from computation-model independence",
    )

    h11 = families["A10-H11"]
    _require(
        h11.get("hypothesis") == "Laboratory mechanisms can remain reproducible without becoming Architecture Canon.",
        "H11 exact A10 hypothesis drift",
    )
    _require("federation" not in str(h11.get("hypothesis", "")).lower(), "H11 must not be redefined as federation")
    non_targets = plan.get("explicit_non_targets")
    _require(isinstance(non_targets, list), "explicit_non_targets required")
    _require(
        any("composition/federation" in str(item) and "not A10-H11" in str(item) for item in non_targets),
        "plan must preserve D7-F08 composition/federation as separate from H11",
    )


def _validate_human_docs(repo: Path) -> None:
    required_shared = [
        PLAN_ID,
        PROTOCOL,
        SOURCE_CHECKPOINT,
        "PLANNING_ONLY / EXECUTION_NOT_AUTHORIZED",
        "RESIDUAL_A10_VALIDATION_PLAN",
        "SEPARATE_FAMILY_PREREGISTRATION_SELECTION",
        "A10-H03",
        "A10-H06",
        "A10-H08",
        "A10-H09",
        "A10-H10",
        "A10-H11",
        "INDEPENDENT_COMPUTATION_MODEL",
        "INDEPENDENT_SEMANTIC_ORACLE",
        "composition/federation",
    ]
    for relative in (EN_PATH, RU_PATH):
        try:
            text = (repo / relative).read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise ResidualA10PlanError(f"human plan missing: {relative}") from exc
        lowered = text.lower()
        for literal in required_shared[:-1]:
            _require(literal in text, f"{relative}: missing shared plan literal {literal}")
        _require(required_shared[-1] in lowered, f"{relative}: missing composition/federation separation")
        _require("H11" in text and "Canon" in text, f"{relative}: H11 laboratory/Canon boundary missing")
        _require("simulation" in lowered and "H08" in text, f"{relative}: H08 simulation boundary missing")
        _require("stochastic" in lowered and "H09" in text, f"{relative}: H09 stochastic-rehearsal boundary missing")
        _require("2×2" in text and "H10" in text, f"{relative}: H10 2x2 matrix boundary missing")


def validate(repo: Path) -> None:
    repo = repo.resolve()
    plan = _load(repo / PLAN_PATH)
    _require(plan.get("protocol") == PROTOCOL, "residual plan protocol drift")
    _require(plan.get("plan_id") == PLAN_ID, "residual plan identity drift")
    _require(plan.get("state") == "PLANNING_ONLY / EXECUTION_NOT_AUTHORIZED", "residual plan must remain planning-only")
    _require(plan.get("source_checkpoint_sha") == SOURCE_CHECKPOINT, "residual plan source checkpoint drift")
    _require(plan.get("architecture_position") == "STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL", "architecture position overclaim/drift")
    _require(plan.get("allowed_a10_outcomes") == ALLOWED_OUTCOMES, "A10 outcome vocabulary drift")
    _require(plan.get("residual_targets") == TARGETS, "residual A10 target inventory drift")
    _require(plan.get("independence_classes") == INDEPENDENCE_CLASSES, "independence-class inventory drift")

    decision = plan.get("operator_decision")
    _require(isinstance(decision, Mapping), "ADR-0027 operator decision binding required")
    _require(decision.get("adr") == "ADR-0027", "ADR binding drift")
    _require(decision.get("decision_id") == "OD-POST-D8-001", "operator decision identity drift")
    _require(decision.get("decision_merge_sha") == DECISION_MERGE, "operator decision merge binding drift")
    _require(decision.get("authorized_gate") == "RESIDUAL_A10_VALIDATION_PLAN", "authorized planning gate drift")
    _require(decision.get("authorized_scope") == "RESEARCH_PLANNING_ONLY", "authorized scope drift")
    _require(decision.get("experiment_execution_authorized") is False, "residual experiment execution must remain unauthorized")
    _require(decision.get("runtime_expansion") == "FROZEN", "runtime expansion must remain frozen")
    _require(decision.get("product_runtime_thaw") is False, "product runtime thaw must remain false")
    _require(decision.get("production_authorized") is False, "production must remain unauthorized")
    _require(decision.get("final_canon") == "DEFERRED / NOT_AUTHORIZED_AT_THIS_CHECKPOINT", "Final Canon must remain deferred")

    fail_closed = plan.get("global_fail_closed_rules")
    _require(isinstance(fail_closed, Mapping), "global fail-closed rules required")
    _require(fail_closed.get("subject_self_pass") == "FORBIDDEN", "subject self-pass must remain forbidden")
    _require(fail_closed.get("implementation_self_report_as_semantic_truth") == "FORBIDDEN", "self-report must not become semantic truth")
    _require(fail_closed.get("private_implementation_state_as_mandatory_oracle_input") == "FORBIDDEN", "private-state oracle input must remain forbidden")
    _require(fail_closed.get("post_hoc_rescue_of_failed_run") == "FORBIDDEN", "post-hoc rescue must remain forbidden")
    _require(fail_closed.get("indeterminate_is_legitimate") is True, "INDETERMINATE must remain legitimate")
    _require(fail_closed.get("not_tested_is_legitimate") is True, "NOT_TESTED must remain legitimate")

    strategy = plan.get("family_strategy")
    _require(isinstance(strategy, Mapping), "family strategy required")
    _require(strategy.get("rule") == "ONE_RESEARCH_QUESTION_PER_BOUNDED_FALSIFICATION_FAMILY", "one-question-per-family rule drift")
    _require(strategy.get("giant_bpv2") == "FORBIDDEN_AS_DEFAULT", "giant BPV-2 must remain forbidden by default")
    _require(strategy.get("family_ids_are_planning_labels_not_frozen_experiment_identities") is True, "family labels must not become preregistered experiment identities")

    families = _family_map(plan)
    _validate_special_boundaries(plan, families)

    recommended = plan.get("recommended_order")
    _require(isinstance(recommended, list) and len(recommended) == 6, "recommended family order must contain six entries")
    _require(
        [item.get("hypothesis") for item in recommended if isinstance(item, Mapping)]
        == ["A10-H11", "A10-H03", "A10-H10", "A10-H06", "A10-H09", "A10-H08"],
        "recommended family order drift",
    )
    _require(plan.get("next_gate_after_plan") == "SEPARATE_FAMILY_PREREGISTRATION_SELECTION", "next planning gate drift")
    _require(plan.get("next_gate_execution_authorized") is False, "next gate must not authorize execution")

    _reject_execution_authority(plan)
    _validate_human_docs(repo)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        validate(args.repo)
    except ResidualA10PlanError as exc:
        print(f"Residual A10 plan validation failed: {exc}", file=sys.stderr)
        return 1
    print(
        "Residual A10 plan validation passed; targets=6; families=6; "
        "H11=LAB_CANON_SEPARATION; execution=NOT_AUTHORIZED; runtime=FROZEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
