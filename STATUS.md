# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `4af642930e18752f8f8b0bce75df355f76100d6f`  
> **Published implementation:** PR #50 / Issue #49 / ADR-0017  
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

PostgreSQL, Psycopg, Python modules, SQL tables, JSONB, locks and isolation levels remain replaceable Implementation Profile technologies, not Architecture Canon.

## P3 implemented scope

```text
authoritative PostgreSQL Events
→ repeatable-read selected-instance snapshot
→ canonical payload/envelope verification
→ Event count, global/stream sequence and hash-chain verification
→ explicit deterministic UpcasterRegistry
→ P1 reducer from empty state
→ bounded persisted Replay Receipt
→ locked authoritative-head comparison
→ disposable projection rebuild
→ bounded persisted Projection Rebuild Receipt
→ projection-to-rebuild-Receipt linkage verification
```

Implemented and repository-tested:

- identity and multi-step upcaster routing;
- missing, duplicate, cyclic and invalid path failure;
- canonical semantic-state decoding;
- full selected-instance replay from global sequence `1`;
- P2 stored-event commitment validation during replay;
- global and per-stream sequence validation;
- `GENESIS → nke1` global hash-chain validation;
- disposable projection persistence, read, destroy and rebuild;
- monotonic projection generation through committed rebuild Receipts;
- stale-head rejection before projection publication;
- transactional rollback for Receipt/projection publication faults;
- canonical `REPLAY` and `PROJECTION_REBUILD` Receipts;
- projection/Receipt linkage validation;
- Event, projection and Receipt corruption detection;
- hard non-claims for truth, external authenticity, complete integrity, physical erasure and C-levels.

## Final PR evidence

```text
PR #50 final head: 7e615bc633cbf966211d3b2815f51b8ff9eb9716
Squash merge:      4af642930e18752f8f8b0bce75df355f76100d6f
Changed files:     35
Behind base:       0
```

Final-head workflows:

```text
P3 replay/projection: 31173133661 — PASS
P2 regression:        31173133709 — PASS
P1 semantic core:     31173133657 — PASS
Fixture integrity:    31173133713 — PASS
AI context:           31173133635 — PASS
```

P3 matrix:

```text
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
```

Each P3 matrix job passed 5 semantic tests, 5 manifest tests and validator, 8 unique PostgreSQL P3 integration tests, the P2 unit/integration regression suite and compileall.

No push-to-main workflow run was recorded for merge `4af64293…`; this is `NOT_RECORDED`, not a failure and not an additional PASS.

## Evidence boundary

```text
P3 replay/projection integration: REPOSITORY_REPRODUCED
Kernel runtime conformance:       UNSUPPORTED
C1/C2/C3:                         NOT_ESTABLISHED
```

P3 Receipts prove only their declared selected-instance replay/rebuild operation and checks. They do not establish truth, external authenticity, complete Event Integrity, physical deletion, production durability, security, privacy or compliance.

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

1. publish and merge this documentation-only P3 checkpoint;
2. synchronize final main/merge/run evidence to Notion;
3. close Issue #49 as completed P3 scope;
4. keep physical deletion, P4 and P5 blocked until separate operator decisions;
5. preserve Issue #1 and Issue #18 as independent gates.
