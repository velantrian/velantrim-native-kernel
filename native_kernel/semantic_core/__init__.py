"""Profile-independent semantic core and deterministic schema helpers.

The package remains standard-library-only. It provides semantic objects,
reduction, state decoding and explicit upcaster routing, but no storage adapter,
network service or profile conformance claim.
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
from .state_codec import semantic_state_from_contract_object
from .upcasting import (
    UpcastResult,
    UpcastStep,
    UpcasterRegistry,
    identity_upcaster_registry,
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
    "UpcastResult",
    "UpcastStep",
    "UpcasterRegistry",
    "canonical_json_bytes",
    "claim_id",
    "command_digest",
    "content_hash",
    "domain_hash",
    "identity_upcaster_registry",
    "lineage_id",
    "reduce_event",
    "reduce_events",
    "run_transitions",
    "semantic_state_from_contract_object",
    "state_digest",
    "transition",
]
