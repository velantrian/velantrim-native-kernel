"""Profile-independent P1 semantic core.

This package implements deterministic in-memory semantics only. It provides no
storage adapter, durable append path, database schema, network service or
profile conformance claim.
"""

from .authority import AuthorityDecision, AuthorityGrant, StaticAuthorityPolicy
from .canonical import (
    canonical_json_bytes,
    claim_id,
    command_digest,
    content_hash,
    domain_hash,
    lineage_id,
    state_digest,
)
from .deletion import DeletionReceipt, DeletionState, run_transitions, transition
from .errors import (
    AuthorityDenied,
    ContractViolation,
    InvalidTransition,
    ReceiptOverclaim,
    SemanticCoreError,
    SequenceViolation,
    UnsupportedVersion,
)
from .models import (
    ClaimIdentity,
    Command,
    EventType,
    LineageSeed,
    SemanticContent,
    SemanticEvent,
    SemanticRole,
)
from .receipt import AdmissionReceipt
from .reducer import (
    REDUCER_VERSION,
    SUPPORTED_EVENT_SCHEMA,
    SemanticState,
    reduce_event,
    reduce_events,
)

__all__ = [
    "AdmissionReceipt",
    "AuthorityDecision",
    "AuthorityDenied",
    "AuthorityGrant",
    "ClaimIdentity",
    "Command",
    "ContractViolation",
    "DeletionReceipt",
    "DeletionState",
    "EventType",
    "InvalidTransition",
    "LineageSeed",
    "REDUCER_VERSION",
    "ReceiptOverclaim",
    "SUPPORTED_EVENT_SCHEMA",
    "SemanticContent",
    "SemanticCoreError",
    "SemanticEvent",
    "SemanticRole",
    "SemanticState",
    "SequenceViolation",
    "StaticAuthorityPolicy",
    "UnsupportedVersion",
    "canonical_json_bytes",
    "claim_id",
    "command_digest",
    "content_hash",
    "domain_hash",
    "lineage_id",
    "reduce_event",
    "reduce_events",
    "run_transitions",
    "state_digest",
    "transition",
]
