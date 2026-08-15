#!/usr/bin/env python3
"""Validate Issues #14-#17 and publication/Notion checkpoint roles.

Historical role identities remain exact, but current-only AI surfaces are not
required to duplicate them. Their owners are machine state plus designated
history/synchronization records.

The validator's ``validate()`` function intentionally validates the historical
role view. The standalone CLI may be invoked on a later live repository state;
in that case it projects only the historical Notion checkpoint fields for the
duration of validation and restores ``project-state.json`` byte-for-byte.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Mapping

PUBLICATION_SHA = "10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c"
# Historical manifest/source-reconciliation identity. The name is retained for
# compatibility with the D8/H11 reconciliation wrappers.
NOTION_SYNC_SHA = "70acd0da61fee19131947aa56125833adb156ced"
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

# Exact publication/manifest role bindings are deliberately owned by stable
# human/history synchronization records, not current-only agent orientation.
ROLE_BINDING_SURFACES = (
    "README.md",
    "README.ru.md",
    "STATUS.md",
    "docs/ai/NOTION_HANDOFF.md",
)

# These surfaces still participate in the cross-document non-overclaim scan.
# Keep the legacy name as an alias because later reconciliation layers import
# it from this embedded module.
BOUNDARY_SURFACES = (
    "README.md",
    "README.ru.md",
    "STATUS.md",
    "docs/ai/README.md",
    "docs/ai/CURRENT_STATE.md",
    "docs/ai/KNOWN_RISKS.md",
    "docs/ai/NOTION_HANDOFF.md",
)
CURRENT_SURFACES = BOUNDARY_SURFACES

ACTIVE_RISK_MARKER = "**State:** `OPEN / DOCUMENTATION PROCESS RISK`."
OBSOLETE_RISK_MARKER = "HUMAN AND NOTION RECONCILIATION IN PROGRESS"
SHA_PATTERN = r"[0-9a-f]{40}"


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


def _single_match(text: str, *, relative: str, role: str, pattern: str) -> str:
    matches = re.findall(pattern, text, flags=re.MULTILINE)
    _require(len(matches) == 1, f"{relative}: {role} binding missing or ambiguous")
    value = matches[0]
    _require(isinstance(value, str), f"{relative}: {role} binding malformed")
    return value


def _require_yaml_binding(text: str, *, relative: str, field: str, role: str, expected: str) -> None:
    value = _single_match(
        text,
        relative=relative,
        role=role,
        pattern=rf"^{re.escape(field)}:\s*({SHA_PATTERN})\s*$",
    )
    _require(value == expected, f"{relative}: {role} binding drift")


def _require_table_binding(text: str, *, relative: str, label: str, role: str, expected: str) -> None:
    value = _single_match(
        text,
        relative=relative,
        role=role,
        pattern=rf"^\|\s*{re.escape(label)}\s*\|\s*`({SHA_PATTERN})`\s*\|\s*$",
    )
    _require(value == expected, f"{relative}: {role} binding drift")


def _validate_surface_bindings(texts: Mapping[str, str]) -> None:
    """Validate historical role identities only on their designated owners."""
    _require_table_binding(
        texts["README.md"], relative="README.md", label="Publication checkpoint",
        role="publication checkpoint", expected=PUBLICATION_SHA,
    )
    _require_table_binding(
        texts["README.md"], relative="README.md", label="Manifest source / Notion synchronized descendant",
        role="Notion synchronized descendant", expected=NOTION_SYNC_SHA,
    )
    _require_table_binding(
        texts["README.ru.md"], relative="README.ru.md", label="Publication checkpoint",
        role="publication checkpoint", expected=PUBLICATION_SHA,
    )
    _require_table_binding(
        texts["README.ru.md"], relative="README.ru.md", label="Источник manifest / Notion synchronized descendant",
        role="Notion synchronized descendant", expected=NOTION_SYNC_SHA,
    )

    status = texts["STATUS.md"]
    _require_yaml_binding(status, relative="STATUS.md", field="publication_checkpoint", role="publication checkpoint", expected=PUBLICATION_SHA)
    _require_yaml_binding(status, relative="STATUS.md", field="manifest_generated_from", role="manifest source", expected=NOTION_SYNC_SHA)
    _require_yaml_binding(status, relative="STATUS.md", field="notion_synchronized_through", role="Notion synchronized descendant", expected=NOTION_SYNC_SHA)

    handoff = texts["docs/ai/NOTION_HANDOFF.md"]
    _require_yaml_binding(handoff, relative="docs/ai/NOTION_HANDOFF.md", field="publication_checkpoint", role="publication checkpoint", expected=PUBLICATION_SHA)
    _require_yaml_binding(handoff, relative="docs/ai/NOTION_HANDOFF.md", field="manifest_generated_from", role="manifest source", expected=NOTION_SYNC_SHA)
    _require_yaml_binding(handoff, relative="docs/ai/NOTION_HANDOFF.md", field="latest_synchronized_descendant", role="Notion synchronized descendant", expected=NOTION_SYNC_SHA)

    risks = texts["docs/ai/KNOWN_RISKS.md"]
    _require(ACTIVE_RISK_MARKER in risks, "active current-state drift risk state drift")
    _require(OBSOLETE_RISK_MARKER not in risks, "obsolete current-state drift risk state remains present")


def validate(repo: Path) -> None:
    state = _load_json(repo / "project-state.json")
    _require(state.get("protocol") == "nk-project-state/2", "project-state protocol drift")

    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, Mapping), "checkpoint inventory required")
    _require(checkpoints.get("manifest_generated_from_sha") == NOTION_SYNC_SHA, "reconciliation source checkpoint drift")
    _require(checkpoints.get("publication_checkpoint_sha") == PUBLICATION_SHA, "publication checkpoint drift")
    _require(checkpoints.get("notion_synchronized_through_sha") == NOTION_SYNC_SHA, "Notion synchronization checkpoint drift")
    _require(
        checkpoints.get("publication_checkpoint_sha") != checkpoints.get("notion_synchronized_through_sha"),
        "publication and descendant synchronization roles collapsed",
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
    _require(notion.get("synchronization_required") is True, "Notion synchronization must remain required")
    _require(notion.get("status") == "SYNCED_THROUGH_DESCENDANT_CHECKPOINT", "Notion status drift")
    scope = str(notion.get("scope", ""))
    _require(PUBLICATION_SHA in scope and NOTION_SYNC_SHA in scope, "Notion scope must name publication and synchronized descendant checkpoints")

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


# Pin the historical callable before this module is embedded into later
# reconciliation layers that deliberately redefine the global name `validate`.
validate_historical_view = validate


def _standalone_historical_view(repo: Path) -> None:
    """Run the historical validator against a later live checkout safely."""
    state_path = repo / "project-state.json"
    state = _load_json(state_path)
    original = state_path.read_text(encoding="utf-8")

    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, dict), "checkpoint inventory required")
    checkpoints["notion_synchronized_through_sha"] = NOTION_SYNC_SHA

    notion = state.get("notion")
    _require(isinstance(notion, dict), "Notion state required")
    notion["synchronization_required"] = True
    notion["status"] = "SYNCED_THROUGH_DESCENDANT_CHECKPOINT"
    notion["scope"] = (
        "Publication checkpoint " + PUBLICATION_SHA
        + " and manifest source / synchronized descendant " + NOTION_SYNC_SHA
        + " are the historical reconciliation roles projected for standalone validation."
    )

    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        validate_historical_view(repo)
    finally:
        state_path.write_text(original, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    repo = args.repo.resolve()
    _standalone_historical_view(repo)
    print(
        "Historical reconciliation validation passed via projected historical view; "
        f"publication={PUBLICATION_SHA}; manifest_source={NOTION_SYNC_SHA}; "
        f"issues=14,15,16,17; notion_pages={len(NOTION_PAGE_IDS)}; "
        f"role_binding_surfaces={len(ROLE_BINDING_SURFACES)}; live state restored"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())