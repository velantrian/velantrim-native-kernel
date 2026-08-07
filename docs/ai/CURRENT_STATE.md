# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-07  
**Last verified public `main`:** `bb94835ad612f45e2629655bc9add872d8981357`  
**Active branch / PR:** `agent/p2-postgresql-append` / #47  
**Active issue:** #46  
**Repository status:** `RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Verify exact final PR head, review state and merge SHA.

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
P2 PostgreSQL adapter: AUTHORIZED / REPOSITORY-TESTED
P3–P5:                 REQUIRE SEPARATE GO
Issue #1 / #18:        ACTIVE / INDEPENDENT
```

Decision evidence: Issue #46 and ADR-0016.

## P2 implementation

```text
native_kernel.postgresql_profile
PostgreSQL 16–18
Psycopg >=3.3,<3.4
Python >=3.11,<3.13
```

Components:

1. lazy driver boundary;
2. checksum-locked migrations;
3. Kernel instance and rollback-safe history head;
4. writer owner/epoch/expiry fence;
5. atomic Event/idempotency transaction;
6. scoped idempotency `(instance, command contract, key)`;
7. rollback-safe global/stream counters;
8. canonical payload/envelope storage and `nkp1`/`nke1` commitments;
9. corruption checks for idempotent original-result reads;
10. P2 manifest/validator and declared repository matrix.

## Repository evidence

Evidence head: `e80492bcacde2ff2be3a2ee03aa5aa53a714d288`.

```text
P2 run 31151297646 — PASS
3.11 / PG16 — PASS
3.11 / PG18 — PASS
3.12 / PG16 — PASS
3.12 / PG18 — PASS
AI context run 31151298002 — PASS
P1 semantic core run 31151297696 — PASS
Fixture integrity run 31151298177 — PASS
```

Each P2 job passed 9 unit tests, 5 PostgreSQL integration tests, 5 manifest tests, validator and compileall.

```text
P2 PostgreSQL integration: REPOSITORY_REPRODUCED
Kernel runtime conformance: UNSUPPORTED
C1/C2/C3:                  NOT_ESTABLISHED
```

## Boundaries

P2 does not provide projections/rebuild, replay/upcasters, operational Receipts, deletion execution, network API, P4 conformance, P5 SQLite, production guarantees or ecosystem wiring.

`profile-manifest.json`, `p1-manifest.json` and `p2-manifest.json` are distinct phase records. All 72 assertion statuses remain `UNSUPPORTED` until P4.

## Next gates

1. run all checks on the final documentation/evidence head;
2. inspect full diff and review threads;
3. merge only with no P3/P4/P5 or ecosystem drift;
4. record exact merge and post-merge workflow evidence;
5. keep P3 blocked pending separate GO.
