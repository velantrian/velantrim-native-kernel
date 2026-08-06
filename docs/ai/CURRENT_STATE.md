# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-06  
**Last verified public `main`:** `ff88809fe7d7c79033a150140d20618e04aa1f9d`  
**Latest architecture decision:** PR #38 — ADR-0011…0014 accepted and approved  
**Repository status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`  
**Primary executable Kernel gate:** Issue #1 / authentic source recovery

> This is a last-verified checkpoint. Re-check the actual branch, PR and final merge SHA before relying on it.

```text
ACCEPTED ≠ IMPLEMENTED
APPROVED ≠ EMPIRICALLY PROVEN
FIXTURE TOOLING PASS ≠ KERNEL RUNTIME PASS
LOCALLY_TESTED ≠ REPOSITORY_REPRODUCED
WORKFLOW DECLARED ≠ WORKFLOW EXECUTED
C2 ≠ C3
```

## Accepted exact contracts

```text
ADR-0011 / nk-id/1.0:       ACCEPTED / APPROVED
ADR-0012 / nk-event/1.0:    ACCEPTED / APPROVED
ADR-0013 / nk-deletion/1.0: ACCEPTED / APPROVED
ADR-0014 / nk-fixtures/1.0: ACCEPTED / APPROVED
```

Publication evidence:

```text
PR:          #38
PR head:     5b003208d93774c1a79e770e8259dda99795eab7
Merge SHA:   ff88809fe7d7c79033a150140d20618e04aa1f9d
Changed:     18 files
Review:      0 unresolved threads / 0 actionable findings
Codex:       unavailable due external usage limit
```

The registry is `nk-contract-registry/1.1.0`. Exact assertions governed by ADR-0011–0014 are accepted. `NK-EPI-001…008` remains proposed with ADR-0008.

## Implementation and evidence status

```text
Fixture-integrity tooling:      IMPLEMENTED
Local focused tests:            8 PASS (PR #35 package evidence)
Kernel runtime:                 NOT IMPLEMENTED
Kernel runtime conformance:     UNSUPPORTED
Repository workflow execution:  NOT RECORDED
C2 Kernel profile:              NOT ESTABLISHED
C3 cross-profile evidence:      NOT ESTABLISHED
```

Recorded local evidence:

- 72 unique assertion IDs;
- 72 explicit assertion results from the non-runtime reader;
- two identity golden vectors matched;
- four invalid identity vectors rejected;
- two event-chain scenarios validated;
- two idempotency scenarios validated;
- payload tampering rejected;
- missing and duplicate adapter assertions rejected;
- two deletion lifecycle scenarios validated;
- positive and negative fixtures for `NK-EPI-001…008`.

## Workflow status

The conformance workflow now declares:

```text
pull_request path trigger
push to main path trigger
manual workflow_dispatch
Python 3.11 / 3.12 matrix
```

No run was created for PR #38 or merge SHA `ff88809…`. The GitHub connector has no workflow-dispatch action, and `gh` is unavailable in the local environment.

```text
workflow definition:            ACTIVE / MANUALLY DISPATCHABLE
repository run:                 NOT RECORDED
repository-reproduced evidence: NOT ESTABLISHED
```

This is not a PASS and not a test failure.

## Runtime boundary

The accepted contracts do not provide:

- a durable event store;
- reducer/upcaster execution;
- crash recovery;
- real projection rebuild;
- deletion/key-management implementation;
- PostgreSQL or SQLite adapters;
- a Kernel implementation adapter;
- C2/C3 evidence;
- production privacy, security, deletion or portability.

The built-in report continues to state:

```text
kernel_runtime_conformance: UNSUPPORTED
```

## Issue #1 separation

```text
accepted Issues #14–#17 architecture lineage
≠ recovered v0.1.2.1 source
≠ original 44-test suite
≠ controlled historical import
```

Issue #1 remains blocked by authentic source recovery and a separate operator GO.

## Cross-project boundary

PR #38 does not authorize Titan, Mentaury or Crystal runtime integration, shared authority, shared storage or inherited conformance.

## Next gates

1. Manually run `Conformance fixture integrity` in GitHub Actions and inspect exact jobs/artifacts.
2. Record that run in GitHub and Notion without overstating Kernel evidence.
3. Decide and specify the first clean implementation profile under a new evidence lineage.
4. Require two materially independent profiles before C3.
