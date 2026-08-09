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

- онтологию;
- семантические законы;
- абстрактные состояния и переходы;
- границы identity, времени, provenance, неопределённости и конфликта;
- substrate-independent obligations;
- правила отображения Canon на implementation profiles;
- явные неизвестные и критерии опровержения.

### Эта фаза не определяет

- новый reducer implementation;
- новый database или programming-language profile;
- product integration;
- performance tuning;
- production deployment;
- доказательство поддержки произвольных будущих substrates.

## 3. Обязательные результаты

### A1 — Purpose и Non-goals Kernel

**Статус:** `DRAFTED` — см. [`A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) / [`A1_KERNEL_PURPOSE_AND_NON_GOALS.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md). Ожидает independent review и integrated blueprint review вместе с `A2`–`A10`.

Определить:

- какую проблему изучает Native Kernel;
- какие долговечные свойства он должен сохранять;
- что означает слово `Kernel` в этом проекте;
- что находится вне Kernel;
- границы с Titan, Crystal, Mentaury, операционными системами, базами данных и model runtimes.

**Критерий завершения:** читатель отличает архитектуру от продукта, базы данных, framework, cognitive system и storage engine без обращения к текущему коду.

### A2 — Онтология знания и памяти

Определить candidate primitives и различия между ними, включая:

```text
Occurrence
Signal
Observation
Record
Claim
Concept
Relation
Context
Source
Provenance
Evidence
Interpretation
Hypothesis
Belief
Uncertainty
Conflict
Decision
Action
Outcome
Experience
Memory
Identity
```

Для каждого primitive зафиксировать:

- определение;
- условия identity;
- lifecycle;
- допустимые связи;
- запрещённые смешения;
- неопределённость;
- принадлежность к Canon, contract или profile.

**Критерий завершения:** ни один core term не определяется только через Python fields, SQL rows, JSON, graph nodes, embeddings или LLM operation.

### A3 — Абстрактная машина Native Kernel

Определить минимальную технологически независимую машину, способную выразить заявленную архитектуру.

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

Финальная модель может отвергнуть или перестроить эти стадии.

Обязательные результаты:

- inventory абстрактных состояний;
- transition relations;
- preconditions и postconditions;
- failure states;
- границы deterministic, reproducible и non-deterministic behaviour;
- authority boundaries.

**Критерий завершения:** как минимум два существенно разных гипотетических substrate могут быть сопоставлены машине без переноса SQL/Python semantics в Canon.

### A4 — Семантические законы и инварианты

Создать нумерованный версионированный набор законов.

Candidate laws:

- representation не равна represented reality;
- record не равен occurrence, которое он описывает;
- storage presence не равна admission;
- admission не равна objective truth;
- evidence relevance не равна truth;
- unknown не равен false;
- recency не равна correctness;
- utility не равна epistemic validity;
- conflict detection не равна conflict resolution;
- derived state не может молча переписать history;
- optimization не может молча изменить meaning;
- implementation equivalence должна быть именованной, а не предполагаемой.

Для каждого закона указать:

- rationale;
- counterexample;
- failure mode;
- observable obligation;
- известные исключения или открытую неопределённость.

### A5 — Модель Identity, Time и Change

Определить без привязки к физическому encoding:

- semantic identity;
- record identity;
- content identity;
- lineage identity;
- aliasing и migration;
- occurrence time;
- observation time;
- valid time;
- record time;
- write/causal order;
- correction, revision, supersession, restriction, erasure и forgetting.

**Критерий завершения:** модель объясняет, какие изменения сохраняют identity, создают новую version, создают новую сущность или пока остаются неразрешёнными.

### A6 — Lifecycle знания

Смоделировать путь от raw encounter до возможного использования, пересмотра, ограничения и исторического сохранения.

Lifecycle должен сохранять различия:

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

Ни одно состояние не получает authority только из storage, retrieval rank, repetition, model confidence или usefulness.

### A7 — Модель Conflict, Uncertainty и Revision

Определить:

- candidate и established conflict;
- contradiction и scope mismatch;
- unresolved plurality;
- типы uncertainty;
- missing evidence и provenance gaps;
- authority разрешения;
- reversible и irreversible decisions;
- belief revision без переписывания history;
- возможность системы оставаться undecided.

