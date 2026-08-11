#!/usr/bin/env python3
"""Fail closed when the post-blueprint validation/runtime-freeze boundary drifts.

Historical IAR-1/IAR-1-R1 records retain their publication-time next gate
(BPV1_PLAN_AND_PREREGISTRATION). The frozen preregistration record retains its
own historical next gate (BPV1_EXECUTION_ADMISSION), the gate that was
required after plan merge. Current project state advances only after the
merged, corrected-digest execution-admission package to
BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION, admitting only the BPV1-001 subject
implementation/execution while product runtime remains frozen.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator, Mapping

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
EXPECTED_COMPLETED_DELIVERABLES = EXPECTED_DELIVERABLES[:]
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
    "bpv1_role", "bpv1_plan", "bpv1_execution_admission", "product_runtime_thaw",
    "automatic_canon_promotion", "automatic_runtime_promotion",
}
EXPECTED_HISTORICAL_RECONCILIATION_NEXT_GATE = "BPV1_PLAN_AND_PREREGISTRATION"
# Historical: the gate the frozen preregistration record required after plan
# merge. This never changes once the plan is preregistered/frozen.
EXPECTED_PLAN_NEXT_GATE = "BPV1_EXECUTION_ADMISSION"
EXPECTED_PLAN_POST_MERGE_STATUS = "BLOCKED_PENDING_EXECUTION_ADMISSION"
# Current: the live forward-looking gate/status after execution admission.
EXPECTED_CURRENT_NEXT_CONTENT_SLICE = "BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION"
EXPECTED_CURRENT_BPV1_STATUS = "ADMITTED_FOR_EXPERIMENT_ONLY"
EXPECTED_PLAN_ID = "BPV1-001-cross-lineage-bounded-accountability-v1"
EXPECTED_PLAN_PROTOCOL = "nk-bpv1-preregistration/1"
EXPECTED_PLAN_PATH = "docs/research/BPV1_PREREGISTRATION.json"
EXPECTED_PLAN_MERGE_SHA = "a538d7f1e28858a88b9ee777ac7d6e05b85943db"
EXPECTED_PLAN_SHA256 = "7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0"
EXPECTED_ADMISSION_PROTOCOL = "nk-bpv1-execution-admission-status/1"
EXPECTED_ADMISSION_ID = "BPV1-001-execution-admission-v1"
EXPECTED_ADMISSION_PACKAGE_MERGE_SHA = "6027eec73f11c4626be5553de7e79f827be2c81d"
EXPECTED_SUBJECT_AUTHORIZATION = "AUTHORIZED_FOR_BPV1-001_ONLY"

INTEGRATED_REVIEW_DOCS = (
    "docs/INTEGRATED_A1_A10_REVIEW.md",
    "docs/INTEGRATED_A1_A10_REVIEW.ru.md",
)
INDEPENDENT_REVIEW_DOCS = (
    "docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md",
    "docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md",
)
IAR1_RESULT_JSON = "docs/reviews/IAR-1_RESULT.json"
IAR1_RESULT_MD = "docs/reviews/IAR-1_RESULT.md"
IAR1_RESULT_RU_MD = "docs/reviews/IAR-1_RESULT.ru.md"
IAR1_RECONCILIATION_JSON = "docs/reviews/IAR-1_RECONCILIATION.json"
IAR1_RECONCILIATION_MD = "docs/reviews/IAR-1_RECONCILIATION.md"
IAR1_RECONCILIATION_RU_MD = "docs/reviews/IAR-1_RECONCILIATION.ru.md"

EXPECTED_IAR1_BLOCKERS = [
    "IAR-F01", "IAR-F02", "IAR-F03", "IAR-F05", "IAR-F07", "IAR-F08", "IAR-F09",
]
EXPECTED_IAR1_MATERIAL = ["IAR-F04", "IAR-F06", "IAR-F10"]
EXPECTED_IAR1_SEVERITY = {
    **{finding_id: "BLOCKING" for finding_id in EXPECTED_IAR1_BLOCKERS},
    **{finding_id: "MATERIAL" for finding_id in EXPECTED_IAR1_MATERIAL},
}
EXPECTED_SOURCE_BPV1_DEPENDENCY = {
    **{finding_id: "BLOCKS" for finding_id in EXPECTED_IAR1_BLOCKERS},
    **{finding_id: "SHOULD_INFORM" for finding_id in EXPECTED_IAR1_MATERIAL},
}
EXPECTED_RECONCILED_BPV1_DEPENDENCY = {
    **{finding_id: "RESOLVED_BEFORE_PLAN" for finding_id in EXPECTED_IAR1_BLOCKERS},
    "IAR-F04": "INFORMS_PLAN",
    "IAR-F06": "INFORMS_PLAN",
    "IAR-F10": "INFORMS_FUTURE_COMPOSITION_SCOPE",
}
EXPECTED_IAR1_INPUT_PACKET = [
    "AGENTS.md and mandatory orientation surfaces",
    "A1-A10 provisional architecture documents",
    "integrated A1-A10 reconciliation",
    "ADR-0025",
    "ADR-0026",
    "nk-independent-architecture-review/1",
    "P1-C5 contract/evidence/runtime context sufficient to test implementation capture",
]
EXPECTED_PREREGISTRATION_FIELDS = [
    "scenario_id",
    "purpose_scope",
    "mandatory_obligations",
    "applicability_rules",
    "mandatory_observables",
    "equivalence_predicates",
    "allowed_declared_losses",
    "failure_thresholds",
    "hard_refutation_observations",
    "grounding_mode",
    "threat_model",
    "oracle_authority",
]
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


def _load_json_record(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ArchitectureFreezeError(f"cannot read {label}: {exc}") from exc
    _require(isinstance(value, dict), f"{label} must contain an object")
    return value


def _parse_timestamp(value: Any, label: str) -> datetime:
    _require(isinstance(value, str) and value.strip(), f"{label} timestamp required")
    normalized = value.strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ArchitectureFreezeError(f"invalid {label} timestamp: {value}") from exc
    _require(parsed.tzinfo is not None, f"{label} timestamp must include timezone")
    return parsed.astimezone(timezone.utc)


def _verification_observations(value: Any, path: str = "$") -> Iterator[tuple[str, Any]]:
    if isinstance(value, Mapping):
        verification = value.get("verification")
        if isinstance(verification, Mapping) and "observed_at" in verification:
            yield f"{path}.verification.observed_at", verification.get("observed_at")
        for key, child in value.items():
            if key != "verification":
                yield from _verification_observations(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _verification_observations(child, f"{path}[{index}]")


def _validate_snapshot_chronology(state: Mapping[str, Any]) -> None:
    snapshot_time = _parse_timestamp(state.get("observed_at"), "project-state observed_at")
    for path, raw_observed_at in _verification_observations(state):
        observation_time = _parse_timestamp(raw_observed_at, path)
        _require(
            snapshot_time >= observation_time,
            f"project-state observed_at predates constituent verification: {path}",
        )


def _validate_source_finding(finding_id: str, item: Mapping[str, Any]) -> None:
    _require(item.get("severity") == EXPECTED_IAR1_SEVERITY[finding_id], f"{finding_id} severity drift")
    _require(item.get("status") == "OPEN", f"{finding_id} source review status must remain OPEN")
    _require(item.get("bpv1_dependency") == EXPECTED_SOURCE_BPV1_DEPENDENCY[finding_id], f"{finding_id} source BPV-1 dependency drift")
    for field in (
        "affected_slices", "claim_or_obligation", "finding", "counterexample_or_reasoning",
        "implementation_capture_risk", "falsifiability_impact", "recommended_disposition",
        "source_review_comment_id",
    ):
        _require(item.get(field) not in (None, "", []), f"{finding_id} source finding field required: {field}")
    _require(item.get("implementation_capture_risk") in {"LOW", "MEDIUM", "HIGH"}, f"{finding_id} implementation-capture risk drift")
    _require(item.get("falsifiability_impact") in {"LOW", "MEDIUM", "HIGH"}, f"{finding_id} falsifiability impact drift")
    _require(item.get("recommended_disposition") in {"REMOVE", "WEAKEN", "SPLIT", "CLARIFY", "TEST", "RETAIN"}, f"{finding_id} disposition drift")


def _validate_iar1_records(repo: Path) -> None:
    for path in (
        IAR1_RESULT_MD, IAR1_RESULT_RU_MD, IAR1_RESULT_JSON,
        IAR1_RECONCILIATION_MD, IAR1_RECONCILIATION_RU_MD, IAR1_RECONCILIATION_JSON,
    ):
        _require((repo / path).is_file(), f"missing IAR-1 review/reconciliation record: {path}")

    result = _load_json_record(repo / IAR1_RESULT_JSON, "IAR-1 result")
    _require(result.get("protocol") == "nk-independent-architecture-review-result/1", "IAR-1 result protocol drift")
    _require(result.get("review_id") == "IAR-1", "IAR-1 identity drift")
    _require(result.get("process_outcome") == "QUALIFYING_REVIEW_COMPLETE", "IAR-1 must be a qualifying completed review")
    _require(result.get("reviewed_commit") == "2dd51723e30d5f3c5e86268365bf4cf7639b5e9a", "IAR-1 reviewed commit drift")
    _require(result.get("q1_q12_complete") is True, "IAR-1 Q1-Q12 coverage must be complete")
    _require(result.get("finding_count") == 10, "IAR-1 finding count drift")
    _require(result.get("blocking_findings") == EXPECTED_IAR1_BLOCKERS, "IAR-1 blocking finding inventory drift")
    _require(result.get("material_findings") == EXPECTED_IAR1_MATERIAL, "IAR-1 material finding inventory drift")
    _require(result.get("bpv1_status_recommendation") == "BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION", "IAR-1 must not itself admit BPV-1")
    _require(result.get("product_runtime_status") == "FROZEN", "IAR-1 must preserve runtime freeze")
    _require(result.get("input_packet_read") == EXPECTED_IAR1_INPUT_PACKET, "IAR-1 input packet evidence drift")
    reviewer = result.get("reviewer")
    _require(isinstance(reviewer, Mapping), "IAR-1 reviewer record required")
    _require(reviewer.get("reviewer_identity") == "github-codex-review-agent", "IAR-1 reviewer identity drift")
    _require(reviewer.get("reviewer_kind") == "AGENT", "IAR-1 reviewer kind drift")
    basis = reviewer.get("independence_basis")
    _require(isinstance(basis, str) and len(basis.strip()) >= 80, "IAR-1 substantive independence basis required")
    for marker in ("Separate GitHub review agent", "contributor/collaborator", "did not author"):
        _require(marker in basis, f"IAR-1 independence basis missing evidence marker: {marker}")
    _require(reviewer.get("prior_authorship_of_A1_A10") is False, "IAR-1 reviewer cannot be A1-A10 author")
    _require(reviewer.get("prior_authorship_of_integrated_review") is False, "IAR-1 reviewer cannot be integrated-review author")
    _require(reviewer.get("review_scope") == "A1-A10 + integrated reconciliation", "IAR-1 reviewer scope drift")
    _require(reviewer.get("review_mode") == "ADVERSARIAL_FALSIFICATION", "IAR-1 review mode drift")
    _require(reviewer.get("current_runtime_used_as_architectural_oracle") is False, "IAR-1 must not use current runtime as architecture oracle")
    findings = result.get("findings")
    _require(isinstance(findings, list) and len(findings) == 10, "IAR-1 findings register must contain ten entries")
    by_id = {item.get("finding_id"): item for item in findings if isinstance(item, Mapping)}
    _require(set(by_id) == set(EXPECTED_IAR1_SEVERITY), "IAR-1 finding ids drift")
    for finding_id, item in by_id.items():
        _validate_source_finding(finding_id, item)

    reconciliation = _load_json_record(repo / IAR1_RECONCILIATION_JSON, "IAR-1 reconciliation")
    _require(reconciliation.get("protocol") == "nk-independent-architecture-review-reconciliation/1", "IAR-1 reconciliation protocol drift")
    _require(reconciliation.get("reconciliation_id") == "IAR-1-R1", "IAR-1 reconciliation identity drift")
    _require(reconciliation.get("review_id") == "IAR-1", "IAR-1 reconciliation review binding drift")
    _require(reconciliation.get("status") == "COMPLETE", "IAR-1 reconciliation must be complete")
    _require(reconciliation.get("architecture_status") == "PROVISIONAL_RECONCILED", "IAR-1 architecture status drift")
    _require(reconciliation.get("runtime_expansion") == "FROZEN", "IAR-1 reconciliation must preserve runtime freeze")
    _require(reconciliation.get("bpv1_status_after_reconciliation") == "BLOCKED_PENDING_PREREGISTERED_PLAN", "IAR-1 reconciliation must preserve its historical post-review BPV-1 status")
    _require(reconciliation.get("next_gate") == EXPECTED_HISTORICAL_RECONCILIATION_NEXT_GATE, "IAR-1 reconciliation next gate drift")
    _require(reconciliation.get("open_blocking_findings") == [], "IAR-1 reconciliation cannot leave blocking findings open")
    _require(reconciliation.get("open_material_findings") == [], "IAR-1 reconciliation cannot leave material findings untracked")
    _require(reconciliation.get("automatic_canon_promotion") is False, "IAR-1 reconciliation cannot auto-promote Canon")
    _require(reconciliation.get("automatic_runtime_promotion") is False, "IAR-1 reconciliation cannot auto-promote runtime")
    reconciled = reconciliation.get("findings")
    _require(isinstance(reconciled, list) and len(reconciled) == 10, "IAR-1 reconciliation must cover all findings")
    reconciled_by_id = {item.get("finding_id"): item for item in reconciled if isinstance(item, Mapping)}
    _require(set(reconciled_by_id) == set(by_id), "IAR-1 reconciliation finding inventory drift")
    for finding_id, item in reconciled_by_id.items():
        _require(item.get("severity") == EXPECTED_IAR1_SEVERITY[finding_id], f"{finding_id} reconciliation severity drift")
        _require(item.get("status") == "RESOLVED", f"{finding_id} must be reconciled before BPV-1 planning")
        _require(bool(str(item.get("reconciliation_record", "")).strip()), f"{finding_id} reconciliation record required")
        _require(item.get("bpv1_dependency") == EXPECTED_RECONCILED_BPV1_DEPENDENCY[finding_id], f"{finding_id} reconciliation BPV-1 dependency drift")
    prereg = reconciliation.get("conformance_preregistration")
    _require(isinstance(prereg, Mapping), "IAR-1 preregistration boundary required")
    _require(prereg.get("required_before_execution") is True, "BPV-1 preregistration must precede execution")
    fields = prereg.get("fields")
    _require(fields == EXPECTED_PREREGISTRATION_FIELDS, "BPV-1 preregistration field inventory drift")
    _require(len(fields) == len(set(fields)), "BPV-1 preregistration field inventory contains duplicates")
    _require(prereg.get("post_hoc_rescoping") == "INVALIDATES_RUN_FOR_CLAIMED_SCOPE", "post-hoc BPV-1 rescoping must fail closed")
    _require(prereg.get("not_applicable_requires_preregistered_rationale") is True, "NOT_APPLICABLE must require preregistered rationale")
    principles = reconciliation.get("principles")
    _require(isinstance(principles, Mapping), "IAR-1 refined principle boundary required")
    _require(principles.get("exact_reconstruction_universal") is False, "exact reconstruction cannot remain universal")
    _require(principles.get("event_sourcing_universal") is False, "Event sourcing cannot become universal")
    _require(principles.get("global_total_order_universal") is False, "global total order cannot become universal")
    _require(principles.get("composition_conformance_implied_by_local_conformance") is False, "local conformance cannot imply composition conformance")


def _validate_current_bpv1_plan(validation: Mapping[str, Any], repo: Path) -> None:
    plan = validation.get("bpv1_plan")
    _require(isinstance(plan, Mapping), "authoritative BPV-1 plan binding required")
    _require(plan.get("protocol") == EXPECTED_PLAN_PROTOCOL, "BPV-1 plan protocol drift")
    _require(plan.get("plan_id") == EXPECTED_PLAN_ID, "BPV-1 plan identity drift")
    _require(plan.get("path") == EXPECTED_PLAN_PATH, "BPV-1 plan path drift")
    _require(plan.get("authoritative_plan_merge_sha") == EXPECTED_PLAN_MERGE_SHA, "BPV-1 authoritative plan merge drift")
    _require(plan.get("status") == "PREREGISTERED / EXECUTION_NOT_AUTHORIZED", "BPV-1 plan status drift")
    _require(plan.get("execution_authorized") is False, "BPV-1 execution must remain blocked at the plan level")
    _require(plan.get("execution_admission_required") is True, "BPV-1 execution admission must remain required")
    _require(plan.get("next_gate") == EXPECTED_PLAN_NEXT_GATE, "BPV-1 plan historical next gate drift")
    record = _load_json_record(repo / EXPECTED_PLAN_PATH, "BPV-1 preregistration")
    _require(record.get("protocol") == EXPECTED_PLAN_PROTOCOL, "BPV-1 preregistration protocol drift")
    _require(record.get("plan_id") == EXPECTED_PLAN_ID, "BPV-1 preregistration identity drift")
    _require(record.get("status") == "PREREGISTERED / EXECUTION_NOT_AUTHORIZED", "BPV-1 preregistration status drift")
    _require(record.get("execution_authorized") is False, "merged BPV-1 preregistration cannot itself authorize execution")
    _require(record.get("next_gate_after_plan_merge") == EXPECTED_PLAN_NEXT_GATE, "merged BPV-1 preregistration historical next gate drift")
    boundary = record.get("execution_boundary")
    _require(isinstance(boundary, Mapping), "BPV-1 execution boundary required")
    _require(boundary.get("plan_merge_authorizes_execution") is False, "plan merge alone cannot authorize BPV-1 execution")
    _require(boundary.get("execution_status_after_plan_merge") == EXPECTED_PLAN_POST_MERGE_STATUS, "BPV-1 post-plan-merge (pre-admission) execution status drift")


def _validate_bpv1_execution_admission(validation: Mapping[str, Any]) -> None:
    admission = validation.get("bpv1_execution_admission")
    _require(isinstance(admission, Mapping), "BPV-1 execution-admission status record required")
    _require(admission.get("protocol") == EXPECTED_ADMISSION_PROTOCOL, "BPV-1 execution-admission protocol drift")
    _require(admission.get("admission_id") == EXPECTED_ADMISSION_ID, "BPV-1 execution-admission identity drift")
    _require(admission.get("status") == "COMPLETE", "BPV-1 execution-admission status drift")
    _require(admission.get("admission_package_pr") == 112, "BPV-1 execution-admission package PR drift")
    _require(admission.get("admission_package_merge_sha") == EXPECTED_ADMISSION_PACKAGE_MERGE_SHA, "BPV-1 execution-admission package merge drift")
    _require(admission.get("plan_merge_sha") == EXPECTED_PLAN_MERGE_SHA, "BPV-1 execution-admission plan-merge binding drift")
    _require(admission.get("plan_sha256") == EXPECTED_PLAN_SHA256, "BPV-1 execution-admission frozen plan digest drift")
    _require(admission.get("subject_implementation_authorization") == EXPECTED_SUBJECT_AUTHORIZATION, "BPV-1 subject implementation authorization drift")
    _require(admission.get("subject_execution_authorization") == EXPECTED_SUBJECT_AUTHORIZATION, "BPV-1 subject execution authorization drift")
    _require(admission.get("product_runtime_integration_authorized") is False, "BPV-1 execution admission cannot authorize product runtime integration")
    _require(admission.get("runtime_expansion") == "FROZEN", "BPV-1 execution admission must preserve runtime freeze")


def validate(state: Mapping[str, Any], *, repo: Path) -> None:
    _require(state.get("protocol") == "nk-project-state/2", "unsupported project-state protocol")
    _validate_snapshot_chronology(state)
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
    _require((refoundation.get("decision"), refoundation.get("issue"), refoundation.get("operator_approval"), refoundation.get("status")) == ("ADR-0025", 88, "APPROVED", "BLUEPRINT COMPLETE / PROVISIONAL / VALIDATION ACTIVE"), "ADR-0025 identity, issue, approval or phase drift")
    _require(refoundation.get("runtime_expansion_frozen") is True, "runtime expansion freeze must remain enabled")
    _require(refoundation.get("existing_reference_runtime_role") == "BOUNDED_REFERENCE_LABORATORY", "existing runtime role drift")
    _require(refoundation.get("plan_en") == "docs/ARCHITECTURE_REFOUNDATION.md" and refoundation.get("plan_ru") == "docs/ARCHITECTURE_REFOUNDATION.ru.md", "architecture blueprint plan identity drift")
    _require(refoundation.get("deliverables") == EXPECTED_DELIVERABLES, "A1-A10 blueprint deliverable inventory drift")
    _require(refoundation.get("completion_requires_operator_review") is True, "blueprint completion must retain separate operator review history")
    completed = refoundation.get("completed_deliverables")
    _require(completed == EXPECTED_COMPLETED_DELIVERABLES, "completed blueprint deliverable inventory drift")
    _require("INDEPENDENT_ARCHITECTURE_REVIEW" not in completed, "independent review gate must not be treated as an A1-A10 deliverable")
    _require("INTEGRATED_A1_A10_REVIEW" not in completed, "integrated review must not be treated as an A1-A10 deliverable")
    _require("OPERATOR_POST_BLUEPRINT_DECISION" not in completed, "operator gate must not be treated as an A1-A10 deliverable")
    _require(all(item in EXPECTED_DELIVERABLES for item in completed), "completed deliverable is not a declared blueprint deliverable")
    _require(len(completed) == len(set(completed)), "completed deliverable inventory must not contain duplicates")
    _require(refoundation.get("next_content_slice") == EXPECTED_CURRENT_NEXT_CONTENT_SLICE, "next architecture validation gate drift")
    for plan_field in ("plan_en", "plan_ru"):
        _require((repo / str(refoundation[plan_field])).is_file(), f"missing architecture blueprint plan: {refoundation[plan_field]}")
    for deliverable in completed:
        for doc_path in COMPLETED_DELIVERABLE_DOCS[deliverable]:
            _require((repo / doc_path).is_file(), f"missing completed deliverable document: {doc_path}")
    for review_doc in INTEGRATED_REVIEW_DOCS:
        _require((repo / review_doc).is_file(), f"missing integrated review document: {review_doc}")

    validation = research.get("post_blueprint_validation")
    _require(isinstance(validation, Mapping), "ADR-0026 post_blueprint_validation object required")
    _require(set(validation) == EXPECTED_POST_BLUEPRINT_FIELDS, "post_blueprint_validation field inventory drift")
    _require((validation.get("decision"), validation.get("issue"), validation.get("operator_approval")) == ("ADR-0026", 88, "APPROVED"), "ADR-0026 identity, issue or approval drift")
    _require(validation.get("selected_option") == "D_INDEPENDENT_CHALLENGE_THEN_BOUNDED_CROSS_LINEAGE_FALSIFICATION", "post-blueprint Option D selection drift")
    _require(validation.get("status") == "AUTHORIZED / REVIEW_COMPLETE / RECONCILIATION_COMPLETE / BPV1_PLAN_PREREGISTERED / EXECUTION_ADMITTED_FOR_EXPERIMENT_ONLY", "post-blueprint validation phase drift")
    _require(validation.get("independent_review_protocol") == "nk-independent-architecture-review/1", "independent review protocol identity drift")
    _require(validation.get("independent_review_document_en") == INDEPENDENT_REVIEW_DOCS[0], "independent review English document drift")
    _require(validation.get("independent_review_document_ru") == INDEPENDENT_REVIEW_DOCS[1], "independent review Russian document drift")
    _require(validation.get("independent_review_status") == "QUALIFYING_REVIEW_COMPLETE", "independent review completion drift")
    _require(validation.get("bpv1_status") == EXPECTED_CURRENT_BPV1_STATUS, "BPV-1 execution must remain admitted for the bounded experiment only")
    _require(validation.get("bpv1_role") == "FALSIFICATION_INSTRUMENT_ONLY", "BPV-1 role drift")
    _require(validation.get("product_runtime_thaw") is False, "Option D must not thaw product runtime")
    _require(validation.get("automatic_canon_promotion") is False, "automatic Canon promotion forbidden")
    _require(validation.get("automatic_runtime_promotion") is False, "automatic runtime promotion forbidden")
    for review_doc in INDEPENDENT_REVIEW_DOCS:
        _require((repo / review_doc).is_file(), f"missing independent review protocol document: {review_doc}")
    _validate_iar1_records(repo)
    _validate_current_bpv1_plan(validation, repo)
    _validate_bpv1_execution_admission(validation)
    _require((repo / "docs/adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md").is_file(), "missing ADR-0026")

    _require(research.get("runtime_freeze_exceptions") == EXPECTED_FREEZE_EXCEPTIONS, "runtime freeze exception inventory drift")
    _require(research.get("canonical_promotion_requires") == EXPECTED_PROMOTION_REQUIREMENTS, "canonical promotion requirement inventory drift")

    issues = state.get("issues")
    _require(isinstance(issues, Mapping), "issue snapshots required")
    issue = issues.get("88")
    _require(isinstance(issue, Mapping), "Issue #88 snapshot required")
    _require(issue.get("state") == "OPEN", "Issue #88 must remain open through validation")
    meaning = str(issue.get("meaning", ""))
    _require("ADR-0026 Option D" in meaning, "Issue #88 must record Option D selection")
    _require("IAR-1 is QUALIFYING_REVIEW_COMPLETE" in meaning, "Issue #88 must record IAR-1 review completion")
    _require("IAR-1-R1 reconciliation" in meaning, "Issue #88 must record IAR-1 reconciliation")
    _require(EXPECTED_PLAN_ID in meaning and EXPECTED_PLAN_MERGE_SHA in meaning, "Issue #88 must record authoritative BPV-1 plan binding")
    _require(EXPECTED_ADMISSION_PACKAGE_MERGE_SHA in meaning, "Issue #88 must record the execution-admission package merge")
    _require(EXPECTED_CURRENT_BPV1_STATUS in meaning, "Issue #88 must record the bounded BPV-1 execution-admission status")
    _require("runtime remain" in meaning.lower() and "frozen" in meaning.lower(), "Issue #88 must preserve runtime freeze")
    verification = issue.get("verification")
    _require(isinstance(verification, Mapping), "Issue #88 verification required")
    _require(verification.get("status") == "VERIFIED" and verification.get("method") == "GITHUB_API" and verification.get("source") == "issue/88", "Issue #88 verification drift")

    non_claims = " ".join(str(item).lower() for item in state.get("non_claims", []))
    for phrase in (
        "architecture re-foundation documentation is not runtime implementation evidence",
        "future-facing blueprint does not prove compatibility with arbitrary future substrates",
        "integrated a1-a10 review completion is not independent validation",
        "adr-0026 operator approval authorizes a validation phase",
        "iar-1 qualifying review completion and iar-1-r1 reconciliation do not prove the architecture correct",
        "bpv-1 preregistration and an authoritative plan merge do not authorize experiment execution",
        "bpv-1 execution admission authorizes only the bpv1-001 subject implementation and execution",
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
    print("Architecture validation boundary passed; chronology=valid; IAR-1=QUALIFYING_REVIEW_COMPLETE; reconciliation=COMPLETE; BPV1_plan=PREREGISTERED; BPV1_execution_admission=COMPLETE; BPV-1_execution=ADMITTED_FOR_EXPERIMENT_ONLY; next=BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION; runtime_expansion_frozen=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
