# Contributing

## Mandatory first read

Before auditing or changing the repository, read:

1. [`AGENTS.md`](./AGENTS.md);
2. [`STATUS.md`](./STATUS.md);
3. [`docs/ai/README.md`](./docs/ai/README.md);
4. [`docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md`](./docs/ai/DOCUMENTATION_SYNC_PROTOCOL.md);
5. the relevant ADRs, risks, component-map sections and recent work-log entries.

Verify the actual branch/PR SHA. Context documents are last-verified checkpoints, not automatically live state.

## Scope

Contributions should preserve research discipline and storage/model/runtime/hardware independence at the contract level.

Good contributions include:

- deterministic tests and executable conformance artifacts;
- reproducible benchmarks;
- explicit invariants;
- failure-case documentation;
- projection adapters that do not become truth authorities;
- narrow performance improvements with semantic parity;
- threat-model, replay, erasure and migration analysis;
- ADRs that separate decisions, evidence, implementation and approval;
- accurate English/Russian documentation parity;
- complete AI/human hand-off records.

Out of scope without prior design discussion:

- claims of consciousness, personhood or autonomous truth;
- replacing deterministic contracts with opaque model decisions;
- direct integration into another project's Canon;
- inserting Crystal TruthGate, Titan cognition policy or Mentaury identity policy as a Kernel dependency;
- broad rewrites combining semantic, storage and performance changes;
- checkpoint, OCC, CRDT or conflict-resolution code hidden inside Issue #1 import;
- production-readiness or future-hardware portability claims without evidence.

## Pull request requirements

A PR should state:

1. the problem and exact base/head SHA;
2. the architecture layer affected;
3. the invariant preserved or changed;
4. tests/checks and exact results;
5. benchmark method when performance is claimed;
6. failure and rollback behaviour;
7. provenance and remaining limitations;
8. whether Titan, Mentaury or Crystal boundaries are affected;
9. whether an ADR is required;
10. decision status, evidence level, implementation status and operator approval;
11. whether paired bilingual documents remain aligned;
12. documentation impact: `NONE`, `GITHUB_ONLY` or `GITHUB_AND_NOTION`;
13. direct Notion synchronization or a structured hand-off.

Use the repository PR template and do not remove its documentation-synchronization block.

## Documentation continuity requirement

Material changes must update the relevant context surfaces:

- `docs/ai/CURRENT_STATE.md` for verified state changes;
- `docs/ai/KNOWN_RISKS.md` for risk changes;
- `docs/ai/COMPONENT_MAP.md` for ownership/first-read changes;
- `docs/ai/WORK_LOG.md` for significant work;
- ADR/RFC for durable decisions;
- affected `STATUS`, roadmap, profile, conformance, integration, security and user documents;
- Notion in the same cycle or `docs/ai/NOTION_HANDOFF.md`.

GitHub must preserve the complete public technical and audit package without requiring Notion access.

## ADR requirement

Create or update an ADR when a change affects:

- Architecture Canon;
- an abstract cross-technology contract;
- event vocabulary or replay semantics;
- checkpoint/snapshot semantics;
- conflict lifecycle;
- admission or epistemic policy;
- portability or migration guarantees;
- Titan, Mentaury or Crystal boundaries;
- a major implementation-profile commitment;
- source-recovery or evidence-lineage policy.

Use [`docs/adr/0000-template.md`](./docs/adr/0000-template.md).

Keep these dimensions separate:

```text
Decision status
≠ Evidence level
≠ Implementation status
≠ Operator approval
```

An accepted ADR is an approved decision, not proof that runtime code exists.

## Bilingual documentation rule

- `README.md` is English; `README.ru.md` is Russian.
- Both retain visible language selectors.
- Substantive paired changes should update both versions in the same PR.
- Translation must preserve maturity, implementation, test, benchmark, security, ADR and ecosystem claims.

## Status discipline

Use consistently:

- `DOCUMENTED_ONLY` — specification with no runtime claim;
- `RESEARCH` — active investigation, not a deliverable;
- `PROPOSED` — suggested change without approval;
- `ACCEPTED` — operator-approved decision, not automatic implementation;
- `EXPERIMENTAL` — runnable mechanism without production assurance;
- `IMPLEMENTED` — present at exact SHA in declared scope;
- `TESTED` — committed test evidence with known result;
- `WIRED`, `ENABLED`, `OBSERVED` — separate runtime claims;
- `PRODUCTION-READY` — prohibited until separate security, reliability, privacy and operational gates pass.

## Decision authority

Review comments and multi-model agreement are advisory.
Only the maintainer/operator may accept architecture or authorize promotion.
Approval is not empirical evidence.

## Import rule

The reported `v0.1.2.1` checkpoint may be imported only from authentic recovered source with original test inventory and operator GO.
Do not silently refactor, reconstruct or approximate it.
Cleanup, redesign, new profiles, checkpoints, conflict lifecycle and benchmark changes belong in later, separately reviewable work under honest lineage.
