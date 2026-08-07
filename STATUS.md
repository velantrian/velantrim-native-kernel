# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `113452a365890bf6c143d76657b810be59530ed4`  
> **Repository status:** `RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`  
> **Current phase:** `P2 MERGED / REPOSITORY-INTEGRATION-TESTED`

## Current profile

```text
Profile ID:       native-kernel/postgresql-reference
Profile version:  0.2-p2
Evidence lineage: clean/postgresql-reference/0.1
P1:               MERGED
P2:               MERGED / REPOSITORY-INTEGRATION-TESTED
P3–P5:            NOT AUTHORIZED
```

PostgreSQL and Psycopg remain replaceable Implementation Profile technologies, not Architecture Canon.

## P2 publication evidence

```text
PR:             #47
Final PR head:  36ddb1d0342914f0c06fe7f31171bac06565ee72
Merge SHA:      113452a365890bf6c143d76657b810be59530ed4
Merge method:   squash
Changed files:  31
Review threads: 0 unresolved
Reviews:        0
Codex review:   unavailable due external usage limit
```

Final-head workflows:

```text
P2 run 31152380799 — PASS
AI context run 31152380802 — PASS
P1 semantic core run 31152380832 — PASS
Fixture integrity run 31152380800 — PASS
```

P2 matrix:

```text
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
```

Every P2 job passed 9 unit tests, 5 PostgreSQL integration tests, 5 manifest tests, validator and compileall.

No push-to-main workflow run was recorded for merge `113452a3…`.

## Implemented P2 scope

- lazy Psycopg boundary;
- checksum-locked migrations with advisory-lock serialization;
- Kernel instance registration;
- DB-backed writer owner/epoch/expiry lease;
- stale/expired writer fencing;
- atomic Event/idempotency persistence;
- same-key/same-digest original-result return;
- conflicting-key rejection;
- rollback-safe global and stream counters;
- canonical payload/envelope bytes;
- `nkp1` payload commitment and `nke1` global chain;
- stored-event consistency checks.

## Evidence boundary

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

1. merge the post-P2 continuity checkpoint;
2. synchronize final main/evidence to Notion and close Issue #46;
3. keep P3 blocked until separate operator GO;
4. preserve Issue #1 and Issue #18 as independent gates;
5. keep all assertion-level runtime support `UNSUPPORTED` until P4.
