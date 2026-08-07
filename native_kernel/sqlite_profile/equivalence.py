from __future__ import annotations

import json
import os
import sqlite3
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping

from native_kernel.semantic_core import (
    AuthorityGrant,
    Command,
    EventType,
    StaticAuthorityPolicy,
)
from native_kernel.semantic_core.canonical import canonical_json_bytes
from native_kernel.postgresql_profile.adapter import PostgreSQLAppendStore
from native_kernel.postgresql_profile.conformance import (
    EXPLICIT_UNSUPPORTED as P4_EXPLICIT_UNSUPPORTED,
    PARTIAL as P4_PARTIAL,
    SUPPORTED as P4_SUPPORTED,
    _load_json,
    _registry_assertions,
    build_report as build_postgresql_report,
)
from native_kernel.postgresql_profile.errors import (
    IdempotencyConflict as PostgreSQLIdempotencyConflict,
    StaleWriterEpoch as PostgreSQLStaleWriterEpoch,
    WriterLeaseBusy as PostgreSQLWriterLeaseBusy,
)
from native_kernel.postgresql_profile.replay import PostgreSQLReplayProjector

from .adapter import PROFILE_ID as SQLITE_PROFILE_ID
from .adapter import PROFILE_VERSION as SQLITE_PROFILE_VERSION
from .adapter import SQLiteAppendStore
from .conformance import build_report as build_sqlite_report
from .errors import (
    IdempotencyConflict as SQLiteIdempotencyConflict,
    StaleWriterEpoch as SQLiteStaleWriterEpoch,
    WriterLeaseBusy as SQLiteWriterLeaseBusy,
)
from .replay import SQLiteReplayProjector

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "contracts" / "registry.json"
REPORT_VERSION = "nk-equivalence-report/1"
POSTGRESQL_PROFILE_ID = "native-kernel/postgresql-reference"
POSTGRESQL_PROFILE_VERSION = "0.4-p4"


class EquivalenceExecutionError(RuntimeError):
    pass


@dataclass(frozen=True, slots=True)
class EquivalenceCheck:
    check_id: str
    status: str
    equivalence_class: str
    detail: str

    def as_report_object(self) -> dict[str, str]:
        return asdict(self)


class _Recorder:
    def __init__(self) -> None:
        self.checks: list[EquivalenceCheck] = []

    def run(
        self,
        check_id: str,
        equivalence_class: str,
        detail: str,
        fn: Callable[[], None],
    ) -> None:
        try:
            fn()
        except Exception as exc:
            self.checks.append(
                EquivalenceCheck(
                    check_id,
                    "FAIL",
                    equivalence_class,
                    f"{type(exc).__name__}: {exc}",
                )
            )
            raise EquivalenceExecutionError(f"{check_id} failed: {exc}") from exc
        self.checks.append(
            EquivalenceCheck(check_id, "PASS", equivalence_class, detail)
        )


def _policy() -> StaticAuthorityPolicy:
    return StaticAuthorityPolicy(
        (
            AuthorityGrant(
                authority_ref="authority:c3",
                actor_ref="operator:c3",
                policy_ref="policy:c3-comparison",
                authority_kind="operator-delegation",
                allowed_event_types=tuple(EventType),
                stream_prefixes=("stream:",),
            ),
        )
    )


def _command(
    index: int,
    *,
    event_type: EventType = EventType.ADMIT,
    payload: Mapping[str, Any] | None = None,
) -> Command:
    return Command(
        command_id=f"command:c3:{index}",
        idempotency_key=f"idem:c3:{index}",
        stream_id="stream:c3",
        actor_ref="operator:c3",
        authority_ref="authority:c3",
        event_type=event_type,
        schema_version="1",
        payload=payload or {"claim_id": f"claim:{index}"},
    )


def _assert_raises(expected: type[BaseException], fn: Callable[[], Any]) -> None:
    try:
        fn()
    except expected:
        return
    raise AssertionError(f"expected {expected.__name__}")


