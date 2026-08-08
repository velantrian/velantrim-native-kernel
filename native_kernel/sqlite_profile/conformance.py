from __future__ import annotations

import json
import os
import sqlite3
import tempfile
import uuid
from pathlib import Path
from typing import Any, Iterable, Mapping

from native_kernel.semantic_core import (
    AuthorityGrant,
    Command,
    EventType,
    StaticAuthorityPolicy,
)
from native_kernel.postgresql_profile.conformance import (
    ConformanceCheck,
    ConformanceExecutionError,
    EXPLICIT_UNSUPPORTED as P4_EXPLICIT_UNSUPPORTED,
    PARTIAL as P4_PARTIAL,
    REGISTRY,
    REPORT_VERSION,
    SUPPORTED as P4_SUPPORTED,
    _CheckRecorder,
    _load_json,
    _registry_assertions,
    _run_semantic_checks,
    _validate_traceability,
)

from .adapter import EVIDENCE_LINEAGE, PROFILE_ID, PROFILE_VERSION, SQLiteAppendStore
from .errors import (
    HistoryAdvanced,
    IdempotencyConflict,
    StaleWriterEpoch,
    StoredEventCorrupt,
    WriterLeaseBusy,
)
from .models import AppendStatus
from .replay import SQLiteReplayProjector
from .runtime import linked_sqlite_version

REGISTRY_VERSION = "nk-contract-registry/1.1.0"


def _command(
    key: str,
    *,
    event_type: EventType = EventType.ADMIT,
    payload: Mapping[str, Any] | None = None,
    stream_id: str = "stream:p5",
    authority_ref: str = "authority:p5",
) -> Command:
    return Command(
        command_id="command:" + uuid.uuid4().hex,
        idempotency_key=key,
        stream_id=stream_id,
        actor_ref="operator:p5",
        authority_ref=authority_ref,
        event_type=event_type,
        schema_version="1",
        payload=payload or {"claim_id": "claim:a"},
    )


def _policy() -> StaticAuthorityPolicy:
    return StaticAuthorityPolicy(
        (
            AuthorityGrant(
                authority_ref="authority:p5",
                actor_ref="operator:p5",
                policy_ref="policy:p5-admission",
                authority_kind="operator-delegation",
                allowed_event_types=tuple(EventType),
                stream_prefixes=("stream:",),
            ),
        )
    )


def _assert_raises(expected: type[BaseException], fn: Any) -> None:
    try:
        fn()
    except expected:
        return
    raise AssertionError(f"expected {expected.__name__}")


