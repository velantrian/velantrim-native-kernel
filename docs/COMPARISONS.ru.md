# 🆚 Native Kernel — заметки о сравнении

**Роль документа:** human-facing, non-authoritative поверхность сравнения  
**Последняя проверка источников:** 2026-08-14  
**Current-state authority:** этот файл **не** определяет runtime, Canon, H11 admission или production state Native Kernel.

## Зачем нужен этот документ

Native Kernel пересекается с memory-, retrieval-, graph- и history-preservation системами, но не пытается заменить их все.

Сравнение отвечает на более узкий вопрос:

> **Какую архитектурную задачу каждый подход в первую очередь пытается решить и какие обязательства прямо входят в его публично заявленную цель?**

Это **не рейтинг** и не основание утверждать, что Native Kernel универсально «лучше».

## Как читать матрицу

- ✅ — явное свойство cited architecture или pattern.
- 🟢 — сильная поддержка в публичном позиционировании с оговорками по scope.
- 🟡 — условная, component-dependent или смежная характеристика, но не формальный invariant.
- 🛡 — design target Native Kernel; **не** заявление universal proof.
- 🎯 — явная research goal / boundary Native Kernel.

Формулировки об отсутствии намеренно консервативны. «Не является заявленным contract» **не** означает «невозможно реализовать».

## Матрица сравнения

| Критерий | 🧬 Native Kernel | 🧠 Letta / MemGPT | 🕸 Graphiti | 📚 Vector RAG | 📜 Event Sourcing |
|---|---|---|---|---|---|
| **Основная сущность** | ⚖️ Семантические обязательства, различия и инварианты между заменяемыми профилями | 💭 Stateful agent + persistent / advanced memory | 🔗 Temporal entities, facts, relationships и source episodes | 📄 Извлекаемые passages / documents, представленные через retrieval index | 📝 Domain events в append-only event stream |
| **Ответ на вопрос** | 🎯 «Какой смысл обязан оставаться валидным или явно изменённым при замене реализации?» | 🤔 «Как агент сохраняет и использует state / memory во времени?» | 🕵️ «Что истинно сейчас или было истинно раньше и как сущности связаны во времени?» | 🔍 «Какой внешний контекст релевантен текущему запросу?» | ⏳ «Какие изменения произошли и как из них получить текущее состояние?» |
| **Устойчивость к смене LLM** | 🛡️ Model-independence — design target; текущие evidence bounded и не являются universal proof | 🟢 Letta прямо заявляет model-agnostic позиционирование; точное поведение всё равно зависит от выбранной модели | 🟡 LLM участвует в extraction / reasoning; cross-model semantic equivalence не является заявленным contract | 🟡 Generator можно заменить; exact output не инвариантен, а retriever / index тоже могут меняться | ✅ Сам pattern по своей природе не зависит от LLM |
| **Устойчивость к смене БД / storage** | 🛡️ Storage-independence — design target; semantic obligations находятся выше конкретного profile | 🟡 Persistent state поддерживает разные deployment modes, но storage-equivalence не является главным публичным contract | 🟡 Есть разные back-end / integration choices; эквивалентность semantics между всеми backends здесь не выводится | 🟡 Index / store заменяемы, но смена embeddings или indexing обычно требует re-indexing | 🟢 Технологию event store можно менять при сохранении порядка, event meaning и migration semantics; при этом pattern всё равно ограничивает storage design |
| **Временной фокус** | 🕰️ Прошлое + настоящее + будущее lifecycle: validity, lineage, revision, obligations и loss | 🕰️ Long-lived agent state между взаимодействиями | 📜 Прошлое + настоящее temporal validity с изменяющимися facts | 📖 Current retrieval по внешнему corpus; время важно только если оно представлено в данных / metadata | 🗂️ Историческая последовательность events → текущее state |
| **Сбой / перезапуск** | 🔄 Conforming implementation должна восстанавливать durable semantic state и unresolved obligations; текущая лаборатория не universal proof | ✅ Persistent agent state / memory рассчитаны на сохранение между sessions, если backing state сохранён | ✅ Persisted context graph поддерживает incremental updates; полный rebuild при каждом restart не требуется | ✅ Persisted index переживает restart; conversational / workflow state находится вне plain RAG | ✅ State можно rehydrate из event stream; projections / snapshots позволяют не replay-ить всю историю с genesis каждый раз |
| **Роль в стеке** | 🏛️ Semantic-contract / «constitution-like» слой | 🧩 Agent runtime + memory / context layer | 🗺️ Temporal context-graph / memory layer | 📇 Retrieval / knowledge-augmentation layer | 📋 Persistence + history architecture pattern |
| **Что должно переживать замену реализаций?** | 🎯 Заявленные semantic obligations и distinctions — если replacement conforming; потеря должна быть явной | 🟡 Agent-memory abstractions могут переживать model swap, но exact behavioral equivalence публично не гарантируется | 🟡 Сохранённый temporal graph / provenance может переживать замену компонентов; extraction behavior может измениться | 🟡 Source corpus может сохраниться; embeddings / index часто требуют regeneration при смене encoder или indexing semantics | ✅ Event history может переживать замену реализации при сохранении event schema / meaning; business logic автоматически не сохраняется |

