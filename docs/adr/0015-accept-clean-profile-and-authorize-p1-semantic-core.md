# ADR-0015: Accept clean profile lineage and authorize bounded P1 semantic core

- **Decision status:** `ACCEPTED`
- **Evidence level:** `LOCALLY_TESTED`
- **Implementation status:** `PARTIAL — P1 SEMANTIC CORE ONLY`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-06`
- **Deciders:** `@velantrian`
- **Track:** `Clean Implementation Profile`
- **Related:** Issue #40, Issue #43, RFC-0002, ADR-0001, ADR-0009, ADR-0011…0014

## Context

RFC-0002 published a clean PostgreSQL reference-profile plan under evidence lineage `clean/postgresql-reference/0.1`. The profile remained proposed and runtime work required two separate decisions:

1. accept or reject the clean profile lineage and planning contract;
2. separately authorize a bounded implementation phase.

The authentic `v0.1.2.1` source remains unavailable in accessible sources. New implementation work must not be represented as recovery or continuation of that historical checkpoint.

## Decision

The operator accepts:

```text
Profile ID:       native-kernel/postgresql-reference
Planning lineage: clean/postgresql-reference/0.1
RFC-0002:         ACCEPTED
P1 semantic core: AUTHORIZED
```

P1 uses Python 3.11+ and the standard library as a reversible laboratory implementation choice. The package boundary is:

```text
native_kernel.semantic_core
```

P1 may implement:

- canonical identity and command bytes;
- immutable semantic domain objects;
- explicit deny-by-default authority decisions;
- a deterministic version-bound in-memory reducer;
- deletion/restriction state transitions;
- Receipt overclaim rejection;
- focused tests and local evidence.

## Explicitly not authorized

```text
PostgreSQL or SQLite adapter
SQL schema, driver or migration framework
durable append/idempotency store
writer lease persistence
projection persistence
network API
P2–P5 implementation
C1/C2/C3 profile conformance
Titan, Mentaury or Crystal wiring
recovered v0.1.2.1 claim
```

P2 and later phases require separate operator GO.

## Rationale

A profile-independent semantic core is the smallest implementation slice that can test accepted identity, authority, deterministic reduction, deletion-state and Receipt boundaries without binding semantics to PostgreSQL or starting durable storage work prematurely.

Python standard library is selected only for P1 because:

- existing fixture and governance tooling already runs on Python 3.11/3.12;
- no new dependency or licensing assumption is required;
- the code remains inspectable and easily replaceable;
- the choice does not define Architecture Canon or future profile languages.

## Evidence and status boundary

Recorded P1 evidence:

```text
20 focused unit tests PASS locally
Python compileall PASS
identity golden vectors matched
invalid identity vectors rejected
authority deny-by-default exercised
reducer determinism and version/sequence failures exercised
deletion fixture paths exercised
Receipt overclaims rejected
forbidden database/network imports absent
```

This evidence establishes only the tested P1 code path.

```text
P1 local PASS
≠ durable Kernel runtime
≠ PostgreSQL profile
≠ repository-reproduced C2
≠ cross-profile C3
```

All profile assertion rows remain `runtime_support: UNSUPPORTED` until a later conformance adapter emits scoped evidence under ADR-0014.

## Issue #1 boundary

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test suite
≠ declaration that historical source is globally lost
```

Issue #1 remains active and independent.

## Consequences

### Positive

- accepted contracts gain their first bounded implementation slice;
- identity and reducer behaviour become executable without storage coupling;
- authority and Receipt limits become fail-closed code paths;
- P2 can later consume a tested semantic core rather than embed semantics in SQL.

### Negative / deferred

- the semantic core is not a useful persistent Kernel by itself;
- provisional `nkd0` and `nks0` digests are implementation details, not accepted cross-profile contracts;
- no storage durability, crash recovery, migration or operational deletion exists;
- repository CI evidence may remain unrecorded until GitHub Actions executes.

## Supersession and rollback

P1 may be replaced by another language or package layout if accepted contracts and fixture behaviour remain preserved. Removing P1 must preserve this ADR, evidence history and the clean-lineage distinction.
