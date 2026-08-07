from __future__ import annotations

import json
import os
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping

from native_kernel.semantic_core import (
    AdmissionReceipt,
    AuthorityDenied,
    AuthorityGrant,
    ClaimIdentity,
    Command,
    ContractViolation,
    DeletionReceipt,
    DeletionState,
    EventType,
    InvalidTransition,
    ReceiptOverclaim,
    SemanticContent,
    SemanticEvent,
    SemanticRole,
    SequenceViolation,
    StaticAuthorityPolicy,
    UnsupportedVersion,
    claim_id,
    content_hash,
    lineage_id,
    reduce_events,
    run_transitions,
)
from native_kernel.postgresql_profile.adapter import (
    EVIDENCE_LINEAGE,
    PROFILE_ID,
    PostgreSQLAppendStore,
)
from native_kernel.postgresql_profile.errors import (
    HistoryAdvanced,
    IdempotencyConflict,
    StaleWriterEpoch,
    StoredEventCorrupt,
    WriterLeaseBusy,
)
from native_kernel.postgresql_profile.models import AppendStatus
from native_kernel.postgresql_profile.replay import PostgreSQLReplayProjector

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "contracts" / "registry.json"
PROFILE_VERSION = "0.4-p4"
REPORT_VERSION = "nk-evidence-report/1"
REGISTRY_VERSION = "nk-contract-registry/1.1.0"


class ConformanceExecutionError(RuntimeError):
    pass


@dataclass(frozen=True, slots=True)
class ConformanceCheck:
    check_id: str
    status: str
    detail: str

    def as_report_object(self) -> dict[str, str]:
        return asdict(self)


class _CheckRecorder:
    def __init__(self) -> None:
        self.checks: list[ConformanceCheck] = []

    def run(self, check_id: str, detail: str, fn: Callable[[], None]) -> None:
        try:
            fn()
        except Exception as exc:
            self.checks.append(
                ConformanceCheck(check_id, "FAIL", f"{type(exc).__name__}: {exc}")
            )
            raise ConformanceExecutionError(f"{check_id} failed: {exc}") from exc
        self.checks.append(ConformanceCheck(check_id, "PASS", detail))


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ConformanceExecutionError(f"{path} must contain a JSON object")
    return value


def _command(
    key: str,
    *,
    event_type: EventType = EventType.ADMIT,
    payload: Mapping[str, Any] | None = None,
    stream_id: str = "stream:p4",
    authority_ref: str = "authority:p4",
) -> Command:
    return Command(
        command_id="command:" + uuid.uuid4().hex,
        idempotency_key=key,
        stream_id=stream_id,
        actor_ref="operator:p4",
        authority_ref=authority_ref,
        event_type=event_type,
        schema_version="1",
        payload=payload or {"claim_id": "claim:a"},
    )


def _policy() -> StaticAuthorityPolicy:
    return StaticAuthorityPolicy(
        (
            AuthorityGrant(
                authority_ref="authority:p4",
                actor_ref="operator:p4",
                policy_ref="policy:p4-admission",
                authority_kind="operator-delegation",
                allowed_event_types=tuple(EventType),
                stream_prefixes=("stream:",),
            ),
        )
    )


def _assert_raises(expected: type[BaseException], fn: Callable[[], Any]) -> None:
    try:
        fn()
    except expected:
        return
    raise AssertionError(f"expected {expected.__name__}")


def _registry_assertions(registry: Mapping[str, Any]) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    families = registry.get("families")
    if not isinstance(families, list):
        raise ConformanceExecutionError("registry families must be a list")
    for family in families:
        if not isinstance(family, dict):
            raise ConformanceExecutionError("registry family must be an object")
        family_id = family.get("family_id")
        contract_version = family.get("contract_version")
        decision_status = family.get("decision_status")
        assertions = family.get("assertions")
        if not all(
            isinstance(item, str) and item
            for item in (family_id, contract_version, decision_status)
        ):
            raise ConformanceExecutionError("registry family metadata is invalid")
        if not isinstance(assertions, list):
            raise ConformanceExecutionError(f"{family_id}: assertions must be a list")
        for assertion in assertions:
            if not isinstance(assertion, dict):
                raise ConformanceExecutionError(f"{family_id}: assertion must be an object")
            assertion_id = assertion.get("assertion_id")
            if not isinstance(assertion_id, str) or not assertion_id:
                raise ConformanceExecutionError(f"{family_id}: assertion_id is invalid")
            if assertion_id in result:
                raise ConformanceExecutionError(f"duplicate assertion {assertion_id}")
            result[assertion_id] = {
                "family_id": family_id,
                "contract_version": contract_version,
                "decision_status": decision_status,
            }
    return result


