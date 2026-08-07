from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Mapping

from native_kernel.semantic_core.canonical import freeze_json
from native_kernel.semantic_core.errors import ContractViolation
from native_kernel.semantic_core.models import EventType

_HASH_RE = re.compile(r"^(?:nke1|nkp1):[0-9a-f]{64}$")


def _nonempty(name: str, value: object) -> str:
    if not isinstance(value, str) or not value:
        raise ContractViolation(f"{name} must be a non-empty string")
    return value


def _positive_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ContractViolation(f"{name} must be a positive integer")
    return value


class AppendStatus(str, Enum):
    APPENDED = "APPENDED"
    RETURN_ORIGINAL_APPEND_RESULT = "RETURN_ORIGINAL_APPEND_RESULT"


@dataclass(frozen=True, slots=True)
class WriterToken:
    instance_id: str
    owner_id: str
    epoch: int
    expires_at: datetime

    def __post_init__(self) -> None:
        _nonempty("instance_id", self.instance_id)
        _nonempty("owner_id", self.owner_id)
        _positive_int("epoch", self.epoch)
        if not isinstance(self.expires_at, datetime) or self.expires_at.tzinfo is None:
            raise ContractViolation("expires_at must be timezone-aware")
        object.__setattr__(self, "expires_at", self.expires_at.astimezone(timezone.utc))


@dataclass(frozen=True, slots=True)
class StoredEvent:
    instance_id: str
    event_id: str
    command_id: str
    idempotency_key: str
    command_contract: str
    command_digest: str
    stream_id: str
    global_seq: int
    stream_seq: int
    actor_ref: str
    authority_ref: str
    recorded_at: datetime
    event_type: EventType
    schema_version: str
    payload: Mapping[str, Any]
    prev_global_hash: str
    payload_hash: str
    event_hash: str
    writer_epoch: int
    payload_canonical: bytes
    envelope_canonical: bytes

    def __post_init__(self) -> None:
        for name in (
            "instance_id", "event_id", "command_id", "idempotency_key",
            "command_contract", "command_digest", "stream_id", "actor_ref",
            "authority_ref", "schema_version",
        ):
            _nonempty(name, getattr(self, name))
        _positive_int("global_seq", self.global_seq)
        _positive_int("stream_seq", self.stream_seq)
        _positive_int("writer_epoch", self.writer_epoch)
        if not isinstance(self.event_type, EventType):
            raise ContractViolation("event_type must be EventType")
        if not isinstance(self.recorded_at, datetime) or self.recorded_at.tzinfo is None:
            raise ContractViolation("recorded_at must be timezone-aware")
        if self.prev_global_hash != "GENESIS" and not re.fullmatch(r"nke1:[0-9a-f]{64}", self.prev_global_hash):
            raise ContractViolation("prev_global_hash must be GENESIS or an nke1 hash")
        if not _HASH_RE.fullmatch(self.payload_hash) or not self.payload_hash.startswith("nkp1:"):
            raise ContractViolation("payload_hash must use nkp1")
        if not _HASH_RE.fullmatch(self.event_hash) or not self.event_hash.startswith("nke1:"):
            raise ContractViolation("event_hash must use nke1")
        if not isinstance(self.payload_canonical, bytes) or not self.payload_canonical:
            raise ContractViolation("payload_canonical must contain bytes")
        if not isinstance(self.envelope_canonical, bytes) or not self.envelope_canonical:
            raise ContractViolation("envelope_canonical must contain bytes")
        object.__setattr__(self, "recorded_at", self.recorded_at.astimezone(timezone.utc))
        object.__setattr__(self, "payload", freeze_json(self.payload))


@dataclass(frozen=True, slots=True)
class AppendResult:
    status: AppendStatus
    event: StoredEvent

    def __post_init__(self) -> None:
        if not isinstance(self.status, AppendStatus):
            raise ContractViolation("status must be AppendStatus")
        if not isinstance(self.event, StoredEvent):
            raise ContractViolation("event must be StoredEvent")
