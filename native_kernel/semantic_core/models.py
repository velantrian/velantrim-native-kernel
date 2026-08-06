from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping

from .canonical import (
    claim_id as derive_claim_id,
    command_digest as derive_command_digest,
    content_hash as derive_content_hash,
    freeze_json,
    lineage_id as derive_lineage_id,
    thaw_json,
)
from .errors import ContractViolation

_UTC_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


class SemanticRole(str, Enum):
    PROPOSITION = "proposition"
    OBSERVATION = "observation"
    MEASUREMENT = "measurement"
    INTERPRETATION = "interpretation"
    HYPOTHESIS = "hypothesis"
    QUESTION = "question"
    UNKNOWN = "unknown"


class EventType(str, Enum):
    ADMIT = "ADMIT"
    LINK = "LINK"
    UTILIZED = "UTILIZED"
    SUPERSEDED = "SUPERSEDED"
    ERASED = "ERASED"


def _require_nonempty(name: str, value: str) -> None:
    if not isinstance(value, str) or not value:
        raise ContractViolation(f"{name} must be a non-empty string")


@dataclass(frozen=True, slots=True)
class SemanticContent:
    role: SemanticRole
    scope: Mapping[str, Any]
    fields: Mapping[str, Any]
    contract: str = field(default="nk-semantic-content/1", init=False)

    def __post_init__(self) -> None:
        frozen_scope = freeze_json(self.scope)
        frozen_fields = freeze_json(self.fields)
        if "domain" not in frozen_scope or not isinstance(frozen_scope["domain"], str):
            raise ContractViolation("semantic content scope must declare a string domain")
        reserved = {"contract", "role", "scope"}
        overlap = reserved.intersection(frozen_fields)
        if overlap:
            raise ContractViolation(f"semantic content fields use reserved keys: {sorted(overlap)}")
        object.__setattr__(self, "scope", frozen_scope)
        object.__setattr__(self, "fields", frozen_fields)

    def as_contract_object(self) -> dict[str, Any]:
        return {
            "contract": self.contract,
            "role": self.role.value,
            "scope": thaw_json(self.scope),
            **thaw_json(self.fields),
        }

    @property
    def content_hash(self) -> str:
        return derive_content_hash(self.as_contract_object())


@dataclass(frozen=True, slots=True)
class ClaimIdentity:
    content_hash: str
    source_ref: str
    source_record_id: str
    asserted_at: str
    contract: str = field(default="nk-claim-identity/1", init=False)

    def __post_init__(self) -> None:
        if not re.fullmatch(r"nkh1:[0-9a-f]{64}", self.content_hash):
            raise ContractViolation("content_hash must use the nkh1 SHA-256 form")
        _require_nonempty("source_ref", self.source_ref)
        _require_nonempty("source_record_id", self.source_record_id)
        if not _UTC_RE.fullmatch(self.asserted_at):
            raise ContractViolation("asserted_at must use exact UTC second form YYYY-MM-DDTHH:MM:SSZ")

    def as_contract_object(self) -> dict[str, Any]:
        return {
            "contract": self.contract,
            "content_hash": self.content_hash,
            "source_ref": self.source_ref,
            "source_record_id": self.source_record_id,
            "asserted_at": self.asserted_at,
        }

    @property
    def claim_id(self) -> str:
        return derive_claim_id(self.as_contract_object())


@dataclass(frozen=True, slots=True)
class LineageSeed:
    namespace: str
    seed: str
    contract: str = field(default="nk-lineage/1", init=False)

    def __post_init__(self) -> None:
        _require_nonempty("namespace", self.namespace)
        _require_nonempty("seed", self.seed)

    def as_contract_object(self) -> dict[str, str]:
        return {"contract": self.contract, "namespace": self.namespace, "seed": self.seed}

    @property
    def lineage_id(self) -> str:
        return derive_lineage_id(self.as_contract_object())


@dataclass(frozen=True, slots=True)
class Command:
    command_id: str
    idempotency_key: str
    stream_id: str
    actor_ref: str
    authority_ref: str
    event_type: EventType
    schema_version: str
    payload: Mapping[str, Any]
    contract: str = field(default="nk-command/1", init=False)

    def __post_init__(self) -> None:
        for name in (
            "command_id",
            "idempotency_key",
            "stream_id",
            "actor_ref",
            "authority_ref",
            "schema_version",
        ):
            _require_nonempty(name, getattr(self, name))
        object.__setattr__(self, "payload", freeze_json(self.payload))

    def as_contract_object(self) -> dict[str, Any]:
        return {
            "contract": self.contract,
            "command_id": self.command_id,
            "idempotency_key": self.idempotency_key,
            "stream_id": self.stream_id,
            "actor_ref": self.actor_ref,
            "authority_ref": self.authority_ref,
            "event_type": self.event_type.value,
            "schema_version": self.schema_version,
            "payload": thaw_json(self.payload),
        }

    @property
    def digest(self) -> str:
        return derive_command_digest(self.as_contract_object())


@dataclass(frozen=True, slots=True)
class SemanticEvent:
    global_seq: int
    stream_id: str
    stream_seq: int
    event_type: EventType
    schema_version: str
    payload: Mapping[str, Any]

    def __post_init__(self) -> None:
        if self.global_seq < 1 or self.stream_seq < 1:
            raise ContractViolation("event sequences must be positive integers")
        _require_nonempty("stream_id", self.stream_id)
        _require_nonempty("schema_version", self.schema_version)
        object.__setattr__(self, "payload", freeze_json(self.payload))

    def as_contract_object(self) -> dict[str, Any]:
        return {
            "global_seq": self.global_seq,
            "stream_id": self.stream_id,
            "stream_seq": self.stream_seq,
            "event_type": self.event_type.value,
            "schema_version": self.schema_version,
            "payload": thaw_json(self.payload),
        }
