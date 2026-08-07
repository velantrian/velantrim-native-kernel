<div align="center">

# 🧬 Velantrim Native Kernel

### Технологически нейтральные контракты и заменяемые профили для проверяемой памяти

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-P3%20PARTIAL-6f42c1)
![Maturity](https://img.shields.io/badge/maturity-RESEARCH-blue)
![Runtime](https://img.shields.io/badge/runtime-REPLAY%20PROFILE-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Conflict visibility · Deterministic reduction · Auditable Receipts**

> **Сохранять смысл при смене технологий. Проверять до повышения статуса.**

</div>

> [!IMPORTANT]
> **Текущее состояние репозитория:** `RESEARCH / P3 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`.  
> Реализованы P1 semantic reduction, P2 PostgreSQL append/idempotency и ограниченный P3 persisted replay/projection rebuild/operational Receipts. P3 integration воспроизведён в PostgreSQL 16/18 × Python 3.11/3.12. Physical deletion, P4 assertion-level conformance, P5 independent-profile portability, C1/C2/C3 и production guarantees отсутствуют.

## ⚡ За 30 секунд

Velantrim Native Kernel — независимый личный долгосрочный архитектурный и implementation research project.

Он исследует, как память, записанные изменения и epistemic state могут сохранять смысл при замене баз данных, языков программирования, поставщиков моделей, процессоров и будущих вычислительных субстратов.

```text
🏛️ Architecture Canon
        ↓
📐 Принятые abstract contracts
        ↓
🔌 Заменяемые implementation profiles
        ↓
🧪 Воспроизводимое evidence
```

Современные технологии — лабораторные инструменты, а не вечные определения:

```text
PostgreSQL · SQLite · Python · files · graph · vector · LLM · CPU/GPU
                         ≠
                 Architecture Canon
```

## 📊 Точный текущий статус

| Область | Состояние |
|---|---|
| Архитектура и инварианты | **Документированы** |
| Foundational contract families | **Приняты** — ADR-0010 |
| Точные identity/event/deletion/fixture contracts | **Приняты** — ADR-0011…0014 |
| Clean PostgreSQL profile plan | **Принят** — RFC-0002 / ADR-0015 |
| P1 profile-independent semantic core | **Частично реализован; repository-tested** |
| P2 PostgreSQL append/idempotency | **Частично реализован; repository-integration-tested** |
| P3 persisted replay/projection rebuild/Receipts | **Частично реализован; repository-integration-tested** |
| Physical/cryptographic deletion execution | **Не реализован** |
| P4 profile conformance adapter | **Не реализован / не разрешён** |
| P5 independent SQLite profile | **Не реализован / не разрешён** |
| Profile C1/C2/C3 | **Не установлены** |
| Исторический source `v0.1.2.1` и оригинальные 44 tests | **Не найдены в доступных источниках; Issue #1 открыт** |
| Titan, Mentaury или Crystal integration | **Не активна** |
| Production readiness | **Не заявляется** |

```text
P3 replay/projection integration PASS
≠ полный Kernel runtime
≠ physical deletion
≠ assertion-level conformance
≠ C1/C2/C3
≠ доказанная storage neutrality
≠ production readiness
```

## 🧩 Что реализует P1

Package: [`native_kernel.semantic_core`](./native_kernel/semantic_core/README.md)

- canonical JSON subset и identity helpers `nkh1` / `nkc1` / `nkl1`;
- immutable semantic content, Claim identity, Command и logical Event objects;
- explicit deny-by-default authority decisions;
- deterministic version-bound reduction;
- deletion/restriction transition semantics;
- admission/deletion Receipt overclaim guards;
- standard-library deterministic upcaster registry и canonical state decoder;
- Python standard-library-only semantic layer.

## 🐘 Что реализует P2

Package: [`native_kernel.postgresql_profile`](./native_kernel/postgresql_profile/README.md)

```text
explicit authority
→ DB-backed writer owner/epoch fence
→ durable scoped idempotency
→ rollback-safe global/stream counters
→ atomic Event + idempotency commit
→ canonical payload/envelope bytes
→ nkp1 / nke1 integrity chain
```

Профильные решения:

- PostgreSQL `16–18`;
- Psycopg `>=3.3,<3.4`, lazy import;
- Python `>=3.11,<3.13`;
- numbered SQL migrations с SHA-256 ledger;
- один authoritative writer lease на Kernel instance.

Это заменяемые технологии профиля, а не Canon.

## 🔁 Что реализует P3

```text
authoritative PostgreSQL Events
→ repeatable-read snapshot
→ canonical payload/envelope checks
→ Event count, global/stream sequence и hash-chain checks
→ explicit upcaster path
→ P1 reducer from empty state
→ bounded Replay Receipt
→ locked authoritative-head comparison
→ disposable projection rebuild
→ bounded Projection Rebuild Receipt
```

P3 добавляет:

- replay полной истории выбранного instance от sequence `1`;
- explicit identity/multi-step schema upcaster routing;
- failure при missing, ambiguous, cyclic или invalid upcaster paths;
- deterministic state digest reconstruction;
- disposable `semantic-state` projection persistence;
- projection destroy и deterministic rebuild;
- monotonic projection generation через committed rebuild Receipts;
- stale-head rejection до публикации projection;
- transactional rollback при ошибке Receipt/projection publication;
- canonical persisted Replay и Projection Rebuild Receipts;
- жёсткие non-claims для truth, external authenticity, complete integrity, physical erasure и C-levels.

Hash chain и replay checks — ограниченное integrity evidence. Это не signatures, consensus, external notarization или защита от любого privileged database rewrite.

## 🧪 Repository evidence

### Финальное P2 evidence

```text
PR #47 final head: 36ddb1d0342914f0c06fe7f31171bac06565ee72
P2 run 31152380799 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
```

### Начальное executable-head evidence P3

```text
PR #50 executable head: 0f8fd4ffe5d5fb0d4bc01f3e441a053f691dbba3
P3 run 31171581859 — PASS
P2 regression run 31171581795 — PASS
P1 semantic core run 31171581787 — PASS
Fixture integrity run 31171581791 — PASS
```

P3 прошёл PostgreSQL `16/18 × Python 3.11/3.12`. Каждый P3 job выполнил:

- 5 semantic unit tests;
- 5 P3 manifest tests и validator;
- 7 PostgreSQL replay/projection/Receipt integration scenarios;
- P2 unit/integration regression suite;
- compileall.

Final PR head должен повторить затронутые проверки после documentation/evidence изменений. Ранний PASS остаётся evidence только для своего exact SHA.

## 🚫 Что ещё отсутствует

```text
physical или cryptographic deletion execution
backup/export/provider/key erasure evidence
network API
P4 assertion-scoped conformance adapter
P5 independent SQLite profile
C1 / C2 / C3
production credentials, security, privacy, backup, HA или compliance guarantees
```

P4–P5 требуют отдельных решений оператора.

## 🧬 Canon shape

```text
🧩 Claim
   ↓
📜 Append-only Event History
   ↓
🧠 Deterministic State Reconstruction
   ↓
🗂️ Rebuildable Projections
   ↓
🎯 Task-Specific Context Selection
   ↓
🧾 Auditable Receipt
```

| Компонент | Значение |
|---|---|
| **Claim** | Устойчивая semantic identity; существование не устанавливает truth |
| **Event** | Явная запись принятого command-driven изменения |
| **Reducer** | Детерминированно выводит state из объявленной history/version |
| **Projection** | Disposable read model, который должен восстанавливаться |
| **Receipt** | Объявляет evidence обработки, omissions и proof limits |

Принятая Event vocabulary остаётся небольшой:

```text
ADMIT · LINK · UTILIZED · SUPERSEDED · ERASED
```

## 🏗️ Архитектурные слои

### Architecture Canon

Смысл, который должен пережить замену технологий: identity roles, provenance, time, conflict visibility, authority boundaries и Receipt semantics.

### Abstract contracts

Versioned behavioural obligations: `nk-id/1.0`, `nk-event/1.0`, `nk-deletion/1.0`, `nk-fixtures/1.0`.

### Implementation profiles

Конкретные лабораторные реализации. PostgreSQL принят как preferred full-profile direction; SQLite остаётся optional independent embedded/portable profile. Ни один из них не является Canon.

### Evidence

Code presence, local tests, repository CI, assertion-scoped conformance, cross-profile comparison, Shadow evaluation и operational evidence — отдельные уровни продвижения.

## 🐘 Clean PostgreSQL profile lineage

```text
Profile ID:       native-kernel/postgresql-reference
Evidence lineage: clean/postgresql-reference/0.1
Current phase:    P3
```

План реализации:

```text
P0 — accepted RFC и planning manifest              COMPLETE
P1 — profile-independent semantic core             MERGED / REPOSITORY-TESTED
P2 — PostgreSQL append/idempotency adapter          PARTIAL / INTEGRATION-TESTED
P3 — replay, projection rebuild и Receipts          PARTIAL / INTEGRATION-TESTED
P4 — conformance adapter и assertion evidence       BLOCKED / SEPARATE GO
P5 — independent SQLite profile для C3 research     BLOCKED / SEPARATE GO
```

Читайте [`RFC-0002`](./docs/rfc/0002-postgresql-reference-profile-v0.ru.md), [`ADR-0015`](./docs/adr/0015-accept-clean-profile-and-authorize-p1-semantic-core.md), [`ADR-0016`](./docs/adr/0016-authorize-p2-postgresql-append-profile.md), [`ADR-0017`](./docs/adr/0017-authorize-p3-replay-projection-receipts.md) и [`profiles/README.md`](./profiles/README.md).

## 🔒 Граница source recovery

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
≠ заявление, что source глобально утрачен
```

Issue #1 остаётся активным и независимым.

## 🌐 Границы экосистемы

- **Native Kernel** — semantic memory, Event, replay и evidence-profile research;
- **Titan** — cognition, retrieval, tools и orchestration в своём проекте;
- **Mentaury Soul** — digital individuality и continuity в своём проекте;
- **Crystal** — verifiable memory, evidence и audit в своём проекте.

Cross-links не создают единый runtime, database, identity authority или Canon.

## 🧪 Проверка

```bash
python -m unittest discover -s tests -p 'test_p3_semantic.py' -v
python -m unittest discover -s tests -p 'test_p3_manifest.py' -v
python tools/profiles/validate_p3_manifest.py

python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_p3_postgresql_integration.py' -v
```

P2 и contract fixture tooling остаются отдельными regression/evidence surfaces. Отсутствующий run фиксируется как `NOT_RECORDED`, а не PASS.

## 📚 Карта репозитория

| Path | Назначение |
|---|---|
| [`STATUS.md`](./STATUS.md) | authoritative maturity/evidence boundary |
| [`ARCHITECTURE.md`](./ARCHITECTURE.md) | Canon shape и инварианты |
| [`docs/contracts/`](./docs/contracts/) | принятые точные контракты |
| [`contracts/`](./contracts/) | registry, schemas и fixtures |
| [`native_kernel/semantic_core/`](./native_kernel/semantic_core/) | P1 semantics + P3 standard-library schema helpers |
| [`native_kernel/postgresql_profile/`](./native_kernel/postgresql_profile/) | bounded P2/P3 PostgreSQL profile |
| [`profiles/`](./profiles/) | P0/P1/P2/P3 manifests |
| [`docs/adr/`](./docs/adr/) | durable decisions |
| [`docs/rfc/`](./docs/rfc/) | bounded research/profile specifications |
| [`docs/ai/`](./docs/ai/) | current state, risks, map и work log |
| [`prototype/`](./prototype/) | source-recovery boundary, не reconstructed runtime |

## 🛣️ Следующие gates

1. пройти same-final-head P3, P2, P1, fixture и AI-context checks;
2. сохранять assertion-level runtime support `UNSUPPORTED` до P4;
3. требовать отдельный operator GO до P4;
4. решить Issue #18 о publication/licensing;
5. сохранять независимость Issue #1 и ecosystem projects;
6. требовать materially independent second profile до C3.

## ⚖️ Лицензия

Репозиторий публичен, но open-source license пока отсутствует. Публичная видимость сама по себе не даёт права копировать, изменять, распространять или развёртывать материалы. Смотрите Issue #18.

---

**[English](./README.md) · [Русский](./README.ru.md)**
