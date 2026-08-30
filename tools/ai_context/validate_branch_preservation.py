#!/usr/bin/env python3
"""Fail-closed validator for repository branch-preservation safety records."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path, PurePosixPath
from typing import Any

PROTOCOL = "nk-branch-preservation/1"
STATUS = "BOUNDED_REPOSITORY_HYGIENE_SAFETY_CONTRACT"
MANIFEST = Path("evidence/branch-preservation-v1.json")
FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
MIN_CITATION_PREFIX = 12

TOP_LEVEL_KEYS = {"protocol", "status", "authority_boundary", "policy", "protected_refs"}
AUTHORITY_KEYS = {
    "h11_outcome_changed",
    "runtime_authorized",
    "canon_authorized",
    "production_authorized",
    "branch_deletion_authorized",
    "auto_delete_authorized",
}
POLICY_KEYS = {"purpose", "default_action", "migration_rule"}
REF_KEYS = {"ref", "tip_sha", "cited_by", "reason", "migration_state"}
EXPECTED_POLICY = {
    "purpose": "Prevent deletion of refs that currently keep repository-cited historical evidence commits reachable until durable main-reachable anchors are recorded.",
    "default_action": "NO_DELETION_FROM_THIS_MANIFEST",
    "migration_rule": "Preserve the historical PR-head identity and add a durable main-reachable checkpoint before a protected ref may leave this manifest.",
}

# Deliberately duplicated from the manifest. Any change to a protected ref,
# frozen tip, preservation classification, or declared citation inventory must
# be an explicit validator change rather than a manifest-only weakening.
FROZEN_CONTRACT = {
    "agent/adr0023-evidence-finalization": {"tip_sha": "c9d3944627b40619002428d2a37b8621b2cbfe3b", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("docs/ai/WORK_LOG.md",)},
    "agent/c4-offline-shadow": {"tip_sha": "b7786c088ef2cfd203c02625a5e0c40129cbf148", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("docs/ai/C4_IMPLEMENTATION_RECORD.md",)},
    "agent/iar-1-review-request": {"tip_sha": "3ca47783cf1b4bde46158bce5aa183ceed82d0f5", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("docs/reviews/IAR-1_LATE_REVIEW_FOLLOWUP.md",)},
    "agent/iar1-late-review-followup": {"tip_sha": "157be487a6727cf0ec2a36988ad5ab203ba5e0b2", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("docs/reviews/IAR-1_LATE_REVIEW_FOLLOWUP.md",)},
    "agent/operator-decision-packages": {"tip_sha": "57c14742f705f96e33e929e7e206f14169d42fc0", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("docs/ai/ISSUE_RECONCILIATION.md",)},
    "agent/p3-replay-projections": {"tip_sha": "7e615bc633cbf966211d3b2815f51b8ff9eb9716", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("docs/ai/P3_IMPLEMENTATION_RECORD.md",)},
    "agent/p4-conformance-adapter": {"tip_sha": "0e7adf71475d37d5c096718762cbc08086c5e465", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("docs/ai/P4_IMPLEMENTATION_RECORD.md",)},
    "agent/p5-sqlite-c3": {"tip_sha": "6483c9a229aea7d49929745b7652e67f1c39949c", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("docs/ai/P5_IMPLEMENTATION_RECORD.md",)},
    "agent/pr85-post-merge-review-fixes": {"tip_sha": "c3b8695bf3d7207ac4c6b19dcb5e9e2bda92f764", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("docs/ai/NOTION_HANDOFF.md",)},
    "agent/sqlite-integrity-wal-safety": {"tip_sha": "ab7a203ce7ed8ec46c341bc4da9063d56f023338", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("docs/ai/P5_IMPLEMENTATION_RECORD.md",)},
    "archive/bootstrap-v0.1.2.1-docs-lineage": {"tip_sha": "d64855afc4b34bcfb0ed8f1c3766925d287b07c6", "migration_state": "INTENTIONAL_LONG_LIVED_LINEAGE", "cited_by": ("docs/source-recovery/2026-08-09-bootstrap-branch-resweep.md",)},
    "bootstrap/research-kernel-v0.1.2.1": {"tip_sha": "d64855afc4b34bcfb0ed8f1c3766925d287b07c6", "migration_state": "INTENTIONAL_LONG_LIVED_LINEAGE", "cited_by": ("docs/source-recovery/2026-08-09-bootstrap-branch-resweep.md",)},
    "research/h11-family-selection": {"tip_sha": "d9273a22c411467109112f1fc6ea263ed8819d1d", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("project-state.json", "tools/ai_context/validate_project_state.py")},
    "research/h11-preregistration": {"tip_sha": "1dca13cdd2759c70d810f44977a227fe1147d4bb", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("project-state.json", "tools/ai_context/validate_project_state.py")},
    "research/residual-a10-validation-plan": {"tip_sha": "918ac46f4d93f085171b03564f9fbe30f543b200", "migration_state": "PENDING_MAIN_REACHABLE_ANCHOR", "cited_by": ("project-state.json", "tools/ai_context/validate_project_state.py")},
}


class BranchPreservationError(RuntimeError):
    pass


def _require(value: bool, message: str) -> None:
    if not value:
        raise BranchPreservationError(message)


def _git(repo: Path, *args: str) -> str:
    proc = subprocess.run(["git", "-C", str(repo), *args], text=True, capture_output=True)
    if proc.returncode != 0:
        raise BranchPreservationError(proc.stderr.strip() or "git command failed")
    return proc.stdout.strip()


def _remote_branch_sha(repo: Path, ref: str) -> str:
    output = _git(repo, "ls-remote", "--exit-code", "--heads", "origin", f"refs/heads/{ref}")
    rows = [line.split() for line in output.splitlines() if line.strip()]
    _require(len(rows) == 1 and len(rows[0]) == 2, f"remote protected branch must resolve exactly once: {ref}")
    sha, remote_ref = rows[0]
    _require(remote_ref == f"refs/heads/{ref}", f"remote protected branch identity mismatch: {ref}")
    _require(FULL_SHA.fullmatch(sha) is not None, f"remote protected branch returned invalid SHA: {ref}")
    return sha


def _resolve_citation(repo: Path, raw: str, manifest_path: Path) -> tuple[Path, str]:
    _require(isinstance(raw, str) and raw.strip(), "citation path must be a non-empty string")
    relative = PurePosixPath(raw)
    _require(not relative.is_absolute(), f"citation path must be repository-relative: {raw}")
    _require(".." not in relative.parts, f"citation path escapes repository: {raw}")
    candidate = (repo / Path(*relative.parts)).resolve()
    try:
        normalized = candidate.relative_to(repo).as_posix()
    except ValueError as exc:
        raise BranchPreservationError(f"citation path escapes repository: {raw}") from exc
    _require(candidate != manifest_path.resolve(), "preservation manifest cannot self-satisfy a citation")
    _require(candidate.is_file(), f"citation file required: {raw}")
    return candidate, normalized


def _citation_contains_anchor(path: Path, sha: str, ref: str, state: str) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as exc:
        raise BranchPreservationError(f"citation file must be readable UTF-8 text: {path}") from exc
    if state == "PENDING_MAIN_REACHABLE_ANCHOR":
        return sha[:MIN_CITATION_PREFIX] in text
    return sha[:MIN_CITATION_PREFIX] in text or ref in text


def _exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    actual = set(value)
    _require(actual == expected, f"{label} keys drift: expected {sorted(expected)}, got {sorted(actual)}")


def validate(repo: Path, manifest_path: Path | None = None) -> None:
    repo = repo.resolve()
    path = (manifest_path or repo / MANIFEST).resolve()
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))

    _require(isinstance(data, dict), "branch preservation manifest must be an object")
    _exact_keys(data, TOP_LEVEL_KEYS, "top-level manifest")
    _require(data.get("protocol") == PROTOCOL, "branch preservation protocol drift")
    _require(data.get("status") == STATUS, "branch preservation status drift")

    boundary = data.get("authority_boundary")
    _require(isinstance(boundary, dict), "authority boundary required")
    _exact_keys(boundary, AUTHORITY_KEYS, "authority_boundary")
    for key in AUTHORITY_KEYS:
        _require(boundary.get(key) is False, f"authority boundary must remain false: {key}")

    policy = data.get("policy")
    _require(isinstance(policy, dict), "preservation policy required")
    _exact_keys(policy, POLICY_KEYS, "policy")
    _require(policy == EXPECTED_POLICY, "preservation no-deletion policy drift")

    refs = data.get("protected_refs")
    _require(isinstance(refs, list) and refs, "protected_refs must be non-empty")
    names: set[str] = set()

    for item in refs:
        _require(isinstance(item, dict), "protected ref entry must be an object")
        _exact_keys(item, REF_KEYS, "protected ref entry")
        ref = item.get("ref")
        sha = item.get("tip_sha")
        state = item.get("migration_state")
        reason = item.get("reason")
        cited_by = item.get("cited_by")

        _require(isinstance(ref, str) and ref and ref not in names, f"duplicate/invalid ref: {ref}")
        names.add(ref)
        _require(ref in FROZEN_CONTRACT, f"unexpected protected ref requires explicit validator update: {ref}")
        frozen = FROZEN_CONTRACT[ref]
        _require(isinstance(sha, str) and FULL_SHA.fullmatch(sha) is not None, f"full 40-char SHA required: {ref}")
        _require(sha == frozen["tip_sha"], f"frozen protected tip drift: {ref}")
        _require(state == frozen["migration_state"], f"frozen migration_state drift: {ref}")
        _require(isinstance(reason, str) and reason.strip(), f"reason required: {ref}")
        _require(isinstance(cited_by, list) and cited_by, f"cited_by must be non-empty: {ref}")
        _require(all(isinstance(value, str) and value.strip() for value in cited_by), f"invalid cited_by path: {ref}")

        normalized: list[str] = []
        citation_paths: list[Path] = []
        for citation in cited_by:
            citation_path, normalized_path = _resolve_citation(repo, citation, path)
            normalized.append(normalized_path)
            citation_paths.append(citation_path)
        _require(len(set(normalized)) == len(normalized), f"duplicate normalized cited_by path: {ref}")
        _require(tuple(normalized) == tuple(frozen["cited_by"]), f"frozen cited_by drift: {ref}")

        actual = _remote_branch_sha(repo, ref)
        _require(actual == sha, f"protected remote ref tip drift: {ref}: expected {sha}, got {actual}")

        for citation, citation_path in zip(cited_by, citation_paths):
            _require(
                _citation_contains_anchor(citation_path, sha, ref, state),
                f"citation anchor missing for {ref}: {citation}",
            )

    missing = set(FROZEN_CONTRACT) - names
    _require(not missing, "protected ref inventory incomplete: " + ", ".join(sorted(missing)))


if __name__ == "__main__":
    try:
        validate(Path("."))
    except (BranchPreservationError, json.JSONDecodeError) as exc:
        raise SystemExit(f"BRANCH_PRESERVATION_INVALID: {exc}")
    print("BRANCH_PRESERVATION_VALID")
