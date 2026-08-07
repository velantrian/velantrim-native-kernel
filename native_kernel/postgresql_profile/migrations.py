from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .errors import MigrationDrift

_MIGRATION_RE = re.compile(r"^(\d{4})_([a-z0-9_]+)\.sql$")
_BOOTSTRAP = """
CREATE SCHEMA IF NOT EXISTS native_kernel;
CREATE TABLE IF NOT EXISTS native_kernel.schema_migrations (
    version text PRIMARY KEY,
    name text NOT NULL,
    sha256 text NOT NULL CHECK (sha256 ~ '^[0-9a-f]{64}$'),
    applied_at timestamptz NOT NULL DEFAULT transaction_timestamp()
);
"""


@dataclass(frozen=True, slots=True)
class Migration:
    version: str
    name: str
    sql: str
    sha256: str
    path: Path


def discover_migrations(root: Path | None = None) -> tuple[Migration, ...]:
    directory = root or Path(__file__).with_name("sql")
    migrations: list[Migration] = []
    for path in sorted(directory.glob("*.sql")):
        match = _MIGRATION_RE.fullmatch(path.name)
        if not match:
            raise ValueError(f"invalid migration filename: {path.name}")
        raw = path.read_bytes()
        migrations.append(
            Migration(
                version=match.group(1),
                name=match.group(2),
                sql=raw.decode("utf-8"),
                sha256=hashlib.sha256(raw).hexdigest(),
                path=path,
            )
        )
    versions = [item.version for item in migrations]
    if len(versions) != len(set(versions)):
        raise ValueError("duplicate migration version")
    if not migrations:
        raise ValueError("no PostgreSQL migrations discovered")
    return tuple(migrations)


def apply_migrations(connection: Any, migrations: Iterable[Migration] | None = None) -> tuple[str, ...]:
    selected = tuple(migrations or discover_migrations())
    applied: list[str] = []
    with connection.transaction():
        with connection.cursor() as cursor:
            # Serialize bootstrap and ledger changes across independent processes.
            cursor.execute("SELECT pg_advisory_xact_lock(%s)", (7319462100200001,))
            cursor.execute(_BOOTSTRAP)
            for migration in selected:
                cursor.execute(
                    "SELECT name, sha256 FROM native_kernel.schema_migrations WHERE version = %s FOR UPDATE",
                    (migration.version,),
                )
                row = cursor.fetchone()
                if row is not None:
                    if row[0] != migration.name or row[1] != migration.sha256:
                        raise MigrationDrift(
                            f"migration {migration.version} differs from recorded checksum/name"
                        )
                    continue
                cursor.execute(migration.sql)
                cursor.execute(
                    "INSERT INTO native_kernel.schema_migrations(version, name, sha256) VALUES (%s, %s, %s)",
                    (migration.version, migration.name, migration.sha256),
                )
                applied.append(migration.version)
    return tuple(applied)
