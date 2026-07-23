# Contributing

## Scope

Contributions should preserve the repository's research discipline and storage/model/runtime/hardware independence at the contract level.

Good contributions include:

- deterministic tests;
- reproducible benchmarks;
- explicit invariants;
- failure-case documentation;
- projection adapters that do not become truth authorities;
- narrow performance improvements with semantic parity;
- threat-model and replay analysis;
- portability and migration experiments;
- ADRs that separate decisions, evidence, and implementation status;
- accurate English/Russian documentation parity.

Out of scope without a prior design discussion:

- claims of consciousness, personhood, or autonomous truth;
- replacing deterministic contracts with opaque LLM decisions;
- direct integration into Crystal Canon;
- inserting Crystal TruthGate as a Native Kernel dependency;
- broad rewrites that combine semantic, storage, and performance changes;
- checkpoint, OCC, CRDT, or conflict-resolution code hidden inside Issue #1 import;
- production-readiness or future-hardware portability claims without evidence.

## Pull request requirements

A pull request should state:

1. the specific problem;
2. the architecture layer affected;
3. the invariant being preserved or changed;
4. tests added or updated;
5. benchmark method when performance is claimed;
6. failure and rollback behaviour;
7. whether the change affects Titan or Crystal boundaries;
8. whether an ADR is required;
9. decision status, evidence level, and implementation status;
10. whether `README.md` and `README.ru.md` remain semantically aligned.

## ADR requirement

Create or update an ADR when a change affects:

- Architecture Canon;
- an abstract cross-technology contract;
- event vocabulary or replay semantics;
- checkpoint/snapshot semantics;
- conflict lifecycle;
- admission or epistemic policy;
- portability or migration guarantees;
- Titan or Crystal boundaries;
- a major implementation-profile commitment.

Use [`docs/adr/0000-template.md`](./docs/adr/0000-template.md).

Keep these dimensions separate:

```text
Decision status
≠ Evidence level
≠ Implementation status
```

An accepted ADR is an approved decision, not automatic proof that runtime code exists.

## Bilingual README rule

- `README.md` is English.
- `README.ru.md` is Russian.
- Both must retain a visible language selector.
- Substantive changes should update both versions in the same PR.
- Translation must preserve maturity, implementation, test, benchmark, security, ADR, and integration claims.

## Status discipline

Use the following terms consistently:

- `DOCUMENTED_ONLY` — specification with no runtime claim;
- `RESEARCH` — active investigation, not a deliverable;
- `PROPOSED` — suggested architectural change without approval;
- `EXPERIMENTAL` — runnable mechanism without production assurance;
- `IMPLEMENTED` — present in the repository and covered by reviewable tests;
- `PRODUCTION-READY` — prohibited until a separate security, reliability, privacy, and operational gate is satisfied.

## Decision authority

Review comments and multi-model agreement are advisory. Only the repository maintainer or operator may move a proposal into an accepted architecture or implementation decision.

## Import rule

The existing `v0.1.2.1` local prototype must be imported without silent refactoring. Any cleanup, package restructuring, semantic change, checkpoint implementation, conflict lifecycle, or benchmark change should occur in a later, separately reviewable PR.
