#!/usr/bin/env python3
"""Validate current truth after completion and Notion sync of RAVP-001."""
from __future__ import annotations

import copy
from pathlib import Path
from typing import Any, Mapping

_PRE_PLAN_PATH = Path(__file__).with_name("validate_project_state_post_adr0027.py")
_saved_name = __name__
globals()["__name__"] = "validate_project_state_post_adr0027_embedded"
exec(compile(_PRE_PLAN_PATH.read_text(encoding="utf-8"), str(_PRE_PLAN_PATH), "exec"), globals(), globals())
globals()["__name__"] = _saved_name
_PRE_PLAN_VALIDATE = validate

ADR0027_DECISION_MERGE = "57993f39906ae7266011f6146c9a485d0587d2bf"
ADR0027_GITHUB_TRUTH_SHA = "90bcb0fa2a3a2e85a590e9ba79746f3297b55457"
D8_NOTION_SYNC_SHA = "491ff7b229606d228ca04985b19b146878390e08"
RESIDUAL_PLAN_MERGE = "edc0501d71a827462aafd1ac4497920a719a4519"
RESIDUAL_PLAN_HEAD = "918ac46f4d93f085171b03564f9fbe30f543b200"
RESIDUAL_PLAN_ID = "RAVP-001-residual-a10-validation-plan-v1"
RESIDUAL_TARGETS = ["A10-H03", "A10-H06", "A10-H08", "A10-H09", "A10-H10", "A10-H11"]
RECOMMENDED_ORDER = ["A10-H11", "A10-H03", "A10-H10", "A10-H06", "A10-H09", "A10-H08"]
NEXT_GATE = "SEPARATE_FAMILY_PREREGISTRATION_SELECTION"


def _pre_plan_view(state: Mapping[str, Any]) -> dict[str, Any]:
    """Project current state onto the preserved post-ADR-0027/pre-readback layer."""
    value = copy.deepcopy(dict(state))
    value["checkpoints"]["notion_synchronized_through_sha"] = D8_NOTION_SYNC_SHA
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
    notion.pop("decision_sync_status", None)
    notion.pop("surface_count", None)
    notion.pop("read_back_verified_count", None)
    notion.pop("new_pages_created", None)
    notion["scope"] = (
        "ADR-0027 / OD-POST-D8-001 decision merge " + ADR0027_DECISION_MERGE
        + " is bound in GitHub truth; Notion synchronization/read-back is pending."
    )
    return value


