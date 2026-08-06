# 📚 Документация Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

Эта папка разделяет назначение проекта, архитектуру, проверку соответствия, исследовательские предложения, интеграционные границы, принятые решения и записи непрерывности для ИИ и людей.

> [!IMPORTANT]
> Всегда смотрите на статус документа. Описанное или принятое архитектурное решение ещё не означает, что соответствующий механизм реализован в коде.

## С чего начинать

| Документ | Для чего он нужен | Статус |
|---|---|---|
| [`../AGENTS.md`](../AGENTS.md) | Обязательные правила первого чтения для ИИ, аудиторов и ревьюеров | действующее руководство репозитория |
| [`ai/README.md`](./ai/README.md) | AI context pack: текущее состояние, карта документов, риски, метод аудита, журнал и протокол GitHub↔Notion | действующий слой непрерывности |
| [`FOUNDATIONAL_INTENT.ru.md`](./FOUNDATIONAL_INTENT.ru.md) · [English](./FOUNDATIONAL_INTENT.md) | Глубокое объяснение, зачем Native Kernel существует отдельно, какую проблему исследует и что будет означать успех | архитектурный замысел |
| [`FOUNDATIONAL_CONTRACT_SKELETON.ru.md`](./FOUNDATIONAL_CONTRACT_SKELETON.ru.md) · [English](./FOUNDATIONAL_CONTRACT_SKELETON.md) | Каркас из шести семейств: семантические роли, идентичность, события, полномочия, конфликт/unknown и семантическая эквивалентность | принятая abstract-contract map; не реализована |
| [`contracts/NORMATIVE_CONTRACTS_V1.ru.md`](./contracts/NORMATIVE_CONTRACTS_V1.ru.md) · [English](./contracts/NORMATIVE_CONTRACTS_V1.md) | Точные v1-контракты identity, single-writer append/replay, deletion/restriction и executable fixtures | приняты ADR-0011…0014; fixture tooling проверено локально; Kernel runtime не реализован |
| [`LONG_HORIZON_VISION.md`](./LONG_HORIZON_VISION.md) | Архитектурный Canon, контракты, профили и будущие технологии | исследовательское видение |
| [`STORAGE_AND_EXECUTION_PROFILES.ru.md`](./STORAGE_AND_EXECUTION_PROFILES.ru.md) · [English](./STORAGE_AND_EXECUTION_PROFILES.md) | PostgreSQL как основной полный профиль, SQLite как опциональный embedded-профиль, offline-работа, выбор профиля и миграция | принятое направление; не реализовано |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | Как проверить соответствие реализации архитектуре | принятый abstract contract; fixture-integrity tooling существует; Kernel runtime evidence отсутствует |
| [`DECISION_PROCESS.md`](./DECISION_PROCESS.md) | Как разделять решение, доказательства, реализацию, мнение ИИ и одобрение оператора | процесс управления решениями |
| [`adr/README.md`](./adr/README.md) | Индекс Architecture Decision Records | действующий governance-процесс |
| [`VELANTRIM_ECOSYSTEM.md`](./VELANTRIM_ECOSYSTEM.md) | Роли и ссылки Native Kernel, Mentaury Soul, Titan и Crystal | карта навигации и границ |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | Технические границы Native Kernel, Titan, Mentaury и Crystal | документированная граница |
| [`BENCHMARKS.md`](./BENCHMARKS.md) | Правила бенчмарков и доказательств | исследовательская политика |
| [`research/BIO_INSPIRED_COMPUTATION_AND_KITARA.ru.md`](./research/BIO_INSPIRED_COMPUTATION_AND_KITARA.ru.md) · [English](./research/BIO_INSPIRED_COMPUTATION_AND_KITARA.md) | Био-вдохновлённый и Kitara research-трек | proposed / experimental / not implemented |
| [`research/PHYSARUM_ROUTING_EXPERIMENT.ru.md`](./research/PHYSARUM_ROUTING_EXPERIMENT.ru.md) · [English](./research/PHYSARUM_ROUTING_EXPERIMENT.md) | Ограниченный эксперимент адаптивной flow-маршрутизации | proposed / not implemented |

## Рекомендуемый порядок чтения

