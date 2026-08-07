# RFC-0002: PostgreSQL Reference Profile v0

- **Status:** `ACCEPTED`
- **Operator approval:** `APPROVED`
- **Current phase:** `P2 PARTIAL / REPOSITORY-INTEGRATION-TESTED`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Profile version:** `0.2-p2`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Related:** ADR-0001, ADR-0009, ADR-0011–0016, Issues #1, #18 and #46, PR #47

## Purpose and boundary

This is the first clean full-profile lineage. It is not a reconstruction or relabelling of missing `v0.1.2.1`.

```text
clean reference profile
≠ recovered historical source
≠ Architecture Canon
≠ automatic C1/C2/C3
```

PostgreSQL tables, Psycopg, Python modules, locks, indexes and migration files are replaceable profile details.

## Phase status

| Phase | State |
|---|---|
| P0 profile plan | accepted / complete |
| P1 semantic core | merged / repository-tested |
| P2 authoritative append/idempotency | partial / repository-integration-tested |
| P3 replay/projections/Receipts | not authorized |
| P4 conformance adapter | not authorized |
| P5 independent SQLite profile | not authorized |

## P2 technology profile

```text
PostgreSQL compatibility: 16–18
Repository matrix:        PG16/18 × Python3.11/3.12
Driver:                   psycopg >=3.3,<3.4
Migration strategy:       numbered SQL + SHA-256 ledger
Writer strategy:          durable owner/epoch lease per instance
Counter strategy:         row-locked transactional counters
```

The driver is lazy so P1 remains standard-library-only.

## Transaction model

```text
Command
→ explicit authority
→ lock instance
→ validate writer owner/epoch/expiry
→ inspect durable idempotency
   ├── same digest → original committed Event
   └── different digest → IDEMPOTENCY_CONFLICT
→ allocate contiguous global/stream numbers
→ canonical payload/envelope bytes
→ append Event and advance counters
→ persist idempotency result
→ commit
→ acknowledge
```

Idempotency scope: `(instance_id, command_contract, idempotency_key)`.

Normal tables, not PostgreSQL sequences, own authoritative counters because rollback must not consume visible ordering values.

## Integrity and migration boundaries

P2 stores JSONB plus exact canonical payload/envelope bytes, `nkp1`, `nke1`, previous global hash and writer epoch. Hash chains are integrity signals, not authentication.

Migrations use `NNNN_name.sql`, a SHA-256 ledger and a transaction advisory lock. Applied-version byte drift fails explicitly.

## Repository evidence

PR #47 evidence head `e80492bcacde2ff2be3a2ee03aa5aa53a714d288`:

```text
P2 run 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
AI context run 31151298002 — PASS
P1 and fixture integrity — PASS
```

Each P2 job passed unit, manifest, compile and five integration scenarios: migration idempotency, lease fencing, retry/conflict atomicity, rollback-safe sequence reuse and concurrent same-digest append.

## Evidence limit

```text
P2 integration REPOSITORY_REPRODUCED
≠ P3 replay/projection runtime
≠ operational deletion
≠ P4 conformance
≠ C1/C2/C3
≠ production operations guarantee
```

All 72 assertion-level runtime statuses remain `UNSUPPORTED` until P4.

## Promotion gate

P3 requires a separate operator GO and a new issue/PR.
