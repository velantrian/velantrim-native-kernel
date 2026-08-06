# Current Status

> **Verified:** 2026-08-06  
> **Last verified public `main`:** `9fd608f3f1d2915b961644015eb6b5e1a93e84d3`  
> **Repository status:** `RESEARCH / P1 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`  
> **Kernel phase:** `P1 SEMANTIC CORE MERGED`  
> **Issue #1:** `BLOCKED BY AUTHENTIC SOURCE RECOVERY`

## Project identity

Velantrim Native Kernel is an independent, architecture-first and technology-neutral memory/event/replay research project.

```text
Architecture Canon
→ accepted abstract contracts
→ replaceable implementation profiles
→ reproducible evidence
```

PostgreSQL, SQLite, Python, files, graphs, vectors, LLMs, CPUs, GPUs and future substrates are research instruments. They do not define permanent semantic architecture.

## Mandatory distinctions

```text
accepted contract
≠ partial semantic-core implementation
≠ durable profile runtime
≠ tested storage adapter
≠ C1/C2/C3
≠ operational evidence
```

Operator approval authorizes a decision or phase. It is not empirical evidence.

## Accepted decisions and lineage

The repository accepts:

- ADR-0010 — foundational contract-family ownership;
- ADR-0011 — `nk-id/1.0` canonical identity;
- ADR-0012 — `nk-event/1.0` append/idempotency/order/replay boundary;
- ADR-0013 — `nk-deletion/1.0` restriction/deletion/retention semantics;
- ADR-0014 — `nk-fixtures/1.0` executable fixture/evidence protocol;
- RFC-0002 / ADR-0015 — clean PostgreSQL reference-profile lineage and bounded P1 semantic core.

```text
Profile ID:        native-kernel/postgresql-reference
Evidence lineage:  clean/postgresql-reference/0.1
Current phase:     P1
Operator approval: APPROVED
```

`NK-EPI-001…008` and ADR-0008 remain `PROPOSED`.

## P1 publication evidence

```text
PR:             #44
Final PR head:  273d9369e624d8e4c4033dc7842ebbcc46642668
Merge SHA:      9fd608f3f1d2915b961644015eb6b5e1a93e84d3
Merge method:   squash
Changed files:  30
Review threads: 0 unresolved
Codex review:   unavailable due external usage limit
```

P1 adds `native_kernel.semantic_core` using the Python standard library.

Implemented:

- deterministic canonical JSON and `nkh1` / `nkc1` / `nkl1` identity helpers;
- immutable semantic content, Claim identity, command and logical Event objects;
- explicit deny-by-default authority decisions;
- deterministic version-bound in-memory reducer;
- deletion/restriction transition semantics;
- admission and deletion Receipt overclaim guards;
- P1 implementation manifest, validator and workflow definition.

Manual review also corrected duplicated authority scope and hardened enum, timestamp, sequence, authority, Receipt and deletion inputs.

## Evidence boundary

Exact final-content validation in the available local environment:

```text
semantic-core tests:       20 PASS
P1-manifest tests:          4 PASS
AI-context validator tests: 7 PASS
Python compileall:          PASS
P1 manifest validator:      PASS
local interpreter:          Python 3.13.5
external dependencies:      NONE
```

The declared profile range is Python `>=3.11,<3.13`. No exact GitHub Actions run was created for the PR head or merge SHA, so Python 3.11/3.12 repository evidence remains `NOT_RECORDED`.

```text
local final-content evidence: LOCALLY_TESTED
repository workflow result:   NOT_RECORDED
Kernel runtime conformance:   UNSUPPORTED
C1/C2/C3:                     NOT_ESTABLISHED
```

The Python 3.13 local result is an extra compatibility check, not a substitute for the missing declared-range repository run.

## Explicitly absent

```text
PostgreSQL / SQLite adapter
SQL schema, driver or migrations
durable append and idempotency
writer lease persistence
authoritative replay and crash recovery
projection persistence and rebuild
network API
profile conformance adapter
C1 / C2 / C3
production security/privacy/deletion guarantees
```

The reducer handles supplied logical in-memory Events. It is not an authoritative history store and does not establish durable replay.

All 72 registered assertions remain runtime `UNSUPPORTED` until a future P4 conformance adapter emits complete assertion-scoped evidence.

## Clean-lineage and Issue #1 separation

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
≠ declaration that the historical source is globally lost
```

Issue #1 remains active and independent.

## Ecosystem boundary

P1 does not authorize Titan, Mentaury or Crystal runtime integration, shared storage, inherited identity, authority or conformance.

## Remaining gates

1. keep P2 PostgreSQL work blocked until separate operator GO;
2. settle Issue #18 publication/licensing terms;
3. define PostgreSQL version, driver, migration and writer-lease choices before P2;
4. preserve assertion-level runtime support as `UNSUPPORTED` until P4;
5. require an independent second profile before C3;
6. keep Issue #1 source recovery separately governed;
7. obtain exact Python 3.11/3.12 repository workflow evidence when execution becomes available.