def _run_semantic_checks(pack: Mapping[str, Any], recorder: _CheckRecorder) -> None:
    golden = pack["identity_golden"]["vectors"]
    invalid = pack["identity_invalid"]["vectors"]

    def registry_check() -> None:
        registry = _load_json(REGISTRY)
        if registry.get("registry_version") != REGISTRY_VERSION:
            raise AssertionError("unexpected registry version")
        assertions = _registry_assertions(registry)
        if len(assertions) != 72:
            raise AssertionError(f"expected 72 assertions, found {len(assertions)}")
        proposed = {
            assertion_id
            for assertion_id, metadata in assertions.items()
            if metadata["decision_status"] == "PROPOSED"
        }
        if proposed != {f"NK-EPI-{index:03d}" for index in range(1, 9)}:
            raise AssertionError("proposed assertion set drifted")

    recorder.run(
        "p4.registry.contracts",
        "registry 1.1.0 has 72 unique assertions and only NK-EPI-001..008 remain proposed",
        registry_check,
    )

    def golden_check() -> None:
        for vector in golden:
            if content_hash(vector["content"]) != vector["expected"]["content_hash"]:
                raise AssertionError(f"{vector['vector_id']}: content hash mismatch")
            if claim_id(vector["claim_identity"]) != vector["expected"]["claim_id"]:
                raise AssertionError(f"{vector['vector_id']}: claim id mismatch")
            if lineage_id(vector["lineage_seed"]) != vector["expected"]["lineage_id"]:
                raise AssertionError(f"{vector['vector_id']}: lineage id mismatch")

    recorder.run(
        "p4.identity.golden",
        f"{len(golden)} accepted identity golden vectors matched exact v1 identifiers",
        golden_check,
    )

    def invalid_check() -> None:
        for vector in invalid:
            _assert_raises(
                ContractViolation,
                lambda value=vector["input"]: content_hash(value),
            )

    recorder.run(
        "p4.identity.invalid",
        f"{len(invalid)} invalid canonical identity vectors were rejected",
        invalid_check,
    )

    def semantic_roles_check() -> None:
        objects = [
            SemanticContent(
                role=role,
                scope={"domain": "p4", "language": "en"},
                fields={"value": role.value, "method_ref": "method:p4"},
            )
            for role in SemanticRole
        ]
        rendered = [item.as_contract_object() for item in objects]
        if {item["role"] for item in rendered} != {
            role.value for role in SemanticRole
        }:
            raise AssertionError("semantic roles collapsed")
        if any(item["scope"]["domain"] != "p4" for item in rendered):
            raise AssertionError("scope was not preserved")
        observation = next(
            item for item in objects if item.role is SemanticRole.OBSERVATION
        )
        identity = ClaimIdentity(
            content_hash=observation.content_hash,
            source_ref="source:p4",
            source_record_id="record:p4",
            asserted_at="2026-08-07T00:00:00Z",
        )
        if observation.content_hash == identity.claim_id:
            raise AssertionError("semantic content and source-bound Claim identity collapsed")
        if (
            next(
                item for item in objects if item.role is SemanticRole.UNKNOWN
            ).as_contract_object()["role"]
            == "false"
        ):
            raise AssertionError("unknown collapsed to false")

    recorder.run(
        "p4.semantic.roles",
        "seven semantic roles, explicit scope and source-bound Claim identity remained distinguishable",
        semantic_roles_check,
    )

    def authority_check() -> None:
        policy = _policy()
        allowed = policy.require(_command("idem:p4:authority"))
        if not (
            allowed.allowed
            and allowed.policy_ref == "policy:p4-admission"
            and allowed.authority_kind == "operator-delegation"
            and allowed.scope == "stream:p4"
        ):
            raise AssertionError("allowed authority decision lost inspectable fields")
        _assert_raises(
            AuthorityDenied,
            lambda: policy.require(
                _command("idem:p4:deny", authority_ref="authority:missing")
            ),
        )

    recorder.run(
        "p4.authority.policy",
        "explicit scoped grant allowed one command and deny-by-default rejected unknown authority",
        authority_check,
    )

    def receipt_check() -> None:
        decision = _policy().require(_command("idem:p4:receipt"))
        receipt = AdmissionReceipt(
            command_id="command:p4",
            decision=decision,
            known_limits=("authority decision is not truth evidence",),
        )
        if receipt.as_contract_object()["claims_truth_established"] is not False:
            raise AssertionError("admission Receipt truth boundary changed")
        _assert_raises(
            ReceiptOverclaim,
            lambda: AdmissionReceipt(
                command_id="command:p4",
                decision=decision,
                known_limits=("invalid overclaim",),
                claims_truth_established=True,
            ),
        )
        deletion = DeletionReceipt(
            request_id="request:p4",
            authority_ref="authority:privacy",
            policy_ref="policy:erase",
            final_state=DeletionState.PARTIALLY_ERASED,
            verified_locations=("projection",),
            unverified_or_pending_locations=("backup",),
            known_limits=("physical deletion is not established",),
        )
        if deletion.as_contract_object()["claims_complete_global_erasure"] is not False:
            raise AssertionError("deletion Receipt overclaimed")
        _assert_raises(
            ReceiptOverclaim,
            lambda: DeletionReceipt(
                request_id="request:p4",
                authority_ref="authority:privacy",
                policy_ref="policy:erase",
                final_state=DeletionState.PHYSICALLY_ERASED,
                verified_locations=("primary",),
                unverified_or_pending_locations=("backup",),
                known_limits=("invalid overclaim",),
                claims_complete_global_erasure=True,
            ),
        )

    recorder.run(
        "p4.receipts.boundaries",
        "admission and deletion Receipts preserved truth and global-erasure non-claims",
        receipt_check,
    )

    def reducer_check() -> None:
        events = [
            SemanticEvent(
                1,
                "stream:p4",
                1,
                EventType.ADMIT,
                "1",
                {"claim_id": "claim:a"},
            ),
            SemanticEvent(
                2,
                "stream:p4",
                2,
                EventType.LINK,
                "1",
                {
                    "from_claim_id": "claim:a",
                    "relation": "SUPPORTS",
                    "to_claim_id": "claim:b",
                },
            ),
            SemanticEvent(
                3,
                "stream:p4",
                3,
                EventType.UTILIZED,
                "1",
                {"claim_id": "claim:a"},
            ),
            SemanticEvent(
                4,
                "stream:p4",
                4,
                EventType.SUPERSEDED,
                "1",
                {"claim_id": "claim:a", "by_claim_id": "claim:b"},
            ),
            SemanticEvent(
                5,
                "stream:p4",
                5,
                EventType.ERASED,
                "1",
                {"claim_id": "claim:a"},
            ),
        ]
        left = reduce_events(events)
        right = reduce_events(events)
        if left != right or left.digest != right.digest or left.last_global_seq != 5:
            raise AssertionError("deterministic reduction mismatch")

    recorder.run(
        "p4.reducer.determinism",
        "P1 reducer produced identical state and digest for the same ordered Event sequence",
        reducer_check,
    )

    def reducer_failures_check() -> None:
        _assert_raises(
            SequenceViolation,
            lambda: reduce_events(
                [
                    SemanticEvent(
                        2,
                        "stream:p4",
                        1,
                        EventType.ADMIT,
                        "1",
                        {"claim_id": "claim:a"},
                    )
                ]
            ),
        )
        _assert_raises(
            UnsupportedVersion,
            lambda: reduce_events(
                [
                    SemanticEvent(
                        1,
                        "stream:p4",
                        1,
                        EventType.ADMIT,
                        "2",
                        {"claim_id": "claim:a"},
                    )
                ]
            ),
        )

    recorder.run(
        "p4.reducer.failures",
        "non-contiguous sequence and unsupported Event schema failed explicitly",
        reducer_failures_check,
    )

    def deletion_check() -> None:
        for scenario in pack["deletion_scenarios"]["scenarios"]:
            final = run_transitions(
                DeletionState(scenario["initial_state"]),
                [DeletionState(item["to"]) for item in scenario["transitions"]],
            )
            if final.value != scenario["expected_final_state"]:
                raise AssertionError(f"{scenario['scenario_id']}: final state mismatch")
        _assert_raises(
            InvalidTransition,
            lambda: run_transitions(
                DeletionState.ACTIVE,
                [DeletionState.PHYSICALLY_ERASED],
            ),
        )

    recorder.run(
        "p4.deletion.semantic",
        "accepted deletion/restriction fixture paths completed and a forbidden jump failed",
        deletion_check,
    )


