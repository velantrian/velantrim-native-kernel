# 🧬 Переоснование архитектуры — Blueprint before Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **State:** `ACTIVE / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`  
> **Decision:** [`ADR-0025`](./adr/0025-blueprint-before-runtime-expansion.md)  
> **Issue:** [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Граница evidence:** только architecture research и governance; без runtime или maturity promotion

## 1. Зачем нужна эта фаза

Native Kernel задуман как technology-neutral архитектура для memory, knowledge, meaning, provenance, uncertainty, conflict, revision и explanation.

Существующие Python, PostgreSQL, SQLite, CI и evidence сохраняются как bounded laboratory. Они не должны становиться определением Kernel только потому, что появились первыми.

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

## 2. Граница фазы

### Этой фазе принадлежат

- ontology;
- semantic laws;
- abstract state и transition models;
- boundaries identity, time, provenance, uncertainty и conflict;
- substrate-independent obligations;
- mapping rules между Canon и implementation profiles;
- explicit unknowns и falsification criteria.

### Этой фазе не принадлежат

- новая reducer implementation;
- новый database или programming-language profile;
- product integration;
- performance tuning;
- production deployment;
- proof того, что arbitrary future substrates уже conform.

## 3. Обязательные deliverables

### A1 — Purpose и Non-goals Kernel

**Status:** `DRAFTED / PROVISIONAL` — см. [`A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) / [`A1_KERNEL_PURPOSE_AND_NON_GOALS.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md). Ожидает independent review и integrated blueprint review вместе с `A2`–`A10`.

A1 определяет проблему Native Kernel, durable qualities, значение `Kernel`, внешние границы и отношения с Titan, Crystal, Mentaury, operating systems, databases и model runtimes.

**Completion test:** выполнен для first-draft scope: читатель отличает architecture от product, database, framework, cognitive system и storage engine без обращения к текущему source code. Final acceptance всё ещё требует independent и integrated review.

### A2 — Knowledge and Memory Ontology

**Status:** `DRAFTED / PROVISIONAL` — см. [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md) / [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md). Ожидает independent review и integrated blueprint review вместе с A1 и A3–A10.

Drafted inventory различает:

```text
Signal · Observation · Record · Proposition · Claim · Interpretation
Hypothesis · Belief · Knowledge · Memory · Evidence · Source · Provenance
Context · Relation · State · Change · Event · Conflict · Contradiction
Uncertainty · Revision · Supersession · Authority · Receipt
```

Для каждого concept A2 фиксирует working definition, non-definition, neighbouring distinctions, allowed relations, identity/lifecycle notes, minimum semantic obligations, unresolved questions, falsification/counterexample и provisional primitive/derived/open classification.

A2 отвергает current Python fields, SQL rows, JSON, graph nodes, embeddings, LLM operations или Event-sourced laboratory mechanics как определения этих concepts.

**Completion test:** выполнен для first-draft scope; final acceptance всё ещё требует independent и integrated review.

### A3 — Абстрактная машина Native Kernel

**Status:** `DRAFTED / PROVISIONAL` — см. [`A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md`](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md) / [`A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md`](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md). Ожидает independent review и integrated blueprint review вместе с A1–A2 и A4–A10.

A3 определяет provisional scoped obligation-and-transition machine, а не переносит current Event/reducer laboratory в Canon. Она фиксирует 13 logical configuration facets и 13 transition families, explicit preconditions/postconditions, failure/indeterminacy outcomes, Authority boundaries, order/concurrency requirements, determinism/reproducibility limits, bounded accountability и contrasting substrate mappings.

Она сохраняет как минимум:

```text
abstract machine ≠ runtime implementation
transition ≠ Event envelope
transition relation ≠ reducer
history visibility ≠ mandatory Event sourcing
admission ≠ truth
deterministic output ≠ true output
profile conformance ≠ production authorization
```

**Completion test:** выполнен для first-draft scope: materially different manual, adaptive/analog и conventional digital mappings выражают provisional machine без переноса SQL/Python semantics в Canon. Final acceptance всё ещё требует independent и integrated review.

### A4 — Семантические законы и инварианты

**Status:** `DRAFTED / PROVISIONAL` — см. [`A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md`](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md) / [`A4_SEMANTIC_LAWS_AND_INVARIANTS.md`](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md). Ожидает independent review и integrated blueprint review вместе с A1–A3 и A5–A10.

A4 создаёт первый GitHub-resident numbered/versioned law-set candidate:

```text
law_set: nk-semantic-laws/A4-draft-1
law_count: 28
```

28 laws — текущий deduplicated result reconciliation A1 durable qualities, A2 non-equivalences, A3 transition obligations, существующих documentation targets NK-EPI и A4 plan. Count provisional и может измениться во время review; это не число, которое требуется сохранять само по себе.

Laws организованы вокруг:

- representation и epistemic boundaries;
- Context, Provenance и Authority;
- identity, Memory, time и Change;
- Relations, Conflict и Uncertainty;
- derived views, selection и accountability;
- substrate, reproducibility и conformance.

Каждый law содержит:

- statement;
- rationale;
- counterexample/falsifier;
- failure mode;
- observable obligation;
- exception/open uncertainty.

A4 явно сохраняет, среди прочего:

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

Ранее ошибочный Notion-only identity `nk-semantic-laws/0.1-draft` не переиспользуется и никогда не был authoritative GitHub A4 law set.

**Completion test:** выполнен для first-draft scope: law set numbered, versioned, substrate-neutral и falsifiable на уровне obligations, maps back к A2/A3, содержит contrasting substrate thought experiments и оставляет detailed identity/time/lifecycle/conflict/conformance mechanisms для A5–A8. Final acceptance всё ещё требует independent и integrated review.

### A5 — Модель Identity, Time и Change

**Status:** `NEXT BOUNDED SLICE`.

Определить без привязки к physical encoding:

- semantic identity;
- Record identity;
- content identity;
- lineage identity;
- aliasing и migration;
- occurrence time;
- Observation time;
- valid time;
- Record time;
- write/causal/partial order;
- correction, Revision, Supersession, restriction, erasure и forgetting.

A5 должен refine A4, не ослабляя его молча. В частности, он должен объяснить, какие changes preserve identity, create new version, create new entity или remain undecided, и как temporal/order relations остаются named, не схлопываясь в implementation write order.

**Completion test:** model объясняет, какие changes preserve identity, create new version, create new entity или remain undecided без требования одного physical encoding.

### A6 — Lifecycle знания

Смоделировать lifecycle от raw encounter до possible use, revision, restriction и historical retention.

Lifecycle должен сохранять distinctions:

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

Ни одно lifecycle state не получает Authority только из storage, retrieval rank, repetition, model confidence или usefulness.

### A7 — Модель Conflict, Uncertainty и Revision

Определить candidate versus established Conflict, Contradiction versus scope mismatch, unresolved plurality, Uncertainty types, Evidence/Provenance gaps, resolution Authority, reversible/irreversible decisions, Belief Revision без rewriting history и возможность system оставаться undecided.

### A8 — Контракт substrate independence

Определить, что future implementation обязана preserve или explicitly translate, включая semantic identity, history/Change visibility, Provenance, temporal meaning, Uncertainty/Conflict visibility, reconstruction или accepted functional equivalent, Authority/admission boundaries, bounded explanations/Receipts, migration и loss disclosure.

Контракт должен выявить assumptions, являющиеся artifacts current Event-sourcing practice, а не permanent architecture.

### A9 — Граница Reference Laboratory

Классифицировать текущую implementation:

```text
Python + PostgreSQL + SQLite
= bounded reference laboratory
≠ final architecture
```

Для каждого major module позднее определить: valid example abstract contract, temporary experiment, implementation-specific mechanism, falsification tool, legacy evidence, которое остаётся readable, но не направляет blueprint, либо candidate на later replacement/removal.

На этой фазе ничего не удаляется и не переписывается только потому, что reclassification возможна.

### A10 — Open Questions и Falsification Criteria

Зафиксировать вопросы, на которые project пока не отвечает, например:

- является ли append-only history Canon requirement или одним implementation explicit Change;
- может ли identity существовать без stable serialized bytes;
- каков minimum reconstruction/replay на analog или neuromorphic substrates;
- какие формы Uncertainty сравнимы across profiles;
- можно ли represent forgetting без permanent retention forbidden content;
- что означает same semantic State across probabilistic systems.

Каждая major architectural hypothesis должна включать evidence, которое способно её weaken или refute.

## 4. Последовательность работы

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

Документы могут iterate, но later layers не могут молча redefine earlier ones.

## 5. Research method

Каждый deliverable должен содержать:

1. definitions;
2. explicit non-equivalences;
3. candidate formal model;
4. counterexamples;
5. failure cases;
6. unresolved questions;
7. relationship to existing contracts и runtime;
8. substrate mapping examples;
9. review status;
10. evidence boundary.

Sources, papers, existing systems и AI analyses являются inputs. Они не становятся Canon автоматически.

## 6. Policy runtime freeze

Разрешены:

- critical integrity и security fixes;
- reproducibility и provenance corrections;
- evidence preservation;
- validator и current-truth repair;
- historical recovery;
- isolated architecture experiments без runtime promotion.

Не разрешены без separate explicit operator decision:

- new semantic features;
- reducer v2;
- new Event vocabulary;
- new databases, language ports, model adapters или ecosystem integrations;
- performance optimization, меняющая semantic behaviour;
- new evidence или maturity labels как proof unfinished blueprint.

## 7. Связь с pending decisions

Issue #18 и ADR-0024 остаются pending.

```text
Architecture Re-foundation can proceed now.
License selection remains required before an open contribution/publication regime.
ADR-0024 remains required before any reducer-v2 path resumes.
```

Ни одно pending decision не блокирует blueprint research. Ни одно не решается молча этим plan или A1–A4.

## 8. Gate завершения blueprint

Фаза не завершена только потому, что существуют десять документов.

Completion требует:

- всех десяти deliverables, присутствующих и linked;
- reconciled terminology;
- contradictions, listed rather than hidden;
- labelled implementation-specific assumptions;
- explicit open questions и falsification criteria;
- documented mapping к existing accepted contracts;
- минимум двух contrasting substrate thought experiments;
- independent critical review или explicit record, что оно unavailable;
- operator review и separate decision о next phase.

## 9. Текущий прогресс

```text
Architecture Re-foundation decision: established by ADR-0025
Blueprint plan: this document
Blueprint content: A1-A4 DRAFTED / PROVISIONAL; A5-A10 NOT YET COMPLETE
Next bounded slice: A5 IDENTITY / TIME / CHANGE
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```
