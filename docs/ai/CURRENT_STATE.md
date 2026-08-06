# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-06  
**Last verified public `main`:** `3243336dc7ff7ef88583c6f2c419c375c26947cf`  
**Latest merged package:** PR #35 exact-contract proposals + PR #36 continuity checkpoint  
**Repository status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`  
**Primary executable Kernel gate:** Issue #1 / Stage 0.5 authentic source recovery

> This is a last-verified checkpoint, not an automatically updated database. Compare it with the actual branch or PR before relying on it.

```text
DOCUMENTED ≠ IMPLEMENTED
PROPOSED ≠ ACCEPTED
MERGED ≠ ACCEPTED
FIXTURE TOOLING PASS ≠ KERNEL RUNTIME PASS
LOCALLY_TESTED ≠ REPOSITORY_REPRODUCED
WORKFLOW ACTIVE ≠ WORKFLOW RUN EXECUTED
C2 ≠ C3
Operator approval ≠ empirical evidence
```

## Public `main` reality

`main` now contains:

- Architecture Canon and accepted ADR-0010 family ownership;
- ADR-0011 through ADR-0014 as **PROPOSED** exact contracts;
- bilingual identity, append/replay, deletion and fixture-protocol documents;
- 72 assertion IDs, schemas and executable fixture corpora;
- hardened standard-library fixture-integrity tooling;
- eight focused tests;
- active `Conformance fixture integrity` workflow definition;
- no public Native Kernel runtime;
- no authentic `v0.1.2.1` source or original 44-test suite.

## Publication evidence

```text
PR #35 final head:          270596d672f740cc9123d506af3b10f50e691ad6
PR #35 squash merge:        0552ae284d56148972e9bcc8de5f80a7f462c0f3
PR #36 checkpoint head:     b116abe8bc4a9dc1848c03b6f84d2b6633584532
PR #36 squash merge:        3243336dc7ff7ef88583c6f2c419c375c26947cf
PR #35 changed files:       24
Unresolved review threads:  0
Actionable review comments: 0
```

Codex automated review was unavailable because the external review service reached its usage limit. This is not a code finding.

## Decision status

```text
ADR-0011 — canonical identity v1:             PROPOSED / APPROVAL PENDING
ADR-0012 — single-writer append/replay v1:    PROPOSED / APPROVAL PENDING
ADR-0013 — deletion/restriction/retention v1: PROPOSED / APPROVAL PENDING
ADR-0014 — executable fixture protocol v1:    PROPOSED / APPROVAL PENDING
Fixture-integrity tooling:                    IMPLEMENTED IN MAIN
Kernel runtime:                               NOT IMPLEMENTED
Kernel runtime conformance:                   UNSUPPORTED
C3 cross-profile evidence:                    NOT ESTABLISHED
```

Publishing the ADR files does not accept them.

## Local fixture evidence

Recorded during PR #35 authoring and hardening:

- `8 PASS` focused tests;
- 72 unique assertion IDs;
- 72 explicit `UNSUPPORTED` assertion results from the non-runtime reader;
- two identity golden vectors matched;
- four invalid identity vectors rejected;
- two event-chain scenarios and two idempotency scenarios validated;
- payload-hash tampering rejected;
- incomplete and duplicated adapter assertion reports rejected;
- two deletion lifecycle scenarios validated;
- positive and negative fixtures for every `NK-EPI-001…008`.

## GitHub Actions status

The workflow is registered and active:

```text
Workflow: Conformance fixture integrity
Workflow ID: 328870784
Matrix: Python 3.11 / 3.12
```

No GitHub Actions workflow run or GitHub Actions check suite was created for:

- PR #35 final head;
- PR #35 merge `0552ae…`;
- PR #36 head;
- PR #36 merge `324333…`, despite a matching `contracts/**` push path.

Repository Actions permissions/settings could not be read through the connected integration (`403 Resource not accessible by integration`). External app check suites were queued on the commit, but no GitHub Actions suite existed.

Therefore the exact status is:

```text
workflow definition:             ACTIVE
local fixture evidence:          LOCALLY_TESTED / PASS
repository workflow execution:   NOT_TRIGGERED / NOT_RECORDED
repository-reproduced evidence:  NOT ESTABLISHED
```

This is neither a test failure nor a PASS. A user-originated push or manual workflow dispatch in GitHub is required to establish the first repository run; the current connector cannot perform workflow dispatch.

## Issue #1 separation

```text
Issues #14–#17 proposal lineage
≠ controlled v0.1.2.1 import
≠ recovered source
≠ original 44-test evidence
```

Issue #1 remains blocked by operator-controlled authentic source recovery.

## Claims allowed

May claim:

- exact contracts and fixture tooling are published in `main`;
- local fixture validation passed eight focused tests;
- the runner prevents silent assertion skips and reports Kernel support as `UNSUPPORTED`;
- the workflow definition is active.

Must not claim:

- ADR-0011–0014 accepted before explicit operator approval;
- repository-reproduced CI evidence;
- runnable Kernel or implemented durable append/replay/deletion;
- C2/C3 Kernel conformance;
- production security, privacy, erasure or portability;
- historical recovery or active ecosystem integration.

## Remaining gates

1. Explicit operator decision on ADR-0011…0014: `ACCEPT`, `REVISE` or `REJECT`.
2. User-originated GitHub Actions execution and exact run evidence.
3. Future implementation-profile mappings and real replay/deletion evidence.
4. Two materially independent profiles before C3.
5. Issue #1 authentic-source gate remains independent.
