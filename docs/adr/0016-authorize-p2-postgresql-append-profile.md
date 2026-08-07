# ADR-0016: Authorize the P2 PostgreSQL authoritative append profile

- **Decision status:** `ACCEPTED`
- **Evidence level:** `LOCALLY_TESTED_UNIT_ONLY`
- **Implementation status:** `PARTIAL — P2 CODE AND DECLARED INTEGRATION TESTS`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-07`
- **Decider:** `@velantrian`
- **Track:** `Implementation Profile`
- **Related:** Issue #46, RFC-0002, ADR-0001, ADR-0009, ADR-0012, ADR-0015

## Context

P1 established profile-independent semantic objects, authority checks and deterministic logical reduction. It did not provide durable history. The operator separately authorized P2 on 2026-08-07.

## Decision

Implement a bounded PostgreSQL authoritative append/idempotency adapter with these reversible profile choices:

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

## Required transaction boundary

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

Same key and same canonical command digest returns the original Event. Same key with a different digest fails as `IDEMPOTENCY_CONFLICT` without a new append.

## Integrity boundary

P2 stores exact canonical payload and envelope bytes and the accepted `nkp1`/`nke1` SHA-256 commitments. The chain is an integrity signal, not authentication, consensus or protection from every privileged database rewrite.

## Writer boundary

One Kernel instance has one current writer owner/epoch lease. Epoch is monotonic in the instance row. Stale, replaced, released or expired tokens fail explicitly.

## Rejected/deferred alternatives

- PostgreSQL sequences for authoritative counters: deferred because sequence increments are not rolled back and would violate contiguous P2 evidence expectations;
- advisory lock as the only writer identity: rejected because owner, epoch and expiry must be durable and inspectable;
- Alembic: deferred to avoid adding a second framework before the schema stabilizes;
- per-request PostgreSQL/SQLite routing: rejected by ADR-0009;
- multi-writer consensus: outside `nk-event/1.0`.

## Evidence

Available local evidence:

```text
9 P2 unit tests PASS
5 P2 manifest tests PASS
P2 manifest validator PASS
compileall PASS
5 PostgreSQL integration tests DECLARED / SKIPPED — no local PostgreSQL DSN
repository workflow result NOT_RECORDED
```

This does not establish declared-range PostgreSQL integration, C1, C2, C3, production durability, security, privacy or deletion guarantees.

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

## Promotion gate

P2 may be described as PostgreSQL-integrated only after exact PostgreSQL 16/18 integration runs are recorded. All 72 registry assertions remain runtime `UNSUPPORTED` until P4.
