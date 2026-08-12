#!/usr/bin/env python3
"""Validate H11 current reconciliation over preserved D8/history guards."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping

_D8_PATH = Path(__file__).with_name("validate_reconciliation_d8.py")
_saved = __name__
globals()["__name__"] = "validate_reconciliation_d8_embedded"
exec(compile(_D8_PATH.read_text(encoding="utf-8"), str(_D8_PATH), "exec"), globals(), globals())
globals()["__name__"] = _saved
_D8_VALIDATE = validate

H11_TRUTH_SYNC_SHA = "4a75ff15542013c033030620bdff61997e365140"
PRE_PLAN_ADR0027_TRUTH_SYNC_SHA = "90bcb0fa2a3a2e85a590e9ba79746f3297b55457"
RESIDUAL_PLAN_MERGE = "edc0501d71a827462aafd1ac4497920a719a4519"
RESIDUAL_PLAN_ID = "RAVP-001-residual-a10-validation-plan-v1"
RESIDUAL_PLAN_HEAD = "918ac46f4d93f085171b03564f9fbe30f543b200"
H11_SELECTION_MERGE = "bcd3b3f6c9d898315c93e5d24b5d0e02c95508cc"
H11_PLAN_ID = "H11-001-c5-lab-canon-separation-v1"
H11_PLAN_HEAD = "1dca13cdd2759c70d810f44977a227fe1147d4bb"
H11_NEXT_GATE = "A10_H11_EXECUTION_ADMISSION"
H11_BLOCKER = "BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER"
CURRENT_MARKER = "POST_H11_PREREGISTRATION_CURRENT"
CURRENT_TRUTH_SURFACES = ("AGENTS.md", "docs/ai/POST_RESIDUAL_A10_STATE.md")


def _d8_repo_view(repo: Path) -> None:
    """Validate immutable D8 chronology through a temporary state projection."""
    state_path = repo / "project-state.json"
    state = _load_json(state_path)
    original = state_path.read_text(encoding="utf-8")
    state["checkpoints"]["notion_synchronized_through_sha"] = D8_NOTION_SYNC_SHA
    notion = state["notion"]
    notion["synchronization_required"] = False
    notion["status"] = "SYNCED_THROUGH_DESCENDANT_CHECKPOINT"
    notion["scope"] = (
        "Publication checkpoint " + PUBLICATION_SHA
        + ", manifest source " + NOTION_SYNC_SHA
        + ", D8 Notion synchronization checkpoint " + D8_NOTION_SYNC_SHA
        + ", and D8 consolidated record merge " + D8_RECORD_MERGE_SHA
        + " remain distinct historical roles."
    )
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        _D8_VALIDATE(repo)
    finally:
        state_path.write_text(original, encoding="utf-8")


def validate(repo: Path) -> None:
    _d8_repo_view(repo)
    state = _load_json(repo / "project-state.json")

    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, Mapping), "checkpoint inventory required")
    _require(checkpoints.get("notion_synchronized_through_sha") == H11_TRUTH_SYNC_SHA, "H11 Notion synchronization checkpoint drift")

    notion = state.get("notion")
    _require(isinstance(notion, Mapping), "Notion state required")
    _require(notion.get("synchronization_required") is False, "H11 Notion synchronization must be complete")
    _require(notion.get("decision_sync_status") == "SYNCHRONIZED", "H11 Notion synchronization status drift")
    _require(notion.get("surface_count") == 7 and notion.get("read_back_verified_count") == 7 and notion.get("new_pages_created") == 0, "H11 Notion read-back must remain 7/7 with zero new pages")
    scope = str(notion.get("scope", ""))
    for marker in (H11_TRUTH_SYNC_SHA, H11_PLAN_ID, "7/7", H11_NEXT_GATE, "NOT_ESTABLISHED", "NOT_TESTED"):
        _require(marker in scope, f"Notion scope missing H11 marker: {marker}")

    validation = state["tracks"]["long_horizon_research"]["post_blueprint_validation"]
    decision = validation.get("post_d8_operator_decision")
    _require(isinstance(decision, Mapping), "ADR-0027 decision record required")
    _require(decision.get("next_gate") == "RESIDUAL_A10_VALIDATION_PLAN", "historical ADR-0027 next gate drift")
    _require(decision.get("experiment_execution_authorized") is False, "historical ADR-0027 execution boundary drift")

    plan = validation.get("residual_a10_validation_plan")
    _require(isinstance(plan, Mapping), "RAVP-001 current result required")
    _require(plan.get("plan_id") == RESIDUAL_PLAN_ID, "RAVP-001 identity drift")
    _require(plan.get("exact_head_sha") == RESIDUAL_PLAN_HEAD, "RAVP-001 exact-head drift")
    _require(plan.get("merge_sha") == RESIDUAL_PLAN_MERGE, "RAVP-001 historical merge binding drift")
    _require(plan.get("notion_read_back_verified_count") == 7, "RAVP-001 historical Notion read-back drift")
    _require(plan.get("selected_family") == "A10-H11", "H11 must be the current selected family")
    _require(plan.get("next_gate") == H11_NEXT_GATE, "H11 current next gate drift")
    _require(plan.get("next_gate_scope") == "EXECUTION_ADMISSION_ONLY", "H11 current gate scope drift")
    _require(plan.get("family_preregistration_authorized") is True and plan.get("family_preregistration_complete") is True, "H11 preregistration binding drift")
    _require(plan.get("experiment_implementation_authorized") is False, "H11 experiment implementation must remain unauthorized")
    _require(plan.get("experiment_execution_authorized") is False, "H11 experiment execution must remain unauthorized")

    selection = plan.get("family_selection")
    _require(isinstance(selection, Mapping) and selection.get("merge_sha") == H11_SELECTION_MERGE, "H11 selection binding drift")
    _require(selection.get("preregistration_authorized_by_selection_package") is False, "selection package self-authorization boundary drift")

    h11 = plan.get("h11_preregistration")
    _require(isinstance(h11, Mapping), "H11 preregistration current record required")
    _require(h11.get("plan_id") == H11_PLAN_ID and h11.get("exact_head_sha") == H11_PLAN_HEAD and h11.get("merge_sha") == H11_TRUTH_SYNC_SHA, "H11 preregistration checkpoint drift")
    _require(h11.get("status") == "PREREGISTERED / EXECUTION_NOT_AUTHORIZED", "H11 preregistration status drift")
    _require(h11.get("qualifying_reviewer_reproducer") == "NOT_ESTABLISHED / MUST_BE_VERIFIED_AT_EXECUTION_ADMISSION", "H11 reviewer status drift")
    _require(h11.get("no_qualifying_reviewer_outcome") == H11_BLOCKER, "H11 no-reviewer blocker drift")
    _require(h11.get("current_a10_outcome") == "NOT_TESTED", "H11 must remain NOT_TESTED")
    _require(h11.get("implementation_authorized") is False and h11.get("execution_authorized") is False, "H11 preregistration cannot authorize execution")

    for relative in CURRENT_TRUTH_SURFACES:
        text = _read(repo / relative)
        _require(CURRENT_MARKER in text or H11_NEXT_GATE in text, f"{relative}: H11 current-truth marker missing")
        _require(H11_NEXT_GATE in text, f"{relative}: H11 current next gate missing")
        _require("NOT_ESTABLISHED" in text, f"{relative}: H11 independence boundary missing")
        _require("NOT_TESTED" in text, f"{relative}: H11 current outcome boundary missing")
        _require("execution" in text.lower(), f"{relative}: H11 execution boundary missing")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    repo = args.repo.resolve()
    validate(repo)
    print(
        "Reconciliation validation passed; D8 history preserved; H11=PREREGISTERED/NOT_TESTED; "
        "Notion=7/7; next=A10_H11_EXECUTION_ADMISSION; reviewer=NOT_ESTABLISHED; execution=NOT_AUTHORIZED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
