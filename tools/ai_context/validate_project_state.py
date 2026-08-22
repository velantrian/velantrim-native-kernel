#!/usr/bin/env python3
"""Validate current truth after the fail-closed H11 execution-admission checkpoint."""
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
ADR0028_DECISION_MERGE = "4a13d2b4ee8001a43f7e3e701dbe9025dbcfd0df"
ADR0028_RECONCILIATION_MERGE = "5ebb33f5a74a81a7a49dae36ed29247d9b71db87"
ADR0028_NOTION_DECISION_STATUS = "COMPLETE / READ_BACK_VERIFIED"
D8_NOTION_SYNC_SHA = "491ff7b229606d228ca04985b19b146878390e08"
RESIDUAL_PLAN_MERGE = "edc0501d71a827462aafd1ac4497920a719a4519"
RESIDUAL_PLAN_HEAD = "918ac46f4d93f085171b03564f9fbe30f543b200"
RESIDUAL_PLAN_ID = "RAVP-001-residual-a10-validation-plan-v1"
RESIDUAL_TARGETS = ["A10-H03", "A10-H06", "A10-H08", "A10-H09", "A10-H10", "A10-H11"]
RECOMMENDED_ORDER = ["A10-H11", "A10-H03", "A10-H10", "A10-H06", "A10-H09", "A10-H08"]
H11_SELECTION_ID = "RFS-001-a10-h11-preregistration-selection-v1"
H11_SELECTION_HEAD = "d9273a22c411467109112f1fc6ea263ed8819d1d"
H11_SELECTION_MERGE = "bcd3b3f6c9d898315c93e5d24b5d0e02c95508cc"
H11_PLAN_ID = "H11-001-c5-lab-canon-separation-v1"
H11_PLAN_HEAD = "1dca13cdd2759c70d810f44977a227fe1147d4bb"
H11_PLAN_MERGE = "4a75ff15542013c033030620bdff61997e365140"
H11_PLAN_SHA256 = "60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914"
H11_ADMISSION_PR = 129
H11_ADMISSION_MERGE = "f7d13fce0104a4c2ce67589e954b09365a82f36f"
H11_STATE_BINDING_PR = 130
H11_STATE_BINDING_MERGE = "e36b7f45410d74b8a65406bff6fdd6d070fa96b0"
H11_FAMILY_ID = "RAVP-H11-LAB-CANON-SEPARATION"
H11_CURRENT_GATE = "A10_H11_EXECUTION_ADMISSION"
H11_BLOCKER = "BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER"
H11_NEXT_DEPENDENCY = "IMPLEMENT_ADR0028_POSITIVE_QUALIFICATION_PATH_THEN_ESTABLISH_GENUINELY_EXTERNAL_CANDIDATE"
H11_BUNDLE = "native-kernel/c5/2026-08-08-adr0023"