## Почему некоторые интуитивные сокращения здесь намеренно не используются

Несколько эффектных формулировок слишком сильны для research-facing репозитория:

- **Letta нельзя корректно назвать «слабо устойчивой к смене LLM»**: текущий публичный README прямо называет платформу model-agnostic. Это не означает идентичное поведение всех моделей.
- **Graphiti не требует общего полного перестроения графа после restart**: публичный README подчёркивает incremental updates без complete graph recomputation.
- **Persisted Vector RAG index не исчезает при restart агента**: plain RAG просто не определяет более широкий conversational / workflow state агента.
- **Event sourcing не обязан replay-ить историю от genesis при каждом запросе**: materialized views, projections и snapshots используются, чтобы избегать полного replay.
- **Native Kernel не утверждает «переживает вообще всё»**: architecture требует сохранения заявленных semantic obligations при conforming replacement либо явной фиксации loss / change. Текущие evidence bounded.

Эти коррекции делают таблицу менее рекламной, но значительно более защищаемой.

## Что это сравнение реально означает

### 🧠 Letta / MemGPT

Текущий репозиторий Letta описывает Letta как платформу для **stateful agents** с advanced memory, способной поддерживать learning/self-improvement over time. Там же прямо заявляется model-agnostic позиционирование.

Поэтому Native Kernel пересекается с Letta в long-lived state и memory, но задаёт другой архитектурный вопрос: какие semantic obligations должны оставаться валидными, если меняется agent framework, model, storage profile или substrate?

### 🕸 Graphiti

Graphiti описывает себя как framework для **temporal context graphs for AI agents**. В публичной документации прямо присутствуют temporal validity, изменение фактов, source episodes/provenance, hybrid retrieval и incremental updates без полного graph recomputation.

По нескольким измерениям это делает Graphiti гораздо ближе к Native Kernel, чем flat vector store. Различие в scope: Native Kernel рассматривает provenance, uncertainty, revision, loss, authority и substrate replacement как части technology-neutral contract, а не выбирает temporal graph как саму архитектуру.

### 📚 Vector RAG

Исходная RAG-формулировка объединяет parametric model memory с внешней non-parametric memory, доступной через retrieval; исходная реализация использует dense vector index и neural retriever. Основная задача — retrieval-augmented generation для knowledge-intensive tasks.

Vector RAG stack может быть полезным механизмом внутри Native Kernel-compatible системы, но retrieval relevance само по себе не устанавливает semantic identity, authority, provenance, lifecycle или revision obligations claim.

### 📜 Event sourcing

Event-sourcing pattern хранит последовательность изменений/events как append-only system of record и позволяет восстанавливать/materialize текущий state из этой истории. Canonical guidance также подчёркивает materialized views и projections, потому что постоянный full replay дорог.

Это полезно для auditability и historical reconstruction. Native Kernel специально не приравнивает «существует event log» к «knowledge semantics сохранены»: event sourcing может быть implementation/profile mechanism, не становясь universal Kernel law.

### 🧬 Native Kernel

Заявленный фокус Native Kernel — не конкретный memory engine. Проект исследует, какие semantic distinctions и obligations должны переживать замену реализаций и как failure, uncertainty, revision, supersession, retention/loss, provenance и authority остаются явными.

Текущая реализация — **bounded reference laboratory**, а не доказательство того, что её Python/PostgreSQL/SQLite/event-oriented mechanisms являются universal Canon.

## Реестр источников

Проверено **2026-08-14** по primary или canonical sources:

| Объект | Источник | Что он подтверждает в этом сравнении |
|---|---|---|
| Letta / MemGPT | https://github.com/letta-ai/letta | Фокус на stateful agents и advanced memory; текущее публичное model-agnostic позиционирование; persistent/local/self-hosted deployment framing |
| Graphiti | https://github.com/getzep/graphiti | Temporal context graphs, temporal validity, source provenance, incremental updates, отсутствие требования полного graph recomputation, agent retrieval/context focus |
| Retrieval-Augmented Generation | https://arxiv.org/abs/2005.11401 | Исходный RAG framing: parametric + non-parametric memory, dense vector index, neural retrieval и retrieval-augmented generation |
| Event sourcing | https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing | Append-only event/change history, system-of-record role, rehydration, materialized views/projections и migration/design trade-offs |
| Native Kernel | ../PROJECT_OVERVIEW.ru.md и ../ARCHITECTURE.md | Собственные заявленные architecture, boundaries и non-claims Native Kernel |

## Правило поддержки

При существенном изменении сравнения:

1. заново проверить внешние primary sources;
2. обновить **Последнюю проверку источников**;
3. предпочитать conditional / scoped формулировки необоснованным «система X не умеет Y»;
4. держать матрицу в root README достаточно компактной, чтобы она ориентировала, а не заменяла этот документ;
5. сохранять подробные caveats и source ledger здесь;
6. не превращать comparison language в Native Kernel authority, evidence или current-state claim.

Если внешний проект изменился, должен измениться этот документ. Stable Native Kernel architecture не должна зависеть от того, что competitor остаётся неизменным.
