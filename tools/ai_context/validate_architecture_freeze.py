#!/usr/bin/env python3
"""Validate architecture boundaries after completion of RAVP-001 planning."""
from __future__ import annotations

import copy
import sys
from pathlib import Path
from typing import Any, Mapping

_PRE_PLAN_PATH = Path(__file__).with_name("validate_architecture_freeze_post_adr0027.py")
_saved_name = __name__
globals()["__name__"] = "validate_architecture_freeze_post_adr0027_embedded"
exec(compile(_PRE_PLAN_PATH.read_text(encoding="utf-8"), str(_PRE_PLAN_PATH), "exec"), globals(), globals())
globals()["__name__"] = _saved_name
_PRE_PLAN_VALIDATE = validate

ADR0027_TRUTH_SYNC_SHA = "90bcb0fa2a3a2e85a590e9ba79746f3297b55457"
ADR0027_DECISION_MERGE = "57993f39906ae7266011f6146c9a485d0587d2bf"
RESIDUAL_PLAN_MERGE = "edc0501d71a827462aafd1ac4497920a719a4519"
NEXT_GATE = "SEPARATE_FAMILY_PREREGISTRATION_SELECTION"
RESIDUAL_TARGETS = ["A10-H03", "A10-H06", "A10-H08", "A10-H09", "A10-H10", "A10-H11"]


def _pre_plan_view(state: Mapping[str, Any]) -> dict[str, Any]:
    """Project current state onto the ADR-0027/pre-readback residual-planning guard."""
    value = copy.deepcopy(dict(state))
    value["checkpoints"]["notion_synchronized_through_sha"] = ADR0027_TRUTH_SYNC_SHA
    research = value["tracks"]["long_horizon_research"]
    research["status"] = "ACTIVE / POST-D8 RESIDUAL VALIDATION PLANNING / NO AUTOMATIC PROMOTION"
    ref = research["architecture_refoundation"]
    ref["status"] = "BLUEPRINT COMPLETE / PROVISIONAL / RESIDUAL VALIDATION PLANNING AUTHORIZED"
    ref["next_content_slice"] = "RESIDUAL_A10_VALIDATION_PLAN"
    validation = research["post_blueprint_validation"]
    validation["status"] = "COMPLETE / OPTION_D_OPERATOR_DECISION_ACCEPTED / RESIDUAL_VALIDATION_PLANNING_AUTHORIZED"
    validation.pop("residual_a10_validation_plan", None)
    notion = value["notion"]
    notion["synchronization_required"] = True
    notion["decision_sync_status"] = "PENDING_READ_BACK_VERIFICATION"
    notion["surface_count"] = 7
    notion["read_back_verified_count"] = 3
    notion["new_pages_created"] = 0
    notion["scope"] = (
        "ADR-0027 / OD-POST-D8-001 at "
        + ADR0027_DECISION_MERGE
        + " is bound into GitHub current truth at "
        + ADR0027_TRUTH_SYNC_SHA
        + "; seven existing Notion surfaces were written, but read-back verification remains incomplete. "
        "Current next gate is RESIDUAL_A10_VALIDATION_PLAN in RESEARCH_PLANNING_ONLY scope; experiment execution is not authorized."
    )
    value["issues"]["88"]["meaning"] = (
        "Architecture Re-foundation A1-A10 remains provisional. ADR-0027 / OD-POST-D8-001 at "
        + ADR0027_DECISION_MERGE
        + " accepted the post-D8 decision, keeps Final Canon deferred, and keeps runtime frozen. "
        "RESIDUAL_A10_VALIDATION_PLAN is the next RESEARCH_PLANNING_ONLY gate; experiment execution is not authorized."
    )
    return value


def _validate_current(state: Mapping[str, Any]) -> None:
    research = state["tracks"]["long_horizon_research"]
    _require(research.get("runtime_authorized") is False, "runtime authority must remain frozen")
    ref = research["architecture_refoundation"]
    _require(ref.get("runtime_expansion_frozen") is True, "runtime expansion must remain frozen")
    _require(ref.get("next_content_slice") == NEXT_GATE, "post-plan architecture gate drift")
    validation = research["post_blueprint_validation"]
    _require(validation.get("product_runtime_thaw") is False, "product runtime thaw must remain false")
    _require(validation.get("automatic_canon_promotion") is False, "automatic Canon promotion must remain false")
    _require(validation.get("automatic_runtime_promotion") is False, "automatic runtime promotion must remain false")

    plan = validation.get("residual_a10_validation_plan")
    _require(isinstance(plan, Mapping), "RAVP-001 completion record required")
    _require(plan.get("merge_sha") == RESIDUAL_PLAN_MERGE, "RAVP-001 merge binding drift")
    _require(plan.get("families") == RESIDUAL_TARGETS, "residual family inventory drift")
    _require(plan.get("selected_family") is None, "no family may be silently selected")
    _require(plan.get("next_gate") == NEXT_GATE, "RAVP-001 next gate drift")
    _require(plan.get("next_gate_scope") == "PREREGISTRATION_SELECTION_ONLY", "next gate scope drift")
    _require(plan.get("family_preregistration_authorized") is False, "family preregistration must remain unauthorized")
    _require(plan.get("experiment_implementation_authorized") is False, "experiment implementation must remain unauthorized")
    _require(plan.get("experiment_execution_authorized") is False, "experiment execution must remain unauthorized")
    _require(plan.get("composition_federation_is_h11") is False, "composition/federation must remain distinct from H11")
    _require(
        plan.get("h11_definition") == "LABORATORY_MECHANISMS_REPRODUCIBLE_WITHOUT_BECOMING_ARCHITECTURE_CANON",
        "H11 definition drift",
    )

    decision = validation.get("post_d8_operator_decision")
    _require(isinstance(decision, Mapping), "ADR-0027 decision record required")
    _require(decision.get("next_gate") == "RESIDUAL_A10_VALIDATION_PLAN", "historical ADR-0027 gate must remain unchanged")
    _require(decision.get("next_gate_scope") == "RESEARCH_PLANNING_ONLY", "historical ADR-0027 scope must remain unchanged")
    _require(decision.get("experiment_execution_authorized") is False, "ADR-0027 execution boundary drift")

    _require(state["checkpoints"].get("notion_synchronized_through_sha") == RESIDUAL_PLAN_MERGE, "post-plan Notion checkpoint drift")
    _require(state["status"]["production_authorized"] is False, "production must remain unauthorized")


def validate(state: Mapping[str, Any], *, repo: Path) -> None:
    _PRE_PLAN_VALIDATE(_pre_plan_view(state), repo=repo)
    _validate_current(state)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", nargs="?", type=Path, default=Path("project-state.json"))
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    state_path = args.state if args.state.is_absolute() else repo / args.state
    try:
        validate(_load(state_path), repo=repo)
    except ArchitectureFreezeError as exc:
        print(f"Architecture validation boundary failed: {exc}", file=sys.stderr)
        return 1
    print(
        "Architecture validation passed; RAVP-001=COMPLETE; "
        "next=SEPARATE_FAMILY_PREREGISTRATION_SELECTION; selected_family=NONE; "
        "preregistration=false; execution=false; runtime_expansion_frozen=true"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