def _run_sqlite_checks(database_path: str, recorder: _CheckRecorder) -> None:
    policy = _policy()
    store = SQLiteAppendStore(database_path, policy)
    projector = SQLiteReplayProjector(database_path)

    def migrations_check() -> None:
        first = store.migrate()
        if not first:
            raise AssertionError("fresh SQLite profile applied no migrations")
        if store.migrate() != ():
            raise AssertionError("repeated migration pass was not empty")

    recorder.run(
        "p5.sqlite.migrations",
        "numbered SQLite migrations applied and repeated migration pass was empty",
        migrations_check,
    )

    instance = "instance:" + uuid.uuid4().hex
    store.register_instance(instance)
    primary = store.acquire_writer_lease(instance, "writer:p5-primary", ttl_seconds=120)

    def writer_fencing_check() -> None:
        _assert_raises(
            WriterLeaseBusy,
            lambda: store.acquire_writer_lease(instance, "writer:p5-other", ttl_seconds=120),
        )
        store.release_writer_lease(primary)
        replacement = store.acquire_writer_lease(instance, "writer:p5-other", ttl_seconds=120)
        if replacement.epoch <= primary.epoch:
            raise AssertionError("writer epoch did not advance")
        _assert_raises(StaleWriterEpoch, lambda: store.append(_command("idem:p5:stale"), primary))

    recorder.run(
        "p5.sqlite.writer-fencing",
        "BEGIN IMMEDIATE profile reproduced busy lease, epoch advance and stale token rejection",
        writer_fencing_check,
    )

    instance = "instance:" + uuid.uuid4().hex
    store.register_instance(instance)
    token = store.acquire_writer_lease(instance, "writer:p5", ttl_seconds=120)

    def append_idempotency_check() -> None:
        command = _command("idem:p5:append")
        first = store.append(command, token)
        retry = store.append(command, token)
        if first.status is not AppendStatus.APPENDED:
            raise AssertionError("first append was not APPENDED")
        if retry.status is not AppendStatus.RETURN_ORIGINAL_APPEND_RESULT:
            raise AssertionError("retry did not return original result")
        if first.event.event_hash != retry.event.event_hash:
            raise AssertionError("retry returned a different Event")
        _assert_raises(
            IdempotencyConflict,
            lambda: store.append(
                _command("idem:p5:append", payload={"claim_id": "claim:different"}), token
            ),
        )
        if store.count_events(instance) != 1:
            raise AssertionError("idempotency conflict changed Event count")

    recorder.run(
        "p5.sqlite.append-idempotency",
        "append, same-digest retry and conflicting key reuse matched the event contract",
        append_idempotency_check,
    )

    def rollback_check() -> None:
        rollback_instance = "instance:" + uuid.uuid4().hex
        store.register_instance(rollback_instance)
        rollback_token = store.acquire_writer_lease(
            rollback_instance, "writer:p5-rollback", ttl_seconds=120
        )

        def fail_after_insert(_: object) -> None:
            raise RuntimeError("P5 fault injection")

        failing = SQLiteAppendStore(database_path, policy, fault_hook=fail_after_insert)
        command = _command("idem:p5:rollback")
        _assert_raises(RuntimeError, lambda: failing.append(command, rollback_token))
        if store.count_events(rollback_instance) != 0:
            raise AssertionError("failed append persisted an Event")
        result = store.append(command, rollback_token)
        if (result.event.global_seq, result.event.stream_seq) != (1, 1):
            raise AssertionError("rollback left a sequence gap")

    recorder.run(
        "p5.sqlite.rollback-ordering",
        "injected failure rolled back and next append retained contiguous sequences",
        rollback_check,
    )

    def replay_projection_check() -> None:
        replay_instance = "instance:" + uuid.uuid4().hex
        store.register_instance(replay_instance)
        replay_token = store.acquire_writer_lease(
            replay_instance, "writer:p5-replay", ttl_seconds=120
        )
        for command in (
            _command(
                "idem:p5:replay:1",
                payload={"claim_id": "claim:a"},
                stream_id="stream:p5-replay",
            ),
            _command(
                "idem:p5:replay:2",
                event_type=EventType.LINK,
                payload={
                    "from_claim_id": "claim:a",
                    "relation": "SUPPORTS",
                    "to_claim_id": "claim:b",
                },
                stream_id="stream:p5-replay",
            ),
            _command(
                "idem:p5:replay:3",
                event_type=EventType.UTILIZED,
                payload={"claim_id": "claim:a"},
                stream_id="stream:p5-replay",
            ),
        ):
            store.append(command, replay_token)
        replayed = projector.replay(replay_instance)
        if replayed.snapshot.event_count != 3 or replayed.snapshot.state.last_global_seq != 3:
            raise AssertionError("SQLite persisted replay did not cover history")
        if any(
            getattr(replayed.receipt, field)
            for field in (
                "claims_truth_established",
                "claims_external_authenticity",
                "claims_complete_integrity",
                "claims_complete_erasure",
            )
        ):
            raise AssertionError("Replay Receipt overclaimed")
        first = projector.rebuild_projection(replay_instance)
        if projector.load_projection(replay_instance) != first.projection:
            raise AssertionError("stored projection did not round-trip")
        if not projector.destroy_projection(replay_instance):
            raise AssertionError("projection destroy did not remove row")
        second = projector.rebuild_projection(replay_instance)
        if second.projection.state_digest != first.projection.state_digest:
            raise AssertionError("projection rebuild changed state")
        if second.projection.generation != first.projection.generation + 1:
            raise AssertionError("projection generation was not monotonic")

    recorder.run(
        "p5.sqlite.replay-projection",
        "persisted replay and projection destroy/rebuild with bounded Receipts were reproduced",
        replay_projection_check,
    )

    def stale_head_check() -> None:
        stale_instance = "instance:" + uuid.uuid4().hex
        store.register_instance(stale_instance)
        stale_token = store.acquire_writer_lease(
            stale_instance, "writer:p5-stale", ttl_seconds=120
        )
        store.append(_command("idem:p5:stale:before"), stale_token)

        def advance(_: object) -> None:
            store.append(_command("idem:p5:stale:after"), stale_token)

        stale = SQLiteReplayProjector(database_path, snapshot_hook=advance)
        _assert_raises(HistoryAdvanced, lambda: stale.rebuild_projection(stale_instance))
        if projector.count_receipts(stale_instance) != 0:
            raise AssertionError("stale rebuild committed a Receipt")

    recorder.run(
        "p5.sqlite.stale-head",
        "history advancement between replay and publication rejected obsolete projection",
        stale_head_check,
    )

    def corruption_check() -> None:
        corrupt_instance = "instance:" + uuid.uuid4().hex
        store.register_instance(corrupt_instance)
        corrupt_token = store.acquire_writer_lease(
            corrupt_instance, "writer:p5-corrupt", ttl_seconds=120
        )
        store.append(_command("idem:p5:corrupt"), corrupt_token)
        store.corrupt_payload_canonical_for_test(corrupt_instance, 1, b"{}")
        _assert_raises(
            StoredEventCorrupt,
            lambda: projector.replay(corrupt_instance, persist_receipt=False),
        )

    recorder.run(
        "p5.sqlite.corruption",
        "stored canonical payload corruption was detected before replay evidence",
        corruption_check,
    )


