from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .canonical import normalize_canonical
from .errors import ContractViolation
from .reducer import REDUCER_VERSION, SemanticState


def _object(value: object) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ContractViolation("semantic state must be a mapping")
    normalized = normalize_canonical(value)
    if not isinstance(normalized, dict):
        raise ContractViolation("semantic state must normalize to an object")
    return normalized


def _list(data: Mapping[str, Any], key: str) -> Sequence[Any]:
    value = data.get(key)
    if not isinstance(value, list):
        raise ContractViolation(f"semantic state field {key} must be a list")
    return value


def semantic_state_from_contract_object(value: object) -> SemanticState:
    data = _object(value)
    if data.get("contract") != "nk-p1-semantic-state/1":
        raise ContractViolation("unsupported semantic state contract")
    if data.get("reducer_version") != REDUCER_VERSION:
        raise ContractViolation("semantic state reducer version mismatch")
    last_global_seq = data.get("last_global_seq")
    if isinstance(last_global_seq, bool) or not isinstance(last_global_seq, int) or last_global_seq < 0:
        raise ContractViolation("last_global_seq must be a non-negative integer")

    stream_offsets: list[tuple[str, int]] = []
    for item in _list(data, "stream_offsets"):
        if not isinstance(item, Mapping):
            raise ContractViolation("stream offset must be an object")
        stream_id = item.get("stream_id")
        stream_seq = item.get("stream_seq")
        if not isinstance(stream_id, str) or not stream_id:
            raise ContractViolation("stream offset requires stream_id")
        if isinstance(stream_seq, bool) or not isinstance(stream_seq, int) or stream_seq < 1:
            raise ContractViolation("stream offset requires positive stream_seq")
        stream_offsets.append((stream_id, stream_seq))

    def strings(key: str) -> tuple[str, ...]:
        result: list[str] = []
        for item in _list(data, key):
            if not isinstance(item, str) or not item:
                raise ContractViolation(f"{key} must contain non-empty strings")
            result.append(item)
        return tuple(result)

    links: list[tuple[str, str, str]] = []
    for item in _list(data, "links"):
        if not isinstance(item, Mapping):
            raise ContractViolation("link must be an object")
        values = (item.get("from_claim_id"), item.get("relation"), item.get("to_claim_id"))
        if any(not isinstance(part, str) or not part for part in values):
            raise ContractViolation("link fields must be non-empty strings")
        links.append(values)  # type: ignore[arg-type]

    utilization: list[tuple[str, int]] = []
    for item in _list(data, "utilization_counts"):
        if not isinstance(item, Mapping):
            raise ContractViolation("utilization count must be an object")
        claim_id = item.get("claim_id")
        count = item.get("count")
        if not isinstance(claim_id, str) or not claim_id:
            raise ContractViolation("utilization count requires claim_id")
        if isinstance(count, bool) or not isinstance(count, int) or count < 1:
            raise ContractViolation("utilization count requires positive count")
        utilization.append((claim_id, count))

    superseded: list[tuple[str, str]] = []
    for item in _list(data, "superseded_by"):
        if not isinstance(item, Mapping):
            raise ContractViolation("superseded entry must be an object")
        claim_id = item.get("claim_id")
        successor = item.get("by_claim_id")
        if not isinstance(claim_id, str) or not claim_id or not isinstance(successor, str) or not successor:
            raise ContractViolation("superseded entry requires claim_id and by_claim_id")
        superseded.append((claim_id, successor))

    state = SemanticState(
        reducer_version=REDUCER_VERSION,
        last_global_seq=last_global_seq,
        stream_offsets=tuple(sorted(stream_offsets)),
        admitted_claim_ids=tuple(sorted(strings("admitted_claim_ids"))),
        links=tuple(sorted(links)),
        utilization_counts=tuple(sorted(utilization)),
        superseded_by=tuple(sorted(superseded)),
        erased_claim_ids=tuple(sorted(strings("erased_claim_ids"))),
    )
    if state.as_contract_object() != data:
        raise ContractViolation("semantic state object is not in canonical reducer form")
    return state
