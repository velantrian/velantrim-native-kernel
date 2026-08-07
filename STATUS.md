# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `1dc493e9d23b99ee4bbf6015348599cd56f6cb56`  
> **Active implementation:** Issue #58 / PR #59 / `agent/p5-sqlite-c3`  
> **Repository status:** `RESEARCH / P5 PARTIAL CROSS-PROFILE CONFORMANCE / NOT PRODUCTION-READY`

## Current profiles

```text
PostgreSQL profile: native-kernel/postgresql-reference@0.4-p4
Lineage:           clean/postgresql-reference/0.1

SQLite profile:    native-kernel/sqlite-embedded@0.5-p5
Lineage:           clean/sqlite-embedded/0.1
```

```text
P1: MERGED / REPOSITORY-TESTED
P2: MERGED / REPOSITORY-INTEGRATION-TESTED
P3: MERGED / REPOSITORY-INTEGRATION-TESTED
P4: MERGED / PARTIAL / POSTGRESQL C2 REPOSITORY-REPRODUCED
P5: IMPLEMENTED / PARTIAL / SQLITE C2 + CROSS-PROFILE C3 PREVIOUS-HEAD EVIDENCE
C4/C5: NOT AUTHORIZED / NOT ESTABLISHED
```

PostgreSQL, SQLite, Psycopg, Python, SQL layouts, files and lock primitives remain replaceable Implementation Profile technologies, not Architecture Canon.

## Assertion-scoped result maps

Single-profile PostgreSQL and SQLite C2 reports:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

PostgreSQL↔SQLite C3 comparison:

```text
SUPPORTED:   45
PARTIAL:     10
UNSUPPORTED: 17
FAILED:       0
TOTAL:       72
support_state: PARTIAL
```

C3 promotes exactly `NK-SEM-008`, `NK-ID-008`, `NK-EQV-002` and `NK-EQV-003` through passed cross-profile evidence. All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

```text
C3 for 45 SUPPORTED assertions
≠ support for all 72
≠ PostgreSQL/SQLite operational equivalence
≠ truth/authenticity
≠ physical deletion
≠ production readiness
```

## P5 architecture route

```text
accepted contracts + fixture pack
        ↓
PostgreSQL reference profile ───────────┐
                                       ├─→ declared equivalence checks
independent stdlib SQLite profile ──────┘
        ↓
BYTE / STRUCTURAL / SEMANTIC / BEHAVIOURAL
        ↓
72 explicit assertion results
        ↓
nk-equivalence-report/1 + retained artifacts
```

SQLite independently implements:

- migrations and instance registration;
- `BEGIN IMMEDIATE` single-writer serialization;
- owner/epoch/expiry fencing;
- durable idempotency and rollback-safe ordering;
- canonical Event commitments and hash-chain checks;
- replay, projection rebuild and bounded Receipts;
- stale-head and corruption rejection;
- exact PostgreSQL authoritative-history import.

## Initial P5 repository evidence

```text
Evidence head: d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
P5/C3 run:    31181341275 — PASS
P4 run:       31181341370 — PASS
P1 run:       31181341405 — PASS
Fixtures:     31181340889 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Four artifacts are retained for 30 days. Each contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
```

Artifact digests:

```text
py3.11/pg16 sha256:6e74f1be560afa54033beaa0c396d8395ed47d27ee89961746cda416e42cb8a5
py3.11/pg18 sha256:dec4f52dd6f7d6b6d71251bc9f931bcfc115ba65deae5a1ed888f77ea71ca680
py3.12/pg16 sha256:727b2a204035acb1d9fd116faecb284e8c8dda81722cb3646510cd1e779143bb
py3.12/pg18 sha256:705182b68f5806274723c43ea0d4c3cb1f240baf623db5260f151f24bacfea29
```

This is `PASS_PREVIOUS_HEAD`, not final-head evidence. Documentation/governance commits must repeat the matrix before merge.

## Explicitly absent

- exhaustive cross-profile state-space proof;
- PostgreSQL/SQLite operational equivalence;
- complete conflict representation/resolution;
- physical or cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- truth/signature/notarization certification;
- network API;
- C4 shadow evaluation;
- C5 operational security/privacy/incident evidence;
- production security, HA, backup, restore or compliance guarantees;
- Titan, Mentaury or Crystal runtime wiring;
- historical `v0.1.2.1` recovery;
- package publication decision under Issue #18.

## Issue #1 boundary

```text
clean/postgresql-reference/0.1 + clean/sqlite-embedded/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 remains active and independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## Next gate

1. finish GitHub and Notion P5 documentation synchronization;
2. repeat P5/C3, P4, P1, fixture and AI-context checks on one final exact PR head;
3. verify four final-head artifacts and inspect one archive;
4. review and merge PR #59 only with all non-goals preserved;
5. publish post-merge continuity evidence;
6. require a new explicit GO before C4, C5, production, deletion execution or ecosystem integration.
