"""Independent SQLite embedded implementation profile for Native Kernel P5.

The profile is replaceable implementation technology. It does not change the
Architecture Canon and does not imply PostgreSQL operational equivalence.
"""

from .adapter import EVIDENCE_LINEAGE, PROFILE_ID, PROFILE_VERSION, SQLiteAppendStore
from .conformance import build_report as build_sqlite_conformance_report
from .equivalence import build_comparison_report
from .errors import (
    HistoryAdvanced,
    IdempotencyConflict,
    ImportConflict,
    MigrationDrift,
    ProjectionCorrupt,
    ProjectionNotFound,
    ReceiptCorrupt,
    ReplayIntegrityError,
    SQLiteProfileError,
    SQLiteConfigurationError,
    StaleWriterEpoch,
    StoredEventCorrupt,
    UnknownKernelInstance,
    UnsafeSQLiteVersion,
    WriterLeaseBusy,
    WriterLeaseExpired,
)
from .runtime import MINIMUM_WAL_SAFE_SQLITE, linked_sqlite_version
from .models import AppendResult, AppendStatus, StoredEvent, WriterToken
from .replay import SQLiteReplayProjector
from .replay_models import (
    OperationType,
    OperationalReceipt,
    ProjectionRebuildResult,
    ReplayResult,
    ReplaySnapshot,
    StoredProjection,
)

__all__ = [
    "PROFILE_ID",
    "PROFILE_VERSION",
    "EVIDENCE_LINEAGE",
    "SQLiteAppendStore",
    "SQLiteReplayProjector",
    "AppendResult",
    "AppendStatus",
    "StoredEvent",
    "WriterToken",
    "OperationType",
    "OperationalReceipt",
    "ProjectionRebuildResult",
    "ReplayResult",
    "ReplaySnapshot",
    "StoredProjection",
    "build_sqlite_conformance_report",
    "build_comparison_report",
    "SQLiteProfileError",
    "SQLiteConfigurationError",
    "UnsafeSQLiteVersion",
    "MINIMUM_WAL_SAFE_SQLITE",
    "linked_sqlite_version",
    "MigrationDrift",
    "UnknownKernelInstance",
    "WriterLeaseBusy",
    "WriterLeaseExpired",
    "StaleWriterEpoch",
    "IdempotencyConflict",
    "StoredEventCorrupt",
    "ReplayIntegrityError",
    "HistoryAdvanced",
    "ProjectionNotFound",
    "ProjectionCorrupt",
    "ReceiptCorrupt",
    "ImportConflict",
]