### A8 — Контракт substrate independence

Определить, что future implementation обязана сохранить или явно перевести.

Контракт классифицирует обязательства:

- semantic identity;
- видимость history и change;
- provenance;
- temporal meaning;
- видимость uncertainty и conflict;
- replay/reconstruction или принятый functional equivalent;
- authority и admission boundaries;
- bounded explanations/Receipts;
- migration и disclosure потерь.

Также необходимо определить, какие assumptions могут быть артефактами современного event sourcing.

### A9 — Граница Reference Laboratory

Классифицировать текущую реализацию:

```text
Python + PostgreSQL + SQLite
= bounded reference laboratory
≠ final architecture
```

Для каждого крупного модуля позднее определить, является ли он:

- допустимым примером abstract contract;
- временным экспериментом;
- implementation-specific механизмом;
- инструментом falsification;
- legacy evidence, которое должно оставаться читаемым, но не управлять blueprint;
- candidate на removal или replacement после blueprint review.

На этой фазе код и evidence не удаляются и не переписываются только из-за возможной реклассификации.

### A10 — Открытые вопросы и критерии falsification

Зафиксировать вопросы, на которые проект пока не отвечает.

Примеры:

- Является ли append-only history требованием Canon или одной реализацией explicit change?
- Может ли identity существовать без стабильных serialized bytes?
- Каков минимальный смысл replay для analog или neuromorphic substrates?
- Какие формы uncertainty сравнимы между profiles?
- Возможно ли forgetting без постоянного удержания запрещённого content?
- Что означает одинаковое semantic state в probabilistic systems?

Каждая крупная архитектурная гипотеза должна содержать evidence, которое способно её ослабить или опровергнуть.

## 4. Последовательность работы

```text
A1 Purpose и Non-goals
→ A2 Ontology
→ A3 Abstract Machine
→ A4 Semantic Laws
→ A5 Identity / Time / Change
→ A6 Knowledge Lifecycle
→ A7 Conflict / Uncertainty / Revision
→ A8 Substrate Independence
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ интегрированный blueprint review
→ operator decision о возобновлении runtime work
```

Документы могут итеративно уточняться, но поздние слои не могут молча переопределять ранние.

## 5. Метод исследования

Каждый deliverable должен включать:

1. definitions;
2. explicit non-equivalences;
3. candidate formal model;
4. counterexamples;
5. failure cases;
6. unresolved questions;
7. связь с существующими contracts и runtime;
8. substrate mapping examples;
9. review status;
10. evidence boundary.

Источники, papers, existing systems и AI analyses являются inputs. Они не становятся Canon автоматически.

## 6. Политика runtime freeze

Разрешено:

- critical integrity и security fixes;
- reproducibility и provenance corrections;
- evidence preservation;
- validator и current-truth repair;
- historical recovery;
- изолированные architecture experiments без runtime promotion.

Не разрешено без отдельного explicit operator decision:

- новые semantic features;
- reducer v2;
- новый event vocabulary;
- новые databases, language ports, model adapters или ecosystem integrations;
- performance optimization, меняющая semantic behaviour;
- новые evidence или maturity labels как доказательство незавершённого blueprint.

## 7. Связь с pending decisions

Issue #18 и ADR-0024 остаются pending.

```text
Architecture Re-foundation может продолжаться сейчас.
License selection остаётся обязательным до открытого contribution/publication режима.
ADR-0024 остаётся обязательным до возобновления reducer-v2 path.
```

Ни одно pending decision не блокирует ontology и blueprint research. Этот plan не принимает их молча.

## 8. Gate завершения blueprint

Фаза не завершается только потому, что создано десять документов.

Необходимо:

- наличие и linkage всех десяти deliverables;
- reconciliation терминологии;
- явный список противоречий;
- маркировка implementation-specific assumptions;
- открытые вопросы и falsification criteria;
- mapping к существующим accepted contracts;
- минимум два контрастных substrate thought experiments;
- independent critical review или явная запись о его отсутствии;
- operator review и отдельное решение о следующей фазе.

## 9. Текущий прогресс

```text
Architecture Re-foundation decision: established by ADR-0025
Blueprint plan: этот документ
Blueprint content: A1 DRAFTED / A2-A10 NOT YET COMPLETE
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```
