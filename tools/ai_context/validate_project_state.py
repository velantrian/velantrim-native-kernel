#!/usr/bin/env python3
"""Validate Native Kernel's machine-readable project-state snapshot."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Mapping

SHA_RE = re.compile(r"^[0-9a-f]{40}$")


class ProjectStateError(RuntimeError):
    """Raised when project-state validation fails closed."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ProjectStateError(message)


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ProjectStateError(f"cannot read project state: {exc}") from exc
    _require(isinstance(value, dict), "project-state top level must be an object")
    return value


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def validate(state: Mapping[str, Any], *, repo: Path, check_git: bool = True) -> None:
    _require(state.get("protocol") == "nk-project-state/1", "unsupported project-state protocol")

    repository = state.get("repository")
    _require(isinstance(repository, Mapping), "repository object required")
    _require(repository.get("full_name") == "velantrian/velantrim-native-kernel", "repository identity drift")
    _require(repository.get("visibility") == "PUBLIC", "repository visibility drift")
    _require(repository.get("default_branch") == "main", "default branch drift")
    observed = repository.get("observed_main_sha")
    implementation = repository.get("implementation_evidence_sha")
    _require(isinstance(observed, str) and SHA_RE.fullmatch(observed) is not None, "invalid observed main SHA")
    _require(isinstance(implementation, str) and SHA_RE.fullmatch(implementation) is not None, "invalid implementation evidence SHA")

    status = state.get("status")
    _require(isinstance(status, Mapping), "status object required")
    _require(
        status.get("repository_status")
        == "RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY",
        "repository status drift",
    )
    _require(status.get("support_state") == "PARTIAL", "support state must remain PARTIAL")
    _require(status.get("kernel_runtime_conformance") == "C4", "runtime conformance must remain C4")
    _require(status.get("operational_validation") == "C5_BOUNDED_REHEARSAL", "wrong operational validation")
    _require(status.get("production_authorized") is False, "production must remain unauthorized")

    tracks = state.get("tracks")
    _require(isinstance(tracks, Mapping), "tracks object required")
    _require(set(tracks) == {"historical_recovery", "clean_implementation", "long_horizon_research"}, "exact H/C/R tracks required")
    historical = tracks["historical_recovery"]
    clean = tracks["clean_implementation"]
    research = tracks["long_horizon_research"]
    _require(historical.get("id") == "H", "historical track id must be H")
    _require(historical.get("evidence_state") == "NOT_FOUND_IN_ACCESSIBLE_SOURCES", "historical evidence state drift")
    _require(historical.get("blocks_clean_implementation") is False, "historical recovery must not block clean lineage")
    _require(historical.get("may_claim_globally_lost") is False, "global-loss overclaim forbidden")
    _require(clean.get("id") == "C" and clean.get("status") == "ACTIVE / PARTIAL", "clean track must remain active/partial")
    phases = clean.get("phases")
    _require(isinstance(phases, Mapping) and set(phases) == {"P1", "P2", "P3", "P4", "P5", "C4", "C5"}, "clean phase inventory drift")
    _require(research.get("id") == "R", "research track id must be R")
    _require(research.get("runtime_authorized") is False, "research must not authorize runtime")

    assertion_map = state.get("assertion_map")
    _require(
        assertion_map == {"supported": 45, "partial": 10, "unsupported": 17, "failed": 0, "total": 72},
        "assertion map drift",
    )
    nk_epi = state.get("nk_epi")
    _require(isinstance(nk_epi, Mapping), "NK-EPI object required")
    _require(
        (nk_epi.get("supported"), nk_epi.get("partial"), nk_epi.get("unsupported"), nk_epi.get("failed"))
        == (0, 0, 8, 0),
        "NK-EPI map drift",
    )
    _require(nk_epi.get("decision_status") == "PROPOSED", "NK-EPI must remain proposed")
    _require(nk_epi.get("promotion_authorized") is False, "NK-EPI promotion is not authorized")

    issues = state.get("issues")
    _require(isinstance(issues, Mapping), "issue snapshots required")
    _require(issues.get("1", {}).get("state") == "OPEN", "Issue #1 state drift")
    _require(issues.get("64", {}).get("state") == "CLOSED", "Issue #64 must be closed")
    _require(issues.get("64", {}).get("state_reason") == "COMPLETED", "Issue #64 completion reason required")
    for number in ("1", "64"):
        verification = issues[number].get("verification")
        _require(isinstance(verification, Mapping), f"Issue #{number} verification required")
        _require(verification.get("status") == "VERIFIED", f"Issue #{number} must be directly verified")
        _require(verification.get("method") == "GITHUB_API", f"Issue #{number} verification method drift")

    evidence = state.get("evidence", {}).get("c5_bundle")
    _require(isinstance(evidence, Mapping), "C5 durable evidence entry required")
    _require(evidence.get("protocol") == "nk-evidence-bundle/1", "evidence protocol drift")
    _require(evidence.get("status") == "CAPTURED_REPOSITORY_RESIDENT", "C5 bytes must be repository-resident")
    _require(evidence.get("checkpoint_count") == 2 and evidence.get("artifact_count") == 8, "C5 evidence inventory drift")
    bundle_path = repo / str(evidence.get("path"))
    _require(bundle_path.is_file(), "C5 evidence manifest missing")

    non_claims = " ".join(str(item).lower() for item in state.get("non_claims", []))
    for phrase in ("not production readiness", "does not promote nk-epi", "not recovered v0.1.2.1", "do not prove live-data safety"):
        _require(phrase in non_claims, f"missing project-state boundary: {phrase}")

    if check_git and (repo / ".git").exists():
        for label, sha in (("observed main", observed), ("implementation evidence", implementation)):
            _require(_git(repo, "cat-file", "-e", f"{sha}^{{commit}}").returncode == 0, f"{label} commit does not exist")
            _require(_git(repo, "merge-base", "--is-ancestor", sha, "HEAD").returncode == 0, f"{label} SHA is not an ancestor of HEAD")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", nargs="?", type=Path, default=Path("project-state.json"))
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--no-git", action="store_true")
    args = parser.parse_args()
    repo = args.repo.resolve()
    state = _load(args.state if args.state.is_absolute() else repo / args.state)
    validate(state, repo=repo, check_git=not args.no_git)
    print(
        "Project-state validation passed; "
        f"checkpoint={state['repository']['observed_main_sha']}; "
        f"runtime={state['status']['kernel_runtime_conformance']}; "
        f"operational={state['status']['operational_validation']}; "
        f"assertions={state['assertion_map']['supported']}/"
        f"{state['assertion_map']['partial']}/"
        f"{state['assertion_map']['unsupported']}/"
        f"{state['assertion_map']['failed']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
