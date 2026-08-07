"""Bounded PostgreSQL append, replay, projection, Receipt and P4 evidence profile.

PostgreSQL and Psycopg are replaceable profile technologies, not Architecture
Canon. Importing this package does not import Psycopg; a driver is required only
when a real connection is requested. P4 conformance remains assertion-scoped
and does not imply complete profile support or C3.
"""
from .adapter import (
    EVIDENCE_LINEAGE,
    PROFILE_ID,
    PostgreSQLAppendStore,
    connection_factory_from_dsn,
)
from .conformance import (
    PROFILE_VERSION,
    ConformanceCheck,
    ConformanceExecutionError,
    build_report,
    render_report,
    report_from_environment,
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
    "ConformanceCheck",
    "ConformanceExecutionError",
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
    "PROFILE_VERSION",
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
    "build_report",
    "canonical_recorded_at",
    "connection_factory_from_dsn",
    "discover_migrations",
    "event_hash",
    "payload_hash",
    "render_report",
    "report_from_environment",
]
