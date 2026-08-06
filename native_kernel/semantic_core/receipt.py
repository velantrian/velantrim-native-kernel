from __future__ import annotations

from dataclasses import dataclass

from .authority import AuthorityDecision
from .errors import ContractViolation, ReceiptOverclaim


@dataclass(frozen=True, slots=True)
class AdmissionReceipt:
    command_id: str
    decision: AuthorityDecision
    known_limits: tuple[str, ...]
    claims_truth_established: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.command_id, str) or not self.command_id:
            raise ContractViolation("command_id must be a non-empty string")
        if not isinstance(self.decision, AuthorityDecision):
            raise ContractViolation("decision must be an AuthorityDecision")
        if not isinstance(self.claims_truth_established, bool):
            raise ContractViolation("claims_truth_established must be boolean")
        if self.claims_truth_established:
            raise ReceiptOverclaim(
                "an admission Receipt cannot claim that an authority decision establishes truth"
            )
        if not self.known_limits or any(
            not isinstance(limit, str) or not limit for limit in self.known_limits
        ):
            raise ReceiptOverclaim(
                "an admission Receipt must state non-empty proof limitations"
            )

    def as_contract_object(self) -> dict[str, object]:
        return {
            "contract": "nk-admission-receipt/p1",
            "command_id": self.command_id,
            "decision": "ALLOW" if self.decision.allowed else "DENY",
            "authority_kind": self.decision.authority_kind,
            "scope": self.decision.scope,
            "policy_ref": self.decision.policy_ref,
            "actor_ref": self.decision.actor_ref,
            "authority_ref": self.decision.authority_ref,
            "basis": list(self.decision.basis),
            "known_limits": list(self.known_limits),
            "claims_truth_established": False,
        }
