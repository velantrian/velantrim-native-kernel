# Velantrim Native Kernel

> **Status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`  
> **Current prototype track:** `v0.1.2.1`  
> **Relationship:** independent Velantrim research project; not part of Crystal runtime

Velantrim Native Kernel explores a storage- and model-independent memory substrate built around immutable claims, an append-only event history, deterministic state reconstruction, typed relationships, explicit temporal validity, auditable context selection, and receipts.

The project is intentionally narrow: it studies the information and memory kernel beneath higher-level agents. It does not claim consciousness, human-like cognition, autonomous truth, or production readiness.

## Core shape

```text
Claim
→ immutable Event Log
→ deterministic Epistemic State projection
→ rebuildable read models and indexes
→ task-specific context selection
→ auditable Receipt
```

The event history is intended to remain authoritative. SQLite, graph, vector, FTS, and other indexes are treated as replaceable projections rather than independent truth authorities.

## Research objectives

- preserve architecture across database, model-provider, and hardware changes;
- separate semantic identity from storage representation;
- reconstruct current state deterministically from history;
- expose provenance, conflicts, temporal validity, and selection decisions;
- keep truth admission separate from relevance and utility;
- evaluate the kernel through reproducible tests and Offline Shadow before any live integration.

## Current maturity boundary

The active research prototype has previously reached a locally verified `v0.1.2.1` checkpoint with 44 deterministic tests. The code and tests are not yet part of this public repository's `main` branch; they require a separate reviewable import PR.

The architecture does **not** yet claim:

- complete write-level idempotency;
- full event-envelope integrity;
- multi-writer concurrency guarantees;
- universally linear context selection;
- complete bi-temporal semantics;
- proven task sufficiency or genuine minimal evidence grip;
- production security or privacy readiness;
- live integration with Titan or Crystal.

See [`STATUS.md`](./STATUS.md) for the exact implementation boundary.

## Repository map

```text
README.md                         project overview and reading rule
STATUS.md                         current implementation truth
ARCHITECTURE.md                   formal shape, invariants, and boundaries
ROADMAP.md                        staged research and validation plan
docs/BENCHMARKS.md                benchmark methodology and known limits
docs/INTEGRATION_BOUNDARIES.md    Titan and Crystal separation rules
SECURITY.md                       research-stage security policy
CONTRIBUTING.md                   contribution and decision rules
prototype/README.md               controlled import plan for v0.1.2.1 code/tests
```

## Relationship to Titan and Crystal

- **Titan / Full Exo-Cortex** is the broader research environment in which Native Kernel ideas may be evaluated.
- **Crystal** is an independent, grant-facing verifiable-memory product. Crystal does not depend on this repository.
- No Native Kernel event log may write directly to Crystal Canon.
- Any future transfer into Crystal requires a separate RFC, threat model, tests, reproducible evaluation, review, and explicit maintainer approval.

See [`docs/INTEGRATION_BOUNDARIES.md`](./docs/INTEGRATION_BOUNDARIES.md).

## Research discipline

The repository distinguishes:

- **Canon Shape** — stable architectural form worth preserving;
- **Experimental** — mechanisms currently under evaluation;
- **Anti-Canon** — claims or shortcuts explicitly rejected.

Architecture is not promoted because it is elegant or because multiple language models agree. Promotion requires reproducible evidence, tests, failure analysis, rollback behaviour, and an explicit operator decision.

## License

No open-source license has been granted yet. The repository is public for research visibility and review, but the absence of a license does not grant permission to copy, modify, redistribute, or deploy the material.