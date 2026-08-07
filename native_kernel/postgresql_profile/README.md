# 🐘 PostgreSQL Reference Profile — P2 + P3 + P4

`native_kernel.postgresql_profile` is the bounded PostgreSQL implementation and assertion-evidence profile for the clean Native Kernel lineage.

```text
P1 semantic Command + explicit authority
        ↓
P2 authoritative append transaction
        ↓
P3 verified replay + disposable projections + bounded Receipts
        ↓
P4 assertion-scoped checks + nk-evidence-report/1
```

## Profile choices

- PostgreSQL compatibility: `16–18`;
- repository matrix: PostgreSQL `16/18` × Python `3.11/3.12`;
- driver: `psycopg>=3.3,<3.4`;
- migrations: numbered SQL with SHA-256 ledger;
- one DB-backed writer lease per Kernel instance;
- replay snapshot: repeatable-read;
- projection publication: locked current-head comparison;
- P4 report protocol: `nk-evidence-report/1`.

These are replaceable profile choices, not Architecture Canon.

## Install

```bash
python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
```

Psycopg is loaded only for DSN-backed operations.

## Append usage

```python
from native_kernel.postgresql_profile import PostgreSQLAppendStore

store = PostgreSQLAppendStore.from_dsn(dsn, authority_port)
store.migrate()
store.register_instance("instance:local")
token = store.acquire_writer_lease("instance:local", "writer:primary")
result = store.append(command, token)
```

`authority_port.require(command)` must succeed before append. Storage presence never creates authority.

## Replay and projection usage

```python
from native_kernel.postgresql_profile import PostgreSQLReplayProjector

projector = PostgreSQLReplayProjector.from_dsn(dsn)
projector.migrate()
replay = projector.replay("instance:local")
rebuild = projector.rebuild_projection("instance:local")
projection = projector.load_projection("instance:local")
projector.destroy_projection("instance:local")
receipt = projector.load_receipt(rebuild.receipt.receipt_id)
```

A projection is disposable. Destroying it does not remove authoritative Events or committed Receipt history.

## Idempotency and ordering

Scope:

```text
(instance_id, command_contract, idempotency_key)
```

- first command → `APPENDED`;
- same key + same digest → original result;
- same key + different digest → `IDEMPOTENCY_CONFLICT`.

Event and idempotency result commit atomically. Global and stream sequences remain contiguous after rollback.

## Verified replay

For one selected instance, P3:

1. captures the authoritative sequence/hash head;
2. verifies Event count/max sequence;
3. validates stored canonical payload/envelope commitments;
4. validates the `GENESIS → nke1` chain;
5. applies an explicit deterministic upcaster path;
6. reduces from empty through the P1 reducer;
7. verifies final sequence/hash against the captured head.

Unknown schema versions fail without an explicit path.

## Stale projection protection

```text
history unchanged → publish Receipt/projection
history advanced  → HistoryAdvanced; publish nothing
```

Receipt and projection publication roll back together.

## Operational Receipts

P3 persists canonical `REPLAY` and `PROJECTION_REBUILD` Receipts. They record the declared operation, selected instance, source head/range, reducer/schema version, state digest, projection generation and limitations.

They do not prove truth, external authenticity, complete integrity, physical deletion, C3 or production guarantees.

## P4 conformance usage

Python API:

```python
from pathlib import Path
from native_kernel.postgresql_profile import build_report, render_report

report = build_report(
    Path("contracts/fixture-pack.json"),
    dsn=dsn,
    conformance_level="C1",
    evidence_level="LOCALLY_TESTED",
)
print(render_report(report))
```

Runner-compatible CLI:

```bash
export NK_TEST_POSTGRES_DSN='postgresql://...'
export NK_CONFORMANCE_LEVEL=C1
export NK_EVIDENCE_LEVEL=LOCALLY_TESTED

python tools/conformance/runner.py adapter \
  --output p4-report.json \
  -- python tools/conformance/postgresql_profile_adapter.py

python tools/conformance/validate_p4_report.py p4-report.json
```

Repository C2 additionally requires exact non-local commit/run/Python/PostgreSQL metadata and retained CI artifacts.

## P4 assertion map

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
```

Every supported/partial result references passed checks and limitations. All `NK-EPI-001…008` results remain unsupported because the family remains proposed.

```text
support_state: PARTIAL
kernel_runtime_conformance: C2
```

C2 applies only to the 41 supported results.

## P4 check groups

Profile-neutral:

- registry coverage and decision statuses;
- identity golden/invalid vectors;
- semantic roles/scope/source-bound identity;
- deny-by-default authority;
- Receipt proof boundaries;
- reducer determinism/failures;
- semantic deletion transitions.

PostgreSQL:

- migration idempotency;
- writer fencing;
- append/retry/conflict;
- rollback-safe ordering;
- persisted replay and projection rebuild;
- stale-head rejection;
- stored corruption detection.

Evidence:

- exact environment metadata;
- assertion-to-check traceability.

## Repository evidence

Initial P4 evidence head:

```text
93710131fffdea7d9a586cc05e7f258c07fae707
```

```text
P4 run 31175767586 — PASS
PostgreSQL 16/18 × Python 3.11/3.12 — PASS
P1/P2/P3 regressions — PASS
4 JSON artifacts retained
```

Exact artifact digests are recorded in `docs/ai/P4_IMPLEMENTATION_RECORD.md`.

## Validation

```bash
python -m unittest discover -s tests -p 'test_p4_conformance_unit.py' -v
python -m unittest discover -s tests -p 'test_p4_manifest.py' -v
python tools/profiles/validate_p4_manifest.py

NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_p4_postgresql_integration.py' -v
```

## Migrations

`NNNN_name.sql` checksums are stored in `native_kernel.schema_migrations`. An advisory transaction lock serializes bootstrap and ledger changes.

P3 migration adds disposable projection and Receipt tables without redesigning the P2 authoritative append transaction. P4 adds no SQL schema.

## Explicit limits

This package does not implement:

- P5 independent SQLite profile;
- C3 cross-profile equivalence;
- physical/cryptographic deletion execution;
- complete conflict subsystem;
- restore-before-visibility enforcement;
- truth/signature/notarization certification;
- network API;
- C4/C5 or production operation;
- Titan, Mentaury or Crystal wiring;
- historical source recovery.
