from __future__ import annotations


class PostgreSQLProfileError(RuntimeError):
    """Base error for the clean PostgreSQL reference profile."""


class DriverUnavailable(PostgreSQLProfileError):
    """Psycopg is not installed for a requested PostgreSQL operation."""


class MigrationDrift(PostgreSQLProfileError):
    """A previously recorded migration version has different bytes."""


class UnknownKernelInstance(PostgreSQLProfileError):
    """The requested Kernel instance has not been registered."""


class WriterLeaseBusy(PostgreSQLProfileError):
    """Another non-expired writer owns the instance lease."""


class WriterLeaseExpired(PostgreSQLProfileError):
    """The supplied writer lease has expired or was explicitly released."""


class StaleWriterEpoch(PostgreSQLProfileError):
    """The supplied writer token no longer matches the stored epoch/owner."""


class IdempotencyConflict(PostgreSQLProfileError):
    """An idempotency key was reused with a different command digest."""


class StoredEventCorrupt(PostgreSQLProfileError):
    """Stored event bytes do not match their declared commitments."""
