# 📚 Документация Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

Эта папка разделяет назначение, архитектуру, контракты, profiles, evidence, research, интеграционные границы и continuity records.

> [!IMPORTANT]
> Текущая зрелость: `RESEARCH / P4 PARTIAL ASSERTION CONFORMANCE / NOT PRODUCTION-READY`. Acceptance, implementation и evidence остаются разными состояниями.

## С чего начинать

| Документ | Назначение | Текущая граница |
|---|---|---|
| [`../AGENTS.md`](../AGENTS.md) | Обязательные правила репозитория | P4/C2 и phase boundaries |
| [`../STATUS.md`](../STATUS.md) | Authoritative текущее состояние | 41 supported / 13 partial / 18 unsupported |
| [`ai/README.md`](./ai/README.md) | Карта AI/human continuity | active context pack |
| [`ai/P4_IMPLEMENTATION_RECORD.md`](./ai/P4_IMPLEMENTATION_RECORD.md) | Exact P4 checks, runs, artifacts и limitations | previous-head C2 evidence |
| [`FOUNDATIONAL_INTENT.ru.md`](./FOUNDATIONAL_INTENT.ru.md) · [English](./FOUNDATIONAL_INTENT.md) | Зачем существует Native Kernel | архитектурный замысел |
| [`FOUNDATIONAL_CONTRACT_SKELETON.ru.md`](./FOUNDATIONAL_CONTRACT_SKELETON.ru.md) · [English](./FOUNDATIONAL_CONTRACT_SKELETON.md) | Карта contract families | accepted abstraction |
| [`contracts/NORMATIVE_CONTRACTS_V1.ru.md`](./contracts/NORMATIVE_CONTRACTS_V1.ru.md) · [English](./contracts/NORMATIVE_CONTRACTS_V1.md) | Exact v1 identity/event/deletion/fixture contracts | accepted; profile support partial |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | Assertion states и C0–C5 | P4 adapter реализован; C3 отсутствует |
| [`rfc/0002-postgresql-reference-profile-v0.ru.md`](./rfc/0002-postgresql-reference-profile-v0.ru.md) | Lifecycle clean PostgreSQL profile | P1–P4 active lineage |
| [`adr/README.md`](./adr/README.md) | Durable decisions | ADR-0018 accepted |
| [`VELANTRIM_ECOSYSTEM.md`](./VELANTRIM_ECOSYSTEM.md) | Роли проектов | navigation/boundary map |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | Cross-project boundaries | runtime inheritance отсутствует |
| [`DECISION_PROCESS.md`](./DECISION_PROCESS.md) | Разделение decision/evidence/approval | governance process |

## Порядок чтения

```text
AGENTS + STATUS
→ AI context pack + P4 implementation record
→ foundational intent/contracts
→ Architecture Canon
→ RFC-0002 + ADR-0015…0018
→ source/tests/manifests/workflows
→ exact run/jobs/artifacts
```

## Главное различие

```text
Architecture Canon
≠ Abstract Contract
≠ Accepted Decision
≠ Implementation Profile
≠ Assertion Result
≠ Evidence Level
≠ Production Evidence
```

Текущая карта P4:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
support_state: PARTIAL
```

```text
P4 C2 ≠ все 72 supported
P4 C2 ≠ C3
P4 C2 ≠ truth/authenticity
P4 C2 ≠ physical deletion
```

## Слои executable evidence

### Fixture integrity

Standard-library reader проверяет registry/schema/fixture consistency и намеренно выдаёт все assertions как unsupported. Fixture PASS не является Kernel runtime conformance.

### PostgreSQL P4 adapter

P4 adapter выполняет bounded semantic и PostgreSQL checks и выдаёт один `nk-evidence-report/1` result для каждого зарегистрированного assertion.

Команды и границы описаны в [`../tools/conformance/README.md`](../tools/conformance/README.md).

Первоначальное C2 evidence:

```text
head 93710131fffdea7d9a586cc05e7f258c07fae707
run 31175767586 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 — PASS
4 JSON artifacts retained
```

C2 достоверно только вместе с внешне видимым exact run/head/artifact, а не с самостоятельно созданным JSON report.

## Технологическая нейтральность

```text
сначала смысл и инварианты
→ затем abstract contracts
→ после этого replaceable profiles
→ evidence scoped к exact assertions
```

PostgreSQL, SQLite, Python, graphs, vectors, LLMs и hardware — инструменты, а не Canon.

## Текущие отсутствующие области

- independent SQLite profile и C3;
- complete conflict subsystem;
- physical/cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- C4/C5 и production operation;
- историческое восстановление `v0.1.2.1`.

## Для ИИ и ревьюеров

1. проверить exact SHA и относится ли claim к `main` или open PR;
2. проследить conformance claim от assertion ID до result, check IDs и artifact;
3. сохранять `support_state: PARTIAL` и support counts;
4. сохранять границы Issue #1, Issue #18 и ecosystem;
5. обновлять GitHub и Notion continuity records при material changes;
6. не начинать P5/C3 без отдельного operator GO.
