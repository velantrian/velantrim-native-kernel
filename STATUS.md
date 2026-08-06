# Current Status

> **Verified:** 2026-08-06  
> **Repository status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`  
> **Kernel runtime:** `NOT IMPLEMENTED`  
> **Issue #1:** `BLOCKED BY AUTHENTIC SOURCE RECOVERY`

## Project identity

Velantrim Native Kernel is an independent, personal, long-horizon architecture research project.

It is architecture-first and technology-neutral:

```text
Architecture Canon
→ accepted abstract contracts
→ replaceable implementation profiles
→ reproducible evidence
```

Current technologies are research instruments. PostgreSQL, SQLite, files, graphs, vectors, LLMs, CPUs, GPUs and future substrates do not define the permanent semantic architecture.

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

The repository accepts:

- ADR-0010 — foundational contract-family ownership;
- ADR-0011 — `nk-id/1.0` canonical identity;
- ADR-0012 — `nk-event/1.0` single-writer append/idempotency/order/replay boundary;
- ADR-0013 — `nk-deletion/1.0` restriction/deletion/retention semantics;
- ADR-0014 — `nk-fixtures/1.0` executable fixture/evidence protocol.

Accepted family map:

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

No additional event verb is accepted by ADR-0011–0014.

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

The accepted fixture protocol requires:

- stable assertion IDs;
- versioned schemas and fixture corpora;
- byte/structural/semantic/behavioural equivalence classes;
- explicit supported/unsupported/partial/failed assertion results;
- no silent skip;
- exact evidence reports and profile limitations.

## Implemented support tooling

The repository contains:

- `contracts/registry.json` with 72 assertion IDs;
- schema and evidence-report bundles;
- identity, event, idempotency, deletion and epistemic fixtures;
- `tools/conformance/runner.py`;
- eight focused unit tests;
- a Python 3.11/3.12 workflow with PR, push and manual-dispatch entry points.

Recorded local evidence:

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

The built-in reader reports:

```text
support_state: SUPPORTED
kernel_runtime_conformance: UNSUPPORTED
```

This means the fixture-integrity reader completed. It does not mean a Kernel runtime exists.

## Repository CI boundary

The workflow definition is active and now declares `workflow_dispatch`. An exact repository run has not yet been recorded for this acceptance state.

Therefore:

```text
local fixture evidence:         LOCALLY_TESTED
repository workflow evidence:   NOT YET RECORDED
Kernel profile C2:              NOT ESTABLISHED
C3 cross-profile equivalence:   NOT ESTABLISHED
```

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

Do not reconstruct an approximation and label it `v0.1.2.1`. Controlled import requires:

1. authentic source archive or location;
2. documented lineage;
3. preserved read-only container and hashes;
4. original test inventory;
5. explicit operator GO.

Issue #1 remains independent from ADR-0011–0014. The accepted exact contracts are new architecture lineage, not recovered historical design.

## Other architecture tracks

- ADR-0009 accepts PostgreSQL as preferred full profile and SQLite as optional embedded profile; adapters remain unimplemented.
- Curiosity Core remains `PROPOSED / DOCUMENTED_ONLY / NOT IMPLEMENTED`.
- Causal relations placement under ADR-0006 is accepted; causal runtime remains absent.
- ADR-0008 world/epistemic boundaries remain proposed.

## Immediate next gates

1. Merge and record the ADR-0011–0014 acceptance PR and exact SHA.
2. Execute the conformance workflow through GitHub Actions and record run/job/artifact evidence.
3. Define the first clean implementation profile under a new version/evidence lineage if authentic source recovery remains blocked.
4. Implement assertion-scoped profile adapters before any C2 claim.
5. Build two materially independent profiles before C3.
6. Keep Issue #1 source recovery and all cross-project integrations separately governed.
