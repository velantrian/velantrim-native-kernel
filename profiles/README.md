# Native Kernel Implementation Profiles

This directory contains machine-readable planning, implementation and evidence surfaces for replaceable profiles.

```text
profile manifest
≠ Architecture Canon
≠ complete runtime support
≠ conformance evidence by itself
```

## Current profiles

| Profile | Decision | Implementation | Evidence | Assertion map |
|---|---|---|---|---|
| `native-kernel/postgresql-reference@0.4-p4` | `ACCEPTED / APPROVED` | `PARTIAL — P1–P4` | `C2 REPOSITORY_REPRODUCED` | `41 / 13 / 18 / 0` |
| `native-kernel/sqlite-embedded@0.5-p5` | `ACCEPTED / APPROVED` | `PARTIAL — P5` | `C2 REPOSITORY_REPRODUCED ON EVIDENCE HEAD` | `41 / 13 / 18 / 0` |
| PostgreSQL↔SQLite comparison | ADR-0019 | `PARTIAL — C3` | `REPOSITORY_REPRODUCED ON EVIDENCE HEAD` | `45 / 10 / 17 / 0` |

Lineages:

```text
clean/postgresql-reference/0.1
clean/sqlite-embedded/0.1
```

Both remain independent from Issue #1 and must never be represented as recovered `v0.1.2.1`.

## Manifest roles

PostgreSQL:

- [`postgresql-reference-v0/profile-manifest.json`](./postgresql-reference-v0/profile-manifest.json) — P0 proposal snapshot;
- [`postgresql-reference-v0/p1-manifest.json`](./postgresql-reference-v0/p1-manifest.json) — P1 semantic core;
- [`postgresql-reference-v0/p2-manifest.json`](./postgresql-reference-v0/p2-manifest.json) — P2 append/idempotency;
- [`postgresql-reference-v0/p3-manifest.json`](./postgresql-reference-v0/p3-manifest.json) — P3 replay/projection/Receipts;
- [`postgresql-reference-v0/p4-manifest.json`](./postgresql-reference-v0/p4-manifest.json) — PostgreSQL C2 assertion map.

SQLite/C3:

- [`sqlite-embedded-v0/p5-manifest.json`](./sqlite-embedded-v0/p5-manifest.json) — SQLite C2, C3 comparison map, equivalence classes, artifacts and boundaries.

## Initial P5/C3 evidence

```text
head:                       d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
repository run:             31181341275 PASS
Python 3.11 / PG16 / SQLite 3.45.1: PASS
Python 3.11 / PG18 / SQLite 3.45.1: PASS
Python 3.12 / PG16 / SQLite 3.45.1: PASS
Python 3.12 / PG18 / SQLite 3.45.1: PASS
P1–P4 regressions:          PASS
artifacts:                  4 archives × 3 JSON reports
support_state:              PARTIAL
SQLite C2 supported:        41
Cross-profile C3 supported: 45
```

Each artifact contains:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
```

Validators:

- [`../tools/profiles/validate_p5_manifest.py`](../tools/profiles/validate_p5_manifest.py);
- [`../tools/conformance/validate_p5_report.py`](../tools/conformance/validate_p5_report.py);
- [`../tools/conformance/validate_p4_report.py`](../tools/conformance/validate_p4_report.py).

## Package ownership

[`../native_kernel/postgresql_profile/`](../native_kernel/postgresql_profile/) owns PostgreSQL-specific append, replay, projection, Receipt and P4 report behaviour.

[`../native_kernel/sqlite_profile/`](../native_kernel/sqlite_profile/) independently owns:

- stdlib `sqlite3` migrations and schema;
- `BEGIN IMMEDIATE` single-writer transactions;
- owner/epoch/expiry fencing;
- append/idempotency/order/hash-chain behaviour;
- replay, projections and bounded Receipts;
- exact PostgreSQL-history import;
- SQLite C2 report and C3 comparison.

Shared accepted contracts/fixtures do not make the implementations identical.

## Phase boundary

```text
P0: COMPLETE
P1: MERGED
P2: MERGED
P3: MERGED
P4: MERGED / PARTIAL / C2
P5: IMPLEMENTED / PARTIAL / C2+C3 PREVIOUS-HEAD EVIDENCE
C4/C5: NOT AUTHORIZED / NOT ESTABLISHED
Production: NOT CLAIMED
```

## Assertion boundary

```text
SQLite C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
C3:        45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
```

C2/C3 apply only to `SUPPORTED`. All eight proposed `NK-EPI` assertions remain `UNSUPPORTED`.

## Read next

- [`../STATUS.md`](../STATUS.md)
- [`../docs/adr/0019-authorize-p5-sqlite-and-c3-equivalence.md`](../docs/adr/0019-authorize-p5-sqlite-and-c3-equivalence.md)
- [`../docs/ai/P5_IMPLEMENTATION_RECORD.md`](../docs/ai/P5_IMPLEMENTATION_RECORD.md)
- [`../docs/CONFORMANCE_MODEL.md`](../docs/CONFORMANCE_MODEL.md)
- [Issue #58](https://github.com/velantrian/velantrim-native-kernel/issues/58)
- [PR #59](https://github.com/velantrian/velantrim-native-kernel/pull/59)

No manifest may infer full support, operational equivalence, truth, external authenticity, physical erasure, C4/C5, production readiness or historical recovery from P5 C3 evidence.
