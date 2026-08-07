# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `bb94835ad612f45e2629655bc9add872d8981357`  
> **Active branch:** `agent/p2-postgresql-append` — verify exact PR head  
> **Active issue:** #46  
> **Repository status:** `RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

## Current profile

```text
Profile ID:       native-kernel/postgresql-reference
Profile version:  0.2-p2
Evidence lineage: clean/postgresql-reference/0.1
P1:               MERGED
P2:               AUTHORIZED / ACTIVE BRANCH
P3–P5:            NOT AUTHORIZED
```

PostgreSQL and Psycopg remain replaceable Implementation Profile technologies, not Architecture Canon.

## P2 implemented scope

`native_kernel.postgresql_profile` contains:

- lazy Psycopg connection boundary;
- numbered SQL migrations with SHA-256 ledger and advisory-lock serialization;
- Kernel instance registration;
- DB-backed writer owner/epoch lease;
- stale/expired writer fencing;
- atomic Event and idempotency persistence;
- same-key/same-digest original-result return;
- conflicting-key rejection;
- rollback-safe global and stream counters;
- canonical payload and envelope bytes;
- `nkp1` payload commitment and `nke1` global chain;
- corruption checks when loading an idempotent original result.

Profile choices:

```text
PostgreSQL compatibility: 16–18
CI matrix:                16 and 18
Python:                   >=3.11,<3.13
P2 driver:                psycopg >=3.3,<3.4
Migration framework:      numbered plain SQL
```

## Evidence

Available local evidence:

```text
9 P2 unit tests PASS
5 P2 manifest tests PASS
P2 manifest validator PASS
compileall PASS
5 PostgreSQL integration tests DECLARED / SKIPPED — no local DSN
local interpreter Python 3.13.5
repository CI NOT_RECORDED
```

Required interpretation:

```text
unit/manifest PASS
≠ PostgreSQL integration PASS
≠ replay/projection runtime
≠ assertion-level conformance
≠ C1/C2/C3
≠ production guarantee
```

All 72 registry assertions remain runtime `UNSUPPORTED` until P4.

## Explicitly absent

- P3 projections, rebuild and replay/upcasters;
- operational replay/deletion Receipts;
- byte/key/backup deletion execution;
- network API;
- P4 conformance adapter;
- P5 SQLite profile;
- C1/C2/C3;
- packaging/publication decision under Issue #18;
- Titan, Mentaury or Crystal runtime wiring;
- production credentials, HA, backup, restore, security, privacy or compliance guarantees.

## Issue #1 boundary

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 remains active and independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## Next gates

1. run exact PostgreSQL 16/18 × Python 3.11/3.12 repository integration matrix;
2. review and merge P2 only if the storage scope remains bounded;
3. synchronize exact PR/merge/run evidence to GitHub and Notion;
4. keep P3 blocked until separate operator GO;
5. preserve Issue #1 and Issue #18 as independent gates.