```text
1. AGENTS.md + STATUS.md
        ↓
2. docs/ai context pack
        ↓
3. FOUNDATIONAL_INTENT
        ↓
4. FOUNDATIONAL_CONTRACT_SKELETON
        ↓
5. NORMATIVE_CONTRACTS_V1 + ADR-0011…0014
        ↓
6. LONG_HORIZON_VISION
        ↓
7. STORAGE_AND_EXECUTION_PROFILES
        ↓
8. ARCHITECTURE.md в корне
        ↓
9. CONFORMANCE_MODEL + fixture pack в contracts/
        ↓
10. DECISION_PROCESS + ADR
        ↓
11. ROADMAP + необязательные research notes
```

## Главное различие

```text
Архитектурный Canon
≠ Абстрактный контракт
≠ Принятый точный контракт
≠ Fixture-integrity tooling
≠ Профиль реализации
≠ Реализованный Kernel runtime
≠ Production-доказательства
```

Современные технологии используются как лабораторные инструменты. Они не становятся постоянным определением архитектуры только потому, что применяются сегодня.

## Простыми словами

Native Kernel нужен, чтобы:

- сегодня проверять идеи на доступных инструментах;
- завтра заменять инструменты без переписывания смысла;
- хранить историю архитектурных решений;
- не путать идею, принятое решение, код и доказательство;
- не превращать мнение нескольких ИИ в evidence;
- развивать Kernel отдельно от Titan, Mentaury и Crystal.

## Более глубокое объяснение

Проект меняет обычный порядок:

```text
сначала смысл и инварианты
        ↓
затем абстрактные контракты
        ↓
после этого заменяемые технологические профили
```

Подробное объяснение находится здесь:

- [`FOUNDATIONAL_INTENT.ru.md`](./FOUNDATIONAL_INTENT.ru.md)
- [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md)
- [`FOUNDATIONAL_CONTRACT_SKELETON.ru.md`](./FOUNDATIONAL_CONTRACT_SKELETON.ru.md)
- [`FOUNDATIONAL_CONTRACT_SKELETON.md`](./FOUNDATIONAL_CONTRACT_SKELETON.md)
- [`contracts/NORMATIVE_CONTRACTS_V1.ru.md`](./contracts/NORMATIVE_CONTRACTS_V1.ru.md)
- [`contracts/NORMATIVE_CONTRACTS_V1.md`](./contracts/NORMATIVE_CONTRACTS_V1.md)

## Граница executable fixtures

В репозитории уже есть принятые schemas, golden/invalid vectors и standard-library fixture validator до появления Kernel runtime.

```text
fixture pack PASS
≠ Kernel runtime реализован
≠ C2 Kernel profile conformance
≠ C3 cross-profile equivalence
≠ production deletion guarantee
```

Команды описаны в [`../tools/conformance/README.md`](../tools/conformance/README.md). Machine-readable артефакты: `contracts/registry.json`, `contracts/schema-bundle.json`, `contracts/evidence-report-v1.schema.json`, `contracts/fixture-pack.json`, `contracts/idempotency-scenarios.json`.

Conformance workflow поддерживает PR/push triggers и ручной `workflow_dispatch`; доступный trigger ещё не является выполненным run.

## Необязательный экспериментальный трек

Полезные внешние идеи, которые не входят в Canon, сохраняются как явно ограниченные research notes.

```text
периферийная обработка событий
Adaptive Gain
процедурная / моторная память
сенсомоторные петли
адаптация распределённой сети
Physarum-подобная маршрутизация
```

Эти механизмы могут проверяться как заменяемые profiles. Они не должны определять истину, обходить policy, превращаться в runtime claims или расширять Issue #1.

## Для ИИ и ревьюеров

Начинайте с [`../AGENTS.md`](../AGENTS.md) и [`ai/README.md`](./ai/README.md).
Перед изменением необходимо:

1. проверить точный SHA репозитория или PR;
2. проверить `STATUS.md` и последний verified checkpoint;
3. определить архитектурный уровень;
4. сохранить границы Native Kernel / Titan / Mentaury / Crystal;
5. разделить proposal, acceptance, evidence, implementation и approval;
6. создать или обновить ADR для долговременного решения;
7. не расширять Issue #1 redesign-работой;
8. не превращать технологию, биологическую метафору или adaptive routing в постоянный Canon или epistemic authority;
9. обновлять AI context pack и GitHub↔Notion record при изменении существенных фактов.
