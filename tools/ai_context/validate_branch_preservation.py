#!/usr/bin/env python3
"""Fail-closed validator for repository branch-preservation safety records."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any

PROTOCOL = "nk-branch-preservation/1"
MANIFEST = Path("evidence/branch-preservation-v1.json")
FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
ALLOWED_MIGRATION = {"PENDING_MAIN_REACHABLE_ANCHOR", "INTENTIONAL_LONG_LIVED_LINEAGE"}
MIN_CITATION_PREFIX = 12


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


def _current_repo_files(repo: Path, excluded: Path) -> list[Path]:
    excluded = excluded.resolve()
    return [
        p for p in repo.rglob("*")
        if p.is_file() and ".git" not in p.parts and p.resolve() != excluded
    ]


def _sha_is_cited(repo: Path, sha: str, manifest_path: Path) -> bool:
    needle = sha[:MIN_CITATION_PREFIX]
    for path in _current_repo_files(repo, manifest_path):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if needle in text:
            return True
    return False


def validate(repo: Path, manifest_path: Path | None = None) -> None:
    repo = repo.resolve()
    path = (manifest_path or repo / MANIFEST).resolve()
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))

    _require(data.get("protocol") == PROTOCOL, "branch preservation protocol drift")
    boundary = data.get("authority_boundary")
    _require(isinstance(boundary, dict), "authority boundary required")
    for key in (
        "h11_outcome_changed", "runtime_authorized", "canon_authorized",
        "production_authorized", "branch_deletion_authorized", "auto_delete_authorized",
    ):
        _require(boundary.get(key) is False, f"authority boundary must remain false: {key}")

    refs = data.get("protected_refs")
    _require(isinstance(refs, list) and refs, "protected_refs must be non-empty")
    names: set[str] = set()

    for item in refs:
        _require(isinstance(item, dict), "protected ref entry must be an object")
        ref = item.get("ref")
        sha = item.get("tip_sha")
        state = item.get("migration_state")
        reason = item.get("reason")
        _require(isinstance(ref, str) and ref and ref not in names, f"duplicate/invalid ref: {ref}")
        names.add(ref)
        _require(isinstance(sha, str) and FULL_SHA.fullmatch(sha) is not None, f"full 40-char SHA required: {ref}")
        _require(isinstance(reason, str) and reason.strip(), f"reason required: {ref}")
        _require(state in ALLOWED_MIGRATION, f"invalid migration_state: {ref}")

        remote = f"refs/remotes/origin/{ref}"
        try:
            actual = _git(repo, "rev-parse", remote)
        except BranchPreservationError:
            actual = _git(repo, "rev-parse", f"refs/heads/{ref}")
        _require(actual == sha, f"protected ref tip drift: {ref}: expected {sha}, got {actual}")

        if state == "PENDING_MAIN_REACHABLE_ANCHOR":
            _require(
                _sha_is_cited(repo, sha, path),
                f"protected historical SHA prefix is no longer cited outside the preservation manifest: {ref}",
            )


if __name__ == "__main__":
    try:
        validate(Path("."))
    except (BranchPreservationError, json.JSONDecodeError) as exc:
        raise SystemExit(f"BRANCH_PRESERVATION_INVALID: {exc}")
    print("BRANCH_PRESERVATION_VALID")
