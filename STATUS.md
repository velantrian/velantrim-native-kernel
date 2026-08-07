# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `a8bb0ae232b977856730a1a4f21f977c1f69ca0a`  
> **Published implementation:** PR #59 / Issue #58 / ADR-0019  
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
P5: MERGED / PARTIAL / SQLITE C2 + CROSS-PROFILE C3 REPOSITORY-REPRODUCED
C4/C5: NOT AUTHORIZED / NOT ESTABLISHED
```

PostgreSQL, SQLite, Psycopg, Python, SQL layouts, files and lock primitives remain replaceable Implementation Profile technologies, not Architecture Canon.

## Assertion-scoped result maps

Single-profile PostgreSQL and SQLite C2:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

PostgreSQL↔SQLite C3:

```text
SUPPORTED:   45
PARTIAL:     10
UNSUPPORTED: 17
FAILED:       0
TOTAL:       72
support_state: PARTIAL
```

Cross-profile evidence promotes exactly `NK-SEM-008`, `NK-ID-008`, `NK-EQV-002` and `NK-EQV-003`. All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

```text
C3 for 45 SUPPORTED assertions
≠ support for all 72
≠ PostgreSQL/SQLite operational equivalence
≠ truth/authenticity
≠ physical deletion
≠ production readiness
```

## Published implementation

```text
PR #59 final head:
6483c9a229aea7d49929745b7652e67f1c39949c

PR #59 squash merge / verified main:
a8bb0ae232b977856730a1a4f21f977c1f69ca0a
```

P5 independently implements SQLite migrations, `BEGIN IMMEDIATE` serialization, writer fencing, idempotent append, rollback-safe ordering, Event commitments/hash chain, replay, projection rebuild, bounded Receipts, corruption/stale-head rejection and exact PostgreSQL authoritative-history import.

## Main-push evidence

```text
P5/C3:     31183074126 — PASS
P4:        31183074048 — PASS
P1:        31183073948 — PASS
Fixtures:  31183073969 — PASS
AI context:31183073997 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Each of four main-bound artifacts contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
```

```text
py3.11/pg16 sha256:ca509f6fe9c1bb56c904399e7e6b60e2c743682aa8af21b006b1d1d5bcb6ea4c
py3.11/pg18 sha256:728bcb72a414b3c342e4ed03309593db5c0322e145a7dfc4c5d1834650fa422c
py3.12/pg16 sha256:a0c99b14a27f241dba7b6f37e45e80c592d25e0fae42934fab654a6430fc2d35
py3.12/pg18 sha256:2264682a85720db3c0512fa75466016466b54abb1e0a99274b9f2f99dc2274fb
```

Artifacts are retained until 2026-09-06. One main-bound archive was downloaded and inspected: all three reports were present; C3 was bound to `a8bb0ae2…` / run `31183074126`, covered all 72 IDs with `45/10/17/0`, and all eight comparison checks passed.

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
- package-publication decision under Issue #18.

## Issue #1 boundary

```text
clean/postgresql-reference/0.1 + clean/sqlite-embedded/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 remains active and independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## Next gate

P5 implementation work is complete. The docs-only continuity checkpoint and Notion synchronization remain in this publication cycle. Any C4, C5, production, deletion-execution or ecosystem-integration work requires a new explicit operator GO.
