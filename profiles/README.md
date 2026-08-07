# Native Kernel Implementation and Evidence Profiles

This directory contains machine-readable planning, implementation and evidence surfaces for replaceable profiles and bounded evaluation layers.

```text
profile/evidence manifest
≠ Architecture Canon
≠ complete runtime support
≠ conformance evidence by itself
```

## Current profiles and evidence layers

| Surface | Decision | Implementation | Evidence | Assertion map |
|---|---|---|---|---|
| `native-kernel/postgresql-reference@0.4-p4` | `ACCEPTED / APPROVED` | `PARTIAL — P1–P4` | `C2 REPOSITORY_REPRODUCED` | `41 / 13 / 18 / 0` |
| `native-kernel/sqlite-embedded@0.5-p5` | `ACCEPTED / APPROVED` | `PARTIAL — P5` | `C2 REPOSITORY_REPRODUCED` | `41 / 13 / 18 / 0` |
| PostgreSQL↔SQLite comparison | ADR-0019 | `PARTIAL — C3` | `REPOSITORY_REPRODUCED` | `45 / 10 / 17 / 0` |
| `native-kernel/c4-offline-shadow-v1` | ADR-0020 | `PARTIAL — C4` | `REPOSITORY_REPRODUCED ON APPROVED DATASET` | `45 / 10 / 17 / 0` |

Lineages:

```text
clean/postgresql-reference/0.1
clean/sqlite-embedded/0.1
```

C4 is an evidence layer, not a storage lineage. All surfaces remain independent from Issue #1 and must never be represented as recovered `v0.1.2.1`.

## Manifest roles

PostgreSQL:

- [`postgresql-reference-v0/profile-manifest.json`](./postgresql-reference-v0/profile-manifest.json) — P0 proposal snapshot;
- [`postgresql-reference-v0/p1-manifest.json`](./postgresql-reference-v0/p1-manifest.json) — P1 semantic core;
- [`postgresql-reference-v0/p2-manifest.json`](./postgresql-reference-v0/p2-manifest.json) — P2 append/idempotency;
- [`postgresql-reference-v0/p3-manifest.json`](./postgresql-reference-v0/p3-manifest.json) — P3 replay/projection/Receipts;
- [`postgresql-reference-v0/p4-manifest.json`](./postgresql-reference-v0/p4-manifest.json) — PostgreSQL C2 assertion map.

SQLite/C3:

- [`sqlite-embedded-v0/p5-manifest.json`](./sqlite-embedded-v0/p5-manifest.json) — SQLite C2, C3 comparison map, equivalence classes, artifacts and boundaries.

C4:

- [`shadow-evaluation-v0/c4-manifest.json`](./shadow-evaluation-v0/c4-manifest.json) — approved dataset identity/digest, C3 prerequisite, authority boundary, C4 assertion scope, repository artifacts and non-claims;
- [`shadow-evaluation-v0/README.md`](./shadow-evaluation-v0/README.md) — human-readable profile/evidence guide.

## Approved C4 dataset

```text
dataset_id:      native-kernel/c4-offline-shadow-v1
protocol:        nk-shadow-workload/1
sha256:          15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:           15
assertion scope: 45 / 45 C3-supported assertions
```

The dataset is synthetic recorded repository evidence, not live production traffic.

## First C4 repository evidence

```text
head:                       97abce685a68e24aec9afab451c009df5783b96b
repository run:             31187532364 PASS
Python 3.11 / PG16 / SQLite 3.45.1: PASS
Python 3.11 / PG18 / SQLite 3.45.1: PASS
Python 3.12 / PG16 / SQLite 3.45.1: PASS
Python 3.12 / PG18 / SQLite 3.45.1: PASS
P1–P5 regressions:          PASS
artifacts:                  4 archives × 4 JSON reports
support_state:              PARTIAL
C4 evaluated supported:     45
```

Each artifact contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
c4-shadow-report.json
```

One archive was independently inspected and contained 15/15 matched cases, 15 Shadow Receipts, full 45-assertion C3-supported coverage, zero semantic/critical divergence and all 72 assertion results.

## Validators

- [`../tools/profiles/validate_c4_manifest.py`](../tools/profiles/validate_c4_manifest.py);
- [`../tools/conformance/validate_c4_report.py`](../tools/conformance/validate_c4_report.py);
- [`../tools/profiles/validate_p5_manifest.py`](../tools/profiles/validate_p5_manifest.py);
- [`../tools/conformance/validate_p5_report.py`](../tools/conformance/validate_p5_report.py);
- [`../tools/conformance/validate_p4_report.py`](../tools/conformance/validate_p4_report.py).

## Package ownership

[`../native_kernel/postgresql_profile/`](../native_kernel/postgresql_profile/) owns PostgreSQL-specific append, replay, projection, Receipt and P4 report behaviour.

[`../native_kernel/sqlite_profile/`](../native_kernel/sqlite_profile/) independently owns stdlib `sqlite3` persistence, transactions, fencing, replay, projections, Receipts, exact-history import and SQLite C2/C3 behaviour.

[`../native_kernel/shadow_evaluation/`](../native_kernel/shadow_evaluation/) owns authority-free comparison of approved recorded observations. It does not own persistence, command admission, candidate promotion or deployment.

Shared contracts, fixtures and assertion IDs do not make the implementations identical.

## C4 authority boundary

```text
mode:                  SHADOW_ONLY
authority promotion:   FORBIDDEN
authoritative writes:  FORBIDDEN
side effects:           FORBIDDEN
promotion decision:    NOT_AUTHORIZED
```

Dataset or threshold changes require a new immutable version/digest and repository evidence cycle.

## Phase boundary

```text
P0: COMPLETE
P1: MERGED
P2: MERGED
P3: MERGED
P4: MERGED / PARTIAL / C2
P5: MERGED / PARTIAL / C2+C3
C4: IMPLEMENTED / PARTIAL / OFFLINE SHADOW EVIDENCE
C5: NOT AUTHORIZED / NOT ESTABLISHED
Production: NOT CLAIMED
```

## Assertion boundary

```text
PostgreSQL C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
SQLite C2:     41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
C3:            45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
C4 scope:      45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
```

C2/C3/C4 apply only to `SUPPORTED`. All eight proposed `NK-EPI` assertions remain `UNSUPPORTED`.

## Read next

- [`../STATUS.md`](../STATUS.md)
- [`../docs/adr/0020-authorize-c4-offline-shadow-evaluation.md`](../docs/adr/0020-authorize-c4-offline-shadow-evaluation.md)
- [`../docs/ai/C4_IMPLEMENTATION_RECORD.md`](../docs/ai/C4_IMPLEMENTATION_RECORD.md)
- [`../docs/CONFORMANCE_MODEL.md`](../docs/CONFORMANCE_MODEL.md)
- [`../contracts/shadow-workload-v1.json`](../contracts/shadow-workload-v1.json)
- [Issue #61](https://github.com/velantrian/velantrim-native-kernel/issues/61)
- [PR #62](https://github.com/velantrian/velantrim-native-kernel/pull/62)

No manifest may infer live shadowing, authority promotion, full support, operational equivalence, truth, external authenticity, physical erasure, C5, production readiness or historical recovery from C4 evidence.
