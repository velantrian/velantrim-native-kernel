#!/usr/bin/env python3
"""Validate ADR-0027 current truth after completed seven-surface Notion read-back."""
from __future__ import annotations

import copy
import sys
from pathlib import Path
from typing import Any, Mapping

_PRE_SYNC_PATH = Path(__file__).with_name("validate_architecture_freeze_post_adr0027.py")
_saved_name = __name__
globals()["__name__"] = "validate_architecture_freeze_post_adr0027_embedded"
exec(
    compile(
        _PRE_SYNC_PATH.read_text(encoding="utf-8"),
        str(_PRE_SYNC_PATH),
        "exec",
    ),
    globals(),
    globals(),
)
globals()["__name__"] = _saved_name
_PRE_SYNC_VALIDATE = validate

D8_NOTION_SYNC_SHA = "491ff7b229606d228ca04985b19b146878390e08"
ADR0027_TRUTH_SYNC_SHA = "90bcb0fa2a3a2e85a590e9ba79746f3297b55457"


def _pre_sync_view(state: Mapping[str, Any]) -> dict[str, Any]:
    """Project completed documentation sync onto the pre-readback ADR-0027 guard.

    Only the authoritative completed-sync checkpoint is rewritten. Mutated
    checkpoint values remain visible so historical negative tests fail on the
    original invariant instead of being masked by compatibility projection.
    """
    value = copy.deepcopy(dict(state))
    checkpoints = value["checkpoints"]
    if checkpoints.get("notion_synchronized_through_sha") == ADR0027_TRUTH_SYNC_SHA:
        checkpoints["notion_synchronized_through_sha"] = D8_NOTION_SYNC_SHA
    notion = value["notion"]
    notion["synchronization_required"] = True
    return value


def _validate_completed_sync(state: Mapping[str, Any]) -> None:
    notion = state.get("notion")
    _require(isinstance(notion, Mapping), "Notion synchronization state required")
    _require(
        notion.get("synchronization_required") is False,
        "ADR-0027 Notion synchronization must be complete after verified read-back",
    )
    _require(
        notion.get("decision_sync_status") == "SYNCHRONIZED",
        "ADR-0027 synchronization status must remain SYNCHRONIZED",
    )
    _require(
        notion.get("surface_count") == 7
        and notion.get("read_back_verified_count") == 7
        and notion.get("new_pages_created") == 0,
        "ADR-0027 Notion synchronization must remain 7/7 with zero new pages",
    )
    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, Mapping), "checkpoint inventory required")
    _require(
        checkpoints.get("notion_synchronized_through_sha") == ADR0027_TRUTH_SYNC_SHA,
        "ADR-0027 Notion synchronization checkpoint drift",
    )

    research = state["tracks"]["long_horizon_research"]
    ref = research["architecture_refoundation"]
    validation = research["post_blueprint_validation"]
    decision = validation["post_d8_operator_decision"]
    _require(
        ref.get("next_content_slice") == POST_DECISION_GATE,
        "next architecture validation gate drift; post-ADR-0027 next gate drift",
    )
    _require(ref.get("runtime_expansion_frozen") is True, "ADR-0027 must preserve runtime freeze")
    _require(validation.get("product_runtime_thaw") is False, "ADR-0027 cannot thaw product runtime")
    _require(
        decision.get("next_gate") == POST_DECISION_GATE
        and decision.get("next_gate_scope") == "RESEARCH_PLANNING_ONLY",
        "residual planning gate drift",
    )
    _require(
        decision.get("experiment_execution_authorized") is False,
        "residual experiment execution must remain unauthorized",
    )
    _require(state["status"]["production_authorized"] is False, "production must remain unauthorized")


def validate(state: Mapping[str, Any], *, repo: Path) -> None:
    _PRE_SYNC_VALIDATE(_pre_sync_view(state), repo=repo)
    _validate_completed_sync(state)


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
        "Architecture validation passed; history=D8 preserved; ADR-0027=ACCEPTED; "
        "notion_read_back=7/7; next=RESIDUAL_A10_VALIDATION_PLAN; "
        "execution_authorized=false; runtime_expansion_frozen=true"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
