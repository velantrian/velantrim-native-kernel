#!/usr/bin/env python3
"""Validate architecture boundaries after the blocked H11 execution-admission checkpoint."""
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
H11_SELECTION_MERGE = "bcd3b3f6c9d898315c93e5d24b5d0e02c95508cc"
H11_PLAN_MERGE = "4a75ff15542013c033030620bdff61997e365140"
H11_ADMISSION_MERGE = "f7d13fce0104a4c2ce67589e954b09365a82f36f"
H11_STATE_BINDING_MERGE = "e36b7f45410d74b8a65406bff6fdd6d070fa96b0"
H11_PLAN_SHA256 = "60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914"
H11_CURRENT_GATE = "A10_H11_EXECUTION_ADMISSION"
H11_PLAN_ID = "H11-001-c5-lab-canon-separation-v1"
H11_BLOCKER = "BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER"
H11_NEXT_DEPENDENCY = "IMPLEMENT_ADR0028_POSITIVE_QUALIFICATION_PATH_THEN_ESTABLISH_GENUINELY_EXTERNAL_CANDIDATE"
RESIDUAL_TARGETS = ["A10-H03", "A10-H06", "A10-H08", "A10-H09", "A10-H10", "A10-H11"]


def _pre_plan_view(state: Mapping[str, Any]) -> dict[str, Any]:
    """Project current blocked H11 state onto the ADR-0027/pre-RAVP guard."""
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
    notion["status"] = "SYNCED_THROUGH_DESCENDANT_CHECKPOINT"
    notion["decision_sync_status"] = "PENDING_READ_BACK_VERIFICATION"
    notion["surface_count"] = 7
    notion["read_back_verified_count"] = 3
    notion["new_pages_created"] = 0
    notion["scope"] = (
        "ADR-0027 / OD-POST-D8-001 at " + ADR0027_DECISION_MERGE
        + " is bound into GitHub current truth at " + ADR0027_TRUTH_SYNC_SHA
        + "; seven existing Notion surfaces were written, but read-back verification remains incomplete. "
        "Current next gate is RESIDUAL_A10_VALIDATION_PLAN in RESEARCH_PLANNING_ONLY scope; experiment execution is not authorized."
    )
    value["issues"]["88"]["meaning"] = (
        "Architecture Re-foundation A1-A10 remains provisional. ADR-0027 / OD-POST-D8-001 at "
        + ADR0027_DECISION_MERGE
        + " accepted the post-D8 decision. Final Canon is deferred. Runtime remains frozen. "
        "RESIDUAL_A10_VALIDATION_PLAN is the next RESEARCH_PLANNING_ONLY gate; experiment execution is not authorized."
    )
    return value


