#!/usr/bin/env python3
"""Fail closed when ADR-0025's architecture runtime freeze drifts."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping

EXPECTED_DELIVERABLES = [
    "A1_KERNEL_PURPOSE_AND_NON_GOALS",
    "A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY",
    "A3_ABSTRACT_NATIVE_KERNEL_MACHINE",
    "A4_SEMANTIC_LAWS_AND_INVARIANTS",
    "A5_IDENTITY_TIME_AND_CHANGE",
    "A6_KNOWLEDGE_LIFECYCLE",
    "A7_CONFLICT_UNCERTAINTY_AND_REVISION",
    "A8_SUBSTRATE_INDEPENDENCE_CONTRACT",
    "A9_REFERENCE_LABORATORY_BOUNDARY",
    "A10_OPEN_QUESTIONS_AND_FALSIFICATION",
]
EXPECTED_FREEZE_EXCEPTIONS = [
    "integrity and security fixes",
    "reproducibility and provenance corrections",
    "evidence preservation",
    "validator and current-truth repairs",
    "historical recovery",
    "isolated blueprint falsification experiments without runtime promotion",
]
EXPECTED_PROMOTION_REQUIREMENTS = [
    "explicit ontology or semantic law",
    "abstract machine or contract",
    "failure and falsification cases",
    "separate decision record",
    "operator approval",
]
EXPECTED_REFOUNDATION_FIELDS = {
    "decision",
    "issue",
    "operator_approval",
    "status",
    "runtime_expansion_frozen",
    "existing_reference_runtime_role",
    "plan_en",
    "plan_ru",
    "deliverables",
    "completion_requires_operator_review",
    "next_content_slice",
}


class ArchitectureFreezeError(RuntimeError):
    """Raised when machine state can silently reopen runtime expansion."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ArchitectureFreezeError(message)


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ArchitectureFreezeError(f"cannot read project state: {exc}") from exc
    _require(isinstance(value, dict), "project state must contain an object")
    return value


def validate(state: Mapping[str, Any], *, repo: Path) -> None:
    _require(
        state.get("protocol") == "nk-project-state/2",
        "unsupported project-state protocol",
    )

    status = state.get("status")
    _require(isinstance(status, Mapping), "status object required")
    _require(
        status.get("production_authorized") is False,
        "ADR-0025 cannot coexist with production authorization",
    )

    tracks = state.get("tracks")
    _require(isinstance(tracks, Mapping), "tracks object required")

    clean = tracks.get("clean_implementation")
    _require(isinstance(clean, Mapping), "clean implementation track required")
    _require(
        clean.get("architecture_role") == "BOUNDED_REFERENCE_LABORATORY",
        "clean implementation must remain a bounded reference laboratory",
    )
    _require(
        clean.get("semantic_runtime_expansion_authorized") is False,
        "semantic/runtime expansion is not authorized",
    )
    _require(
        clean.get("maintenance_allowed") is True,
        "bounded maintenance allowance must remain explicit",
    )

    research = tracks.get("long_horizon_research")
    _require(isinstance(research, Mapping), "long-horizon research track required")
    _require(research.get("id") == "R", "research track id must be R")
    _require(
        research.get("status")
        == "ACTIVE / ARCHITECTURE RE-FOUNDATION / NO AUTOMATIC PROMOTION",
        "architecture re-foundation status drift",
    )
    _require(
        research.get("runtime_authorized") is False,
        "research track must not authorize runtime",
    )

    refoundation = research.get("architecture_refoundation")
    _require(
        isinstance(refoundation, Mapping),
        "ADR-0025 architecture_refoundation object required",
    )
    _require(
        set(refoundation) == EXPECTED_REFOUNDATION_FIELDS,
        "architecture_refoundation field inventory drift",
    )
    _require(
        (
            refoundation.get("decision"),
            refoundation.get("issue"),
            refoundation.get("operator_approval"),
            refoundation.get("status"),
        )
        == ("ADR-0025", 88, "APPROVED", "ACTIVE / BLUEPRINT-FIRST"),
        "ADR-0025 identity, issue, approval or phase drift",
    )
    _require(
        refoundation.get("runtime_expansion_frozen") is True,
        "runtime expansion freeze must remain enabled",
    )
    _require(
        refoundation.get("existing_reference_runtime_role")
        == "BOUNDED_REFERENCE_LABORATORY",
        "existing runtime role drift",
    )
    _require(
        refoundation.get("plan_en") == "docs/ARCHITECTURE_REFOUNDATION.md"
        and refoundation.get("plan_ru")
        == "docs/ARCHITECTURE_REFOUNDATION.ru.md",
        "architecture blueprint plan identity drift",
    )
    _require(
        refoundation.get("deliverables") == EXPECTED_DELIVERABLES,
        "A1-A10 blueprint deliverable inventory drift",
    )
    _require(
        refoundation.get("completion_requires_operator_review") is True,
        "blueprint completion must retain separate operator review",
    )
    _require(
        refoundation.get("next_content_slice")
        == "A1_KERNEL_PURPOSE_AND_NON_GOALS",
        "next blueprint content slice drift",
    )

    for plan_field in ("plan_en", "plan_ru"):
        plan = repo / str(refoundation[plan_field])
        _require(plan.is_file(), f"missing architecture blueprint plan: {plan}")

    _require(
        research.get("runtime_freeze_exceptions") == EXPECTED_FREEZE_EXCEPTIONS,
        "runtime freeze exception inventory drift",
    )
    _require(
        research.get("canonical_promotion_requires")
        == EXPECTED_PROMOTION_REQUIREMENTS,
        "canonical promotion requirement inventory drift",
    )

    issues = state.get("issues")
    _require(isinstance(issues, Mapping), "issue snapshots required")
    issue = issues.get("88")
    _require(isinstance(issue, Mapping), "Issue #88 snapshot required")
    _require(issue.get("state") == "OPEN", "Issue #88 must remain open")
    _require(
        "Architecture Re-foundation" in str(issue.get("meaning", "")),
        "Issue #88 meaning drift",
    )
    verification = issue.get("verification")
    _require(isinstance(verification, Mapping), "Issue #88 verification required")
    _require(
        verification.get("status") == "VERIFIED"
        and verification.get("method") == "GITHUB_API"
        and verification.get("source") == "issue/88",
        "Issue #88 verification drift",
    )

    non_claims = " ".join(
        str(item).lower() for item in state.get("non_claims", [])
    )
    for phrase in (
        "architecture re-foundation documentation is not runtime implementation evidence",
        "future-facing blueprint does not prove compatibility with arbitrary future substrates",
    ):
        _require(phrase in non_claims, f"missing architecture boundary: {phrase}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "state",
        nargs="?",
        type=Path,
        default=Path("project-state.json"),
    )
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)

    repo = args.repo.resolve()
    state_path = args.state if args.state.is_absolute() else repo / args.state
    try:
        validate(_load(state_path), repo=repo)
    except ArchitectureFreezeError as exc:
        print(f"Architecture freeze validation failed: {exc}", file=sys.stderr)
        return 1

    print(
        "Architecture freeze validation passed; "
        "decision=ADR-0025; issue=88; deliverables=A1-A10; "
        "runtime_expansion_frozen=true"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