def _translated_mapping(
    source: Mapping[str, tuple[tuple[str, ...], tuple[str, ...]]]
) -> dict[str, tuple[tuple[str, ...], tuple[str, ...]]]:
    result: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {}
    for assertion_id, (evidence, limits) in source.items():
        translated = tuple(
            check.replace("p4.postgresql.", "p5.sqlite.").replace(
                "p4.report.traceability", "p5.report.traceability"
            )
            for check in evidence
        )
        replaced_limits = tuple(
            item.replace("PostgreSQL", "SQLite embedded")
            .replace("one profile", "one SQLite profile")
            .replace("P4", "P5 SQLite C2")
            for item in limits
        )
        result[assertion_id] = (translated, replaced_limits)
    return result


SUPPORTED = _translated_mapping(P4_SUPPORTED)
PARTIAL = _translated_mapping(P4_PARTIAL)
EXPLICIT_UNSUPPORTED = dict(P4_EXPLICIT_UNSUPPORTED)


def _assertion_results(registry: Mapping[str, Any]) -> list[dict[str, Any]]:
    metadata = _registry_assertions(registry)
    results: list[dict[str, Any]] = []
    for assertion_id in sorted(metadata):
        decision_status = metadata[assertion_id]["decision_status"]
        if assertion_id in SUPPORTED:
            evidence, limitations = SUPPORTED[assertion_id]
            status = "SUPPORTED"
        elif assertion_id in PARTIAL:
            evidence, limitations = PARTIAL[assertion_id]
            status = "PARTIAL"
        elif assertion_id in EXPLICIT_UNSUPPORTED:
            evidence = ()
            limitations = EXPLICIT_UNSUPPORTED[assertion_id]
            status = "UNSUPPORTED"
        elif decision_status == "PROPOSED":
            evidence = ("p4.registry.contracts",)
            limitations = (
                "Registry decision status is PROPOSED; P5 cannot promote this assertion.",
                "ADR-0008 and NK-EPI require a separate acceptance decision.",
            )
            status = "UNSUPPORTED"
        else:
            evidence = ()
            limitations = ("No executable SQLite support mapping exists.",)
            status = "UNSUPPORTED"
        item: dict[str, Any] = {
            "assertion_id": assertion_id,
            "status": status,
            "limitations": list(limitations),
        }
        if evidence:
            item["evidence"] = list(evidence)
        results.append(item)
    if len(results) != 72:
        raise ConformanceExecutionError(f"expected 72 results, found {len(results)}")
    return results


