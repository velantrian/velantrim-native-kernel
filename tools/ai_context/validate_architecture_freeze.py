#!/usr/bin/env python3
"""Fail closed when the architecture validation/runtime-freeze boundary drifts."""
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
    "decision", "issue", "operator_approval", "status", "runtime_expansion_frozen",
    "existing_reference_runtime_role", "plan_en", "plan_ru", "deliverables",
    "completion_requires_operator_review", "completed_deliverables", "next_content_slice",
}
EXPECTED_POST_BLUEPRINT_FIELDS = {
    "decision", "issue", "operator_approval", "selected_option", "status",
    "independent_review_protocol", "independent_review_document_en",
    "independent_review_document_ru", "independent_review_status", "bpv1_status",
    "bpv1_role", "product_runtime_thaw", "automatic_canon_promotion",
    "automatic_runtime_promotion",
}
EXPECTED_COMPLETED_DELIVERABLES = EXPECTED_DELIVERABLES[:]
EXPECTED_NEXT_CONTENT_SLICE = "INDEPENDENT_ARCHITECTURE_REVIEW"
INTEGRATED_REVIEW_DOCS = (
    "docs/INTEGRATED_A1_A10_REVIEW.md",
    "docs/INTEGRATED_A1_A10_REVIEW.ru.md",
)
INDEPENDENT_REVIEW_DOCS = (
    "docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md",
    "docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md",
)
COMPLETED_DELIVERABLE_DOCS = {
    item: (f"docs/{item}.md", f"docs/{item}.ru.md")
    for item in EXPECTED_COMPLETED_DELIVERABLES
}


