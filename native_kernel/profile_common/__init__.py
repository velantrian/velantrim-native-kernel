"""Bounded substrate-neutral helpers shared by implementation profiles.

This package is not an implementation profile and must not absorb storage,
runtime, replay, conformance, profile-error, or authority responsibilities.
"""

from .event_envelope import (
    build_event_envelope,
    canonical_recorded_at,
    event_hash,
    payload_hash,
)

__all__ = [
    "build_event_envelope",
    "canonical_recorded_at",
    "event_hash",
    "payload_hash",
]
