#!/usr/bin/env python3
"""Validate Native Kernel's machine-readable project truth surfaces."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Mapping

SHA_RE = re.compile(r"^[0-9a-f]{40}$")
HEAD_RELATIONSHIPS = {"EXACT", "DESCENDANT_OR_EQUAL", "UNRELATED", "UNKNOWN"}
ASSERTION_MAP = {
    "supported": 45,
    "partial": 10,
    "unsupported": 17,
    "failed": 0,
    "total": 72,
}
CONTRACT_FAMILIES = {
    "NK-SEM",
    "NK-ID",
    "NK-EVT",
    "NK-AUT",
    "NK-CFL",
    "NK-EQV",
    "NK-EPI",
}
CHECKPOINT_FIELDS = (
    "manifest_generated_from_sha",
    "runtime_checkpoint_sha",
    "runtime_integrity_checkpoint_sha",
    "evidence_producing_sha",
    "publication_checkpoint_sha",
    "notion_synchronized_through_sha",
)
NOTION_STATUSES = {
    "HANDOFF_REQUIRED",
    "SYNCED_THROUGH_PUBLICATION_CHECKPOINT",
    "SYNCED_THROUGH_DESCENDANT_CHECKPOINT",
}


class ProjectStateError(RuntimeError):
    """Raised when project-state validation fails closed."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ProjectStateError(message)