def _run_postgresql_checks(dsn: str, recorder: _CheckRecorder) -> None:
    policy = _policy()
    store = PostgreSQLAppendStore.from_dsn(dsn, policy)
    projector = PostgreSQLReplayProjector.from_dsn(dsn)

    def migrations_check() -> None:
        store.migrate()
        if store.migrate() != ():
            raise AssertionError("repeated migration pass was not empty")

    recorder.run(
        "p4.postgresql.migrations",
        "numbered PostgreSQL migrations applied and a repeated migration pass was empty",
        migrations_check,
    )

    instance = "instance:" + uuid.uuid4().hex
    store.register_instance(instance)
    primary = store.acquire_writer_lease(
        instance,
        "writer:p4-primary",
        ttl_seconds=120,
    )

    def writer_fencing_check() -> None:
        _assert_raises(
            WriterLeaseBusy,
            lambda: store.acquire_writer_lease(
                instance,
                "writer:p4-other",
                ttl_seconds=120,
            ),
        )
        store.release_writer_lease(primary)
        replacement = store.acquire_writer_lease(
            instance,
            "writer:p4-other",
            ttl_seconds=120,
        )
        if replacement.epoch <= primary.epoch:
            raise AssertionError("writer epoch did not advance")
        _assert_raises(
            StaleWriterEpoch,
            lambda: store.append(_command("idem:p4:stale"), primary),
        )

    recorder.run(
        "p4.postgresql.writer-fencing",
        "busy lease, epoch advance and stale-writer rejection were reproduced",
        writer_fencing_check,
    )

    instance = "instance:" + uuid.uuid4().hex
    store.register_instance(instance)
    token = store.acquire_writer_lease(instance, "writer:p4", ttl_seconds=120)

    def append_idempotency_check() -> None:
        command = _command("idem:p4:append")
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
                _command(
                    "idem:p4:append",
                    payload={"claim_id": "claim:different"},
                ),
                token,
            ),
        )
        if store.count_events(instance) != 1:
            raise AssertionError("idempotency conflict changed Event count")

    recorder.run(
        "p4.postgresql.append-idempotency",
        "append, same-digest retry and conflicting idempotency-key reuse matched the P2 contract",
        append_idempotency_check,
    )

    def rollback_check() -> None:
        rollback_instance = "instance:" + uuid.uuid4().hex
        store.register_instance(rollback_instance)
        rollback_token = store.acquire_writer_lease(
            rollback_instance,
            "writer:p4-rollback",
            ttl_seconds=120,
        )

        def fail_after_insert(_: object) -> None:
            raise RuntimeError("P4 fault injection")

        failing = PostgreSQLAppendStore.from_dsn(
            dsn,
            policy,
            fault_hook=fail_after_insert,
        )
        command = _command("idem:p4:rollback")
        _assert_raises(RuntimeError, lambda: failing.append(command, rollback_token))
        if store.count_events(rollback_instance) != 0:
            raise AssertionError("failed append persisted an Event")
        result = store.append(command, rollback_token)
        if (result.event.global_seq, result.event.stream_seq) != (1, 1):
            raise AssertionError("rollback left a sequence gap")

    recorder.run(
        "p4.postgresql.rollback-ordering",
        "injected append failure rolled back and the next Event retained contiguous global/stream sequence",
        rollback_check,
    )

    def replay_projection_check() -> None:
        replay_instance = "instance:" + uuid.uuid4().hex
        store.register_instance(replay_instance)
        replay_token = store.acquire_writer_lease(
            replay_instance,
            "writer:p4-replay",
            ttl_seconds=120,
        )
        stored = [
            store.append(
                _command(
                    "idem:p4:replay:1",
                    payload={"claim_id": "claim:a"},
                    stream_id="stream:p4-replay",
                ),
                replay_token,
            ).event,
            store.append(
                _command(
                    "idem:p4:replay:2",
                    event_type=EventType.LINK,
                    payload={
                        "from_claim_id": "claim:a",
                        "relation": "SUPPORTS",
                        "to_claim_id": "claim:b",
                    },
                    stream_id="stream:p4-replay",
                ),
                replay_token,
            ).event,
            store.append(
                _command(
                    "idem:p4:replay:3",
                    event_type=EventType.UTILIZED,
                    payload={"claim_id": "claim:a"},
                    stream_id="stream:p4-replay",
                ),
                replay_token,
            ).event,
        ]
        direct = reduce_events(
            SemanticEvent(
                event.global_seq,
                event.stream_id,
                event.stream_seq,
                event.event_type,
                event.schema_version,
                event.payload,
            )
            for event in stored
        )
        replayed = projector.replay(replay_instance)
        if replayed.snapshot.state.digest != direct.digest:
            raise AssertionError("persisted replay differs from direct reduction")
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
            raise AssertionError("projection destroy did not remove a row")
        second = projector.rebuild_projection(replay_instance)
        if second.projection.state_digest != first.projection.state_digest:
            raise AssertionError("projection rebuild changed deterministic state")
        if second.projection.generation != first.projection.generation + 1:
            raise AssertionError("projection generation was not monotonic")

    recorder.run(
        "p4.postgresql.replay-projection",
        "persisted replay matched direct reduction; projection destroy/rebuild and bounded Receipts were reproduced",
        replay_projection_check,
    )

    def stale_head_check() -> None:
        stale_instance = "instance:" + uuid.uuid4().hex
        store.register_instance(stale_instance)
        stale_token = store.acquire_writer_lease(
            stale_instance,
            "writer:p4-stale",
            ttl_seconds=120,
        )
        store.append(_command("idem:p4:stale:before"), stale_token)

        def advance(_: object) -> None:
            store.append(_command("idem:p4:stale:after"), stale_token)

        stale = PostgreSQLReplayProjector.from_dsn(dsn, snapshot_hook=advance)
        _assert_raises(
            HistoryAdvanced,
            lambda: stale.rebuild_projection(stale_instance),
        )
        if projector.count_receipts(stale_instance) != 0:
            raise AssertionError("stale rebuild committed a Receipt")

    recorder.run(
        "p4.postgresql.stale-head",
        "history advancement between replay and publication rejected an obsolete projection",
        stale_head_check,
    )

    def corruption_check() -> None:
        corrupt_instance = "instance:" + uuid.uuid4().hex
        store.register_instance(corrupt_instance)
        corrupt_token = store.acquire_writer_lease(
            corrupt_instance,
            "writer:p4-corrupt",
            ttl_seconds=120,
        )
        event = store.append(_command("idem:p4:corrupt"), corrupt_token).event
        import psycopg

        with psycopg.connect(dsn) as connection:
            with connection.transaction(), connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE native_kernel.events SET payload_canonical = %s "
                    "WHERE instance_id = %s AND global_seq = %s",
                    (b"{}", corrupt_instance, event.global_seq),
                )
        _assert_raises(
            StoredEventCorrupt,
            lambda: projector.replay(corrupt_instance, persist_receipt=False),
        )

    recorder.run(
        "p4.postgresql.corruption",
        "stored canonical payload corruption was detected before replay evidence was emitted",
        corruption_check,
    )


