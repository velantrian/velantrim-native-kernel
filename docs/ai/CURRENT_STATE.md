# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-07  
**Last verified public `main`:** `113452a365890bf6c143d76657b810be59530ed4`  
**Latest implementation:** PR #47 — P2 PostgreSQL authoritative append/idempotency  
**Repository status:** `RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Re-check repository ref, exact workflow evidence and later PRs.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
P2 INTEGRATION PASS ≠ REPLAY/PROJECTION RUNTIME
IMPLEMENTED PROFILE ≠ ASSERTION-LEVEL CONFORMANCE
C1 ≠ C2 ≠ C3
```

## Operator gate

```text
RFC-0002:              ACCEPTED / APPROVED
P1 semantic core:      MERGED
P2 PostgreSQL adapter: AUTHORIZED / MERGED / REPOSITORY-TESTED
P3–P5:                 REQUIRE SEPARATE GO
Issue #1 / #18:        ACTIVE / INDEPENDENT
```

## Exact P2 publication

```text
PR:             #47
Base main:      bb94835ad612f45e2629655bc9add872d8981357
Final PR head:  36ddb1d0342914f0c06fe7f31171bac06565ee72
Merge SHA:      113452a365890bf6c143d76657b810be59530ed4
Changed files:  31
Review threads: 0 unresolved
Reviews:        0
Codex review:   unavailable due external usage limit
```

## Repository evidence

```text
P2 run 31152380799 — PASS
3.11 / PG16 — PASS
3.11 / PG18 — PASS
3.12 / PG16 — PASS
3.12 / PG18 — PASS
AI context run 31152380802 — PASS
P1 semantic core run 31152380832 — PASS
Fixture integrity run 31152380800 — PASS
```

Every P2 matrix job passed 9 unit tests, 5 PostgreSQL integration tests, 5 manifest tests, validator and compileall.

No push-to-main workflow run was created for merge `113452a3…`; this remains `NOT_RECORDED` and does not negate the exact final-head PR evidence.

## Merged P2 package

```text
native_kernel.postgresql_profile
PostgreSQL 16–18
Psycopg >=3.3,<3.4
Python >=3.11,<3.13
```

Implemented components:

1. lazy driver boundary;
2. checksum-locked migrations;
3. Kernel instance and rollback-safe history head;
4. writer owner/epoch/expiry fence;
5. atomic Event/idempotency transaction;
6. scoped idempotency `(instance, command contract, key)`;
7. rollback-safe global/stream counters;
8. canonical payload/envelope storage and `nkp1`/`nke1` commitments;
9. corruption checks for original-result reads.

## Evidence boundary

```text
P2 PostgreSQL integration: REPOSITORY_REPRODUCED
Kernel runtime conformance: UNSUPPORTED
C1/C2/C3:                  NOT_ESTABLISHED
```

P2 does not provide projections/rebuild, replay/upcasters, operational Receipts, deletion execution, network API, P4 conformance, P5 SQLite, production guarantees or ecosystem wiring.

All 72 assertion statuses remain `UNSUPPORTED` until P4.

## Next gates

1. merge the post-P2 checkpoint;
2. synchronize final GitHub evidence to Notion;
3. close Issue #46 as completed P2 scope;
4. keep P3 blocked pending separate GO;
5. preserve Issue #1 and Issue #18 independently.
