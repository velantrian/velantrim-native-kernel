# Current Status

> **Verified:** 2026-08-06  
> **Last verified public `main`:** `9ccbb535e22438092393e2686eb76eb362adb29d`  
> **Active P1 branch:** `agent/p1-semantic-core@5507901f688fffa49acc907de185acc287e27c63`  
> **Repository status:** `RESEARCH / P1 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`  
> **Issue #1:** `BLOCKED BY AUTHENTIC SOURCE RECOVERY`

## Project identity

Velantrim Native Kernel is an independent, architecture-first, technology-neutral memory/event/replay research project.

```text
Architecture Canon
→ accepted abstract contracts
→ replaceable implementation profiles
→ reproducible evidence
```

PostgreSQL, SQLite, Python, files, graphs, vectors, LLMs, CPUs, GPUs and future substrates are research instruments. They do not define the permanent semantic architecture.

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

## Accepted decisions

The repository accepts:

- ADR-0010 — foundational family ownership;
- ADR-0011 — `nk-id/1.0` canonical identity;
- ADR-0012 — `nk-event/1.0` append/idempotency/order/replay boundary;
- ADR-0013 — `nk-deletion/1.0` restriction/deletion/retention semantics;
- ADR-0014 — `nk-fixtures/1.0` executable fixture/evidence protocol;
- RFC-0002 / ADR-0015 — clean PostgreSQL reference-profile lineage and bounded P1 semantic-core implementation.

```text
Profile ID:       native-kernel/postgresql-reference
Evidence lineage: clean/postgresql-reference/0.1
Current phase:    P1
Operator approval: APPROVED
```

`NK-EPI-001…008` and ADR-0008 remain `PROPOSED`.

## P1 implementation reality

The active branch introduces `native_kernel.semantic_core` using Python 3.11+ standard library only.

Implemented:

- deterministic canonical JSON and identity helpers;
- immutable semantic content, Claim identity, command and logical Event objects;
- explicit deny-by-default authority decisions;
- deterministic version-bound in-memory reducer;
- deletion/restriction transition semantics;
- admission and deletion Receipt overclaim guards;
- P1 implementation manifest and validator;
- separate Python 3.11/3.12 workflow definition.

Recorded local validation:

```text
semantic-core tests: 20 PASS
P1-manifest tests:    4 PASS
Python compileall:    PASS
external dependencies: NONE
```

The provisional `nkd0` command digest and `nks0` state digest are profile-local implementation details, not accepted cross-profile contracts.

## Explicitly absent

```text
PostgreSQL / SQLite adapter
SQL schema, driver or migrations
durable append and idempotency
writer lease persistence
projection persistence and rebuild
network API
profile conformance adapter
C1 / C2 / C3
production security/privacy/deletion guarantees
```

The P1 reducer handles logical in-memory Events. It is not an authoritative history store and does not establish durable replay.

## Manifest boundary

Two records are intentionally distinct:

- `profile-manifest.json` — historical P0 proposal snapshot;
- `p1-manifest.json` — current accepted P1 implementation/evidence state.

All 72 registered assertions remain runtime `UNSUPPORTED` until a future P4 conformance adapter emits complete assertion-scoped evidence.

## Repository CI boundary

The P1 workflow definition is present on the active branch and supports PR, push-to-main and manual dispatch on Python 3.11/3.12.

Until an exact GitHub Actions run exists:

```text
local P1 evidence:           LOCALLY_TESTED
repository workflow result: NOT_RECORDED
Kernel runtime conformance: UNSUPPORTED
C1/C2/C3:                  NOT_ESTABLISHED
```

No missing run may be reported as PASS.

## Clean-lineage and Issue #1 separation

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
≠ declaration that the historical source is globally lost
```

Issue #1 remains active and independent.

## Ecosystem boundary

No P1 code authorizes Titan, Mentaury or Crystal runtime integration, shared storage, inherited identity, authority or conformance.

## Remaining gates

1. review and merge P1 with exact local and repository evidence;
2. preserve all assertion-level runtime support as `UNSUPPORTED` until P4;
3. settle Issue #18 publication/licensing terms;
4. require separate operator GO before P2 PostgreSQL work;
5. define PostgreSQL version, driver, migration and writer-lease choices before P2;
6. require an independent second profile before C3;
7. keep Issue #1 source recovery separately governed.
