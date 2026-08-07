# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `b10be105743355a04e58611639a9d28faf7ea514`  
> **Current publication candidate:** PR #62 / Issue #61 / ADR-0020  
> **Repository status:** `RESEARCH / C4 PARTIAL OFFLINE SHADOW EVALUATION / NOT PRODUCTION-READY`

## Current phase

```text
P1: MERGED / REPOSITORY-TESTED
P2: MERGED / REPOSITORY-INTEGRATION-TESTED
P3: MERGED / REPOSITORY-INTEGRATION-TESTED
P4: MERGED / PARTIAL / POSTGRESQL C2 REPOSITORY-REPRODUCED
P5: MERGED / PARTIAL / SQLITE C2 + CROSS-PROFILE C3 REPOSITORY-REPRODUCED
C4: PR #62 OPEN / PARTIAL / OFFLINE RECORDED-WORKLOAD SHADOW EVIDENCE REPOSITORY-REPRODUCED
C5: NOT AUTHORIZED / NOT ESTABLISHED
```

C4 is an evidence layer over the existing profiles. It does not become an authoritative runtime, a storage profile, a deployment mode or an ecosystem authority.

## Profiles and lineages

```text
PostgreSQL profile: native-kernel/postgresql-reference@0.4-p4
Lineage:           clean/postgresql-reference/0.1

SQLite profile:    native-kernel/sqlite-embedded@0.5-p5
Lineage:           clean/sqlite-embedded/0.1

C4 evaluator:      native-kernel/c4-offline-shadow-v1
Dataset protocol:  nk-shadow-workload/1
Report protocol:   nk-shadow-report/1
Receipt protocol:  nk-shadow-receipt/1
```

PostgreSQL, SQLite, Python, Psycopg, SQL layouts, files, locks, CI runners and the current evaluator remain replaceable Implementation Profile technologies, not Architecture Canon.

## Assertion-scoped maps

Single-profile PostgreSQL and SQLite C2:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

PostgreSQL↔SQLite C3 and C4 shadow scope:

```text
SUPPORTED:   45
PARTIAL:     10
UNSUPPORTED: 17
FAILED:       0
TOTAL:       72
support_state: PARTIAL
```

C4 evaluates exactly the existing 45 C3-supported assertions. It does not promote the remaining 27 assertions. All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## C4 authority boundary

```text
mode:                  SHADOW_ONLY
authority promotion:   FORBIDDEN
authoritative writes:  FORBIDDEN
side effects:           FORBIDDEN
promotion decision:    NOT_AUTHORIZED
```

The evaluator accepts an explicitly approved, immutable recorded dataset and compares declared reference/candidate observations. It cannot append to Kernel history, mutate either storage profile, approve a candidate, trigger actions or connect itself to Titan, Mentaury or Crystal.

## Approved C4 dataset

```text
dataset_id:      native-kernel/c4-offline-shadow-v1
dataset_sha256:  15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:           15
assertion scope: 45 / 45 C3-supported assertions
approval:        ADR-0020 / Issue #61 / OFFLINE_RECORDED_WORKLOAD_ONLY
```

The dataset contains approved synthetic repository workloads. It is not captured production traffic.

## First repository C4 evidence

```text
Evidence head: 97abce685a68e24aec9afab451c009df5783b96b
C4 run:       31187532364 — PASS
P5/C3 run:    31187532391 — PASS
P4 run:       31187532618 — PASS
P1 run:       31187532346 — PASS
Fixtures:     31187532580 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Each artifact contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
c4-shadow-report.json
```

Artifact digests:

```text
py3.11/pg16 sha256:59cf39e6cbd3e8c95157676cc3fd838687d5911676b227681efd6c83a7f36e90
py3.11/pg18 sha256:9d4f828095285e479e1a95b87523fbaa800068f82a75cbbefb5f2d736e952032
py3.12/pg16 sha256:f85e29688a0176c168067fb8ed6f889550342c6faffcb4dc7d391715ea5364d4
py3.12/pg18 sha256:6892bc2ab7232c96124d4d207aacf06385f8b2ff6a3ea91097d1db6c2e834328
```

One archive was downloaded and inspected. The exact C4 report was bound to head `97abce68…`, run `31187532364`, Python 3.11, PostgreSQL 16 and SQLite 3.45.1. It contained:

```text
15 / 15 matched cases
15 Shadow Receipts
45 / 45 C3-supported assertion coverage
0 semantic divergences
0 critical divergences
0 missing Receipts
30 declared allowed operational differences
72 assertion results
status: PASS
support_state: PARTIAL
```

Artifacts are retained until 2026-09-06.

## What C4 proves

Within the approved dataset and declared comparison fields, the candidate observations matched the reference observations for canonical identity, authority denial, writer fencing, idempotency, ordering, Event integrity, replay, projection rebuild, conflict/source binding, failure semantics, state equivalence, Receipt proof boundaries, exact history import and report traceability.

Each `nk-shadow-receipt/1` proves only that one recorded case was compared by the offline evaluator under the recorded dataset digest and authority boundary.

## What C4 does not prove

```text
C4 offline shadow PASS
≠ live production shadowing
≠ authority promotion
≠ candidate approval
≠ exhaustive state-space equivalence
≠ PostgreSQL/SQLite operational equivalence
≠ all 72 assertions supported
≠ truth or external authenticity
≠ physical or cryptographic deletion
≠ C5 operational evidence
≠ production readiness
```

## Explicitly absent

- live traffic capture or production replay;
- authority promotion or automatic actions;
- complete conflict representation/resolution;
- physical or cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- truth/signature/notarization certification;
- network API;
- C5 security, privacy, incident, resilience or operational evidence;
- production security, HA, backup, restore or compliance guarantees;
- Titan, Mentaury or Crystal runtime wiring;
- historical `v0.1.2.1` recovery;
- package-publication decision under Issue #18.

## Historical P5 publication checkpoint

```text
PR #59 final head: 6483c9a229aea7d49929745b7652e67f1c39949c
PR #59 merge:      a8bb0ae232b977856730a1a4f21f977c1f69ca0a
PR #60 checkpoint: b10be105743355a04e58611639a9d28faf7ea514
```

P5 established independent SQLite C2 and partial PostgreSQL↔SQLite C3 with map `45/10/17/0`. C4 reuses that exact assertion boundary; it does not replace or broaden it.

## Issue boundaries

```text
clean/postgresql-reference/0.1
+ clean/sqlite-embedded/0.1
+ approved C4 recorded dataset
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 remains active and independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

Issue #18 remains independent. No package was published and no new external runtime dependency was introduced by C4.

## Next gate

Finish exact final-head C4 evidence, review and publication for PR #62, then merge and record a main-bound checkpoint. C5, live shadowing, production, deletion execution and ecosystem integration require a new explicit operator GO.
