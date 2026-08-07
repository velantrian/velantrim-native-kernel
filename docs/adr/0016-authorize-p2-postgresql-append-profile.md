# ADR-0016: Authorize the P2 PostgreSQL authoritative append profile

- **Decision status:** `ACCEPTED`
- **Evidence level:** `REPOSITORY_REPRODUCED — P2 INTEGRATION`
- **Implementation status:** `PARTIAL — P2 APPEND/IDEMPOTENCY PROFILE`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-07`
- **Decider:** `@velantrian`
- **Track:** `Implementation Profile`
- **Related:** Issue #46, PR #47, RFC-0002, ADR-0001, ADR-0009, ADR-0012, ADR-0015

## Context

P1 established profile-independent semantic objects, authority checks and deterministic logical reduction. The operator separately authorized P2 on 2026-08-07.

## Decision

Implement a bounded PostgreSQL authoritative append/idempotency adapter with reversible profile choices:

```text
PostgreSQL compatibility: 16–18
CI service matrix:        16 and 18
Python:                   >=3.11,<3.13
Driver:                   psycopg >=3.3,<3.4
Migrations:               numbered SQL + checksum ledger
Writer:                   one DB-backed owner/epoch lease per instance
Sequences:                rollback-safe row-locked counters
```

PostgreSQL, Psycopg, SQL tables, indexes and migration layout are not Architecture Canon.

## Transaction boundary

```text
explicit authority
→ lock instance and validate writer owner/epoch/expiry
→ inspect scoped durable idempotency record
→ allocate global and stream sequence
→ create canonical payload/envelope bytes and commitments
→ append Event
→ advance counters/history head
→ persist idempotency result
→ commit
→ acknowledge
```

Same key and canonical command digest returns the original Event. Same key with a different digest fails as `IDEMPOTENCY_CONFLICT` without a new append.

## Integrity boundary

P2 stores exact canonical payload/envelope bytes and `nkp1`/`nke1` commitments. The chain is an integrity signal, not authentication, consensus or protection from every privileged database rewrite.

## Writer boundary

One Kernel instance has one current writer owner/epoch lease. Epoch is monotonic. Stale, replaced, released or expired tokens fail explicitly.

## Rejected/deferred alternatives

- PostgreSQL sequences for authoritative counters: rejected for P2 because rollback does not return consumed values;
- advisory lock as the only writer identity: rejected because owner, epoch and expiry must be durable and inspectable;
- Alembic: deferred until the schema stabilizes;
- per-request PostgreSQL/SQLite routing: rejected by ADR-0009;
- multi-writer consensus: outside `nk-event/1.0`.

## Repository evidence

PR #47 head `e80492bcacde2ff2be3a2ee03aa5aa53a714d288` produced:

```text
P2 workflow run: 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
9 P2 unit tests per matrix job — PASS
5 PostgreSQL integration tests per matrix job — PASS
5 P2 manifest tests per matrix job — PASS
compileall and manifest validator — PASS
AI context integrity run 31151298002 — PASS
P1 semantic core and conformance fixture integrity — PASS
```

This establishes the bounded P2 behaviors in the declared repository matrix. It does not establish P3 replay/projections, assertion-level conformance, C1/C2/C3, production durability, security, privacy, HA, backup or deletion guarantees.

## Explicit non-goals

- P3 replay, projections and operational Receipts;
- P4 assertion-scoped conformance;
- P5 SQLite comparison;
- deletion of real bytes/backups/keys;
- network API;
- packaging/publication decision under Issue #18;
- Titan, Mentaury or Crystal wiring;
- Issue #1 historical recovery;
- ADR-0008 or NK-EPI promotion.

## Next gate

P3 requires a separate operator GO and a separate issue/PR. All 72 registry assertions remain runtime `UNSUPPORTED` until P4.
