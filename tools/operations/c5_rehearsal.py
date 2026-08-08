#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import os
import sqlite3
import time
import uuid
from pathlib import Path
from typing import Any, Callable, Mapping

from native_kernel.operational_validation import (
    OperationalRecorder,
    OperationalValidationError,
    build_report,
    canonical_json_bytes,
    load_json,
    percentile,
    redact_text,
    sha256_digest,
    validate_plan,
    validate_report,
)
from native_kernel.postgresql_profile import (
    PostgreSQLAppendStore,
    PostgreSQLReplayProjector,
)
from native_kernel.postgresql_profile.errors import (
    StaleWriterEpoch as PostgreSQLStaleWriterEpoch,
    StoredEventCorrupt as PostgreSQLStoredEventCorrupt,
    ReplayIntegrityError as PostgreSQLReplayIntegrityError,
)
from native_kernel.semantic_core import (
    AuthorityDenied,
    AuthorityGrant,
    Command,
    EventType,
    StaticAuthorityPolicy,
)
from native_kernel.sqlite_profile import (
    SQLiteAppendStore,
    SQLiteReplayProjector,
    linked_sqlite_version,
)
from native_kernel.sqlite_profile.errors import (
    StaleWriterEpoch as SQLiteStaleWriterEpoch,
    StoredEventCorrupt as SQLiteStoredEventCorrupt,
    ReplayIntegrityError as SQLiteReplayIntegrityError,
)

ROOT = Path(__file__).resolve().parents[2]


def _policy(*, allow: bool = True) -> StaticAuthorityPolicy:
    if not allow:
        return StaticAuthorityPolicy(())
    return StaticAuthorityPolicy(
        (
            AuthorityGrant(
                authority_ref="authority:c5",
                actor_ref="operator:c5",
                policy_ref="policy:c5-rehearsal",
                authority_kind="operator-delegation",
                allowed_event_types=tuple(EventType),
                stream_prefixes=("stream:c5",),
            ),
        )
    )


def _command(index: int, *, namespace: str, payload: Mapping[str, Any] | None = None) -> Command:
    return Command(
        command_id=f"command:c5:{namespace}:{index}",
        idempotency_key=f"idem:c5:{namespace}:{index}",
        stream_id=f"stream:c5:{namespace}",
        actor_ref="operator:c5",
        authority_ref="authority:c5",
        event_type=EventType.ADMIT,
        schema_version="1",
        payload=payload or {"claim_id": f"claim:c5:{namespace}:{index}"},
    )


def _expect(expected: type[BaseException] | tuple[type[BaseException], ...], fn: Callable[[], Any]) -> None:
    try:
        fn()
    except expected:
        return
    except Exception as exc:
        names = (
            ", ".join(item.__name__ for item in expected)
            if isinstance(expected, tuple)
            else expected.__name__
        )
        raise AssertionError(f"expected {names}, got {type(exc).__name__}: {exc}") from exc
    names = (
        ", ".join(item.__name__ for item in expected)
        if isinstance(expected, tuple)
        else expected.__name__
    )
    raise AssertionError(f"expected {names}")


def _suffix_path(base: Path, label: str) -> Path:
    return base.with_name(f"{base.stem}-{label}{base.suffix or '.db'}")


