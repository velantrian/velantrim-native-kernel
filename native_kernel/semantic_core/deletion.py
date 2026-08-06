from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from .errors import ContractViolation, InvalidTransition, ReceiptOverclaim


class DeletionState(str, Enum):
    ACTIVE = "ACTIVE"
    RESTRICTED = "RESTRICTED"
    ERASE_REQUESTED = "ERASE_REQUESTED"
    ERASURE_IN_PROGRESS = "ERASURE_IN_PROGRESS"
    PARTIALLY_ERASED = "PARTIALLY_ERASED"
    FAILED_RETRYABLE = "FAILED_RETRYABLE"
    RETENTION_HOLD = "RETENTION_HOLD"
    CRYPTO_ERASED = "CRYPTO_ERASED"
    PHYSICALLY_ERASED = "PHYSICALLY_ERASED"


_ALLOWED: dict[DeletionState, frozenset[DeletionState]] = {
    DeletionState.ACTIVE: frozenset(
        {DeletionState.RESTRICTED, DeletionState.ERASE_REQUESTED, DeletionState.RETENTION_HOLD}
    ),
    DeletionState.RESTRICTED: frozenset(
        {DeletionState.ACTIVE, DeletionState.ERASE_REQUESTED, DeletionState.RETENTION_HOLD}
    ),
    DeletionState.ERASE_REQUESTED: frozenset(
        {
            DeletionState.ERASURE_IN_PROGRESS,
            DeletionState.RETENTION_HOLD,
            DeletionState.FAILED_RETRYABLE,
        }
    ),
    DeletionState.ERASURE_IN_PROGRESS: frozenset(
        {
            DeletionState.PARTIALLY_ERASED,
            DeletionState.CRYPTO_ERASED,
            DeletionState.PHYSICALLY_ERASED,
            DeletionState.FAILED_RETRYABLE,
        }
    ),
    DeletionState.PARTIALLY_ERASED: frozenset(
        {
            DeletionState.ERASURE_IN_PROGRESS,
            DeletionState.FAILED_RETRYABLE,
            DeletionState.PHYSICALLY_ERASED,
            DeletionState.CRYPTO_ERASED,
        }
    ),
    DeletionState.FAILED_RETRYABLE: frozenset(
        {DeletionState.ERASURE_IN_PROGRESS, DeletionState.RETENTION_HOLD}
    ),
    DeletionState.RETENTION_HOLD: frozenset(
        {DeletionState.RESTRICTED, DeletionState.ERASE_REQUESTED}
    ),
    DeletionState.CRYPTO_ERASED: frozenset(),
    DeletionState.PHYSICALLY_ERASED: frozenset(),
}


def transition(current: DeletionState, target: DeletionState) -> DeletionState:
    if target not in _ALLOWED[current]:
        raise InvalidTransition(f"forbidden deletion transition {current.value}->{target.value}")
    return target


def run_transitions(
    initial: DeletionState, targets: Iterable[DeletionState]
) -> DeletionState:
    state = initial
    for target in targets:
        state = transition(state, target)
    return state


@dataclass(frozen=True, slots=True)
class DeletionReceipt:
    request_id: str
    authority_ref: str
    policy_ref: str
    final_state: DeletionState
    verified_locations: tuple[str, ...]
    unverified_or_pending_locations: tuple[str, ...]
    known_limits: tuple[str, ...]
    claims_complete_global_erasure: bool = False

    def __post_init__(self) -> None:
        if self.claims_complete_global_erasure:
            raise ReceiptOverclaim(
                "a P1 deletion Receipt cannot claim complete global erasure"
            )
        if self.final_state not in {
            DeletionState.RESTRICTED,
            DeletionState.PARTIALLY_ERASED,
            DeletionState.CRYPTO_ERASED,
            DeletionState.PHYSICALLY_ERASED,
            DeletionState.FAILED_RETRYABLE,
        }:
            raise ContractViolation("deletion Receipt final_state is not reportable")
        if len(set(self.verified_locations)) != len(self.verified_locations):
            raise ContractViolation("verified_locations contains duplicates")
        if len(set(self.unverified_or_pending_locations)) != len(
            self.unverified_or_pending_locations
        ):
            raise ContractViolation("unverified_or_pending_locations contains duplicates")
        overlap = set(self.verified_locations).intersection(
            self.unverified_or_pending_locations
        )
        if overlap:
            raise ContractViolation(f"locations cannot be both verified and pending: {sorted(overlap)}")
        if self.unverified_or_pending_locations and not self.known_limits:
            raise ReceiptOverclaim("pending locations require explicit known_limits")

    def as_contract_object(self) -> dict[str, object]:
        return {
            "contract": "nk-deletion-receipt/1",
            "request_id": self.request_id,
            "authority_ref": self.authority_ref,
            "policy_ref": self.policy_ref,
            "final_state": self.final_state.value,
            "verified_locations": list(self.verified_locations),
            "unverified_or_pending_locations": list(
                self.unverified_or_pending_locations
            ),
            "known_limits": list(self.known_limits),
            "claims_complete_global_erasure": False,
        }
