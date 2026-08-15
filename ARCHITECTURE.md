# Architecture

## 1. Purpose

Velantrim Native Kernel studies a durable semantic substrate that can survive changes in databases, indexes, model providers, runtimes, hardware, and future computational substrates.

This is an independent, personal, long-horizon research track. It is not the Crystal grant deliverable and is not constrained by a product release schedule.

The architecture is defined by contracts and invariants, not by SQLite, a graph database, a vector store, an LLM API, Python, or conventional binary hardware.

Current technologies remain useful as research instruments. They are implementation profiles, not the permanent definition of the system.

See [`docs/LONG_HORIZON_VISION.md`](./docs/LONG_HORIZON_VISION.md) for the full future-substrate vision.

### Current authority boundary

ADR-0025 initiated the Architecture Re-foundation / blueprint-first phase. The A1–A10 first drafts were subsequently completed, integrated, independently challenged, and reconciled. They are **not Final Canon**.

A1–A10 are preserved as first-draft provenance. Current provisional architecture meaning must be resolved through the accepted authority chain:

```text
ARCHITECTURE.md
→ A1–A10 first-draft provenance
→ docs/INTEGRATED_A1_A10_REVIEW.md
→ docs/reviews/IAR-1_RESULT.md
→ docs/reviews/IAR-1_RECONCILIATION.md
→ later accepted ADR / operator decisions for their explicit scope
```

`IAR-1-R1 reconciliation is the current provisional interpretation where it conflicts with first-draft wording`. A later accepted architecture decision may supersede only the scope it explicitly owns. Final Canon remains `DEFERRED / NOT AUTHORIZED`.

In particular, Event sourcing, append-only history, deterministic reduction, Claim serialization, and rebuildable projections remain binding for the existing P1–C5 reference laboratory and its versioned contracts. The reconciliation explicitly prevents those mechanisms from becoming universal substrate-neutral obligations merely because the laboratory depends on them.

```text
accepted laboratory contract
≠ current provisional architecture minimum
≠ Final Canon
```

## 2. Architecture layers

```text
Architecture authority / candidate Canon
→ Abstract Contracts
→ Replaceable Implementation Profiles
```

### Architecture authority / candidate Canon

The current provisional architecture defines semantic obligations and non-conflation rules while keeping Final Canon deferred.

The minimum problem-level obligations after IAR-1 reconciliation are:

- representation/Claim is not silently equated with represented reality or truth;
- Context, warrant/provenance and Authority assumptions remain explicit where materially relevant;
- `Unknown`, uncertainty and unsupported states remain representable without coercion to `False`;
- change, revision, supersession, retention and loss remain accountable for the declared scope;
- equivalence, capability, degradation and loss claims are made against declared or preregistered observables and failure conditions.

The earlier complete A2 ontology inventory, A3 transition catalogue, A5 identity/time inventory, A6 lifecycle positions, Receipt-shaped accountability, Event-log-shaped history and exact replay/reconstruction remain useful reference structures. They are not the universal minimum merely because they appear in first-draft architecture or the current laboratory.

### Abstract Contracts

Contracts define required behaviour without prescribing a technology. Depending on the declared scenario and capability class, they may cover:

- storage and retention;
- projection, reconstruction or another accountable state/change model;
- retrieval/context selection;
- compute/reduction or an accepted functional equivalent;
- admission and policy;
- audit/accountability;
- migration, equivalence, replay or an accepted functional equivalent.

A contract must not silently turn one current profile mechanism into universal architecture authority.

### Implementation Profiles

Implementation profiles bind contracts to technologies available at a particular time.

The current laboratory profile may use Python, PostgreSQL, SQLite, SQL, JSON, ZIP, SHA-256, Event envelopes, reducers, Receipts, FTS, graph adapters, vector or hybrid retrieval, LLM adapters, and conventional CPU/GPU execution.

A future profile may use a different storage medium, execution model, representation, or hardware substrate without redefining the architecture, provided it satisfies the declared scoped obligations or explicitly reports degradation/non-equivalence.

## 3. Current reference-laboratory shape

The following shape describes the existing P1–C5 event-sourced laboratory. It is preserved for reproducibility and remains authoritative for that versioned implementation lineage. The reconciled architecture leaves append-only history and deterministic reduction as profile mechanisms unless a future governed scenario specifically requires their capabilities.

```text
Claim
→ Event
→ deterministic reduction
→ Epistemic State
→ replaceable projections
→ task-specific context selection
→ Receipt
```

No document or implementation may cite this diagram alone as proof that all future Native Kernel profiles must use the same Event envelope, persistence pattern, reducer, Receipt, or serialized representation.

### Claim

Within the current laboratory, a Claim is the semantic identity of a statement or memory unit. It includes stable identity, content hash, lineage, version/write order, memory type, knowledge type, provenance, and temporal validity.

A Claim is not automatically true because it exists. The full current Claim record is a profile representation; future scoped conformance may preserve the required meanings through another representation.

### Event

