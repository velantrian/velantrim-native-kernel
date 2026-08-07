# Native Kernel Implementation Profiles

This directory contains machine-readable planning, implementation and evidence surfaces for replaceable profiles.

```text
profile manifest
≠ Architecture Canon
≠ complete runtime support
≠ conformance evidence by itself
```

## Current profile

| Profile | Decision | Implementation | Evidence | Conformance |
|---|---|---|---|---|
| `native-kernel/postgresql-reference@0.4-p4` | `ACCEPTED / APPROVED` | `PARTIAL — P1 + P2 + P3 + P4` | `REPOSITORY_REPRODUCED — ASSERTION-SCOPED C2` | `41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED` |

Evidence lineage: `clean/postgresql-reference/0.1`. It remains independent from Issue #1 and must never be represented as recovered `v0.1.2.1`.

## Manifest roles

- [`postgresql-reference-v0/profile-manifest.json`](./postgresql-reference-v0/profile-manifest.json) — historical P0 proposal snapshot;
- [`postgresql-reference-v0/p1-manifest.json`](./postgresql-reference-v0/p1-manifest.json) — P1 semantic-core record;
- [`postgresql-reference-v0/p2-manifest.json`](./postgresql-reference-v0/p2-manifest.json) — P2 append/idempotency evidence record;
- [`postgresql-reference-v0/p3-manifest.json`](./postgresql-reference-v0/p3-manifest.json) — P3 replay/projection/Receipt evidence record;
- [`postgresql-reference-v0/p4-manifest.json`](./postgresql-reference-v0/p4-manifest.json) — current assertion support/C2 evidence record.

## P4 evidence

Initial exact evidence:

```text
head:                       93710131fffdea7d9a586cc05e7f258c07fae707
repository run:             31175767586 PASS
3.11 / PostgreSQL 16:       PASS
3.11 / PostgreSQL 18:       PASS
3.12 / PostgreSQL 16:       PASS
3.12 / PostgreSQL 18:       PASS
P1/P2/P3 regressions:       PASS
artifacts:                  4 RETAINED PER MATRIX JOB
support_state:              PARTIAL
C2 supported assertions:   41
C3:                         NOT_ESTABLISHED
```

Validators:

- [`../tools/profiles/validate_p4_manifest.py`](../tools/profiles/validate_p4_manifest.py);
- [`../tools/conformance/validate_p4_report.py`](../tools/conformance/validate_p4_report.py).

## Package ownership

[`../native_kernel/postgresql_profile/`](../native_kernel/postgresql_profile/) owns replaceable PostgreSQL details:

- migration checksum ledger;
- instance/history head and writer epoch fencing;
- atomic Event/idempotency persistence;
- rollback-safe ordering;
- canonical payload/envelope commitments;
- verified persisted replay;
- disposable projection rebuild;
- bounded operational Receipts;
- assertion-scoped P4 check execution and report generation.

It does not own physical deletion, network API, P5 portability, C3 or production guarantees.

## Phase boundary

```text
P0: COMPLETE
P1: MERGED / REPOSITORY-TESTED
P2: MERGED / REPOSITORY-INTEGRATION-TESTED
P3: MERGED / REPOSITORY-INTEGRATION-TESTED
P4: ACTIVE / PARTIAL / C2 PREVIOUS-HEAD EVIDENCE
P5 SQLite comparison: NOT AUTHORIZED
C3: NOT ESTABLISHED
```

## Assertion boundary

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
```

C2 applies only to `SUPPORTED`. All eight proposed `NK-EPI` assertions remain `UNSUPPORTED`.

## Read next

- [`../STATUS.md`](../STATUS.md)
- [`../docs/rfc/0002-postgresql-reference-profile-v0.md`](../docs/rfc/0002-postgresql-reference-profile-v0.md)
- [`../docs/adr/0018-authorize-p4-assertion-scoped-conformance.md`](../docs/adr/0018-authorize-p4-assertion-scoped-conformance.md)
- [`../docs/ai/P4_IMPLEMENTATION_RECORD.md`](../docs/ai/P4_IMPLEMENTATION_RECORD.md)
- [Issue #55](https://github.com/velantrian/velantrim-native-kernel/issues/55)
- [PR #56](https://github.com/velantrian/velantrim-native-kernel/pull/56)

No manifest may infer C3, truth, external authenticity, physical erasure, production readiness, storage neutrality or historical recovery from P4 C2 evidence.
