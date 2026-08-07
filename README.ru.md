<div align="center">

# 🧬 Velantrim Native Kernel

### Технологически нейтральные контракты, заменяемые профили и ограниченные доказательства проверяемой памяти

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-C4%20PARTIAL-6f42c1)
![Evidence](https://img.shields.io/badge/evidence-OFFLINE%20SHADOW-blue)
![Profiles](https://img.shields.io/badge/profiles-PostgreSQL%20%2B%20SQLite-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Deterministic replay · Cross-profile evidence · Offline shadow evaluation**

> **Сохранять смысл при смене технологий. Повышать статус только после проверки.**

</div>

> [!IMPORTANT]
> **Текущее состояние ветки:** `RESEARCH / C4 PARTIAL OFFLINE SHADOW EVALUATION / NOT PRODUCTION-READY`.  
> PostgreSQL и независимый профиль на standard-library `sqlite3` имеют assertion-scoped repository evidence. C4 добавляет evaluator без authority поверх одного явно утверждённого неизменяемого recorded workload. Это не live shadowing, не candidate promotion, не production authority и не C5.

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
⚖️ Cross-profile equivalence
        ↓
🪞 Offline shadow evaluation без authority
```

Современные технологии — инструменты лаборатории, а не вечные определения:

```text
PostgreSQL · SQLite · Python · JSON · files · graph · vector · LLM · CPU/GPU
                               ≠
                       Architecture Canon
```

## 📊 Точный текущий статус

| Область | Состояние |
|---|---|
| Архитектура и инварианты | **Документированы** |
| Identity/event/deletion/fixture contracts | **Приняты** — ADR-0011…0014 |
| P1 semantic core | **Частичная реализация; repository-tested** |
| P2 PostgreSQL append/idempotency | **Частичная; repository-integration-tested** |
| P3 persisted replay/projections/Receipts | **Частичная; repository-integration-tested** |
| P4 PostgreSQL assertion adapter | **Частичная; C2 repository-reproduced** |
| P5 independent SQLite profile | **Частичная; C2 repository-reproduced** |
| PostgreSQL↔SQLite C3 | **Частичная; repository-reproduced** |
| C4 offline shadow evaluator | **Частичная; repository-reproduced на утверждённом recorded dataset** |
| Single-profile C2 map | **41 supported / 13 partial / 18 unsupported / 0 failed** |
| Cross-profile C3 и C4 scope | **45 supported / 10 partial / 17 unsupported / 0 failed** |
| Live shadowing / candidate promotion | **Не реализованы / не разрешены** |
| Physical/cryptographic deletion | **Не реализовано** |
| Полная conflict subsystem | **Не реализована** |
| C5 / production readiness | **Не разрешены / не установлены** |
| Исторический `v0.1.2.1` | **Не найден в доступных источниках; Issue #1 открыт** |
| Titan/Mentaury/Crystal integration | **Не активна** |

```text
C4 для одного утверждённого 15-case recorded dataset и 45 SUPPORTED assertions
≠ live production shadowing
≠ authority promotion
≠ поддержка всех 72 assertions
≠ exhaustive equivalence
≠ operational equivalence
≠ истина, подлинность или физическое удаление
≠ C5 или production readiness
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
 ↓
C4  approved offline recorded workload / shadow reports / Shadow Receipts
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

SQLite profile владеет собственными migrations, schema, transactions, append, replay, projection и Receipt implementation. Он **не вызывает** PostgreSQL adapters.

Также реализован exact authoritative-history import: PostgreSQL Event bytes и hash commitments переносятся в SQLite и повторно проверяются перед replay.

## ⚖️ P5 cross-profile C3 — prerequisite для C4

Сравнение использует четыре declared equivalence classes:

| Класс | Что сравнивается |
|---|---|
| `BYTE` | canonical identity vectors и exact imported Event bytes/hash chain |
| `STRUCTURAL` | полная форма report и declared fields |
| `SEMANTIC` | reducer state, projection state и Receipt proof fields |
| `BEHAVIOURAL` | accepted/rejected commands, idempotency, fencing и order |

Допустимые различия включают SQL dialect, table layout, server topology, lock mechanisms, independently generated Event IDs/timestamps и operational capabilities.

Недопустимые различия включают canonical identity, payload meaning, declared ordering, hash-chain validity, reducer/projection state, failure outcomes, Receipt proof fields и exact imported bytes/hashes.

Cross-profile evidence повышает ровно:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

Все `NK-EPI-001…008` остаются `UNSUPPORTED / PROPOSED`.

## 🪞 C4 offline shadow evaluation

Пакет: [`native_kernel.shadow_evaluation`](./native_kernel/shadow_evaluation/README.md)

Протоколы:

```text
nk-shadow-workload/1
nk-shadow-report/1
nk-shadow-receipt/1
```

Утверждённый dataset:

```text
dataset_id:      native-kernel/c4-offline-shadow-v1
sha256:          15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:           15
assertion scope: 45 / 45 C3-supported assertions
approval:        ADR-0020 / Issue #61 / OFFLINE_RECORDED_WORKLOAD_ONLY
```

Поток оценки:

```text
утверждённые неизменяемые dataset bytes
+ exact C3 prerequisite report
→ проверка dataset/protocol/digest
→ проверка SHADOW_ONLY authority boundary
→ сравнение declared reference/candidate observations
→ отделение разрешённых operational differences
→ semantic/critical divergence metrics
→ один bounded Shadow Receipt на case
→ полный 72-ID C4 report
```

Обязательная граница authority:

```text
authority promotion:   FORBIDDEN
authoritative writes:  FORBIDDEN
side effects:           FORBIDDEN
promotion decision:    NOT_AUTHORIZED
```

Shadow Receipt доказывает только то, что один recorded case сравнивался при указанном digest, полях и ограничениях. Он не одобряет candidate и не разрешает действие.

## ✅ Первое repository C4 evidence

```text
Evidence head: 97abce685a68e24aec9afab451c009df5783b96b
C4 run:       31187532364 — PASS
P5/C3 run:    31187532391 — PASS
P4 run:       31187532618 — PASS
P1 run:       31187532346 — PASS
Fixtures:     31187532580 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Каждый retained artifact содержит:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
c4-shadow-report.json
```

Один архив был отдельно скачан и проверен:

```text
15 / 15 cases matched
15 Shadow Receipts
45 / 45 C3-supported assertions covered
0 semantic divergences
0 critical divergences
0 missing Receipts
30 declared allowed operational differences
72 assertion results
status: PASS
support_state: PARTIAL
```

Точные artifact digests, история дефектов и границы доказательств записаны в [`docs/ai/C4_IMPLEMENTATION_RECORD.md`](./docs/ai/C4_IMPLEMENTATION_RECORD.md).

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
   ↓
🪞 Non-authoritative shadow observation
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
| **Shadow report** | Сравнение утверждённых recorded observations без authority |
| **Shadow Receipt** | Ограниченное доказательство наблюдения и сравнения одного case |

## 🚫 Явно отсутствует

```text
live production traffic capture или replay
authority promotion / candidate approval / automatic action
exhaustive equivalence proof
PostgreSQL/SQLite operational equivalence
полная conflict subsystem
physical/cryptographic deletion execution
restore-before-visibility enforcement
cross-project authority adapter
truth/signature/notarization certification
network API
C5 security/privacy/incident evidence
production security/backup/HA/compliance guarantees
```

## 🧭 Читать дальше

- [`STATUS.md`](./STATUS.md)
- [`ADR-0020`](./docs/adr/0020-authorize-c4-offline-shadow-evaluation.md)
- [`C4 implementation record`](./docs/ai/C4_IMPLEMENTATION_RECORD.md)
- [`C4 implementation details`](./docs/implementation/c4-offline-shadow-evaluation.md)
- [`C4 manifest`](./profiles/shadow-evaluation-v0/c4-manifest.json)
- [`Approved shadow workload`](./contracts/shadow-workload-v1.json)
- [`Conformance model`](./docs/CONFORMANCE_MODEL.md)
- [`P5 implementation record`](./docs/ai/P5_IMPLEMENTATION_RECORD.md)

## ⚖️ Граница evidence и истины

```text
recorded history ≠ сама реальность
integrity commitment ≠ подпись
operator approval ≠ empirical evidence
retrieval relevance ≠ truth
C2 reproduction ≠ C3 comparison
C3 comparison ≠ C4 offline observation
C4 observation ≠ authority promotion
Receipt/report ≠ unlimited proof
```

## 🔗 Граница экосистемы

Native Kernel автоматически не становится memory runtime или authority других проектов Velantrim.

- **Titan** владеет cognition, retrieval, tools и orchestration;
- **Mentaury Soul** владеет digital individuality и continuity;
- **Crystal** владеет verifiable memory, evidence и audit;
- **Native Kernel** владеет neutral semantic memory/Event/evidence contracts и bounded profiles/evidence protocols.

Интеграция требует отдельных contracts, authority и evidence.

## 🧭 Следующий gate

Текущий publication gate — повторить C4 и все prerequisite checks на одном exact final head PR #62, проверить финальные artifacts, выполнить review и merge, затем воспроизвести evidence на `main` и синхронизировать Notion.

C5, live shadowing, production, deletion execution и ecosystem integration требуют отдельного явного разрешения.
