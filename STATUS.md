# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `bb94835ad612f45e2629655bc9add872d8981357`  
> **Active branch:** `agent/p2-postgresql-append` — verify exact PR head  
> **Active PR / issue:** #47 / #46  
> **Repository status:** `RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

## Current profile

```text
Profile ID:       native-kernel/postgresql-reference
Profile version:  0.2-p2
Evidence lineage: clean/postgresql-reference/0.1
P1:               MERGED
P2:               AUTHORIZED / REPOSITORY-INTEGRATION-TESTED
P3–P5:            NOT AUTHORIZED
```

PostgreSQL and Psycopg remain replaceable Implementation Profile technologies, not Architecture Canon.

## P2 implemented scope

`native_kernel.postgresql_profile` contains:

- lazy Psycopg boundary;
- checksum-locked migrations with advisory-lock serialization;
- Kernel instance registration;
- DB-backed writer owner/epoch lease;
- stale/expired writer fencing;
- atomic Event/idempotency persistence;
- same-key/same-digest original-result return;
- conflicting-key rejection;
- rollback-safe global and stream counters;
- canonical payload/envelope bytes;
- `nkp1` payload commitment and `nke1` global chain;
- stored-event consistency checks.

Profile choices:

```text
PostgreSQL compatibility: 16–18
CI matrix:                16 and 18
Python:                   >=3.11,<3.13
P2 driver:                psycopg >=3.3,<3.4
Migration framework:      numbered plain SQL
```

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

Every P2 job passed unit tests, five PostgreSQL integration tests, manifest guards and compileall.

```text
P2 PostgreSQL integration: REPOSITORY_REPRODUCED
Kernel runtime conformance: UNSUPPORTED
C1/C2/C3:                  NOT_ESTABLISHED
```

P2 evidence is bounded to append/idempotency, writer fencing, rollback and tested concurrency. It is not a complete Kernel/runtime promotion.

## Explicitly absent

- P3 projections/rebuild and replay/upcasters;
- operational replay/deletion Receipts;
- byte/key/backup deletion execution;
- network API;
- P4 conformance adapter;
- P5 SQLite profile;
- C1/C2/C3;
- packaging/publication decision under Issue #18;
- Titan, Mentaury or Crystal runtime wiring;
- production credentials, HA, backup, restore, security, privacy or compliance guarantees.

All 72 registry assertions remain runtime `UNSUPPORTED` until P4.

## Issue #1 boundary

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 remains active and independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## Next gates

1. complete exact final-head workflow and review inspection;
2. merge P2 only with P3/P4/P5 scope absent;
3. synchronize final PR/merge/run evidence to GitHub and Notion;
4. keep P3 blocked until separate operator GO;
5. preserve Issue #1 and Issue #18 as independent gates.
