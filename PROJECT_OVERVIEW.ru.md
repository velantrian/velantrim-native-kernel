# 🧬 Velantrim Native Kernel — Human Project Overview

**[English](./PROJECT_OVERVIEW.md) · [Русский](./PROJECT_OVERVIEW.ru.md)**

> **Аудитория:** человек, который хочет понять архитектуру до чтения формальных contracts.  
> **Это не live-state ledger:** для текущих gates, authorization и evidence status используйте [STATUS.md](STATUS.md) и [project-state.json](project-state.json).  
> **AI agents:** начинайте с [docs/ai/README.md](docs/ai/README.md), а не с этого narrative.

## 🎯 Проблема

Большинство knowledge-систем описывают через технологию, которая их сейчас реализует:

- строки и таблицы;
- документы и JSON;
- graph nodes и edges;
- embeddings и vector search;
- event logs и reducers;
- model context и agent memory.

Эти механизмы полезны, но они не становятся автоматически *смыслом* знания.

Native Kernel задаёт другой вопрос:

> Если storage engine, programming language, processor, memory representation или inference model заменить, **какие semantic obligations должны сохраниться, чтобы мы могли сказать, что тот же процесс знания продолжился?**

Поэтому проект пытается отделить **architecture-level meaning** от **profile-level realization**.

## 🧠 Mental model

```text
world / source
     │
     ▼
👁 observation
     │
     ▼
💬 claim
     │
     ├───────────────┐
     ▼               ▼
🔎 evidence       🧭 provenance
     │               │
     └───────┬───────┘
             ▼
       ⚖ epistemic position
             │
      ┌──────┼────────┐
      ▼      ▼        ▼
   🌫 doubt ⚔ conflict 🔁 revision
      │      │        │
      └──────┴────────┘
             ▼
       🧾 explanation
             │
             ▼
      🕰 accountable history
```

Архитектуру интересуют **relations и obligations** между этими понятиями. Она не требует, чтобы каждая реализация хранила их в одном и том же byte layout.

## 🏛️ Архитектурные слои

```text
┌──────────────────────────────────────────────────────────────┐
│ 🧠 SEMANTIC MEANING                                         │
│ identity · evidence · provenance · uncertainty · revision   │
└───────────────────────────┬──────────────────────────────────┘
                            │ obligations
┌───────────────────────────▼──────────────────────────────────┐
│ 📐 TECHNOLOGY-NEUTRAL CONTRACTS                              │
│ what a conforming realization must preserve / expose        │
└───────────────────────────┬──────────────────────────────────┘
                            │ mapping
┌───────────────────────────▼──────────────────────────────────┐
│ 🔌 PROFILES                                                  │
│ a concrete way to realize the obligations                   │
└───────────────────────────┬──────────────────────────────────┘
                            │ implementation
┌───────────────────────────▼──────────────────────────────────┐
│ 🧪 REFERENCE LABORATORY                                     │
│ executable, bounded, replaceable research machinery         │
└───────────────────────────┬──────────────────────────────────┘
                            │ observations
┌───────────────────────────▼──────────────────────────────────┐
│ 🔬 EVIDENCE / FALSIFICATION                                 │
│ what survived, failed, weakened, or remains untested        │
└───────────────────────────┬──────────────────────────────────┘
                            │ informs — never auto-promotes
┌───────────────────────────▼──────────────────────────────────┐
│ 🚦 GOVERNED DECISIONS                                       │
│ architecture / Final Canon / runtime / production           │
└──────────────────────────────────────────────────────────────┘
```

Нижний слой не имеет права незаметно переписывать верхний. Удобный implementation choice не становится универсальным законом только потому, что текущий код его использует.

## 🧩 Semantic obligations

Текущая архитектурная работа разделяет несколько семейств concerns.

