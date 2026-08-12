#!/usr/bin/env python3
"""Validate ADR-0027 state after seven-surface Notion read-back completion."""
from __future__ import annotations

import copy
from pathlib import Path
from typing import Any, Mapping

_PRE_SYNC_PATH = Path(__file__).with_name("validate_project_state_post_adr0027.py")
_saved_name = __name__
globals()["__name__"] = "validate_project_state_post_adr0027_embedded"
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

DECISION_MERGE = "57993f39906ae7266011f6146c9a485d0587d2bf"
D8_NOTION_SYNC_SHA = "491ff7b229606d228ca04985b19b146878390e08"
ADR0027_TRUTH_SYNC_SHA = "90bcb0fa2a3a2e85a590e9ba79746f3297b55457"
RESIDUAL_TARGETS = (
    "A10-H03",
    "A10-H06",
    "A10-H08",
    "A10-H09",
    "A10-H10",
    "A10-H11",
)


def _pre_sync_view(state: Mapping[str, Any]) -> dict[str, Any]:
    """Project the completed state back onto the immutable pre-readback layer."""
    value = copy.deepcopy(dict(state))
    value["checkpoints"]["notion_synchronized_through_sha"] = D8_NOTION_SYNC_SHA
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
        notion.get("status") == "SYNCED_THROUGH_DESCENDANT_CHECKPOINT",
        "Notion status drift after ADR-0027 read-back",
    )
    _require(
        notion.get("decision_sync_status") == "SYNCHRONIZED",
        "ADR-0027 synchronization status must be SYNCHRONIZED",
    )
    _require(
        notion.get("surface_count") == 7,
        "ADR-0027 Notion synchronization must remain seven-surface scoped",
    )
    _require(
        notion.get("read_back_verified_count") == 7,
        "ADR-0027 Notion read-back must remain 7/7 verified",
    )
    _require(
        notion.get("new_pages_created") == 0,
        "ADR-0027 synchronization must not create new Notion pages",
    )

    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, Mapping), "checkpoint inventory required")
    _require(
        checkpoints.get("notion_synchronized_through_sha") == ADR0027_TRUTH_SYNC_SHA,
        "ADR-0027 Notion synchronization checkpoint drift",
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

    research = state["tracks"]["long_horizon_research"]
    validation = research["post_blueprint_validation"]
    decision = validation.get("post_d8_operator_decision")
    _require(isinstance(decision, Mapping), "post-D8 operator decision required")
    _require(
        decision.get("decision_merge_sha") == DECISION_MERGE,
        "post-D8 decision merge drift",
    )
    _require(
        decision.get("next_gate") == "RESIDUAL_A10_VALIDATION_PLAN",
        "residual planning gate drift",
    )
    _require(
        decision.get("next_gate_scope") == "RESEARCH_PLANNING_ONLY",
        "residual planning scope drift",
    )
    _require(
        decision.get("experiment_execution_authorized") is False,
        "residual experiment execution must remain unauthorized",
    )
    _require(
        tuple(decision.get("residual_validation_targets", ())) == RESIDUAL_TARGETS,
        "residual A10 target set drift",
    )
    _require(
        research.get("runtime_authorized") is False,
        "runtime authority must remain frozen",
    )
    _require(
        research["architecture_refoundation"].get("runtime_expansion_frozen") is True,
        "runtime expansion freeze must remain active",
    )
    _require(
        validation.get("product_runtime_thaw") is False,
        "product runtime thaw must remain false",
    )
    _require(
        state["status"]["production_authorized"] is False,
        "production must remain unauthorized",
    )


def validate(
    state: Mapping[str, Any],
    *,
    repo: Path,
    registry: Mapping[str, Any] | None = None,
    check_git: bool = True,
) -> None:
    _PRE_SYNC_VALIDATE(
        _pre_sync_view(state),
        repo=repo,
        registry=registry,
        check_git=check_git,
    )
    _validate_completed_sync(state)


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
        "Project-state validation passed; ADR-0027=SYNCHRONIZED; "
        "notion_read_back=7/7; next=RESIDUAL_A10_VALIDATION_PLAN; "
        "scope=RESEARCH_PLANNING_ONLY; experiment_execution=NOT_AUTHORIZED; "
        "runtime=FROZEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
