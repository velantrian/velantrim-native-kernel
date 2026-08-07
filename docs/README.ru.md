# 📚 Документация Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

Эта папка разделяет назначение, архитектуру, контракты, implementation profiles, evidence, research, интеграционные границы и continuity records.

> [!IMPORTANT]
> Текущая зрелость ветки: `RESEARCH / P5 PARTIAL CROSS-PROFILE CONFORMANCE / NOT PRODUCTION-READY`. Acceptance, implementation, C2/C3 evidence и operational readiness остаются разными состояниями.

## С чего начинать

| Документ | Назначение | Текущая граница |
|---|---|---|
| [`../AGENTS.md`](../AGENTS.md) | Обязательные правила репозитория | P5/C3 и non-claims |
| [`../STATUS.md`](../STATUS.md) | Authoritative текущее состояние | C3 45/10/17; support partial |
| [`ai/README.md`](./ai/README.md) | Карта AI/human continuity | active context pack |
| [`ai/P5_IMPLEMENTATION_RECORD.md`](./ai/P5_IMPLEMENTATION_RECORD.md) | SQLite/C3 checks, runs, artifacts и limitations | previous-head C2/C3 evidence |
| [`ai/P4_IMPLEMENTATION_RECORD.md`](./ai/P4_IMPLEMENTATION_RECORD.md) | PostgreSQL C2 foundation | historical prerequisite |
| [`FOUNDATIONAL_INTENT.ru.md`](./FOUNDATIONAL_INTENT.ru.md) · [English](./FOUNDATIONAL_INTENT.md) | Зачем существует Native Kernel | архитектурный замысел |
| [`contracts/NORMATIVE_CONTRACTS_V1.ru.md`](./contracts/NORMATIVE_CONTRACTS_V1.ru.md) · [English](./contracts/NORMATIVE_CONTRACTS_V1.md) | Exact v1 contracts | accepted; profile support partial |
| [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) | Assertion states и C0–C5 | P5 C3 реализован частично |
| [`STORAGE_AND_EXECUTION_PROFILES.ru.md`](./STORAGE_AND_EXECUTION_PROFILES.ru.md) · [English](./STORAGE_AND_EXECUTION_PROFILES.md) | Роли PostgreSQL/SQLite | оба реализованы; operational envelopes различаются |
| [`rfc/0002-postgresql-reference-profile-v0.ru.md`](./rfc/0002-postgresql-reference-profile-v0.ru.md) | Clean profile lifecycle | P1–P5 |
| [`adr/0019-authorize-p5-sqlite-and-c3-equivalence.md`](./adr/0019-authorize-p5-sqlite-and-c3-equivalence.md) | Решение P5/C3 | accepted/approved |
| [`adr/README.md`](./adr/README.md) | Durable decisions | ADR-0019 current |
| [`VELANTRIM_ECOSYSTEM.md`](./VELANTRIM_ECOSYSTEM.md) | Роли проектов | navigation/boundary map |
| [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md) | Cross-project boundaries | runtime inheritance отсутствует |
| [`DECISION_PROCESS.md`](./DECISION_PROCESS.md) | Разделение decision/evidence/approval | governance process |

## Порядок чтения

```text
AGENTS + STATUS
→ AI context pack + P5 implementation record
→ foundational intent/contracts
→ Architecture Canon
→ ADR-0019 + RFC-0002
→ PostgreSQL/SQLite source/tests/manifests/workflows
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
≠ Operational Equivalence
≠ Production Evidence
```

Текущие карты:

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
support_state:     PARTIAL
```

```text
C2 ≠ C3
C3 ≠ все 72 supported
C3 semantic equivalence ≠ operational equivalence
C3 ≠ truth/authenticity/physical deletion/production
```

## Слои executable evidence

### Fixture integrity

Standard-library reader проверяет registry/schema/fixture consistency. Fixture PASS сам по себе не является profile runtime conformance.

### Single-profile C2

PostgreSQL и SQLite adapters выдают полные `nk-evidence-report/1` по всем 72 IDs с guarded map `41/13/18/0`.

### Cross-profile C3

Dedicated comparator выдаёт `nk-equivalence-report/1` после независимого выполнения PostgreSQL/SQLite, normalised outcome comparison и exact authoritative-history import.

Первоначальное P5 evidence:

```text
head d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
run 31181341275 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1 — PASS
4 artifacts × 3 JSON reports
```

C2/C3 достоверно только с externally visible exact run/head/artifact evidence.

## Технологическая нейтральность

```text
сначала смысл и инварианты
→ затем abstract contracts
→ затем независимые replaceable profiles
→ comparison evidence scoped к exact assertions
```

PostgreSQL, SQLite, Python, graphs, vectors, LLMs и hardware — инструменты, а не Canon.

## Текущие отсутствующие области

- exhaustive cross-profile equivalence proof;
- operational equivalence;
- complete conflict subsystem;
- physical/cryptographic deletion execution;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- C4/C5 и production operation;
- историческое восстановление `v0.1.2.1`.

## Для ИИ и ревьюеров

1. проверить exact SHA и относится ли claim к `main` или open PR;
2. проследить C2/C3 claim от assertion ID до result, check IDs и artifact;
3. сохранять `support_state: PARTIAL` и exact counts;
4. сохранять semantic-versus-operational equivalence boundary;
5. сохранять Issue #1, Issue #18 и ecosystem boundaries;
6. обновлять GitHub и Notion continuity records при material changes;
7. не начинать C4/C5/production/deletion/integration без отдельного разрешения.
