# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-07  
**Last verified public `main`:** `a8bb0ae232b977856730a1a4f21f977c1f69ca0a`  
**Published issue / PR / ADR:** #58 / #59 / ADR-0019  
**Repository status:** `RESEARCH / P5 PARTIAL CROSS-PROFILE CONFORMANCE / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Re-check the actual branch ref, workflows, artifact state and later checkpoint merge.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
C2 ≠ C3
C3 SUPPORTED ASSERTIONS ≠ SUPPORT FOR ALL 72
C3 SEMANTIC EQUIVALENCE ≠ OPERATIONAL EQUIVALENCE
ASSERTION EVIDENCE ≠ TRUTH / AUTHENTICITY / PHYSICAL ERASURE
```

## Published gate

```text
RFC-0002:              ACCEPTED / APPROVED
P1 semantic core:      MERGED / REPOSITORY-TESTED
P2 PostgreSQL adapter: MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections: MERGED / REPOSITORY-INTEGRATION-TESTED
P4 conformance:        MERGED / PARTIAL / POSTGRESQL C2
P5 SQLite/C3:          MERGED / PARTIAL / REPOSITORY-REPRODUCED
C4/C5/production:      NOT AUTHORIZED / NOT ESTABLISHED
Issue #1 / #18:        ACTIVE / INDEPENDENT
```

## Profile and result map

```text
PostgreSQL  native-kernel/postgresql-reference@0.4-p4
SQLite      native-kernel/sqlite-embedded@0.5-p5
```

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state:     PARTIAL
```

C3 promotions are limited to:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## Publication evidence

```text
PR #59 final head: 6483c9a229aea7d49929745b7652e67f1c39949c
PR #59 merge/main: a8bb0ae232b977856730a1a4f21f977c1f69ca0a

P5/C3 main run: 31183074126 — PASS
P4 main run:    31183074048 — PASS
P1 main run:    31183073948 — PASS
Fixture run:    31183073969 — PASS
AI-context run: 31183073997 — PASS
```

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Four main-bound artifacts are retained until 2026-09-06; each contains PostgreSQL P4, SQLite P5 and C3 reports. One archive was independently inspected and contained all 72 results plus eight passed comparison checks.

## Evidence meaning

```text
SQLite C2:        REPOSITORY_REPRODUCED for 41 SUPPORTED assertions
Cross-profile C3: REPOSITORY_REPRODUCED for 45 SUPPORTED assertions
C4/C5:            NOT_ESTABLISHED
```

C3 does not apply to the 10 `PARTIAL` or 17 `UNSUPPORTED` comparison results.

## Explicitly absent

- exhaustive equivalence proof;
- PostgreSQL/SQLite operational equivalence;
- complete conflict subsystem;
- physical/cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- truth/signature/notarization certification;
- network API;
- C4/C5 and production guarantees;
- Titan, Mentaury or Crystal runtime wiring;
- historical `v0.1.2.1` recovery.

## Next action

Complete the docs-only checkpoint, synchronize Notion and close Issue #58. Any later phase or operational claim requires a new explicit operator authorization.
