# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-07  
**Last verified public `main`:** `4e6be77196c633c25dd3896660335c1448b2baf5`  
**Active branch / PR / issue:** `agent/p3-replay-projections` / #50 / #49  
**Repository status:** `RESEARCH / P3 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Re-check the branch ref, final PR head, workflows, review state and merge SHA.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
P3 INTEGRATION PASS ≠ COMPLETE KERNEL
P3 RECEIPT ≠ TRUTH / AUTHENTICITY / PHYSICAL ERASURE
IMPLEMENTED PROFILE ≠ ASSERTION-LEVEL CONFORMANCE
C1 ≠ C2 ≠ C3
```

## Operator gate

```text
RFC-0002:              ACCEPTED / APPROVED
P1 semantic core:      MERGED / REPOSITORY-TESTED
P2 PostgreSQL adapter: MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections: AUTHORIZED / PR #50 / REPOSITORY-INTEGRATION-TESTED
P4–P5:                 REQUIRE SEPARATE GO
Issue #1 / #18:        ACTIVE / INDEPENDENT
```

Decision evidence: Issue #49 and ADR-0017.

## P3 implementation route

```text
PostgreSQL authoritative history
→ repeatable-read snapshot
→ stored canonical/Event-chain verification
→ explicit UpcasterRegistry
→ P1 reducer from empty state
→ Replay Receipt
→ locked current-head comparison
→ disposable projection rebuild
→ Projection Rebuild Receipt
```

Key properties:

1. selected-instance Event count/max global sequence must equal the instance head;
2. every Event is loaded through P2 commitment verification;
3. `prev_global_hash` must form one chain from `GENESIS`;
4. reducer global/per-stream sequence rules remain active;
5. unknown schema versions require an explicit deterministic upcaster path;
6. projection publication fails if history advanced after replay;
7. Receipt and projection commit together;
8. injected precommit failure preserves the previous projection;
9. destroying a projection does not reset committed generation lineage;
10. Receipt overclaims are forbidden in Python models and SQL constraints.

## Initial repository evidence

Executable head: `0f8fd4ffe5d5fb0d4bc01f3e441a053f691dbba3`.

```text
P3 run 31171581859 — PASS
3.11 / PG16 — PASS
3.11 / PG18 — PASS
3.12 / PG16 — PASS
3.12 / PG18 — PASS
P2 regression run 31171581795 — PASS
P1 semantic core run 31171581787 — PASS
Fixture integrity run 31171581791 — PASS
```

Each P3 job passed 5 semantic tests, 5 manifest tests, 7 PostgreSQL integration scenarios, P2 regression tests and compileall.

A final affected-head run remains required after documentation and manifest evidence changes.

## Evidence boundary

```text
P3 replay/projection integration: REPOSITORY_REPRODUCED
Kernel runtime conformance:       UNSUPPORTED
C1/C2/C3:                         NOT_ESTABLISHED
```

P3 does not implement physical/cryptographic deletion, network API, P4 assertion-scoped conformance, P5 SQLite, production guarantees or ecosystem wiring.

All 72 assertion statuses remain `UNSUPPORTED` until P4.

## Next gates

1. finish bilingual RFC/README and AI continuity synchronization;
2. run P3 and AI-context checks on one final exact PR head;
3. inspect full diff, comments and review threads;
4. squash-merge only with P4/P5 and ecosystem scope absent;
5. record final main/merge/run evidence in GitHub and Notion;
6. close Issue #49 and keep P4 blocked pending separate GO.
