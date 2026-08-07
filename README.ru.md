<div align="center">

# 🧬 Velantrim Native Kernel

### Технологически нейтральные контракты и заменяемые профили для проверяемой памяти

**[English](./README.md) · [Русский](./README.ru.md)**

![Status](https://img.shields.io/badge/status-P2%20PARTIAL-6f42c1)
![Maturity](https://img.shields.io/badge/maturity-RESEARCH-blue)
![Runtime](https://img.shields.io/badge/runtime-APPEND%20PROFILE-orange)
![Production](https://img.shields.io/badge/production-NOT%20READY-red)

**Claims · Events · Provenance · Time · Conflict visibility · Deterministic reduction · Auditable Receipts**

> **Сохранять смысл при смене технологий. Проверять до повышения статуса.**

</div>

> [!IMPORTANT]
> **Текущее состояние репозитория:** `RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`.  
> Существуют profile-independent P1 semantic core и ограниченный P2 PostgreSQL append/idempotency profile. P2 integration воспроизведён в PostgreSQL 16/18 × Python 3.11/3.12. Replay/projections, operational deletion, assertion-level conformance, C1/C2/C3 и production guarantees отсутствуют.

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
| Replay, projections и operational Receipts | **Не реализованы / P3 не разрешён** |
| Profile conformance adapter | **Не реализован / P4 не разрешён** |
| Profile C1/C2/C3 | **Не установлены** |
| Исторический source `v0.1.2.1` и оригинальные 44 tests | **Не найдены в доступных источниках; Issue #1 открыт** |
| Titan, Mentaury или Crystal integration | **Не активна** |
| Production readiness | **Не заявляется** |

```text
P2 PostgreSQL integration PASS
≠ полный Kernel runtime
≠ replay/projection runtime
≠ assertion-level conformance
≠ C1/C2/C3
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
- standard-library-only implementation.

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

## 🧪 P2 repository evidence

PR #47 evidence head `e80492bcacde2ff2be3a2ee03aa5aa53a714d288`:

```text
P2 workflow run 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
AI context integrity run 31151298002 — PASS
P1 semantic core — PASS
Conformance fixture integrity — PASS
```

Каждый P2 matrix job прошёл:

- 9 P2 unit tests;
- 5 PostgreSQL integration tests;
- 5 P2 manifest tests;
- manifest validation и compileall.

Integration suite проверяет migration idempotency, writer fencing, append/retry/conflict atomicity, rollback-safe sequence reuse и concurrent same-digest append.

## 🚫 Что ещё отсутствует

```text
P3 replay и upcaster execution
projection persistence и rebuild
operational replay/deletion Receipts
physical или cryptographic deletion execution
network API
P4 assertion-scoped conformance adapter
P5 independent SQLite profile
C1 / C2 / C3
production security, privacy, backup, HA или compliance guarantees
```

P3–P5 требуют отдельных решений оператора.

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

Конкретные лабораторные реализации. PostgreSQL принят как preferred full-profile direction; SQLite остаётся optional embedded/portable profile. Ни один из них не является Canon.

### Evidence

Code presence, local tests, repository CI, cross-profile comparison, Shadow evaluation и operational evidence — отдельные уровни продвижения.

## 🐘 Clean PostgreSQL profile lineage

```text
Profile ID:       native-kernel/postgresql-reference
Evidence lineage: clean/postgresql-reference/0.1
Current phase:    P2
```

План реализации:

```text
P0 — accepted RFC и planning manifest              COMPLETE
P1 — profile-independent semantic core             MERGED / REPOSITORY-TESTED
P2 — PostgreSQL append/idempotency adapter          PARTIAL / INTEGRATION-TESTED
P3 — replay, projections, deletion work, Receipts   BLOCKED / SEPARATE GO
P4 — conformance adapter и assertion evidence       BLOCKED / SEPARATE GO
P5 — independent SQLite profile для C3 research     BLOCKED / SEPARATE GO
```

Читайте [`RFC-0002`](./docs/rfc/0002-postgresql-reference-profile-v0.ru.md), [`ADR-0015`](./docs/adr/0015-accept-clean-profile-and-authorize-p1-semantic-core.md), [`ADR-0016`](./docs/adr/0016-authorize-p2-postgresql-append-profile.md) и [`profiles/README.md`](./profiles/README.md).

## 🔒 Граница source recovery

Заявленный внешний checkpoint остаётся таким:

```text
v0.1.2.1
44 deterministic tests заявлены внешне
source и original suite не найдены в доступных источниках
```

Clean profile work не является recovered history:

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

P1:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python tools/profiles/validate_p1_manifest.py
```

P2 unit и manifest checks:

```bash
python -m unittest discover -s tests -p 'test_postgresql_profile_unit.py' -v
python -m unittest discover -s tests -p 'test_p2_manifest.py' -v
python tools/profiles/validate_p2_manifest.py
```

P2 PostgreSQL integration:

```bash
python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_postgresql_profile_integration.py' -v
```

Contract fixture tooling остаётся отдельным:

```bash
python -m unittest discover -s tests -p 'test_conformance_runner.py' -v
python tools/conformance/runner.py validate
```

Отсутствующий run фиксируется как `NOT_RECORDED`, а не PASS.

## 📚 Карта репозитория

| Path | Назначение |
|---|---|
| [`STATUS.md`](./STATUS.md) | authoritative maturity/evidence boundary |
| [`ARCHITECTURE.md`](./ARCHITECTURE.md) | Canon shape и инварианты |
| [`docs/contracts/`](./docs/contracts/) | принятые точные контракты |
| [`contracts/`](./contracts/) | registry, schemas и fixtures |
| [`native_kernel/semantic_core/`](./native_kernel/semantic_core/) | bounded P1 implementation |
| [`native_kernel/postgresql_profile/`](./native_kernel/postgresql_profile/) | bounded P2 PostgreSQL profile |
| [`profiles/`](./profiles/) | planning и implementation manifests |
| [`docs/adr/`](./docs/adr/) | durable decisions |
| [`docs/rfc/`](./docs/rfc/) | bounded research/profile specifications |
| [`docs/ai/`](./docs/ai/) | current state, risks, map и work log |
| [`prototype/`](./prototype/) | source-recovery boundary, не reconstructed runtime |

## 🛣️ Следующие gates

1. слить PR #47 только после same-head P2 и AI-context checks;
2. сохранять runtime support всех assertions как `UNSUPPORTED` до P4;
3. решить Issue #18 о publication/licensing;
4. требовать отдельный operator GO до P3;
5. сохранять независимость Issue #1 и экосистемных проектов;
6. требовать independently developed second profile до C3.

## ⚖️ Лицензия

Репозиторий публичен, но open-source license пока отсутствует. Публичная видимость сама по себе не даёт права копировать, изменять, распространять или развёртывать материалы. Смотрите [Issue #18](https://github.com/velantrian/velantrim-native-kernel/issues/18).

---

**[English](./README.md) · [Русский](./README.ru.md)**