| Concern | Какой вопрос задаёт Native Kernel |
|---|---|
| 🧠 Knowledge | Чем observation отличается от claim, evidence item и epistemic position? |
| 🔎 Provenance | Откуда пришёл claim/evidence и что именно этот provenance доказывает? |
| 🕰 Identity & time | Что остаётся «тем же самым» при revision, copying, migration и change? |
| 🌫 Uncertainty | Как представить not-knowing, не превращая его незаметно в ложную certainty? |
| ⚖ Conflict | Как несовместимые positions могут сосуществовать без искусственного universal winner? |
| 🔁 Revision | Как belief меняется, supersede-ится или ослабляется с сохранением accountability? |
| 🗑 Loss / erasure | Что доказывает logical disappearance — и чего не доказывает о physical deletion? |
| 🧾 Explanation | Может ли система объяснить, почему существует текущий state и какое evidence на него повлияло? |
| 🌍 Substrate independence | Могут ли эти obligations пережить смену representation или computational substrate? |

Отсюда следует важное правило:

```text
storage fact ≠ semantic truth
operation receipt ≠ correctness
history visibility ≠ mandatory event sourcing
graph representation ≠ mandatory graph architecture
embedding retrieval ≠ knowledge
profile conformance ≠ production authorization
```

## 🌍 Что здесь означает substrate-neutral

Substrate neutrality — **не** утверждение, что одна текущая implementation уже без изменений работает на любой возможной машине.

Это более строгая архитектурная дисциплина: проект должен быть описуем без случайного превращения сегодняшних механизмов в вечные требования.

Например:

```text
Architecture obligation:
  "revision должна сохранять достаточно lineage,
   чтобы различать replacement, supersession
   и unresolved conflict"

Possible realization A:
  PostgreSQL rows + explicit provenance records

Possible realization B:
  graph edges + temporal validity

Possible realization C:
  append-only cells + derived views

Possible realization D:
  future non-von-Neumann substrate

Question:
  сохраняют ли все четыре declared obligation?
```

Если mapping не может сохранить obligation, корректным результатом может быть **LOSSY**, **PARTIAL**, **REFUTED** или **INDETERMINATE**. Архитектура должна это показать, а не спрятать.

## 🧪 Зачем нужен reference laboratory

Чисто абстрактную архитектуру легко переоценить. Laboratory существует, чтобы атаковать abstractions исполняемыми случаями.

Текущая laboratory lineage включает обычные software mechanisms — Python, PostgreSQL, SQLite и independent-language experiments. Их роль намеренно bounded:

```text
laboratory
   ├── produces observations
   ├── exposes implementation assumptions
   ├── gives invariants something concrete to fail against
   └── provides reproducible evidence
        │
        └── but does NOT define permanent Canon
```

Это позволяет спрашивать:

- переживает ли invariant смену storage?
- зависит ли claim от event-sourced representation, которую архитектура никогда не обосновывала?
- действительно ли нужен «replay», или достаточно accountable reconstruction?
- сохраняет ли механизм meaning или лишь bytes?
- тестировал ли experiment гипотезу или только удобный proxy?

## 🔬 Evidence before promotion

Native Kernel намеренно разделяет состояния:

```text
IMPLEMENTED
    ↓
TESTED
    ↓
EVIDENCE QUALIFIED
    ↓
SUPPORTED FOR A DECLARED SCOPE
    ↓
ARCHITECTURE REASSESSED
    ↓
possible operator decision

None of these arrows is automatic.
```

Failed experiment полезен. Indeterminate experiment полезен. Результат, который ослабляет architecture, полезен.

Research process не оптимизируется на то, чтобы текущий design «победил»; он должен выявлять места, где claims слишком сильны.

## 🆚 Связь с agent-memory и graph systems

Native Kernel пересекается с memory systems, но unit of concern у него другой.

### 🧠 Letta / MemGPT

Letta описывает себя как platform для stateful agents с advanced persistent memory. Это agent-level задача: как agent помнит, учится и переносит state через interactions/models.

Native Kernel задаёт более низкоуровневый архитектурный вопрос: если memory mechanism заменить, какие semantic properties обязаны сохраниться, чтобы новая система считалась equivalent для declared scope?

### 🕸 Graphiti