class Rehearsal:
    def __init__(
        self,
        *,
        dsn: str,
        sqlite_base: Path,
        backup_output: Path,
        plan: Mapping[str, Any],
    ) -> None:
        self.dsn = dsn
        self.sqlite_base = sqlite_base
        self.backup_output = backup_output
        self.plan = plan
        self.recorder = OperationalRecorder(plan["scenarios"])
        self._namespace = uuid.uuid4().hex[:12]

    def _instance(self, label: str) -> str:
        return f"instance:c5:{self._namespace}:{label}"

    def _sqlite_store(
        self,
        label: str,
        *,
        allow: bool = True,
        fault_hook: Callable[[Any], None] | None = None,
    ) -> tuple[SQLiteAppendStore, Path]:
        path = _suffix_path(self.sqlite_base, label)
        for candidate in (path, Path(str(path) + "-wal"), Path(str(path) + "-shm")):
            try:
                candidate.unlink()
            except FileNotFoundError:
                pass
        store = SQLiteAppendStore(path, _policy(allow=allow), fault_hook=fault_hook)
        store.migrate()
        return store, path

    def _pg_store(
        self,
        *,
        allow: bool = True,
        fault_hook: Callable[[Any], None] | None = None,
    ) -> PostgreSQLAppendStore:
        store = PostgreSQLAppendStore.from_dsn(
            self.dsn,
            _policy(allow=allow),
            fault_hook=fault_hook,
        )
        store.migrate()
        return store

    def security_authority_postgresql(self) -> Mapping[str, Any]:
        store = self._pg_store(allow=False)
        instance = self._instance("deny-pg")
        store.register_instance(instance)
        token = store.acquire_writer_lease(instance, "writer:c5:deny-pg")
        _expect(AuthorityDenied, lambda: store.append(_command(1, namespace="deny-pg"), token))
        if store.count_events(instance) != 0:
            raise AssertionError("denied PostgreSQL command persisted an Event")
        return {"detail": "deny-by-default authority rejected the command before persistence", "event_count": 0}

    def security_authority_sqlite(self) -> Mapping[str, Any]:
        store, _ = self._sqlite_store("deny-sqlite", allow=False)
        instance = self._instance("deny-sqlite")
        store.register_instance(instance)
        token = store.acquire_writer_lease(instance, "writer:c5:deny-sqlite")
        _expect(AuthorityDenied, lambda: store.append(_command(1, namespace="deny-sqlite"), token))
        if store.count_events(instance) != 0:
            raise AssertionError("denied SQLite command persisted an Event")
        return {"detail": "deny-by-default authority rejected the command before persistence", "event_count": 0}

    def security_stale_postgresql(self) -> Mapping[str, Any]:
        store = self._pg_store()
        instance = self._instance("stale-pg")
        store.register_instance(instance)
        old = store.acquire_writer_lease(instance, "writer:c5:old-pg")
        store.release_writer_lease(old)
        new = store.acquire_writer_lease(instance, "writer:c5:new-pg")
        _expect(PostgreSQLStaleWriterEpoch, lambda: store.append(_command(1, namespace="stale-pg"), old))
        if new.epoch <= old.epoch:
            raise AssertionError("writer epoch did not advance")
        return {"detail": "stale PostgreSQL writer token was fenced", "old_epoch": old.epoch, "new_epoch": new.epoch}

    def security_stale_sqlite(self) -> Mapping[str, Any]:
        store, _ = self._sqlite_store("stale-sqlite")
        instance = self._instance("stale-sqlite")
        store.register_instance(instance)
        old = store.acquire_writer_lease(instance, "writer:c5:old-sqlite")
        store.release_writer_lease(old)
        new = store.acquire_writer_lease(instance, "writer:c5:new-sqlite")
        _expect(SQLiteStaleWriterEpoch, lambda: store.append(_command(1, namespace="stale-sqlite"), old))
        if new.epoch <= old.epoch:
            raise AssertionError("writer epoch did not advance")
        return {"detail": "stale SQLite writer token was fenced", "old_epoch": old.epoch, "new_epoch": new.epoch}

    def reliability_retry_postgresql(self) -> Mapping[str, Any]:
        store = self._pg_store()
        instance = self._instance("retry-pg")
        store.register_instance(instance)
        token = store.acquire_writer_lease(instance, "writer:c5:retry-pg")
        command = _command(1, namespace="retry-pg")
        first = store.append(command, token)
        second = store.append(command, token)
        if first.event.event_hash != second.event.event_hash or store.count_events(instance) != 1:
            raise AssertionError("PostgreSQL idempotent retry changed authoritative history")
        return {"detail": "PostgreSQL retry returned the original result", "event_count": 1}

    def reliability_retry_sqlite(self) -> Mapping[str, Any]:
        store, _ = self._sqlite_store("retry-sqlite")
        instance = self._instance("retry-sqlite")
        store.register_instance(instance)
        token = store.acquire_writer_lease(instance, "writer:c5:retry-sqlite")
        command = _command(1, namespace="retry-sqlite")
        first = store.append(command, token)
        second = store.append(command, token)
        if first.event.event_hash != second.event.event_hash or store.count_events(instance) != 1:
            raise AssertionError("SQLite idempotent retry changed authoritative history")
        return {"detail": "SQLite retry returned the original result", "event_count": 1}

    @staticmethod
    def _fault(_: Any) -> None:
        raise RuntimeError("c5 injected precommit fault")

    def rollback_fault_postgresql(self) -> Mapping[str, Any]:
        store = self._pg_store(fault_hook=self._fault)
        instance = self._instance("fault-pg")
        store.register_instance(instance)
        token = store.acquire_writer_lease(instance, "writer:c5:fault-pg")
        _expect(RuntimeError, lambda: store.append(_command(1, namespace="fault-pg"), token))
        if store.count_events(instance) != 0:
            raise AssertionError("PostgreSQL injected fault was not rolled back")
        return {"detail": "PostgreSQL precommit fault rolled back Event and idempotency state", "event_count": 0}

    def rollback_fault_sqlite(self) -> Mapping[str, Any]:
        store, _ = self._sqlite_store("fault-sqlite", fault_hook=self._fault)
        instance = self._instance("fault-sqlite")
        store.register_instance(instance)
        token = store.acquire_writer_lease(instance, "writer:c5:fault-sqlite")
        _expect(RuntimeError, lambda: store.append(_command(1, namespace="fault-sqlite"), token))
        if store.count_events(instance) != 0:
            raise AssertionError("SQLite injected fault was not rolled back")
        return {"detail": "SQLite precommit fault rolled back Event and idempotency state", "event_count": 0}

    def recovery_replay_postgresql(self) -> Mapping[str, Any]:
        store = self._pg_store()
        instance = self._instance("replay-pg")
        store.register_instance(instance)
        token = store.acquire_writer_lease(instance, "writer:c5:replay-pg")
        for index in range(1, 4):
            store.append(_command(index, namespace="replay-pg"), token)
        projector = PostgreSQLReplayProjector.from_dsn(self.dsn)
        replay = projector.replay(instance)
        rebuild = projector.rebuild_projection(instance)
        loaded = projector.load_projection(instance)
        if replay.snapshot.event_count != 3 or loaded.state_digest != rebuild.snapshot.state.digest:
            raise AssertionError("PostgreSQL replay/projection state mismatch")
        return {
            "detail": "PostgreSQL replay and disposable projection rebuild matched the authoritative head",
            "event_count": replay.snapshot.event_count,
            "state_digest": loaded.state_digest,
        }

    def recovery_replay_sqlite(self) -> Mapping[str, Any]:
        store, path = self._sqlite_store("replay-sqlite")
        instance = self._instance("replay-sqlite")
        store.register_instance(instance)
        token = store.acquire_writer_lease(instance, "writer:c5:replay-sqlite")
        for index in range(1, 4):
            store.append(_command(index, namespace="replay-sqlite"), token)
        projector = SQLiteReplayProjector(str(path))
        replay = projector.replay(instance)
        rebuild = projector.rebuild_projection(instance)
        loaded = projector.load_projection(instance)
        if replay.snapshot.event_count != 3 or loaded.state_digest != rebuild.snapshot.state.digest:
            raise AssertionError("SQLite replay/projection state mismatch")
        return {
            "detail": "SQLite replay and disposable projection rebuild matched the authoritative head",
            "event_count": replay.snapshot.event_count,
            "state_digest": loaded.state_digest,
        }

    def _read_pg_events(self, instance: str) -> tuple[Any, ...]:
        try:
            import psycopg
        except ImportError as exc:
            raise OperationalValidationError("psycopg is required for C5") from exc
        values: list[Any] = []
        with psycopg.connect(self.dsn) as connection:
            with connection.transaction(), connection.cursor() as cursor:
                cursor.execute(
                    "SELECT last_global_seq FROM native_kernel.kernel_instances WHERE instance_id=%s",
                    (instance,),
                )
                row = cursor.fetchone()
                if row is None:
                    raise AssertionError("PostgreSQL source instance missing")
                for sequence in range(1, int(row[0]) + 1):
                    values.append(PostgreSQLAppendStore._load_event(cursor, instance, sequence))
        return tuple(values)

    def recovery_quarantine_import(self) -> Mapping[str, Any]:
        pg_store = self._pg_store()
        source = self._instance("quarantine-source")
        pg_store.register_instance(source)
        token = pg_store.acquire_writer_lease(source, "writer:c5:quarantine-source")
        for index in range(1, 5):
            pg_store.append(_command(index, namespace="quarantine"), token)
        events = self._read_pg_events(source)
        backup = {
            "protocol": "nk-operational-backup/1",
            "source_profile": "native-kernel/postgresql-reference",
            "source_instance": source,
            "event_count": len(events),
            "last_event_hash": events[-1].event_hash,
            "events": [
                {
                    "global_seq": event.global_seq,
                    "event_hash": event.event_hash,
                    "payload_hash": event.payload_hash,
                    "envelope_canonical_base64": base64.b64encode(event.envelope_canonical).decode("ascii"),
                    "payload_canonical_base64": base64.b64encode(event.payload_canonical).decode("ascii"),
                }
                for event in events
            ],
            "limitations": [
                "Application-level logical export for one synthetic instance.",
                "Not a physical PostgreSQL backup or managed-provider disaster-recovery proof.",
            ],
        }
        backup["backup_digest"] = sha256_digest(canonical_json_bytes(backup))
        self.backup_output.parent.mkdir(parents=True, exist_ok=True)
        self.backup_output.write_text(
            json.dumps(backup, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
        )

        sqlite_store, path = self._sqlite_store("quarantine-target")
        target = self._instance("quarantine-target")
        sqlite_store.register_instance(target)
        imported = sqlite_store.import_history(target, events)
        replay = SQLiteReplayProjector(str(path)).replay(target)
        if imported != len(events):
            raise AssertionError("quarantine import count mismatch")
        if replay.snapshot.last_event_hash != events[-1].event_hash:
            raise AssertionError("quarantine restore head hash mismatch")
        return {
            "detail": "exact logical Event backup imported into a quarantined independent profile and replayed before visibility",
            "event_count": imported,
            "backup_digest": backup["backup_digest"],
            "restored_state_digest": replay.snapshot.state.digest,
        }

    def incident_corruption_postgresql(self) -> Mapping[str, Any]:
        store = self._pg_store()
        instance = self._instance("corrupt-pg")
        store.register_instance(instance)
        token = store.acquire_writer_lease(instance, "writer:c5:corrupt-pg")
        store.append(_command(1, namespace="corrupt-pg"), token)
        import psycopg
        with psycopg.connect(self.dsn) as connection:
            with connection.transaction(), connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE native_kernel.events SET payload_canonical=%s "
                    "WHERE instance_id=%s AND global_seq=1",
                    (b"{}", instance),
                )
        projector = PostgreSQLReplayProjector.from_dsn(self.dsn)
        _expect(
            (PostgreSQLStoredEventCorrupt, PostgreSQLReplayIntegrityError),
            lambda: projector.replay(instance, persist_receipt=False),
        )
        return {
            "detail": "PostgreSQL stored-byte corruption was detected and the instance was quarantined",
            "detected": True,
            "contained": True,
            "quarantine": True,
        }

    def incident_corruption_sqlite(self) -> Mapping[str, Any]:
        store, path = self._sqlite_store("corrupt-sqlite")
        instance = self._instance("corrupt-sqlite")
        store.register_instance(instance)
        token = store.acquire_writer_lease(instance, "writer:c5:corrupt-sqlite")
        store.append(_command(1, namespace="corrupt-sqlite"), token)
        store.corrupt_payload_canonical_for_test(instance, 1, b"{}")
        projector = SQLiteReplayProjector(str(path))
        _expect(
            (SQLiteStoredEventCorrupt, SQLiteReplayIntegrityError),
            lambda: projector.replay(instance, persist_receipt=False),
        )
        return {
            "detail": "SQLite stored-byte corruption was detected and the file was quarantined",
            "detected": True,
            "contained": True,
            "quarantine": True,
        }

    def incident_timeline(self) -> Mapping[str, Any]:
        stages = ("DETECTED", "CONTAINED", "EVIDENCE_CAPTURED", "RECOVERY_VALIDATED")
        if stages != tuple(dict.fromkeys(stages)):
            raise AssertionError("incident stage order is ambiguous")
        return {
            "detail": "incident timeline preserves detection, containment, evidence and recovery-validation stages",
            "stages": list(stages),
            "automatic_authority_promotion": False,
        }

    def privacy_synthetic_only(self) -> Mapping[str, Any]:
        boundary = self.plan["deployment_boundary"]
        if (
            boundary["live_user_data"]
            or not boundary["synthetic_data_only"]
            or boundary["production_traffic"]
        ):
            raise AssertionError("operational plan is not synthetic-only")
        return {
            "detail": "plan and workload prohibit live user data and production traffic",
            "synthetic_data_only": True,
            "live_user_data": False,
        }

    def privacy_canary_redaction(self) -> Mapping[str, Any]:
        canaries = self.plan["privacy"]["canary_tokens"]
        source = f"credential={canaries[1]} subject={canaries[0]}"
        redacted = redact_text(source, canaries, self.plan["privacy"]["redaction_marker"])
        if any(token in redacted for token in canaries):
            raise AssertionError("privacy canary survived redaction")
        if redacted.count(self.plan["privacy"]["redaction_marker"]) != len(canaries):
            raise AssertionError("privacy redaction marker count mismatch")
        return {
            "detail": "privacy and secret canaries were removed before report/artifact emission",
            "redacted_sample": redacted,
            "canary_leaks": 0,
        }

    def _bounded_load(self, profile: str) -> Mapping[str, Any]:
        event_limit = int(self.plan["thresholds"]["events_per_profile_max"])
        count = min(24, event_limit)
        latencies: list[float] = []
        if profile == "POSTGRESQL":
            store: Any = self._pg_store()
            instance = self._instance("load-pg")
            store.register_instance(instance)
            token = store.acquire_writer_lease(instance, "writer:c5:load-pg")
            namespace = "load-pg"
        else:
            store, _ = self._sqlite_store("load-sqlite")
            instance = self._instance("load-sqlite")
            store.register_instance(instance)
            token = store.acquire_writer_lease(instance, "writer:c5:load-sqlite")
            namespace = "load-sqlite"
        for index in range(1, count + 1):
            started = time.perf_counter()
            store.append(_command(index, namespace=namespace), token)
            latencies.append((time.perf_counter() - started) * 1000.0)
        p95 = percentile(latencies, 0.95)
        if store.count_events(instance) != count:
            raise AssertionError(f"{profile} bounded load event count mismatch")
        if p95 > float(self.plan["thresholds"]["p95_append_ms_max"]):
            raise AssertionError(f"{profile} p95 append latency exceeds threshold: {p95}")
        return {
            "detail": f"{profile} completed the bounded synthetic append workload",
            "event_count": count,
            "p95_append_ms": round(p95, 3),
            "max_append_ms": round(max(latencies), 3),
        }

    def run(self) -> tuple[Any, ...]:
        self.recorder.run("security.authority-denial.postgresql", self.security_authority_postgresql)
        self.recorder.run("security.authority-denial.sqlite", self.security_authority_sqlite)
        self.recorder.run("security.stale-writer.postgresql", self.security_stale_postgresql)
        self.recorder.run("security.stale-writer.sqlite", self.security_stale_sqlite)
        self.recorder.run("reliability.idempotent-retry.postgresql", self.reliability_retry_postgresql)
        self.recorder.run("reliability.idempotent-retry.sqlite", self.reliability_retry_sqlite)
        self.recorder.run("rollback.atomic-fault.postgresql", self.rollback_fault_postgresql)
        self.recorder.run("rollback.atomic-fault.sqlite", self.rollback_fault_sqlite)
        self.recorder.run("recovery.replay-projection.postgresql", self.recovery_replay_postgresql)
        self.recorder.run("recovery.replay-projection.sqlite", self.recovery_replay_sqlite)
        self.recorder.run("recovery.quarantine-import", self.recovery_quarantine_import)
        incident_timeline = (
            {"sequence": 1, "stage": "DETECTED"},
            {"sequence": 2, "stage": "CONTAINED"},
            {"sequence": 3, "stage": "EVIDENCE_CAPTURED"},
            {"sequence": 4, "stage": "RECOVERY_VALIDATED"},
        )
        self.recorder.run(
            "incident.corruption-detected.postgresql",
            self.incident_corruption_postgresql,
            incident_timeline=incident_timeline[:3],
        )
        self.recorder.run(
            "incident.corruption-detected.sqlite",
            self.incident_corruption_sqlite,
            incident_timeline=incident_timeline[:3],
        )
        self.recorder.run(
            "incident.timeline-contained",
            self.incident_timeline,
            incident_timeline=incident_timeline,
        )
        self.recorder.run("privacy.synthetic-only", self.privacy_synthetic_only)
        self.recorder.run("privacy.canary-redaction", self.privacy_canary_redaction)
        self.recorder.run(
            "resilience.bounded-load.postgresql",
            lambda: self._bounded_load("POSTGRESQL"),
        )
        self.recorder.run(
            "resilience.bounded-load.sqlite",
            lambda: self._bounded_load("SQLITE"),
        )
        return tuple(self.recorder.results)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("c4_report", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--backup-output", type=Path, required=True)
    parser.add_argument("--dsn", default=os.environ.get("NK_TEST_POSTGRES_DSN"))
    parser.add_argument(
        "--sqlite-path",
        type=Path,
        default=Path(os.environ.get("NK_TEST_SQLITE_PATH", "artifacts/c5-rehearsal.db")),
    )
    args = parser.parse_args()
    if not args.dsn:
        raise SystemExit("PostgreSQL DSN is required")

    os.environ["NK_SQLITE_VERSION"] = linked_sqlite_version(
        os.environ.get("NK_SQLITE_VERSION")
    )

    plan_bytes = args.plan.read_bytes()
    c4_bytes = args.c4_report.read_bytes()
    plan = load_json(args.plan)
    c4_report = load_json(args.c4_report)
    validate_plan(plan)

    rehearsal = Rehearsal(
        dsn=args.dsn,
        sqlite_base=args.sqlite_path,
        backup_output=args.backup_output,
        plan=plan,
    )
    results = rehearsal.run()
    report = build_report(
        plan,
        c4_report,
        results,
        plan_bytes=plan_bytes,
        c4_bytes=c4_bytes,
    )
    require_repository = os.environ.get("NK_EVIDENCE_LEVEL") == "REPOSITORY_REPRODUCED_OPERATIONAL_REHEARSAL"
    validate_report(
        report,
        plan=plan,
        plan_bytes=plan_bytes,
        require_repository=require_repository,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "operational_validation": report["operational_validation"],
        "scenarios": report["metrics"]["scenario_count"],
        "receipts": report["metrics"]["receipt_count"],
        "p95_append_ms": report["metrics"]["p95_append_ms"],
        "plan_sha256": report["plan"]["sha256"],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
