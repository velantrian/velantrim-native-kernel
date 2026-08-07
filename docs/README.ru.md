# 📚 Документация Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

Эта папка разделяет назначение, архитектуру, контракты, implementation profiles, bounded evidence, research, интеграционные границы и continuity records.

> [!IMPORTANT]
> Текущая зрелость ветки: `RESEARCH / C4 PARTIAL OFFLINE SHADOW EVALUATION / NOT PRODUCTION-READY`. Acceptance, implementation, C2/C3/C4 evidence, authority и operational readiness остаются разными состояниями.

## С чего начинать

| Документ | Назначение | Текущая граница |
|---|---|---|
| [`../AGENTS.md`](../AGENTS.md) | Обязательные правила репозитория | C4 offline/no-promotion rules |
| [`../STATUS.md`](../STATUS.md) | Authoritative текущее состояние | C4 45/10/17; support partial |
| [`ai/README.md`](./ai/README.md) | Карта AI/human continuity | active context pack |
| [`ai/C4_IMPLEMENTATION_RECORD.md`](./ai/C4_IMPLEMENTATION_RECORD.md) | Dataset, evaluator, Shadow Receipts, runs, artifacts и limits | exact C4 evidence route |
| [`ai/P5_IMPLEMENTATION_RECORD.md`](./ai/P5_IMPLEMENTATION_RECORD.md) | SQLite/C3 prerequisite evidence | merged prerequisite |
| [`FOUNDATIONAL_INTENT.ru.md`](./FOUNDATIONAL_INTENT.ru.md) · [English](./FOUNDATIONAL_INTENT.md) | Зачем существует Native Kernel | архитектурный замысел |
| [`contracts/NORMATIVE_CONTRACTS_V1.ru.md`](./contracts/NORMATIVE_CONTRACTS_V1.ru.md) · [English](./contracts/NORMATIVE_CONTRACTS_V1.md) | Exact v1 contracts | accepted; profile support partial |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | Assertion states и C0–C5 | C4 реализован частично |
| [`STORAGE_AND_EXECUTION_PROFILES.ru.md`](./STORAGE_AND_EXECUTION_PROFILES.ru.md) · [English](./STORAGE_AND_EXECUTION_PROFILES.md) | Роли PostgreSQL/SQLite | operational envelopes различаются |
| [`adr/0020-authorize-c4-offline-shadow-evaluation.md`](./adr/0020-authorize-c4-offline-shadow-evaluation.md) | Решение C4 | accepted/approved; offline only |
| [`implementation/c4-offline-shadow-evaluation.md`](./implementation/c4-offline-shadow-evaluation.md) | Детали C4 | без authority и side effects |
| [`adr/README.md`](./adr/README.md) | Durable decisions | ADR-0020 current |
| [`VELANTRIM_ECOSYSTEM.md`](./VELANTRIM_ECOSYSTEM.md) | Роли проектов | navigation/boundary map |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | Cross-project boundaries | runtime inheritance отсутствует |

## Порядок чтения

```text
AGENTS + STATUS
→ AI context pack + C4 implementation record
→ foundational intent/contracts
→ Architecture Canon + conformance model
→ ADR-0020 + approved dataset
→ evaluator/validators/tests/workflow
→ exact run/jobs/artifacts
```

## Главное различие

```text
Architecture Canon
≠ Abstract Contract
≠ Accepted Decision
≠ Implementation Profile
≠ Evidence Layer
≠ Assertion Result
≠ Authority Promotion
≠ Production Evidence
```

Текущие карты:

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
Offline C4 scope:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
support_state:     PARTIAL
```

```text
C2 ≠ C3 ≠ C4
C4 offline shadow ≠ live shadowing
C4 observation ≠ authority promotion
C4 ≠ все 72 supported
C4 ≠ operational equivalence / truth / deletion / C5 / production
```

## Слои executable evidence

### Fixture integrity

Standard-library reader проверяет registry/schema/fixture consistency. Fixture PASS сам по себе не является profile runtime conformance.

### Single-profile C2

PostgreSQL и SQLite adapters выдают полные `nk-evidence-report/1` по всем 72 IDs с guarded map `41/13/18/0`.

### Cross-profile C3

Dedicated comparator выдаёт `nk-equivalence-report/1` после независимого выполнения PostgreSQL/SQLite, normalized outcome comparison и exact authoritative-history import.

### Offline C4

Evaluator без authority принимает exact validated C3 report и утверждённый immutable dataset `nk-shadow-workload/1`. Он выдаёт `nk-shadow-report/1` и один bounded `nk-shadow-receipt/1` на каждый case.

```text
dataset: native-kernel/c4-offline-shadow-v1
sha256:  15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:   15
scope:   45 / 45 C3-supported assertions
```

Первое C4 repository evidence:

```text
head 97abce685a68e24aec9afab451c009df5783b96b
run 31187532364 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1 — PASS
4 artifacts × 4 JSON reports
15/15 matched cases · 15 Receipts · 0 semantic/critical divergences
```

C2/C3/C4 достоверно только с externally visible exact run/head/artifact evidence.

## Технологическая нейтральность

```text
сначала смысл и инварианты
→ затем abstract contracts
→ затем независимые replaceable profiles
→ bounded evidence layers поверх declared observations
```

PostgreSQL, SQLite, Python, JSON, graphs, vectors, LLMs и hardware — инструменты, а не Canon.

## Текущие отсутствующие области

- live traffic capture или live production shadowing;
- authority promotion или candidate approval;
- exhaustive cross-profile/state-space equivalence;
- operational equivalence;
- complete conflict subsystem;
- physical/cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- C5 и production operation;
- историческое восстановление `v0.1.2.1`.

## Для ИИ и ревьюеров

1. проверить exact SHA и относится ли claim к `main` или open PR;
2. проследить C4 от ADR/dataset ID/digest до C3 prerequisite, case results, Receipts и retained artifact;
3. сохранять `support_state: PARTIAL` и exact counts;
4. сохранять offline-versus-live и observation-versus-authority boundaries;
5. сохранять Issue #1, Issue #18 и ecosystem boundaries;
6. обновлять GitHub и Notion continuity records при material changes;
7. не начинать C5/live/production/deletion/integration без отдельного разрешения.