def _validate_current(state: Mapping[str, Any]) -> None:
    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, Mapping), "checkpoint inventory required")
    publication = checkpoints.get("publication_checkpoint_sha")
    notion_checkpoint = checkpoints.get("notion_synchronized_through_sha")

    notion = state.get("notion")
    _require(isinstance(notion, Mapping), "Notion synchronization state required")
    notion_status = notion.get("status")
    if notion_status == "SYNCED_THROUGH_PUBLICATION_CHECKPOINT":
        _require(
            notion_checkpoint == publication,
            "publication synchronization status requires equal checkpoints",
        )
    elif notion_status == "SYNCED_THROUGH_DESCENDANT_CHECKPOINT":
        _require(
            notion_checkpoint != publication,
            "descendant synchronization status requires distinct checkpoints",
        )
    else:
        _require(False, "Notion status drift")

    _require(
        notion_checkpoint == RESIDUAL_PLAN_MERGE,
        "Residual A10 plan Notion synchronization checkpoint drift",
    )

    research = state["tracks"]["long_horizon_research"]
    _require(
        research.get("status") == "ACTIVE / RESIDUAL A10 PLAN COMPLETE / PREREGISTRATION FAMILY SELECTION NEXT / NO AUTOMATIC PROMOTION",
        "post-plan research status drift",
    )
    _require(research.get("runtime_authorized") is False, "runtime authority must remain frozen")
    ref = research["architecture_refoundation"]
    _require(ref.get("runtime_expansion_frozen") is True, "runtime expansion freeze must remain active")
    _require(ref.get("next_content_slice") == NEXT_GATE, "post-plan next gate drift")

    validation = research["post_blueprint_validation"]
    _require(
        validation.get("status") == "COMPLETE / RESIDUAL_A10_VALIDATION_PLAN_COMPLETE / PREREGISTRATION_SELECTION_NEXT",
        "post-plan validation status drift",
    )
    _require(validation.get("product_runtime_thaw") is False, "product runtime thaw must remain false")
    _require(validation.get("automatic_canon_promotion") is False, "automatic Canon promotion must remain false")
    _require(validation.get("automatic_runtime_promotion") is False, "automatic runtime promotion must remain false")

    decision = validation.get("post_d8_operator_decision")
    _require(isinstance(decision, Mapping), "ADR-0027 decision record required")
    _require(decision.get("decision_merge_sha") == ADR0027_DECISION_MERGE, "ADR-0027 merge binding drift")
    _require(decision.get("next_gate") == "RESIDUAL_A10_VALIDATION_PLAN", "historical ADR-0027 authorization drift")
    _require(decision.get("next_gate_scope") == "RESEARCH_PLANNING_ONLY", "historical ADR-0027 scope drift")
    _require(decision.get("experiment_execution_authorized") is False, "ADR-0027 execution boundary drift")
    _require(decision.get("residual_validation_targets") == RESIDUAL_TARGETS, "ADR-0027 residual target drift")

    plan = validation.get("residual_a10_validation_plan")
    _require(isinstance(plan, Mapping), "completed residual A10 plan record required")
    _require(plan.get("protocol") == "nk-residual-a10-validation-plan/1", "residual plan protocol drift")
    _require(plan.get("plan_id") == RESIDUAL_PLAN_ID, "residual plan identity drift")
    _require(plan.get("status") == "COMPLETE / MERGED / NOTION_7_OF_7_READ_BACK_VERIFIED", "residual plan status drift")
    _require(plan.get("pr") == 124, "residual plan PR drift")
    _require(plan.get("exact_head_sha") == RESIDUAL_PLAN_HEAD, "residual plan exact-head drift")
    _require(plan.get("merge_sha") == RESIDUAL_PLAN_MERGE, "residual plan merge drift")
    _require(plan.get("exact_head_triggered_workflows") == 6 and plan.get("exact_head_successful_workflows") == 6, "residual plan exact-head CI drift")
    _require(plan.get("post_merge_triggered_workflows") == 6 and plan.get("post_merge_successful_workflows") == 6, "residual plan post-merge CI drift")
    _require(plan.get("notion_surface_count") == 7 and plan.get("notion_read_back_verified_count") == 7 and plan.get("new_notion_pages_created") == 0, "residual plan Notion 7/7 drift")
    _require(plan.get("families") == RESIDUAL_TARGETS, "residual family inventory drift")
    _require(plan.get("recommended_order") == RECOMMENDED_ORDER, "residual recommended order drift")
    _require(plan.get("h11_definition") == "LABORATORY_MECHANISMS_REPRODUCIBLE_WITHOUT_BECOMING_ARCHITECTURE_CANON", "H11 definition drift")
    _require(plan.get("composition_federation_is_h11") is False, "composition/federation must remain separate from H11")
    _require(plan.get("selected_family") is None, "no residual family may be silently selected by sync")
    _require(plan.get("next_gate") == NEXT_GATE, "residual plan next gate drift")
    _require(plan.get("next_gate_scope") == "PREREGISTRATION_SELECTION_ONLY", "next gate scope drift")
    _require(plan.get("family_preregistration_authorized") is False, "family preregistration must not be auto-authorized")
    _require(plan.get("experiment_implementation_authorized") is False, "residual experiment implementation must remain unauthorized")
    _require(plan.get("experiment_execution_authorized") is False, "residual experiment execution must remain unauthorized")

    _require(notion.get("synchronization_required") is False, "Notion sync must be complete")
    _require(notion.get("decision_sync_status") == "SYNCHRONIZED", "Notion sync status drift")
    _require(notion.get("surface_count") == 7 and notion.get("read_back_verified_count") == 7 and notion.get("new_pages_created") == 0, "Notion 7/7 read-back drift")
    scope = str(notion.get("scope", ""))
    for marker in (RESIDUAL_PLAN_MERGE, RESIDUAL_PLAN_ID, "7/7", NEXT_GATE, "No family preregistration", "experiment execution"):
        _require(marker in scope, f"Notion current scope missing marker: {marker}")

    issue = state.get("issues", {}).get("88")
    _require(isinstance(issue, Mapping) and issue.get("state") == "OPEN", "Issue #88 must remain OPEN")
    meaning = str(issue.get("meaning", ""))
    for marker in ("RAVP-001", RESIDUAL_PLAN_MERGE, NEXT_GATE, "Final Canon is deferred", "runtime remains frozen"):
        _require(marker in meaning, f"Issue #88 current meaning missing marker: {marker}")

    _require(state["status"]["production_authorized"] is False, "production must remain unauthorized")


def validate(
    state: Mapping[str, Any],
    *,
    repo: Path,
    registry: Mapping[str, Any] | None = None,
    check_git: bool = True,
) -> None:
    _validate_current(state)
    _PRE_PLAN_VALIDATE(_pre_plan_view(state), repo=repo, registry=registry, check_git=check_git)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", nargs="?", type=Path, default=Path("project-state.json"))
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--no-git", action="store_true")
    args = parser.parse_args()
    repo = args.repo.resolve()
    state_path = args.state if args.state.is_absolute() else repo / args.state
    state = _load(state_path, "project state")
    validate(state, repo=repo, check_git=not args.no_git)
    print(
        "Project-state validation passed; RAVP-001=COMPLETE; Notion=7/7; "
        "next=SEPARATE_FAMILY_PREREGISTRATION_SELECTION; selected_family=NONE; "
        "preregistration=NOT_AUTHORIZED; execution=NOT_AUTHORIZED; runtime=FROZEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