SUPPORTED: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {
    "NK-SEM-001": (("p4.semantic.roles",), ("Source-bound Claim identity is tested for the P1 contract only.",)),
    "NK-SEM-003": (("p4.semantic.roles",), ("No automated scientific truth evaluation is claimed.",)),
    "NK-SEM-004": (("p4.receipts.boundaries",), ("Relevance ranking is outside this profile.",)),
    "NK-SEM-005": (("p4.semantic.roles",), ("Unknown is represented; broader conflict semantics remain incomplete.",)),
    "NK-SEM-006": (("p4.authority.policy",), ("Authority is a deterministic local policy, not operational IAM.",)),
    "NK-SEM-007": (("p4.semantic.roles",), ("Scope enforcement is limited to current semantic objects.",)),
    "NK-ID-001": (("p4.identity.golden",), ("Backend row IDs are outside semantic identity.",)),
    "NK-ID-002": (("p4.identity.golden", "p4.registry.contracts"), ("Only accepted v1 identity contracts are covered.",)),
    "NK-ID-003": (("p4.identity.golden",), ("Canonical determinism is version-bound.",)),
    "NK-ID-004": (("p4.identity.invalid",), ("Canonical decimal semantics beyond strings are not added.",)),
    "NK-ID-005": (("p4.identity.golden",), ("Only declared v1 SHA-256 domains are covered.",)),
    "NK-ID-009": (("p4.identity.golden", "p4.identity.invalid"), ("Applies to the v1 canonical JSON subset.",)),
    "NK-ID-010": (("p4.identity.invalid",), ("Applies only to identity-bearing canonical objects.",)),
    "NK-ID-011": (("p4.identity.golden", "p4.semantic.roles"), ("No identity alias migration is implemented.",)),
    "NK-ID-012": (("p4.identity.golden",), ("Prefix support is limited to nkh1/nkc1/nkl1.",)),
    "NK-EVT-003": (("p4.postgresql.append-idempotency",), ("Command/Event separation is tested in the PostgreSQL profile.",)),
    "NK-EVT-004": (("p4.postgresql.append-idempotency",), ("Idempotency scope is instance + command contract + key.",)),
    "NK-EVT-006": (("p4.postgresql.writer-fencing", "p4.postgresql.rollback-ordering"), ("Single-writer PostgreSQL ordering only.",)),
    "NK-EVT-007": (("p4.postgresql.replay-projection",), ("Only reducer/schema version 1 paths are reproduced.",)),
    "NK-EVT-008": (("p4.postgresql.rollback-ordering", "p4.postgresql.replay-projection"), ("Projection operations remain bounded to the selected instance.",)),
    "NK-EVT-011": (("p4.postgresql.writer-fencing", "p4.postgresql.rollback-ordering"), ("No multi-writer consensus is claimed.",)),
    "NK-EVT-012": (("p4.postgresql.append-idempotency",), ("Conflict behavior is tested for the current command contract.",)),
    "NK-EVT-013": (("p4.postgresql.rollback-ordering", "p4.postgresql.replay-projection"), ("No cross-database transaction is claimed.",)),
    "NK-EVT-014": (("p4.postgresql.corruption", "p4.receipts.boundaries"), ("Hash chains are not signatures or external authenticity.",)),
    "NK-AUT-001": (("p4.authority.policy",), ("Admission is tested through the P1 authority port.",)),
    "NK-AUT-002": (("p4.authority.policy",), ("No retrieval/ranking subsystem is wired.",)),
    "NK-AUT-003": (("p4.authority.policy",), ("Operational identity verification is absent.",)),
    "NK-AUT-005": (("p4.receipts.boundaries",), ("Operator authority remains distinct from empirical evidence.",)),
    "NK-AUT-007": (("p4.deletion.semantic", "p4.receipts.boundaries"), ("Deletion execution is not implemented.",)),
    "NK-AUT-008": (("p4.receipts.boundaries",), ("Admission Receipt is P1-local and non-durable.",)),
    "NK-AUT-009": (("p4.deletion.semantic", "p4.receipts.boundaries"), ("Only semantic distinction is supported.",)),
    "NK-AUT-012": (("p4.receipts.boundaries",), ("Verified locations are caller-provided evidence labels.",)),
    "NK-CFL-006": (("p4.semantic.roles",), ("Explicit Unknown exists; full conflict representation is absent.",)),
    "NK-EQV-001": (("p4.registry.contracts", "p4.report.traceability"), ("Contract versions are resolved through registry 1.1.0.",)),
    "NK-EQV-004": (("p4.report.traceability",), ("Unsupported assertions are explicit in this report.",)),
    "NK-EQV-005": (("p4.registry.contracts", "p4.report.traceability"), ("Evidence is exact to the declared profile and run metadata.",)),
    "NK-EQV-006": (("p4.identity.golden", "p4.deletion.semantic", "p4.postgresql.replay-projection"), ("Evidence classes remain profile-local.",)),
    "NK-EQV-007": (("p4.report.traceability",), ("C3 is explicitly not established.",)),
    "NK-EQV-008": (("p4.receipts.boundaries", "p4.postgresql.replay-projection"), ("Receipts remain bounded to declared operations.",)),
    "NK-EQV-009": (("p4.registry.contracts", "p4.report.traceability"), ("Fixture integrity remains distinct from runtime conformance.",)),
    "NK-EQV-010": (("p4.report.traceability",), ("Adapter failures abort and unsupported results remain emitted.",)),
}