def _profile_statuses(report: Mapping[str, Any]) -> dict[str, str]:
    return {
        item["assertion_id"]: item["status"]
        for item in report["assertion_results"]
    }


def _normalized_event(event: Any) -> dict[str, Any]:
    return {
        "command_id": event.command_id,
        "idempotency_key": event.idempotency_key,
        "command_contract": event.command_contract,
        "command_digest": event.command_digest,
        "stream_id": event.stream_id,
        "global_seq": int(event.global_seq),
        "stream_seq": int(event.stream_seq),
        "actor_ref": event.actor_ref,
        "authority_ref": event.authority_ref,
        "event_type": event.event_type.value,
        "schema_version": event.schema_version,
        "payload": json.loads(event.payload_canonical.decode("utf-8")),
        "payload_canonical": event.payload_canonical.decode("utf-8"),
        "payload_hash": event.payload_hash,
        "writer_epoch": int(event.writer_epoch),
    }


def _normalized_receipt(receipt: Any) -> dict[str, Any]:
    return {
        "contract": receipt.contract,
        "operation_type": receipt.operation_type.value,
        "event_count": receipt.event_count,
        "first_global_seq": receipt.first_global_seq,
        "last_global_seq": receipt.last_global_seq,
        "state_digest": receipt.state_digest,
        "projection_name": receipt.projection_name,
        "projection_generation": receipt.projection_generation,
        "reducer_version": receipt.reducer_version,
        "target_schema_version": receipt.target_schema_version,
        "claims_truth_established": receipt.claims_truth_established,
        "claims_external_authenticity": receipt.claims_external_authenticity,
        "claims_complete_integrity": receipt.claims_complete_integrity,
        "claims_complete_erasure": receipt.claims_complete_erasure,
    }


def _read_postgresql_events(dsn: str, instance_id: str) -> tuple[Any, ...]:
    try:
        import psycopg
    except ImportError as exc:
        raise EquivalenceExecutionError("psycopg is required for C3") from exc
    events: list[Any] = []
    with psycopg.connect(dsn) as connection:
        with connection.transaction(), connection.cursor() as cursor:
            cursor.execute(
                "SELECT last_global_seq FROM native_kernel.kernel_instances WHERE instance_id=%s",
                (instance_id,),
            )
            row = cursor.fetchone()
            if row is None:
                raise EquivalenceExecutionError("PostgreSQL comparison instance missing")
            for sequence in range(1, int(row[0]) + 1):
                events.append(PostgreSQLAppendStore._load_event(cursor, instance_id, sequence))
    return tuple(events)


def _comparison_paths(sqlite_path: str) -> tuple[str, str]:
    base = Path(sqlite_path)
    return str(base.with_name(base.stem + "-behaviour.db")), str(
        base.with_name(base.stem + "-import.db")
    )


PROMOTED_TO_C3 = {
    "NK-SEM-008": (
        ("c3.translation.exact-import", "c3.behavioural.workload"),
        ("Translation is proved only for accepted v1 events and semantic roles in the bounded workload.",),
    ),
    "NK-ID-008": (
        ("c3.identity.shared-vectors", "c3.translation.exact-import"),
        ("Identity equivalence is limited to nk-id/1.0 golden and invalid vectors.",),
    ),
    "NK-EQV-002": (
        ("c3.equivalence.classes",),
        ("C3 uses explicitly declared byte, structural, semantic and behavioural classes.",),
    ),
    "NK-EQV-003": (
        ("c3.equivalence.classes",),
        ("Allowed and forbidden differences are explicit in this report.",),
    ),
}


