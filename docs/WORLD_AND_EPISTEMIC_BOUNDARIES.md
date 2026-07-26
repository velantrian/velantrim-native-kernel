# 🌍 World, Provenance, and Epistemic Boundaries

> **Decision status:** `PROPOSED`  
> **Evidence level:** `DOCUMENTED`  
> **Implementation status:** `NOT_STARTED`  
> **Operator approval:** `PENDING`  
> **Track:** `Foundational Architecture`  
> **Scope:** technology-, model-, runtime-, storage-, hardware-, and worldview-neutral  
> **Issue #1 impact:** `NONE`

## 1. Purpose

This document defines how Velantrim Native Kernel represents reality, models, transformations, origins, unknowns, and worldview claims without pretending that a representation is the represented world.

It does not prescribe a physical theory, biological theory, religious doctrine, model provider, processor, database, runtime, or future computational substrate.

It establishes a discipline of representation.

```text
represented reality
        ≠
observation
        ≠
measurement
        ≠
interpretation
        ≠
model
        ≠
Claim
```

## 2. Independence of represented reality

Native Kernel MUST preserve the distinction between:

- a represented object or process;
- a signal or observation about it;
- a measurement procedure and result;
- an interpretation of the signal;
- a model or symbolic representation;
- a Claim about the object;
- an action performed on the object;
- the provenance or origin attributed to the object.

A representation MUST NOT automatically be treated as ontologically identical to what it represents.

Successful prediction, simulation, imitation, reconstruction, or reproduction of behaviour MUST NOT by itself prove identity with the represented process or internal state.

## 3. Required distinctions

Native Kernel MUST preserve the following distinctions where they are relevant to the declared domain:

1. **Observation** — receipt of a signal, record, testimony, or other evidence candidate.
2. **Measurement** — comparison through a declared procedure, scale, frame, and uncertainty model.
3. **Interpretation** — assignment of meaning under declared assumptions.
4. **Transformation** — alteration of an existing state, structure, or process.
5. **Assembly** — formation of a configuration from available components.
6. **Synthesis** — production through declared inputs, conditions, resources, and processes.
7. **Reproduction** — repetition of a structure, behaviour, function, or process.
8. **Modelling** — construction of a bounded representation.
9. **Explanation** — a causal, formal, mechanistic, statistical, narrative, or other declared account with a stated scope.
10. **Provenance** — the traceable history of sources, inputs, transformations, actors, conditions, and gaps.
11. **Origin Claim** — an assertion about how an object, process, rule, or state came to exist.
12. **Ultimate-Origin Claim** — an assertion about final or absolute grounds of existence, potentially outside a declared empirical frame.

Success at one layer MUST NOT silently be treated as proof of success at another layer.

```text
observation      ≠ explanation
transformation   ≠ origin
assembly         ≠ ultimate origin
reproduction     ≠ identity
behaviour        ≠ inner state
model            ≠ represented reality
```

## 4. Provenance Continuity Principle

Every durable Claim, state transition, decision, Receipt, and action SHOULD identify, within its declared scope:

- sources and inputs;
- actors or originating systems;
- observation or acquisition method;
- transformation chain;
- conditions and resources;
- policy and implementation-profile versions;
- temporal scope;
- known provenance gaps;
- contested or incompatible provenance accounts.

A missing provenance segment MUST be represented as a provenance gap.

A provenance gap MUST NOT silently be converted into:

- creation from nothing;
- absence of any origin;
- a preferred worldview explanation;
- model-generated continuity;
- proof of impossibility;
- permission to erase competing accounts.

## 5. Observer and method limits

Knowledge claims are evaluated relative to declared capabilities and frames, including where relevant:

- available observation methods;
- sensor or interface resolution;
- concepts and representation language;
- computational or non-computational capabilities;
- temporal and spatial access;
- historical context;
- domain and jurisdiction;
- testability conditions;
- implementation-profile limitations.

A limitation of one observer, method, implementation profile, or era MUST NOT automatically become a universal limit on reality.

```text
cannot observe now
        ≠
cannot ever be observed

cannot reproduce with this profile
        ≠
impossible in principle
```

A claim of impossibility MUST declare the frame and grounds under which impossibility is asserted.

## 6. Unknowns and open questions

Native Kernel MUST:

- preserve unknowns explicitly;
- distinguish missing evidence from negative evidence;
- distinguish an unanswered question from a false Claim;
- preserve competing hypotheses where policy permits;
- identify missing evidence and provenance gaps;
- expose observer and method limits;
- preserve review triggers and supersession history;
- prevent unmarked assumptions from filling gaps;
- allow revision when methods, observations, concepts, or declared frames change.

Native Kernel MUST NOT declare a question universally unknowable only because the current profile lacks a verification method.

A formal non-resolvability result MAY be recorded only within an explicit formal system, assumptions, scope, and proof provenance.

### OpenQuestion semantic pattern

An open question SHOULD initially be representable as a Claim pattern rather than a new mandatory root primitive:

```yaml
claim_kind: QUESTION
epistemic_disposition: OPEN
domain: []
known_evidence: []
missing_evidence: []
competing_hypotheses: []
observer_limits: []
provenance_gaps: []
candidate_tests: []
falsification_conditions: []
review_triggers: []
```

A separate `OpenQuestion` contract requires an independent ADR and evidence that the existing Claim, Event, Link, Epistemic State, and Receipt contracts are insufficient.

## 7. Multi-axis epistemic description

A single `KNOWN / UNKNOWN / UNKNOWABLE` enum is insufficient for general architecture because it collapses independent dimensions.