Within the current laboratory, an Event records an append-only mutation or relationship involving a Claim. The implemented verb set includes:

- `ADMIT`
- `LINK`
- `UTILIZED`
- `SUPERSEDED`
- `ERASED`

Current laboratory state is derived from Events rather than maintained as an opaque mutable row. This is an accepted implementation contract for P1–C5, not a universal requirement that every substrate-neutral realization use append-only Events.

### Projection

Within the current laboratory, a projection is rebuildable state derived from its authoritative recorded Event history. Candidate projections include:

- SQLite read tables;
- graph adjacency;
- FTS indexes;
- vector indexes;
- temporal views;
- conflict views.

A projection does not self-canonize and must be reproducible from the history declared authoritative by its profile. The reconciled provisional architecture permits another state/change model when the declared scoped obligations, loss boundaries and conformance predicates remain explicit.

### Epistemic State

Epistemic state is computed from provenance, evidence hygiene, outcomes, validity, and policy. It is not an intrinsic permanent label detached from history.

### Charge

Charge is a relevance or priority signal used during selection. It must remain distinct from truth status. Utility, recency, or repeated use cannot independently prove a claim.

### Typed Links

Links encode explicit semantics such as derivation, requirement, contradiction, or support. Link direction and interpretation must be specified; a label alone is insufficient.

The exact referential semantics of reducer v1 remain a separate operator-controlled issue under Issue #74 / ADR-0024. This document does not reinterpret historical reducer-v1 evidence.

### Context selection

The research prototype performs deterministic lexical activation, typed propagation, eligibility filtering, conflict exposure, and greedy ablation. It is a proxy for task-specific evidence selection, not proof of sufficient context.

### Receipt

A Receipt records what the current laboratory selected and how it processed a request. A Receipt may support replay and auditability. It does not prove task sufficiency, and Receipt-shaped accountability is not a universal architecture requirement after IAR-1 reconciliation.

## 4. Laboratory invariants and cross-cutting boundaries

The following list contains two categories:

```text
items 1–4
= current event-sourced reference-laboratory invariants
= binding for existing P1–C5 contracts and evidence
≠ automatically permanent architecture authority

items 5–30
= cross-cutting semantic, epistemic, governance, and proof boundaries
= interpreted through the integrated review and IAR-1 reconciliation
```

ADR-0025 does not silently repeal accepted laboratory contracts. IAR-1 reconciliation prevents their mechanisms from becoming universal requirements through inertia.

1. Within the current reference laboratory, append-only Event history is authoritative for **recorded laboratory history**, not objective truth or every future profile.
2. Within the current reference laboratory, Claims are immutable semantic records.
3. Within the current reference laboratory, current state is derived rather than silently overwritten.
4. Within the current reference laboratory, projections are disposable and rebuildable.
5. Event history is not equivalent to admitted truth.
6. Selection relevance is not epistemic validity.
7. Utility outcomes are not truth evidence by default.
8. Knowledge type controls policy such as decay; it does not prove correctness.
9. Candidate contradiction is not established contradiction.
10. Conflict detection is not conflict resolution.
11. Receipt replayability does not imply task sufficiency.
12. SQLite, graph, FTS, and vectors are adapters, not the architecture.
13. LLMs may propose or interpret; they do not become the source of truth.
14. Legal deletion and restriction requirements cannot be nullified by an append-only implementation choice.
15. Production promotion requires independent evidence and rollback behaviour.
16. Only the operator or maintainer may approve a research proposal as an accepted implementation decision.
17. Current processor and hardware assumptions belong to an implementation profile, not the architecture minimum.
18. Backend-generated identifiers must not become the only semantic identity of a Claim when the declared scope requires continuity across replacement.
19. Replacing storage, retrieval, models, or hardware must not silently change epistemic meaning.
20. Technology independence is a research hypothesis until demonstrated across multiple implementation profiles/substrates for declared scopes.
21. Speculative future substrates are research possibilities, not implementation evidence.
22. Modern technologies may be used fully as a laboratory without becoming permanent architectural dependencies.
23. A representation is not the represented reality.
24. Observation is not automatically explanation.
25. Transformation or assembly is not proof of origin.
26. Unknown is not equivalent to false.
27. Missing provenance remains explicit as a provenance gap when provenance is material to the declared scope.
28. Current inability is not universal impossibility without declared grounds and scope.
29. Worldview claims must retain explicit domain and scope when that distinction affects interpretation or admission.
30. No observation, model, hypothesis, retrieval result, useful outcome, or proposal may be silently promoted into admitted knowledge.

See [`docs/WORLD_AND_EPISTEMIC_BOUNDARIES.md`](./docs/WORLD_AND_EPISTEMIC_BOUNDARIES.md), [`ADR-0008`](./docs/adr/0008-epistemic-boundaries-are-representation-disciplines.md), [`ADR-0025`](./docs/adr/0025-blueprint-before-runtime-expansion.md), the [`Integrated A1–A10 Review`](./docs/INTEGRATED_A1_A10_REVIEW.md), and [`IAR-1-R1 reconciliation`](./docs/reviews/IAR-1_RECONCILIATION.md).