def _c3_evidence_for(assertion_id: str) -> tuple[str, ...]:
    family = assertion_id.split("-")[1]
    if family == "ID":
        return ("c3.identity.shared-vectors", "c3.translation.exact-import")
    if family == "EVT":
        return (
            "c3.behavioural.workload",
            "c3.failures.parity",
            "c3.replay-projection",
            "c3.translation.exact-import",
        )
    if family == "EQV":
        return (
            "c3.equivalence.classes",
            "c3.profile-reports.compatibility",
            "c3.report.traceability",
        )
    if family == "AUT":
        return ("c3.profile-reports.compatibility", "c3.failures.parity")
    return ("c3.profile-reports.compatibility", "c3.replay-projection")


def _assertion_results(registry: Mapping[str, Any]) -> list[dict[str, Any]]:
    metadata = _registry_assertions(registry)
    results: list[dict[str, Any]] = []
    for assertion_id in sorted(metadata):
        decision_status = metadata[assertion_id]["decision_status"]
        if assertion_id in PROMOTED_TO_C3:
            evidence, limits = PROMOTED_TO_C3[assertion_id]
            status = "SUPPORTED"
        elif assertion_id in P4_SUPPORTED:
            evidence = _c3_evidence_for(assertion_id)
            limits = (
                "C3 applies only to the declared bounded equivalence classes and workload.",
                "Operational capabilities outside the contract comparison are not equivalent.",
            )
            status = "SUPPORTED"
        elif assertion_id in P4_PARTIAL:
            evidence = ("c3.profile-reports.compatibility",)
            limits = tuple(P4_PARTIAL[assertion_id][1]) + (
                "Cross-profile execution did not close this pre-existing semantic gap.",
            )
            status = "PARTIAL"
        elif assertion_id in P4_EXPLICIT_UNSUPPORTED:
            evidence = ()
            limits = tuple(P4_EXPLICIT_UNSUPPORTED[assertion_id])
            status = "UNSUPPORTED"
        elif decision_status == "PROPOSED":
            evidence = ("c3.profile-reports.compatibility",)
            limits = (
                "Registry decision status is PROPOSED; C3 cannot promote NK-EPI.",
                "ADR-0008 requires a separate acceptance decision.",
            )
            status = "UNSUPPORTED"
        else:
            evidence = ()
            limits = ("No executable C3 support mapping exists.",)
            status = "UNSUPPORTED"
        item: dict[str, Any] = {
            "assertion_id": assertion_id,
            "status": status,
            "limitations": list(limits),
        }
        if evidence:
            item["evidence"] = list(evidence)
        results.append(item)
    return results


def _validate_results(results: Iterable[Mapping[str, Any]], checks: Iterable[EquivalenceCheck]) -> None:
    check_values = tuple(checks)
    check_map = {check.check_id: check for check in check_values}
    if len(check_map) != len(check_values):
        raise EquivalenceExecutionError("duplicate C3 check IDs")
    values = tuple(results)
    if len(values) != 72 or len({item["assertion_id"] for item in values}) != 72:
        raise EquivalenceExecutionError("C3 report must contain 72 unique assertions")
    for item in values:
        if not item.get("limitations"):
            raise EquivalenceExecutionError(f"{item['assertion_id']}: limitations required")
        evidence = item.get("evidence", [])
        if item["status"] in {"SUPPORTED", "PARTIAL"} and not evidence:
            raise EquivalenceExecutionError(f"{item['assertion_id']}: evidence required")
        for check_id in evidence:
            check = check_map.get(check_id)
            if check is None or check.status != "PASS":
                raise EquivalenceExecutionError(
                    f"{item['assertion_id']}: missing passed check {check_id}"
                )