Implementations SHOULD be able to preserve or translate dimensions such as:

| Dimension | Example values |
|---|---|
| **Evidence status** | `UNSUPPORTED`, `OBSERVED`, `CORROBORATED`, `REPLICATED`, `CONTESTED` |
| **Inference status** | `DESCRIPTIVE`, `INFERRED`, `HYPOTHESIZED`, `SPECULATIVE` |
| **Testability** | `TESTABLE_NOW`, `TESTABLE_WITH_EXTENSION`, `CURRENTLY_UNTESTABLE`, `NON_EMPIRICAL_IN_FRAME` |
| **Provenance status** | `TRACEABLE`, `PARTIAL`, `UNKNOWN`, `CONTESTED` |
| **Observer scope** | `OBSERVER_RELATIVE`, `SYSTEM_RELATIVE`, `DOMAIN_RELATIVE`, `UNIVERSAL_CLAIM` |
| **Claim domain** | `EMPIRICAL`, `FORMAL`, `METAPHYSICAL`, `ETHICAL`, `CULTURAL` |
| **Temporal status** | `CURRENT`, `HISTORICAL`, `PROVISIONAL`, `SUPERSEDED` |

These values are examples for contract design, not a frozen implementation schema.

## 8. Empirical, formal, cultural, and metaphysical claims

Native Kernel MUST be able to represent different claim domains without silently collapsing them.

A metaphysical, religious, philosophical, cultural, ethical, empirical, or formal claim MUST retain an explicit domain and scope when that distinction affects interpretation or admission.

A metaphysical or religious Claim MUST NOT automatically:

- be removed as noise;
- be promoted to universal empirical fact;
- close an unexplained causal or provenance gap;
- replace missing evidence;
- be prohibited merely because it is non-empirical in the declared frame.

The same discipline applies symmetrically to absolute metaphysical negations.

A worldview Claim MAY be preserved as a declared operator belief, cultural statement, tradition, hypothesis, or philosophical position. It MUST NOT become an unmarked global empirical invariant.

## 9. Anti-dogmatic constraints

Native Kernel MUST NOT:

- treat representation as represented reality;
- treat observation as complete explanation;
- treat transformation as proof of origin;
- treat assembly as proof of ultimate origin;
- treat reproduced behaviour as proof of internal identity;
- treat missing evidence as negative evidence;
- treat unknown as false;
- treat absent provenance as originlessness;
- treat current inability as universal impossibility;
- treat confidence, frequency, utility, recency, or consensus as evidence by themselves;
- treat a worldview as an unmarked empirical fact;
- treat lack of a worldview commitment as empirical disproof;
- close an open question merely to produce a complete narrative;
- silently promote an observation, model, hypothesis, retrieval result, useful outcome, or proposal into admitted knowledge.

## 10. Admission and semantic promotion

No mechanism MAY silently promote meaning between semantic layers.

Promotion MUST be explicit, policy-governed, and auditable where the architecture requires admission.

```text
Observation
    ↓ explicit policy decision
Claim candidate
    ↓ explicit admission and evidence evaluation
Derived epistemic state
```

The abstract architectural concept is **Admission Policy**.

Names such as `GATE`, `TruthGate`, `Guardian`, `L3`, model output filters, human review boards, or future biological or formal mechanisms belong to implementation profiles unless separately accepted as abstract contracts.

## 11. Conformance assertions

This proposal introduces the following documentation-level assertion identifiers:

| Assertion ID | Meaning |
|---|---|
| `NK-EPI-001` | representation is not represented reality |
| `NK-EPI-002` | observation is not automatically explanation |
| `NK-EPI-003` | transformation is not origin |
| `NK-EPI-004` | unknown is not false |
| `NK-EPI-005` | provenance gaps remain explicit |
| `NK-EPI-006` | current inability is not universal impossibility |
| `NK-EPI-007` | worldview domain and scope remain explicit |
| `NK-EPI-008` | semantic layers are not silently promoted |

The IDs are stable documentation targets. They do not imply executable fixtures, a conformance level, or runtime implementation.

## 12. Non-goals

This document does not:

- claim that any current scientific boundary is permanent;
- claim that every boundary is temporary;
- define life, consciousness, matter, or reality conclusively;
- establish a religious or anti-religious doctrine;
- make LLMs, AI agents, SQLite, Python, vectors, graphs, CPU, GPU, or any current technology part of the permanent Canon;
- create a new event verb;
- create a mandatory `OpenQuestion` root primitive;
- alter the controlled source-recovery and import scope of Issue #1;
- claim a runnable Native Kernel implementation;
- change project maturity or production status.

## 13. Canonical formula

> Native Kernel observes, represents, transforms, compares, and audits without identifying its representations with reality. It preserves provenance where traceable and provenance gaps where unknown. It does not turn unknowns into inventions, current limits into eternal prohibitions, or worldviews into unmarked facts. The boundaries of knowledge, life, consciousness, matter, and origin remain open research questions rather than predeclared answers.

## 14. Related documents

- [`../ARCHITECTURE.md`](../ARCHITECTURE.md)
- [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md)
- [`adr/0001-architecture-canon-vs-implementation-profiles.md`](./adr/0001-architecture-canon-vs-implementation-profiles.md)
- [`adr/0008-epistemic-boundaries-are-representation-disciplines.md`](./adr/0008-epistemic-boundaries-are-representation-disciplines.md)
- [`LONG_HORIZON_VISION.md`](./LONG_HORIZON_VISION.md)
