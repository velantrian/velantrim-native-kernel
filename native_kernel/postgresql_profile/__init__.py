"""P2 PostgreSQL authoritative append/idempotency profile.

PostgreSQL and Psycopg are replaceable profile technologies, not Architecture
Canon. Importing this package does not import Psycopg; a driver is required only
when a real connection is requested.
"""
from .adapter import (
    EVIDENCE_LINEAGE,
    PROFILE_ID,
    PostgreSQLAppendStore,
    connection_factory_from_dsn,
)
from .errors import (
    DriverUnavailable,
    IdempotencyConflict,
    MigrationDrift,
    PostgreSQLProfileError,
    StaleWriterEpoch,
    StoredEventCorrupt,
    UnknownKernelInstance,
    WriterLeaseBusy,
    WriterLeaseExpired,
)
from .hashing import build_event_envelope, canonical_recorded_at, event_hash, payload_hash
from .migrations import Migration, apply_migrations, discover_migrations
from .models import AppendResult, AppendStatus, StoredEvent, WriterToken

__all__ = [
    "AppendResult",
    "AppendStatus",
    "DriverUnavailable",
    "EVIDENCE_LINEAGE",
    "IdempotencyConflict",
    "Migration",
    "MigrationDrift",
    "PROFILE_ID",
    "PostgreSQLAppendStore",
    "PostgreSQLProfileError",
    "StaleWriterEpoch",
    "StoredEvent",
    "StoredEventCorrupt",
    "UnknownKernelInstance",
    "WriterLeaseBusy",
    "WriterLeaseExpired",
    "WriterToken",
    "apply_migrations",
    "build_event_envelope",
    "canonical_recorded_at",
    "connection_factory_from_dsn",
    "discover_migrations",
    "event_hash",
    "payload_hash",
]
