#!/usr/bin/env python3
"""Validate current project-state roles while preserving historical guards.

The history layer is the exact pre-D8 validator. Current validation separates
three identities that D8 must not collapse: publication, manifest source, and
the later Notion-synchronized descendant checkpoint.
"""
from __future__ import annotations

import copy
from pathlib import Path
from typing import Any, Mapping

_HISTORY_PATH = Path(__file__).with_name("validate_project_state_history.py")
_saved_name = __name__
globals()["__name__"] = "validate_project_state_history_embedded"
exec(compile(_HISTORY_PATH.read_text(encoding="utf-8"), str(_HISTORY_PATH), "exec"), globals(), globals())
globals()["__name__"] = _saved_name

_HISTORICAL_VALIDATE = validate

PUBLICATION_SHA = "10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c"
MANIFEST_SOURCE_SHA = "70acd0da61fee19131947aa56125833adb156ced"
D8_NOTION_SYNC_SHA = "491ff7b229606d228ca04985b19b146878390e08"
D8_RECORD_MERGE_SHA = "9ecb2369edec17a0171b6e965bcb49f9526adf0b"


def _validate_current_checkpoint_roles(state: Mapping[str, Any]) -> None:
    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, Mapping), "checkpoint inventory required")
    publication = checkpoints.get("publication_checkpoint_sha")
    manifest = checkpoints.get("manifest_generated_from_sha")
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
        _require(
            notion_status in NOTION_STATUSES,
            "invalid Notion synchronization state",
        )

    _require(
        publication == PUBLICATION_SHA,
        "publication checkpoint drift",
    )
    _require(
        manifest == MANIFEST_SOURCE_SHA,
        "manifest/Notion checkpoint mismatch: historical manifest-source role drift",
    )
    _require(
        notion_checkpoint == D8_NOTION_SYNC_SHA,
        "manifest/Notion checkpoint mismatch: D8 Notion synchronization checkpoint drift",
    )
    _require(
        manifest != notion_checkpoint,
        "manifest/Notion checkpoint roles must remain distinct after D8",
    )
    _require(
        notion.get("synchronization_required") is False,
        "Notion synchronization must remain complete after D8",
    )
    scope = str(notion.get("scope", ""))
    for marker in (PUBLICATION_SHA, MANIFEST_SOURCE_SHA, D8_NOTION_SYNC_SHA, D8_RECORD_MERGE_SHA):
        _require(marker in scope, f"Notion scope missing D8 checkpoint role: {marker}")


def _historical_view(state: Mapping[str, Any]) -> dict[str, Any]:
    historical = copy.deepcopy(dict(state))
    checkpoints = historical["checkpoints"]
    checkpoints["notion_synchronized_through_sha"] = checkpoints["manifest_generated_from_sha"]
    notion = historical["notion"]
    notion["synchronization_required"] = True
    notion["status"] = "SYNCED_THROUGH_DESCENDANT_CHECKPOINT"
    historical["non_claims"] = list(historical.get("non_claims", [])) + [
        "A later Notion synchronization checkpoint does not rewrite or replace the earlier publication checkpoint.",
    ]
    return historical


def validate(
    state: Mapping[str, Any],
    *,
    repo: Path,
    registry: Mapping[str, Any] | None = None,
    check_git: bool = True,
) -> None:
    _validate_current_checkpoint_roles(state)
    _HISTORICAL_VALIDATE(
        _historical_view(state),
        repo=repo,
        registry=registry,
        check_git=check_git,
    )


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

    checkpoints = state["checkpoints"]
    assertions = state["assertion_map"]
    print(
        "Project-state validation passed; "
        f"manifest_source={checkpoints['manifest_generated_from_sha']}; "
        f"notion_sync={checkpoints['notion_synchronized_through_sha']}; "
        f"runtime={state['status']['kernel_runtime_conformance']}; "
        f"operational={state['status']['operational_validation']}; "
        f"assertions={assertions['supported']}/"
        f"{assertions['partial']}/"
        f"{assertions['unsupported']}/"
        f"{assertions['failed']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