def _load(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ProjectStateError(f"cannot read {label}: {exc}") from exc
    _require(isinstance(value, dict), f"{label} must contain an object")
    return value


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def _validate_registry(
    registry: Mapping[str, Any], state: Mapping[str, Any]
) -> None:
    _require(
        registry.get("registry_version") == "nk-contract-registry/1.1.0",
        "unexpected contract registry version",
    )
    _require(
        registry.get("status_metadata_version")
        == "nk-contract-registry-status/1",
        "contract registry status metadata version is missing or unsupported",
    )
    _require(
        "runtime_status" not in registry,
        "legacy registry runtime_status is forbidden because it collapses family support",
    )
    _require(
        registry.get("implementation_support") == "PARTIAL",
        "registry implementation support must remain PARTIAL",
    )

    runtime_summary = registry.get("runtime_summary")
    _require(
        isinstance(runtime_summary, Mapping),
        "registry runtime summary required",
    )
    project_status = state["status"]
    for key in (
        "clean_runtime_support",
        "kernel_runtime_conformance",
        "operational_validation",
        "production_authorized",
    ):
        _require(
            runtime_summary.get(key) == project_status.get(key),
            f"registry/project-state mismatch: {key}",
        )

    _require(
        registry.get("assertion_evidence_summary") == state["assertion_map"],
        "registry assertion evidence summary drift",
    )

    families = registry.get("families")
    _require(isinstance(families, list), "registry families must be a list")
    family_index: dict[str, Mapping[str, Any]] = {}
    assertion_ids: set[str] = set()
    for family in families:
        _require(
            isinstance(family, Mapping),
            "registry family must be an object",
        )
        family_id = family.get("family_id")
        _require(
            isinstance(family_id, str) and family_id,
            "registry family_id required",
        )
        _require(
            family_id not in family_index,
            f"duplicate registry family: {family_id}",
        )
        family_index[family_id] = family
        assertions = family.get("assertions")
        _require(
            isinstance(assertions, list),
            f"{family_id}: assertions must be a list",
        )
        for assertion in assertions:
            _require(
                isinstance(assertion, Mapping),
                f"{family_id}: assertion must be an object",
            )
            assertion_id = assertion.get("assertion_id")
            _require(
                isinstance(assertion_id, str) and assertion_id,
                f"{family_id}: assertion_id required",
            )
            _require(
                assertion_id not in assertion_ids,
                f"duplicate assertion: {assertion_id}",
            )
            assertion_ids.add(assertion_id)

    _require(
        set(family_index) == CONTRACT_FAMILIES,
        "registry family inventory drift",
    )
    _require(
        len(assertion_ids) == 72,
        "registry must contain exactly 72 unique assertions",
    )

    for family_id, family in family_index.items():
        if family_id == "NK-EPI":
            _require(
                family.get("decision_status") == "PROPOSED",
                "NK-EPI must remain proposed",
            )
            _require(
                (
                    family.get("implementation_support"),
                    family.get("fixture_support"),
                    family.get("evidence_level"),
                )
                == ("NOT_IMPLEMENTED", "NOT_IMPLEMENTED", "NONE"),
                "NK-EPI support overclaim",
            )
            continue

        _require(
            family.get("decision_status") == "ACCEPTED",
            f"{family_id}: decision status drift",
        )
        _require(
            (
                family.get("implementation_support"),
                family.get("fixture_support"),
                family.get("evidence_level"),
            )
            == ("PARTIAL", "PARTIAL", "C4_PARTIAL"),
            f"{family_id}: implementation, fixture or evidence support drift",
        )


def _validate_checkpoint_relationships(
    checkpoints: Mapping[str, Any], *, repo: Path, check_git: bool
) -> None:
    for field in CHECKPOINT_FIELDS:
        value = checkpoints.get(field)
        _require(
            isinstance(value, str) and SHA_RE.fullmatch(value) is not None,
            f"invalid checkpoint SHA: {field}",
        )

    relationship = checkpoints.get("expected_head_relationship")
    _require(
        relationship in HEAD_RELATIONSHIPS,
        "invalid expected HEAD relationship",
    )
    _require(
        checkpoints["manifest_generated_from_sha"]
        == checkpoints["notion_synchronized_through_sha"],
        "manifest/Notion checkpoint mismatch",
    )
    _require(
        isinstance(checkpoints.get("checkpoint_semantics"), str)
        and checkpoints["checkpoint_semantics"].strip(),
        "checkpoint semantics required",
    )

    if not check_git or not (repo / ".git").exists():
        return

    head_result = _git(repo, "rev-parse", "HEAD")
    _require(head_result.returncode == 0, "cannot resolve repository HEAD")
    head = head_result.stdout.strip()

    for field in CHECKPOINT_FIELDS:
        sha = checkpoints[field]
        _require(
            _git(repo, "cat-file", "-e", f"{sha}^{{commit}}").returncode
            == 0,
            f"{field} commit does not exist: {sha}",
        )

    source = checkpoints["manifest_generated_from_sha"]
    if relationship == "EXACT":
        _require(source == head, "manifest source must equal HEAD")
    elif relationship == "DESCENDANT_OR_EQUAL":
        _require(
            _git(repo, "merge-base", "--is-ancestor", source, head).returncode
            == 0,
            "manifest source is not an ancestor of HEAD",
        )
    elif relationship == "UNRELATED":
        _require(
            _git(repo, "merge-base", "--is-ancestor", source, head).returncode
            != 0,
            "manifest source is unexpectedly an ancestor of HEAD",
        )

    for field in CHECKPOINT_FIELDS[1:]:
        sha = checkpoints[field]
        _require(
            _git(repo, "merge-base", "--is-ancestor", sha, head).returncode
            == 0,
            f"{field} is not an ancestor of HEAD",
        )

    publication = checkpoints["publication_checkpoint_sha"]
    notion_checkpoint = checkpoints["notion_synchronized_through_sha"]
    _require(
        _git(
            repo,
            "merge-base",
            "--is-ancestor",
            publication,
            notion_checkpoint,
        ).returncode
        == 0,
        "publication checkpoint is not an ancestor of the Notion checkpoint",
    )


def validate(
    state: Mapping[str, Any],
    *,
    repo: Path,
    registry: Mapping[str, Any] | None = None,
    check_git: bool = True,
) -> None:
    _require(
        state.get("protocol") == "nk-project-state/2",
        "unsupported project-state protocol",
    )

    repository = state.get("repository")
    _require(isinstance(repository, Mapping), "repository object required")
    _require(
        (
            repository.get("full_name"),
            repository.get("visibility"),
            repository.get("default_branch"),
        )
        == ("velantrian/velantrim-native-kernel", "PUBLIC", "main"),
        "repository identity or visibility drift",
    )

    checkpoints = state.get("checkpoints")
    _require(isinstance(checkpoints, Mapping), "checkpoint inventory required")
    _validate_checkpoint_relationships(
        checkpoints,
        repo=repo,
        check_git=check_git,
    )

    status = state.get("status")
    _require(isinstance(status, Mapping), "status object required")
    _require(
        status.get("repository_status")
        == "RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY",
        "repository status drift",
    )
    _require(
        status.get("support_state")
        == status.get("clean_runtime_support")
        == "PARTIAL",
        "runtime support must remain PARTIAL",
    )
    _require(
        (
            status.get("kernel_runtime_conformance"),
            status.get("operational_validation"),
            status.get("production_authorized"),
        )
        == ("C4", "C5_BOUNDED_REHEARSAL", False),
        "maturity or production authorization drift",
    )

    tracks = state.get("tracks")
    _require(isinstance(tracks, Mapping), "tracks object required")
    _require(
        set(tracks)
        == {
            "historical_recovery",
            "clean_implementation",
            "long_horizon_research",
        },
        "exact H/C/R tracks required",
    )
    historical = tracks["historical_recovery"]
    clean = tracks["clean_implementation"]
    research = tracks["long_horizon_research"]
    _require(historical.get("id") == "H", "historical track id must be H")
    _require(
        historical.get("evidence_state")
        == "NOT_FOUND_IN_ACCESSIBLE_SOURCES",
        "historical evidence state drift",
    )
    _require(
        historical.get("blocks_clean_implementation") is False,
        "historical recovery must not block clean lineage",
    )
    _require(
        historical.get("may_claim_globally_lost") is False,
        "global-loss overclaim forbidden",
    )

    _require(
        clean.get("id") == "C"
        and clean.get("status") == "ACTIVE / PARTIAL",
        "clean track must remain active and partial",
    )
    phases = clean.get("phases")
    _require(
        isinstance(phases, Mapping)
        and set(phases) == {"P1", "P2", "P3", "P4", "P5", "C4", "C5"},
        "clean phase inventory drift",
    )
    integrity_review = clean.get("integrity_review")
    _require(
        isinstance(integrity_review, Mapping),
        "SQLite integrity review required",
    )
    _require(
        integrity_review.get("decision") == "ADR-0023",
        "SQLite integrity decision drift",
    )
    _require(
        integrity_review.get("status")
        == "REPOSITORY_REPRODUCED / EVIDENCE_CAPTURED",
        "SQLite integrity evidence must remain reproduced and captured",
    )
    _require(
        integrity_review.get("sqlite_wal_minimum") == "3.51.3",
        "unsafe SQLite WAL floor",
    )
    _require(
        integrity_review.get("historical_sqlite_version") == "3.45.1",
        "historical SQLite evidence drift",
    )
    _require(
        integrity_review.get("historical_evidence_preserved") is True,
        "historical evidence must remain preserved",
    )
    _require(
        integrity_review.get("affected_assertions_re_adjudicated") is True,
        "affected assertions must remain re-adjudicated",
    )
    _require(
        integrity_review.get("assertion_arithmetic_changed") is False,
        "assertion arithmetic cannot change implicitly",
    )

    _require(research.get("id") == "R", "research track id must be R")
    _require(
        research.get("runtime_authorized") is False,
        "research must not authorize runtime",
    )

    _require(state.get("assertion_map") == ASSERTION_MAP, "assertion map drift")
    nk_epi = state.get("nk_epi")
    _require(isinstance(nk_epi, Mapping), "NK-EPI object required")
    _require(
        (
            nk_epi.get("supported"),
            nk_epi.get("partial"),
            nk_epi.get("unsupported"),
            nk_epi.get("failed"),
        )
        == (0, 0, 8, 0),
        "NK-EPI map drift",
    )
    _require(
        nk_epi.get("decision_status") == "PROPOSED",
        "NK-EPI must remain proposed",
    )
    _require(
        nk_epi.get("implementation_support") == "NOT_IMPLEMENTED",
        "NK-EPI implementation support overclaim",
    )
    _require(
        nk_epi.get("promotion_authorized") is False,
        "NK-EPI promotion is not authorized",
    )

    issues = state.get("issues")
    _require(isinstance(issues, Mapping), "issue snapshots required")
    _require(
        issues.get("1", {}).get("state") == "OPEN",
        "Issue #1 state drift",
    )
    _require(
        issues.get("64", {}).get("state") == "CLOSED",
        "Issue #64 must be closed",
    )
    _require(
        issues.get("64", {}).get("state_reason") == "COMPLETED",
        "Issue #64 completion reason required",
    )
    for number in ("1", "64"):
        verification = issues[number].get("verification")
        _require(
            isinstance(verification, Mapping),
            f"Issue #{number} verification required",
        )
        _require(
            verification.get("status") == "VERIFIED",
            f"Issue #{number} must be directly verified",
        )
        _require(
            verification.get("method") == "GITHUB_API",
            f"Issue #{number} verification method drift",
        )

    evidence_map = state.get("evidence")
    _require(isinstance(evidence_map, Mapping), "evidence inventory required")
    c5_bundle = evidence_map.get("c5_bundle")
    _require(
        isinstance(c5_bundle, Mapping),
        "C5 durable evidence entry required",
    )
    _require(
        c5_bundle.get("protocol") == "nk-evidence-bundle/1",
        "evidence protocol drift",
    )
    _require(
        c5_bundle.get("status") == "CAPTURED_REPOSITORY_RESIDENT",
        "C5 bytes must remain repository-resident",
    )
    _require(
        c5_bundle.get("checkpoint_count") == 2
        and c5_bundle.get("artifact_count") == 8,
        "C5 evidence inventory drift",
    )
    _require(
        c5_bundle.get("original_archives_preserved") is True,
        "original C5 archives must remain preserved",
    )
    c5_path = repo / str(c5_bundle.get("path"))
    _require(c5_path.is_file(), "C5 evidence manifest missing")

    revalidation = evidence_map.get("sqlite_integrity_revalidation")
    _require(
        isinstance(revalidation, Mapping),
        "SQLite integrity revalidation entry required",
    )
    _require(
        revalidation.get("protocol") == "nk-evidence-bundle/1",
        "SQLite evidence protocol drift",
    )
    _require(
        revalidation.get("status") == "CAPTURED_REPOSITORY_RESIDENT",
        "SQLite revalidation evidence missing",
    )
    _require(
        revalidation.get("path")
        == "evidence/c5/2026-08-08-adr0023/manifest.json",
        "SQLite evidence identity drift",
    )
    _require(
        revalidation.get("checkpoint_count") == 2
        and revalidation.get("artifact_count") == 8,
        "SQLite evidence inventory drift",
    )
    _require(
        revalidation.get("required_profiles") == ["P5", "C3", "C4", "C5"],
        "SQLite evidence required-profile inventory drift",
    )
    _require(
        revalidation.get("minimum_linked_sqlite") == "3.51.3",
        "revalidation SQLite floor drift",
    )
    _require(
        revalidation.get("new_evidence_identity_required") is True,
        "new SQLite evidence identity required",
    )
    _require(
        revalidation.get("may_rewrite_2026_08_07_bundle") is False,
        "historical C5 bundle is immutable",
    )
    _require(
        revalidation.get("original_archives_preserved") is True,
        "original SQLite revalidation archives must remain preserved",
    )
    revalidation_path = repo / revalidation["path"]
    _require(
        revalidation_path.is_file(),
        "SQLite revalidation manifest missing",
    )

    notion = state.get("notion")
    _require(
        isinstance(notion, Mapping),
        "Notion synchronization state required",
    )
    _require(
        notion.get("synchronization_required") is True,
        "Notion synchronization must remain required",
    )
    notion_status = notion.get("status")
    _require(
        notion_status in NOTION_STATUSES,
        "invalid Notion synchronization state",
    )
    publication = checkpoints["publication_checkpoint_sha"]
    notion_checkpoint = checkpoints["notion_synchronized_through_sha"]
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
        _require(
            checkpoints["manifest_generated_from_sha"] == notion_checkpoint,
            "descendant synchronization manifest must use the Notion checkpoint",
        )

    non_claims = " ".join(
        str(item).lower() for item in state.get("non_claims", [])
    )
    for phrase in (
        "not production readiness",
        "does not promote nk-epi",
        "not recovered v0.1.2.1",
        "do not prove live-data safety",
        "preserved the assertion arithmetic",
        "does not silently broaden the proof scope",
        "does not rewrite or replace the earlier publication checkpoint",
    ):
        _require(
            phrase in non_claims,
            f"missing project-state boundary: {phrase}",
        )

    _validate_registry(
        registry
        or _load(repo / "contracts" / "registry.json", "contract registry"),
        state,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "state",
        nargs="?",
        type=Path,
        default=Path("project-state.json"),
    )
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
        f"source={checkpoints['manifest_generated_from_sha']}; "
        f"relationship={checkpoints['expected_head_relationship']}; "
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
