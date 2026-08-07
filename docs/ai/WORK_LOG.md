# 🧾 Native Kernel AI Engineering Work Log

This is a concise chronology and hand-off surface. Re-verify exact SHAs, runs and artifacts before treating an entry as present reality.

---

## 2026-08-07 — C4 offline shadow evaluation implemented; PR #62 open

```text
Status:            PR OPEN / C4 PARTIAL / OFFLINE RECORDED-WORKLOAD SHADOW
Issue / PR:        #61 / #62
Base main:         b10be105743355a04e58611639a9d28faf7ea514
First evidence:    97abce685a68e24aec9afab451c009df5783b96b
ADR:               ADR-0020
C5 / production:   NOT AUTHORIZED / NOT ESTABLISHED
Notion impact:     GITHUB_AND_NOTION AFTER MERGE
```

Authorized boundary:

```text
OFFLINE_RECORDED_WORKLOAD_ONLY
SHADOW_ONLY
NO AUTHORITY PROMOTION
NO AUTHORITATIVE WRITES
NO SIDE EFFECTS
NO C5 / PRODUCTION / ECOSYSTEM WIRING
```

Implemented:

- approved `nk-shadow-workload/1` dataset;
- exact dataset SHA-256 binding;
- authority-free offline evaluator;
- `nk-shadow-report/1` protocol;
- per-case bounded `nk-shadow-receipt/1`;
- semantic, behavioural, integrity and proof-boundary comparison;
- explicit allowed operational differences;
- fail-closed critical and semantic divergence gates;
- complete 72-ID report with C4 limited to 45 C3-supported assertions;
- strict validators and anti-overclaim tests;
- 4× C4 matrix producing P4, P5, C3 and C4 reports;
- P1–P5 regressions in every C4 job.

Approved dataset:

```text
dataset_id:      native-kernel/c4-offline-shadow-v1
sha256:          15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:           15
assertion scope: 45 / 45 C3-supported assertions
```

### Bootstrap evidence

The first single-file connector payload was truncated and failed with `base64: invalid input`; no source evidence was claimed from that run.

The payload was replaced by six individually hashed parts plus a final archive digest. Bootstrap run `31187117717` passed:

- six part digests;
- final archive SHA-256 `c7895b487762853f3236e30cff5c69db1f9482a5ef360f7d29f2b5ce582e5066`;
- archive listing/extraction;
- 19 C4 tests;
- manifest validation;
- compileall;
- source publication.

Temporary bootstrap files and workflow were removed before the executable PR head.

### First genuine matrix defect

Run `31187288110` failed in all four environments before prerequisite report generation. The test `test_repository_metadata_is_required_when_requested` inherited repository evidence environment variables from CI and incorrectly expected a local report.

The test was isolated from ambient environment state. Evaluator and validator requirements were not weakened.

### First complete repository evidence

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

One artifact was downloaded and inspected:

```text
15 / 15 cases matched
15 Shadow Receipts
45 / 45 C3-supported assertions covered
0 semantic divergences
0 critical divergences
0 missing Receipts
30 allowed operational differences
72 assertion results
status: PASS
support_state: PARTIAL
```

```text
C4 PASS for one approved recorded dataset
≠ live production shadowing
≠ authority promotion
≠ candidate approval
≠ exhaustive equivalence
≠ all 72 supported
≠ C5
≠ production readiness
```

Remaining work: public/AI documentation guard, exact final-head evidence, review, merge, main-bound checkpoint, Notion synchronization and Issue #61 closure.

---

## 2026-08-07 — P5 SQLite and assertion-scoped C3 merged

```text
Status:          MERGED / P5 PARTIAL / SQLITE C2 + CROSS-PROFILE C3
Issue / PR:      #58 / #59
Base main:       1dc493e9d23b99ee4bbf6015348599cd56f6cb56
Final PR head:   6483c9a229aea7d49929745b7652e67f1c39949c
Merge:           a8bb0ae232b977856730a1a4f21f977c1f69ca0a
Checkpoint main: b10be105743355a04e58611639a9d28faf7ea514
PostgreSQL:      native-kernel/postgresql-reference@0.4-p4
SQLite:          native-kernel/sqlite-embedded@0.5-p5
ADR:             ADR-0019
```

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state:     PARTIAL
```

Implemented a materially independent stdlib SQLite profile, complete profile reports and a separate `nk-equivalence-report/1` comparator. Cross-profile evidence promoted only `NK-SEM-008`, `NK-ID-008`, `NK-EQV-002` and `NK-EQV-003`. All `NK-EPI-001…008` remained proposed and unsupported.

### Final publication evidence

```text
PR-head P5/C3: 31182711376 — PASS
Main P5/C3:    31183074126 — PASS
Checkpoint:    b10be105743355a04e58611639a9d28faf7ea514
```

A final-head archive and a main-bound archive were each inspected. Both contained PostgreSQL P4, SQLite P5 and C3 reports with all 72 assertions, map `45/10/17/0` and eight passed comparison checks.

---

## 2026-08-07 — P4 assertion-scoped conformance merged

```text
Issue / PR:    #55 / #56
Final PR head: 0e7adf71475d37d5c096718762cbc08086c5e465
Merge:         db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad
Checkpoint:    1dc493e9d23b99ee4bbf6015348599cd56f6cb56
ADR:           ADR-0018
```

PostgreSQL P4 added complete 72-ID evidence reporting with `41/13/18/0` and assertion-scoped C2.

---

## 2026-08-07 — P3 replay/projections/Receipts merged

```text
Issue / PR: #49 / #50
Merge:      4af642930e18752f8f8b0bce75df355f76100d6f
ADR:        ADR-0017
```

---

## 2026-08-07 — P2 PostgreSQL append/idempotency merged

```text
Issue / PR: #46 / #47
Merge:      113452a365890bf6c143d76657b810be59530ed4
ADR:        ADR-0016
```

---

## 2026-08-06 — P1 semantic core merged

```text
Issue / PR: #43 / #44
Merge:      9fd608f3f1d2915b961644015eb6b5e1a93e84d3
ADR:        ADR-0015
```

---

## Continuing rule

Record exact PR/SHA, dataset ID/digest, support counts, evidence level, artifacts, thresholds, authority boundary, limitations, Notion state and next action. Never infer complete support, truth, authenticity, physical deletion, operational equivalence or production readiness from C2/C3/C4 evidence.