def build_report(
    fixture_pack_path: Path,
    *,
    database_path: str,
    conformance_level: str = "C1",
    evidence_level: str = "LOCALLY_TESTED",
    evidence_commit: str = "LOCAL",
    evidence_run_id: str = "LOCAL",
    python_version: str = "LOCAL",
    sqlite_version: str = sqlite3.sqlite_version,
) -> dict[str, Any]:
    sqlite_version = linked_sqlite_version(sqlite_version)
    if conformance_level not in {"C1", "C2"}:
        raise ConformanceExecutionError("SQLite adapter supports only C1 or C2")
    if evidence_level not in {"LOCALLY_TESTED", "REPOSITORY_REPRODUCED"}:
        raise ConformanceExecutionError("invalid SQLite evidence level")
    if conformance_level == "C2" and evidence_level != "REPOSITORY_REPRODUCED":
        raise ConformanceExecutionError("C2 requires REPOSITORY_REPRODUCED")
    if not database_path:
        raise ConformanceExecutionError("database_path must be non-empty")
    pack = _load_json(fixture_pack_path)
    if pack.get("fixture_pack_version") != "nk-conformance-fixtures/1.0.0":
        raise ConformanceExecutionError("unsupported fixture pack version")
    registry = _load_json(REGISTRY)
    recorder = _CheckRecorder()
    _run_semantic_checks(pack, recorder)
    _run_sqlite_checks(database_path, recorder)
    recorder.run(
        "p5.environment.metadata",
        (
            f"profile={PROFILE_ID}@{PROFILE_VERSION}; commit={evidence_commit}; "
            f"run={evidence_run_id}; python={python_version}; sqlite={sqlite_version}"
        ),
        lambda: None,
    )
    provisional = _assertion_results(registry)
    traceability = ConformanceCheck(
        "p5.report.traceability",
        "PASS",
        "all 72 assertions emitted once with evidence/limitations; NK-EPI remained unsupported",
    )
    _validate_traceability(provisional, [*recorder.checks, traceability])
    recorder.checks.append(traceability)
    results = _assertion_results(registry)
    _validate_traceability(results, recorder.checks)
    counts = {
        status: sum(1 for item in results if item["status"] == status)
        for status in ("SUPPORTED", "PARTIAL", "UNSUPPORTED", "FAILED")
    }
    expected = {"SUPPORTED": 41, "PARTIAL": 13, "UNSUPPORTED": 18, "FAILED": 0}
    if counts != expected:
        raise ConformanceExecutionError(f"unexpected SQLite summary {counts}")
    return {
        "report_version": REPORT_VERSION,
        "profile_id": PROFILE_ID,
        "profile_version": PROFILE_VERSION,
        "support_state": "PARTIAL",
        "kernel_runtime_conformance": conformance_level,
        "evidence_level": evidence_level,
        "assertion_results": results,
        "checks": [check.as_report_object() for check in recorder.checks],
        "limitations": [
            "C1/C2 applies only to SQLite assertion results marked SUPPORTED at this evidence scope.",
            "PARTIAL and UNSUPPORTED assertions remain outside supported conformance.",
            "SQLite C2 alone is not C3 cross-profile equivalence.",
            "SQLite operational envelope is embedded/single-file and not PostgreSQL operational equivalence.",
            "No truth, external authenticity, physical deletion, C4/C5 or production claim is made.",
            f"Evidence lineage is {EVIDENCE_LINEAGE}; independent from v0.1.2.1 recovery.",
        ],
    }


def report_from_environment(fixture_pack_path: Path) -> dict[str, Any]:
    return build_report(
        fixture_pack_path,
        database_path=os.environ.get("NK_TEST_SQLITE_PATH", ""),
        conformance_level=os.environ.get("NK_CONFORMANCE_LEVEL", "C1"),
        evidence_level=os.environ.get("NK_EVIDENCE_LEVEL", "LOCALLY_TESTED"),
        evidence_commit=os.environ.get("NK_EVIDENCE_COMMIT", "LOCAL"),
        evidence_run_id=os.environ.get("NK_EVIDENCE_RUN_ID", "LOCAL"),
        python_version=os.environ.get("NK_PYTHON_VERSION", "LOCAL"),
        sqlite_version=os.environ.get("NK_SQLITE_VERSION", sqlite3.sqlite_version),
    )


def render_report(report: Mapping[str, Any]) -> str:
    return json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
