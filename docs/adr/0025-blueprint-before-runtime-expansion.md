# ADR-0025: Complete the architecture blueprint before further runtime expansion

- **Decision status:** `ACCEPTED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `PARTIAL`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-09`
- **Deciders:** `@velantrian`
- **Track:** `Architecture Canon`
- **Related:** `Issue #88`, `ADR-0001`, `ADR-0007`, `ADR-0024`
- **Tags:** `blueprint-first, architecture-refoundation, runtime-freeze, substrate-neutrality`

> [!IMPORTANT]
> This decision changes research priority and governance. It does not change runtime semantics, evidence, maturity, license terms, or the decision status of ADR-0024.

## Context 🧭

Native Kernel was created as a future-facing, substrate-neutral blueprint for durable memory, knowledge, meaning, provenance, uncertainty, conflict, revision, and explanation.

The repository already separates Architecture Canon, abstract contracts, and implementation profiles. However, practical work accumulated around Python, PostgreSQL, SQLite, CI, evidence bundles, and reducer behaviour before the full ontology and abstract Kernel machine were formed.

The existing P1–C5 implementation is useful. It exposed real architectural questions and produced bounded evidence. The risk is allowing that laboratory to become the architecture by inertia.

```text
available machinery
must not define
permanent semantic meaning
```

The operator explicitly redirected the project to complete its architecture blueprint before further semantic/runtime expansion.

## Inputs considered 🔍

Repository evidence:

- `ARCHITECTURE.md`, `docs/FOUNDATIONAL_INTENT.md`, and `docs/LONG_HORIZON_VISION.md` already state that current technologies are replaceable instruments;
- P1–C5 demonstrate a bounded reference lineage, not a complete substrate-neutral architecture;
- the active roadmap nevertheless centred the next work on license, reducer, and implementation-oriented gates;
- the current ontology, abstract machine, knowledge lifecycle, and substrate-independence obligations are distributed and incomplete.

Operator direction:

- return the project to its original future-facing architecture purpose;
- stop allowing modern systems and code to distract from formation of the blueprint;
- retain current implementation work as a laboratory rather than discard it.

## Decision drivers 🎯

- semantic durability;
- substrate neutrality;
- prevention of implementation-driven architecture;
- explicit epistemic boundaries;
- long-horizon portability;
- inspectable research progression;
- preservation of existing evidence and history.

## Considered options 🧪

### Option A — Continue the current implementation sequence

Proceed from license and ADR-0024 to NK-SAM, Event commitment, and reducer v2.

**Rejected because:** this keeps implementation pressure at the centre before the architecture blueprint is sufficiently complete.

### Option B — Delete or abandon the reference runtime

Remove Python/SQL work and restart as pure theory.

**Rejected because:** the existing runtime is valuable as a falsification instrument and its evidence/history must remain intact.

### Option C — Blueprint-first re-foundation with a bounded reference laboratory

Freeze new semantic/runtime expansion, preserve current code and evidence, and complete the architecture blueprint in explicit layers before authorizing new runtime work.

**Selected.**

## Decision ✅

Native Kernel enters an active **Architecture Re-foundation / Blueprint-first** phase.

The current P1–C5 clean implementation is classified as:

```text
BOUNDED REFERENCE LABORATORY
not architectural authority
not the final Kernel definition
```

No new semantic/runtime expansion is authorized until the blueprint completion gate is reviewed by the operator.

The blueprint phase must produce ten versioned deliverables:

1. Kernel purpose and non-goals;
2. knowledge and memory ontology;
3. abstract Native Kernel machine;
4. semantic laws and invariants;
5. identity, time, and change model;
6. knowledge lifecycle;
7. conflict, uncertainty, and revision model;
8. substrate-independence contract;
9. reference-implementation boundary;
10. open research questions and falsification criteria.

### Allowed work during the freeze

