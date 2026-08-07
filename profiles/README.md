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
| `native-kernel/postgresql-reference@0.2-p2` | `ACCEPTED / APPROVED` | `PARTIAL — P1 + P2` | `UNIT-TESTED; PG INTEGRATION NOT ESTABLISHED` | `UNSUPPORTED` |

Evidence lineage: `clean/postgresql-reference/0.1`. It remains independent from Issue #1 and must never be represented as recovered `v0.1.2.1`.

## Manifest roles

### P0 planning snapshot

[`postgresql-reference-v0/profile-manifest.json`](./postgresql-reference-v0/profile-manifest.json) remains the historical proposal snapshot. Its `PROPOSED/PENDING/NOT_STARTED` values describe the moment it was created.

### P1 implementation record

[`postgresql-reference-v0/p1-manifest.json`](./postgresql-reference-v0/p1-manifest.json) records the bounded profile-independent semantic core.

### P2 implementation record

[`postgresql-reference-v0/p2-manifest.json`](./postgresql-reference-v0/p2-manifest.json) records:

```text
decision:                    ACCEPTED / APPROVED
phase:                       P2
implementation:              PARTIAL
P2 unit tests:                9 PASS
P2 manifest tests:            5 PASS
compileall/validator:         PASS
PostgreSQL integration tests: 5 DECLARED / NOT RUN NO DSN
repository CI:               NOT_RECORDED
runtime conformance:         UNSUPPORTED
```

Validator: [`../tools/profiles/validate_p2_manifest.py`](../tools/profiles/validate_p2_manifest.py).

## P2 package

[`../native_kernel/postgresql_profile/`](../native_kernel/postgresql_profile/) owns the replaceable PostgreSQL storage details:

- lazy Psycopg boundary;
- migration checksum ledger;
- Kernel instance and history head;
- writer owner/epoch lease;
- atomic Event/idempotency persistence;
- rollback-safe ordering counters;
- canonical payload/envelope bytes and integrity chain.

It does not own replay/projections, deletion execution, network API or conformance.

## Phase boundary

```text
P0 plan: COMPLETE
P1 semantic core: MERGED / LOCALLY_TESTED
P2 PostgreSQL append: AUTHORIZED / PARTIAL / UNIT-TESTED
PostgreSQL integration: NOT_ESTABLISHED
P3 replay/projections/Receipts: NOT AUTHORIZED
P4 conformance adapter: NOT AUTHORIZED
P5 SQLite comparison: NOT AUTHORIZED
```

All 72 registered assertions remain runtime `UNSUPPORTED` until P4 emits complete assertion-scoped evidence.

## Read next

- [`../docs/rfc/0002-postgresql-reference-profile-v0.md`](../docs/rfc/0002-postgresql-reference-profile-v0.md)
- [`../docs/rfc/0002-postgresql-reference-profile-v0.ru.md`](../docs/rfc/0002-postgresql-reference-profile-v0.ru.md)
- [`../docs/adr/0016-authorize-p2-postgresql-append-profile.md`](../docs/adr/0016-authorize-p2-postgresql-append-profile.md)
- [Issue #46](https://github.com/velantrian/velantrim-native-kernel/issues/46)

No manifest may claim recovery, production readiness, storage neutrality, PostgreSQL integration or conformance through documentation, unit tests or a workflow definition alone.
