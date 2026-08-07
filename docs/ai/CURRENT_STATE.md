# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-07  
**Last verified public `main`:** `bb94835ad612f45e2629655bc9add872d8981357`  
**Active branch:** `agent/p2-postgresql-append` — re-check exact PR head  
**Active issue:** #46 — PostgreSQL authoritative append/idempotency adapter  
**Repository status:** `RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Verify exact branch, PR, workflow runs and merge SHA.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
P2 CODE ≠ POSTGRESQL INTEGRATION EVIDENCE
DURABLE APPEND ≠ REPLAY/PROJECTION RUNTIME
IMPLEMENTED PROFILE ≠ ASSERTION-LEVEL CONFORMANCE
C1 ≠ C2 ≠ C3
```

## Operator gate

```text
RFC-0002:              ACCEPTED / APPROVED
P1 semantic core:      MERGED
P2 PostgreSQL adapter: GO / ACTIVE
P3–P5:                 REQUIRE SEPARATE GO
Issue #1:              ACTIVE / INDEPENDENT
Issue #18:             ACTIVE / INDEPENDENT
```

Decision evidence: Issue #46 and ADR-0016.

## Active P2 implementation

```text
native_kernel.postgresql_profile
PostgreSQL 16–18
Psycopg >=3.3,<3.4
Python >=3.11,<3.13
```

Components:

1. lazy driver boundary;
2. exact migration files and SHA-256 ledger;
3. Kernel instance row and rollback-safe history head;
4. one writer owner/epoch lease per instance;
5. atomic Event/idempotency transaction;
6. scoped idempotency `(instance, command contract, key)`;
7. rollback-safe global/stream counters;
8. canonical payload/envelope storage and `nkp1`/`nke1` commitments;
9. integration tests for migration, fencing, retry/conflict, rollback and concurrency;
10. P2 manifest/validator and PostgreSQL 16/18 workflow matrix.

## Evidence state

```text
P2 unit tests:                 9 PASS
P2 manifest tests:             5 PASS
manifest validator:            PASS
compileall:                    PASS
PostgreSQL integration tests:  5 DECLARED / NOT RUN NO DSN
repository workflow evidence:  NOT_RECORDED
Kernel runtime conformance:    UNSUPPORTED
C1/C2/C3:                      NOT_ESTABLISHED
```

The available local interpreter is Python 3.13.5, outside the declared profile range. It is not a substitute for Python 3.11/3.12 repository evidence.

## Boundaries

P2 does not provide projections/rebuild, replay/upcasters, deletion execution, network API, conformance adapter, C1/C2/C3, production guarantees or ecosystem wiring.

`profile-manifest.json`, `p1-manifest.json` and `p2-manifest.json` are separate historical/current phase records. All 72 assertion results remain `UNSUPPORTED` until P4.

## Next gates

1. verify complete branch diff and remote syntax;
2. open/review P2 PR;
3. inspect exact PostgreSQL 16/18 matrix results;
4. merge only with no P3/P4 drift;
5. finalize Notion and Issue #46 evidence;
6. keep P3 blocked pending separate GO.
