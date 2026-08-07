# Native Kernel Implementation Profiles

This directory contains machine-readable planning and evidence surfaces for replaceable implementation profiles.

```text
profile manifest
≠ Architecture Canon
≠ complete runtime
≠ conformance evidence by itself
```

## Current profile

| Profile | Decision | Implementation | Evidence | Runtime conformance |
|---|---|---|---|---|
| `native-kernel/postgresql-reference@0.2-p2` | `ACCEPTED / APPROVED` | `PARTIAL — P1 + P2` | `REPOSITORY_REPRODUCED — P2 INTEGRATION` | `UNSUPPORTED` |

Evidence lineage: `clean/postgresql-reference/0.1`. It remains independent from Issue #1 and must never be represented as recovered `v0.1.2.1`.

## Manifest roles

- [`postgresql-reference-v0/profile-manifest.json`](./postgresql-reference-v0/profile-manifest.json) — historical P0 proposal snapshot;
- [`postgresql-reference-v0/p1-manifest.json`](./postgresql-reference-v0/p1-manifest.json) — P1 semantic-core record;
- [`postgresql-reference-v0/p2-manifest.json`](./postgresql-reference-v0/p2-manifest.json) — current P2 append/idempotency evidence record.

Current P2 evidence:

```text
implementation:             PARTIAL
repository run:             31151297646 PASS
3.11 / PostgreSQL 16:       PASS
3.11 / PostgreSQL 18:       PASS
3.12 / PostgreSQL 16:       PASS
3.12 / PostgreSQL 18:       PASS
runtime conformance:        UNSUPPORTED
```

Validator: [`../tools/profiles/validate_p2_manifest.py`](../tools/profiles/validate_p2_manifest.py).

## P2 package

[`../native_kernel/postgresql_profile/`](../native_kernel/postgresql_profile/) owns replaceable PostgreSQL storage details:

- lazy Psycopg boundary;
- migration checksum ledger;
- Kernel instance/history head;
- writer owner/epoch lease;
- atomic Event/idempotency persistence;
- rollback-safe ordering counters;
- canonical payload/envelope bytes and integrity chain.

It does not own replay/projections, deletion execution, network API or conformance.

## Phase boundary

```text
P0: COMPLETE
P1: MERGED / REPOSITORY-TESTED
P2: PARTIAL / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections/Receipts: NOT AUTHORIZED
P4 conformance adapter: NOT AUTHORIZED
P5 SQLite comparison: NOT AUTHORIZED
```

All 72 registered assertions remain runtime `UNSUPPORTED` until P4 emits complete assertion-scoped evidence.

## Read next

- [`../docs/rfc/0002-postgresql-reference-profile-v0.md`](../docs/rfc/0002-postgresql-reference-profile-v0.md)
- [`../docs/adr/0016-authorize-p2-postgresql-append-profile.md`](../docs/adr/0016-authorize-p2-postgresql-append-profile.md)
- [Issue #46](https://github.com/velantrian/velantrim-native-kernel/issues/46)
- [PR #47](https://github.com/velantrian/velantrim-native-kernel/pull/47)

No manifest may claim recovery, production readiness, storage neutrality or conformance from P2 integration evidence alone.
