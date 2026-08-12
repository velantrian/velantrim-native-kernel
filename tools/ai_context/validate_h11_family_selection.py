#!/usr/bin/env python3
"""Validate the bounded A10-H11 preregistration-selection candidate."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping

SELECTION_PATH = Path("docs/research/H11_FAMILY_SELECTION.json")
HUMAN_PATH = Path("docs/research/H11_FAMILY_SELECTION.md")
PLAN_PATH = Path("docs/research/RESIDUAL_A10_VALIDATION_PLAN.json")

PROTOCOL = "nk-residual-family-selection/1"
SELECTION_ID = "RFS-001-a10-h11-preregistration-selection-v1"
SOURCE_CHECKPOINT = "eeddda7382558f939f9bddb19ab80dd8dfbdbee4"
PLAN_ID = "RAVP-001-residual-a10-validation-plan-v1"
PLAN_MERGE = "edc0501d71a827462aafd1ac4497920a719a4519"
HYPOTHESIS = "A10-H11"
FAMILY_ID = "RAVP-H11-LAB-CANON-SEPARATION"
NEXT_GATE = "A10_H11_FAMILY_PREREGISTRATION"
PLAN_REASON = "Lowest execution burden and protects all later families from profile-to-Canon leakage."
REQUIRED_PREREG_FIELDS = {
    "experiment_identity",
    "historical_laboratory_checkpoint_and_evidence_identity",
    "exact_laboratory_reproduction_manifest",
    "architecture_obligation_inventory",
    "mechanism_dependency_graph",
    "frozen_mechanism_leakage_rubric",
    "externally_visible_observables",
    "equivalence_predicate",
    "allowed_losses",
    "failure_conditions",
    "hard_refutation",
    "grounding_mode",
    "threat_trust_model",
    "semantic_oracle_authority",
    "reviewer_reproducer_independence_basis",
    "reproduction_requirements",
    "allowed_a10_outcome_vocabulary",
}


class H11FamilySelectionError(ValueError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise H11FamilySelectionError(message)


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise H11FamilySelectionError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise H11FamilySelectionError(f"invalid JSON in {path}: {exc}") from exc
    _require(isinstance(value, dict), f"{path} root must be an object")
    return value


def _reject_authority(value: Any, path: str = "root") -> None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            child = f"{path}.{key}"
            lowered = key.lower()
            if "implementation_authorized" in lowered or "execution_authorized" in lowered:
                _require(item is False, f"{child} must remain false")
            _reject_authority(item, child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _reject_authority(item, f"{path}[{index}]")


def validate(repo: Path, selection_override: Mapping[str, Any] | None = None) -> None:
    repo = repo.resolve()
    selection = dict(selection_override) if selection_override is not None else _load(repo / SELECTION_PATH)
    plan = _load(repo / PLAN_PATH)

    _require(selection.get("protocol") == PROTOCOL, "selection protocol drift")
    _require(selection.get("selection_id") == SELECTION_ID, "selection identity drift")
    _require(selection.get("state") == "CANDIDATE_SELECTION / PREREGISTRATION_NOT_YET_AUTHORIZED", "selection package must remain non-self-authorizing")
    _require(selection.get("source_checkpoint_sha") == SOURCE_CHECKPOINT, "selection source checkpoint drift")
    _require(selection.get("selection_scope") == "PREREGISTRATION_SELECTION_ONLY", "selection scope drift")
    _require(selection.get("selected_hypothesis") == HYPOTHESIS, "only A10-H11 may be selected by this package")
    _require(selection.get("selected_family_id") == FAMILY_ID, "H11 family identity drift")
    _require(selection.get("selected_hypothesis_text") == "Laboratory mechanisms can remain reproducible without becoming Architecture Canon.", "H11 hypothesis text drift")

    source_plan = selection.get("source_plan")
    _require(isinstance(source_plan, Mapping), "source plan binding required")
    _require(source_plan.get("protocol") == "nk-residual-a10-validation-plan/1", "source plan protocol drift")
    _require(source_plan.get("plan_id") == PLAN_ID, "source plan identity drift")
    _require(source_plan.get("merge_sha") == PLAN_MERGE, "source plan merge drift")

    _require(plan.get("plan_id") == PLAN_ID, "live RAVP identity drift")
    families = plan.get("families")
    _require(isinstance(families, list), "RAVP family inventory required")
    h11 = next((item for item in families if isinstance(item, Mapping) and item.get("hypothesis_id") == HYPOTHESIS), None)
    _require(isinstance(h11, Mapping), "RAVP H11 family required")
    _require(h11.get("family_id") == FAMILY_ID, "RAVP H11 family id drift")
    _require(h11.get("hypothesis") == selection.get("selected_hypothesis_text"), "selection must preserve exact RAVP H11 hypothesis")

    order = plan.get("recommended_order")
    _require(isinstance(order, list) and bool(order), "RAVP recommended order required")
    first = order[0]
    _require(isinstance(first, Mapping) and first.get("hypothesis") == HYPOTHESIS and first.get("order") == 1, "H11 must remain first in RAVP recommended order")
    _require(first.get("reason") == PLAN_REASON, "H11 selection rationale must match frozen RAVP reason")

    basis = selection.get("selection_basis")
    _require(isinstance(basis, Mapping), "selection basis required")
    _require(basis.get("recommended_order_position") == 1, "selection order position drift")
    _require(basis.get("plan_reason") == PLAN_REASON, "selection plan reason drift")

    boundary = selection.get("h11_boundary")
    _require(isinstance(boundary, Mapping), "H11 boundary required")
    _require(boundary.get("definition") == "LABORATORY_MECHANISMS_REPRODUCIBLE_WITHOUT_BECOMING_ARCHITECTURE_CANON", "H11 boundary definition drift")
    _require(boundary.get("composition_federation_is_h11") is False, "composition/federation must remain separate from H11")
    _require(boundary.get("required_independence_axis") == ["INDEPENDENT_SEMANTIC_ORACLE"], "H11 required independence axis drift")

    prereg_fields = selection.get("preregistration_required_fields")
    _require(isinstance(prereg_fields, list), "preregistration field inventory required")
    _require(set(prereg_fields) == REQUIRED_PREREG_FIELDS, "H11 preregistration field inventory drift")
    _require(selection.get("next_gate_if_accepted") == NEXT_GATE, "H11 next gate drift")
    _require(selection.get("preregistration_authorized_by_this_package") is False, "selection package cannot self-authorize preregistration")
    _require(selection.get("experiment_implementation_authorized") is False, "H11 implementation must remain unauthorized")
    _require(selection.get("experiment_execution_authorized") is False, "H11 execution must remain unauthorized")
    _require(selection.get("runtime_expansion") == "FROZEN", "runtime expansion must remain frozen")
    _require(selection.get("product_runtime_thaw") is False, "product runtime thaw must remain false")
    _require(selection.get("production_authorized") is False, "production must remain unauthorized")
    _require("DEFERRED" in str(selection.get("final_canon")), "Final Canon must remain deferred")
    _reject_authority(selection)

    non_targets = selection.get("explicit_non_targets")
    _require(isinstance(non_targets, list), "explicit non-targets required")
    text = json.dumps(non_targets, ensure_ascii=False).lower()
    for marker in ("composition/federation", "implementation or execution", "final canon", "issue #18", "issue #74", "track h"):
        _require(marker in text, f"selection non-target boundary missing: {marker}")

    human = (repo / HUMAN_PATH).read_text(encoding="utf-8")
    for marker in (SELECTION_ID, SOURCE_CHECKPOINT, PLAN_ID, HYPOTHESIS, FAMILY_ID, NEXT_GATE, "preregistration_authorized_by_this_package: false", "experiment_execution_authorized: false", "A10-H11 ≠ composition/federation"):
        _require(marker in human, f"human selection document missing marker: {marker}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        validate(args.repo)
    except H11FamilySelectionError as exc:
        print(f"H11 family selection validation failed: {exc}", file=sys.stderr)
        return 1
    print("H11 family selection candidate valid; preregistration=false; implementation=false; execution=false; runtime=FROZEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
