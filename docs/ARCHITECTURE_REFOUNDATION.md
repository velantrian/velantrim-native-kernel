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

Define:

- the problem Native Kernel exists to study;
- the durable qualities it seeks to preserve;
- what the word `Kernel` means here;
- what belongs outside the Kernel;
- boundaries with Titan, Crystal, Mentaury, operating systems, databases, and model runtimes.

**Completion test:** a reader can distinguish the architecture from a product, database, framework, cognitive system, and storage engine without referring to current source code.

### A2 — Knowledge and Memory Ontology

**Status:** `DRAFTED / PROVISIONAL` — see [`A2_KERNEL_PURPOSE_AND_NON_GOALS.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) / [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md). Pending independent review and integrated blueprint review with A1 and A3–A10.

The drafted inventory distinguishes:

```text
Signal
Observation
Record
Proposition
Claim
Interpretation
Hypothesis
Belief
Knowledge
Memory
Evidence
Source
Provenance
Context
Relation
State
Change
Event
Conflict
Contradiction
Uncertainty
Revision
Supersession
Authority
Receipt
```

For every concept A2 records:

- a working architectural definition;
- what it is not;
- neighbouring distinctions;
- allowed relations;
- identity and lifecycle notes;
- minimum semantic obligations;
- unresolved questions;
- falsification or counterexample;
- provisional classification as `CANDIDATE_PRIMITIVE`, `DERIVED_CONCEPT`, or `OPEN_QUESTION`.

A2 compares a linear pipeline, Event-centred ontology, relation-first model, and stratified role ontology. It uses the stratified organization only as a drafting aid, not Canon. Event and State remain open primitive questions; Knowledge and Memory do not require an LLM, embeddings, SQL, JSON, digital bytes, or a specific processor.

**Completion test:** satisfied for first-draft scope: no core term is defined only through Python fields, SQL rows, JSON, graph nodes, embeddings, an LLM operation, or current Event-sourced laboratory mechanics. Final acceptance still requires independent and integrated review.

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

**Completion test:** satisfied for first-draft scope: materially different manual, analog/neuromorphic, and digital mappings can express the provisional machine without importing SQL/Python semantics into Canon. Final acceptance still requires independent and integrated review.

### A4 — Semantic Laws and Invariants

**Status:** `NEXT BOUNDED SLICE`.

Create a numbered, versioned law set.

Candidate laws include:

- representation is not represented reality;
- a Record is not the occurrence it describes;
- Observation is not Claim;
- Claim is not Truth;
- Evidence is not Source;
- repetition is not Evidence;
- Belief is not Knowledge;
- Memory is not merely a stored Record;
- retrieval relevance is not epistemic validity;
- Conflict is not necessarily Contradiction;
- unknown is not false;
- Event use in P1–C5 does not make Event a universal primitive;
- State is not necessarily reducer output;
- storage presence is not admission;
- admission is not objective truth;
- recency is not correctness;
- utility is not epistemic validity;
- conflict detection is not conflict resolution;
- derived state cannot silently rewrite history;
- optimization cannot silently change meaning;
- implementation equivalence must be named rather than assumed.

For every law provide:

- rationale;
- counterexample;
- failure mode;
- observable obligation;
- known exceptions or open uncertainty.

### A5 — Identity, Time, and Change Model

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
- write/causal order;
- correction, Revision, Supersession, restriction, erasure, and forgetting.

**Completion test:** the model explains which changes preserve identity, create a new version, create a new entity, or remain undecided.

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

Define:

- candidate versus established Conflict;
- Contradiction versus scope mismatch;
- unresolved plurality;
- Uncertainty types;
- missing Evidence and Provenance gaps;
- resolution Authority;
- reversible versus irreversible decisions;
- Belief Revision without rewriting history;
- how the system may remain undecided.

### A8 — Substrate-independence Contract

Define what a future implementation must preserve or explicitly translate.

The contract must classify obligations such as:

- semantic identity;
- history and Change visibility;
- Provenance;
- temporal meaning;
- Uncertainty and Conflict visibility;
- replay/reconstruction or an accepted functional equivalent;
- Authority and admission boundaries;
- bounded explanations/Receipts;
- migration and loss disclosure.

It must also identify architecture assumptions that may be artifacts of present Event-sourcing practice.

### A9 — Reference Laboratory Boundary

Classify the current implementation:

```text
Python + PostgreSQL + SQLite
= bounded reference laboratory
≠ final architecture
```

For every major module determine later whether it is:

- a valid example of an abstract contract;
- a temporary experiment;
- an implementation-specific mechanism;
- a falsification tool;
- legacy evidence that should remain readable but not guide the blueprint;
- a candidate for removal or replacement after blueprint review.

No deletion or rewrite occurs in this phase merely because reclassification is possible.

### A10 — Open Questions and Falsification Criteria

Record questions that the project does not yet answer.

Examples:

- Is append-only history a Canon requirement or one implementation of explicit Change?
- Can identity exist without stable serialized bytes?
- What is the minimum notion of replay on analog or neuromorphic substrates?
- Which forms of Uncertainty can be compared across profiles?
- Can forgetting be represented without permanent retention of forbidden content?
- What constitutes the same semantic State across probabilistic systems?

Each major architectural hypothesis must include evidence that would weaken or refute it.

## 4. Work sequence

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Ontology                                   DRAFTED / PROVISIONAL
→ A3 Abstract Machine                           DRAFTED / PROVISIONAL
→ A4 Semantic Laws                              NEXT BOUNDED SLICE
→ A5 Identity / Time / Change
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

Neither pending decision blocks ontology and blueprint research. Neither is silently decided by this plan or A1–A3.

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
Blueprint content: A1-A3 DRAFTED / PROVISIONAL; A4-A10 NOT YET COMPLETE
Next bounded slice: A4 SEMANTIC LAWS AND INVARIANTS
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```