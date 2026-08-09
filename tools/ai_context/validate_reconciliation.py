#!/usr/bin/env python3
"""Validate the bounded Issues #14-#17 and Notion reconciliation record."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

PUBLICATION_SHA = "10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c"
ISSUES = ("14", "15", "16", "17")
ISSUE_COMMENTS = {
    "14": "5231286665",
    "15": "5231287409",
    "16": "5231288045",
    "17": "5231288737",
}
NOTION_PAGE_IDS = (
    "3b7ac84d-0547-81ff-8f04-cf967ff80069",
    "3b7ac84d-0547-8163-9376-e0454ccddc03",
    "3b7ac84d-0547-817e-b7c2-c04fbbcf78c1",
    "3b7ac84d-0547-8112-8595-ca44940cc242",
    "3b7ac84d-0547-8101-ada4-de9702b68eb3",
    "3b7ac84d-0547-81b6-80a6-f87a05ed6f9e",
)


class ReconciliationError(RuntimeError):
    """Raised when the reconciliation record drifts or overclaims."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ReconciliationError(message)


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ReconciliationError(f"cannot read {path}: {exc}") from exc
    _require(isinstance(value, dict), f"{path} must contain an object")
    return value


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ReconciliationError(f"cannot read {path}: {exc}") from exc


def validate(repo: Path) -> None:
    state = _load_json(repo / "project-state.json")
    _require(state.get("protocol") == "nk-project-state/2", "project-state protocol drift")

    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, Mapping), "checkpoint inventory required")
    _require(
        checkpoints.get("manifest_generated_from_sha") == PUBLICATION_SHA,
        "reconciliation source checkpoint drift",
    )
    _require(
        checkpoints.get("publication_checkpoint_sha") == PUBLICATION_SHA,
        "publication checkpoint drift",
    )
    _require(
        checkpoints.get("notion_synchronized_through_sha") == PUBLICATION_SHA,
        "Notion synchronization checkpoint drift",
    )

    issues = state.get("issues")
    _require(isinstance(issues, Mapping), "issue snapshots required")
    for number in ISSUES:
        issue = issues.get(number)
        _require(isinstance(issue, Mapping), f"Issue #{number} snapshot missing")
        _require(issue.get("state") == "OPEN", f"Issue #{number} must remain OPEN")
        _require(
            isinstance(issue.get("meaning"), str) and issue["meaning"].strip(),
            f"Issue #{number} meaning required",
        )
        verification = issue.get("verification")
        _require(
            isinstance(verification, Mapping),
            f"Issue #{number} verification required",
        )
        _require(
            verification.get("status") == "VERIFIED"
            and verification.get("method") == "GITHUB_API"
            and verification.get("source") == f"issue/{number}",
            f"Issue #{number} verification drift",
        )

    notion = state.get("notion")
    _require(isinstance(notion, Mapping), "Notion state required")
    _require(
        notion.get("synchronization_required") is True,
        "Notion synchronization must remain required",
    )
    _require(
        notion.get("status") == "SYNCED_THROUGH_PUBLICATION_CHECKPOINT",
        "Notion status drift",
    )
    _require(
        PUBLICATION_SHA in str(notion.get("scope", "")),
        "Notion scope must name the synchronized checkpoint",
    )

    issue_record = _read(repo / "docs/ai/ISSUE_RECONCILIATION.md")
    notion_record = _read(repo / "docs/ai/NOTION_HANDOFF.md")
    current_state = _read(repo / "docs/ai/CURRENT_STATE.md")
    status = _read(repo / "STATUS.md")

    for number, comment_id in ISSUE_COMMENTS.items():
        _require(f"Issue #{number}" in issue_record, f"Issue #{number} missing from record")
        _require(comment_id in issue_record, f"Issue #{number} comment identity missing")

    for page_id in NOTION_PAGE_IDS:
        _require(page_id in notion_record, f"Notion page identity missing: {page_id}")

    for text, label in (
        (issue_record, "issue reconciliation"),
        (notion_record, "Notion synchronization"),
        (current_state, "AI current state"),
        (status, "human status"),
    ):
        _require(PUBLICATION_SHA in text, f"{label} checkpoint drift")

    boundaries = " ".join((issue_record, notion_record, current_state, status)).lower()
    for phrase in (
        "remain open",
        "not production readiness",
        "not runtime evidence",
        "only then reducer-v2 runtime",
    ):
        _require(phrase in boundaries, f"missing reconciliation boundary: {phrase}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    repo = args.repo.resolve()
    validate(repo)
    print(
        "Reconciliation validation passed; "
        f"publication={PUBLICATION_SHA}; issues=14,15,16,17; notion_pages={len(NOTION_PAGE_IDS)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