- architecture and ontology research;
- contract clarification that does not authorize runtime;
- integrity, security, reproducibility, and evidence-preservation fixes;
- truth-surface and validator repairs;
- isolated experiments explicitly designed to falsify a blueprint assumption;
- historical recovery under the existing provenance gate.

### Not authorized during the freeze

- reducer v2;
- new semantic Event verbs;
- new storage/runtime/language profiles;
- LLM, vector, Titan, Crystal, or Mentaury integration;
- performance-driven semantic changes;
- executable NK-EPI, Temporal, full Admission, or operational deletion;
- maturity or production promotion.

Issue #18 remains `PENDING_OPERATOR`. ADR-0024 remains `PROPOSED / PENDING_OPERATOR`. This decision does not choose or bypass either one.

### One-line rationale

> Native Kernel will complete the meaning-level blueprint before extending its laboratory implementation, preserving existing evidence while preventing current machinery from becoming permanent architecture by default.

## Consequences 📌

### Positive

- restores the original project centre of gravity;
- makes ontology and semantic laws explicit before more code;
- preserves present technologies as useful experiments without canonizing them;
- gives future profiles a clearer conformance target;
- reduces architecture drift caused by implementation convenience.

### Negative / accepted trade-offs

- feature and runtime expansion pauses;
- existing code may later require reclassification or replacement;
- blueprint work will expose unresolved philosophical and formal questions;
- current C4/C5 evidence remains bounded and may not map cleanly to the final blueprint.

### Neutral

- all current runtime and evidence identities remain readable and unchanged;
- the repository remains public without an operator-selected license;
- production authorization remains false.

## Invariants 🔒

1. Current implementation profiles cannot define Canon by existence.
2. Existing reducer-v1 histories and evidence remain immutable.
3. A blueprint document is not runtime evidence.
4. A future substrate claim requires named obligations and evidence, not futuristic language.
5. Modern technologies may be used as instruments without becoming architectural dependencies.
6. Runtime work resumes only through a separate explicit decision after blueprint review.
7. License and ADR-0024 authority remain separate from this priority decision.

## Architecture-layer placement

| Question | Answer |
|---|---|
| Architecture Canon changed? | `yes — research priority and completion gate` |
| Abstract contract changed? | `no runtime contract in this ADR` |
| Implementation profile selected? | `no` |
| Runtime code exists? | `existing bounded laboratory only` |
| Production evidence exists? | `no` |

## Validation and evidence 🧪

| Evidence | Result |
|---|---|
| Operator direction | approved in the project conversation and recorded in Issue #88 |
| Repository consistency | ADR, roadmap, machine/current-state surfaces, and AI guidance must agree |
| Runtime/evidence scope | unchanged |
| Next evidence | blueprint review artifacts and explicit falsification records |

## Failure cases 🚨

- adding code because a current library makes it convenient before its semantic obligation exists;
- describing a Python/SQL object as the ontology of the Kernel;
- treating a detailed blueprint as proof of feasibility;
- using the freeze to avoid integrity or evidence-preservation fixes;
- silently resuming runtime expansion under an unrelated maintenance PR;
- claiming arbitrary future hardware support without a mapping and equivalence model.

## Rollback / supersession

This decision may be superseded only by a later ADR that:

- identifies which blueprint deliverables are complete or intentionally rejected;
- records unresolved risks;
- defines the exact runtime scope being reopened;
- preserves existing history and evidence identities;
- receives explicit operator approval.

## References 📚

- [`../../ARCHITECTURE.md`](../../ARCHITECTURE.md)
- [`../FOUNDATIONAL_INTENT.md`](../FOUNDATIONAL_INTENT.md)
- [`../LONG_HORIZON_VISION.md`](../LONG_HORIZON_VISION.md)
- [`../ARCHITECTURE_REFOUNDATION.md`](../ARCHITECTURE_REFOUNDATION.md)
- [`../../ROADMAP.md`](../../ROADMAP.md)