Graphiti — open-source temporal context graph engine для AI agents. Он отслеживает evolving facts, temporal validity и provenance и поддерживает graph-aware retrieval.

Эти capabilities очень релевантны Native Kernel, но Native Kernel не объявляет graph универсальным representation. Graph может быть одним profile, если сохраняет требуемую semantics.

### 📚 RAG, event sourcing и другие механизмы

RAG может быть retrieval mechanism. Event sourcing — history mechanism. Relational database — storage mechanism. Graph — relation mechanism. LLM — inference mechanism.

Native Kernel рассматривает их как **candidate instruments**, а не identity-defining primitives.

| Mechanism | Native Kernel view |
|---|---|
| Vector search | полезный retrieval profile, не knowledge itself |
| Knowledge graph | полезный relational profile, не обязательная universal topology |
| Event log | полезный history profile, не автоматически universal semantic primitive |
| LLM memory block | полезный agent-memory profile, не source of architectural truth |
| SQL schema | полезный durable mapping, не Canon сам по себе |

Официальная основа сравнения: [Letta](https://github.com/letta-ai/letta) и [Graphiti](https://github.com/getzep/graphiti).

## 🧭 Что делает проект необычным

Особенно важны четыре решения:

1. **Implementation намеренно понижена в статусе.**  
   Текущий working code — evidence-producing machinery, а не определение architecture.

2. **Uncertainty и conflict — first-class.**  
   Система должна уметь сказать «unresolved», «weakened» или «unknown», не превращая это в принудительный binary answer.

3. **Evidence имеет bounded authority.**  
   Passed test поддерживает только hypotheses и scope, которые действительно adjudicated.

4. **Promotion управляется отдельно.**  
   Architecture, Final Canon, runtime authorization и production authorization — разные решения.

## 🧱 Чем проект не пытается быть

Native Kernel сейчас не заявляет себя как:

- production database;
- universal memory server;
- законченный autonomous-agent framework;
- replacement для любого knowledge graph;
- доказательство того, что один event model работает на каждом substrate;
- доказательство quantum, neuromorphic или biological portability;
- production-authorized runtime.

Это могут быть будущие implementation contexts или experiments. Они не следуют автоматически из текущей architecture.

## 📚 Deep reading map

```text
👤 Human understanding
README.ru.md
  ↓
PROJECT_OVERVIEW.ru.md
  ↓
ARCHITECTURE.md
  ↓
docs/A1...A10
  ↓
docs/research/
  ↓
evidence/

🤖 Machine / agent continuity
docs/ai/README.md
  ↓
AGENTS.md
  ↓
project-state.json
  ↓
docs/ai/CURRENT_STATE.md
  ↓
required contracts / ADRs / research artifacts

📊 Live state
STATUS.md + project-state.json
```

Полезные entry points:

- [ARCHITECTURE.md](ARCHITECTURE.md) — архитектурная ориентация.
- [docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md](docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) — purpose и non-goals.
- [docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md](docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md) — ontology.
- [docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md](docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md) — substrate-independence contract.
- [docs/A9_REFERENCE_LABORATORY_BOUNDARY.ru.md](docs/A9_REFERENCE_LABORATORY_BOUNDARY.ru.md) — laboratory vs architecture.
- [docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.ru.md](docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.ru.md) — hypotheses и falsification.
- [STATUS.md](STATUS.md) — current human-readable status.
- [project-state.json](project-state.json) — machine-readable state.
- [docs/ai/README.md](docs/ai/README.md) — AI/agent entrypoint.

## 🚦 Authority note

Этот overview намеренно **stable**. Его нужно менять, когда меняется conceptual architecture, а не после каждого PR.

Если нужно узнать, открыт ли gate, квалифицирован ли reviewer, разрешён ли runtime или какой evidence checkpoint текущий, не выводите это из этой страницы. Читайте current-state surfaces.

> **Коротко:** Native Kernel пытается сделать knowledge architecture устойчивой к технологической замене, не притворяясь, что preservation произошло, если evidence говорит обратное.
