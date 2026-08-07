from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any, Mapping

from native_kernel.semantic_core.canonical import canonical_json_bytes, domain_hash
from native_kernel.semantic_core.errors import ContractViolation
from native_kernel.semantic_core.models import Command

_EVENT_HASH_RE = re.compile(r"^nke1:[0-9a-f]{64}$")


def payload_hash(payload: Mapping[str, Any]) -> str:
    return "nkp1:" + domain_hash("nk-event-payload-v1", payload)


def event_hash(envelope_without_hash: Mapping[str, Any]) -> str:
    return "nke1:" + domain_hash("nk-event-envelope-v1", envelope_without_hash)


def canonical_recorded_at(value: datetime) -> str:
    if not isinstance(value, datetime) or value.tzinfo is None:
        raise ContractViolation("recorded_at must be timezone-aware")
    utc = value.astimezone(timezone.utc)
    if utc.microsecond:
        raise ContractViolation("recorded_at must be truncated to an exact UTC second")
    return utc.strftime("%Y-%m-%dT%H:%M:%SZ")


def build_event_envelope(
    command: Command,
    *,
    event_id: str,
    global_seq: int,
    stream_seq: int,
    recorded_at: datetime,
    prev_global_hash: str,
) -> tuple[dict[str, Any], bytes, bytes]:
    if not isinstance(command, Command):
        raise ContractViolation("command must be a Command")
    if not isinstance(event_id, str) or not event_id:
        raise ContractViolation("event_id must be a non-empty string")
    if isinstance(global_seq, bool) or not isinstance(global_seq, int) or global_seq < 1:
        raise ContractViolation("global_seq must be a positive integer")
    if isinstance(stream_seq, bool) or not isinstance(stream_seq, int) or stream_seq < 1:
        raise ContractViolation("stream_seq must be a positive integer")
    if prev_global_hash != "GENESIS" and not _EVENT_HASH_RE.fullmatch(prev_global_hash):
        raise ContractViolation("prev_global_hash must be GENESIS or an nke1 hash")

    command_object = command.as_contract_object()
    payload = command_object["payload"]
    p_hash = payload_hash(payload)
    envelope: dict[str, Any] = {
        "contract": "nk-event-envelope/1",
        "event_id": event_id,
        "command_id": command.command_id,
        "idempotency_key": command.idempotency_key,
        "stream_id": command.stream_id,
        "global_seq": global_seq,
        "stream_seq": stream_seq,
        "actor_ref": command.actor_ref,
        "authority_ref": command.authority_ref,
        "recorded_at": canonical_recorded_at(recorded_at),
        "event_type": command.event_type.value,
        "schema_version": command.schema_version,
        "payload": payload,
        "prev_global_hash": prev_global_hash,
        "payload_hash": p_hash,
    }
    envelope["event_hash"] = event_hash(envelope)
    return envelope, canonical_json_bytes(payload), canonical_json_bytes(envelope)
