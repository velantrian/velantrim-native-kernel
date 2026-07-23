# Architecture

## 1. Purpose

Velantrim Native Kernel studies a durable semantic substrate that can survive changes in databases, indexes, model providers, runtimes, hardware, and future computational substrates.

This is an independent, personal, long-horizon research track. It is not the Crystal grant deliverable and is not constrained by a product release schedule.

The architecture is defined by contracts and invariants, not by SQLite, a graph database, a vector store, an LLM API, Python, or conventional binary hardware.

Current technologies remain useful as research instruments. They are implementation profiles, not the permanent definition of the system.

See [`docs/LONG_HORIZON_VISION.md`](./docs/LONG_HORIZON_VISION.md) for the full future-substrate vision.

## 2. Architecture layers

```text
Architecture Canon
→ Abstract Contracts
→ Replaceable Implementation Profiles
```

### Architecture Canon

The Canon defines stable semantic meaning:

- identity and lineage;
- explicit change history;
- state reconstruction;
- provenance and evidence boundaries;
- temporal semantics;
- conflict visibility;
- context accountability;
- auditable Receipts.

### Abstract Contracts

Contracts define required behaviour without prescribing a technology:

- storage;
- projection;
- retrieval;
- compute and reduction;
- admission and policy;
- audit and Receipt;
- migration and replay.

### Implementation Profiles

Implementation profiles bind those contracts to technologies available at a particular time.

The current laboratory profile may use Python, SQLite, FTS, graph adapters, vector or hybrid retrieval, LLM adapters, and conventional CPU/GPU execution.

A future profile may use a different storage medium, execution model, representation, or hardware substrate without redefining the Canon.

## 3. Canon Shape

```text
Claim
→ Event
→ deterministic reduction
→ Epistemic State
→ replaceable projections
→ task-specific context selection
→ Receipt
```

### Claim

A Claim is the semantic identity of a statement or memory unit. It includes stable identity, content hash, lineage, version/write order, memory type, knowledge type, provenance, and temporal validity.

A Claim is not automatically true because it exists.

### Event

An Event records an append-only mutation or relationship involving a Claim. The current research model uses a small explicit verb set such as:

- `ADMIT`
- `LINK`
- `UTILIZED`
- `SUPERSEDED`
- `ERASED`

Current state is derived from events rather than maintained as an opaque mutable row.

### Projection

A projection is rebuildable state derived from authoritative history. Candidate projections include:

- SQLite read tables;
- graph adjacency;
- FTS indexes;
- vector indexes;
- temporal views;
- conflict views.

A projection does not self-canonize and must be reproducible from authoritative history.

### Epistemic State

Epistemic state is computed from provenance, evidence hygiene, outcomes, validity, and policy. It is not an intrinsic permanent label detached from history.

### Charge

Charge is a relevance or priority signal used during selection. It must remain distinct from truth status. Utility, recency, or repeated use cannot independently prove a claim.

### Typed Links

Links encode explicit semantics such as derivation, requirement, contradiction, or support. Link direction and interpretation must be specified; a label alone is insufficient.

### Context selection

The research prototype performs deterministic lexical activation, typed propagation, eligibility filtering, conflict exposure, and greedy ablation. It is a proxy for task-specific evidence selection, not proof of sufficient context.

### Receipt

A Receipt records what the engine selected and how it processed a request. A receipt may support replay and auditability. It does not prove that the selected set was sufficient for the user's real task.

## 4. Core invariants

