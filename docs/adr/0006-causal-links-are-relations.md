# ADR-0006: Causal links are relations, not knowledge types

- **Decision status:** `ACCEPTED`
- **Evidence level:** `DOCUMENTED` + `OPERATOR_APPROVED`
- **Implementation status:** `NOT_STARTED`
- **Date:** `2026-07-25`
- **Deciders:** `@velantrian`
- **Track:** `Abstract Contract`
- **Related:** `Issue #1`, `PR #11`, `ADR-0005`, `ROADMAP.md`, Notion decision `D-NK-09`
- **Tags:** `causality, relations, topology, epistemics, lineage, temporal-semantics`

> [!NOTE]
> This decision prevents causality from collapsing three independent axes: decay policy, epistemic status, and topology. It accepts the architectural direction without claiming that a causal runtime, schema, event verb, or repository-reproduced implementation already exists.

## Context 🧭

Native Kernel needs a durable place for statements such as “A contributes to B” or “A causes B under conditions C.” A local or external prototype has been reported to use a `LINK` with `relation = "CAUSES"`, but no executable source or test proving that behaviour exists in public `main`.

Two tempting representations would overload existing fields:

- `knowledge_type: CAUSAL_LINK` would mix causal meaning with decay or retention policy;
- `parents` would mix causal topology with Claim lineage.

Both options make future replay, conflict handling, temporal queries, and adapter replacement harder because one field would carry several unrelated meanings.

- **Problem:** choose the abstract location of causal semantics without inventing runtime evidence.
- **Constraints:** preserve independent semantic axes, deterministic replay, provenance, explicit temporal meaning, and rebuildable projections.
- **Non-goals:** implement a causal engine, add an event verb, canonize a confidence formula, import Titan's `CausalContextBuilder`, or expand Issue #1.
- **Current implementation boundary:** public `main` contains documentation only; the reported external prototype has not been imported.
- **Source-derived facts:** the architecture already separates knowledge type, epistemic state, lineage, and link topology conceptually.
- **Open uncertainty:** directed-link payload, evidence policy, mechanism representation, temporal lag, intervention semantics, query API, and implementation profile.

## Inputs considered 🔍

```text
Repository evidence:
- architecture separates knowledge type, epistemic state, lineage, and topology
- public main contains no runtime implementation or causal contract tests
- directed-link and full bi-temporal contracts remain future work

External / local observations:
- an uncommitted prototype was reported to represent CAUSES as a LINK relation
- that observation remains EXTERNALLY_OBSERVED until exact import and reproduction

AI-generated inputs:
- proposals to add CAUSAL_LINK as a knowledge type
- proposals to reuse parents for causal ancestry
- proposals to introduce a dedicated causal read model

Operator interpretation:
- causality belongs on a typed directed relation
- implementation must wait for directed-link and temporal contracts
- the decision is accepted; implementation is not started
```

AI-generated inputs and external prototype reports are design inputs, not repository implementation evidence.

## Decision drivers 🎯

- semantic separation;
- deterministic replay;
- epistemic honesty;
- provenance and temporal clarity;
- portability across graph and non-graph profiles;
- conflict visibility;
- testability;
- bounded implementation scope;
- compatibility with future Titan research without making Titan Canon.

## Considered options 🧪

### Option A — Represent causality as `knowledge_type`

**Advantages**

- simple filtering;
- superficially compact schema.

**Disadvantages**

- confuses what a Claim means with how it decays or is retained;
- cannot naturally represent multiple causal relations between ordinary Claims;
- makes policy and topology inseparable.

### Option B — Represent causality through `parents`

**Advantages**

- reuses an existing lineage-like field;
- avoids a new relation contract.

**Disadvantages**

- destroys the distinction between derivation lineage and world-model causality;
- makes replay and provenance interpretation ambiguous;
- cannot express conditional, negative, or scoped causal relations safely.

### Option C — Represent causality as a typed directed relation

**Advantages**

- preserves independent semantic axes;
- allows evidence, provenance, scope, polarity, mechanism, and temporal metadata to evolve explicitly;
- supports graph and non-graph implementation profiles;
- permits a future causal read model without redefining Claim identity.

**Disadvantages**

- depends on a directed-link contract;
- requires explicit admission, temporal, conflict, and Receipt rules;
- does not by itself prove causal truth.

## Decision ✅

**We will:**

- represent causal semantics through a typed, directed relation such as `CAUSES`;
- keep causal assertions subject to explicit evidence, provenance, admission, temporal, conflict, and Receipt policies;
- treat any causal graph, index, traversal, score, or `CausalContextBuilder` as a rebuildable implementation profile or higher-level integration module;
- specify the concrete payload and query contract only after directed-link and temporal semantics are defined;
- preserve `D-NK-09` as the external decision identifier linking Notion and this ADR.

**We will not:**

- change `knowledge_type` to encode causality;
- overload `parents`, which remains lineage;
- treat relation existence, relation weight, embedding similarity, repeated use, or model confidence as causal proof;
- claim that `CAUSES` exists in public runtime code until committed code and tests demonstrate it;
- add a causal runtime, event vocabulary, or Titan integration through this documentation-only decision;
- expand or refactor the controlled `v0.1.2.1` import in Issue #1.

