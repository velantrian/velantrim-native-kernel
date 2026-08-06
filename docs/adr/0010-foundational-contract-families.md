# ADR-0010: Separate foundational contracts by semantic role

- **Decision status:** `ACCEPTED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-06`
- **Deciders:** `@velantrian`
- **Track:** `Architecture Canon / Abstract Contract`
- **Related:** `Issues #14, #15, #16, #17; ADR-0001, ADR-0003, ADR-0004, ADR-0007, ADR-0008; PR #28`
- **Tags:** `semantic-model, identity, events, authority, conflict, conformance`

> [!NOTE]
> Native Kernel is currently an architecture-first project. The risk is not only missing runtime code; it is allowing an overloaded `Claim`, one event schema, one database, or one authority mechanism to become the implicit architecture before the foundational responsibilities are separated.

## Context 🧭

The repository already documents Claims, Events, provenance, temporal meaning, conflict visibility, admission, deterministic reduction, rebuildable projections, Receipts, and conformance levels.

However, several foundational boundaries were distributed across architecture prose, the world/epistemic boundary proposal, the conformance model, and Issues #14–#17.

- **Problem:** future profiles could use the same terminology while assigning different meanings to Claim roles, identity, recorded events, authority, conflict, unknowns, or equivalence.
- **Constraints:** remain technology-neutral; preserve the current maturity boundary; do not alter Issue #1; do not invent implementation evidence; do not accept new event verbs implicitly.
- **Non-goals:** select a database, programming language, ontology, runtime, model provider, hash algorithm, multi-writer protocol, or deletion mechanism.
- **Current implementation boundary:** no public Native Kernel runtime implements these contracts.
- **Source-derived facts:** Issues #14–#17 already identify missing identity, append/replay, deletion, and executable-conformance contracts.
- **Open uncertainty:** exact schemas, canonical bytes, authority roles, event envelopes, conflict lifecycle, and fixture formats still require separate decisions and evidence.

## Inputs considered 🔍

```text
Repository evidence:
- ARCHITECTURE.md
- docs/CONFORMANCE_MODEL.md
- docs/WORLD_AND_EPISTEMIC_BOUNDARIES.md
- ADR-0001, 0003, 0004, 0007, 0008, 0009
- Issues #14, #15, #16, #17
- STATUS.md and docs/ai risk/context records

External research:
- none required for this organizational decision

AI-generated inputs:
- architecture audit identified overloaded semantic roles and missing authority/identity joints

Operator interpretation and decision:
- the immediate project goal is an architecture, framework, foundation, and skeleton rather than a complete runtime
- the six-family skeleton was explicitly accepted on 2026-08-06
```

AI-generated inputs are design inputs, not approval or implementation evidence. Operator acceptance is recorded separately and does not substitute for runtime evidence.

## Decision drivers 🎯

- semantic durability;
- epistemic honesty;
- explicit authority;
- conflict visibility;
- deterministic replay readiness;
- portability;
- testability;
- migration and compatibility;
- resistance to technology lock-in;
- bounded architectural complexity.

## Considered options 🧪

### Option A — Continue with distributed prose only

**Description**

Keep the current concepts in separate documents and let future implementers infer how they fit together.

**Advantages**

- no new taxonomy;
- minimal documentation change.

**Disadvantages**

- high risk of inconsistent profile mappings;
- no stable family IDs for fixtures and evidence;
- overloaded Claim/Event concepts remain easy to misinterpret;
- authority and unknown handling can remain implicit.

### Option B — Freeze one complete universal schema now

**Description**

Define mandatory entities, fields, enums, serialization, and runtime behaviour for all six areas in one decision.

**Advantages**

- immediate implementation target;
- simple short-term consistency.

**Disadvantages**

- prematurely binds Canon to an untested representation;
- combines too many independent decisions;
- risks making current software assumptions permanent;
- cannot honestly claim evidence or cross-profile portability.

### Option C — Adopt a six-family skeleton with stable assertion namespaces

**Description**

Separate responsibilities into six contract families while deferring exact schemas and algorithms to focused ADRs, issues, fixtures, and profile evidence.

**Advantages**

- clarifies architecture without pretending to implement it;
- provides stable traceability targets;
- keeps current technology replaceable;
- allows details to evolve independently;
- maps directly to existing issues and conformance levels.

**Disadvantages**

- introduces another architectural document;
- requires ongoing bilingual and registry discipline;
- does not itself solve canonical encoding, event integrity, deletion, or runtime conformance.

## Decision ✅

**We will:**

1. organize the foundational architecture into six contract families:
   - `NK-SEM` — semantic roles;
   - `NK-ID` — identity and canonical encoding;
   - `NK-EVT` — event, observation, and recorded change;
   - `NK-AUT` — authority and admission;
   - `NK-CFL` — conflict and explicit unknowns;
   - `NK-EQV` — conformance and semantic equivalence;
2. use stable assertion IDs inside each family;
3. keep `Claim` as the current durable root record while requiring semantic-role distinctions or explicit translations;
4. require authoritative transitions to preserve the meaning of an Authority Envelope;
5. require conflict and unknown states to remain explicit rather than forcing a silent winner;
6. map mature assertions to versioned fixtures, profile mappings, evidence records, and declared equivalence classes;
7. keep exact schemas, canonical bytes, event envelopes, lifecycle verbs, deletion mechanisms, and profile implementations in separately reviewed work.

**We will not:**

- accept a new event verb through this umbrella ADR;
- define a mandatory database schema or class hierarchy;
- equate the accepted assertion namespaces with executable conformance;
- change Issue #1 or claim that the historical external checkpoint used this skeleton;
- treat operator approval as empirical or implementation evidence.

