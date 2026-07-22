# Architecture

## 1. Purpose

Velantrim Native Kernel studies a durable semantic substrate that can survive changes in databases, indexes, model providers, and hardware. The architecture is defined by contracts and invariants, not by SQLite, a graph database, a vector store, or an LLM API.

## 2. Canon Shape

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

## 3. Core invariants

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

## 4. Temporal model

The architecture distinguishes at least:

- **valid time** — when a claim is asserted to hold in the represented world;
- **knowledge or record time** — when the system learned or recorded it;
- **write order** — deterministic ordering used for concurrency or version checks.

These dimensions must not be collapsed into one overloaded version field.

The current prototype has partial temporal support. Full bi-temporal query semantics remain future work.

## 5. Event Integrity target

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

## 6. Read model separation

Two concepts must remain distinct:

- **ReadIndex** — stable structural indexes built once per snapshot, such as claims, events, adjacency, lineage, outcomes, and charge caches;
- **PullContext** — query-, time-, and task-dependent state used for one selection request.

This separation avoids rebuilding structural information for every inner operation while preserving deterministic query-specific behaviour.

## 7. Complexity boundary

The desired snapshot build cost is approximately `O(E + L + C)` for events, links, and claims. The complete selection pipeline is not yet guaranteed linear because greedy ablation may approach `O(K²)` in the number of activated candidates.

Performance statements must distinguish:

- selective queries;
- broad queries;
- snapshot construction;
- activation;
- conflict analysis;
- ablation.

## 8. Canon, Experimental, Anti-Canon

### Canon Shape

- Claim as semantic identity;
- append-only event authority;
- deterministic reduction;
- replaceable projections;
- explicit epistemic boundaries;
- auditable receipts;
- storage and model independence.

### Experimental

- current charge formula;
- lexical activation;
- propagation weights;
- greedy ablation;
- candidate-conflict heuristics;
- validation thresholds;
- current SQLite schema.

### Anti-Canon

The project rejects:

- treating embeddings or graph edges as truth;
- claiming consciousness or personhood;
- equating repeated use with correctness;
- hiding unresolved conflicts;
- calling lexical context selection genuine sufficient Grip;
- binding the architecture permanently to one database;
- direct research-runtime writes into Crystal Canon;
- promoting proposals based solely on multi-model consensus.