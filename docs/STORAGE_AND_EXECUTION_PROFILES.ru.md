# 🐘📦 Профили хранения и выполнения

**[English](./STORAGE_AND_EXECUTION_PROFILES.md) · [Русский](./STORAGE_AND_EXECUTION_PROFILES.ru.md)**

| Измерение | Состояние |
|---|---|
| Решение | `ACCEPTED` |
| PostgreSQL profile | `P1–P4 PARTIAL / C2 REPOSITORY-REPRODUCED` |
| SQLite profile | `P5 PARTIAL / C2 REPOSITORY-REPRODUCED ON EVIDENCE HEAD` |
| Cross-profile comparison | `C3 PARTIAL / REPOSITORY-REPRODUCED ON EVIDENCE HEAD` |
| Архитектурный слой | Implementation Profiles, не Architecture Canon |
| Production | `NOT READY / NOT CLAIMED` |

> [!WARNING]
> Historical P5/C3/C4/C5 evidence использовал SQLite 3.45.1. ADR-0023 теперь требует фактически linked SQLite 3.51.3+ до открытия WAL. Safe-version PR-head и final-main reproduction сохранён additively; historical artifacts остаются неизменными, assertion arithmetic не меняется.

> [!IMPORTANT]
> PostgreSQL и SQLite — заменяемые современные профили. Ни одна база данных не определяет смысл Claim, Event, Relation, Conflict, Projection или Receipt.

## Компактная схема

```text
🏛️ Architecture Canon
        ↓
📐 Storage / Replay / Evidence contracts
        ↓
┌──────────────────────┬──────────────────────┐
│ PostgreSQL reference │ SQLite embedded      │
│ local/server service │ single-file profile  │
│ P1–P4                │ P5                   │
└──────────┬───────────┴──────────┬───────────┘
           └──── C3 comparison ───┘
```

## 🐘 PostgreSQL reference profile

```text
Profile: native-kernel/postgresql-reference@0.4-p4
Role:    полный локальный/server profile
```

Он использует PostgreSQL 16–18, Psycopg, checksum-locked migrations, transactional writer fencing, durable idempotency, rollback-safe ordering, verified replay, projections, bounded Receipts и полный P4 report.

## 📦 SQLite embedded profile

```text
Profile: native-kernel/sqlite-embedded@0.5-p5
Role:    embedded / portable / single-file profile
```

Он использует standard-library `sqlite3`, fail-closed linked SQLite 3.51.3+ WAL gate, exact Stored Event Envelope verification, foreign keys, synchronous FULL, `BEGIN IMMEDIATE`, atomic migrations, собственные schema/append/replay/projection/Receipt code и exact PostgreSQL-history import.

SQLite implementation не вызывает PostgreSQL adapters.

## Offline не означает SQLite

```text
❌ offline = SQLite
❌ online  = PostgreSQL

✅ полный локальный service = local model + Kernel + PostgreSQL localhost
✅ embedded utility         = application + SQLite file
```

Оба профиля могут работать без интернета. Выбор профиля — deployment/operational decision, а не семантическое определение.

## Когда выбирать PostgreSQL

- несколько процессов или агентов;
- network access и roles;
- long-running service;
- большие histories и сложные queries;
- более широкий concurrency envelope;
- зрелые backup/restore/replication tools.

## Когда выбирать SQLite

- один portable file;
- embedded application;
- отсутствие отдельного database service;
- constrained device или local utility;
- fixtures, recovery, diagnostics и demos;
- bounded single-writer envelope.

```text
SQLite ≠ degraded semantics
SQLite = smaller operational profile
```

## Один authoritative profile на Kernel instance

```text
❌ request A → PostgreSQL authority
❌ request B → SQLite authority

✅ один instance → один active authoritative profile
✅ переход профиля → explicit fenced import/migration с evidence
```

Случайная маршрутизация authoritative writes создаёт неоднозначный порядок, дубли/пропуски Claims и невоспроизводимые Receipts.

## Exact history import

P5 реализует bounded перенос PostgreSQL history в SQLite:

```text
PostgreSQL authoritative Events
→ verify canonical bytes/order/hash chain
→ import exact Event IDs/timestamps/payloads/hashes
→ verify SQLite stored history
→ replay from sequence 1
→ compare canonical state
```

Это не online replication, failover или готовый migration product.

## ⚖️ C3 equivalence classes

| Класс | Сравнение |
|---|---|
| `BYTE` | identity vectors и exact imported Event bytes/hash chain |
| `STRUCTURAL` | contract/report fields и relations |
| `SEMANTIC` | reducer/projection state и Receipt boundaries |
| `BEHAVIOURAL` | accepted/rejected commands, idempotency, fencing и order |

Текущая C3 map:

```text
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
support_state: PARTIAL
```

Cross-profile evidence повышает только:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

## Допустимые различия

- SQL dialect и schema/index layout;
- server process против embedded file;
- row locks против `BEGIN IMMEDIATE`;
- independently generated Event IDs/timestamps;
- IAM, networking, replication, failover, concurrency и administration;
- non-semantic metadata и query plans.

## Недопустимые различия

- canonical identity и Command digest;
- semantic payload и declared order;
- hash-chain validity;
- reducer/projection state;
- idempotency, stale-writer и corruption outcomes;
- Receipt proof fields;
- exact Event bytes/hash commitments при history import.

## Evidence

```text
Evidence head: d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
P5/C3 run:    31181341275 — PASS
Matrix:        Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1
Artifacts:     4 archives × 3 JSON reports
```

Это historical evidence на SQLite 3.45.1. Оно не удовлетворяет текущему WAL floor 3.51.3; additive bundle ADR-0023 хранит replacement proof, не переименовывая эти строки.

## Явные границы

```text
C3 semantic/behavioural equivalence
≠ поддержка всех 72 assertions
≠ operational equivalence
≠ exhaustive proof
≠ backup/restore или failover equivalence
≠ truth/authenticity
≠ physical deletion
≠ C4/C5
≠ production readiness
```

Будущий storage substrate может не иметь SQL, таблиц или файлов. Он будет считаться conforming только после реализации accepted contracts и собственного assertion-scoped C2/C3 evidence.
