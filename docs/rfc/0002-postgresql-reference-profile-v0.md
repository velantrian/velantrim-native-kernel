# RFC-0002: PostgreSQL Reference Profile v0

- **Status:** `ACCEPTED`
- **Operator approval:** `APPROVED`
- **Current phase:** `P2 PARTIAL IMPLEMENTATION`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Profile version:** `0.2-p2`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Related:** ADR-0001, ADR-0009, ADR-0011–0016, Issues #1, #18 and #46

## Purpose

Define and implement the first clean full-profile lineage without reconstructing or relabelling the missing historical `v0.1.2.1` checkpoint.

```text
clean reference profile
≠ recovered historical source
≠ Architecture Canon
≠ automatic C1/C2/C3
```

## Architecture boundary

The profile implements accepted abstract contracts. PostgreSQL tables, Psycopg, Python modules, locks, indexes and migration files are replaceable profile details.

```text
Architecture Canon
→ nk-id / nk-event / nk-deletion / nk-fixtures
→ clean PostgreSQL profile
```

## Phase status

| Phase | State |
|---|---|
| P0 profile plan | accepted / complete |
| P1 semantic core | merged / locally tested |
| P2 authoritative append/idempotency | authorized / partial branch implementation |
| P3 replay/projections/Receipts | not authorized |
| P4 conformance adapter | not authorized |
| P5 independent SQLite profile | not authorized |

## P2 technology profile

```text
PostgreSQL compatibility: 16–18
CI service matrix:        16 and 18
Python:                   >=3.11,<3.13
Driver:                   psycopg >=3.3,<3.4
Migration strategy:       numbered SQL + SHA-256 ledger
Writer strategy:          durable owner/epoch lease per instance
Counter strategy:         row-locked transactional counters
```

The driver is loaded lazily so `native_kernel.semantic_core` remains standard-library-only.

## P2 transaction model

```text
Command
→ explicit authority check
→ lock Kernel instance
→ validate current writer owner/epoch/expiry
→ inspect durable idempotency key
   ├── same digest → return original committed Event
   └── different digest → IDEMPOTENCY_CONFLICT
→ allocate contiguous global and stream numbers
→ build canonical payload/envelope bytes
→ append Event
→ advance instance and stream counters
→ persist idempotency result
→ commit
→ acknowledge
```

The idempotency scope is:

```text
(instance_id, command_contract, idempotency_key)
```

Global and stream counters are stored in normal tables rather than PostgreSQL sequences because transaction rollback must not consume visible authoritative sequence numbers.

## Writer fencing

`kernel_instances.writer_epoch` is monotonic. The lease row records owner, epoch and expiry. Append, renew and release require a matching non-expired token. A new lease owner or a reacquisition after expiry increments the epoch.

This is single-writer fencing, not distributed consensus.

## Event integrity

P2 stores:

- JSONB payload for profile queries;
- exact canonical payload bytes;
- exact canonical Event envelope bytes;
- `nkp1` payload commitment;
- `nke1` global hash chain;
- previous global hash and writer epoch.

The chain detects inconsistency under the tested model. It is not authentication or protection against every privileged rewrite.

## Migrations

Files use `NNNN_name.sql`. Exact SHA-256 and name are recorded in `native_kernel.schema_migrations`. Applied-version byte drift fails explicitly. A PostgreSQL advisory transaction lock serializes bootstrap and migration-ledger operations.

## Evidence

```text
9 P2 unit tests PASS
5 P2 manifest tests PASS
validator and compileall PASS
5 PostgreSQL integration tests declared
local PostgreSQL integration NOT RUN — no DSN/server
repository CI NOT_RECORDED
```

The integration suite covers:

1. migration and instance idempotency;
2. lease busy/release/epoch fencing;
3. append/retry/conflict atomicity;
4. rollback preserving sequence 1;
5. concurrent same-digest append producing one Event.

## Non-goals

P2 does not implement P3 projections/replay, operational Receipts, deletion execution, network API, P4 conformance, P5 SQLite, C1/C2/C3, production operational guarantees, ecosystem wiring or source recovery.

All 72 assertion-level runtime results remain `UNSUPPORTED` until P4.

## Promotion criteria

P2 can be called PostgreSQL-integrated only after exact PostgreSQL 16/18 runs are recorded. P3 requires a separate operator GO and a new issue/PR.
