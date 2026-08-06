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
| `native-kernel/postgresql-reference` | `ACCEPTED / APPROVED` | `PARTIAL — P1 SEMANTIC CORE` | `LOCALLY_TESTED` | `UNSUPPORTED` |

Evidence lineage:

```text
clean/postgresql-reference/0.1
```

It remains independent from Issue #1 and must never be represented as recovered `v0.1.2.1`.

## Two manifest roles

### P0 planning snapshot

[`postgresql-reference-v0/profile-manifest.json`](./postgresql-reference-v0/profile-manifest.json) is the immutable historical planning record published before operator acceptance.

It intentionally retains:

```text
decision_status: PROPOSED
operator_approval: PENDING
implementation_status: NOT_STARTED
```

Those values describe the state when the proposal was created; they are not the current profile state.

### P1 implementation record

[`postgresql-reference-v0/p1-manifest.json`](./postgresql-reference-v0/p1-manifest.json) is the current bounded implementation/evidence record:

```text
decision:                  ACCEPTED / APPROVED
phase:                     P1
implementation:            PARTIAL
local semantic tests:      20 PASS
local manifest tests:       4 PASS
compileall:                PASS
repository CI:             NOT_RECORDED
kernel runtime conformance: UNSUPPORTED
```

The validator is [`../tools/profiles/validate_p1_manifest.py`](../tools/profiles/validate_p1_manifest.py).

## P1 implemented scope

Package: [`../native_kernel/semantic_core/`](../native_kernel/semantic_core/).

- canonical identity helpers;
- immutable semantic domain objects;
- deterministic command bytes and provisional digest;
- deny-by-default authority policy;
- deterministic in-memory reducer;
- deletion/restriction state transitions;
- Receipt overclaim guards.

P1 contains no database adapter, SQL schema, durable append/idempotency, projection persistence, network API or ecosystem wiring.

## Phase boundary

```text
P0 planning: COMPLETE
P1 semantic core: PARTIAL / LOCALLY_TESTED
P2 PostgreSQL adapter: BLOCKED / SEPARATE GO
P3 replay/projections/Receipts: BLOCKED
P4 conformance adapter/CI evidence: BLOCKED
P5 independent SQLite comparison: BLOCKED
```

All 72 registered assertions remain `UNSUPPORTED` for runtime conformance until a future P4 adapter emits complete assertion-scoped evidence.

## Read next

- [`../docs/rfc/0002-postgresql-reference-profile-v0.md`](../docs/rfc/0002-postgresql-reference-profile-v0.md)
- [`../docs/rfc/0002-postgresql-reference-profile-v0.ru.md`](../docs/rfc/0002-postgresql-reference-profile-v0.ru.md)
- [`../docs/adr/0015-accept-clean-profile-and-authorize-p1-semantic-core.md`](../docs/adr/0015-accept-clean-profile-and-authorize-p1-semantic-core.md)
- [Issue #40](https://github.com/velantrian/velantrim-native-kernel/issues/40)
- [Issue #43](https://github.com/velantrian/velantrim-native-kernel/issues/43)

No manifest may claim recovery, production readiness, storage neutrality or integration through documentation or local tests alone.
