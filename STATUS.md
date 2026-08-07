# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `4e6be77196c633c25dd3896660335c1448b2baf5`  
> **Active branch / PR / issue:** `agent/p3-replay-projections` / #50 / #49  
> **Repository status:** `RESEARCH / P3 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

## Current profile

```text
Profile ID:       native-kernel/postgresql-reference
Profile version:  0.3-p3
Evidence lineage: clean/postgresql-reference/0.1
P1:               MERGED / REPOSITORY-TESTED
P2:               MERGED / REPOSITORY-INTEGRATION-TESTED
P3:               AUTHORIZED / REPOSITORY-INTEGRATION-TESTED / PR OPEN
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
- Receipt non-claims for truth, external authenticity, complete integrity, physical erasure and C-levels.

## Repository evidence

Initial executable PR head:

```text
Head:          0f8fd4ffe5d5fb0d4bc01f3e441a053f691dbba3
P3 run:        31171581859 — PASS
P2 regression: 31171581795 — PASS
P1 core:       31171581787 — PASS
Fixtures:      31171581791 — PASS
```

P3 matrix:

```text
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
```

Every P3 matrix job passed 5 semantic tests, 5 manifest tests, 7 PostgreSQL integration scenarios, P2 regression tests and compileall.

The final PR head must repeat affected workflows after documentation/evidence updates. The initial PASS remains evidence only for its exact SHA.

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

1. complete exact final-head P3, P2, P1, fixture and AI-context checks;
2. inspect PR #50 full diff, comments and review threads;
3. merge only with P4/P5, physical deletion and ecosystem scope absent;
4. synchronize final PR/merge/run evidence to GitHub and Notion;
5. require separate operator GO before P4.