def _validate_current(state: Mapping[str, Any]) -> None:
    research = state["tracks"]["long_horizon_research"]
    _require(research.get("runtime_authorized") is False, "runtime authority must remain frozen")
    _require(research.get("status") == "ACTIVE / H11 EXECUTION ADMISSION BLOCKED / NO AUTOMATIC PROMOTION", "H11 blocked research status drift")
    ref = research["architecture_refoundation"]
    _require(ref.get("runtime_expansion_frozen") is True, "runtime expansion must remain frozen")
    _require(ref.get("next_content_slice") == H11_CURRENT_GATE, "next architecture validation gate drift")

    validation = research["post_blueprint_validation"]
    _require(validation.get("status") == "COMPLETE / H11_EXECUTION_ADMISSION_BLOCKED / NO_AUTOMATIC_PROMOTION", "H11 blocked validation status drift")
    _require(validation.get("product_runtime_thaw") is False, "product runtime thaw must remain false")
    _require(validation.get("automatic_canon_promotion") is False, "automatic Canon promotion must remain false")
    _require(validation.get("automatic_runtime_promotion") is False, "automatic runtime promotion must remain false")

    plan = validation.get("residual_a10_validation_plan")
    _require(isinstance(plan, Mapping), "RAVP-001 completion record required")
    _require(plan.get("merge_sha") == RESIDUAL_PLAN_MERGE, "RAVP-001 merge binding drift")
    _require(plan.get("families") == RESIDUAL_TARGETS, "residual family inventory drift")
    _require(plan.get("selected_family") == "A10-H11", "only H11 may be the selected residual family")
    _require(plan.get("selected_family_id") == "RAVP-H11-LAB-CANON-SEPARATION", "H11 family identity drift")
    _require(plan.get("family_preregistration_authorized") is True and plan.get("family_preregistration_complete") is True, "H11 preregistration binding drift")
    _require(plan.get("next_gate") == H11_CURRENT_GATE, "H11 current gate drift")
    _require(plan.get("next_gate_scope") == "EXECUTION_ADMISSION_ONLY", "H11 current gate scope drift")
    _require(plan.get("execution_admission_state") == H11_BLOCKER, "H11 execution admission blocker drift")
    _require(plan.get("next_dependency") == H11_NEXT_DEPENDENCY, "H11 next dependency drift")
    _require(plan.get("experiment_implementation_authorized") is False, "experiment implementation must remain unauthorized")
    _require(plan.get("experiment_execution_authorized") is False, "experiment execution must remain unauthorized")
    _require(plan.get("composition_federation_is_h11") is False, "composition/federation must remain distinct from H11")
    _require(plan.get("h11_definition") == "LABORATORY_MECHANISMS_REPRODUCIBLE_WITHOUT_BECOMING_ARCHITECTURE_CANON", "H11 definition drift")

    selection = plan.get("family_selection")
    _require(isinstance(selection, Mapping), "H11 selection binding required")
    _require(selection.get("merge_sha") == H11_SELECTION_MERGE, "H11 selection merge drift")
    _require(selection.get("preregistration_authorized_by_selection_package") is False, "H11 selection package cannot self-authorize preregistration")

    h11 = plan.get("h11_preregistration")
    _require(isinstance(h11, Mapping), "H11 preregistration current binding required")
    _require(h11.get("plan_id") == H11_PLAN_ID and h11.get("merge_sha") == H11_PLAN_MERGE, "H11 preregistration identity/merge drift")
    _require(h11.get("status") == "PREREGISTERED / EXECUTION_NOT_AUTHORIZED", "H11 preregistration status drift")
    _require(h11.get("required_oracle_class") == "INDEPENDENT_SEMANTIC_ORACLE", "H11 independent semantic oracle requirement drift")
    _require(h11.get("qualifying_reviewer_reproducer") == "NOT_ESTABLISHED / MUST_BE_VERIFIED_AT_EXECUTION_ADMISSION", "historical H11 preregistration reviewer status drift")
    _require(h11.get("no_qualifying_reviewer_outcome") == H11_BLOCKER, "H11 no-reviewer blocker drift")
    _require(h11.get("current_a10_outcome") == "NOT_TESTED", "H11 must remain NOT_TESTED")
    _require(h11.get("implementation_authorized") is False and h11.get("execution_authorized") is False, "H11 preregistration must not authorize execution")

    admission = plan.get("h11_execution_admission")
    _require(isinstance(admission, Mapping), "H11 execution admission current binding required")
    _require(admission.get("protocol") == "nk-h11-execution-admission/1", "H11 admission protocol drift")
    _require(admission.get("status") == "BLOCKED", "H11 admission must remain BLOCKED")
    _require(admission.get("admission_package_pr") == 129 and admission.get("admission_package_merge_sha") == H11_ADMISSION_MERGE, "H11 admission checkpoint drift")
    _require(admission.get("plan_merge_sha") == H11_PLAN_MERGE and admission.get("plan_sha256") == H11_PLAN_SHA256, "H11 frozen plan binding drift")
    _require(admission.get("admission_result") == H11_BLOCKER, "H11 blocked admission result drift")
    _require(admission.get("qualifying_reviewer_reproducer") == "NOT_ESTABLISHED", "H11 admission cannot fabricate reviewer independence")
    _require(admission.get("required_oracle_class") == "INDEPENDENT_SEMANTIC_ORACLE", "H11 required oracle drift")
    _require(admission.get("implementation_authorized") is False and admission.get("execution_authorized") is False, "blocked H11 admission cannot authorize implementation/execution")
    _require(admission.get("dependency_graph_execution_authorized") is False and admission.get("semantic_adjudication_authorized") is False, "blocked H11 admission cannot execute graph/adjudication")
    _require(admission.get("h11_outcome") == "NOT_TESTED", "blocked admission must not become INDETERMINATE or another A10 outcome")
    _require(admission.get("runtime_expansion") == "FROZEN" and admission.get("product_runtime_thaw") is False, "H11 admission cannot thaw runtime")
    _require(admission.get("final_canon") == "DEFERRED / NOT_AUTHORIZED", "H11 admission cannot promote Final Canon")
    _require(admission.get("production_authorized") is False, "H11 admission cannot authorize production")

    decision = validation.get("post_d8_operator_decision")
    _require(isinstance(decision, Mapping), "ADR-0027 decision record required")
    _require(decision.get("next_gate") == "RESIDUAL_A10_VALIDATION_PLAN", "historical ADR-0027 gate must remain unchanged")
    _require(decision.get("next_gate_scope") == "RESEARCH_PLANNING_ONLY", "historical ADR-0027 scope must remain unchanged")
    _require(decision.get("experiment_execution_authorized") is False, "ADR-0027 execution boundary drift")

    issue = state.get("issues", {}).get("88")
    _require(isinstance(issue, Mapping), "Issue #88 snapshot required")
    _require(issue.get("state") == "OPEN", "Issue #88 must remain open")
    meaning = str(issue.get("meaning", ""))
    for marker in ("A10-H11", H11_PLAN_ID, H11_ADMISSION_MERGE, H11_STATE_BINDING_MERGE, H11_CURRENT_GATE, H11_BLOCKER, "NOT_TESTED"):
        _require(marker in meaning, f"Option D selection/current Issue #88 blocked H11 truth missing: {marker}")
    verification = issue.get("verification")
    _require(isinstance(verification, Mapping), "Issue #88 verification required")
    _require(verification.get("status") == "VERIFIED" and verification.get("method") == "GITHUB_API" and verification.get("source") == "issue/88", "Issue #88 verification drift")

    _require(state["checkpoints"].get("notion_synchronized_through_sha") == H11_STATE_BINDING_MERGE, "H11 post-130 Notion checkpoint drift")
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
        "Architecture validation passed; H11 admission=BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER; "
        "H11=NOT_TESTED; reviewer=NOT_ESTABLISHED; execution=false; runtime_expansion_frozen=true"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
