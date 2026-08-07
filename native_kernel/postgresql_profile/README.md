# 🐘 PostgreSQL Reference Profile — P2 + P3

`native_kernel.postgresql_profile` is the bounded PostgreSQL implementation profile for the clean Native Kernel lineage.

```text
P1 semantic Command + explicit authority
        ↓
P2 authoritative append transaction
        ├── writer owner/epoch fence
        ├── durable scoped idempotency
        ├── rollback-safe global/stream sequences
        ├── canonical payload/envelope bytes
        └── nkp1 / nke1 integrity chain
        ↓
P3 verified persisted replay
        ├── repeatable-read snapshot
        ├── canonical/Event-chain verification
        ├── explicit UpcasterRegistry
        ├── P1 reducer from empty state
        ├── bounded Replay Receipt
        └── stale-head publication guard
        ↓
P3 disposable projection rebuild
        ├── monotonic generation
        ├── atomic Receipt + projection commit
        └── bounded Projection Rebuild Receipt
```

## Profile choices

- PostgreSQL compatibility: `16–18`;
- repository matrix: PostgreSQL `16` and `18` × Python `3.11` and `3.12`;
- driver: `psycopg>=3.3,<3.4`;
- migrations: numbered SQL with SHA-256 ledger;
- one DB-backed writer lease per Kernel instance;
- replay snapshot: repeatable-read, read-only;
- projection publication: locked current-head comparison.

These are replaceable profile choices, not Architecture Canon.

## Install

```bash
python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
```

Importing the semantic core or PostgreSQL profile does not import Psycopg. The driver is loaded only for a DSN-backed operation.

## Append usage

```python
from native_kernel.postgresql_profile import PostgreSQLAppendStore

store = PostgreSQLAppendStore.from_dsn(dsn, authority_port)
store.migrate()
store.register_instance("instance:local")
token = store.acquire_writer_lease("instance:local", "writer:primary")
append_result = store.append(command, token)
```

`authority_port.require(command)` must succeed before append. Storage presence never creates authority.

## Replay and projection usage

```python
from native_kernel.postgresql_profile import PostgreSQLReplayProjector

projector = PostgreSQLReplayProjector.from_dsn(dsn)
projector.migrate()

replay_result = projector.replay("instance:local")
rebuild_result = projector.rebuild_projection("instance:local")
projection = projector.load_projection("instance:local")
projector.destroy_projection("instance:local")
receipt = projector.load_receipt(rebuild_result.receipt.receipt_id)
```

A projection is a disposable read model. Destroying it does not remove authoritative Events or committed Receipt history and does not reset projection-generation lineage.

## Idempotency

Scope:

```text
(instance_id, command_contract, idempotency_key)
```

- first command → `APPENDED`;
- same key + same digest → `RETURN_ORIGINAL_APPEND_RESULT`;
- same key + different digest → `IDEMPOTENCY_CONFLICT`.

The Event and idempotency record commit atomically.

## Verified replay

For the selected instance, P3:

1. captures the authoritative sequence/hash head in a repeatable-read snapshot;
2. requires Event count/max sequence to equal that head;
3. loads every Event from sequence `1` using P2 stored-event checks;
4. validates the `GENESIS → nke1` global hash chain;
5. applies an explicit deterministic upcaster path;
6. reduces from empty through the declared P1 reducer;
7. requires the replayed final hash and sequence to match the snapshot head.

Unknown schema versions are not silently treated as current. A missing, ambiguous, cyclic or invalid path fails.

## Stale projection protection

Replay and projection publication are separate transactions. Before publication, P3 locks the Kernel instance row and compares current sequence/hash with the replay snapshot.

```text
history unchanged → publish Receipt/projection
history advanced  → HistoryAdvanced; publish nothing
```

Receipt and projection changes roll back together if publication fails.

## Operational Receipts

P3 persists canonical Receipts for:

- `REPLAY`;
- `PROJECTION_REBUILD`.

They record the instance, Event range/head, reducer/schema version, state digest, projection generation when applicable, and explicit limitations.

They do **not** prove:

- truth of recorded Claims;
- external authenticity, signatures or notarization;
- absence of every privileged rewrite before the snapshot;
- complete Event Integrity under every threat model;
- physical deletion of bytes, backups, exports, logs or keys;
- C1/C2/C3 or production durability/security/privacy/compliance.

## Migrations

Migration files use `NNNN_name.sql`. Exact checksums are recorded in `native_kernel.schema_migrations`; applied-version drift fails. An advisory transaction lock serializes bootstrap and ledger changes.

P3 migration adds only disposable projection and operational Receipt tables. It does not redesign the P2 authoritative Event append transaction.

## Repository evidence

Initial P3 executable head:

```text
head 0f8fd4ffe5d5fb0d4bc01f3e441a053f691dbba3
P3 run 31171581859 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
P2 regression — PASS
```

Every P3 matrix job passed semantic tests, manifest guards, seven PostgreSQL integration scenarios, P2 regressions and compileall. Final-PR evidence must still be taken from the exact final head after all documentation/evidence updates.

## Validation

```bash
python -m unittest discover -s tests -p 'test_p3_semantic.py' -v
python -m unittest discover -s tests -p 'test_p3_manifest.py' -v
python tools/profiles/validate_p3_manifest.py

NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_p3_postgresql_integration.py' -v
```

P2 regression:

```bash
python -m unittest discover -s tests -p 'test_postgresql_profile_unit.py' -v
NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_postgresql_profile_integration.py' -v
```

## Explicit limits

P3 does not implement physical/cryptographic deletion, network API, P4 assertion-scoped conformance, P5 independent SQLite, C1/C2/C3, production HA/backup/credentials/compliance guarantees or ecosystem integration.

All 72 assertion-level runtime results remain `UNSUPPORTED` until P4.
