# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-07  
**Last verified public `main`:** `4af642930e18752f8f8b0bce75df355f76100d6f`  
**Published PR / issue:** #50 / #49  
**Repository status:** `RESEARCH / P3 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Verify this recorded SHA against the actual branch before future work.

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

Decision evidence: Issue #49 and ADR-0017.

## P3 implementation route

```text
PostgreSQL authoritative history
→ repeatable-read snapshot
→ stored canonical/Event-chain verification
→ explicit UpcasterRegistry
→ P1 reducer from empty state
→ bounded Replay Receipt
→ locked current-head comparison
→ disposable projection rebuild
→ bounded Projection Rebuild Receipt
→ linked rebuild-Receipt verification
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
10. a loaded projection must match its linked rebuild Receipt;
11. Receipt overclaims are forbidden in Python models and SQL constraints.

## Final repository evidence

```text
PR #50 final head: 7e615bc633cbf966211d3b2815f51b8ff9eb9716
PR #50 merge:      4af642930e18752f8f8b0bce75df355f76100d6f
P3 run:            31173133661 — PASS
P2 run:            31173133709 — PASS
P1 run:            31173133657 — PASS
Fixtures run:      31173133713 — PASS
AI context run:    31173133635 — PASS
```

P3 matrix:

```text
3.11 / PG16 — PASS
3.11 / PG18 — PASS
3.12 / PG16 — PASS
3.12 / PG18 — PASS
```

Each matrix job passed 5 semantic tests, 5 manifest tests and validator, 8 unique PostgreSQL P3 integration tests, P2 regressions and compileall.

Review state before merge:

```text
unresolved review threads: 0
submitted reviews:          0
technical PR comments:      0
Codex review:               unavailable due usage limit
behind base:                0
```

No push-to-main workflow run was recorded for merge `4af64293…`; status is `NOT_RECORDED`.

## Evidence boundary

```text
P3 replay/projection integration: REPOSITORY_REPRODUCED
Kernel runtime conformance:       UNSUPPORTED
C1/C2/C3:                         NOT_ESTABLISHED
```

P3 does not implement physical/cryptographic deletion, network API, P4 assertion-scoped conformance, P5 SQLite, production guarantees or ecosystem wiring.

All 72 assertion statuses remain `UNSUPPORTED` until P4.

## Next gates

1. merge the P3 documentation checkpoint;
2. synchronize final checkpoint/main evidence to Notion;
3. close Issue #49 as completed;
4. keep P4/P5 and physical deletion blocked pending separate GO;
5. preserve Issue #1 and Issue #18 independence.
