#!/usr/bin/env python3
"""Fail-closed validator for repository branch-preservation safety records."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path, PurePosixPath
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


def _resolve_citation(repo: Path, raw: str, manifest_path: Path) -> Path:
    _require(isinstance(raw, str) and raw.strip(), "citation path must be a non-empty string")
    relative = PurePosixPath(raw)
    _require(not relative.is_absolute(), f"citation path must be repository-relative: {raw}")
    _require(".." not in relative.parts, f"citation path escapes repository: {raw}")
    candidate = (repo / Path(*relative.parts)).resolve()
    try:
        candidate.relative_to(repo)
    except ValueError as exc:
        raise BranchPreservationError(f"citation path escapes repository: {raw}") from exc
    _require(candidate != manifest_path.resolve(), "preservation manifest cannot self-satisfy a citation")
    _require(candidate.is_file(), f"citation file required: {raw}")
    return candidate


def _citation_contains_anchor(path: Path, sha: str, ref: str, state: str) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as exc:
        raise BranchPreservationError(f"citation file must be readable UTF-8 text: {path}") from exc
    if state == "PENDING_MAIN_REACHABLE_ANCHOR":
        return sha[:MIN_CITATION_PREFIX] in text
    return sha[:MIN_CITATION_PREFIX] in text or ref in text


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
        cited_by = item.get("cited_by")

        _require(isinstance(ref, str) and ref and ref not in names, f"duplicate/invalid ref: {ref}")
        names.add(ref)
        _require(isinstance(sha, str) and FULL_SHA.fullmatch(sha) is not None, f"full 40-char SHA required: {ref}")
        _require(isinstance(reason, str) and reason.strip(), f"reason required: {ref}")
        _require(state in ALLOWED_MIGRATION, f"invalid migration_state: {ref}")
        _require(isinstance(cited_by, list) and cited_by, f"cited_by must be non-empty: {ref}")
        _require(all(isinstance(value, str) and value.strip() for value in cited_by), f"invalid cited_by path: {ref}")
        _require(len(set(cited_by)) == len(cited_by), f"duplicate cited_by path: {ref}")

        remote = f"refs/remotes/origin/{ref}"
        try:
            actual = _git(repo, "rev-parse", remote)
        except BranchPreservationError:
            actual = _git(repo, "rev-parse", f"refs/heads/{ref}")
        _require(actual == sha, f"protected ref tip drift: {ref}: expected {sha}, got {actual}")

        for citation in cited_by:
            citation_path = _resolve_citation(repo, citation, path)
            _require(
                _citation_contains_anchor(citation_path, sha, ref, state),
                f"citation anchor missing for {ref}: {citation}",
            )


if __name__ == "__main__":
    try:
        validate(Path("."))
    except (BranchPreservationError, json.JSONDecodeError) as exc:
        raise SystemExit(f"BRANCH_PRESERVATION_INVALID: {exc}")
    print("BRANCH_PRESERVATION_VALID")
