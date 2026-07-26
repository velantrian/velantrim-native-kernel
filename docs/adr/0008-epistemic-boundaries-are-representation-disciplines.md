# ADR-0008: Epistemic boundaries are representation disciplines, not a fixed worldview

- **Decision status:** `PROPOSED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Operator approval:** `PENDING`
- **Date:** `2026-07-26`
- **Deciders:** `@velantrian`
- **Track:** `Foundational Architecture`
- **Related:** `ARCHITECTURE.md`, `docs/WORLD_AND_EPISTEMIC_BOUNDARIES.md`, `docs/CONFORMANCE_MODEL.md`, Issue #17
- **Tags:** `epistemics, provenance, world-model, unknowns, metaphysics, conformance, portability`

> [!NOTE]
> This ADR proposes a technology- and worldview-neutral discipline for representing reality, transformations, origins, unknowns, and worldview claims. It does not claim runtime implementation, scientific closure, theological authority, or a change to Issue #1.

## Context 🧭

Native Kernel already separates truth from relevance, utility, freshness, write order, model output, and projection state. It preserves provenance, uncertainty, temporal meaning, conflict visibility, and explicit admission decisions.

A remaining gap is that the architecture does not yet state, in one durable decision, how to preserve distinctions such as:

```text
representation ≠ represented reality
observation    ≠ explanation
transformation ≠ origin
unknown        ≠ false
current limit  ≠ universal impossibility
worldview      ≠ unmarked empirical fact
```

Without an explicit boundary, future implementations could silently:

- treat a model or simulation as ontologically identical to its target;
- treat successful manipulation as proof of origin;
- fill provenance gaps with assumptions or generated narrative;
- convert current technical limits into eternal impossibility claims;
- promote religious, anti-religious, philosophical, or cultural positions into unmarked empirical Canon;
- introduce implementation-specific names such as `TruthGate`, `Guardian`, `L3`, or `GATE` as universal architecture.

## Problem

Define a stable epistemic discipline without prescribing a final ontology, scientific theory, religious doctrine, AI stack, processor, database, runtime, or future substrate.

## Decision drivers 🎯

- epistemic honesty;
- provenance continuity;
- explicit observer and method scope;
- anti-dogmatism;
- worldview neutrality;
- symmetry between metaphysical affirmation and negation;
- technology portability;
- compatibility with future scientific revision;
- conformance testability;
- separation of Canon, abstract contracts, and implementation profiles.

## Considered options 🧪

### Option A — Encode a fixed scientific-materialist worldview

**Advantages**

- superficially simple;
- aligns with some engineering communities;
- reduces vocabulary for non-empirical claims.

**Disadvantages**

- turns one worldview into an unmarked global invariant;
- cannot represent religious, philosophical, cultural, or ethical claims faithfully;
- risks treating current scientific boundaries as final;
- violates the project's technology- and observer-neutral ambition.

### Option B — Encode a fixed theological worldview

**Advantages**

- preserves a meaningful operator worldview;
- gives a declared answer to ultimate-origin questions.

**Disadvantages**

- closes empirical and provenance gaps without testable evidence;
- excludes other operators and domains;
- turns personal or cultural meaning into mandatory global Canon;
- risks a "God of the gaps" architecture;
- is not operationally testable as a general memory contract.

### Option C — Ignore metaphysical and ultimate-origin claims

**Advantages**

- keeps a narrow engineering surface;
- avoids direct worldview conflict.

**Disadvantages**

- silently discards real human knowledge domains;
- cannot preserve cultural, religious, philosophical, and ethical context;
- mistakes non-empirical scope for meaninglessness;
- prevents symmetrical classification of metaphysical affirmation and negation.

### Option D — Define a neutral discipline of representation

**Advantages**

- preserves different claim domains without collapsing them;
- keeps provenance gaps explicit;
- avoids turning current inability into universal impossibility;
- supports scientific revision and worldview diversity;
- is expressible through Claim, Event, Link, Epistemic State, Admission, and Receipt contracts;
- supports stable conformance assertions.

**Disadvantages**

- requires more explicit metadata and scope;
- does not provide emotionally or philosophically final answers;
- needs careful terminology and fixtures;
- may expose persistent unresolved questions.

## Proposed decision ✅

Adopt Option D.

Native Kernel SHOULD define epistemic boundaries as a discipline of representation rather than a final description of reality.

The architecture MUST preserve the following distinctions when applicable:

1. representation is not represented reality;
2. observation is not automatically explanation;
3. transformation or assembly is not proof of origin;
4. unknown is not false;
5. missing provenance is preserved as a provenance gap;
6. current inability is not universal impossibility;
7. worldview claims retain explicit domain and scope;
8. semantic layers are not silently promoted.

The abstract admission concept remains **Admission Policy**. Names such as `GATE`, `TruthGate`, `Guardian`, `L3`, LLM filters, human boards, and future mechanisms remain implementation-profile terms unless separately accepted through an ADR.

## Provenance Continuity Principle 🔗

Every durable Claim, state transition, decision, Receipt, and action SHOULD preserve traceable inputs, actors, methods, transformation chains, conditions, policy/profile versions, temporal scope, and known gaps within its declared contract.

Unknown provenance MUST NOT silently become:

- creation from nothing;
- originlessness;
- a preferred worldview explanation;
- generated continuity;
- proof of impossibility;
- permission to erase competing accounts.

## Open questions ❓

An open question SHOULD initially be represented as a Claim semantic pattern with evidence, missing evidence, hypotheses, observer limits, provenance gaps, candidate tests, falsification conditions, and review triggers.

This ADR does not create a mandatory `OpenQuestion` root primitive. A separate primitive requires evidence that existing contracts are insufficient.

## Conformance impact 🧪

The proposal defines documentation-level assertion IDs:

- `NK-EPI-001` — representation is not represented reality;
- `NK-EPI-002` — observation is not automatically explanation;
- `NK-EPI-003` — transformation is not origin;
- `NK-EPI-004` — unknown is not false;
- `NK-EPI-005` — provenance gaps remain explicit;
- `NK-EPI-006` — current inability is not universal impossibility;
- `NK-EPI-007` — worldview domain and scope remain explicit;
- `NK-EPI-008` — semantic layers are not silently promoted.

These identifiers do not claim executable fixtures or a conformance level. Fixture work belongs under Issue #17.

## Consequences ⚖️

### Positive

- future profiles can evolve without changing epistemic meaning;
- scientific breakthroughs do not automatically invalidate the Canon;
- religious and metaphysical claims can be preserved without becoming empirical authority;
- provenance gaps remain visible and reviewable;
- current method limits remain explicitly scoped;
- AI-specific mechanisms do not become universal architecture by vocabulary leakage.

### Costs

- Claim and Receipt profiles may require richer domain and scope metadata;
- conformance fixtures must distinguish missing and negative evidence;
- user interfaces may need to expose unresolved questions and competing frames;
- simplistic `KNOWN / UNKNOWN / UNKNOWABLE` schemas may require translation.

### Risks

- overly abstract wording may become non-operational;
- domain labels may be abused as truth labels;
- implementations may claim compliance without preserving gaps;
- worldview neutrality may be misrepresented as indifference or hostility.

### Mitigations

- stable assertion IDs;
- positive and negative conformance fixtures;
- explicit contract-to-test traceability;
- domain is not evidence status;
- observer scope and temporal status remain separate axes;
- operator approval remains separate from evidence.

## Non-goals 🚫

This ADR does not:

- define life, consciousness, matter, God, or reality conclusively;
- declare any current scientific limit permanent;
- declare every current limit temporary;
- adopt an AI-agent memory security profile as universal Canon;
- mandate local-first deployment, ACLs, encryption, prompts, models, or L3 terminology;
- create runtime code or tests;
- change `STATUS.md`;
- recover or replace `v0.1.2.1`;
- alter Issue #1 or its controlled-import boundary;
- upgrade project maturity.

## Acceptance criteria 📋

The ADR may become `ACCEPTED` only after explicit operator approval and review confirms that:

- the foundational specification is technology- and worldview-neutral;
- no implementation-profile term is promoted into Canon;
- the eight assertion IDs are traceable from architecture prose to the conformance model;
- OpenQuestion remains a semantic pattern unless separately justified;
- `STATUS.md` and Issue #1 remain unchanged;
- Notion mirrors GitHub without becoming the authoritative specification.

## Rollback and supersession 🔄

Because this ADR is documentation-only, rollback consists of reverting the associated documentation commits or superseding this ADR.

Any superseding ADR must preserve the historical reasoning and explicitly address representation, provenance gaps, observer limits, worldview scope, and semantic promotion.

## Related documents 📚

- [`../WORLD_AND_EPISTEMIC_BOUNDARIES.md`](../WORLD_AND_EPISTEMIC_BOUNDARIES.md)
- [`../../ARCHITECTURE.md`](../../ARCHITECTURE.md)
- [`../CONFORMANCE_MODEL.md`](../CONFORMANCE_MODEL.md)
- [`0001-architecture-canon-vs-implementation-profiles.md`](./0001-architecture-canon-vs-implementation-profiles.md)
- [`0007-operator-approval-is-not-evidence.md`](./0007-operator-approval-is-not-evidence.md)
- [Issue #17](https://github.com/velantrian/velantrim-native-kernel/issues/17)
