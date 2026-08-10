# 🧬 Architecture Re-foundation — Blueprint before Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **State:** `ACTIVE / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`  
> **Decision:** [`ADR-0025`](./adr/0025-blueprint-before-runtime-expansion.md)  
> **Issue:** [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Evidence boundary:** architecture research and governance only; no runtime or maturity promotion

## 1. Why this phase exists

Native Kernel is intended to be a technology-neutral architecture for memory, knowledge, meaning, provenance, uncertainty, conflict, revision, and explanation.

The existing Python, PostgreSQL, SQLite, CI, and evidence work is retained as a bounded laboratory. It must not become the definition of the Kernel merely because it exists first.

```text
meaning and invariants
        ↓
abstract Kernel machine
        ↓
versioned contracts
        ↓
replaceable profiles
        ↓
experiments and evidence
```

## 2. Phase boundary

### This phase owns

- ontology;
- semantic laws;
- abstract state and transition models;
- identity, time, provenance, uncertainty, and conflict boundaries;
- substrate-independent obligations;
- mapping rules between Canon and implementation profiles;
- explicit unknowns and falsification criteria.

### This phase does not own

- a new reducer implementation;
- a new database or programming language profile;
- product integration;
- performance tuning;
- production deployment;
- proof that arbitrary future substrates already conform.

## 3. Required deliverables

### A1 — Kernel Purpose and Non-goals

**Status:** `DRAFTED / PROVISIONAL` — see [`A1_KERNEL_PURPOSE_AND_NON_GOALS.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) / [`A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md). Pending independent review and integrated blueprint review with `A2`–`A10`.

Define the problem Native Kernel studies, the durable qualities it seeks to preserve, what `Kernel` means here, what belongs outside it, and boundaries with Titan, Crystal, Mentaury, operating systems, databases, and model runtimes.

**Completion test:** satisfied for first-draft scope: a reader can distinguish the architecture from a product, database, framework, cognitive system, and storage engine without referring to current source code. Final acceptance still requires independent and integrated review.

### A2 — Knowledge and Memory Ontology

**Status:** `DRAFTED / PROVISIONAL` — see [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) / [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md). Pending independent review and integrated blueprint review with A1 and A3–A10.

The drafted inventory distinguishes:

```text
Signal · Observation · Record · Proposition · Claim · Interpretation
Hypothesis · Belief · Knowledge · Memory · Evidence · Source · Provenance
Context · Relation · State · Change · Event · Conflict · Contradiction
Uncertainty · Revision · Supersession · Authority · Receipt
```

For every concept A2 records a working definition, non-definition, neighbouring distinctions, allowed relations, identity/lifecycle notes, minimum semantic obligations, unresolved questions, falsification/counterexample, and provisional primitive/derived/open classification.

A2 rejects current Python fields, SQL rows, JSON, graph nodes, embeddings, LLM operations, or Event-sourced laboratory mechanics as the definition of those concepts.

**Completion test:** satisfied for first-draft scope; final acceptance still requires independent and integrated review.

### A3 — Abstract Native Kernel Machine

**Status:** `DRAFTED / PROVISIONAL` — see [`A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md`](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) / [`A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md`](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md). Pending independent review and integrated blueprint review with A1–A2 and A4–A10.

A3 defines a provisional scoped obligation-and-transition machine rather than promoting the current Event/reducer laboratory into Canon. It records thirteen logical configuration facets and thirteen transition families, explicit preconditions/postconditions, failure and indeterminacy outcomes, Authority boundaries, order/concurrency requirements, determinism/reproducibility limits, bounded accountability, and contrasting substrate mappings.

It preserves at least:

```text
abstract machine ≠ runtime implementation
transition ≠ Event envelope
transition relation ≠ reducer
history visibility ≠ mandatory Event sourcing
admission ≠ truth
deterministic output ≠ true output
profile conformance ≠ production authorization
```

**Completion test:** satisfied for first-draft scope: materially different manual, adaptive/analog, and conventional digital mappings can express the provisional machine without importing SQL/Python semantics into Canon. Final acceptance still requires independent and integrated review.

### A4 — Semantic Laws and Invariants

**Status:** `DRAFTED / PROVISIONAL` — see [`A4_SEMANTIC_LAWS_AND_INVARIANTS.md`](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md) / [`A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md`](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md). Pending independent review and integrated blueprint review with A1–A3 and A5–A10.

A4 creates the first GitHub-resident numbered/versioned law-set candidate:

```text
law_set: nk-semantic-laws/A4-draft-1
law_count: 28
```

The 28 laws are the current deduplicated result of reconciling A1 durable qualities, A2 non-equivalences, A3 transition obligations, existing NK-EPI documentation targets, and the A4 plan. The count is provisional and may change during review; it is not a target to preserve for its own sake.

The laws are organized around:

- representation and epistemic boundaries;
- Context, Provenance, and Authority;
- identity, Memory, time, and Change;
- Relations, Conflict, and Uncertainty;
- derived views, selection, and accountability;
- substrate, reproducibility, and conformance.

Every law provides:

- a statement;
- rationale;
- counterexample/falsifier;
- failure mode;
- observable obligation;
- exception/open uncertainty.

A4 explicitly preserves, among other rules:

```text
representation ≠ represented reality
Claim / admission / availability ≠ objective truth
Source or repetition ≠ Evidence by itself
Unknown / missing / unsupported / failed ≠ False
semantic identity ≠ storage identity
write order ≠ represented-world order
Revision ≠ silent overwrite
Supersession ≠ deletion or falsity
Conflict detection ≠ conflict resolution
derived view ≠ universal State
retrieval / utility / recency ≠ epistemic validity
Receipt/accountability ≠ correctness or truth
history visibility ≠ mandatory Event sourcing
determinism/reproducibility ≠ truth or physical identity
profile conformance ≠ production authorization
```

The previously erroneous Notion-only identity `nk-semantic-laws/0.1-draft` is not reused and never represented an authoritative GitHub A4 law set.

**Completion test:** satisfied for first-draft scope: the law set is numbered, versioned, substrate-neutral, falsifiable at the obligation level, maps back to A2/A3, includes contrasting substrate thought experiments, and leaves detailed identity/time/lifecycle/conflict/conformance mechanisms to A5–A8. Final acceptance still requires independent and integrated review.

### A5 — Identity, Time, and Change Model

**Status:** `NEXT BOUNDED SLICE`.

Define without committing to a physical encoding:

- semantic identity;
- Record identity;
- content identity;
- lineage identity;
- aliasing and migration;
- occurrence time;
- Observation time;
- valid time;
- Record time;
- write/causal/partial order;
- correction, Revision, Supersession, restriction, erasure, and forgetting.

A5 must refine A4 without silently weakening it. In particular, it must explain which changes preserve identity, create a new version, create a new entity, or remain undecided, and how temporal/order relations remain named instead of collapsing into implementation write order.

**Completion test:** the model explains which changes preserve identity, create a new version, create a new entity, or remain undecided without requiring one physical encoding.

### A6 — Knowledge Lifecycle

Model the lifecycle from raw encounter to possible use, revision, restriction, and historical retention.

The lifecycle must preserve distinctions among:

```text
captured
observed
interpreted
hypothesized
supported
contested
admitted
rejected
unknown
superseded
restricted
erased/forgotten
```

No lifecycle state may obtain authority solely from storage, retrieval rank, repetition, model confidence, or usefulness.

### A7 — Conflict, Uncertainty, and Revision Model

Define candidate versus established Conflict, Contradiction versus scope mismatch, unresolved plurality, Uncertainty types, Evidence/Provenance gaps, resolution Authority, reversible/irreversible decisions, Belief Revision without rewriting history, and how the system may remain undecided.

### A8 — Substrate-independence Contract

Define what a future implementation must preserve or explicitly translate, including semantic identity, history/Change visibility, Provenance, temporal meaning, Uncertainty/Conflict visibility, reconstruction or accepted functional equivalent, Authority/admission boundaries, bounded explanations/Receipts, migration, and loss disclosure.

It must identify assumptions that are artifacts of present Event-sourcing practice rather than permanent architecture.

### A9 — Reference Laboratory Boundary

Classify the current implementation:

```text
Python + PostgreSQL + SQLite
= bounded reference laboratory
≠ final architecture
```

For every major module determine later whether it is a valid example of an abstract contract, temporary experiment, implementation-specific mechanism, falsification tool, legacy evidence that remains readable but does not guide the blueprint, or candidate for later replacement/removal.

No deletion or rewrite occurs in this phase merely because reclassification is possible.

### A10 — Open Questions and Falsification Criteria

Record questions the project does not yet answer, such as:

- Is append-only history a Canon requirement or one implementation of explicit Change?
- Can identity exist without stable serialized bytes?
- What is the minimum notion of reconstruction/replay on analog or neuromorphic substrates?
- Which forms of Uncertainty can be compared across profiles?
- Can forgetting be represented without permanent retention of forbidden content?
- What constitutes the same semantic State across probabilistic systems?

Each major architectural hypothesis must include evidence that would weaken or refute it.

## 4. Work sequence

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Ontology                                   DRAFTED / PROVISIONAL
→ A3 Abstract Machine                           DRAFTED / PROVISIONAL
→ A4 Semantic Laws                              DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   NEXT BOUNDED SLICE
→ A6 Knowledge Lifecycle
→ A7 Conflict / Uncertainty / Revision
→ A8 Substrate Independence
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ operator decision on reopening runtime work
```

Documents may iterate, but later layers cannot silently redefine earlier ones.

## 5. Research method

Each deliverable should contain:

1. definitions;
2. explicit non-equivalences;
3. candidate formal model;
4. counterexamples;
5. failure cases;
6. unresolved questions;
7. relationship to existing contracts and runtime;
8. substrate mapping examples;
9. review status;
10. evidence boundary.

Sources, papers, existing systems, and AI analyses are inputs. They do not become Canon automatically.

## 6. Runtime freeze policy

Allowed:

- critical integrity and security fixes;
- reproducibility and provenance corrections;
- evidence preservation;
- validator and current-truth repair;
- historical recovery;
- isolated architecture experiments with no runtime promotion.

Not allowed without a separate explicit operator decision:

- new semantic features;
- reducer v2;
- new Event vocabulary;
- new databases, language ports, model adapters, or ecosystem integrations;
- performance optimization that changes semantic behaviour;
- new evidence or maturity labels presented as proof of the unfinished blueprint.

## 7. Relationship to pending decisions

Issue #18 and ADR-0024 remain pending.

```text
Architecture Re-foundation can proceed now.
License selection remains required before an open contribution/publication regime.
ADR-0024 remains required before any reducer-v2 path resumes.
```

Neither pending decision blocks blueprint research. Neither is silently decided by this plan or A1–A4.

## 8. Blueprint completion gate

The phase is not complete merely because ten documents exist.

Completion requires:

- all ten deliverables present and linked;
- terminology reconciled across them;
- contradictions listed rather than hidden;
- implementation-specific assumptions labelled;
- open questions and falsification criteria explicit;
- mapping to existing accepted contracts documented;
- at least two contrasting substrate thought experiments;
- independent critical review or an explicit record that it is unavailable;
- operator review and a separate decision on the next phase.

## 9. Current progress

```text
Architecture Re-foundation decision: established by ADR-0025
Blueprint plan: this document
Blueprint content: A1-A4 DRAFTED / PROVISIONAL; A5-A10 NOT YET COMPLETE
Next bounded slice: A5 IDENTITY / TIME / CHANGE
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```
