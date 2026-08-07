# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-07  
**Last verified public `main`:** `1dc493e9d23b99ee4bbf6015348599cd56f6cb56`  
**Active branch / PR / issue:** `agent/p5-sqlite-c3` / #59 / #58  
**Repository status:** `RESEARCH / P5 PARTIAL CROSS-PROFILE CONFORMANCE / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Re-check the branch ref, workflows, artifact state, reviews and merge SHA.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
C2 ≠ C3
C3 SUPPORTED ASSERTIONS ≠ SUPPORT FOR ALL 72
C3 SEMANTIC EQUIVALENCE ≠ OPERATIONAL EQUIVALENCE
ASSERTION EVIDENCE ≠ TRUTH / AUTHENTICITY / PHYSICAL ERASURE
```

## Operator gate

```text
RFC-0002:              ACCEPTED / APPROVED
P1 semantic core:      MERGED / REPOSITORY-TESTED
P2 PostgreSQL adapter: MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections: MERGED / REPOSITORY-INTEGRATION-TESTED
P4 conformance:        MERGED / PARTIAL / POSTGRESQL C2
P5 SQLite/C3:          AUTHORIZED / IMPLEMENTED / PREVIOUS-HEAD EVIDENCE
C4/C5/production:      NOT AUTHORIZED / NOT ESTABLISHED
Issue #1 / #18:        ACTIVE / INDEPENDENT
```

Decision and implementation records: Issue #58, ADR-0019, PR #59 and `P5_IMPLEMENTATION_RECORD.md`.

## Profile map

```text
PostgreSQL reference  native-kernel/postgresql-reference@0.4-p4
SQLite embedded      native-kernel/sqlite-embedded@0.5-p5
```

The SQLite profile is independent: it uses stdlib `sqlite3`, its own migrations, tables, transactions, append/replay/projection/Receipt code and exact-history import path.

## Result maps

PostgreSQL/SQLite single-profile C2:

```text
41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
```

Cross-profile C3:

```text
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state: PARTIAL
```

Cross-profile evidence promotes only:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## C3 comparison route

```text
same accepted contracts
→ independent PostgreSQL execution
→ independent SQLite execution
→ normalized Event/outcome comparison
→ reducer/projection/Receipt comparison
→ exact PostgreSQL Event import into SQLite
→ BYTE / STRUCTURAL / SEMANTIC / BEHAVIOURAL checks
→ 72 assertion results
→ nk-equivalence-report/1
```

## Initial exact evidence

```text
Evidence head: d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
P5/C3 run:    31181341275 — PASS
P4 run:       31181341370 — PASS
P1 run:       31181341405 — PASS
Fixtures:     31181340889 — PASS
Artifacts:    4 archives × 3 JSON reports
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

One artifact was downloaded and inspected. It contained all three expected reports; C3 was bound to the exact SHA/run/environment, covered all 72 IDs with `45/10/17/0`, and all eight comparison checks were `PASS`.

## Evidence meaning

```text
SQLite C2:       REPOSITORY_REPRODUCED for 41 SUPPORTED assertions
Cross-profile C3: REPOSITORY_REPRODUCED for 45 SUPPORTED assertions
C4/C5:           NOT_ESTABLISHED
```

C3 does not apply to the 10 `PARTIAL` or 17 `UNSUPPORTED` comparison results.

## Explicitly absent

- exhaustive equivalence proof;
- operational equivalence between PostgreSQL and SQLite;
- complete conflict subsystem;
- physical/cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- truth/signature/notarization certification;
- network API;
- C4/C5 and production guarantees;
- Titan, Mentaury or Crystal runtime wiring;
- historical `v0.1.2.1` recovery.

## Current finalization gates

1. complete GitHub and Notion P5 documentation synchronization;
2. repeat P5/C3, P4, P1, fixture and AI-context checks on one final exact PR head;
3. verify four final-head artifacts and inspect one archive;
4. inspect full diff, comments, reviews and unresolved threads;
5. merge only with C4/C5/deletion/production/ecosystem scope absent;
6. publish post-merge continuity evidence and close Issue #58;
7. require separate operator GO before any later phase or operational claim.
