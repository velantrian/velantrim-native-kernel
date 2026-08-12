#!/usr/bin/env python3
"""Validate post-RAVP current reconciliation over preserved D8/history guards."""
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

ADR0027_TRUTH_SYNC_SHA = "edc0501d71a827462aafd1ac4497920a719a4519"
PRE_PLAN_ADR0027_TRUTH_SYNC_SHA = "90bcb0fa2a3a2e85a590e9ba79746f3297b55457"
RESIDUAL_PLAN_ID = "RAVP-001-residual-a10-validation-plan-v1"
RESIDUAL_PLAN_HEAD = "918ac46f4d93f085171b03564f9fbe30f543b200"
NEXT_GATE = "SEPARATE_FAMILY_PREREGISTRATION_SELECTION"
CURRENT_MARKER = "POST_RESIDUAL_A10_PLAN_CURRENT"
CURRENT_TRUTH_SURFACES = ("AGENTS.md", "docs/ai/POST_RESIDUAL_A10_STATE.md")


def _d8_repo_view(repo: Path) -> None:
    """Validate immutable D8 chronology through a temporary state projection."""
    state_path = repo / "project-state.json"
    state = _load_json(state_path)
    original = state_path.read_text(encoding="utf-8")
    checkpoints = state["checkpoints"]
    if checkpoints.get("notion_synchronized_through_sha") == ADR0027_TRUTH_SYNC_SHA:
        checkpoints["notion_synchronized_through_sha"] = D8_NOTION_SYNC_SHA
    state["notion"]["synchronization_required"] = False
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
    _require(
        checkpoints.get("notion_synchronized_through_sha") == ADR0027_TRUTH_SYNC_SHA,
        "Residual A10 plan Notion synchronization checkpoint drift",
    )

    notion = state.get("notion")
    _require(isinstance(notion, Mapping), "Notion state required")
    _require(notion.get("synchronization_required") is False, "post-plan Notion synchronization must be complete")
    _require(notion.get("decision_sync_status") == "SYNCHRONIZED", "post-plan Notion synchronization status drift")
    _require(
        notion.get("surface_count") == 7
        and notion.get("read_back_verified_count") == 7
        and notion.get("new_pages_created") == 0,
        "post-plan Notion read-back must remain 7/7 with zero new pages",
    )
    scope = str(notion.get("scope", ""))
    for marker in (ADR0027_TRUTH_SYNC_SHA, RESIDUAL_PLAN_ID, "7/7", NEXT_GATE, "No family preregistration", "experiment execution"):
        _require(marker in scope, f"Notion scope missing post-plan marker: {marker}")

    validation = state["tracks"]["long_horizon_research"]["post_blueprint_validation"]
    decision = validation.get("post_d8_operator_decision")
    _require(isinstance(decision, Mapping), "ADR-0027 decision record required")
    _require(decision.get("next_gate") == "RESIDUAL_A10_VALIDATION_PLAN", "historical ADR-0027 next gate drift")
    _require(decision.get("experiment_execution_authorized") is False, "historical ADR-0027 execution boundary drift")

    plan = validation.get("residual_a10_validation_plan")
    _require(isinstance(plan, Mapping), "RAVP-001 current result required")
    _require(plan.get("plan_id") == RESIDUAL_PLAN_ID, "RAVP-001 identity drift")
    _require(plan.get("exact_head_sha") == RESIDUAL_PLAN_HEAD, "RAVP-001 exact-head drift")
    _require(plan.get("merge_sha") == ADR0027_TRUTH_SYNC_SHA, "RAVP-001 merge binding drift")
    _require(plan.get("notion_read_back_verified_count") == 7, "RAVP-001 Notion read-back drift")
    _require(plan.get("selected_family") is None, "no residual family may be silently selected")
    _require(plan.get("next_gate") == NEXT_GATE, "RAVP-001 next gate drift")
    _require(plan.get("family_preregistration_authorized") is False, "family preregistration must remain unauthorized")
    _require(plan.get("experiment_implementation_authorized") is False, "experiment implementation must remain unauthorized")
    _require(plan.get("experiment_execution_authorized") is False, "experiment execution must remain unauthorized")

    for relative in CURRENT_TRUTH_SURFACES:
        text = _read(repo / relative)
        _require(CURRENT_MARKER in text or NEXT_GATE in text, f"{relative}: post-plan current-truth marker missing")
        _require(NEXT_GATE in text, f"{relative}: current next gate missing")
        _require("execution" in text.lower(), f"{relative}: execution boundary missing")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    repo = args.repo.resolve()
    validate(repo)
    print(
        "Reconciliation validation passed; D8 history preserved; RAVP-001=COMPLETE; "
        "Notion=7/7; next=SEPARATE_FAMILY_PREREGISTRATION_SELECTION; "
        "selected_family=NONE; execution=NOT_AUTHORIZED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
