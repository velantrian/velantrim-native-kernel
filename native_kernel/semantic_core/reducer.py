from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any, Iterable

from .canonical import state_digest as derive_state_digest
from .errors import ContractViolation, SequenceViolation, UnsupportedVersion
from .models import EventType, SemanticEvent

REDUCER_VERSION = "nk-p1-reducer/1"
SUPPORTED_EVENT_SCHEMA = "1"


@dataclass(frozen=True, slots=True)
class SemanticState:
    reducer_version: str = REDUCER_VERSION
    last_global_seq: int = 0
    stream_offsets: tuple[tuple[str, int], ...] = ()
    admitted_claim_ids: tuple[str, ...] = ()
    links: tuple[tuple[str, str, str], ...] = ()
    utilization_counts: tuple[tuple[str, int], ...] = ()
    superseded_by: tuple[tuple[str, str], ...] = ()
    erased_claim_ids: tuple[str, ...] = ()

    def as_contract_object(self) -> dict[str, Any]:
        return {
            "contract": "nk-p1-semantic-state/1",
            "reducer_version": self.reducer_version,
            "last_global_seq": self.last_global_seq,
            "stream_offsets": [
                {"stream_id": stream_id, "stream_seq": sequence}
                for stream_id, sequence in self.stream_offsets
            ],
            "admitted_claim_ids": list(self.admitted_claim_ids),
            "links": [
                {"from_claim_id": source, "relation": relation, "to_claim_id": target}
                for source, relation, target in self.links
            ],
            "utilization_counts": [
                {"claim_id": claim_id, "count": count}
                for claim_id, count in self.utilization_counts
            ],
            "superseded_by": [
                {"claim_id": claim_id, "by_claim_id": successor}
                for claim_id, successor in self.superseded_by
            ],
            "erased_claim_ids": list(self.erased_claim_ids),
        }

    @property
    def digest(self) -> str:
        return derive_state_digest(self.as_contract_object())


def _string(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ContractViolation(f"event payload requires non-empty string {key}")
    return value


def reduce_event(state: SemanticState, event: SemanticEvent) -> SemanticState:
    if state.reducer_version != REDUCER_VERSION:
        raise UnsupportedVersion(f"unsupported reducer version {state.reducer_version}")
    if event.schema_version != SUPPORTED_EVENT_SCHEMA:
        raise UnsupportedVersion(f"unsupported event schema version {event.schema_version}")
    if event.global_seq != state.last_global_seq + 1:
        raise SequenceViolation(
            f"expected global_seq {state.last_global_seq + 1}, got {event.global_seq}"
        )

    stream_offsets = dict(state.stream_offsets)
    expected_stream = stream_offsets.get(event.stream_id, 0) + 1
    if event.stream_seq != expected_stream:
        raise SequenceViolation(
            f"expected stream_seq {expected_stream} for {event.stream_id}, got {event.stream_seq}"
        )
    stream_offsets[event.stream_id] = event.stream_seq

    payload = dict(event.payload)
    admitted = set(state.admitted_claim_ids)
    links = set(state.links)
    utilized = dict(state.utilization_counts)
    superseded = dict(state.superseded_by)
    erased = set(state.erased_claim_ids)

    if event.event_type is EventType.ADMIT:
        admitted.add(_string(payload, "claim_id"))
    elif event.event_type is EventType.LINK:
        links.add(
            (
                _string(payload, "from_claim_id"),
                _string(payload, "relation"),
                _string(payload, "to_claim_id"),
            )
        )
    elif event.event_type is EventType.UTILIZED:
        claim_id = _string(payload, "claim_id")
        utilized[claim_id] = utilized.get(claim_id, 0) + 1
    elif event.event_type is EventType.SUPERSEDED:
        superseded[_string(payload, "claim_id")] = _string(payload, "by_claim_id")
    elif event.event_type is EventType.ERASED:
        erased.add(_string(payload, "claim_id"))
    else:  # pragma: no cover - Enum makes this unreachable
        raise ContractViolation(f"unsupported event type {event.event_type}")

    return replace(
        state,
        last_global_seq=event.global_seq,
        stream_offsets=tuple(sorted(stream_offsets.items())),
        admitted_claim_ids=tuple(sorted(admitted)),
        links=tuple(sorted(links)),
        utilization_counts=tuple(sorted(utilized.items())),
        superseded_by=tuple(sorted(superseded.items())),
        erased_claim_ids=tuple(sorted(erased)),
    )


def reduce_events(
    events: Iterable[SemanticEvent],
    *,
    initial: SemanticState | None = None,
    reducer_version: str = REDUCER_VERSION,
) -> SemanticState:
    if reducer_version != REDUCER_VERSION:
        raise UnsupportedVersion(f"unsupported reducer version {reducer_version}")
    state = initial or SemanticState(reducer_version=reducer_version)
    for event in events:
        state = reduce_event(state, event)
    return state