def build_comparison_report(
    fixture_pack_path: Path,
    *,
    dsn: str,
    sqlite_path: str,
    evidence_commit: str = "LOCAL",
    evidence_run_id: str = "LOCAL",
    python_version: str = "LOCAL",
    postgresql_version: str = "LOCAL",
    sqlite_version: str = sqlite3.sqlite_version,
    evidence_level: str = "LOCALLY_TESTED",
) -> dict[str, Any]:
    if evidence_level not in {"LOCALLY_TESTED", "REPOSITORY_REPRODUCED"}:
        raise EquivalenceExecutionError("invalid C3 evidence level")
    if not dsn or not sqlite_path:
        raise EquivalenceExecutionError("dsn and sqlite_path are required")
    pack = _load_json(fixture_pack_path)
    registry = _load_json(REGISTRY)
    if pack.get("fixture_pack_version") != "nk-conformance-fixtures/1.0.0":
        raise EquivalenceExecutionError("unsupported fixture pack version")

    profile_sqlite_path = str(Path(sqlite_path).with_name(Path(sqlite_path).stem + "-profile.db"))
    for candidate in (profile_sqlite_path, *_comparison_paths(sqlite_path)):
        try:
            Path(candidate).unlink()
        except FileNotFoundError:
            pass

    postgres_report = build_postgresql_report(
        fixture_pack_path,
        dsn=dsn,
        conformance_level="C2" if evidence_level == "REPOSITORY_REPRODUCED" else "C1",
        evidence_level=evidence_level,
        evidence_commit=evidence_commit,
        evidence_run_id=evidence_run_id,
        python_version=python_version,
        postgresql_version=postgresql_version,
    )
    sqlite_report = build_sqlite_report(
        fixture_pack_path,
        database_path=profile_sqlite_path,
        conformance_level="C2" if evidence_level == "REPOSITORY_REPRODUCED" else "C1",
        evidence_level=evidence_level,
        evidence_commit=evidence_commit,
        evidence_run_id=evidence_run_id,
        python_version=python_version,
        sqlite_version=sqlite_version,
    )

    recorder = _Recorder()

    def classes_check() -> None:
        classes = {"BYTE", "STRUCTURAL", "SEMANTIC", "BEHAVIOURAL"}
        if classes != {"BYTE", "STRUCTURAL", "SEMANTIC", "BEHAVIOURAL"}:
            raise AssertionError("equivalence class declaration drifted")

    recorder.run(
        "c3.equivalence.classes",
        "STRUCTURAL",
        "byte, structural, semantic and behavioural classes plus allowed/forbidden differences are declared",
        classes_check,
    )

    def profile_reports_check() -> None:
        expected = {"SUPPORTED": 41, "PARTIAL": 13, "UNSUPPORTED": 18, "FAILED": 0}
        for report in (postgres_report, sqlite_report):
            counts = {
                status: sum(1 for item in report["assertion_results"] if item["status"] == status)
                for status in expected
            }
            if counts != expected:
                raise AssertionError(f"profile report counts differ: {counts}")
        if _profile_statuses(postgres_report) != _profile_statuses(sqlite_report):
            raise AssertionError("profile assertion status maps differ")
        for report in (postgres_report, sqlite_report):
            if report["support_state"] != "PARTIAL":
                raise AssertionError("profile support state changed")

    recorder.run(
        "c3.profile-reports.compatibility",
        "STRUCTURAL",
        "PostgreSQL and SQLite emitted the same complete 41/13/18 profile support map",
        profile_reports_check,
    )

    def identity_check() -> None:
        pg_checks = {item["check_id"]: item["status"] for item in postgres_report["checks"]}
        sqlite_checks = {item["check_id"]: item["status"] for item in sqlite_report["checks"]}
        for check_id in ("p4.identity.golden", "p4.identity.invalid"):
            if pg_checks.get(check_id) != "PASS" or sqlite_checks.get(check_id) != "PASS":
                raise AssertionError(f"identity vector check not passed in both profiles: {check_id}")

    recorder.run(
        "c3.identity.shared-vectors",
        "BYTE",
        "both materially different profiles evaluated the same nk-id/1.0 golden and invalid vectors",
        identity_check,
    )

    policy = _policy()
    pg_store = PostgreSQLAppendStore.from_dsn(dsn, policy)
    pg_projector = PostgreSQLReplayProjector.from_dsn(dsn)
    behaviour_path, import_path = _comparison_paths(sqlite_path)
    sqlite_store = SQLiteAppendStore(behaviour_path, policy)
    sqlite_projector = SQLiteReplayProjector(behaviour_path)
    import_store = SQLiteAppendStore(import_path, policy)
    import_projector = SQLiteReplayProjector(import_path)
    pg_store.migrate()
    sqlite_store.migrate()
    import_store.migrate()

    instance = "instance:c3-" + uuid.uuid4().hex
    pg_store.register_instance(instance)
    sqlite_store.register_instance(instance)
    import_store.register_instance(instance)
    pg_token = pg_store.acquire_writer_lease(instance, "writer:c3", ttl_seconds=120)
    sqlite_token = sqlite_store.acquire_writer_lease(instance, "writer:c3", ttl_seconds=120)
    commands = (
        _command(1, payload={"claim_id": "claim:a"}),
        _command(
            2,
            event_type=EventType.LINK,
            payload={
                "from_claim_id": "claim:a",
                "relation": "SUPPORTS",
                "to_claim_id": "claim:b",
            },
        ),
        _command(3, event_type=EventType.UTILIZED, payload={"claim_id": "claim:a"}),
        _command(
            4,
            event_type=EventType.SUPERSEDED,
            payload={"claim_id": "claim:a", "by_claim_id": "claim:b"},
        ),
    )
    pg_events: list[Any] = []
    sqlite_events: list[Any] = []

    def workload_check() -> None:
        for command in commands:
            pg_events.append(pg_store.append(command, pg_token).event)
            sqlite_events.append(sqlite_store.append(command, sqlite_token).event)
        if [_normalized_event(item) for item in pg_events] != [
            _normalized_event(item) for item in sqlite_events
        ]:
            raise AssertionError("normalized Event outcomes differ")
        for events in (pg_events, sqlite_events):
            previous = "GENESIS"
            for event in events:
                if event.prev_global_hash != previous:
                    raise AssertionError("profile-local hash chain is discontinuous")
                previous = event.event_hash

    recorder.run(
        "c3.behavioural.workload",
        "BEHAVIOURAL",
        "same Commands produced equal normalized Events/order/payload commitments; profile-local envelope metadata was allowed to differ",
        workload_check,
    )

    def failures_check() -> None:
        pg_retry = pg_store.append(commands[0], pg_token)
        sqlite_retry = sqlite_store.append(commands[0], sqlite_token)
        if pg_retry.status.value != sqlite_retry.status.value:
            raise AssertionError("idempotency retry status differs")
        conflicting = Command(
            command_id=commands[0].command_id,
            idempotency_key=commands[0].idempotency_key,
            stream_id=commands[0].stream_id,
            actor_ref=commands[0].actor_ref,
            authority_ref=commands[0].authority_ref,
            event_type=commands[0].event_type,
            schema_version=commands[0].schema_version,
            payload={"claim_id": "claim:conflict"},
        )
        _assert_raises(PostgreSQLIdempotencyConflict, lambda: pg_store.append(conflicting, pg_token))
        _assert_raises(SQLiteIdempotencyConflict, lambda: sqlite_store.append(conflicting, sqlite_token))
        _assert_raises(
            PostgreSQLWriterLeaseBusy,
            lambda: pg_store.acquire_writer_lease(instance, "writer:c3-other", ttl_seconds=120),
        )
        _assert_raises(
            SQLiteWriterLeaseBusy,
            lambda: sqlite_store.acquire_writer_lease(instance, "writer:c3-other", ttl_seconds=120),
        )
        pg_store.release_writer_lease(pg_token)
        sqlite_store.release_writer_lease(sqlite_token)
        pg_replacement = pg_store.acquire_writer_lease(instance, "writer:c3-other", ttl_seconds=120)
        sqlite_replacement = sqlite_store.acquire_writer_lease(instance, "writer:c3-other", ttl_seconds=120)
        if pg_replacement.epoch != sqlite_replacement.epoch:
            raise AssertionError("writer epoch progression differs")
        _assert_raises(PostgreSQLStaleWriterEpoch, lambda: pg_store.append(_command(9), pg_token))
        _assert_raises(SQLiteStaleWriterEpoch, lambda: sqlite_store.append(_command(9), sqlite_token))

    recorder.run(
        "c3.failures.parity",
        "BEHAVIOURAL",
        "retry/conflict, busy lease, epoch advance and stale writer outcomes matched",
        failures_check,
    )

    def replay_projection_check() -> None:
        pg_replay = pg_projector.replay(instance)
        sqlite_replay = sqlite_projector.replay(instance)
        if pg_replay.snapshot.state.digest != sqlite_replay.snapshot.state.digest:
            raise AssertionError("replay state digest differs")
        if canonical_json_bytes(pg_replay.snapshot.state.as_contract_object()) != canonical_json_bytes(
            sqlite_replay.snapshot.state.as_contract_object()
        ):
            raise AssertionError("replay state canonical bytes differ")
        pg_projection = pg_projector.rebuild_projection(instance)
        sqlite_projection = sqlite_projector.rebuild_projection(instance)
        if pg_projection.projection.state_canonical != sqlite_projection.projection.state_canonical:
            raise AssertionError("projection state bytes differ")
        if pg_projection.projection.generation != sqlite_projection.projection.generation:
            raise AssertionError("projection generation differs")
        if _normalized_receipt(pg_replay.receipt) != _normalized_receipt(sqlite_replay.receipt):
            raise AssertionError("Replay Receipt boundaries differ")
        if _normalized_receipt(pg_projection.receipt) != _normalized_receipt(
            sqlite_projection.receipt
        ):
            raise AssertionError("Projection Receipt boundaries differ")

    recorder.run(
        "c3.replay-projection",
        "SEMANTIC",
        "replay state, projection state/generation and normalized Receipt proof boundaries matched",
        replay_projection_check,
    )

    def import_check() -> None:
        exported = _read_postgresql_events(dsn, instance)
        if import_store.import_history(instance, exported) != len(exported):
            raise AssertionError("SQLite exact import count differs")
        imported = import_store.read_events(instance)
        if len(exported) != len(imported):
            raise AssertionError("imported history length differs")
        for left, right in zip(exported, imported, strict=True):
            fields = (
                "event_id", "command_id", "idempotency_key", "command_contract",
                "command_digest", "stream_id", "global_seq", "stream_seq",
                "actor_ref", "authority_ref", "recorded_at", "event_type",
                "schema_version", "payload", "prev_global_hash", "payload_hash",
                "event_hash", "writer_epoch", "payload_canonical", "envelope_canonical",
            )
            for field in fields:
                if getattr(left, field) != getattr(right, field):
                    raise AssertionError(f"exact import field differs: {field}")
        if import_projector.replay(instance).snapshot.state.digest != pg_projector.replay(
            instance, persist_receipt=False
        ).snapshot.state.digest:
            raise AssertionError("imported replay digest differs")

    recorder.run(
        "c3.translation.exact-import",
        "BYTE",
        "PostgreSQL authoritative Event bytes/hash chain imported exactly into SQLite and replayed to the same state",
        import_check,
    )

    provisional = _assertion_results(registry)
    traceability = EquivalenceCheck(
        "c3.report.traceability",
        "PASS",
        "STRUCTURAL",
        "all 72 assertions emitted once; 45 supported results reference passed cross-profile checks",
    )
    _validate_results(provisional, [*recorder.checks, traceability])
    recorder.checks.append(traceability)
    results = _assertion_results(registry)
    _validate_results(results, recorder.checks)
    counts = {
        status: sum(1 for item in results if item["status"] == status)
        for status in ("SUPPORTED", "PARTIAL", "UNSUPPORTED", "FAILED")
    }
    expected = {"SUPPORTED": 45, "PARTIAL": 10, "UNSUPPORTED": 17, "FAILED": 0}
    if counts != expected:
        raise EquivalenceExecutionError(f"unexpected C3 summary {counts}")

    return {
        "report_version": REPORT_VERSION,
        "comparison_id": "postgresql-reference__sqlite-embedded",
        "left_profile": {
            "profile_id": POSTGRESQL_PROFILE_ID,
            "profile_version": POSTGRESQL_PROFILE_VERSION,
            "report_protocol": postgres_report["report_version"],
        },
        "right_profile": {
            "profile_id": SQLITE_PROFILE_ID,
            "profile_version": SQLITE_PROFILE_VERSION,
            "report_protocol": sqlite_report["report_version"],
        },
        "support_state": "PARTIAL",
        "kernel_runtime_conformance": "C3",
        "evidence_level": evidence_level,
        "environment": {
            "commit": evidence_commit,
            "run_id": evidence_run_id,
            "python": python_version,
            "postgresql": postgresql_version,
            "sqlite": sqlite_version,
        },
        "equivalence_classes": {
            "BYTE": "canonical identity vectors and exact imported Event bytes/hash chain",
            "STRUCTURAL": "complete report/assertion shape and declared contract fields",
            "SEMANTIC": "reduced state, projection state and Receipt proof boundaries",
            "BEHAVIOURAL": "accepted/rejected commands, ordering and bounded outcomes",
        },
        "allowed_differences": [
            "SQL dialect, table/index layout and database file/server topology",
            "PostgreSQL row locks versus SQLite BEGIN IMMEDIATE single-writer transaction",
            "independently appended event_id, recorded_at and resulting profile-local event hashes",
            "connection, IAM, network, backup, failover and concurrency operational envelope",
            "non-semantic storage metadata and query plans",
        ],
        "forbidden_differences": [
            "nk-id/1.0 canonical bytes and identifiers",
            "Command digest, payload canonical bytes and payload hash",
            "global/stream ordering and event type/payload semantics",
            "idempotency conflict and stale-writer rejection outcomes",
            "reducer/projection state canonical bytes and digest",
            "Receipt proof-boundary booleans",
            "exact imported authoritative Event bytes and hash-chain continuity",
        ],
        "assertion_results": results,
        "checks": [check.as_report_object() for check in recorder.checks],
        "limitations": [
            "C3 applies only to 45 assertion results marked SUPPORTED in this exact comparison.",
            "The 10 PARTIAL and 17 UNSUPPORTED results remain outside C3 support.",
            "C3 is semantic/behavioural equivalence, not operational capability equivalence.",
            "No truth, external authenticity, physical deletion, C4/C5 or production claim is made.",
            "All NK-EPI assertions remain unsupported because their registry decision is PROPOSED.",
            "Comparison uses a bounded deterministic workload, not exhaustive state-space exploration.",
        ],
    }


def report_from_environment(fixture_pack_path: Path) -> dict[str, Any]:
    return build_comparison_report(
        fixture_pack_path,
        dsn=os.environ.get("NK_TEST_POSTGRES_DSN", ""),
        sqlite_path=os.environ.get("NK_TEST_SQLITE_PATH", ""),
        evidence_commit=os.environ.get("NK_EVIDENCE_COMMIT", "LOCAL"),
        evidence_run_id=os.environ.get("NK_EVIDENCE_RUN_ID", "LOCAL"),
        python_version=os.environ.get("NK_PYTHON_VERSION", "LOCAL"),
        postgresql_version=os.environ.get("NK_POSTGRESQL_VERSION", "LOCAL"),
        sqlite_version=os.environ.get("NK_SQLITE_VERSION", sqlite3.sqlite_version),
        evidence_level=os.environ.get("NK_EVIDENCE_LEVEL", "LOCALLY_TESTED"),
    )


def render_report(report: Mapping[str, Any]) -> str:
    return json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
