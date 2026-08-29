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

# Deliberately duplicated from the manifest. Changing/removing one of these
# preservation obligations must therefore be an explicit validator change,
# not a manifest-only weakening hidden inside an unrelated PR.
FROZEN_REF_TIPS = {
    "agent/adr0023-evidence-finalization": "c9d3944627b40619002428d2a37b8621b2cbfe3b",
    "agent/c4-offline-shadow": "b7786c088ef2cfd203c02625a5e0c40129cbf148",
    "agent/iar-1-review-request": "3ca47783cf1b4bde46158bce5aa183ceed82d0f5",
    "agent/iar1-late-review-followup": "157be487a6727cf0ec2a36988ad5ab203ba5e0b2",
    "agent/operator-decision-packages": "57c14742f705f96e33e929e7e206f14169d42fc0",
    "agent/p3-replay-projections": "7e615bc633cbf966211d3b2815f51b8ff9eb9716",
    "agent/p4-conformance-adapter": "0e7adf71475d37d5c096718762cbc08086c5e465",
    "agent/p5-sqlite-c3": "6483c9a229aea7d49929745b7652e67f1c39949c",
    "agent/pr85-post-merge-review-fixes": "c3b8695bf3d7207ac4c6b19dcb5e9e2bda92f764",
    "agent/sqlite-integrity-wal-safety": "ab7a203ce7ed8ec46c341bc4da9063d56f023338",
    "archive/bootstrap-v0.1.2.1-docs-lineage": "d64855afc4b34bcfb0ed8f1c3766925d287b07c6",
    "bootstrap/research-kernel-v0.1.2.1": "d64855afc4b34bcfb0ed8f1c3766925d287b07c6",
    "research/h11-family-selection": "d9273a22c411467109112f1fc6ea263ed8819d1d",
    "research/h11-preregistration": "1dca13cdd2759c70d810f44977a227fe1147d4bb",
    "research/residual-a10-validation-plan": "918ac46f4d93f085171b03564f9fbe30f543b200",
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
        _require(ref in FROZEN_REF_TIPS, f"unexpected protected ref requires explicit validator update: {ref}")
        _require(isinstance(sha, str) and FULL_SHA.fullmatch(sha) is not None, f"full 40-char SHA required: {ref}")
        _require(sha == FROZEN_REF_TIPS[ref], f"frozen protected tip drift: {ref}")
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

    missing = set(FROZEN_REF_TIPS) - names
    _require(not missing, "protected ref inventory incomplete: " + ", ".join(sorted(missing)))


if __name__ == "__main__":
    try:
        validate(Path("."))
    except (BranchPreservationError, json.JSONDecodeError) as exc:
        raise SystemExit(f"BRANCH_PRESERVATION_INVALID: {exc}")
    print("BRANCH_PRESERVATION_VALID")