1. The append-only event history is authoritative.
2. Claims are immutable semantic records.
3. Current state is derived, not silently overwritten.
4. Projections are disposable and rebuildable.
5. Event history is not equivalent to admitted truth.
6. Selection relevance is not epistemic validity.
7. Utility outcomes are not truth evidence by default.
8. Knowledge type controls policy such as decay; it does not prove correctness.
9. Candidate contradiction is not established contradiction.
10. Conflict detection is not conflict resolution.
11. Receipt replayability does not imply task sufficiency.
12. SQLite, graph, FTS, and vectors are adapters, not the architecture.
13. LLMs may propose or interpret; they do not become the source of truth.
14. Legal deletion and restriction requirements cannot be nullified by append-only design.
15. Production promotion requires independent evidence and rollback behaviour.
16. Only the operator or maintainer may approve a research proposal as an accepted implementation decision.
17. Current processor and hardware assumptions belong to an implementation profile, not the Canon.
18. Backend-generated identifiers must not become the only semantic identity of a Claim.
19. Replacing storage, retrieval, models, or hardware must not silently change epistemic meaning.
20. Technology independence is a research hypothesis until demonstrated across multiple implementation profiles.
21. Speculative future substrates are research possibilities, not implementation evidence.
22. Modern technologies may be used fully as a laboratory without becoming permanent architectural dependencies.

## 5. Temporal model

The architecture distinguishes at least:

- **valid time** — when a claim is asserted to hold in the represented world;
- **knowledge or record time** — when the system learned or recorded it;
- **write order** — deterministic ordering used for concurrency or version checks.

These dimensions must not be collapsed into one overloaded version field.

The current prototype has partial temporal support. Full bi-temporal query semantics remain future work.

## 6. Event Integrity target

A future complete event envelope should bind fields such as:

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

The envelope requires a threat model, crash-consistency rules, replay rules, and multi-writer ordering. A simple hash chain alone is not sufficient.

## 7. Read model separation

Two concepts must remain distinct:

- **ReadIndex** — stable structural indexes built once per snapshot, such as claims, events, adjacency, lineage, outcomes, and charge caches;
- **PullContext** — query-, time-, and task-dependent state used for one selection request.

This separation avoids rebuilding structural information for every inner operation while preserving deterministic query-specific behaviour.

## 8. Complexity boundary

The desired snapshot build cost is approximately `O(E + L + C)` for events, links, and claims. The complete selection pipeline is not yet guaranteed linear because greedy ablation may approach `O(K²)` in the number of activated candidates.

Performance statements must distinguish:

- selective queries;
- broad queries;
- snapshot construction;
- activation;
- conflict analysis;
- ablation.

## 9. Portability contract

A new implementation profile is acceptable only if it can preserve or explicitly translate:

- Claim identity and lineage;
- Event ordering and replay semantics;
- provenance and temporal meaning;
- conflict visibility;
- epistemic-state boundaries;
- Receipt semantics.

Candidate portability evidence includes:

```text
same authoritative history
→ implementation profile A
→ semantic state A

same authoritative history
→ implementation profile B
→ semantic state B

required result:
explicitly defined semantic equivalence
```

Bit-for-bit equality is not assumed across all future substrates. The required equivalence level must be documented and tested.

## 10. Canon, Experimental, Anti-Canon

### Canon Shape

- Claim as semantic identity;
- append-only event authority;
- deterministic reduction;
- replaceable projections;
- explicit epistemic boundaries;
- auditable receipts;
- storage, model, runtime, and hardware independence at the contract level.

### Experimental

- current charge formula;
- lexical activation;
- propagation weights;
- greedy ablation;
- candidate-conflict heuristics;
- validation thresholds;
- current SQLite schema;
- current Python runtime;
- current retrieval and model adapters;
- future-substrate portability experiments.

### Anti-Canon

The project rejects:

- treating embeddings or graph edges as truth;
- claiming consciousness or personhood;
- equating repeated use with correctness;
- hiding unresolved conflicts;
- calling lexical context selection genuine sufficient evidence grip;
- binding the architecture permanently to one database, language, model provider, processor, or hardware platform;
- treating current binary execution as the ontology of memory;
- treating speculative future hardware as proof that the architecture works;
- direct research-runtime writes into Crystal Canon;
- promoting proposals based solely on multi-model consensus.
