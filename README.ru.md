# 🧬 Velantrim Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

### Технологически нейтральная архитектура семантической памяти, версионированные контракты и ограниченные evidence

> **Текущее состояние:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

Velantrim Native Kernel исследует, как разные реализации и будущие вычислительные субстраты могут сохранять объявленный смысл, identity, provenance, историю, неопределённость и границы доказательства без их незаметного изменения.

Это **не** ядро операционной системы, не готовый продукт базы данных, не LLM memory plugin, не vector store и не определение Python framework.

```text
одинаковый объявленный смысл
        ↓
разные физические механизмы
        ↓
именованная наблюдаемая эквивалентность
```

## Архитектурная граница

```text
Architecture Canon
→ Versioned Abstract Contracts
→ Replaceable Implementation Profiles
→ Fixtures and Tests
→ Evidence
→ Status and Maturity
```

Canon определяет устойчивые семантические требования. Python, JSON, SHA-256, PostgreSQL, SQLite, UTF-8, LLM, vectors, обычное бинарное hardware и CI — заменяемые profiles или инструменты, а не постоянный Canon.

Текущий код Python, PostgreSQL и SQLite является ограниченной reference implementation. Он не является окончательным определением Native Kernel.

## Текущее состояние

```text
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

```text
P1–P5: merged
C4:     merged / partial / offline shadow evidence
C5:     merged / partial / bounded synthetic operational rehearsal
```

C5 не повышает semantic assertions и не разрешает production.

## Модель checkpoint

Машиночитаемая правда записана в [`project-state.json`](project-state.json) по протоколу `nk-project-state/2`.

| Роль | Checkpoint |
|---|---|
| Merge reconciliation машиночитаемой правды | `d9eee591de308a689ace940c2efe58c9e8a137f2` |
| Runtime checkpoint | `675aa4b398a2fc0181dc71d38904a2d33a09f5f8` |
| Runtime integrity checkpoint | `a1cdc6d8f36d67f40f065641809bc6da463c10a4` |
| Evidence-producing checkpoint | `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7` |
| Notion синхронизирован по | `626f34e6328b455258f2dd5fcf2145ec4db64a60` |

Live `main` определяется через GitHub или checked-out Git ref. Committed manifest записывает проверенные checkpoints и ожидаемую связь с HEAD; он не пытается содержать SHA собственного commit.

## Текущая карта evidence

В репозитории сохранены две неизменяемые C5 evidence identities:

```text
evidence/c5/2026-08-07/manifest.json
evidence/c5/2026-08-08-adr0023/manifest.json
```

ADR-0023 устанавливает linked SQLite `3.51.3` как текущий WAL floor. Исторические artifacts SQLite `3.45.1` остаются неизменными и version-bound.

Evidence доказывает только объявленные code, environment, fixtures, workflow runs и ограниченные outputs.

```text
repository-resident evidence
≠ independent custody
≠ complete authenticity
≠ live-data safety
≠ physical deletion
≠ production readiness
```

## Три независимые линии

```text
H — Historical Recovery
  authentic v0.1.2.1 и оригинальные 44 теста
  NOT_FOUND_IN_ACCESSIBLE_SOURCES / OPEN / INDEPENDENT

C — Clean Implementation
  P1–P5 + C4 + C5
  ACTIVE / PARTIAL

R — Long-Horizon Research
  PROPOSED / BOUNDED / NO AUTOMATIC PROMOTION
```

Clean implementation не выдаётся за восстановленный `v0.1.2.1`. Historical recovery не блокирует clean lineage. Research prose не становится Canon или runtime автоматически.

## Текущие gates

```text
human-readable truth reconciliation
→ reconciliation Issues #14–#17 и Notion
→ operator decision по license/publication — Issue #18
→ operator decision по ADR-0024 — Issue #74
→ NK-SAM и именованные equivalence profiles
→ Event/history commitment contract
→ только затем reducer-v2 runtime
```

Пока не разрешены в текущем slice:

- reducer-v2 runtime;
- executable NK-EPI;
- Temporal runtime;
- полный Admission lifecycle;
- operational deletion;
- полная независимая Rust/Go implementation;
- интеграция Titan, Crystal или Mentaury;
- production promotion.

## Быстрый старт для человека

Минимальная проверка semantic core требует Python 3.11 или 3.12:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
```

Проверка machine-state integrity:

```bash
python tools/ai_context/validate_project_state.py --repo .
```

SQLite profile работает fail-closed, если Python связан с SQLite старше `3.51.3`. PostgreSQL setup, допустимые skips и полные команды находятся в [`docs/QUICKSTART.ru.md`](docs/QUICKSTART.ru.md).

## Явные неэквивалентности

```text
Claim ≠ truth
admission ≠ objective truth
Unknown ≠ False
runtime implementation ≠ evidence
evidence ≠ operator authorization
C5 PASS ≠ production readiness
PostgreSQL + SQLite ≠ full substrate neutrality
hash chain ≠ complete authenticity
logical ERASED ≠ physical deletion
public repository ≠ open-source license
```

## Читать дальше

- [`STATUS.md`](STATUS.md) — authoritative human current-state surface
- [`project-state.json`](project-state.json) — authoritative committed machine status
- [`ROADMAP.md`](ROADMAP.md) — active gate sequence
- [`docs/QUICKSTART.ru.md`](docs/QUICKSTART.ru.md) — setup и tests
- [`docs/GLOSSARY.ru.md`](docs/GLOSSARY.ru.md) — terminology и non-equivalences
- [`AGENTS.md`](AGENTS.md) — обязательные инструкции репозитория
- [`docs/ai/CURRENT_STATE.md`](docs/ai/CURRENT_STATE.md) — AI continuity checkpoint
- [`docs/ai/KNOWN_RISKS.md`](docs/ai/KNOWN_RISKS.md) — active и closed risks
- [`evidence/c5/README.md`](evidence/c5/README.md) — сохранённые evidence identities
- [`docs/CONFORMANCE_MODEL.md`](docs/CONFORMANCE_MODEL.md) — conformance levels и proof boundaries
- [`docs/research/POST_C5_RESEARCH_BACKLOG.md`](docs/research/POST_C5_RESEARCH_BACKLOG.md) — только proposed research

Историческая status и review chronology остаётся доступной в Git history и version-bound implementation/evidence records.