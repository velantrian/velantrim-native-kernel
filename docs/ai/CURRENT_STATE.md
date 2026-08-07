# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-07  
**Last verified public `main`:** `4af642930e18752f8f8b0bce75df355f76100d6f`  
**P3 merge:** PR #50 / `4af642930e18752f8f8b0bce75df355f76100d6f`  
**Checkpoint branch:** `agent/p3-post-merge-checkpoint`  
**Repository status:** `RESEARCH / P3 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Re-check exact refs and workflow evidence after later changes.

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
P3 replay/projections: MERGED / REPOSITORY-INTEGRATION-TESTED
P4–P5:                 REQUIRE SEPARATE GO
Issue #1 / #18:        ACTIVE / INDEPENDENT
```

Decision and implementation evidence: Issue #49, ADR-0017 and PR #50.

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
→ linked Receipt consistency verification
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
10. projection load verifies its linked rebuild Receipt;
11. Receipt overclaims are forbidden in Python models and SQL constraints.

## Final repository evidence

Final PR head: `7e615bc633cbf966211d3b2815f51b8ff9eb9716`.

```text
P3 run 31173133661 — PASS
3.11 / PG16 — PASS
3.11 / PG18 — PASS
3.12 / PG16 — PASS
3.12 / PG18 — PASS
P2 regression run 31173133709 — PASS
P1 semantic core run 31173133657 — PASS
Fixture integrity run 31173133713 — PASS
AI context run 31173133635 — PASS
```

Each P3 job passed 5 semantic tests, 5 manifest/anti-overclaim tests, 8 PostgreSQL integration scenarios, P2 regression tests and compileall.

The squash merge is `4af642930e18752f8f8b0bce75df355f76100d6f`. No push-to-main workflow run was recorded for that SHA; this remains `NOT_RECORDED`, not PASS.

## Evidence boundary

```text
P3 replay/projection integration: REPOSITORY_REPRODUCED
Kernel runtime conformance:       UNSUPPORTED
C1/C2/C3:                         NOT_ESTABLISHED
```

P3 does not implement physical/cryptographic deletion, network API, P4 assertion-scoped conformance, P5 SQLite, production guarantees or ecosystem wiring.

All 72 assertion statuses remain `UNSUPPORTED` until P4.

## Next gates

1. validate and merge the post-merge continuity checkpoint;
2. synchronize exact main/checkpoint evidence to Notion;
3. close Issue #49 for the completed bounded P3 scope;
4. require a new operator decision before P4;
5. preserve Issue #1 source recovery and Issue #18 licensing as independent work.