class ArchitectureFreezeError(RuntimeError):
    pass


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
    _require(state.get("protocol") == "nk-project-state/2", "unsupported project-state protocol")
    status = state.get("status")
    _require(isinstance(status, Mapping), "status object required")
    _require(status.get("production_authorized") is False, "architecture validation cannot coexist with production authorization")

    tracks = state.get("tracks")
    _require(isinstance(tracks, Mapping), "tracks object required")
    clean = tracks.get("clean_implementation")
    _require(isinstance(clean, Mapping), "clean implementation track required")
    _require(clean.get("architecture_role") == "BOUNDED_REFERENCE_LABORATORY", "clean implementation must remain a bounded reference laboratory")
    _require(clean.get("semantic_runtime_expansion_authorized") is False, "semantic/runtime expansion is not authorized")
    _require(clean.get("maintenance_allowed") is True, "bounded maintenance allowance must remain explicit")

    research = tracks.get("long_horizon_research")
    _require(isinstance(research, Mapping), "long-horizon research track required")
    _require(research.get("id") == "R", "research track id must be R")
    _require(research.get("status") == "ACTIVE / POST-BLUEPRINT VALIDATION / NO AUTOMATIC PROMOTION", "post-blueprint validation status drift")
    _require(research.get("runtime_authorized") is False, "research track must not authorize runtime")

    refoundation = research.get("architecture_refoundation")
    _require(isinstance(refoundation, Mapping), "ADR-0025 architecture_refoundation object required")
    _require(set(refoundation) == EXPECTED_REFOUNDATION_FIELDS, "architecture_refoundation field inventory drift")
    _require(
        (refoundation.get("decision"), refoundation.get("issue"), refoundation.get("operator_approval"), refoundation.get("status"))
        == ("ADR-0025", 88, "APPROVED", "BLUEPRINT COMPLETE / PROVISIONAL / VALIDATION ACTIVE"),
        "ADR-0025 identity, issue, approval or phase drift",
    )
    _require(refoundation.get("runtime_expansion_frozen") is True, "runtime expansion freeze must remain enabled")
    _require(refoundation.get("existing_reference_runtime_role") == "BOUNDED_REFERENCE_LABORATORY", "existing runtime role drift")
    _require(refoundation.get("plan_en") == "docs/ARCHITECTURE_REFOUNDATION.md" and refoundation.get("plan_ru") == "docs/ARCHITECTURE_REFOUNDATION.ru.md", "architecture blueprint plan identity drift")
    _require(refoundation.get("deliverables") == EXPECTED_DELIVERABLES, "A1-A10 blueprint deliverable inventory drift")
    _require(refoundation.get("completion_requires_operator_review") is True, "blueprint completion must retain separate operator review history")

    completed = refoundation.get("completed_deliverables")
    _require(completed == EXPECTED_COMPLETED_DELIVERABLES, "completed blueprint deliverable inventory drift")
    _require(EXPECTED_NEXT_CONTENT_SLICE not in completed, "independent review gate must not be treated as an A1-A10 deliverable")
    _require("INTEGRATED_A1_A10_REVIEW" not in completed, "integrated review must not be treated as an A1-A10 deliverable")
    _require("OPERATOR_POST_BLUEPRINT_DECISION" not in completed, "operator gate must not be treated as an A1-A10 deliverable")
    _require(all(item in EXPECTED_DELIVERABLES for item in completed), "completed deliverable is not a declared blueprint deliverable")
    _require(len(completed) == len(set(completed)), "completed deliverable inventory must not contain duplicates")
    _require(refoundation.get("next_content_slice") == EXPECTED_NEXT_CONTENT_SLICE, "next architecture validation gate drift")

    for plan_field in ("plan_en", "plan_ru"):
        _require((repo / str(refoundation[plan_field])).is_file(), f"missing architecture blueprint plan: {refoundation[plan_field]}")
    for deliverable in completed:
        docs = COMPLETED_DELIVERABLE_DOCS.get(deliverable)
        _require(docs is not None, f"missing completed deliverable document mapping: {deliverable}")
        for doc_path in docs:
            _require((repo / doc_path).is_file(), f"missing completed deliverable document: {doc_path}")
    for review_doc in INTEGRATED_REVIEW_DOCS:
        _require((repo / review_doc).is_file(), f"missing integrated review document: {review_doc}")

    validation = research.get("post_blueprint_validation")
    _require(isinstance(validation, Mapping), "ADR-0026 post_blueprint_validation object required")
    _require(set(validation) == EXPECTED_POST_BLUEPRINT_FIELDS, "post_blueprint_validation field inventory drift")
    _require(
        (validation.get("decision"), validation.get("issue"), validation.get("operator_approval"))
        == ("ADR-0026", 88, "APPROVED"),
        "ADR-0026 identity, issue or approval drift",
    )
    _require(
        validation.get("selected_option") == "D_INDEPENDENT_CHALLENGE_THEN_BOUNDED_CROSS_LINEAGE_FALSIFICATION",
        "post-blueprint Option D selection drift",
    )
    _require(validation.get("status") == "AUTHORIZED / INDEPENDENT_REVIEW_FIRST", "post-blueprint validation phase drift")
    _require(validation.get("independent_review_protocol") == "nk-independent-architecture-review/1", "independent review protocol identity drift")
    _require(validation.get("independent_review_document_en") == INDEPENDENT_REVIEW_DOCS[0], "independent review English document drift")
    _require(validation.get("independent_review_document_ru") == INDEPENDENT_REVIEW_DOCS[1], "independent review Russian document drift")
    _require(validation.get("independent_review_status") == "NOT_ESTABLISHED", "independent review must not be self-certified")
    _require(validation.get("bpv1_status") == "BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION", "BPV-1 must remain blocked before qualifying review and reconciliation")
    _require(validation.get("bpv1_role") == "FALSIFICATION_INSTRUMENT_ONLY", "BPV-1 role drift")
    _require(validation.get("product_runtime_thaw") is False, "Option D must not thaw product runtime")
    _require(validation.get("automatic_canon_promotion") is False, "automatic Canon promotion forbidden")
    _require(validation.get("automatic_runtime_promotion") is False, "automatic runtime promotion forbidden")
    for review_doc in INDEPENDENT_REVIEW_DOCS:
        _require((repo / review_doc).is_file(), f"missing independent review protocol document: {review_doc}")
    _require((repo / "docs/adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md").is_file(), "missing ADR-0026")

    _require(research.get("runtime_freeze_exceptions") == EXPECTED_FREEZE_EXCEPTIONS, "runtime freeze exception inventory drift")
    _require(research.get("canonical_promotion_requires") == EXPECTED_PROMOTION_REQUIREMENTS, "canonical promotion requirement inventory drift")

    issues = state.get("issues")
    _require(isinstance(issues, Mapping), "issue snapshots required")
    issue = issues.get("88")
    _require(isinstance(issue, Mapping), "Issue #88 snapshot required")
    _require(issue.get("state") == "OPEN", "Issue #88 must remain open through validation")
    meaning = str(issue.get("meaning", ""))
    _require("operator selected ADR-0026 Option D" in meaning, "Issue #88 must record Option D selection")
    _require("INDEPENDENT_ARCHITECTURE_REVIEW" in meaning, "Issue #88 must record independent review as next gate")
    _require("runtime remains frozen" in meaning, "Issue #88 must preserve runtime freeze")
    verification = issue.get("verification")
    _require(isinstance(verification, Mapping), "Issue #88 verification required")
    _require(verification.get("status") == "VERIFIED" and verification.get("method") == "GITHUB_API" and verification.get("source") == "issue/88", "Issue #88 verification drift")

    non_claims = " ".join(str(item).lower() for item in state.get("non_claims", []))
    for phrase in (
        "architecture re-foundation documentation is not runtime implementation evidence",
        "future-facing blueprint does not prove compatibility with arbitrary future substrates",
        "integrated a1-a10 review completion is not independent validation",
        "adr-0026 operator approval authorizes a validation phase",
        "runtime thaw",
    ):
        _require(phrase in non_claims, f"missing architecture boundary: {phrase}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", nargs="?", type=Path, default=Path("project-state.json"))
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    state_path = args.state if args.state.is_absolute() else repo / args.state
    try:
        validate(_load(state_path), repo=repo)
    except ArchitectureFreezeError as exc:
        print(f"Architecture validation boundary failed: {exc}", file=sys.stderr)
        return 1
    print("Architecture validation boundary passed; next=INDEPENDENT_ARCHITECTURE_REVIEW; independent_review=NOT_ESTABLISHED; BPV-1=BLOCKED; runtime_expansion_frozen=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())