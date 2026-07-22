# Contributing

## Scope

Contributions should preserve the repository's research discipline and storage/model independence.

Good contributions include:

- deterministic tests;
- reproducible benchmarks;
- explicit invariants;
- failure-case documentation;
- projection adapters that do not become truth authorities;
- narrow performance improvements with semantic parity;
- threat-model and replay analysis.

Out of scope without a prior design discussion:

- claims of consciousness, personhood, or autonomous truth;
- replacing deterministic contracts with opaque LLM decisions;
- direct integration into Crystal Canon;
- broad rewrites that combine semantic, storage, and performance changes;
- production-readiness claims without evidence.

## Pull request requirements

A pull request should state:

1. the specific problem;
2. the invariant being preserved or changed;
3. tests added or updated;
4. benchmark method when performance is claimed;
5. failure and rollback behaviour;
6. whether the change affects Titan or Crystal boundaries.

## Status discipline

Use the following terms consistently:

- `DOCUMENTED_ONLY` — specification with no runtime claim;
- `RESEARCH` — active investigation, not a deliverable;
- `EXPERIMENTAL` — runnable mechanism without production assurance;
- `IMPLEMENTED` — present in the repository and covered by reviewable tests;
- `PRODUCTION-READY` — prohibited until a separate security, reliability, privacy, and operational gate is satisfied.

## Decision authority

Review comments and multi-model agreement are advisory. Only the repository maintainer or operator may move a proposal from research or proposed status into an accepted implementation decision.

## Import rule

The existing `v0.1.2.1` local prototype must be imported without silent refactoring. Any cleanup, package restructuring, semantic change, or benchmark change should occur in a later, separately reviewable PR.