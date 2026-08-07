<div align="center">

# 🧬 Velantrim Native Kernel

### Технологически нейтральные контракты и заменяемые профили проверяемой памяти

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-P5%20PARTIAL-6f42c1)
![Evidence](https://img.shields.io/badge/evidence-C3%20ASSERTION--SCOPED-blue)
![Profiles](https://img.shields.io/badge/profiles-PostgreSQL%20%2B%20SQLite-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Deterministic replay · Cross-profile evidence**

> **Сохранять смысл при смене технологий. Повышать статус только после проверки.**

</div>

> [!IMPORTANT]
> **Текущее состояние ветки:** `RESEARCH / P5 PARTIAL CROSS-PROFILE CONFORMANCE / NOT PRODUCTION-READY`.  
> PostgreSQL и независимый профиль на standard-library `sqlite3` имеют repository C2 evidence. Их cross-profile comparison содержит **45 `SUPPORTED`, 10 `PARTIAL`, 17 `UNSUPPORTED`, 0 `FAILED`**. C3 относится только к этим 45 поддержанным результатам и не означает полную поддержку или operational equivalence.

## ⚡ За 30 секунд

Velantrim Native Kernel — независимый долгосрочный архитектурный и исследовательский проект.

Он изучает, как сохранять смысл памяти, записанных изменений и доказательств при смене баз данных, языков, моделей, процессоров и будущих вычислительных субстратов.

```text
🏛️ Architecture Canon
        ↓
📐 Принятые абстрактные контракты
        ↓
🔌 Заменяемые Implementation Profiles
        ↓
🧪 Assertion-scoped воспроизводимые доказательства
        ↓
⚖️ Явная cross-profile equivalence
```

Современные технологии — инструменты лаборатории, а не вечные определения:

```text
PostgreSQL · SQLite · Python · files · graph · vector · LLM · CPU/GPU
                         ≠
                 Architecture Canon
```

## 📊 Точный статус

| Область | Состояние |
|---|---|
| Архитектура и инварианты | **Документированы** |
| Identity/event/deletion/fixture contracts | **Приняты** — ADR-0011…0014 |
| P1 semantic core | **Частичная реализация; repository-tested** |
| P2 PostgreSQL append/idempotency | **Частичная; repository-integration-tested** |
| P3 persisted replay/projections/Receipts | **Частичная; repository-integration-tested** |
| P4 PostgreSQL assertion adapter | **Частичная; C2 repository-reproduced** |
| P5 independent SQLite profile | **Частичная; C2 repository-reproduced на evidence head** |
| PostgreSQL/SQLite C3 | **Частичная; repository-reproduced на evidence head** |
| Single-profile map | **41 supported / 13 partial / 18 unsupported / 0 failed** |
| Cross-profile C3 map | **45 supported / 10 partial / 17 unsupported / 0 failed** |
| Physical/cryptographic deletion | **Не реализовано** |
| Полная conflict subsystem | **Не реализована** |
| C4/C5 / production readiness | **Не установлены / не заявляются** |
| Исторический `v0.1.2.1` | **Не найден в доступных источниках; Issue #1 открыт** |
| Titan/Mentaury/Crystal integration | **Не активна** |

```text
C3 для 45 SUPPORTED assertions
≠ поддержка всех 72
≠ operational equivalence PostgreSQL и SQLite
≠ истина или подлинность
≠ физическое удаление
≠ production readiness
```

## 🧩 Маршрут реализации

```text
P1  canonical identity / semantic objects / authority / reducer
 ↓
P2  PostgreSQL append / idempotency / writer fencing
 ↓
P3  persisted replay / projection rebuild / bounded Receipts
 ↓
P4  полный PostgreSQL 72-ID report / C2
 ↓
P5  независимый SQLite profile / полный SQLite report
 ↓
C3  PostgreSQL ↔ SQLite equivalence comparison
```

## 🐘 PostgreSQL reference profile

Пакет: [`native_kernel.postgresql_profile`](./native_kernel/postgresql_profile/README.md)

- PostgreSQL `16–18`;
- Psycopg `>=3.3,<3.4`;
- checksum-locked migrations;
- owner/epoch/expiry writer fencing;
- durable idempotency и rollback-safe ordering;
- canonical Event commitments и hash chain;
- replay, disposable projections и bounded Receipts;
- полный assertion-scoped P4 report.

## 🗃️ SQLite embedded profile

Пакет: [`native_kernel.sqlite_profile`](./native_kernel/sqlite_profile/README.md)

```text
stdlib sqlite3
→ WAL + foreign keys + synchronous FULL
→ BEGIN IMMEDIATE single-writer transaction
→ owner / epoch / expiry fence
→ append / retry / rollback-safe ordering
→ Event hash chain
→ replay / projections / Receipts
```

SQLite profile использует собственные migrations, schema, transactions, append, replay, projection и Receipt implementation. Он **не вызывает** PostgreSQL adapters.

Также реализован exact authoritative-history import: PostgreSQL Event bytes и hash commitments переносятся в SQLite и повторно проверяются перед replay.

## ⚖️ P5 cross-profile C3

Сравнение использует четыре declared equivalence classes:

| Класс | Что сравнивается |
|---|---|
| `BYTE` | canonical identity vectors и exact imported Event bytes/hash chain |
| `STRUCTURAL` | полная форма report и declared fields |
| `SEMANTIC` | reducer state, projection state и Receipt proof fields |
| `BEHAVIOURAL` | accepted/rejected commands, idempotency, fencing и order |

Допустимые различия:

- SQL dialect и table/index layout;
- server topology против одного локального файла;
- PostgreSQL row locks против SQLite `BEGIN IMMEDIATE`;
- независимо созданные Event IDs/timestamps;
- IAM, networking, replication, failover, concurrency и administration.

Недопустимые различия:

- canonical identity и Command digest;
- payload meaning и declared ordering;
- hash-chain validity;
- reducer/projection canonical state;
- idempotency, stale-writer и corruption outcomes;
- bounded Receipt proof fields;
- bytes/hashes при exact authoritative-history import.

Cross-profile evidence повышает ровно четыре assertions:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

Все `NK-EPI-001…008` остаются `UNSUPPORTED / PROPOSED`.

## ✅ Первоначальное P5 repository evidence

```text
Evidence head: d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
P5/C3 run:    31181341275 — PASS
P4 run:       31181341370 — PASS
P1 run:       31181341405 — PASS
Fixtures:     31181340889 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

В каждой среде сохраняется один artifact с тремя файлами:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
```

Один архив был отдельно скачан и проверен. В нём присутствовали все три report, exact SHA/run/version metadata, все 72 results и восемь пройденных cross-profile checks.

Точные digests и история найденных дефектов записаны в [`docs/ai/P5_IMPLEMENTATION_RECORD.md`](./docs/ai/P5_IMPLEMENTATION_RECORD.md).

## 🧬 Форма Canon

```text
🧩 Claim
   ↓
📜 Append-only Event history
   ↓
🧠 Deterministic state reconstruction
   ↓
🗂️ Rebuildable projections
   ↓
🧾 Bounded Receipts and evidence reports
```

| Компонент | Значение |
|---|---|
| **Claim** | Стабильная семантическая идентичность; существование не доказывает истину |
| **Event** | Явная запись authority-admitted изменения |
| **Reducer** | Детерминированно выводит state из объявленной history/version |
| **Projection** | Disposable read model, производная от authoritative Events |
| **Receipt** | Evidence одной операции с явными пределами |
| **Evidence report** | Поддержка профиля и traceability по каждому assertion |
| **Equivalence report** | Сравнение declared profiles по каждому assertion |

## 🚫 Явно отсутствует

```text
exhaustive equivalence proof
PostgreSQL/SQLite operational equivalence
полная conflict subsystem
physical/cryptographic deletion execution
restore-before-visibility enforcement
cross-project authority adapter
truth/signature/notarization certification
network API
C4/C5
production security/privacy/backup/HA/compliance guarantees
```

## 🧭 Читать дальше

- [`STATUS.md`](./STATUS.md)
- [`ADR-0019`](./docs/adr/0019-authorize-p5-sqlite-and-c3-equivalence.md)
- [`P5 implementation record`](./docs/ai/P5_IMPLEMENTATION_RECORD.md)
- [`Conformance model`](./docs/CONFORMANCE_MODEL.md)
- [`Storage and execution profiles`](./docs/STORAGE_AND_EXECUTION_PROFILES.md)
- [`P5 manifest`](./profiles/sqlite-embedded-v0/p5-manifest.json)

## ⚖️ Граница evidence и истины

```text
recorded history ≠ сама реальность
integrity commitment ≠ подпись
operator approval ≠ empirical evidence
retrieval relevance ≠ truth
C2 reproduction ≠ C3 comparison
C3 comparison ≠ operational equivalence
Receipt/report ≠ unlimited proof
```

## 🔗 Граница экосистемы

Native Kernel автоматически не становится memory runtime или authority других проектов Velantrim.

- **Titan** владеет cognition, retrieval, tools и orchestration;
- **Mentaury Soul** владеет digital individuality и continuity;
- **Crystal** владеет verifiable memory, evidence и audit;
- **Native Kernel** владеет neutral semantic memory/Event/evidence contracts и bounded profiles.

Интеграция требует отдельных contracts, authority и evidence.

## 🧭 Следующий gate

Текущая задача — завершить documentation synchronization, повторить P5/C3 на одном final exact PR head, проверить финальные artifacts и слить PR #59. Любая работа C4, C5, production, deletion execution или ecosystem integration требует отдельного явного разрешения.
