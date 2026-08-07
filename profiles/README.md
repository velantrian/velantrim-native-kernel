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
| `native-kernel/postgresql-reference@0.3-p3` | `ACCEPTED / APPROVED` | `PARTIAL — P1 + P2 + P3` | `REPOSITORY_REPRODUCED — P3 INTEGRATION` | `UNSUPPORTED` |

Evidence lineage: `clean/postgresql-reference/0.1`. It remains independent from Issue #1 and must never be represented as recovered `v0.1.2.1`.

## Manifest roles

- [`postgresql-reference-v0/profile-manifest.json`](./postgresql-reference-v0/profile-manifest.json) — historical P0 proposal snapshot;
- [`postgresql-reference-v0/p1-manifest.json`](./postgresql-reference-v0/p1-manifest.json) — P1 semantic-core record;
- [`postgresql-reference-v0/p2-manifest.json`](./postgresql-reference-v0/p2-manifest.json) — P2 append/idempotency evidence record;
- [`postgresql-reference-v0/p3-manifest.json`](./postgresql-reference-v0/p3-manifest.json) — current replay/projection/Receipt evidence record.

Initial P3 executable evidence:

```text
head:                       0f8fd4ffe5d5fb0d4bc01f3e441a053f691dbba3
repository run:             31171581859 PASS
3.11 / PostgreSQL 16:       PASS
3.11 / PostgreSQL 18:       PASS
3.12 / PostgreSQL 16:       PASS
3.12 / PostgreSQL 18:       PASS
P2 regression:              PASS
runtime conformance:        UNSUPPORTED
```

Validator: [`../tools/profiles/validate_p3_manifest.py`](../tools/profiles/validate_p3_manifest.py).

## P2/P3 package

[`../native_kernel/postgresql_profile/`](../native_kernel/postgresql_profile/) owns replaceable PostgreSQL details:

- lazy Psycopg boundary;
- migration checksum ledger;
- Kernel instance/history head;
- writer owner/epoch lease;
- atomic Event/idempotency persistence;
- rollback-safe ordering counters;
- canonical payload/envelope bytes and integrity chain;
- verified persisted replay from sequence `1`;
- explicit upcaster routing;
- disposable semantic-state projection rebuild;
- canonical bounded Replay/Projection Rebuild Receipts;
- stale-head and transactional rollback protection.

It does not own physical deletion, network API, P4 assertion conformance, P5 portability or production guarantees.

## Phase boundary

```text
P0: COMPLETE
P1: MERGED / REPOSITORY-TESTED
P2: PARTIAL / REPOSITORY-INTEGRATION-TESTED
P3: PARTIAL / REPOSITORY-INTEGRATION-TESTED
P4 conformance adapter: NOT AUTHORIZED
P5 SQLite comparison: NOT AUTHORIZED
```

All 72 registered assertions remain runtime `UNSUPPORTED` until P4 emits complete assertion-scoped evidence.

## Read next

- [`../docs/rfc/0002-postgresql-reference-profile-v0.md`](../docs/rfc/0002-postgresql-reference-profile-v0.md)
- [`../docs/adr/0017-authorize-p3-replay-projection-receipts.md`](../docs/adr/0017-authorize-p3-replay-projection-receipts.md)
- [Issue #49](https://github.com/velantrian/velantrim-native-kernel/issues/49)
- [PR #50](https://github.com/velantrian/velantrim-native-kernel/pull/50)

No manifest may claim recovery, truth, external authenticity, physical erasure, production readiness, storage neutrality or assertion-level conformance from P3 integration evidence alone.
