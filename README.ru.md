<div align="center">

# 🧬 Velantrim Native Kernel

### Технологически нейтральные контракты и заменяемые профили для проверяемой памяти

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-P1%20PARTIAL-6f42c1)
![Maturity](https://img.shields.io/badge/maturity-RESEARCH-blue)
![Runtime](https://img.shields.io/badge/runtime-SEMANTIC%20CORE%20ONLY-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Conflict visibility · Deterministic reduction · Auditable Receipts**

> **Сохранять смысл при смене технологий. Проверять до повышения статуса.**

</div>

> [!IMPORTANT]
> **Текущее состояние репозитория:** `RESEARCH / P1 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`.  
> В `main` теперь существует независимый от хранилища semantic core, но по-прежнему отсутствуют durable Native Kernel history store, PostgreSQL adapter, projection runtime, network service, C1/C2/C3 profile conformance и восстановленная реализация `v0.1.2.1`.

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
| P1 profile-independent semantic core | **Частично реализован; локально проверен** |
| PostgreSQL или SQLite adapter | **Не реализован / не разрешён** |
| Durable append, idempotency и replay | **Не реализованы** |
| Profile C1/C2/C3 | **Не установлены** |
| Исторический source `v0.1.2.1` и оригинальные 44 tests | **Не найдены в доступных источниках; Issue #1 открыт** |
| Titan, Mentaury или Crystal integration | **Не активна** |
| Production readiness | **Не заявляется** |

```text
P1 code существует
≠ полный Kernel runtime
≠ PostgreSQL profile
≠ repository-reproduced C2
≠ доказанная storage neutrality
```

## 🧩 Что реализует P1

Package: [`native_kernel.semantic_core`](./native_kernel/semantic_core/README.md)

- canonical JSON subset и identity helpers `nkh1` / `nkc1` / `nkl1`;
- immutable semantic content, Claim identity, command и logical Event objects;
- explicit deny-by-default authority decisions;
- deterministic version-bound in-memory reduction;
- deletion/restriction transition semantics;
- admission и deletion Receipt overclaim guards;
- Python 3.11+ только со standard library.

Локальное branch evidence P1:

```text
20 semantic-core tests PASS
4 P1-manifest tests PASS
Python compileall PASS
```

Logical reducer не является authoritative event store. Локальный PASS не является GitHub Actions или operational evidence.

## 🚫 Что ещё отсутствует

```text
PostgreSQL / SQLite adapter
SQL schema и migrations
durable event append
persistent idempotency
writer lease persistence
projection persistence и rebuild
network API
profile conformance adapter
C1 / C2 / C3
production security, privacy или deletion guarantees
```

P2–P5 требуют отдельных решений оператора.

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

Конкретные лабораторные реализации. PostgreSQL принят как preferred full profile direction; SQLite остаётся optional embedded/portable profile. Ни один из них не является Canon.

### Evidence

Code presence, local tests, repository CI, cross-profile comparison, Shadow evaluation и operational evidence — отдельные уровни продвижения.

## 🐘 Clean PostgreSQL profile lineage

```text
Profile ID:       native-kernel/postgresql-reference
Evidence lineage: clean/postgresql-reference/0.1
Current phase:    P1
```

План реализации:

```text
P0 — accepted RFC и planning manifest              COMPLETE
P1 — profile-independent semantic core             PARTIAL / LOCALLY_TESTED
P2 — PostgreSQL append/idempotency adapter          BLOCKED / SEPARATE GO
P3 — replay, projections, deletion work, Receipts   BLOCKED
P4 — conformance adapter и repository evidence      BLOCKED
P5 — independent SQLite profile для C3 research     BLOCKED
```

Читайте [`RFC-0002`](./docs/rfc/0002-postgresql-reference-profile-v0.ru.md), [`ADR-0015`](./docs/adr/0015-accept-clean-profile-and-authorize-p1-semantic-core.md) и [`profiles/README.md`](./profiles/README.md).

## 🔒 Граница source recovery

Заявленный внешний checkpoint остаётся таким:

```text
v0.1.2.1
44 deterministic tests заявлены внешне
source и original suite не найдены в доступных источниках
```

Clean P1 work не является recovered history:

```text
clean/postgresql-reference/0.1
≠ v0.1.2.1
≠ original 44-test evidence
≠ заявление, что source глобально утрачен
```

Смотрите [Issue #1](https://github.com/velantrian/velantrim-native-kernel/issues/1).

## 🌐 Границы экосистемы

- **Native Kernel** — semantic memory/event/replay contract research;
- **Titan** — cognition, retrieval, tools и orchestration в своём проекте;
- **Mentaury Soul** — digital individuality и continuity в своём проекте;
- **Crystal** — verifiable memory, evidence и audit в своём проекте.

Cross-links не создают единый runtime, database, identity authority или Canon.

## 🧪 Проверка

Команды P1:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python -m compileall -q native_kernel
python tools/profiles/validate_p1_manifest.py
```

Contract fixture tooling остаётся отдельным:

```bash
python -m unittest discover -s tests -p 'test_conformance_runner.py' -v
python tools/conformance/runner.py validate
```

Отсутствующий GitHub Actions run фиксируется как `NOT_RECORDED`, а не PASS.

## 📚 Карта репозитория

| Path | Назначение |
|---|---|
| [`STATUS.md`](./STATUS.md) | authoritative maturity/evidence boundary |
| [`ARCHITECTURE.md`](./ARCHITECTURE.md) | Canon shape и инварианты |
| [`docs/contracts/`](./docs/contracts/) | принятые точные контракты |
| [`contracts/`](./contracts/) | registry, schemas и fixtures |
| [`native_kernel/semantic_core/`](./native_kernel/semantic_core/) | bounded P1 implementation |
| [`profiles/`](./profiles/) | planning и implementation manifests |
| [`docs/adr/`](./docs/adr/) | durable decisions |
| [`docs/rfc/`](./docs/rfc/) | bounded research/profile specifications |
| [`docs/ai/`](./docs/ai/) | current state, risks, map и work log |
| [`prototype/`](./prototype/) | source-recovery boundary, не reconstructed runtime |

## 🛣️ Следующие gates

1. слить P1 и воспроизвести workflow evidence на exact SHA;
2. сохранять runtime support всех assertions как `UNSUPPORTED` до conformance adapter;
3. решить Issue #18 о publication/licensing;
4. требовать отдельный operator GO до P2 PostgreSQL work;
5. сохранять независимость Issue #1 и экосистемных проектов;
6. требовать independently developed second profile до C3.

## ⚖️ Лицензия

Репозиторий публичен, но open-source license пока отсутствует. Публичная видимость сама по себе не даёт права копировать, изменять, распространять или развёртывать материалы. Смотрите [Issue #18](https://github.com/velantrian/velantrim-native-kernel/issues/18).

---

**[English](./README.md) · [Русский](./README.ru.md)**