PARTIAL: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {
    "NK-SEM-002": (("p4.semantic.roles",), ("Method/provenance fields are preserved when supplied but are not role-specific required fields.",)),
    "NK-ID-006": (("p4.identity.golden", "p4.postgresql.append-idempotency"), ("Cryptographic collision injection and alias adjudication are not implemented.",)),
    "NK-ID-008": (("p4.identity.golden", "p4.identity.invalid"), ("One profile evaluates the vectors; an independent second profile is absent.",)),
    "NK-EVT-001": (("p4.semantic.roles", "p4.postgresql.replay-projection"), ("No separate represented-world occurrence object is implemented.",)),
    "NK-EVT-002": (("p4.semantic.roles", "p4.postgresql.append-idempotency"), ("asserted_at and recorded_at are distinct; observation/valid time are not fully modeled.",)),
    "NK-EVT-005": (("p4.postgresql.append-idempotency",), ("Commit-before-return is reproduced, but a durability grade is not encoded in AppendResult.",)),
    "NK-EVT-009": (("p4.reducer.determinism", "p4.deletion.semantic"), ("Supersession and logical erase are explicit; correction and physical erasure execution are incomplete.",)),
    "NK-EVT-010": (("p4.postgresql.corruption", "p4.receipts.boundaries"), ("Tested tamper signals are bounded; forks, privileged rewrites and external authentication remain outside proof.",)),
    "NK-AUT-004": (("p4.authority.policy",), ("Explicit grant scope is enforced; delegation chains and revocation are absent.",)),
    "NK-AUT-010": (("p4.deletion.semantic",), ("Retry/partial states are explicit; no durable deletion worker or idempotent location executor exists.",)),
    "NK-CFL-003": (("p4.reducer.determinism", "p4.receipts.boundaries"), ("Write order is not claimed as truth, but a full conflict subsystem is absent.",)),
    "NK-EQV-002": (("p4.report.traceability",), ("Equivalence classes are declared by the contract model; no second-profile comparison is executed.",)),
    "NK-EQV-003": (("p4.report.traceability",), ("Current profile limitations are explicit; cross-profile allowed/forbidden differences await P5.",)),
}

