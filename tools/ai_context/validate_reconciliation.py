#!/usr/bin/env python3
"""Validate completed ADR-0027 reconciliation over preserved D8/history guards."""
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

DECISION_MERGE = "57993f39906ae7266011f6146c9a485d0587d2bf"
ADR0027_TRUTH_SYNC_SHA = "90bcb0fa2a3a2e85a590e9ba79746f3297b55457"
CURRENT_MARKER = "POST_D8_OPERATOR_DECISION_CURRENT"


def _d8_repo_view(repo: Path) -> None:
    """Validate immutable D8 history through a temporary compatibility view.

    The D8 validator reads repository files directly. Completed ADR-0027
    synchronization advances only the Notion descendant checkpoint, so project
    state is temporarily projected back to the D8 checkpoint. Deliberately
    corrupted checkpoint values are not rewritten and therefore still fail
    closed in D8 validation.
    """
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
        "ADR-0027 Notion synchronization checkpoint drift",
    )

    notion = state.get("notion")
    _require(isinstance(notion, Mapping), "Notion state required")
    _require(
        notion.get("synchronization_required") is False,
        "ADR-0027 Notion synchronization must be complete after read-back",
    )
    _require(
        notion.get("decision_sync_status") == "SYNCHRONIZED",
        "ADR-0027 synchronization status drift",
    )
    _require(
        notion.get("surface_count") == 7
        and notion.get("read_back_verified_count") == 7
        and notion.get("new_pages_created") == 0,
        "ADR-0027 Notion read-back must remain 7/7 with zero new pages",
    )
    scope = str(notion.get("scope", ""))
    for marker in (
        DECISION_MERGE,
        ADR0027_TRUTH_SYNC_SHA,
        "7/7",
        "RESIDUAL_A10_VALIDATION_PLAN",
        "RESEARCH_PLANNING_ONLY",
        "experiment execution is not authorized",
    ):
        _require(marker in scope, f"Notion scope missing completed-sync marker: {marker}")

    decision = state["tracks"]["long_horizon_research"]["post_blueprint_validation"].get(
        "post_d8_operator_decision"
    )
    _require(
        isinstance(decision, Mapping)
        and decision.get("decision_merge_sha") == DECISION_MERGE,
        "ADR-0027 machine binding drift",
    )
    _require(
        decision.get("next_gate") == "RESIDUAL_A10_VALIDATION_PLAN"
        and decision.get("next_gate_scope") == "RESEARCH_PLANNING_ONLY",
        "ADR-0027 residual planning gate drift",
    )
    _require(
        decision.get("experiment_execution_authorized") is False,
        "ADR-0027 residual experiment execution must remain unauthorized",
    )

    for relative in CURRENT_SURFACES:
        _require(
            CURRENT_MARKER in _read(repo / relative),
            f"{relative}: current ADR-0027 overlay missing",
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    repo = args.repo.resolve()
    validate(repo)
    print(
        "Reconciliation validation passed; D8 history preserved; "
        "ADR-0027 sync=SYNCHRONIZED; read_back=7/7; "
        "next=RESIDUAL_A10_VALIDATION_PLAN; execution=NOT_AUTHORIZED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
