# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `07bf1cc955307783f8eaa3becbaa924087b8b325`  
> **Implementation publication:** PR #62 merged / Issue #61 pending final closure / ADR-0020  
> **Repository status:** `RESEARCH / C4 PARTIAL OFFLINE SHADOW EVALUATION / NOT PRODUCTION-READY`

## Current phase

```text
P1: MERGED / REPOSITORY-TESTED
P2: MERGED / REPOSITORY-INTEGRATION-TESTED
P3: MERGED / REPOSITORY-INTEGRATION-TESTED
P4: MERGED / PARTIAL / POSTGRESQL C2 REPOSITORY-REPRODUCED
P5: MERGED / PARTIAL / SQLITE C2 + CROSS-PROFILE C3 REPOSITORY-REPRODUCED
C4: MERGED / PARTIAL / OFFLINE RECORDED-WORKLOAD SHADOW EVIDENCE REPOSITORY-REPRODUCED
C5: NOT AUTHORIZED / NOT ESTABLISHED
```

C4 is an evidence layer over the existing profiles. It is not an authoritative runtime, storage profile, deployment mode or ecosystem authority.

## Publication lineage

```text
C4 base main:       b10be105743355a04e58611639a9d28faf7ea514
PR #62 final head:  b7786c088ef2cfd203c02625a5e0c40129cbf148
PR #62 merge/main:  07bf1cc955307783f8eaa3becbaa924087b8b325
```

## Profiles, protocols and maps

```text
PostgreSQL: native-kernel/postgresql-reference@0.4-p4
SQLite:     native-kernel/sqlite-embedded@0.5-p5
C4 dataset: native-kernel/c4-offline-shadow-v1

Dataset protocol: nk-shadow-workload/1
Report protocol:  nk-shadow-report/1
Receipt protocol: nk-shadow-receipt/1
```

Single-profile PostgreSQL and SQLite C2:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

PostgreSQL↔SQLite C3 and C4 assertion scope:

```text
SUPPORTED:   45
PARTIAL:     10
UNSUPPORTED: 17
FAILED:       0
TOTAL:       72
support_state: PARTIAL
```

C4 evaluates exactly the existing 45 C3-supported assertions. It does not promote the remaining 27 assertions. All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## Authority boundary

```text
mode:                  SHADOW_ONLY
authority promotion:   FORBIDDEN
authoritative writes:  FORBIDDEN
side effects:           FORBIDDEN
promotion decision:    NOT_AUTHORIZED
```

The evaluator cannot append to Kernel history, mutate either storage profile, approve a candidate, trigger actions or connect itself to Titan, Mentaury or Crystal.

## Approved dataset

```text
dataset_id:      native-kernel/c4-offline-shadow-v1
dataset_sha256:  15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:           15
assertion scope: 45 / 45 C3-supported assertions
approval:        ADR-0020 / Issue #61 / OFFLINE_RECORDED_WORKLOAD_ONLY
```

The dataset contains approved synthetic repository workloads. It is not captured production traffic.

## Exact PR-head evidence

```text
Final head:    b7786c088ef2cfd203c02625a5e0c40129cbf148
C4 run:        31189149796 — PASS
P5/C3 run:     31189149627 — PASS
P4 run:        31189149839 — PASS
P1 run:        31189149436 — PASS
Fixtures:      31189149449 — PASS
AI context:    31189149274 — PASS
```

## Exact implementation-main evidence

```text
Main:          07bf1cc955307783f8eaa3becbaa924087b8b325
C4 run:        31189474449 — PASS
P5/C3 run:     31189474409 — PASS
P4 run:        31189474739 — PASS
P1 run:        31189474300 — PASS
Fixtures:      31189474351 — PASS
AI context:    31189474423 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Every C4 job passed C4 unit/report/manifest guards, exact P4/P5/C3 prerequisite generation, offline evaluation, P1–P5 regressions, compileall and four-report artifact upload.

## Main-bound artifacts

Each artifact contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
c4-shadow-report.json
```

```text
py3.11/pg16 sha256:3e58a0ea73445d99a94c1e6b7c637640b9852e20b0a71a47f243a14e49995e44
py3.11/pg18 sha256:14cd00c605d247873ff4ae58b3e8d884b6a3e986f13c1f47e0665eee5e33cb9e
py3.12/pg16 sha256:08e1ecccc2679a7ce7bc8fadf43a9586794696b08f8f549f9350d8c658cc160f
py3.12/pg18 sha256:4f890220eb7b1aed36aab74e4aedf4b6e6a4bd71dcc81534a6fe546ae9c75fd6
```

Artifacts are retained until 2026-09-06.

One main-bound archive was downloaded and inspected. It was bound to exact `main@07bf1cc9…` and run `31189474449` and contained:

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

The inspected Receipt explicitly recorded:

```text
authority_promoted: false
authoritative_write_performed: false
side_effects_executed: false
```

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

Publish and merge this documentation-only checkpoint, reproduce the bounded C4 evidence on the resulting `main`, synchronize Notion and close Issue #61. C5, live shadowing, production, deletion execution and ecosystem integration require a new explicit operator GO.
