# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `4f8cb0a8b7d9ca678a8578cf005b118fd6dff150`  
> **Active implementation:** Issue #55 / PR #56 / `agent/p4-conformance-adapter`  
> **Repository status:** `RESEARCH / P4 PARTIAL ASSERTION CONFORMANCE / NOT PRODUCTION-READY`

## Current profile

```text
Profile ID:       native-kernel/postgresql-reference
Profile version:  0.4-p4
Evidence lineage: clean/postgresql-reference/0.1
P1:               MERGED / REPOSITORY-TESTED
P2:               MERGED / REPOSITORY-INTEGRATION-TESTED
P3:               MERGED / REPOSITORY-INTEGRATION-TESTED
P4:               PARTIAL / C2 REPOSITORY-REPRODUCED ON PREVIOUS PR HEAD
P5:               NOT AUTHORIZED
```

PostgreSQL, Psycopg, Python modules, SQL tables, locks and current processors remain replaceable Implementation Profile technologies, not Architecture Canon.

## P4 assertion-scoped conformance

P4 adds an executable profile adapter for `nk-evidence-report/1`:

```text
72 registered assertion IDs
→ P1 semantic checks
→ P2 append/fencing checks
→ P3 replay/projection/Receipt checks
→ one explicit result per assertion
→ evidence/check references + limitations
→ strict independent validation
→ retained repository artifacts
```

Current conservative support map:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

All `NK-EPI-001…008` results remain `UNSUPPORTED`; ADR-0008 and the epistemic family remain `PROPOSED`.

## C1/C2 meaning

Conformance levels remain assertion-scoped.

```text
C1 / C2 applies only to results marked SUPPORTED
PARTIAL remains PARTIAL
UNSUPPORTED remains UNSUPPORTED
support_state remains PARTIAL
```

A top-level P4 `C2 / REPOSITORY_REPRODUCED` report means that the repository reproduced the 41 supported assertion results with exact code, environment, CI traceability and artifacts. It does not mean all 72 assertions are supported.

```text
P4 C2
≠ complete profile support
≠ C3 cross-profile equivalence
≠ accepted NK-EPI
≠ truth/authenticity certification
≠ physical deletion
≠ production readiness
```

## Initial P4 repository evidence

Exact executable/evidence head:

```text
93710131fffdea7d9a586cc05e7f258c07fae707
```

Workflow evidence:

```text
P4 run:      31175767586 — PASS
P1 run:      31175767587 — PASS
P2 run:      31175767636 — PASS
P3 run:      31175768175 — PASS
Fixtures:    31175767614 — PASS
```

P4 matrix:

```text
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
```

Every P4 matrix job passed:

- 5 assertion-mapping and traceability tests;
- 5 P4 manifest/anti-overclaim tests;
- one full PostgreSQL C1 report integration test;
- C2 report generation and strict validation;
- P1, P2 and P3 regressions;
- compileall;
- JSON artifact upload.

Four evidence artifacts are retained for 30 days and are bound to run `31175767586` and head `93710131…`.

The current documentation head is later than the executable evidence head. A final exact-head P4 and governance run remains required before merge.

## Implemented P1–P4 route

```text
semantic identity and authority                    ← P1
PostgreSQL append/idempotency/writer fencing       ← P2
persisted replay and disposable projections        ← P3
bounded operational Receipts                       ← P3
72-assertion evidence adapter and report validator ← P4
```

P4 does not add new authoritative storage semantics. It evaluates and reports existing bounded behavior against the accepted registry.

## Explicitly absent

- P5 independent SQLite profile;
- C3 cross-profile equivalence;
- dedicated conflict representation/resolution subsystem;
- physical or cryptographic deletion execution;
- provider/backup/export/log/key erasure evidence;
- restore-before-visibility deletion enforcement;
- cross-project authority adapter;
- network API;
- C4 shadow evaluation;
- C5 operational security/privacy/incident evidence;
- production credentials, HA, backup, restore or compliance guarantees;
- Titan, Mentaury or Crystal runtime wiring;
- package publication decision under Issue #18.

## Issue #1 boundary

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 remains active and independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## Current gates

1. finish GitHub and Notion P4 documentation synchronization;
2. run P4, P1, P2, P3, fixture and AI-context checks on one final exact PR head;
3. inspect PR #56 diff, comments, reviews and unresolved threads;
4. merge only with P5/C3/deletion/production/ecosystem scope absent;
5. record final PR head, merge SHA, runs and artifact state;
6. require separate operator GO before P5 or any C3 claim.
