"""Bounded PostgreSQL append, replay, projection and Receipt profile.

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
    HistoryAdvanced,
    IdempotencyConflict,
    MigrationDrift,
    PostgreSQLProfileError,
    ProjectionCorrupt,
    ProjectionNotFound,
    ReceiptCorrupt,
    ReplayIntegrityError,
    StaleWriterEpoch,
    StoredEventCorrupt,
    UnknownKernelInstance,
    WriterLeaseBusy,
    WriterLeaseExpired,
)
from .hashing import build_event_envelope, canonical_recorded_at, event_hash, payload_hash
from .migrations import Migration, apply_migrations, discover_migrations
from .models import AppendResult, AppendStatus, StoredEvent, WriterToken
from .receipt_store import DEFAULT_LIMITS
from .replay import DEFAULT_PROJECTION, PostgreSQLReplayProjector
from .replay_models import (
    OperationType,
    OperationalReceipt,
    ProjectionRebuildResult,
    ReplayResult,
    ReplaySnapshot,
    StoredProjection,
)

__all__ = [
    "AppendResult",
    "AppendStatus",
    "DEFAULT_LIMITS",
    "DEFAULT_PROJECTION",
    "DriverUnavailable",
    "EVIDENCE_LINEAGE",
    "HistoryAdvanced",
    "IdempotencyConflict",
    "Migration",
    "MigrationDrift",
    "OperationType",
    "OperationalReceipt",
    "PROFILE_ID",
    "PostgreSQLAppendStore",
    "PostgreSQLProfileError",
    "PostgreSQLReplayProjector",
    "ProjectionCorrupt",
    "ProjectionNotFound",
    "ProjectionRebuildResult",
    "ReceiptCorrupt",
    "ReplayIntegrityError",
    "ReplayResult",
    "ReplaySnapshot",
    "StaleWriterEpoch",
    "StoredEvent",
    "StoredEventCorrupt",
    "StoredProjection",
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
