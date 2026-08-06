# Current Status

> **Verified:** 2026-08-06  
> **Last verified public `main`:** `ff88809fe7d7c79033a150140d20618e04aa1f9d`  
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
≠ implemented runtime
≠ tested runtime
≠ wired integration
≠ enabled deployment
≠ operational evidence
```

Operator approval is authority over architecture. It is not empirical evidence.

## Accepted architecture contracts

PR #38 accepted and published:

- ADR-0011 — `nk-id/1.0` canonical identity;
- ADR-0012 — `nk-event/1.0` single-writer append/idempotency/order/replay boundary;
- ADR-0013 — `nk-deletion/1.0` restriction/deletion/retention semantics;
- ADR-0014 — `nk-fixtures/1.0` executable fixture/evidence protocol.

```text
PR #38 head:  5b003208d93774c1a79e770e8259dda99795eab7
Merge SHA:    ff88809fe7d7c79033a150140d20618e04aa1f9d
Decision:     ACCEPTED
Approval:     APPROVED
```

ADR-0010 remains the accepted family-ownership map:

```text
NK-SEM — semantic roles
NK-ID  — identity and canonical encoding
NK-EVT — event, observation and recorded change
NK-AUT — authority and admission
NK-CFL — conflict and explicit unknowns
NK-EQV — conformance and semantic equivalence
```

`NK-EPI-001…008` and ADR-0008 remain `PROPOSED`.

## Exact accepted boundaries

### Identity

- NFC UTF-8 canonical JSON subset;
- sorted keys and compact encoding;
- binary floats and explicit null forbidden in identity-bearing objects;
- content, Claim, lineage and storage identity separated;
- domain-separated SHA-256 identifiers `nkh1`, `nkc1`, `nkl1`;
- collisions are hard incidents;
- migrations preserve inspectable aliases and lineage.

### Event, append and replay

- one authoritative writer in v1;
- durable idempotency scope;
- same key plus different command digest is rejected;
- contiguous global and stream sequence;
- history append precedes disposable projection updates;
- hash chain is an integrity signal, not authenticity or consensus;
- replay binds schema/upcaster/reducer versions.

Accepted event vocabulary remains:

```text
ADMIT · LINK · UTILIZED · SUPERSEDED · ERASED
```

### Deletion and restriction

```text
logical ERASED
≠ restriction
≠ physical deletion
≠ crypto-erasure
≠ global-erasure proof
```

Profiles must declare data locations, authority, policy, retries, partial completion, retention holds, restore quarantine, key-destruction evidence and Receipt limits.

### Conformance fixtures

The accepted protocol requires stable assertion IDs, versioned schemas/fixtures, declared equivalence classes, explicit assertion results, no silent skip, and exact evidence limitations.

## Implemented support tooling

The repository contains:

- registry `nk-contract-registry/1.1.0` with 72 assertion IDs;
- schemas and evidence-report contract;
- identity, event, idempotency, deletion and epistemic fixtures;
- standard-library conformance runner;
- eight focused tests;
- Python 3.11/3.12 workflow with PR, push and manual `workflow_dispatch` entry points.

Recorded local package evidence:

```text
8 tests PASS
72 unique assertion IDs
72 explicit assertion statuses
2 identity golden vectors matched
4 invalid identity vectors rejected
2 event-chain scenarios validated
2 idempotency scenarios validated
2 deletion scenarios validated
NK-EPI-001…008 positive + negative coverage
```

The built-in reader deliberately reports:

```text
support_state: SUPPORTED
kernel_runtime_conformance: UNSUPPORTED
```

## Repository CI boundary

No GitHub Actions run was created for PR #38 or merge `ff88809…`. The workflow is active and now supports manual dispatch, but the connected GitHub integration cannot dispatch it and the local environment has no authenticated `gh` executable.

```text
local fixture evidence:         LOCALLY_TESTED
repository workflow evidence:   NOT RECORDED
Kernel profile C2:              NOT ESTABLISHED
C3 cross-profile equivalence:   NOT ESTABLISHED
```

This is neither CI PASS nor test failure.

## Current public runtime boundary

No runnable Native Kernel implementation or original Kernel regression suite is present in `main`.

The repository must not claim:

- a durable event store, reducer, replay engine or deletion runtime;
- public reproduction of the historical 44-test checkpoint;
- C2/C3 Kernel conformance;
- production event sourcing, privacy, security or erasure;
- demonstrated portability across arbitrary current or future hardware;
- active Titan, Mentaury or Crystal runtime integration.

## Issue #1 source-recovery blocker

The reported external checkpoint remains:

```text
v0.1.2.1
44 deterministic tests reported externally
source and original suite not located in accessible sources
```

Accessible search supports `NOT_FOUND_IN_ACCESSIBLE_SOURCES`, not `GLOBALLY_LOST`.

Issue #1 remains independent from ADR-0011–0014. The accepted exact contracts are new architecture lineage, not recovered historical design.

## Immediate next gates

1. Execute `Conformance fixture integrity` manually in GitHub Actions and record run/job/artifact evidence.
2. Define the first clean implementation profile under a new version/evidence lineage if authentic source recovery remains blocked.
3. Implement assertion-scoped profile adapters before any C2 claim.
4. Build two materially independent profiles before C3.
5. Keep Issue #1 source recovery and all cross-project integrations separately governed.
