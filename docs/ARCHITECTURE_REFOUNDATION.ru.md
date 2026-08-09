# 🧬 Переоснование архитектуры — чертёж до Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **Состояние:** `ACTIVE / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`  
> **Решение:** [`ADR-0025`](./adr/0025-blueprint-before-runtime-expansion.md)  
> **Issue:** [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Граница evidence:** только архитектурное исследование и governance; без повышения runtime или maturity

## 1. Зачем нужна эта фаза

Native Kernel задуман как технологически нейтральная архитектура памяти, знания, смысла, provenance, неопределённости, конфликта, пересмотра и объяснения.

Существующие Python, PostgreSQL, SQLite, CI и evidence сохраняются как ограниченная лаборатория. Они не должны становиться определением Kernel только потому, что были реализованы первыми.

```text
смысл и инварианты
        ↓
абстрактная машина Kernel
        ↓
версионированные контракты
        ↓
заменяемые profiles
        ↓
эксперименты и evidence
```

## 2. Граница фазы

### Эта фаза определяет

- ontology;
- semantic laws;
- abstract state и transition models;
- границы identity, time, Provenance, Uncertainty и Conflict;
- substrate-independent obligations;
- mapping rules между Canon и implementation profiles;
- explicit unknowns и falsification criteria.

### Эта фаза не определяет

- новый reducer implementation;
- новый database или programming-language profile;
- product integration;
- performance tuning;
- production deployment;
- proof, что arbitrary future substrates уже conform.

## 3. Обязательные результаты

### A1 — Purpose и Non-goals Kernel

**Статус:** `DRAFTED / PROVISIONAL` — см. [`A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) / [`A1_KERNEL_PURPOSE_AND_NON_GOALS.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md). Ожидает independent review и integrated blueprint review вместе с `A2`–`A10`.

Определить:

- какую проблему изучает Native Kernel;
- какие долговечные свойства он должен сохранять;
- что означает слово `Kernel` в этом проекте;
- что находится вне Kernel;
- границы с Titan, Crystal, Mentaury, operating systems, databases и model runtimes.

**Критерий завершения:** читатель отличает architecture от product, database, framework, cognitive system и storage engine без обращения к current source code.

### A2 — Онтология знания и памяти

**Статус:** `DRAFTED / PROVISIONAL` — см. [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md) / [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md). Ожидает independent review и integrated blueprint review вместе с A1 и A3–A10.

Drafted inventory различает:

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

Для каждого concept A2 фиксирует:

- working architectural definition;
- чем concept не является;
- отличия от neighbouring concepts;
- allowed relations;
- identity и lifecycle notes;
- minimum semantic obligations;
- unresolved questions;
- falsification или counterexample;
- provisional classification `CANDIDATE_PRIMITIVE`, `DERIVED_CONCEPT` или `OPEN_QUESTION`.

A2 сравнивает linear pipeline, Event-centred ontology, relation-first model и stratified role ontology. Stratified organization используется только как drafting aid, не Canon. Event и State остаются open primitive questions; Knowledge и Memory не требуют LLM, embeddings, SQL, JSON, digital bytes или specific processor.

**Критерий завершения:** выполнен для first-draft scope: ни один core term не определяется только через Python fields, SQL rows, JSON, graph nodes, embeddings, LLM operation или current Event-sourced laboratory mechanics. Final acceptance всё ещё требует independent/integrated review.

### A3 — Абстрактная машина Native Kernel

**Статус:** `NEXT BOUNDED SLICE`.

Определить minimal technology-independent machine, способную выразить declared architecture.

Candidate stages:

```text
encounter
→ capture
→ identify
→ bind provenance
→ classify semantic role
→ admit or quarantine
→ relate
→ detect conflict
→ revise
→ derive state
→ select context
→ emit bounded explanation/Receipt
```

Final model может reject/reorganize эти stages. Она должна использовать A2 concepts, не превращая A2 navigation groups в mandatory pipeline stages.

Обязательные результаты:

- inventory abstract states;
- transition relations;
- preconditions и postconditions;
- failure states;
- границы deterministic, reproducible и non-deterministic behaviour;
- Authority boundaries.

**Критерий завершения:** минимум два materially different hypothetical substrates map to machine без переноса SQL/Python semantics в Canon.

### A4 — Семантические законы и инварианты

Создать numbered, versioned law set.

Candidate laws:

- representation ≠ represented reality;
- Record ≠ occurrence, которое он описывает;
- Observation ≠ Claim;
- Claim ≠ Truth;
- Evidence ≠ Source;
- repetition ≠ Evidence;
- Belief ≠ Knowledge;
- Memory ≠ merely stored Record;
- retrieval relevance ≠ epistemic validity;
- Conflict ≠ necessarily Contradiction;
- unknown ≠ false;
- Event use in P1–C5 не делает Event universal primitive;
- State ≠ necessarily reducer output;
- storage presence ≠ admission;
- admission ≠ objective truth;
- recency ≠ correctness;
- utility ≠ epistemic validity;
- conflict detection ≠ conflict resolution;
- derived state не может silently rewrite history;
- optimization не может silently change meaning;
- implementation equivalence должна быть named, а не assumed.

Для каждого law указать:

- rationale;
- counterexample;
- failure mode;
- observable obligation;
- known exceptions/open uncertainty.

### A5 — Модель Identity, Time и Change

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
- write/causal order;
- correction, Revision, Supersession, restriction, erasure и forgetting.

**Критерий завершения:** model объясняет, какие Changes preserve identity, create new version, create new entity или remain undecided.

### A6 — Lifecycle знания

Смоделировать путь от raw encounter до possible use, Revision, restriction и historical retention.

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

Определить:

- candidate versus established Conflict;
- Contradiction versus scope mismatch;
- unresolved plurality;
- Uncertainty types;
- missing Evidence и Provenance gaps;
- resolution Authority;
- reversible versus irreversible decisions;
- Belief Revision без rewriting history;
- возможность system оставаться undecided.

### A8 — Контракт substrate independence

Определить, что future implementation обязана preserve или explicitly translate.

Contract классифицирует obligations:

- semantic identity;
- visibility history и Change;
- Provenance;
- temporal meaning;
- visibility Uncertainty и Conflict;
- replay/reconstruction или accepted functional equivalent;
- Authority и admission boundaries;
- bounded explanations/Receipts;
- migration и loss disclosure.

Также нужно определить assumptions, которые могут быть artifacts present Event sourcing.

### A9 — Граница Reference Laboratory

Классифицировать current implementation:

```text
Python + PostgreSQL + SQLite
= bounded reference laboratory
≠ final architecture
```

Для каждого major module позднее определить, является ли он:

- valid example abstract contract;
- temporary experiment;
- implementation-specific mechanism;
- falsification tool;
- legacy evidence, сохраняемым readable, но не governing blueprint;
- candidate for removal/replacement после blueprint review.

На этой фазе code/evidence не удаляются и не переписываются только из-за possible reclassification.

### A10 — Открытые вопросы и критерии falsification

Зафиксировать вопросы, на которые project пока не отвечает.

Примеры:

- Append-only history — Canon requirement или одна implementation explicit Change?
- Может ли identity существовать без stable serialized bytes?
- Каков minimum replay на analog/neuromorphic substrates?
- Какие forms Uncertainty сравнимы across profiles?
- Возможно ли forgetting без permanent retention forbidden content?
- Что означает same semantic State в probabilistic systems?

Каждая major architectural hypothesis должна содержать evidence, способное её weaken/refute.

## 4. Последовательность работы

```text
A1 Purpose и Non-goals                           DRAFTED / PROVISIONAL
→ A2 Ontology                                   DRAFTED / PROVISIONAL
→ A3 Abstract Machine                           NEXT BOUNDED SLICE
→ A4 Semantic Laws
→ A5 Identity / Time / Change
→ A6 Knowledge Lifecycle
→ A7 Conflict / Uncertainty / Revision
→ A8 Substrate Independence
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ operator decision о возобновлении runtime work
```

Documents могут iteratively уточняться, но later layers не могут silently redefine earlier ones.

## 5. Метод исследования

Каждый deliverable должен включать:

1. definitions;
2. explicit non-equivalences;
3. candidate formal model;
4. counterexamples;
5. failure cases;
6. unresolved questions;
7. relationship to existing contracts/runtime;
8. substrate mapping examples;
9. review status;
10. evidence boundary.

Sources, papers, existing systems и AI analyses являются inputs. Они не становятся Canon автоматически.

## 6. Политика runtime freeze

Разрешено:

- critical integrity/security fixes;
- reproducibility/provenance corrections;
- evidence preservation;
- validator/current-truth repair;
- historical recovery;
- isolated architecture experiments без runtime promotion.

Не разрешено без отдельного explicit operator decision:

- новые semantic features;
- reducer v2;
- новый Event vocabulary;
- новые databases, language ports, model adapters или ecosystem integrations;
- performance optimization, меняющая semantic behaviour;
- новые evidence/maturity labels как proof unfinished blueprint.

## 7. Связь с pending decisions

Issue #18 и ADR-0024 остаются pending.

```text
Architecture Re-foundation может продолжаться сейчас.
License selection требуется до open contribution/publication regime.
ADR-0024 требуется до возобновления reducer-v2 path.
```

Ни одно pending decision не блокирует ontology/blueprint research. Ни plan, ни A2 не принимают их silently.

## 8. Gate завершения blueprint

Фаза не завершена только потому, что созданы ten documents.

Completion требует:

- all ten deliverables present/linked;
- reconciled terminology;
- explicit contradictions;
- labelled implementation-specific assumptions;
- open questions/falsification criteria;
- mapping to existing accepted contracts;
- минимум два contrasting substrate thought experiments;
- independent critical review или record unavailable;
- operator review и separate next-phase decision.

## 9. Текущий прогресс

```text
Architecture Re-foundation decision: established by ADR-0025
Blueprint plan: этот документ
Blueprint content: A1-A2 DRAFTED / PROVISIONAL; A3-A10 NOT YET COMPLETE
Next bounded slice: A3 ABSTRACT NATIVE KERNEL MACHINE
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```
