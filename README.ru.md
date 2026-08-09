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
| Merge reconciliation человекочитаемой правды | `07549a0cd952b4e06b61ef24d21b2dcdbc9f861d` |
| Repository record Issues и Notion | `cdf559a3a32decd538e4cab3dd7fb591fc6e9322` |
| Operator decision packages / publication checkpoint | `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c` |
| Runtime checkpoint | `675aa4b398a2fc0181dc71d38904a2d33a09f5f8` |
| Runtime integrity checkpoint | `a1cdc6d8f36d67f40f065641809bc6da463c10a4` |
| Evidence-producing checkpoint | `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7` |
| Notion синхронизирован по | `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c` |

Exact head PR #83: `57c14742f705f96e33e929e7e206f14169d42fc0`. Пять exact-head workflows и пять post-merge workflows прошли; на каждом checkpoint было 18 успешных jobs без failed, cancelled или skipped. Review submissions и unresolved review threads отсутствовали; уведомление Codex о quota не являлось review или approval.

Live `main` определяется через GitHub или checked-out Git ref. Committed manifest записывает проверенные checkpoints и ожидаемую связь с HEAD; он не пытается содержать SHA собственного commit.

## Reconciliation правды

```text
machine-readable truth: COMPLETE / PR #80
human-readable truth:   COMPLETE / PR #81
Issues #14–#17:         RECONCILED / OPEN / PR #82 RECORD
Notion dashboard:       SYNCED THROUGH PR #83
```

Исторические отчёты и proposals сохранены, но исключены из authoritative current-state retrieval path.

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
operator decision по license/publication — Issue #18
  PENDING_OPERATOR / selected_option: null
→ operator decision по ADR-0024 — Issue #74
  PROPOSED / PENDING_OPERATOR / selected_option: null
→ NK-SAM и именованные equivalence profiles
→ Event/history commitment contract
→ только затем reducer-v2 runtime
```

До явных решений license не изменена, external contributions остаются не приняты, package publication не разрешена, reducer v1 остаётся immutable, а reducer-v2 runtime не авторизован.

Пока не разрешены:

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
- [`docs/ai/ISSUE_RECONCILIATION.md`](docs/ai/ISSUE_RECONCILIATION.md) — reconciliation foundational issues
- [`docs/ai/NOTION_HANDOFF.md`](docs/ai/NOTION_HANDOFF.md) — текущий Notion sync record
- [`docs/ai/KNOWN_RISKS.md`](docs/ai/KNOWN_RISKS.md) — active и closed risks
- [`evidence/c5/README.md`](evidence/c5/README.md) — сохранённые evidence identities
- [`docs/CONFORMANCE_MODEL.md`](docs/CONFORMANCE_MODEL.md) — conformance levels и proof boundaries
- [`docs/research/POST_C5_RESEARCH_BACKLOG.md`](docs/research/POST_C5_RESEARCH_BACKLOG.md) — только proposed research

Историческая status и review chronology остаётся доступной в Git history и version-bound implementation/evidence records.
