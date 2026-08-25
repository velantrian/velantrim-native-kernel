# OpenClaw Conformance Specimen v0.1

Status: RESEARCH SPECIMEN ONLY
Date: 2026-08-24

## Purpose

OpenClaw is an external implementation specimen that may be used to challenge or falsify Native Kernel hypotheses about substrate-neutral semantics. It is not an authority source and does not modify current H11, runtime freeze, Final Canon, or production state.

## Candidate properties to test

1. Manifest-first discovery can remain semantically meaningful across different runtime/plugin implementations.
2. Typed capability contracts can survive replacement of concrete providers and transports.
3. Atomic publication of runtime/provider snapshots can preserve consistency under implementation replacement.
4. Explicit roles/capabilities can be mapped into technology-neutral authorization semantics without inheriting vendor-specific policy.
5. Separation of scheduler, task ledger, lifecycle hook, and action authority can survive substrate changes.

## Non-invariants

The following MUST NOT be promoted to Native Kernel invariants merely because OpenClaw implements them:

- one long-lived gateway process;
- WebSocket transport;
- a specific plugin manifest shape;
- in-process plugin loading;
- transcript compaction;
- any persona/workspace file convention;
- any concrete queue, provider, or channel implementation.

## Falsification questions

For each candidate property, test:

- Does the semantic claim survive replacement of OpenClaw's concrete technology?
- Is the property necessary, or merely one convenient implementation?
- Can an alternative implementation preserve the intended human/system capability without the same mechanism?
- Does the mechanism accidentally transfer authority that belongs to another domain?

## Boundary

`external implementation evidence != Native Kernel invariant`

`working implementation != universal law`

`conformance specimen != authorization`

No candidate in this document changes H11 status. H11 remains subject to its existing independent reviewer/reproducer requirements. Runtime remains frozen unless separately authorized through Native Kernel governance.
