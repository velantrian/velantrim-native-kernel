# Current Status

> **Date:** 2026-07-22  
> **Prototype track:** `v0.1.2.1`  
> **Repository status:** `RESEARCH / DOCUMENTATION-FIRST / NOT PRODUCTION-READY`

## Reading rule

This file is the current implementation boundary for this repository. Architectural documents may describe future mechanisms, but only code and tests present in the repository count as implemented.

## Current public repository state

The repository currently contains the research specification and governance boundary. The previously tested Python prototype and its 44-test suite are not yet merged into this repository.

Therefore the public repository may currently claim:

- a documented Native Kernel architecture;
- an explicit Canon / Experimental / Anti-Canon separation;
- a staged roadmap;
- benchmark methodology;
- Titan and Crystal integration boundaries;
- a controlled import plan for the existing prototype.

It must not yet claim:

- a runnable public kernel implementation;
- public reproduction of the 44-test result;
- production-ready event sourcing;
- complete write idempotency;
- full Event Integrity;
- multi-writer safety;
- universal linear-time context selection;
- genuine task sufficiency;
- production security or privacy.

## Existing external prototype checkpoint

A local research snapshot identified as `v0.1.2.1` previously passed:

```text
44 deterministic tests
```

This result remains external evidence until the exact code, tests, environment, and commands are imported into a reviewable pull request and pass repository CI.

## Known architectural limitations

### Broad-query scaling

Typical read-path work was substantially reduced through event indexing and charge caching, but broad queries remain superlinear because neighbour discovery and greedy ablation still contain repeated work.

### Write idempotency

Read-time deduplication is not equivalent to durable command idempotency. Duplicate writes require an explicit event-level contract.

### Evidence integrity

A non-empty evidence string is only a hygiene condition. It is not source verification, cryptographic evidence, or proof of truth.

### Event-envelope integrity

A future event envelope must bind ordering, actor, timestamp, schema version, idempotency key, payload commitment, and previous hash under an explicit threat model.

### Conflict semantics

Candidate and canonical conflicts are separated conceptually, but directionality, admission, resolution, and lifecycle policy remain research work.

### Context selection

The current prototype uses lexical proxy ablation. It must not be described as proven sufficient or globally minimal evidence selection.

## Next repository gate

The next PR should import the exact `v0.1.2.1` prototype and tests without semantic redesign, then establish:

1. reproducible Python environment;
2. exact test command;
3. CI on supported Python versions;
4. benchmark script and methodology;
5. code-to-document parity;
6. no unsupported production claims.

Only after that PR passes review may this status change from `DOCUMENTATION-FIRST` to `RUNNABLE RESEARCH PROTOTYPE`.