### One-line rationale

> In the context of an architecture-first, technology-neutral memory substrate, facing overloaded concepts and profile drift, we selected a six-family contract skeleton to preserve semantic boundaries and traceability, accepting additional governance work because a premature universal schema would hard-code unproven assumptions.

## Consequences 📌

### Positive

- semantic objects, identity, events, authority, conflict, and equivalence have separate ownership;
- future schemas and profiles receive stable mapping targets;
- issues and fixtures can evolve without redefining the whole architecture;
- cross-project authority leakage becomes easier to detect;
- unknowns and conflicts remain first-class architecture concerns.

### Negative / accepted trade-offs

- more documentation and bilingual synchronization are required;
- exact runtime design remains unresolved;
- some existing terminology will need mapping rather than direct reuse;
- future changes to stable assertion IDs require explicit compatibility and supersession handling.

### Neutral

- current repository maturity remains `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`;
- no implementation profile is selected or activated;
- no source-recovery result changes;
- acceptance does not create C1–C5 conformance evidence.

## Invariants 🔒

1. Semantic content, source assertion, observation, evidence, admission, and epistemic state are not silently collapsed.
2. Content, Claim, lineage, Event, and storage identity remain distinguishable.
3. A represented-world occurrence is not equated with the system record about it.
4. Storage presence, retrieval, utility, confidence, repetition, or model output does not imply authority.
5. Candidate conflict, established conflict, resolution, and unknown remain distinct.
6. Equivalence is versioned and explicitly defined.
7. Unsupported assertions remain visible.
8. Current technology remains an implementation profile, not permanent Canon.
9. Issue #1 controlled import remains separate.

## Architecture-layer placement

| Question | Answer |
|---|---|
| Architecture Canon changed? | `yes — accepted foundational organization and boundaries` |
| Abstract contract changed? | `yes — accepted taxonomy and assertion namespaces` |
| Implementation profile selected? | `no` |
| Runtime code exists? | `no` |
| Production evidence exists? | `no` |

## Implementation notes 🔧

- normative architecture map: `docs/FOUNDATIONAL_CONTRACT_SKELETON.md` and Russian counterpart;
- documentation navigation and ADR index must expose ADR-0010 as accepted;
- AI context map, known risks, and work log must preserve the acceptance/evidence distinction;
- future exact identity work remains in Issue #14;
- future append/replay work remains in Issue #15;
- future deletion/restriction work remains in Issue #16;
- future executable fixtures and runner remain in Issue #17;
- no Titan, Mentaury, or Crystal runtime integration is authorized.

## Validation and evidence 🧪

| Evidence | Artifact / command | Result | Required for next level |
|---|---|---|---|
| Documentation | foundational skeleton + ADR | accepted/documented | maintain bilingual and reference consistency |
| Link/status validation | AI-context guard / repository review | required on final PR/main head | clean structural result |
| Unit tests | not applicable to docs-only decision | none | future schemas/encoders/runners |
| Replay test | not implemented | absent | Issue #15/#17 artifacts |
| Cross-profile evidence | not implemented | absent | two independent profiles |
| Operator approval | explicit decision on 2026-08-06 | approved | does not replace empirical evidence |

## Failure cases 🚨

- treating conceptual roles as a frozen universal ontology;
- presenting assertion IDs as passing tests;
- letting profile-specific names become universal authority contracts;
- adding event verbs without separate compatibility review;
- collapsing unknown into false;
- forcing a conflict winner through write order;
- using this document to claim the missing historical source was reconstructed;
- claiming runtime implementation or portability merely because the architecture was accepted.

## Rollback / supersession

- Because no runtime contract is implemented, supersession currently requires documentation and compatibility handling rather than data migration.
- After acceptance, supersession must preserve aliases and migration guidance for contract/evidence references.
- A future alternative is justified if the six-family split prevents necessary semantics, creates irreducible overlap, or fails cross-profile fixture design.
- ADR-0010 remains historical evidence even if superseded.

## Consistency checklist 🔱

- [x] Event history remains authoritative about recorded changes.
- [x] History is not equated with truth.
- [x] Projection/cache is not promoted to Canon.
- [x] Relevance/utility is not equated with truth.
- [x] Candidate conflict is not described as resolved conflict.
- [x] Current technology is not silently promoted to permanent architecture.
- [x] Titan and Crystal boundaries remain explicit.
- [x] Issue #1 import scope is not silently expanded.
- [x] Decision status, evidence level, implementation status, and approval remain separate.

## References 📚

- [`../FOUNDATIONAL_CONTRACT_SKELETON.md`](../FOUNDATIONAL_CONTRACT_SKELETON.md)
- [`../FOUNDATIONAL_CONTRACT_SKELETON.ru.md`](../FOUNDATIONAL_CONTRACT_SKELETON.ru.md)
- [`../../ARCHITECTURE.md`](../../ARCHITECTURE.md)
- [`../CONFORMANCE_MODEL.md`](../CONFORMANCE_MODEL.md)
- [`../WORLD_AND_EPISTEMIC_BOUNDARIES.md`](../WORLD_AND_EPISTEMIC_BOUNDARIES.md)
- [Issue #14](https://github.com/velantrian/velantrim-native-kernel/issues/14)
- [Issue #15](https://github.com/velantrian/velantrim-native-kernel/issues/15)
- [Issue #16](https://github.com/velantrian/velantrim-native-kernel/issues/16)
- [Issue #17](https://github.com/velantrian/velantrim-native-kernel/issues/17)