EXPLICIT_UNSUPPORTED: dict[str, tuple[str, ...]] = {
    "NK-SEM-008": ("No independent profile translation exists before P5.",),
    "NK-ID-007": ("Identity migration and aliasing are not implemented.",),
    "NK-AUT-006": ("No cross-project runtime authority adapter is wired.",),
    "NK-AUT-011": ("No restore visibility path exists.",),
    "NK-CFL-001": ("Candidate conflict representation is not implemented.",),
    "NK-CFL-002": ("Conflict detection/resolution separation is not implemented.",),
    "NK-CFL-004": ("Multiple incompatible Claims are not represented by a dedicated conflict model.",),
    "NK-CFL-005": ("Conflict mismatch dimensions are not modeled.",),
    "NK-CFL-007": ("Conflict resolution history/authority/policy is not implemented.",),
    "NK-CFL-008": ("No profile-translation conflict preservation exists before P5.",),
}


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
                "Registry decision status is PROPOSED; P4 cannot promote this assertion.",
                "ADR-0008 and NK-EPI require a separate acceptance decision.",
            )
            status = "UNSUPPORTED"
        else:
            evidence = ()
            limitations = (
                "No executable P4 support mapping exists for this accepted assertion.",
            )
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
        raise ConformanceExecutionError(
            f"expected 72 assertion results, found {len(results)}"
        )
    return results


