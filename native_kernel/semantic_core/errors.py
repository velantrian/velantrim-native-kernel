from __future__ import annotations


class SemanticCoreError(ValueError):
    """Base error for deterministic P1 semantic-core contract failures."""


class ContractViolation(SemanticCoreError):
    """Input violates a declared semantic-core contract."""


class AuthorityDenied(SemanticCoreError):
    """No explicit authority grant permits the requested command."""


class UnsupportedVersion(SemanticCoreError):
    """A schema or reducer version is unsupported."""


class SequenceViolation(SemanticCoreError):
    """A logical event sequence is non-contiguous or inconsistent."""


class InvalidTransition(SemanticCoreError):
    """A deletion/restriction state transition is forbidden."""


class ReceiptOverclaim(SemanticCoreError):
    """A Receipt claims more than the recorded evidence can establish."""
