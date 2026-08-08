# 🧬 Velantrim Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

### Технологически нейтральные контракты семантической памяти, заменяемые профили и ограниченные доказательства

> **Текущее состояние:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

Native Kernel исследует сохранение semantic identity, Event history, deterministic replay и bounded evidence при смене баз данных, языков, моделей и вычислительных субстратов.

Это **не** ядро операционной системы, не замена Linux, не unikernel и не framework драйверов устройств.

```text
Architecture Canon
→ abstract contracts
→ replaceable PostgreSQL / SQLite profiles
→ C2 profile evidence
→ C3 cross-profile comparison
→ C4 offline shadow evaluation
→ C5 bounded synthetic operational rehearsal
```

PostgreSQL, SQLite, Python, JSON, CI, LLM, vectors и hardware — заменяемые инструменты, а не Canon.

## Быстрый старт для человека

Самая быстрая технологически нейтральная проверка требует только Python 3.11 или 3.12:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
```

SQLite profile намеренно fail-closed, если Python связан с SQLite старше 3.51.3. Инструкции по сборке, PostgreSQL setup, допустимым skips и полным локальным командам находятся в [`docs/QUICKSTART.ru.md`](docs/QUICKSTART.ru.md). Термины и ключевые неэквивалентности собраны в [`docs/GLOSSARY.ru.md`](docs/GLOSSARY.ru.md).

## Текущая карта evidence

> **Integrity revalidation:** ADR-0023 merged и repository-reproduced на linked SQLite 3.51.3. Точные P5/C3/C4/C5 checkpoints и восемь оригинальных C5 ZIP сохранены под новой evidence identity. Исторические artifacts SQLite 3.45.1 не изменены; assertions re-adjudicated без promotion и изменения arithmetic.

> **Финализация post-merge review:** четыре follow-up gap, воспроизведённые на `main@d8fe6c9…`, исправлены в [PR #72](https://github.com/velantrian/velantrim-native-kernel/pull/72), exact head `ebb6ac99e2051c01f0fb8e8effc7eaad6d4fe8da`, squash-merge `main@a1cdc6d8f36d67f40f065641809bc6da463c10a4`. JSON type-exact сравнение Event, workflow triggers для SQLite builder, совместимые v1 evidence-schema fields и exact associated-run identities прошли все девять PR workflows и все девять post-merge workflows на `main`. Сохранённые ZIP остаются evidence только своих исходных producing commits и не переобозначаются как доказательство более позднего кода.

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
Offline C4 scope:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
C5 assertion map:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
support_state:     PARTIAL
NK-EPI:            0 / 8 SUPPORTED
```

```text
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
production_authorized: false
```

## Три независимые линии

```text
H — historical recovery
v0.1.2.1 и оригинальные 44 теста
NOT_FOUND_IN_ACCESSIBLE_SOURCES / всё ещё открыто

C — clean implementation
P1–P5 + C4 + C5
ACTIVE / PARTIAL

R — long-horizon research
PROPOSED / BOUNDED / без автоматического promotion
```

Clean implementation не выдаётся за восстановленный `v0.1.2.1`. Исторический поиск не блокирует clean lineage.

## C5 bounded operational rehearsal

```text
plan:       native-kernel/c5-bounded-rehearsal-v1
protocol:   nk-operational-plan/1
sha256:     4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios:  18
deployment: CI_EPHEMERAL_SYNTHETIC
```

Финальный проверенный checkpoint:

```text
head 3d56912260ea41b5b501b65477bff1642dfc2d58
run  31205512911 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1
```

Эта matrix — historical evidence именно тех runs, а не текущий SQLite minimum. См. [ADR-0023](docs/adr/0023-harden-sqlite-wal-and-event-integrity.md).

ADR-0023 safe-runtime checkpoint:

```text
head 675aa4b398a2fc0181dc71d38904a2d33a09f5f8
P5/C3 run 31251526992 — PASS
C4 run     31251526965 — PASS
C5 run     31251526982 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 × linked SQLite 3.51.3
```

```text
18/18 scenarios PASS в каждом matrix job
18 Receipts на job
0 canary leaks
0 recovery failures
0 uncontained incidents
```

Historical и ADR-0023 C5 identities сохраняют шестнадцать точных ZIP-архивов в [`evidence/c5/`](evidence/c5/README.md) с archive- и file-level hashes.

## Точная граница

```text
C5 bounded rehearsal
≠ production readiness
≠ live user traffic
≠ cloud IAM / multi-region HA
≠ compliance certification
≠ physical backup или deletion
≠ operational equivalence
≠ authority promotion
≠ ecosystem wiring
≠ NK-EPI promotion
```

## Читать дальше

- [`docs/QUICKSTART.ru.md`](docs/QUICKSTART.ru.md)
- [`docs/GLOSSARY.ru.md`](docs/GLOSSARY.ru.md)
- [`project-state.json`](project-state.json)
- [`STATUS.md`](STATUS.md)
- [`AGENTS.md`](AGENTS.md)
- [`evidence/c5/README.md`](evidence/c5/README.md)
- [`docs/ai/C5_IMPLEMENTATION_RECORD.md`](docs/ai/C5_IMPLEMENTATION_RECORD.md)
- [`docs/research/POST_C5_RESEARCH_BACKLOG.md`](docs/research/POST_C5_RESEARCH_BACKLOG.md)
- [`docs/CONFORMANCE_MODEL.md`](docs/CONFORMANCE_MODEL.md)
