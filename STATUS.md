# Current Status

> **Date:** 2026-07-23  
> **Prototype track:** `v0.1.2.1`  
> **Repository status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`

## Project identity

Velantrim Native Kernel is an independent, personal, long-horizon architecture research project.

It is separate from the Crystal grant-facing product track. It may study or reuse ideas from Titan, Crystal, academic work, and external systems, but it follows its own architecture and evidence gates.

The project is architecture-first: it describes durable semantic and epistemic contracts while using modern technologies as replaceable implementation profiles and research instruments.

See [`docs/LONG_HORIZON_VISION.md`](./docs/LONG_HORIZON_VISION.md).

## Reading rule

This file is the current implementation boundary for this repository. Architectural documents may describe future mechanisms or future computational substrates, but only code and tests present in the repository count as implemented.

The following distinctions are mandatory:

```text
architecture Canon
≠ abstract contract
≠ implementation profile
≠ implemented runtime
≠ production evidence
```

## Current public repository state

The repository currently contains the research specification and governance boundary. The previously tested Python prototype and its 44-test suite are not yet merged into this repository.

Therefore the public repository may currently claim:

- a documented Native Kernel architecture;
- an independent long-horizon research vision;
- a separation between Architecture Canon, Abstract Contracts, and Implementation Profiles;
- an explicit Canon / Experimental / Anti-Canon separation;
- a staged roadmap;
- benchmark methodology;
- Titan and Crystal integration boundaries;
- a controlled import plan for the existing prototype;
- current technologies as candidate laboratory adapters rather than permanent architecture.

It must not yet claim:

- a runnable public kernel implementation;
- public reproduction of the 44-test result;
- production-ready event sourcing;
- complete write idempotency;
- full Event Integrity;
- multi-writer safety;
- universal linear-time context selection;
- genuine task sufficiency;
- production security or privacy;
- demonstrated portability across arbitrary hardware or future computational substrates;
- superiority of non-binary, neuromorphic, photonic, or other speculative execution models;
- that SQLite, graph, vector retrieval, LLMs, or conventional processors are rejected.

## Existing external prototype checkpoint

A local research snapshot identified as `v0.1.2.1` previously passed:

```text
44 deterministic tests
```

This result remains external evidence until the exact code, tests, environment, and commands are imported into a reviewable pull request and pass repository CI.

## Current implementation profile

The intended near-term laboratory profile may use:

- Python;
- SQLite or append-only files;
- FTS or lexical retrieval;
- graph adapters;
- vector or hybrid retrieval adapters;
- local or remote model adapters;
- conventional CPU/GPU execution.

These choices are implementation candidates. They do not redefine the Architecture Canon.

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

### Technology portability

Technology independence is currently an architectural target. It has not yet been demonstrated across multiple storage engines, runtimes, processors, or future computational substrates.

## Next repository gate

The next implementation PR should import the exact `v0.1.2.1` prototype and tests without semantic redesign, then establish:

1. reproducible Python environment;
2. exact test command;
3. CI on supported Python versions;
4. benchmark script and methodology;
5. code-to-document parity;
6. no unsupported production claims.

The long-horizon architecture track may continue in documentation and bounded research notes, but it must not alter the controlled import baseline.

Only after the import PR passes review may this status change from `DOCUMENTED_ONLY` to `RUNNABLE RESEARCH PROTOTYPE`.