## 5. World and epistemic boundary

Native Kernel defines an epistemic discipline rather than a fixed worldview.

```text
representation   ≠ represented reality
observation      ≠ explanation
transformation   ≠ origin
unknown          ≠ false
current limit    ≠ universal impossibility
worldview claim  ≠ unmarked empirical fact
```

The abstract architectural boundary is **Admission Policy**. Labels such as `GATE`, `TruthGate`, `Guardian`, `L3`, LLM filters, human boards, or future mechanisms belong to implementation profiles unless separately accepted as abstract contracts.

A missing provenance segment must remain explicit when provenance is material to the declared scope. It must not be silently converted into creation from nothing, originlessness, a preferred worldview explanation, generated continuity, or proof of impossibility.

The following documentation-level conformance IDs are reserved:

- `NK-EPI-001` — representation is not represented reality;
- `NK-EPI-002` — observation is not automatically explanation;
- `NK-EPI-003` — transformation is not origin;
- `NK-EPI-004` — unknown is not false;
- `NK-EPI-005` — provenance gaps remain explicit;
- `NK-EPI-006` — current inability is not universal impossibility;
- `NK-EPI-007` — worldview domain and scope remain explicit;
- `NK-EPI-008` — semantic layers are not silently promoted.

These IDs do not imply executable fixtures, runtime support, or a conformance level.

## 6. Identity, time and order

The first-draft A5 inventory distinguishes multiple identity and temporal/order dimensions. IAR-1 reconciliation keeps that inventory as analytical vocabulary rather than a mandatory universal latent schema.

For a declared scenario, materially required distinctions may include:

- valid time;
- knowledge or record time;
- local write/order relations;
- predecessor/successor or causal relations;
- identity continuity across representation/profile replacement.

Required dimensions must not be silently collapsed when that would change the declared meaning. No global total order is introduced by the architecture merely because the current laboratory uses integer sequence/order mechanisms.

## 7. Event Integrity profile target

The current Event-based laboratory family uses stronger Event-integrity machinery and may bind fields such as:

```text
event_id
global_seq
timestamp
schema_version
actor
command_id / idempotency_key
claim_id
verb
payload_hash
previous_hash
```

That profile requires a threat model, crash-consistency rules, replay rules, and multi-writer ordering. A simple hash chain alone is not sufficient.

IAR-1 reconciliation does **not** make this Event envelope, append-only history, exact replay, or one ordering mechanism a universal Kernel requirement. Another realization may use snapshots, witnesses, bounded summaries, procedural accounts, or another accountable state/change model if it preserves the preregistered obligations for its declared scope.

## 8. Read model separation

Two concepts remain distinct in the current laboratory:

- **ReadIndex** — stable structural indexes built once per snapshot, such as claims, events, adjacency, lineage, outcomes, and charge caches;
- **PullContext** — query-, time-, and task-dependent state used for one selection request.

This separation avoids rebuilding structural information for every inner operation while preserving deterministic query-specific behaviour. It is a laboratory design property, not a universal architecture requirement.

## 9. Complexity boundary

The desired laboratory snapshot build cost is approximately `O(E + L + C)` for events, links, and claims. The complete selection pipeline is not yet guaranteed linear because greedy ablation may approach `O(K²)` in the number of activated candidates.

Performance statements must distinguish:

- selective queries;
- broad queries;
- snapshot construction;
- activation;
- conflict analysis;
- ablation.

These performance properties belong to the current laboratory and are not substrate-neutral semantic requirements.

## 10. Portability and scoped conformance

A new implementation profile is acceptable for a declared scope only if it can preserve the required semantic obligations or explicitly report degradation, loss, unsupported capability or indeterminacy under the governing conformance scenario.

The current provisional minimum emphasizes:

- representation/truth non-conflation;
- explicit Context, warrant/provenance and Authority assumptions where materially relevant;
- representable Unknown/uncertainty/unsupported states;
- accountable change, revision, retention and loss for the declared scope;
- preregistered observables, equivalence predicates, allowed losses and failure conditions for conformance/falsification claims.

A scenario may additionally require exact reconstruction, replay, particular identity/time distinctions, conflict semantics, physical/cryptographic erasure evidence, or other capabilities. Those requirements must be declared for that scope rather than silently inferred from the current profile.

Candidate portability evidence therefore has the form:

```text
same declared semantic scenario/input
→ implementation profile A
→ scoped observations A

same declared semantic scenario/input
→ implementation profile B
→ scoped observations B

required result:
preregistered/declared equivalence predicates
+ disclosed degradation/non-equivalence/loss
+ explicit authority and uncertainty boundaries
```

The current PostgreSQL/SQLite comparison is bounded evidence for the existing Python semantic lineage. It is not proof that the listed mechanisms are Final Canon, that the profiles are independent computation models, or that arbitrary future substrates are supported.
