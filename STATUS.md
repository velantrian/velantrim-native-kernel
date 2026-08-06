# Current Status

> **Verified:** 2026-08-06  
> **Last verified public `main`:** `1e721aeb5b116694a0dbb417c377aa9f92b6f8e5`  
> **Repository status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`  
> **Kernel runtime:** `NOT IMPLEMENTED`  
> **Issue #1:** `BLOCKED BY AUTHENTIC SOURCE RECOVERY`

## Project identity

Velantrim Native Kernel is an independent, architecture-first, technology-neutral memory/event/replay research project.

```text
Architecture Canon
→ accepted abstract contracts
→ replaceable implementation profiles
→ reproducible evidence
```

PostgreSQL, SQLite, files, graphs, vectors, LLMs, CPUs, GPUs and future substrates are research instruments. They do not define the permanent semantic architecture.

## Mandatory status distinctions

```text
accepted contract
≠ proposed implementation profile
≠ accepted profile plan
≠ runtime implementation GO
≠ tested runtime
≠ operational evidence
```

Operator approval is authority over architecture or planning promotion. It is not empirical evidence.

## Accepted architecture contracts

PR #38 accepted and published:

- ADR-0011 — `nk-id/1.0` canonical identity;
- ADR-0012 — `nk-event/1.0` single-writer append/idempotency/order/replay boundary;
- ADR-0013 — `nk-deletion/1.0` restriction/deletion/retention semantics;
- ADR-0014 — `nk-fixtures/1.0` executable fixture/evidence protocol.

```text
PR #38 merge: ff88809fe7d7c79033a150140d20618e04aa1f9d
PR #39 final checkpoint: 350734c8ce8d8cbc742def7df9f3d5044a5953ab
Decision: ACCEPTED
Approval: APPROVED
```

ADR-0010 remains the accepted family map. `NK-EPI-001…008` and ADR-0008 remain `PROPOSED`.

## Published PostgreSQL profile proposal

PR #41 publishes RFC-0002 as a proposal:

```text
PR #41 merge:       1e721aeb5b116694a0dbb417c377aa9f92b6f8e5
Profile ID:         native-kernel/postgresql-reference
Planning version:   nk-pg-profile/0.1-proposed
Evidence lineage:   clean/postgresql-reference/0.1
RFC status:         PROPOSED / DOCUMENTED_ONLY
Operator approval:  PENDING
Implementation:     NOT_STARTED
Runtime support:    UNSUPPORTED
```

The plan defines one authoritative writer, transaction/idempotency outcomes, PostgreSQL as a replaceable storage adapter, replay/rebuild, deletion inventory, neutral migration boundaries, tests/faults and C0→C5 promotion gates.

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
≠ declaration that historical source is globally lost
```

Issue #1 remains active and independent. Runtime work requires a separate operator GO after RFC review.

## Machine-readable planning manifest

`profiles/postgresql-reference-v0/profile-manifest.json` currently states:

```text
72 registry assertions mapped exactly once
64 accepted-family assertions: PLANNED
8 NK-EPI assertions: DEFERRED_PROPOSED_FAMILY
72 runtime-support results: UNSUPPORTED
72 evidence states: NONE
historical lineage: null
```

The planning validator and five focused local tests reject missing/duplicate assertions, false runtime support, historical lineage and silent `NK-EPI` promotion.

This validates the planning manifest, not a Kernel runtime.

## Implemented support tooling

The repository contains:

- registry `nk-contract-registry/1.1.0` with 72 assertions;
- schemas and conformance fixtures;
- standard-library conformance runner;
- eight focused fixture tests;
- profile-manifest validator with five focused tests;
- Python 3.11/3.12 workflow covering both artifact families.

Recorded local tooling evidence:

```text
conformance fixture tests: 8 PASS
profile manifest tests:     5 PASS
Kernel runtime:             UNSUPPORTED
```

## Repository CI boundary

No GitHub Actions run was created for PR #41 or merge `1e721aeb…`.

```text
local tooling evidence:       LOCALLY_TESTED
repository workflow evidence: NOT RECORDED
Kernel profile C1/C2:         NOT ESTABLISHED
C3 cross-profile equivalence: NOT ESTABLISHED
```

This is neither CI PASS nor test failure.

## Current public runtime boundary

No runnable Native Kernel implementation, PostgreSQL adapter, reducer, replay engine, projection system or deletion mechanism exists in `main`.

The repository must not claim:

- public reproduction of the historical 44-test checkpoint;
- PostgreSQL profile C1/C2/C3;
- production event sourcing, privacy, security or erasure;
- demonstrated portability across arbitrary current or future hardware;
- active Titan, Mentaury or Crystal runtime integration.

## Additional blockers before runtime

- RFC-0002 operator acceptance is pending;
- a separate runtime implementation GO is required;
- language, package layout, PostgreSQL version and writer lease are undecided;
- Issue #18 licensing/contribution terms remain unresolved;
- exact repository workflow evidence is missing.

## Immediate next gates

1. Record final PR #41 publication in GitHub and Notion.
2. Obtain an explicit operator decision on RFC-0002 and the clean profile lineage.
3. Resolve whether P1 may begin while Issue #1 remains active.
4. Resolve language/dependency/license/PostgreSQL-version decisions before runtime code.
5. Require a separate runtime GO before P1.
6. Implement and evidence each phase through separate PRs; require an independent second profile before C3.
