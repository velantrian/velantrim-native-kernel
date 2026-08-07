# 🐘 PostgreSQL Reference Profile — P2

`native_kernel.postgresql_profile` is the bounded P2 storage adapter for the clean Native Kernel lineage.

```text
P1 semantic Command + explicit authority
        ↓
P2 PostgreSQL transaction
        ├── writer owner/epoch fence
        ├── durable scoped idempotency
        ├── rollback-safe global/stream sequences
        ├── canonical payload/envelope bytes
        └── nkp1 / nke1 integrity chain
```

## Profile choices

- PostgreSQL compatibility: `16–18`;
- repository matrix: PostgreSQL `16` and `18` × Python `3.11` and `3.12`;
- driver: `psycopg>=3.3,<3.4`;
- migrations: numbered SQL with SHA-256 ledger;
- one DB-backed writer lease per Kernel instance.

These are replaceable profile choices, not Architecture Canon.

## Install

```bash
python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
```

Importing P1 or P2 does not import Psycopg. The driver is loaded only for a DSN-backed connection.

## Minimal usage

```python
from native_kernel.postgresql_profile import PostgreSQLAppendStore

store = PostgreSQLAppendStore.from_dsn(dsn, authority_port)
store.migrate()
store.register_instance("instance:local")
token = store.acquire_writer_lease("instance:local", "writer:primary")
result = store.append(command, token)
```

`authority_port.require(command)` must succeed before append. Storage presence never creates authority.

## Idempotency

Scope:

```text
(instance_id, command_contract, idempotency_key)
```

- first command → `APPENDED`;
- same key + same digest → `RETURN_ORIGINAL_APPEND_RESULT`;
- same key + different digest → `IDEMPOTENCY_CONFLICT`.

The Event and idempotency record commit atomically.

## Writer fencing

`kernel_instances.writer_epoch` is monotonic. A token must match current owner/epoch and remain unexpired. Release/replacement makes older tokens unusable.

## Migrations

Files use `NNNN_name.sql`. Exact checksums are recorded in `native_kernel.schema_migrations`; applied-version drift fails. An advisory transaction lock serializes bootstrap and ledger changes.

## Repository evidence

PR #47 head `e80492bcacde2ff2be3a2ee03aa5aa53a714d288`:

```text
P2 run 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
```

Every matrix job passed unit tests, manifest guards, five PostgreSQL integration scenarios and compileall.

## Validation

```bash
python -m unittest discover -s tests -p 'test_postgresql_profile_unit.py' -v
python -m unittest discover -s tests -p 'test_p2_manifest.py' -v
python tools/profiles/validate_p2_manifest.py

NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_postgresql_profile_integration.py' -v
```

## Explicit limits

P2 does not implement projection persistence/rebuild, replay/upcasters, deletion-byte execution, network API, conformance adapter, C1/C2/C3, production HA/backup/credentials/compliance guarantees or ecosystem integration.

All 72 assertion-level runtime results remain `UNSUPPORTED` until P4.
