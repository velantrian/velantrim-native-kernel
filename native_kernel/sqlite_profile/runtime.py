from __future__ import annotations

import re
import sqlite3

from .errors import SQLiteConfigurationError, UnsafeSQLiteVersion

MINIMUM_WAL_SAFE_SQLITE = "3.51.3"
_MINIMUM_WAL_SAFE_SQLITE_PARTS = (3, 51, 3)
_VERSION_RE = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")


def parse_sqlite_version(value: object) -> tuple[int, int, int]:
    """Parse the exact three-component SQLite runtime version."""

    if not isinstance(value, str):
        raise UnsafeSQLiteVersion("linked SQLite version must be an exact string")
    match = _VERSION_RE.fullmatch(value)
    if match is None:
        raise UnsafeSQLiteVersion(
            f"linked SQLite version {value!r} is not in exact MAJOR.MINOR.PATCH form"
        )
    return tuple(int(part) for part in match.groups())  # type: ignore[return-value]


def sqlite_wal_version_is_safe(value: object) -> bool:
    """Return whether a version is outside the known WAL-reset bug range."""

    try:
        version = parse_sqlite_version(value)
    except UnsafeSQLiteVersion:
        return False
    return version >= _MINIMUM_WAL_SAFE_SQLITE_PARTS


def require_safe_sqlite_for_wal(version: object | None = None) -> str:
    """Fail closed before opening a WAL database on a vulnerable SQLite build.

    The profile intentionally uses a single conservative floor rather than
    silently accepting branch-specific backports. A backport may be added only
    through an explicit allowlist and its own reproducible CI evidence.
    """

    observed = sqlite3.sqlite_version if version is None else version
    if not sqlite_wal_version_is_safe(observed):
        raise UnsafeSQLiteVersion(
            "SQLite WAL mode requires linked SQLite >= "
            f"{MINIMUM_WAL_SAFE_SQLITE}; observed {observed!r}. "
            "Versions 3.7.0 through 3.51.2 are affected by the upstream "
            "WAL-reset corruption bug unless an explicitly evidenced backport is used."
        )
    return str(observed)


def linked_sqlite_version(declared: object | None = None) -> str:
    """Return the linked version and reject conflicting evidence metadata."""

    observed = require_safe_sqlite_for_wal()
    if declared is not None and declared != observed:
        raise SQLiteConfigurationError(
            f"declared SQLite version {declared!r} differs from linked version {observed!r}"
        )
    return observed
