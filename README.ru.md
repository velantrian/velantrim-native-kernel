<div align="center">

# 🧬 Velantrim Native Kernel

### Технологически нейтральные контракты и заменяемые профили для проверяемой памяти

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-P4%20PARTIAL-6f42c1)
![Evidence](https://img.shields.io/badge/evidence-C2%20ASSERTION--SCOPED-blue)
![Profile](https://img.shields.io/badge/profile-PostgreSQL-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Conflict visibility · Deterministic reduction · Auditable evidence**

> **Сохранять смысл при смене технологий. Проверять до повышения статуса.**

</div>

> [!IMPORTANT]
> **Текущее состояние ветки:** `RESEARCH / P4 PARTIAL ASSERTION CONFORMANCE / NOT PRODUCTION-READY`.  
> P1–P3 реализуют ограниченное семантическое и PostgreSQL-ядро. P4 теперь выдаёт полный отчёт по 72 assertions: **41 `SUPPORTED`, 13 `PARTIAL`, 18 `UNSUPPORTED`, 0 `FAILED`**. Repository C2 evidence относится только к 41 поддержанному assertion. P5/C3, физическое удаление, сертификация истины/подлинности и production-гарантии отсутствуют.

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
🧪 Воспроизводимые assertion-scoped доказательства
```

Современные технологии — инструменты лаборатории, а не вечные определения:

```text
PostgreSQL · SQLite · Python · files · graph · vector · LLM · CPU/GPU
                         ≠
                 Architecture Canon
```

## 📊 Точный текущий статус

| Область | Состояние |
|---|---|
| Архитектура и инварианты | **Документированы** |
| Точные identity/event/deletion/fixture контракты | **Приняты** — ADR-0011…0014 |
| Clean PostgreSQL profile | **Принят** — RFC-0002 / ADR-0015 |
| P1 semantic core | **Частичная реализация; repository-tested** |
| P2 PostgreSQL append/idempotency | **Частичная реализация; repository-integration-tested** |
| P3 persisted replay/projections/Receipts | **Частичная реализация; repository-integration-tested** |
| P4 assertion-scoped adapter | **Частичная реализация; C2 reproduced на evidence head** |
| P4 support map | **41 supported / 13 partial / 18 unsupported / 0 failed** |
| P5 independent SQLite profile | **Не реализован / не разрешён** |
| C3 cross-profile equivalence | **Не установлена** |
| Физическое/криптографическое удаление | **Не реализовано** |
| Исторический `v0.1.2.1` и исходные 44 теста | **Не найдены в доступных источниках; Issue #1 открыт** |
| Runtime-интеграция Titan, Mentaury или Crystal | **Не активна** |
| Production readiness | **Не заявляется** |

```text
P4 C2 для 41 SUPPORTED assertions
≠ поддержка всех 72 assertions
≠ C3
≠ storage neutrality
≠ истина или подлинность
≠ физическое удаление
≠ production readiness
```

## 🧩 P1 — семантическое ядро

Пакет: [`native_kernel.semantic_core`](./native_kernel/semantic_core/README.md)

- canonical JSON subset и идентификаторы `nkh1` / `nkc1` / `nkl1`;
- immutable SemanticContent, ClaimIdentity, Command и logical Event;
- explicit deny-by-default authority;
- deterministic version-bound reducer;
- deletion/restriction transition semantics;
- защита Admission/Deletion Receipts от overclaim;
- deterministic upcaster registry и canonical state decoder;
- семантический слой только на Python standard library.

## 🐘 P2 — authoritative PostgreSQL append

Пакет: [`native_kernel.postgresql_profile`](./native_kernel/postgresql_profile/README.md)

```text
explicit authority
→ writer owner/epoch fence
→ scoped durable idempotency
→ rollback-safe sequence allocation
→ atomic Event + idempotency commit
→ canonical payload/envelope commitments
```

Технологии профиля:

- PostgreSQL `16–18`;
- Psycopg `>=3.3,<3.4`;
- Python `>=3.11,<3.13`;
- numbered SQL migrations с SHA-256 ledger;
- один writer lease на Kernel instance.

Это заменяемые технологии профиля, а не Canon.

## 🔁 P3 — replay, projections и operational Receipts

```text
authoritative PostgreSQL Events
→ repeatable-read verified snapshot
→ explicit schema upcasting
→ P1 reduction from empty state
→ bounded Replay Receipt
→ locked head comparison
→ disposable projection rebuild
→ bounded Projection Rebuild Receipt
```

P3 предоставляет:

- полный replay выбранного instance от sequence `1`;
- canonical Event и global hash-chain checks;
- explicit failures для неподдерживаемых schema paths;
- deterministic projection destroy/rebuild;
- monotonic committed generation;
- stale-head rejection;
- atomic Receipt + projection publication;
- проверку связи projection с её rebuild Receipt;
- явные non-claims для истины, внешней подлинности, полной integrity и физического удаления.

## 🧪 P4 — assertion-scoped conformance

P4 связывает исполняемое поведение со всеми 72 registry IDs:

```text
registry + fixtures
→ semantic checks
→ PostgreSQL checks
→ один result для каждого assertion
→ passed check IDs + limitations
→ strict independent validation
→ JSON evidence artifact
```

Текущая карта результатов:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
```

Каждый `SUPPORTED` или `PARTIAL` result ссылается на один или несколько пройденных checks и содержит ограничения. Missing, duplicate, unknown или untraceable результаты отклоняются.

Все `NK-EPI-001…008` остаются `UNSUPPORTED`, потому что их registry decision остаётся `PROPOSED`.

### Граница C1 / C2

- `C1 / LOCALLY_TESTED` — команды и failures выполнены локально;
- `C2 / REPOSITORY_REPRODUCED` — exact implementation/environment воспроизведены в repository CI с artifacts;
- `C3` — требует materially independent второго профиля и comparison evidence.

Отчёт сохраняет:

```text
support_state: PARTIAL
kernel_runtime_conformance: C2
```

Это означает C2 для **41 supported results**, а не полную поддержку профиля.

## ✅ Первоначальное P4 repository evidence

Evidence head:

```text
93710131fffdea7d9a586cc05e7f258c07fae707
```

Workflow:

```text
P4 run 31175767586 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
P1/P2/P3 regressions — PASS
4 JSON evidence artifacts — retained
```

Каждый P4 matrix job сгенерировал и строго проверил C2 report, выполнил P1–P3 regression suites, compileall и загрузил отдельный artifact.

Exact artifact digests и ограничения записаны в [`docs/ai/P4_IMPLEMENTATION_RECORD.md`](./docs/ai/P4_IMPLEMENTATION_RECORD.md).

## 🚫 Явно отсутствует

```text
P5 independent SQLite profile
C3 cross-profile equivalence
полная conflict subsystem
physical/cryptographic deletion execution
restore-before-visibility enforcement
cross-project authority adapter
truth/signature/notarization certification
network API
C4/C5
production security/privacy/backup/HA/compliance guarantees
```

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
| **Reducer** | Детерминированно выводит состояние из объявленной истории/версии |
| **Projection** | Disposable read model, производная от authoritative Events |
| **Receipt** | Evidence одной объявленной операции с явными пределами |
| **Evidence report** | Состояние поддержки и traceability по каждому assertion |

Принятый Event vocabulary остаётся небольшим:

```text
ADMIT · LINK · UTILIZED · SUPERSEDED · ERASED
```

## 🐘 Clean profile lineage

```text
Profile ID:       native-kernel/postgresql-reference
Profile version:  0.4-p4
Evidence lineage: clean/postgresql-reference/0.1
```

```text
P0 — RFC и planning manifest                       COMPLETE
P1 — semantic core                                MERGED
P2 — PostgreSQL append/idempotency                 MERGED
P3 — replay/projections/Receipts                   MERGED
P4 — assertion-scoped conformance                  ACTIVE / PARTIAL / C2 EVIDENCE
P5 — independent SQLite profile / C3 research      BLOCKED / SEPARATE GO
```

Читать:

- [`STATUS.md`](./STATUS.md)
- [`RFC-0002`](./docs/rfc/0002-postgresql-reference-profile-v0.ru.md)
- [`ADR-0018`](./docs/adr/0018-authorize-p4-assertion-scoped-conformance.md)
- [`P4 implementation record`](./docs/ai/P4_IMPLEMENTATION_RECORD.md)
- [`Conformance model`](./docs/CONFORMANCE_MODEL.md)
- [`Profile manifests`](./profiles/postgresql-reference-v0/)

## ⚖️ Граница evidence и истины

```text
recorded history ≠ сама реальность
integrity commitment ≠ подпись
operator approval ≠ empirical evidence
retrieval relevance ≠ truth
C2 reproduction ≠ C3 equivalence
Receipt/report ≠ unlimited proof
```

## 🔗 Граница экосистемы

Native Kernel автоматически не становится memory runtime или authority других проектов Velantrim.

- **Titan** владеет cognition, retrieval, tools и orchestration;
- **Mentaury Soul** владеет digital individuality и continuity;
- **Crystal** владеет verifiable memory, evidence и grant-facing product boundaries;
- **Native Kernel** владеет neutral semantic memory/Event/evidence contracts и bounded profiles.

Интеграция требует отдельных contracts, authority и evidence.

## 🧭 Следующий gate

P5 и любое заявление C3 требуют нового явного operator GO, materially independent SQLite profile и сравнения declared semantic equivalence. P4 не разрешает эту работу.
