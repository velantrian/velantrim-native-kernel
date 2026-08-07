# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-07  
**Last verified public `main`:** `b10be105743355a04e58611639a9d28faf7ea514`  
**Active issue / PR / ADR:** #61 / #62 / ADR-0020  
**Repository status:** `RESEARCH / C4 PARTIAL OFFLINE SHADOW EVALUATION / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Re-check the actual branch ref, exact workflows, artifact contents and later checkpoint merge.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
C2 ≠ C3 ≠ C4
C4 OFFLINE SHADOW ≠ LIVE SHADOWING
C4 SHADOW OBSERVATION ≠ AUTHORITY PROMOTION
C4 SUPPORTED ASSERTIONS ≠ SUPPORT FOR ALL 72
ASSERTION EVIDENCE ≠ TRUTH / AUTHENTICITY / PHYSICAL ERASURE
```

## Current gate

```text
RFC-0002:              ACCEPTED / APPROVED
P1 semantic core:      MERGED / REPOSITORY-TESTED
P2 PostgreSQL adapter: MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections: MERGED / REPOSITORY-INTEGRATION-TESTED
P4 conformance:        MERGED / PARTIAL / POSTGRESQL C2
P5 SQLite/C3:          MERGED / PARTIAL / REPOSITORY-REPRODUCED
C4 offline shadow:     PR #62 OPEN / PARTIAL / REPOSITORY-REPRODUCED ON PREVIOUS HEAD
C5/production:         NOT AUTHORIZED / NOT ESTABLISHED
Issue #1 / #18:        ACTIVE / INDEPENDENT
```

## Profiles, protocols and result map

```text
PostgreSQL  native-kernel/postgresql-reference@0.4-p4
SQLite      native-kernel/sqlite-embedded@0.5-p5
C4 dataset  native-kernel/c4-offline-shadow-v1
```

```text
Dataset protocol: nk-shadow-workload/1
Report protocol:  nk-shadow-report/1
Receipt protocol: nk-shadow-receipt/1
```

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
C4 shadow scope:   45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state:     PARTIAL
```

C4 evaluates only the 45 assertions already supported at C3. All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## Authority boundary

```text
shadow mode:          OFFLINE_RECORDED_WORKLOAD
authority promotion: FORBIDDEN
authoritative writes:FORBIDDEN
side effects:         FORBIDDEN
promotion decision:  NOT_AUTHORIZED
```

The C4 evaluator is not a command path and does not call append, projection mutation, external actions or ecosystem tools.

## Approved dataset

```text
dataset_id:     native-kernel/c4-offline-shadow-v1
sha256:         15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:          15
assertion scope:45 / 45 C3-supported assertions
approval:       ADR-0020 / Issue #61 / OFFLINE_RECORDED_WORKLOAD_ONLY
```

The dataset is synthetic repository evidence, not captured production traffic.

## First repository evidence

```text
Evidence head: 97abce685a68e24aec9afab451c009df5783b96b
C4 run:       31187532364 — PASS
P5/C3 run:    31187532391 — PASS
P4 run:       31187532618 — PASS
P1 run:       31187532346 — PASS
Fixture run:  31187532580 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Each artifact contains PostgreSQL P4, SQLite P5, C3 equivalence and C4 shadow reports. One artifact was downloaded and inspected.

```text
15 / 15 cases matched
15 / 15 Shadow Receipts present
45 / 45 C3-supported assertions covered
0 semantic divergences
0 critical divergences
0 missing Receipts
30 declared allowed operational differences
72 assertion results
```

Artifact digests:

```text
py3.11/pg16 sha256:59cf39e6cbd3e8c95157676cc3fd838687d5911676b227681efd6c83a7f36e90
py3.11/pg18 sha256:9d4f828095285e479e1a95b87523fbaa800068f82a75cbbefb5f2d736e952032
py3.12/pg16 sha256:f85e29688a0176c168067fb8ed6f889550342c6faffcb4dc7d391715ea5364d4
py3.12/pg18 sha256:6892bc2ab7232c96124d4d207aacf06385f8b2ff6a3ea91097d1db6c2e834328
```

Artifacts are retained until 2026-09-06.

## Evidence meaning

```text
PostgreSQL C2:   REPOSITORY_REPRODUCED for 41 SUPPORTED assertions
SQLite C2:       REPOSITORY_REPRODUCED for 41 SUPPORTED assertions
Cross-profile C3:REPOSITORY_REPRODUCED for 45 SUPPORTED assertions
Offline C4:      REPOSITORY_REPRODUCED for the approved 15-case dataset and 45-assertion scope
C5:              NOT_ESTABLISHED
```

A passing C4 report means the declared observations matched inside this exact dataset and threshold policy. It is not an exhaustive or operational proof.

## Explicitly absent

- live traffic capture or live production shadowing;
- authority promotion, candidate approval or automatic action;
- exhaustive equivalence proof;
- PostgreSQL/SQLite operational equivalence;
- complete conflict subsystem;
- physical/cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- truth/signature/notarization certification;
- network API;
- C5 security/privacy/incident evidence;
- production security, HA, backup, restore or compliance guarantees;
- Titan, Mentaury or Crystal runtime wiring;
- historical `v0.1.2.1` recovery.

## Next action

Finish exact final-head C4 matrix, public documentation validation and PR #62 review. After merge, record main-bound evidence and a docs-only publication checkpoint. C5 or any live/production/integration work requires a new explicit operator GO.
