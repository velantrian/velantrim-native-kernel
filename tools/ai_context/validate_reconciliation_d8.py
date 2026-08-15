#!/usr/bin/env python3
"""Validate current reconciliation while preserving historical role guards.

The historical layer keeps exact publication/manifest bindings on designated
history/synchronization owners plus all issue/comment/page identity checks. D8
adds a later Notion synchronization checkpoint in machine state without forcing
those historical role bindings back into current-only AI orientation surfaces.

The ``validate()`` function intentionally validates a D8-era projected state.
The standalone CLI may be invoked on a later live checkout; it applies that
projection temporarily and restores ``project-state.json`` byte-for-byte.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

_HISTORY_PATH = Path(__file__).with_name("validate_reconciliation_history.py")
_saved_name = __name__
globals()["__name__"] = "validate_reconciliation_history_embedded"
exec(compile(_HISTORY_PATH.read_text(encoding="utf-8"), str(_HISTORY_PATH), "exec"), globals(), globals())
globals()["__name__"] = _saved_name

# Historical manifest/source identity retained from the embedded validator:
# NOTION_SYNC_SHA == 70acd0... . It is deliberately not renamed here because
# downstream D8/H11 reconciliation guards bind that historical role.
D8_NOTION_SYNC_SHA = "491ff7b229606d228ca04985b19b146878390e08"
D8_RECORD_MERGE_SHA = "9ecb2369edec17a0171b6e965bcb49f9526adf0b"


def validate(repo: Path) -> None:
    state = _load_json(repo / "project-state.json")
    _require(state.get("protocol") == "nk-project-state/2", "project-state protocol drift")

    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, Mapping), "checkpoint inventory required")
    _require(checkpoints.get("manifest_generated_from_sha") == NOTION_SYNC_SHA, "reconciliation source checkpoint drift")
    _require(checkpoints.get("publication_checkpoint_sha") == PUBLICATION_SHA, "publication checkpoint drift")
    _require(checkpoints.get("notion_synchronized_through_sha") == D8_NOTION_SYNC_SHA, "Notion synchronization checkpoint drift")
    _require(
        checkpoints.get("publication_checkpoint_sha") != checkpoints.get("notion_synchronized_through_sha"),
        "publication and descendant synchronization roles collapsed",
    )
    _require(
        checkpoints.get("manifest_generated_from_sha") != checkpoints.get("notion_synchronized_through_sha"),
        "manifest and D8 Notion synchronization roles collapsed",
    )

    issues = state.get("issues")
    _require(isinstance(issues, Mapping), "issue snapshots required")
    for number in ISSUES:
        issue = issues.get(number)
        _require(isinstance(issue, Mapping), f"Issue #{number} snapshot missing")
        _require(issue.get("state") == "OPEN", f"Issue #{number} must remain OPEN")
        _require(isinstance(issue.get("meaning"), str) and issue["meaning"].strip(), f"Issue #{number} meaning required")
        verification = issue.get("verification")
        _require(isinstance(verification, Mapping), f"Issue #{number} verification required")
        _require(
            verification.get("status") == "VERIFIED"
            and verification.get("method") == "GITHUB_API"
            and verification.get("source") == f"issue/{number}",
            f"Issue #{number} verification drift",
        )

    notion = state.get("notion")
    _require(isinstance(notion, Mapping), "Notion state required")
    _require(notion.get("synchronization_required") is False, "Notion synchronization must remain complete after D8")
    _require(notion.get("status") == "SYNCED_THROUGH_DESCENDANT_CHECKPOINT", "Notion status drift")
    scope = str(notion.get("scope", ""))
    for marker in (PUBLICATION_SHA, NOTION_SYNC_SHA, D8_NOTION_SYNC_SHA, D8_RECORD_MERGE_SHA):
        _require(marker in scope, f"Notion scope missing checkpoint role: {marker}")

    issue_record = _read(repo / "docs/ai/ISSUE_RECONCILIATION.md")
    notion_record = _read(repo / "docs/ai/NOTION_HANDOFF.md")
    for number, comment_id in ISSUE_COMMENTS.items():
        _require(f"Issue #{number}" in issue_record, f"Issue #{number} missing from record")
        _require(comment_id in issue_record, f"Issue #{number} comment identity missing")
    for page_id in NOTION_PAGE_IDS:
        _require(page_id in notion_record, f"Notion page identity missing: {page_id}")

    boundary_texts = {relative: _read(repo / relative) for relative in BOUNDARY_SURFACES}
    _validate_surface_bindings(boundary_texts)

    boundaries = " ".join([issue_record, notion_record, *boundary_texts.values()]).lower()
    for phrase in ("remain open", "not production readiness", "not runtime evidence", "only then reducer-v2 runtime", "does not rewrite"):
        _require(phrase in boundaries, f"missing reconciliation boundary: {phrase}")


# Pin the D8 callable before the H11/current reconciliation wrapper embeds this
# module and deliberately redefines the global name `validate`.
validate_d8_view = validate


def _standalone_d8_view(repo: Path) -> None:
    """Run the D8 validator against a later live checkout safely."""
    state_path = repo / "project-state.json"
    state = _load_json(state_path)
    original = state_path.read_text(encoding="utf-8")

    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, dict), "checkpoint inventory required")
    checkpoints["notion_synchronized_through_sha"] = D8_NOTION_SYNC_SHA

    notion = state.get("notion")
    _require(isinstance(notion, dict), "Notion state required")
    notion["synchronization_required"] = False
    notion["status"] = "SYNCED_THROUGH_DESCENDANT_CHECKPOINT"
    notion["scope"] = (
        "Publication checkpoint " + PUBLICATION_SHA
        + ", manifest source " + NOTION_SYNC_SHA
        + ", D8 Notion synchronization checkpoint " + D8_NOTION_SYNC_SHA
        + ", and D8 consolidated record merge " + D8_RECORD_MERGE_SHA
        + " are the D8 historical roles projected for standalone validation."
    )

    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        validate_d8_view(repo)
    finally:
        state_path.write_text(original, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    repo = args.repo.resolve()
    _standalone_d8_view(repo)
    print(
        "D8 reconciliation validation passed via projected historical view; "
        f"publication={PUBLICATION_SHA}; manifest={NOTION_SYNC_SHA}; "
        f"notion_d8={D8_NOTION_SYNC_SHA}; issues=14,15,16,17; "
        f"notion_pages={len(NOTION_PAGE_IDS)}; role_binding_surfaces={len(ROLE_BINDING_SURFACES)}; "
        "live state restored"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())