#!/usr/bin/env python3
"""Fail-closed validator for migrated historical evidence anchors."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path, PurePosixPath
from typing import Any

PROTOCOL = "nk-evidence-anchor-migration/1"
STATUS = "BOUNDED_PROVENANCE_MIGRATION"
MANIFEST = Path("evidence/evidence-anchor-migration-v1.json")
MAIN_REF = "refs/remotes/origin/main"
FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
MIN_CITATION_PREFIX = 12

TOP_LEVEL_KEYS = {"protocol", "status", "authority_boundary", "policy", "migrations"}
AUTHORITY_KEYS = {
    "branch_deletion_authorized",
    "auto_delete_authorized",
    "h11_outcome_changed",
    "runtime_authorized",
    "canon_authorized",
    "production_authorized",
}
POLICY_KEYS = {
    "historical_identity_retained",
    "durable_checkpoint_requirement",
    "deletion_requires_separate_owner_action",
}
ENTRY_KEYS = {
    "ref",
    "historical_head_sha",
    "pull_request",
    "durable_main_sha",
    "cited_by",
    "migration_state",
}
EXPECTED_POLICY = {
    "historical_identity_retained": True,
    "durable_checkpoint_requirement": "MERGED_PR_MAIN_REACHABLE_CHECKPOINT",
    "deletion_requires_separate_owner_action": True,
}
MIGRATION_STATE = "DURABLE_MAIN_CHECKPOINT_RECORDED"

FROZEN_MIGRATIONS = {
    "agent/adr0023-evidence-finalization": {"historical_head_sha":"c9d3944627b40619002428d2a37b8621b2cbfe3b","pull_request":70,"durable_main_sha":"f13e0c8a948789d8d4e93e95fd95b61324478528","cited_by":("docs/ai/WORK_LOG.md",)},
    "agent/c4-offline-shadow": {"historical_head_sha":"b7786c088ef2cfd203c02625a5e0c40129cbf148","pull_request":62,"durable_main_sha":"07bf1cc955307783f8eaa3becbaa924087b8b325","cited_by":("docs/ai/C4_IMPLEMENTATION_RECORD.md",)},
    "agent/iar-1-review-request": {"historical_head_sha":"3ca47783cf1b4bde46158bce5aa183ceed82d0f5","pull_request":107,"durable_main_sha":"845f2c8e9322c5353f9d6b421e44d1da71b82f58","cited_by":("docs/reviews/IAR-1_LATE_REVIEW_FOLLOWUP.md",)},
    "agent/iar1-late-review-followup": {"historical_head_sha":"157be487a6727cf0ec2a36988ad5ab203ba5e0b2","pull_request":108,"durable_main_sha":"e465b7019040913c3a5bd2d4344eb2dea74cc60c","cited_by":("docs/reviews/IAR-1_LATE_REVIEW_FOLLOWUP.md",)},
    "agent/operator-decision-packages": {"historical_head_sha":"57c14742f705f96e33e929e7e206f14169d42fc0","pull_request":83,"durable_main_sha":"10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c","cited_by":("docs/ai/ISSUE_RECONCILIATION.md",)},
    "agent/p3-replay-projections": {"historical_head_sha":"7e615bc633cbf966211d3b2815f51b8ff9eb9716","pull_request":50,"durable_main_sha":"4af642930e18752f8f8b0bce75df355f76100d6f","cited_by":("docs/ai/P3_IMPLEMENTATION_RECORD.md",)},
    "agent/p4-conformance-adapter": {"historical_head_sha":"0e7adf71475d37d5c096718762cbc08086c5e465","pull_request":56,"durable_main_sha":"db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad","cited_by":("docs/ai/P4_IMPLEMENTATION_RECORD.md",)},
    "agent/p5-sqlite-c3": {"historical_head_sha":"6483c9a229aea7d49929745b7652e67f1c39949c","pull_request":59,"durable_main_sha":"a8bb0ae232b977856730a1a4f21f977c1f69ca0a","cited_by":("docs/ai/P5_IMPLEMENTATION_RECORD.md",)},
    "agent/pr85-post-merge-review-fixes": {"historical_head_sha":"c3b8695bf3d7207ac4c6b19dcb5e9e2bda92f764","pull_request":86,"durable_main_sha":"70acd0da61fee19131947aa56125833adb156ced","cited_by":("docs/ai/NOTION_HANDOFF.md",)},
    "agent/sqlite-integrity-wal-safety": {"historical_head_sha":"ab7a203ce7ed8ec46c341bc4da9063d56f023338","pull_request":69,"durable_main_sha":"675aa4b398a2fc0181dc71d38904a2d33a09f5f8","cited_by":("docs/ai/P5_IMPLEMENTATION_RECORD.md",)},
    "research/h11-family-selection": {"historical_head_sha":"d9273a22c411467109112f1fc6ea263ed8819d1d","pull_request":126,"durable_main_sha":"bcd3b3f6c9d898315c93e5d24b5d0e02c95508cc","cited_by":("project-state.json","tools/ai_context/validate_project_state.py")},
    "research/h11-preregistration": {"historical_head_sha":"1dca13cdd2759c70d810f44977a227fe1147d4bb","pull_request":127,"durable_main_sha":"4a75ff15542013c033030620bdff61997e365140","cited_by":("project-state.json","tools/ai_context/validate_project_state.py")},
    "research/residual-a10-validation-plan": {"historical_head_sha":"918ac46f4d93f085171b03564f9fbe30f543b200","pull_request":124,"durable_main_sha":"edc0501d71a827462aafd1ac4497920a719a4519","cited_by":("project-state.json","tools/ai_context/validate_project_state.py")},
}


class EvidenceAnchorMigrationError(RuntimeError):
    pass


def _require(value: bool, message: str) -> None:
    if not value:
        raise EvidenceAnchorMigrationError(message)


def _git(repo: Path, *args: str) -> str:
    proc = subprocess.run(["git", "-C", str(repo), *args], text=True, capture_output=True)
    if proc.returncode != 0:
        raise EvidenceAnchorMigrationError(proc.stderr.strip() or "git command failed")
    return proc.stdout.strip()


def _is_ancestor(repo: Path, ancestor: str, descendant: str) -> bool:
    proc = subprocess.run(["git", "-C", str(repo), "merge-base", "--is-ancestor", ancestor, descendant], text=True, capture_output=True)
    return proc.returncode == 0


def _resolve_citation(repo: Path, raw: str, manifest_path: Path) -> tuple[Path, str]:
    _require(isinstance(raw, str) and raw.strip(), "citation path must be a non-empty string")
    relative = PurePosixPath(raw)
    _require(not relative.is_absolute(), f"citation path must be repository-relative: {raw}")
    _require(".." not in relative.parts, f"citation path escapes repository: {raw}")
    candidate = (repo / Path(*relative.parts)).resolve()
    try:
        normalized = candidate.relative_to(repo).as_posix()
    except ValueError as exc:
        raise EvidenceAnchorMigrationError(f"citation path escapes repository: {raw}") from exc
    _require(candidate != manifest_path.resolve(), "migration manifest cannot self-satisfy a citation")
    _require(candidate.is_file(), f"citation file required: {raw}")
    return candidate, normalized


def _contains_historical_identity(path: Path, sha: str) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as exc:
        raise EvidenceAnchorMigrationError(f"citation file must be readable UTF-8 text: {path}") from exc
    return sha[:MIN_CITATION_PREFIX] in text


def _exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    _require(set(value) == expected, f"{label} keys drift")


def validate(repo: Path, manifest_path: Path | None = None) -> None:
    repo = repo.resolve()
    path = (manifest_path or repo / MANIFEST).resolve()
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))

    _require(isinstance(data, dict), "migration manifest must be an object")
    _exact_keys(data, TOP_LEVEL_KEYS, "top-level migration manifest")
    _require(data.get("protocol") == PROTOCOL, "migration protocol drift")
    _require(data.get("status") == STATUS, "migration status drift")

    boundary = data.get("authority_boundary")
    _require(isinstance(boundary, dict), "authority boundary required")
    _exact_keys(boundary, AUTHORITY_KEYS, "authority_boundary")
    for key in AUTHORITY_KEYS:
        _require(boundary.get(key) is False, f"authority boundary must remain false: {key}")

    policy = data.get("policy")
    _require(isinstance(policy, dict), "migration policy required")
    _exact_keys(policy, POLICY_KEYS, "policy")
    _require(policy == EXPECTED_POLICY, "migration policy drift")

    _require(_git(repo, "rev-parse", MAIN_REF), f"main ref required: {MAIN_REF}")

    migrations = data.get("migrations")
    _require(isinstance(migrations, list) and migrations, "migrations must be non-empty")
    names: set[str] = set()

    for item in migrations:
        _require(isinstance(item, dict), "migration entry must be an object")
        _exact_keys(item, ENTRY_KEYS, "migration entry")
        ref = item.get("ref")
        historical = item.get("historical_head_sha")
        pr = item.get("pull_request")
        durable = item.get("durable_main_sha")
        cited_by = item.get("cited_by")
        state = item.get("migration_state")

        _require(isinstance(ref, str) and ref and ref not in names, f"duplicate/invalid migrated ref: {ref}")
        names.add(ref)
        _require(ref in FROZEN_MIGRATIONS, f"unexpected migration requires explicit validator update: {ref}")
        frozen = FROZEN_MIGRATIONS[ref]
        _require(isinstance(historical, str) and FULL_SHA.fullmatch(historical) is not None, f"full historical SHA required: {ref}")
        _require(isinstance(durable, str) and FULL_SHA.fullmatch(durable) is not None, f"full durable SHA required: {ref}")
        _require(historical != durable, f"historical and durable identities must remain distinct: {ref}")
        _require(historical == frozen["historical_head_sha"], f"historical identity drift: {ref}")
        _require(pr == frozen["pull_request"], f"pull request identity drift: {ref}")
        _require(durable == frozen["durable_main_sha"], f"durable main checkpoint drift: {ref}")
        _require(state == MIGRATION_STATE, f"migration state drift: {ref}")
        _require(isinstance(cited_by, list) and cited_by, f"cited_by must be non-empty: {ref}")

        normalized: list[str] = []
        citation_paths: list[Path] = []
        for citation in cited_by:
            citation_path, normalized_path = _resolve_citation(repo, citation, path)
            normalized.append(normalized_path)
            citation_paths.append(citation_path)
        _require(len(set(normalized)) == len(normalized), f"duplicate normalized cited_by path: {ref}")
        _require(tuple(normalized) == tuple(frozen["cited_by"]), f"frozen cited_by drift: {ref}")
        _require(_is_ancestor(repo, durable, MAIN_REF), f"durable checkpoint is not reachable from origin/main: {ref}")
        for citation, citation_path in zip(cited_by, citation_paths):
            _require(_contains_historical_identity(citation_path, historical), f"historical identity missing from citation for {ref}: {citation}")

    missing = set(FROZEN_MIGRATIONS) - names
    _require(not missing, "migration inventory incomplete: " + ", ".join(sorted(missing)))


if __name__ == "__main__":
    try:
        validate(Path("."))
    except (EvidenceAnchorMigrationError, json.JSONDecodeError) as exc:
        raise SystemExit(f"EVIDENCE_ANCHOR_MIGRATION_INVALID: {exc}")
    print("EVIDENCE_ANCHOR_MIGRATION_VALID")