def _pre_plan_view(state: Mapping[str, Any]) -> dict[str, Any]:
    """Project current H11 state onto the preserved post-ADR-0027/pre-RAVP layer."""
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
    notion["status"] = "SYNCED_THROUGH_DESCENDANT_CHECKPOINT"
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
        _require(notion_checkpoint == publication, "publication synchronization status requires equal checkpoints")
    elif notion_status == "SYNCED_THROUGH_DESCENDANT_CHECKPOINT":
        _require(notion_checkpoint != publication, "descendant synchronization status requires distinct checkpoints")
    else:
        _require(False, "Notion status drift")
    _require(notion_checkpoint == H11_STATE_BINDING_MERGE, "H11 post-130 Notion synchronization checkpoint drift")

    research = state["tracks"]["long_horizon_research"]
    _require(research.get("status") == "ACTIVE / H11 EXECUTION ADMISSION BLOCKED / NO AUTOMATIC PROMOTION", "H11 blocked-admission research status drift")
    _require(research.get("runtime_authorized") is False, "runtime authority must remain frozen")
    ref = research["architecture_refoundation"]
    _require(ref.get("runtime_expansion_frozen") is True, "runtime expansion freeze must remain active")
    _require(ref.get("next_content_slice") == H11_CURRENT_GATE, "H11 current architecture validation gate drift")

    validation = research["post_blueprint_validation"]
    _require(validation.get("status") == "COMPLETE / H11_EXECUTION_ADMISSION_BLOCKED / NO_AUTOMATIC_PROMOTION", "H11 blocked-admission post-blueprint validation status drift")
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
    _require(plan.get("pr") == 124 and plan.get("exact_head_sha") == RESIDUAL_PLAN_HEAD and plan.get("merge_sha") == RESIDUAL_PLAN_MERGE, "residual plan immutable checkpoint drift")
    _require(plan.get("exact_head_triggered_workflows") == 6 and plan.get("exact_head_successful_workflows") == 6, "residual plan exact-head CI drift")
    _require(plan.get("post_merge_triggered_workflows") == 6 and plan.get("post_merge_successful_workflows") == 6, "residual plan post-merge CI drift")
    _require(plan.get("notion_surface_count") == 7 and plan.get("notion_read_back_verified_count") == 7 and plan.get("new_notion_pages_created") == 0, "residual plan historical Notion 7/7 drift")
    _require(plan.get("families") == RESIDUAL_TARGETS, "residual family inventory drift")
    _require(plan.get("recommended_order") == RECOMMENDED_ORDER, "residual recommended order drift")
    _require(plan.get("h11_definition") == "LABORATORY_MECHANISMS_REPRODUCIBLE_WITHOUT_BECOMING_ARCHITECTURE_CANON", "H11 definition drift")
    _require(plan.get("composition_federation_is_h11") is False, "composition/federation must remain separate from H11")
    _require(plan.get("selected_family") == "A10-H11", "selected family drift: only A10-H11 is current")
    _require(plan.get("selected_family_id") == H11_FAMILY_ID, "selected H11 family identity drift")
    _require(plan.get("family_preregistration_authorized") is True, "H11 preregistration current binding drift")
    _require(plan.get("family_preregistration_complete") is True, "H11 preregistration completion drift")
    _require(plan.get("next_gate") == H11_CURRENT_GATE, "H11 current gate drift")
    _require(plan.get("next_gate_scope") == "EXECUTION_ADMISSION_ONLY", "H11 current gate scope drift")
    _require(plan.get("execution_admission_state") == H11_BLOCKER, "H11 execution-admission state drift")
    _require(plan.get("next_dependency") == H11_NEXT_DEPENDENCY, "H11 next dependency drift")
    _require(plan.get("experiment_implementation_authorized") is False, "H11 implementation must remain unauthorized")
    _require(plan.get("experiment_execution_authorized") is False, "H11 execution must remain unauthorized")

    selection = plan.get("family_selection")
    _require(isinstance(selection, Mapping), "H11 family selection binding required")
    _require(selection.get("protocol") == "nk-residual-family-selection/1", "H11 selection protocol drift")
    _require(selection.get("selection_id") == H11_SELECTION_ID, "H11 selection identity drift")
    _require(selection.get("pr") == 126 and selection.get("exact_head_sha") == H11_SELECTION_HEAD and selection.get("merge_sha") == H11_SELECTION_MERGE, "H11 selection checkpoint drift")
    _require(selection.get("selected_hypothesis") == "A10-H11" and selection.get("selected_family_id") == H11_FAMILY_ID, "H11 selection target drift")
    _require(selection.get("preregistration_authorized_by_selection_package") is False, "selection package must remain non-self-authorizing")

    h11 = plan.get("h11_preregistration")
    _require(isinstance(h11, Mapping), "H11 preregistration binding required")
    _require(h11.get("protocol") == "nk-h11-preregistration/1", "H11 preregistration protocol drift")
    _require(h11.get("plan_id") == H11_PLAN_ID, "H11 preregistration plan identity drift")
    _require(h11.get("status") == "PREREGISTERED / EXECUTION_NOT_AUTHORIZED", "H11 preregistration status drift")
    _require(h11.get("pr") == 127 and h11.get("exact_head_sha") == H11_PLAN_HEAD and h11.get("merge_sha") == H11_PLAN_MERGE, "H11 preregistration checkpoint drift")
    _require(h11.get("exact_head_successful_workflows") == 6 and h11.get("post_merge_successful_workflows") == 6, "H11 preregistration CI drift")
    _require(h11.get("notion_read_back_verified_count") == 7 and h11.get("new_notion_pages_created") == 0, "H11 preregistration Notion 7/7 drift")
    _require(h11.get("frozen_laboratory_bundle") == H11_BUNDLE, "H11 frozen laboratory bundle drift")
    _require(h11.get("required_oracle_class") == "INDEPENDENT_SEMANTIC_ORACLE", "H11 oracle independence drift")
    _require(h11.get("qualifying_reviewer_reproducer") == "NOT_ESTABLISHED / MUST_BE_VERIFIED_AT_EXECUTION_ADMISSION", "historical H11 preregistration reviewer status drift")
    _require(h11.get("no_qualifying_reviewer_outcome") == H11_BLOCKER, "H11 preregistration no-reviewer blocker drift")
    _require(h11.get("current_a10_outcome") == "NOT_TESTED", "H11 must remain NOT_TESTED")
    _require(h11.get("implementation_authorized") is False and h11.get("execution_authorized") is False, "H11 preregistration cannot authorize execution")
    _require(h11.get("next_gate") == H11_CURRENT_GATE, "H11 preregistration historical next gate drift")

    admission = plan.get("h11_execution_admission")
    _require(isinstance(admission, Mapping), "H11 execution-admission current binding required")
    _require(admission.get("protocol") == "nk-h11-execution-admission/1", "H11 execution-admission protocol drift")
    _require(admission.get("admission_id") == "H11-001-execution-admission-v1", "H11 execution-admission identity drift")
    _require(admission.get("status") == "BLOCKED", "H11 execution admission must remain BLOCKED")
    _require(admission.get("admission_package_pr") == H11_ADMISSION_PR and admission.get("admission_package_merge_sha") == H11_ADMISSION_MERGE, "H11 admission package checkpoint drift")
    _require(admission.get("plan_merge_sha") == H11_PLAN_MERGE and admission.get("plan_sha256") == H11_PLAN_SHA256, "H11 frozen plan binding drift")
    _require(admission.get("admission_result") == H11_BLOCKER, "H11 admission blocker drift")
    _require(admission.get("qualifying_reviewer_reproducer") == "NOT_ESTABLISHED", "H11 admission cannot fabricate a qualifying reviewer/reproducer")
    _require(admission.get("required_oracle_class") == "INDEPENDENT_SEMANTIC_ORACLE", "H11 admission required oracle drift")
    _require(admission.get("implementation_authorized") is False and admission.get("execution_authorized") is False, "H11 blocked admission cannot authorize implementation/execution")
    _require(admission.get("dependency_graph_execution_authorized") is False, "H11 dependency-graph execution must remain unauthorized")
    _require(admission.get("semantic_adjudication_authorized") is False, "H11 semantic adjudication must remain unauthorized")
    _require(admission.get("h11_outcome") == "NOT_TESTED", "H11 blocked admission is not an A10 outcome")
    _require(admission.get("runtime_expansion") == "FROZEN" and admission.get("product_runtime_thaw") is False, "H11 admission cannot thaw runtime")
    _require(admission.get("final_canon") == "DEFERRED / NOT_AUTHORIZED", "H11 admission cannot promote Final Canon")
    _require(admission.get("production_authorized") is False, "H11 admission cannot authorize production")

    _require(notion.get("surface_count") == 8 and notion.get("read_back_verified_count") == 8 and notion.get("new_pages_created") == 0, "ADR-0028 Notion 8/8 read-back drift")
    _require(notion.get("synchronization_required") is False, "ADR-0028 Notion sync must be complete")
    _require(notion.get("decision_sync_status") == ADR0028_NOTION_DECISION_STATUS, "ADR-0028 Notion sync status drift")
    scope = str(notion.get("scope", ""))
    for marker in (ADR0028_DECISION_MERGE, ADR0028_RECONCILIATION_MERGE, "Eight existing Native Kernel Notion projections", "zero new pages", "H11 admission remains BLOCKED", "NOT_ESTABLISHED", "NOT_TESTED", "FROZEN"):
        _require(marker in scope, f"ADR-0028 completed Notion scope missing marker: {marker}")

    issue = state.get("issues", {}).get("88")
    _require(isinstance(issue, Mapping) and issue.get("state") == "OPEN", "Issue #88 must remain OPEN")
    meaning = str(issue.get("meaning", ""))
    for marker in ("Architecture Re-foundation A1-A10 remains provisional", H11_CURRENT_GATE, H11_BLOCKER, "ADR-0028", "OPTION_C_HYBRID_TWO_BASIS", "NOT_STARTED", "NOT_ESTABLISHED", "NOT_TESTED", "Final Canon is deferred", "runtime remains frozen"):
        _require(marker in meaning, f"Issue #88 ADR-0028/current H11 meaning missing marker: {marker}")

    evidence = state.get("evidence", {})
    admission_evidence = evidence.get("h11_execution_admission")
    _require(isinstance(admission_evidence, Mapping), "H11 execution-admission evidence binding required")
    _require(admission_evidence.get("path") == "docs/research/H11_EXECUTION_ADMISSION.json", "H11 admission evidence path drift")
    _require(admission_evidence.get("merge_sha") == H11_ADMISSION_MERGE, "H11 admission evidence merge drift")
    _require(admission_evidence.get("admission_result") == H11_BLOCKER, "H11 admission evidence blocker drift")
    _require(admission_evidence.get("h11_outcome") == "NOT_TESTED", "H11 admission evidence must preserve NOT_TESTED")
    _require(state["status"]["production_authorized"] is False, "production must remain unauthorized")


def validate(state: Mapping[str, Any], *, repo: Path, registry: Mapping[str, Any] | None = None, check_git: bool = True) -> None:
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
    print("Project-state validation passed; ADR-0028=OPTION_C_HYBRID_TWO_BASIS; H11 admission=BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER; H11=NOT_TESTED; reviewer=NOT_ESTABLISHED; execution=NOT_AUTHORIZED; runtime=FROZEN; Notion=READ_BACK_VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
