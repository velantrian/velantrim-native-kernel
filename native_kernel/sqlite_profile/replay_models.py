from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any

from native_kernel.semantic_core.canonical import canonical_json_bytes, domain_hash
from native_kernel.semantic_core.errors import ContractViolation, ReceiptOverclaim
from native_kernel.semantic_core.reducer import REDUCER_VERSION, SemanticState

_HASH_RE = re.compile(r"^nke1:[0-9a-f]{64}$")
_STATE_RE = re.compile(r"^nks0:[0-9a-f]{64}$")


class OperationType(str, Enum):
    REPLAY = "REPLAY"
    PROJECTION_REBUILD = "PROJECTION_REBUILD"


def _nonempty(name: str, value: object) -> str:
    if not isinstance(value, str) or not value:
        raise ContractViolation(f"{name} must be a non-empty string")
    return value


def _nonnegative(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ContractViolation(f"{name} must be a non-negative integer")
    return value


def _aware(name: str, value: object) -> datetime:
    if not isinstance(value, datetime) or value.tzinfo is None:
        raise ContractViolation(f"{name} must be timezone-aware")
    return value.astimezone(timezone.utc).replace(microsecond=0)


@dataclass(frozen=True, slots=True)
class ReplaySnapshot:
    instance_id: str
    state: SemanticState
    event_count: int
    first_global_seq: int
    last_global_seq: int
    last_event_hash: str | None
    reducer_version: str = REDUCER_VERSION
    target_schema_version: str = "1"

    def __post_init__(self) -> None:
        _nonempty("instance_id", self.instance_id)
        if not isinstance(self.state, SemanticState):
            raise ContractViolation("state must be SemanticState")
        _nonnegative("event_count", self.event_count)
        _nonnegative("first_global_seq", self.first_global_seq)
        _nonnegative("last_global_seq", self.last_global_seq)
        _nonempty("reducer_version", self.reducer_version)
        _nonempty("target_schema_version", self.target_schema_version)
        if self.event_count == 0:
            if self.first_global_seq != 0 or self.last_global_seq != 0 or self.last_event_hash is not None:
                raise ContractViolation("empty snapshot must use zero sequences and no hash")
        else:
            if self.first_global_seq != 1 or self.last_global_seq != self.event_count:
                raise ContractViolation("snapshot must cover contiguous history from sequence 1")
            if not isinstance(self.last_event_hash, str) or not _HASH_RE.fullmatch(self.last_event_hash):
                raise ContractViolation("non-empty snapshot requires an nke1 head hash")
        if self.state.last_global_seq != self.last_global_seq:
            raise ContractViolation("state head differs from snapshot head")


@dataclass(frozen=True, slots=True)
class OperationalReceipt:
    receipt_id: str
    operation_type: OperationType
    instance_id: str
    event_count: int
    first_global_seq: int
    last_global_seq: int
    state_digest: str
    known_limits: tuple[str, ...]
    created_at: datetime
    last_event_hash: str | None = None
    projection_name: str | None = None
    projection_generation: int | None = None
    reducer_version: str = REDUCER_VERSION
    target_schema_version: str = "1"
    claims_truth_established: bool = False
    claims_external_authenticity: bool = False
    claims_complete_integrity: bool = False
    claims_complete_erasure: bool = False
    contract: str = field(default="nk-operational-receipt/p3", init=False)

    def __post_init__(self) -> None:
        _nonempty("receipt_id", self.receipt_id)
        if not isinstance(self.operation_type, OperationType):
            raise ContractViolation("operation_type must be OperationType")
        _nonempty("instance_id", self.instance_id)
        _nonnegative("event_count", self.event_count)
        _nonnegative("first_global_seq", self.first_global_seq)
        _nonnegative("last_global_seq", self.last_global_seq)
        if not isinstance(self.state_digest, str) or not _STATE_RE.fullmatch(self.state_digest):
            raise ContractViolation("state_digest must use nks0")
        _nonempty("reducer_version", self.reducer_version)
        _nonempty("target_schema_version", self.target_schema_version)
        object.__setattr__(self, "created_at", _aware("created_at", self.created_at))
        if self.last_event_hash is not None and not _HASH_RE.fullmatch(self.last_event_hash):
            raise ContractViolation("last_event_hash must use nke1 when present")
        if not self.known_limits or any(not isinstance(item, str) or not item for item in self.known_limits):
            raise ReceiptOverclaim("operational Receipt must state proof limitations")
        if len(set(self.known_limits)) != len(self.known_limits):
            raise ContractViolation("known_limits must not contain duplicates")
        for name in (
            "claims_truth_established", "claims_external_authenticity",
            "claims_complete_integrity", "claims_complete_erasure",
        ):
            value = getattr(self, name)
            if not isinstance(value, bool):
                raise ContractViolation(f"{name} must be boolean")
            if value:
                raise ReceiptOverclaim(f"P5 operational Receipt cannot set {name}=true")
        if self.operation_type is OperationType.REPLAY:
            if self.projection_name is not None or self.projection_generation is not None:
                raise ContractViolation("REPLAY Receipt cannot declare a projection")
        else:
            _nonempty("projection_name", self.projection_name)
            if isinstance(self.projection_generation, bool) or not isinstance(self.projection_generation, int) or self.projection_generation < 1:
                raise ContractViolation("projection_generation must be positive")

    def as_contract_object(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "contract": self.contract,
            "receipt_id": self.receipt_id,
            "operation_type": self.operation_type.value,
            "instance_id": self.instance_id,
            "event_count": self.event_count,
            "first_global_seq": self.first_global_seq,
            "last_global_seq": self.last_global_seq,
            "state_digest": self.state_digest,
            "known_limits": list(self.known_limits),
            "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "reducer_version": self.reducer_version,
            "target_schema_version": self.target_schema_version,
            "claims_truth_established": False,
            "claims_external_authenticity": False,
            "claims_complete_integrity": False,
            "claims_complete_erasure": False,
        }
        if self.last_event_hash is not None:
            result["last_event_hash"] = self.last_event_hash
        if self.projection_name is not None:
            result["projection_name"] = self.projection_name
        if self.projection_generation is not None:
            result["projection_generation"] = self.projection_generation
        return result

    @property
    def canonical_bytes(self) -> bytes:
        return canonical_json_bytes(self.as_contract_object())

    @property
    def receipt_hash(self) -> str:
        return "nkr0:" + domain_hash("nk-p3-operational-receipt-v0", self.as_contract_object())


@dataclass(frozen=True, slots=True)
class StoredProjection:
    instance_id: str
    projection_name: str
    generation: int
    state: SemanticState
    state_digest: str
    last_global_seq: int
    last_event_hash: str | None
    receipt_id: str
    rebuilt_at: datetime
    state_canonical: bytes
    reducer_version: str = REDUCER_VERSION
    target_schema_version: str = "1"

    def __post_init__(self) -> None:
        _nonempty("instance_id", self.instance_id)
        _nonempty("projection_name", self.projection_name)
        if isinstance(self.generation, bool) or not isinstance(self.generation, int) or self.generation < 1:
            raise ContractViolation("generation must be positive")
        if not isinstance(self.state, SemanticState):
            raise ContractViolation("state must be SemanticState")
        if not isinstance(self.state_digest, str) or not _STATE_RE.fullmatch(self.state_digest):
            raise ContractViolation("state_digest must use nks0")
        _nonnegative("last_global_seq", self.last_global_seq)
        if self.last_event_hash is not None and not _HASH_RE.fullmatch(self.last_event_hash):
            raise ContractViolation("last_event_hash must use nke1 when present")
        _nonempty("receipt_id", self.receipt_id)
        object.__setattr__(self, "rebuilt_at", _aware("rebuilt_at", self.rebuilt_at))
        if not isinstance(self.state_canonical, bytes) or not self.state_canonical:
            raise ContractViolation("state_canonical must contain bytes")
        if self.state.last_global_seq != self.last_global_seq:
            raise ContractViolation("projection state head differs from stored head")


@dataclass(frozen=True, slots=True)
class ReplayResult:
    snapshot: ReplaySnapshot
    receipt: OperationalReceipt


@dataclass(frozen=True, slots=True)
class ProjectionRebuildResult:
    snapshot: ReplaySnapshot
    projection: StoredProjection
    receipt: OperationalReceipt