def _validate_traceability(
    assertion_results: Iterable[Mapping[str, Any]],
    checks: Iterable[ConformanceCheck],
) -> None:
    check_values = tuple(checks)
    check_map = {check.check_id: check for check in check_values}
    if len(check_map) != len(check_values):
        raise ConformanceExecutionError("duplicate check IDs")
    for result in assertion_results:
        status = result["status"]
        evidence = result.get("evidence", [])
        limitations = result.get("limitations", [])
        if status in {"SUPPORTED", "PARTIAL"} and not evidence:
            raise ConformanceExecutionError(
                f"{result['assertion_id']}: {status} requires evidence"
            )
        if not limitations:
            raise ConformanceExecutionError(
                f"{result['assertion_id']}: limitations are required"
            )
        for check_id in evidence:
            check = check_map.get(check_id)
            if check is None:
                raise ConformanceExecutionError(
                    f"{result['assertion_id']}: unknown evidence check {check_id}"
                )
            if check.status != "PASS":
                raise ConformanceExecutionError(
                    f"{result['assertion_id']}: evidence check {check_id} did not pass"
                )


def build_report(
    fixture_pack_path: Path,
    *,
    dsn: str,
    conformance_level: str = "C1",
    evidence_level: str = "LOCALLY_TESTED",
    evidence_commit: str = "LOCAL",
    evidence_run_id: str = "LOCAL",
    python_version: str = "LOCAL",
    postgresql_version: str = "LOCAL",
) -> dict[str, Any]:
    if conformance_level not in {"C1", "C2"}:
        raise ConformanceExecutionError("P4 adapter supports only C1 or C2")
    if evidence_level not in {"LOCALLY_TESTED", "REPOSITORY_REPRODUCED"}:
        raise ConformanceExecutionError("invalid P4 evidence level")
    if conformance_level == "C2" and evidence_level != "REPOSITORY_REPRODUCED":
        raise ConformanceExecutionError(
            "C2 requires REPOSITORY_REPRODUCED evidence"
        )
    if not dsn:
        raise ConformanceExecutionError("dsn must be non-empty")
    pack = _load_json(fixture_pack_path)
    if pack.get("fixture_pack_version") != "nk-conformance-fixtures/1.0.0":
        raise ConformanceExecutionError("unsupported fixture pack version")
    registry = _load_json(REGISTRY)
    recorder = _CheckRecorder()
    _run_semantic_checks(pack, recorder)
    _run_postgresql_checks(dsn, recorder)

    recorder.run(
        "p4.environment.metadata",
        (
            f"profile={PROFILE_ID}@{PROFILE_VERSION}; commit={evidence_commit}; "
            f"run={evidence_run_id}; python={python_version}; "
            f"postgresql={postgresql_version}"
        ),
        lambda: None,
    )
    provisional = _assertion_results(registry)
    traceability_check = ConformanceCheck(
        "p4.report.traceability",
        "PASS",
        "all 72 assertions were emitted once with evidence/limitations and proposed NK-EPI remained unsupported",
    )
    _validate_traceability(provisional, [*recorder.checks, traceability_check])
    recorder.checks.append(traceability_check)
    results = _assertion_results(registry)
    _validate_traceability(results, recorder.checks)

    counts = {
        status: sum(1 for item in results if item["status"] == status)
        for status in ("SUPPORTED", "PARTIAL", "UNSUPPORTED", "FAILED")
    }
    expected_counts = {
        "SUPPORTED": 41,
        "PARTIAL": 13,
        "UNSUPPORTED": 18,
        "FAILED": 0,
    }
    if counts != expected_counts:
        raise ConformanceExecutionError(f"unexpected assertion summary {counts}")

    return {
        "report_version": REPORT_VERSION,
        "profile_id": PROFILE_ID,
        "support_state": "PARTIAL",
        "kernel_runtime_conformance": conformance_level,
        "evidence_level": evidence_level,
        "assertion_results": results,
        "checks": [check.as_report_object() for check in recorder.checks],
        "limitations": [
            "C1/C2 applies only to assertion results marked SUPPORTED at this exact evidence scope.",
            "PARTIAL and UNSUPPORTED assertions remain outside the supported conformance set.",
            "C2 is repository reproduction for one PostgreSQL profile, not C3 cross-profile equivalence.",
            "No truth, external authenticity, physical deletion, C4/C5 or production claim is made.",
            f"Evidence lineage is {EVIDENCE_LINEAGE}; it is independent from v0.1.2.1 source recovery.",
        ],
    }


def report_from_environment(fixture_pack_path: Path) -> dict[str, Any]:
    return build_report(
        fixture_pack_path,
        dsn=os.environ.get("NK_TEST_POSTGRES_DSN", ""),
        conformance_level=os.environ.get("NK_CONFORMANCE_LEVEL", "C1"),
        evidence_level=os.environ.get("NK_EVIDENCE_LEVEL", "LOCALLY_TESTED"),
        evidence_commit=os.environ.get("NK_EVIDENCE_COMMIT", "LOCAL"),
        evidence_run_id=os.environ.get("NK_EVIDENCE_RUN_ID", "LOCAL"),
        python_version=os.environ.get("NK_PYTHON_VERSION", "LOCAL"),
        postgresql_version=os.environ.get("NK_POSTGRESQL_VERSION", "LOCAL"),
    )


def render_report(report: Mapping[str, Any]) -> str:
    return json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
