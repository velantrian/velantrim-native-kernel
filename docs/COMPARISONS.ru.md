# 🆚 Native Kernel — заметки о сравнении

**Роль документа:** human-facing, non-authoritative поверхность сравнения  
**Последняя проверка источников:** 2026-08-14  
**Current-state authority:** этот файл **не** определяет runtime, Canon, H11 admission или production state Native Kernel.

## Зачем нужен этот документ

Native Kernel пересекается с memory-, retrieval-, graph- и history-preservation системами, но не пытается заменить их все.

Сравнение отвечает на более узкий вопрос:

> **Какую архитектурную задачу каждый подход в первую очередь пытается решить и какие обязательства прямо входят в его публично заявленную цель?**

Это **не рейтинг** и не основание утверждать, что Native Kernel универсально «лучше».

## Как читать обозначения

- ✅ — явно центральная функция по cited source или архитектуре.
- 🟡 — функция присутствует или близка, но это не тот же архитектурный target.
- ◻️ — **не обнаружено как основная заявленная цель в проверенных материалах**; это не доказывает отсутствие capability.
- 🔌 — может использоваться как optional implementation mechanism.
- 🎯 — явная research goal или boundary Native Kernel.

## Матрица сравнения

| Критерий | 🧠 Letta / MemGPT | 🕸 Graphiti | 📚 Vector RAG | 📜 Event sourcing | 🧬 Native Kernel |
|---|---|---|---|---|---|
| **Основной заявленный фокус** | Stateful agents с advanced/persistent memory | Temporal context graphs для AI agents | Retrieval-augmented generation с внешней non-parametric memory | Append-only история изменений/events с восстановлением текущего state | Сохранение заявленных semantic obligations между заменяемыми реализациями |
| **Agent memory / retrieval** | ✅ Core | ✅ Core retrieval/context function | ✅ Core retrieval function | ◻️ Не основная задача pattern | 🔌 Optional mechanism, а не сама архитектура |
| **Temporal relations / provenance** | 🟡 Persistent agent state/history; здесь не приравнивается к тому же provenance contract | ✅ Явные temporal validity и provenance к source episodes | 🟡 Retrieved sources могут давать grounding, но provenance semantics не являются архитектурой исходной RAG-формулировки | ✅ Historical reconstruction/auditability центральны | ✅ Явная архитектурная concern |
| **Поверхность заменяемости implementation** | 🟡 Letta публично описывает model-agnostic operation; это не считается доказательством cross-substrate semantic equivalence | 🟡 Framework/back-end choices — implementation concern; semantic-equivalence claim здесь не выводится | 🟡 Retriever, index, generator и corpus могут меняться | 🟡 Переиспользуемый architecture pattern, но его adoption ограничивает storage/state design | 🎯 Замена implementation/profile — явная boundary |
| **Substrate-neutral semantic contract** | ◻️ Не обнаружено как основная заявленная цель в cited source | ◻️ Не обнаружено как основная заявленная цель в cited source | ◻️ Не является целью исходной RAG-формулировки | ◻️ Event history сама по себе не представлена как substrate-neutral knowledge-semantics contract | 🎯 Core research goal |
| **Falsification-first architecture** | ◻️ Не обнаружено как основная заявленная цель в cited source | ◻️ Не обнаружено как основная заявленная цель в cited source | ◻️ Не является целью исходной RAG-формулировки | ◻️ Не основная задача pattern | 🎯 Core research method |

## Что это сравнение реально означает

### 🧠 Letta / MemGPT

Текущий репозиторий Letta описывает Letta как платформу для **stateful agents** с advanced memory, способной поддерживать learning/self-improvement over time. Также публично заявляется model-agnostic позиционирование.

Поэтому Native Kernel пересекается с Letta в long-lived state и memory, но задаёт другой архитектурный вопрос: какие semantic obligations должны оставаться валидными, если меняется agent framework, model, storage profile или substrate?

### 🕸 Graphiti

Graphiti описывает себя как framework для **temporal context graphs for AI agents**. В публичной документации прямо присутствуют temporal validity, изменение фактов, source episodes/provenance и hybrid retrieval.

По нескольким измерениям это делает Graphiti гораздо ближе к Native Kernel, чем flat vector store. Различие в scope: Native Kernel рассматривает provenance, uncertainty, revision, loss, authority и substrate replacement как части technology-neutral contract, а не выбирает temporal graph как саму архитектуру.

### 📚 Vector RAG

Исходная RAG-формулировка объединяет parametric model memory с внешней non-parametric memory, доступной через retrieval. Основная задача — retrieval-augmented generation для knowledge-intensive tasks.

Vector RAG stack может быть полезным механизмом внутри Native Kernel-compatible системы, но retrieval relevance само по себе не устанавливает semantic identity, authority, provenance, lifecycle или revision obligations claim.

### 📜 Event sourcing

Event-sourcing pattern хранит последовательность изменений/events как append-only system of record и позволяет восстанавливать/materialize текущий state из этой истории.

Это полезно для auditability и historical reconstruction. Native Kernel специально не приравнивает «существует event log» к «knowledge semantics сохранены»: event sourcing может быть implementation/profile mechanism, не становясь universal Kernel law.

### 🧬 Native Kernel

Заявленный фокус Native Kernel — не конкретный memory engine. Проект исследует, какие semantic distinctions и obligations должны переживать замену реализаций и как failure, uncertainty, revision, supersession, retention/loss, provenance и authority остаются явными.

Текущая реализация — **bounded reference laboratory**, а не доказательство того, что её Python/PostgreSQL/SQLite/event-oriented mechanisms являются universal Canon.

## Реестр источников

Проверено **2026-08-14** по primary или canonical sources:

| Объект | Источник | Что он подтверждает в этом сравнении |
|---|---|---|
| Letta / MemGPT | https://github.com/letta-ai/letta | Фокус на stateful agents и advanced memory; текущее публичное model-agnostic позиционирование |
| Graphiti | https://github.com/getzep/graphiti | Temporal context graphs, temporal validity, source provenance, agent retrieval/context focus |
| Retrieval-Augmented Generation | https://arxiv.org/abs/2005.11401 | Исходный RAG framing: parametric + non-parametric memory и retrieval-augmented generation |
| Event sourcing | https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing | Append-only event/change history, system-of-record role, materialized state и trade-offs |
| Native Kernel | ../PROJECT_OVERVIEW.ru.md и ../ARCHITECTURE.md | Собственные заявленные architecture, boundaries и non-claims Native Kernel |

## Правило поддержки

При существенном изменении сравнения:

1. заново проверить внешние primary sources;
2. обновить **Последнюю проверку источников**;
3. предпочитать формулировку «не обнаружено как основная заявленная цель» вместо необоснованного «система этого не умеет»;
4. оставлять root README коротким;
5. не превращать comparison language в Native Kernel authority, evidence или current-state claim.

Если внешний проект изменился, должен измениться этот документ. Stable Native Kernel architecture не должна зависеть от того, что competitor остаётся неизменным.
