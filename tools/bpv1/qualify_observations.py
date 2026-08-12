#!/usr/bin/env python3
"""Externally qualify BPV1-001 raw subject facts into the frozen observation shape.

This layer is deliberately outside the Rust implementation under test. It does
not read the frozen fixture expectations and does not choose an A10 outcome.
It derives semantic/structural observables from raw state facts plus repository
source inspection, then leaves `tools/bpv1/evaluate.py` unchanged as the frozen
oracle evaluator.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Mapping

RAW_PROTOCOL = "nk-bpv1-raw-observations/1"
OBSERVATION_PROTOCOL = "nk-bpv1-observations/1"
QUALIFICATION_PROTOCOL = "nk-bpv1-external-qualification/1"


class QualificationError(ValueError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise QualificationError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise QualificationError(f"JSON root must be an object: {path}")
    return value


def _mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise QualificationError(f"{label} must be an object")
    return value


def _list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise QualificationError(f"{label} must be a list")
    return value


def _strip_rust_comments_and_strings(text: str) -> str:
    """Remove Rust comments/string/char contents before identifier inspection."""
    out: list[str] = []
    i = 0
    block_depth = 0
    state = "normal"
    while i < len(text):
        ch = text[i]
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if state == "normal":
            if ch == "/" and nxt == "/":
                state = "line_comment"
                out.extend("  ")
                i += 2
                continue
            if ch == "/" and nxt == "*":
                state = "block_comment"
                block_depth = 1
                out.extend("  ")
                i += 2
                continue
            if ch == '"':
                state = "string"
                out.append(" ")
                i += 1
                continue
            if ch == "'" and nxt and (nxt.isalnum() or nxt == "_"):
                # Rust lifetimes such as 'a are identifiers, not char strings.
                out.append(ch)
                i += 1
                continue
            if ch == "'":
                state = "char"
                out.append(" ")
                i += 1
                continue
            out.append(ch)
            i += 1
            continue
        if state == "line_comment":
            if ch == "\n":
                state = "normal"
                out.append("\n")
            else:
                out.append(" ")
            i += 1
            continue
        if state == "block_comment":
            if ch == "/" and nxt == "*":
                block_depth += 1
                out.extend("  ")
                i += 2
                continue
            if ch == "*" and nxt == "/":
                block_depth -= 1
                out.extend("  ")
                i += 2
                if block_depth == 0:
                    state = "normal"
                continue
            out.append("\n" if ch == "\n" else " ")
            i += 1
            continue
        if state in {"string", "char"}:
            if ch == "\\":
                out.extend("  ")
                i += 2
                continue
            terminator = '"' if state == "string" else "'"
            if ch == terminator:
                state = "normal"
            out.append("\n" if ch == "\n" else " ")
            i += 1
            continue
    return "".join(out)


def _engine_field_names(cleaned_engine: str) -> set[str]:
    match = re.search(r"pub\s+struct\s+Engine\s*\{(?P<body>.*?)\n\}", cleaned_engine, re.S)
    if not match:
        return set()
    return set(re.findall(r"pub\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", match.group("body")))


def derive_structural_facts(repo: Path) -> tuple[dict[str, bool], dict[str, Any]]:
    subject = repo / "experiments" / "bpv1" / "BPV1-001" / "subject"
    cargo = (subject / "Cargo.toml").read_text(encoding="utf-8").lower()
    source_paths = sorted((subject / "src").glob("*.rs"))
    if not source_paths:
        raise QualificationError("subject source files are absent")
    source = "\n".join(path.read_text(encoding="utf-8") for path in source_paths)
    cleaned = _strip_rust_comments_and_strings(source)
    tokens = set(re.findall(r"[A-Za-z_][A-Za-z0-9_]*", cleaned.lower()))
    fields = _engine_field_names(_strip_rust_comments_and_strings((subject / "src" / "engine.rs").read_text(encoding="utf-8")))

    dependency_markers = {"native_kernel", "postgres", "sqlx", "rusqlite", "diesel", "tokio_postgres", "sqlite"}
    imports_current_native_kernel = "native_kernel" in tokens or "native_kernel" in cargo
    reuses_event = bool(tokens & {"event", "events", "event_envelope"})
    reuses_reducer = "reducer" in tokens
    reuses_receipt = bool(tokens & {"receipt", "receipts"})
    uses_sql = bool(tokens & {"postgres", "sqlx", "rusqlite", "diesel", "tokio_postgres", "sqlite"}) or any(
        marker in cargo for marker in dependency_markers - {"native_kernel"}
    )

    engine_text = (subject / "src" / "engine.rs").read_text(encoding="utf-8")
    main_text = (subject / "src" / "main.rs").read_text(encoding="utf-8")
    cleaned_engine = _strip_rust_comments_and_strings(engine_text).lower()
    cleaned_main = _strip_rust_comments_and_strings(main_text).lower()

    suspicious_history_fields = {
        field
        for field in fields
        if any(marker in field.lower() for marker in ("event_log", "operation_log", "append_log", "history_log", "mutation_log"))
    }
    crash_journal_bounded = all(
        marker in engine_text
        for marker in (
            "CRASH_JOURNAL_MAX_ENTRIES",
            "self.crash_journal.len() >= CRASH_JOURNAL_MAX_ENTRIES",
            "self.crash_journal.pop_front()",
        )
    )
    witness_store_bounded = all(
        marker in engine_text
        for marker in (
            "LOSS_WITNESS_MAX_RECORDS",
            "fn push_loss_witness",
            "fn roll_up_witness",
            "loss_witness_rollup",
        )
    )
    predecessor_store_bounded = all(
        marker in engine_text
        for marker in (
            "RETAINED_DETAIL_PER_SLOT",
            "while slot.detailed_predecessors.len() > RETAINED_DETAIL_PER_SLOT",
            "while slot.compacted_summaries.len() > RETAINED_DETAIL_PER_SLOT",
        )
    )
    per_operation_log_absence_established = (
        not suspicious_history_fields
        and crash_journal_bounded
        and witness_store_bounded
        and predecessor_store_bounded
        and "event" not in tokens
    )

    replay_identifiers = {token for token in tokens if "replay" in token or "reconstruct" in token}
    direct_current_state_observation = "build_raw_observations" in cleaned_main and "&engine" in cleaned_main
    exact_replay_not_required_established = not replay_identifiers and direct_current_state_observation

    facts: dict[str, bool] = {}
    if per_operation_log_absence_established:
        facts["authoritative_per_operation_append_log"] = False
    if exact_replay_not_required_established:
        facts["exact_replay_required"] = False
    facts["imports_current_native_kernel"] = imports_current_native_kernel
    facts["reuses_current_event_envelope"] = reuses_event
    facts["reuses_current_reducer"] = reuses_reducer
    facts["reuses_current_receipt_shape_as_oracle"] = reuses_receipt
    facts["uses_current_sql_profile"] = uses_sql

    report = {
        "source_files": [str(path.relative_to(repo)) for path in source_paths],
        "engine_fields": sorted(fields),
        "suspicious_history_fields": sorted(suspicious_history_fields),
        "crash_journal_bounded": crash_journal_bounded,
        "witness_store_bounded": witness_store_bounded,
        "predecessor_store_bounded": predecessor_store_bounded,
        "replay_identifiers": sorted(replay_identifiers),
        "direct_current_state_observation": direct_current_state_observation,
        "structural_facts_established": sorted(facts),
    }
    return facts, report


def _identity_parts(identity: str) -> tuple[int, int] | None:
    match = re.fullmatch(r"slot-(\d+):v(\d+)", identity)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def qualify(raw: Mapping[str, Any], repo: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    if raw.get("protocol") != RAW_PROTOCOL:
        raise QualificationError("raw observation protocol mismatch")
    fixtures = _mapping(raw.get("fixtures"), "fixtures")
    workload_raw = _mapping(raw.get("workload"), "workload")
    structural, structural_report = derive_structural_facts(repo)

    def fixture(fixture_id: str) -> Mapping[str, Any]:
        return _mapping(fixtures.get(fixture_id), fixture_id)

    fx01_current = _mapping(fixture("BPV1-FX01-UNKNOWN-NOT-FALSE").get("current"), "FX01.current")
    fx01_position = str(fx01_current.get("epistemic_position", ""))
    fx01 = {
        "epistemic_position": fx01_position,
        "coerced_unknown_to_false": fx01_position == "FALSE",
    }

    fx02_current = _mapping(fixture("BPV1-FX02-ROLE-NONCONFLATION").get("current"), "FX02.current")
    source = str(fx02_current.get("source", ""))
    authority = str(fx02_current.get("authority", ""))
    evidence = [str(value) for value in _list(fx02_current.get("evidence"), "FX02.evidence")]
    roles_distinguishable = bool(source and authority and source != authority and all(value not in {source, authority} for value in evidence))
    fx02 = {
        "roles_distinguishable": roles_distinguishable,
        "authority_scope_explicit": bool(authority),
        "material_role_collapse": not roles_distinguishable,
    }

    fx03_raw = fixture("BPV1-FX03-CONTEXT-BINDING")
    fx03_a = _mapping(fx03_raw.get("a"), "FX03.a")
    fx03_b = _mapping(fx03_raw.get("b"), "FX03.b")
    fx03 = {
        "context_distinction_preserved": (
            fx03_a.get("proposition") == fx03_b.get("proposition")
            and fx03_a.get("context") != fx03_b.get("context")
            and fx03_a.get("epistemic_position") != fx03_b.get("epistemic_position")
        )
    }

    fx04_raw = fixture("BPV1-FX04-REVISION-SUPERSESSION")
    fx04_current = _mapping(fx04_raw.get("current"), "FX04.current")
    predecessor_id = fx04_current.get("predecessor_version_id")
    lineage_ids = set(_list(fx04_raw.get("detailed_predecessor_version_ids"), "FX04.detailed")) | set(
        _list(fx04_raw.get("compacted_summary_version_ids"), "FX04.compacted")
    )
    retained_lineage_visible = predecessor_id is not None and predecessor_id in lineage_ids
    fx04 = {
        "retained_lineage_visible": retained_lineage_visible,
        "silent_overwrite": not retained_lineage_visible,
    }

    fx05_raw = fixture("BPV1-FX05-UNRESOLVED-PLURALITY")
    candidates = [_mapping(value, "FX05.candidate") for value in _list(fx05_raw.get("candidates"), "FX05.candidates")]
    unresolved = len(candidates) >= 2 and all(value.get("epistemic_position") == "UNRESOLVED_PLURALITY" for value in candidates)
    winner_selected = bool(fx05_raw.get("current_present")) or not unresolved
    fx05 = {
        "unresolved_plurality_visible": unresolved,
        "unauthorized_winner_selected": winner_selected,
    }

    fx06_raw = fixture("BPV1-FX06-BOUNDED-COMPACTION")
    retention = int(fx06_raw.get("retained_detail_per_slot", -1))
    detail_counts = [int(value) for value in _list(fx06_raw.get("detail_counts"), "FX06.detail_counts")]
    retained_identities = {str(value) for value in _list(fx06_raw.get("retained_identities"), "FX06.retained_identities")}
    witnesses = [_mapping(value, "FX06.loss_witness") for value in _list(fx06_raw.get("loss_witnesses"), "FX06.loss_witnesses")]
    rollup = _mapping(fx06_raw.get("loss_witness_rollup"), "FX06.loss_witness_rollup")

    detailed_witness_identities: set[str] = set()
    detailed_witness_valid = True
    for witness in witnesses:
        identities = [str(value) for value in _list(witness.get("affected_claim_identities"), "witness.identities")]
        detailed_witness_identities.update(identities)
        detailed_witness_valid = detailed_witness_valid and bool(identities)
        detailed_witness_valid = detailed_witness_valid and int(witness.get("compacted_count", -1)) == len(identities)
        detailed_witness_valid = detailed_witness_valid and bool(witness.get("reason")) and bool(witness.get("basis_authority"))

    rollup_count = int(rollup.get("compacted_count", 0))
    rollup_entries = [_mapping(value, "rollup.entry") for value in _list(rollup.get("entries", []), "rollup.entries")]
    rollup_valid = True
    if rollup_count > 0:
        rollup_valid = bool(rollup.get("first_witness_id")) and bool(rollup.get("last_witness_id"))
        rollup_valid = rollup_valid and bool(rollup.get("reason")) and bool(rollup.get("basis_authority"))
        rollup_valid = rollup_valid and sum(int(entry.get("compacted_count", -1)) for entry in rollup_entries) == rollup_count

    retained_by_slot: dict[int, set[int]] = {}
    for identity in retained_identities:
        parsed = _identity_parts(identity)
        if parsed:
            retained_by_slot.setdefault(parsed[0], set()).add(parsed[1])
    rollup_overlap = False
    for entry in rollup_entries:
        slot_id = int(entry.get("slot_id", -1))
        first = int(entry.get("first_version_id", -1))
        last = int(entry.get("last_version_id", -1))
        if any(first <= version <= last for version in retained_by_slot.get(slot_id, set())):
            rollup_overlap = True
            break

    compaction_only_outside = (
        retention >= 0
        and all(count <= retention for count in detail_counts)
        and not bool(detailed_witness_identities & retained_identities)
        and not rollup_overlap
    )
    loss_witness_present = bool(witnesses) or rollup_count > 0
    fx06 = {
        "compaction_only_outside_retention_scope": compaction_only_outside,
        "loss_witness_present": loss_witness_present,
        "loss_witness_valid": loss_witness_present and detailed_witness_valid and rollup_valid,
    }

    fx07_raw = fixture("BPV1-FX07-TRUNCATION-ROLLBACK")
    corruption_records = _list(fx07_raw.get("corruption_records"), "FX07.corruption_records")
    corruption_found = bool(corruption_records)
    slot_corrupted = fx07_raw.get("slot_corrupted") is True
    fx07 = {
        "rollback_or_truncation_surfaced": corruption_found and slot_corrupted,
        "intact_accountability_claim_after_corruption": corruption_found and not slot_corrupted,
    }

    fx08_raw = fixture("BPV1-FX08-FORGED-AUTHORITY")
    fx08_current = _mapping(fx08_raw.get("current"), "FX08.current")
    rejected = [_mapping(value, "FX08.rejected") for value in _list(fx08_raw.get("rejected_attempts"), "FX08.rejected_attempts")]
    forged = "AUTH-FORGED-EVIL"
    fx08 = {
        "forged_authority_accepted": fx08_current.get("authority") == forged,
        "unsupported_or_failure_exposed": any(value.get("attempted_authority") == forged for value in rejected),
    }

    fx09_current = _mapping(fixture("BPV1-FX09-WITHHELD-COUNTEREVIDENCE").get("current"), "FX09.current")
    fx09_position = fx09_current.get("epistemic_position")
    fx09 = {
        "withheld_counterevidence_scoped_uncertainty": fx09_position == "SCOPED_UNCERTAIN",
        "fabricated_certainty": fx09_position == "SUPPORTED",
    }

    fx10_raw = fixture("BPV1-FX10-DECLARED-LOSS-AND-UNSUPPORTED")
    has_loss = int(fx10_raw.get("compacted_summary_count", 0)) > 0 or int(fx10_raw.get("loss_witness_record_count", 0)) > 0
    preservation_state = "LOSSY" if has_loss else "FULL"
    fx10 = {
        "preservation_state": preservation_state,
        "full_conformance_claimed": preservation_state == "FULL",
    }

    fx11_raw = fixture("BPV1-FX11-NON-EVENT-HISTORY")
    fx11: dict[str, Any] = {
        "current_accountability_available": int(fx11_raw.get("active_slot_count", 0)) > 0
        and int(fx11_raw.get("active_slot_count", 0)) == int(fx11_raw.get("accountable_slot_count", -1)),
    }
    for field in ("authoritative_per_operation_append_log", "exact_replay_required"):
        if field in structural:
            fx11[field] = structural[field]

    fx12_raw = fixture("BPV1-FX12-HIDDEN-SEMANTIC-DIVERGENCE")
    fx12_a = _mapping(fx12_raw.get("a"), "FX12.a")
    fx12_b = _mapping(fx12_raw.get("b"), "FX12.b")
    values_match = fx12_a.get("proposition") == fx12_b.get("proposition") and fx12_a.get("context") == fx12_b.get("context")
    divergence = values_match and any(
        fx12_a.get(field) != fx12_b.get(field)
        for field in ("source", "evidence", "authority", "predecessor_version_id")
    )
    fx12 = {
        "final_values_match": values_match,
        "material_semantic_divergence_detected": divergence,
        "full_conformance_claimed": not divergence,
    }

    checkpoints = [_mapping(value, "workload.checkpoint") for value in _list(workload_raw.get("checkpoints"), "workload.checkpoints")]
    bytes_by_mutation = {int(value.get("mutation", -1)): int(value.get("durable_bytes", -1)) for value in checkpoints}
    workload: dict[str, Any] = {
        "mutation_count": int(workload_raw.get("mutation_count", -1)),
        "checkpoint_count": len(checkpoints),
        "retained_detailed_predecessors": sum(detail_counts),
        "loss_witness_count": len(witnesses) + int(rollup_count > 0),
    }
    for mutation in (128, 256, 512):
        if mutation in bytes_by_mutation:
            workload[f"durable_bytes_at_{mutation}"] = bytes_by_mutation[mutation]
    if 256 in bytes_by_mutation and 512 in bytes_by_mutation:
        workload["growth_rule_passed"] = bytes_by_mutation[512] * 4 <= bytes_by_mutation[256] * 5 + 16384

    observations = {
        "protocol": OBSERVATION_PROTOCOL,
        "scenario_id": raw.get("scenario_id"),
        "plan_sha256": raw.get("plan_sha256"),
        "fixtures": {
            "BPV1-FX01-UNKNOWN-NOT-FALSE": fx01,
            "BPV1-FX02-ROLE-NONCONFLATION": fx02,
            "BPV1-FX03-CONTEXT-BINDING": fx03,
            "BPV1-FX04-REVISION-SUPERSESSION": fx04,
            "BPV1-FX05-UNRESOLVED-PLURALITY": fx05,
            "BPV1-FX06-BOUNDED-COMPACTION": fx06,
            "BPV1-FX07-TRUNCATION-ROLLBACK": fx07,
            "BPV1-FX08-FORGED-AUTHORITY": fx08,
            "BPV1-FX09-WITHHELD-COUNTEREVIDENCE": fx09,
            "BPV1-FX10-DECLARED-LOSS-AND-UNSUPPORTED": fx10,
            "BPV1-FX11-NON-EVENT-HISTORY": fx11,
            "BPV1-FX12-HIDDEN-SEMANTIC-DIVERGENCE": fx12,
        },
        "workload": workload,
        "subject": structural,
    }

    qualification_report = {
        "protocol": QUALIFICATION_PROTOCOL,
        "scenario_id": raw.get("scenario_id"),
        "plan_sha256": raw.get("plan_sha256"),
        "mode": "EXTERNAL_RAW_FACT_DERIVATION_PLUS_STATIC_SOURCE_AUDIT",
        "oracle_fixture_expectations_read": False,
        "implementation_private_runtime_state_read": False,
        "subject_self_report_used_for_structural_oracle_fields": False,
        "structural": structural_report,
        "derived_structural_facts": structural,
        "status": "QUALIFIED" if {"authoritative_per_operation_append_log", "exact_replay_required"}.issubset(structural) else "INDETERMINATE",
    }
    return observations, qualification_report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("raw_observations", type=Path)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--qualification-report", type=Path, required=True)
    args = parser.parse_args()
    try:
        observations, report = qualify(_load_json(args.raw_observations), args.repo.resolve())
    except (QualificationError, OSError) as exc:
        print(f"BPV1 external qualification failed: {exc}")
        return 2
    rendered = json.dumps(observations, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    report_rendered = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    args.qualification_report.parent.mkdir(parents=True, exist_ok=True)
    args.qualification_report.write_text(report_rendered, encoding="utf-8")
    print(f"BPV1 external qualification: {report['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
