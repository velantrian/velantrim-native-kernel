# 🧬 Velantrim Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

### Технологически нейтральная архитектура долговечного знания, памяти, изменений и объяснения

> **Текущее состояние:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Активная фаза:** `ARCHITECTURE RE-FOUNDATION / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`

Velantrim Native Kernel исследует, какой смысл, identity, provenance, time, uncertainty, conflict, revision и explanation должны сохраняться при смене баз данных, языков, моделей, процессоров и носителей информации.

Это **не** ядро операционной системы, не database product, не LLM memory plugin, не vector store и не определение Python framework.

```text
сначала определить смысл и инварианты
        ↓
определить абстрактную машину Kernel
        ↓
определить версионированные контракты
        ↓
сопоставить заменяемые implementation profiles
        ↓
проверять и опровергать их
```

## Архитектурная граница

```text
Architecture Purpose and Ontology
→ Abstract Native Kernel Machine
→ Semantic Laws and Invariants
→ Versioned Abstract Contracts
→ Replaceable Implementation Profiles
→ Fixtures and Tests
→ Evidence
→ Status and Maturity
```

Python, JSON, SHA-256, PostgreSQL, SQLite, graphs, vectors, LLM, обычное hardware и CI являются заменяемыми research instruments. Они не являются постоянным Canon.

Текущая Python/PostgreSQL/SQLite lineage — **bounded reference laboratory**, а не окончательное определение Native Kernel.

## Текущее состояние

```text
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

C5 не повышает semantic assertions и не разрешает production.

## Модель checkpoint

Машиночитаемая правда записана в [`project-state.json`](project-state.json) по протоколу `nk-project-state/2`.

| Роль | Checkpoint |
|---|---|
| Reconciliation machine truth | `d9eee591de308a689ace940c2efe58c9e8a137f2` |
| Reconciliation human truth | `07549a0cd952b4e06b61ef24d21b2dcdbc9f861d` |
| Record Issues и Notion | `cdf559a3a32decd538e4cab3dd7fb591fc6e9322` |
| Publication checkpoint | `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c` |
| Runtime checkpoint | `675aa4b398a2fc0181dc71d38904a2d33a09f5f8` |
| Runtime integrity checkpoint | `a1cdc6d8f36d67f40f065641809bc6da463c10a4` |
| Evidence-producing checkpoint | `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7` |
| Источник manifest / Notion synchronized descendant | `70acd0da61fee19131947aa56125833adb156ced` |

Publication checkpoint остаётся identity decision packages из PR #83. Более поздний Notion checkpoint PR #86 не переписывает и не заменяет его. Live `main` определяется через GitHub или checked-out Git ref; committed state не предсказывает SHA собственного будущего merge.

## Reconciliation правды

```text
machine-readable truth: COMPLETE / PR #80
human-readable truth:   COMPLETE / PR #81
Issues #14–#17:         RECONCILED / OPEN / PR #82
publication checkpoint: PR #83
Notion dashboard:       SYNCED AND READ BACK THROUGH PR #86
checkpoint role repair: COMPLETE / PR #87
```

Исторические отчёты и proposals сохраняются, но не переопределяют current state.

## Текущая карта evidence

В репозитории сохранены две неизменяемые C5 evidence identities:

```text
evidence/c5/2026-08-07/manifest.json
evidence/c5/2026-08-08-adr0023/manifest.json
```

ADR-0023 устанавливает linked SQLite `3.51.3` как текущий WAL floor. Исторические SQLite `3.45.1` artifacts остаются неизменными и version-bound.

```text
repository-resident evidence
≠ independent custody
≠ complete authenticity
≠ live-data safety
≠ physical deletion
≠ production readiness
```

ADR-0025 не расширяет границы существующего evidence.

## Три независимые линии

```text
H — Historical Recovery
  authentic v0.1.2.1 и оригинальные 44 теста
  NOT_FOUND_IN_ACCESSIBLE_SOURCES / OPEN / INDEPENDENT