### One-line rationale

> In the context of future causal reasoning, facing the risk of collapsing decay, belief, lineage, and topology, we selected typed directed relations to preserve semantic separation, accepting a later and more explicit contract because causal meaning must remain auditable and portable.

## Consequences 📌

### Positive

- knowledge type, epistemic status, lineage, and topology remain separate;
- graph and non-graph profiles can implement the same abstract relation;
- causal evidence and uncertainty can remain visible;
- a future causal read model can be deleted and rebuilt without becoming a second Canon.

### Negative / accepted trade-offs

- implementation is blocked on directed-link and temporal contracts;
- causal assertions need more metadata and validation than a bare edge;
- migration from any external prototype may require an explicit adapter or upcast.

### Neutral

- ordinary Claim selection, charge, PULL, and conflict behaviour do not change through this ADR;
- a numeric edge weight, if used by a profile, remains ranking policy rather than semantic truth.

## Invariants 🔒

1. `knowledge_type` does not encode causal topology.
2. `parents` expresses lineage, not causation.
3. Causal direction is explicit and is not inferred from write order.
4. A causal relation does not become true merely because it exists in a graph or projection.
5. Canonical causal assertions require policy-defined evidence and provenance.
6. Temporal validity, system knowledge time, and technical write order remain distinct.
7. Causal projections and indexes are rebuildable from authoritative recorded history.
8. Similarity, salience, utility, frequency, and model confidence are not causal evidence.
9. Missing causal evidence may remain `UNKNOWN` or `INSUFFICIENT_EVIDENCE`.
10. No implementation or event-vocabulary claim is created by this ADR alone.
11. Issue #1 remains an exact baseline import without causal redesign.

## Architecture-layer placement

| Question | Answer |
|---|---|
| Architecture Canon changed? | `no` |
| Abstract contract changed? | `accepted future relation placement` |
| Implementation profile selected? | `no` |
| Runtime code exists? | `no public repository evidence` |
| Production evidence exists? | `no` |

## Implementation notes 🔧

Before implementation, a separate RFC or ADR must define at least:

- relation identity and direction;
- source and target Claim requirements;
- evidence and provenance references;
- valid-time and known-time semantics;
- conditions, polarity, mechanism, lag, and scope where applicable;
- admission and authorization;
- contradiction, supersession, and retraction behaviour;
- deterministic replay and migration/upcast rules;
- projection rebuild and query semantics;
- Receipt fields and honest reproducibility level.

The current roadmap places implementation after the directed-link contract. Full bi-temporal semantics may be a dependency for canonical causal assertions. Titan's `CausalContextBuilder`, counterfactual reasoning, interventions, and causal discovery remain higher-level research concerns.

## Validation and evidence 🧪

| Evidence | Artifact / command | Result | Required for next level |
|---|---|---|---|
| Documentation | ADR-0006 + ADR index + Roadmap | semantic placement recorded | review consistency |
| Operator approval | Notion `D-NK-09` | architectural direction accepted | preserve cross-link |
| Unit tests | none | `NOT_STARTED` | typed-relation contract tests |
| Replay test | none | `NOT_STARTED` | deterministic directed-link replay |
| Benchmark | none | not applicable yet | only after implementation |
| Offline Shadow | none | `NOT_STARTED` | only after bounded runtime exists |

## Failure cases 🚨

- an adapter maps `CAUSES` into `knowledge_type`;
- an implementation interprets lineage parents as causal parents;
- an undirected projection loses causal direction;
- a relation weight is presented as causal confidence or proof;
- causal truth changes because write order changes;
- missing evidence is silently treated as support;
- a projection becomes the only copy of causal meaning;
- a Titan-specific ontology silently becomes Native Kernel Canon.

## Rollback / supersession

This ADR may be superseded if a reviewed experiment shows that typed relations cannot preserve the required causal semantics or portability. A superseding ADR must preserve historical readability, define migration, and explain the evidence that changed the decision.

## Consistency checklist 🔱

- [x] Event history remains authoritative about recorded changes.
- [x] History is not equated with truth.
- [x] Projection/cache is not promoted to Canon.
- [x] Relevance/utility is not equated with truth.
- [x] Candidate conflict is not described as resolved conflict.
- [x] Current technology is not silently promoted to permanent architecture.
- [x] Titan and Crystal boundaries remain explicit.
- [x] Issue #1 import scope is not silently expanded.
- [x] Decision status, evidence level, and implementation status remain separate.

## References 📚

- [`README.md`](../../README.md)
- [`ARCHITECTURE.md`](../../ARCHITECTURE.md)
- [`ROADMAP.md`](../../ROADMAP.md)
- [`docs/DECISION_PROCESS.md`](../DECISION_PROCESS.md)
- [`ADR-0005`](./0005-curiosity-core-is-optional-and-non-authoritative.md)
- [Notion Decision Ledger `D-NK-09`](https://app.notion.com/p/3a5ac84d054781cc920def45a66fe953)
