from __future__ import annotations


class SQLiteProfileError(RuntimeError):
    """Base error for the clean SQLite embedded profile."""


class MigrationDrift(SQLiteProfileError):
    """A recorded SQLite migration version has different bytes."""


class UnknownKernelInstance(SQLiteProfileError):
    """The requested Kernel instance has not been registered."""


class WriterLeaseBusy(SQLiteProfileError):
    """Another non-expired writer owns the embedded profile lease."""


class WriterLeaseExpired(SQLiteProfileError):
    """The supplied writer token has expired or was released."""


class StaleWriterEpoch(SQLiteProfileError):
    """The supplied writer token no longer matches stored epoch/owner."""


class IdempotencyConflict(SQLiteProfileError):
    """An idempotency key was reused with a different command digest."""


class StoredEventCorrupt(SQLiteProfileError):
    """Stored event bytes do not match their declared commitments."""


class ReplayIntegrityError(SQLiteProfileError):
    """Persisted history cannot be replayed under declared checks."""


class HistoryAdvanced(SQLiteProfileError):
    """Authoritative history changed after replay and before publication."""


class ProjectionNotFound(SQLiteProfileError):
    """The requested disposable projection does not exist."""


class ProjectionCorrupt(SQLiteProfileError):
    """Stored projection bytes or digest are inconsistent."""


class ReceiptCorrupt(SQLiteProfileError):
    """Stored operational Receipt bytes or commitments are inconsistent."""


class ImportConflict(SQLiteProfileError):
    """Imported history conflicts with existing SQLite authoritative history."""