C — Clean Reference Implementation
  P1–P5 + C4 + C5
  PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY

R — Architecture Re-foundation
  blueprint A1–A10
  ACTIVE / BLUEPRINT-FIRST / NO AUTOMATIC RUNTIME PROMOTION
```

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
```

## Активная архитектурная фаза

ADR-0025 фиксирует operator-approved направление: завершить архитектурный чертёж до дальнейшего semantic/runtime expansion.

```text
A1 Purpose и Non-goals
→ A2 Knowledge and Memory Ontology
→ A3 Abstract Native Kernel Machine
→ A4 Semantic Laws and Invariants
→ A5 Identity / Time / Change
→ A6 Knowledge Lifecycle
→ A7 Conflict / Uncertainty / Revision
→ A8 Substrate-independence Contract
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ отдельное operator decision до возобновления runtime expansion
```

План: [English](docs/ARCHITECTURE_REFOUNDATION.md) · [Русский](docs/ARCHITECTURE_REFOUNDATION.ru.md).  
Решение: [`ADR-0025`](docs/adr/0025-blueprint-before-runtime-expansion.md).  
Tracking: [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88).

Во время freeze разрешены integrity, security, reproducibility, provenance, evidence-preservation, truth-surface и historical-recovery работы. Новые semantic/runtime features не авторизованы.

## Pending decisions

```text
Issue #18 — license/publication
  PENDING_OPERATOR / selected_option: null
  блокирует open contributions и package publication

Issue #74 / ADR-0024 — reducer referential semantics
  PROPOSED / PENDING_OPERATOR / selected_option: null
  блокирует reducer-v2 work
```

Ни одно решение не блокирует blueprint research. ADR-0025 не принимает их молча.

После blueprint review downstream work может быть рассмотрен заново:

```text
reconcile contract families
→ define NK-SAM and named equivalence
→ define portable Event/history commitment
→ decide ADR-0024 outcome if reducer work resumes
→ only then reducer-v2 runtime
```

## Быстрый старт для человека

Текущая laboratory требует Python 3.11 или 3.12:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_context.py --repo .
```

SQLite profile работает fail-closed, если Python связан с SQLite старше `3.51.3`. Полный setup находится в [`docs/QUICKSTART.ru.md`](docs/QUICKSTART.ru.md).

## Явные неэквивалентности

```text
Claim ≠ truth
admission ≠ objective truth
Unknown ≠ False
Architecture Canon ≠ implementation profile
reference laboratory ≠ final architecture
blueprint documentation ≠ implementation evidence
runtime implementation ≠ evidence
evidence ≠ operator authorization
C5 PASS ≠ production readiness
PostgreSQL + SQLite ≠ full substrate neutrality
hash chain ≠ complete authenticity
logical ERASED ≠ physical deletion
public repository ≠ open-source license
future-facing design ≠ demonstrated future substrate support
```

## Читать дальше

- [`STATUS.md`](STATUS.md) — authoritative human current state
- [`project-state.json`](project-state.json) — committed machine state
- [`ROADMAP.md`](ROADMAP.md) — active sequence
- [`docs/ARCHITECTURE_REFOUNDATION.ru.md`](docs/ARCHITECTURE_REFOUNDATION.ru.md) — blueprint plan
- [`AGENTS.md`](AGENTS.md) — обязательные инструкции репозитория
- [`docs/ai/CURRENT_STATE.md`](docs/ai/CURRENT_STATE.md) — AI continuity state
- [`docs/ai/KNOWN_RISKS.md`](docs/ai/KNOWN_RISKS.md) — active risks
- [`docs/QUICKSTART.ru.md`](docs/QUICKSTART.ru.md) — laboratory setup и tests
- [`docs/GLOSSARY.ru.md`](docs/GLOSSARY.ru.md) — terminology и distinctions
- [`docs/adr/README.md`](docs/adr/README.md) — architecture decisions
- [`evidence/c5/README.md`](evidence/c5/README.md) — retained evidence identities

Историческая status и review chronology остаётся доступной в Git history и version-bound records.
