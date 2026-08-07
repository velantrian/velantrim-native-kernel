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
- CI matrix: PostgreSQL `16` and `18`;
- Python: `>=3.11,<3.13`;
- driver: `psycopg>=3.3,<3.4`;
- migrations: numbered plain SQL with SHA-256 checksum ledger;
- one authoritative DB-backed writer lease per Kernel instance.

These are replaceable profile choices, not Architecture Canon.

## Install for profile/integration work

```bash
python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
```

Importing `native_kernel.semantic_core` or this package does not import Psycopg. The driver is loaded only when a DSN-backed connection is requested.

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

The key scope is:

```text
(instance_id, command_contract, idempotency_key)
```

- first command → `APPENDED`;
- same key + same command digest → `RETURN_ORIGINAL_APPEND_RESULT`;
- same key + different digest → `IDEMPOTENCY_CONFLICT`.

The event and idempotency record commit atomically.

## Writer fencing

`kernel_instances.writer_epoch` is monotonic. A lease token must match the current owner and epoch and must not be expired. Releasing or replacing a lease makes old tokens stale.

## Migrations

Migration filenames use `NNNN_name.sql`. Each exact file checksum is recorded in `native_kernel.schema_migrations`. Modified bytes under an applied version fail as migration drift. An advisory transaction lock serializes bootstrap and ledger changes.

## Validation

```bash
python -m unittest discover -s tests -p 'test_postgresql_profile_unit.py' -v
python -m unittest discover -s tests -p 'test_p2_manifest.py' -v
python tools/profiles/validate_p2_manifest.py
python -m compileall -q native_kernel tools tests

NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_postgresql_profile_integration.py' -v
```

## Explicit limits

P2 does not implement projection persistence/rebuild, replay/upcasters, deletion-byte execution, network API, conformance adapter, C1/C2/C3, production HA/backup/credentials/compliance guarantees, or ecosystem integration.

All 72 assertion-level runtime results remain `UNSUPPORTED` until P4.
