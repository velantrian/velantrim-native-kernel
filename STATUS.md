# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `4af642930e18752f8f8b0bce75df355f76100d6f`  
> **P3 merge:** PR #50 / `4af642930e18752f8f8b0bce75df355f76100d6f`  
> **Checkpoint branch:** `agent/p3-post-merge-checkpoint`  
> **Repository status:** `RESEARCH / P3 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

## Current profile

```text
Profile ID:       native-kernel/postgresql-reference
Profile version:  0.3-p3
Evidence lineage: clean/postgresql-reference/0.1
P1:               MERGED / REPOSITORY-TESTED
P2:               MERGED / REPOSITORY-INTEGRATION-TESTED
P3:               MERGED / REPOSITORY-INTEGRATION-TESTED
P4–P5:            NOT AUTHORIZED
```

PostgreSQL, Psycopg, Python modules, SQL tables and locks remain replaceable Implementation Profile technologies, not Architecture Canon.

## P3 implementation

```text
authoritative PostgreSQL Events
→ repeatable-read snapshot
→ canonical payload/envelope verification
→ Event count, sequence and global hash-chain verification
→ explicit deterministic upcaster registry
→ P1 reducer from empty state
→ bounded persisted Replay Receipt
→ locked authoritative-head comparison
→ disposable projection rebuild
→ bounded persisted Projection Rebuild Receipt
→ projection-to-Receipt consistency verification
```

Implemented:

- explicit identity and multi-step upcaster routing;
- failure on missing, duplicate, cyclic or invalid upcaster paths;
- canonical semantic-state decoding;
- full selected-instance replay from global sequence `1`;
- P2 stored-event commitment verification during replay;
- reducer global/per-stream sequence verification;
- disposable projection persistence, read, destroy and rebuild;
- monotonic generation through committed rebuild Receipts;
- stale-head rejection before projection publication;
- transactional rollback for Receipt/projection publication faults;
- canonical `REPLAY` and `PROJECTION_REBUILD` Receipts;
- projection rows verified against their linked rebuild Receipt;
- Receipt non-claims for truth, external authenticity, complete integrity, physical erasure and C-levels.

## Repository evidence

Final PR head:

```text
Head:          7e615bc633cbf966211d3b2815f51b8ff9eb9716
P3 run:        31173133661 — PASS
P2 regression: 31173133709 — PASS
P1 core:       31173133657 — PASS
Fixtures:      31173133713 — PASS
AI context:    31173133635 — PASS
```

P3 matrix:

```text
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
```

Every P3 matrix job passed 5 semantic tests, 5 manifest/anti-overclaim tests, 8 PostgreSQL integration scenarios, P2 regression tests and compileall.

No push-to-main workflow run was recorded for merge `4af64293…`; this is `NOT_RECORDED`, not PASS.

## Evidence boundary

```text
P3 replay/projection integration: REPOSITORY_REPRODUCED
Kernel runtime conformance:       UNSUPPORTED
C1/C2/C3:                         NOT_ESTABLISHED
```

P3 Receipts prove only their declared selected-instance snapshot/rebuild operation and checks. They do not establish truth, external authenticity, complete Event Integrity, physical deletion, production durability, security, privacy or compliance.

## Explicitly absent

- physical or cryptographic deletion execution;
- provider/backup/export/log/key erasure evidence;
- network API;
- P4 complete assertion-scoped conformance adapter;
- P5 independent SQLite profile;
- C1/C2/C3;
- package publication decision under Issue #18;
- Titan, Mentaury or Crystal runtime wiring;
- production credentials, HA, backup, restore or compliance guarantees.

All 72 registry assertions remain runtime `UNSUPPORTED` until P4.

## Issue #1 boundary

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 remains active and independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## Next gates

1. merge the post-merge continuity checkpoint after AI-context validation;
2. synchronize final merge/checkpoint evidence to Notion;
3. close Issue #49 as completed for the bounded P3 scope;
4. require separate operator GO before P4;
5. preserve Issues #1 and #18 as independent gates.