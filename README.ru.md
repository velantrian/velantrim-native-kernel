# 🧬 Velantrim Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

### Технологически нейтральная архитектура долговечного знания, памяти, изменений и объяснения

> **Текущее состояние:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Активная фаза:** `POST-BLUEPRINT VALIDATION / IAR-1 RECONCILED / BPV1 PLAN NEXT / RUNTIME EXPANSION FROZEN`

Velantrim Native Kernel исследует, какой смысл, identity, provenance, time, uncertainty, conflict, revision и explanation должны сохраняться при смене баз данных, языков, моделей, процессоров и носителей информации.

Это **не** ядро операционной системы, не database product, не LLM memory plugin, не vector store и не определение Python framework.

```text
сначала определить problem-level смысл и candidate obligations
        ↓
заранее зафиксировать scope, observables, threat/grounding assumptions и failure rules
        ↓
независимо вывести заменяемую bounded realization
        ↓
сопоставить её с provisional reference taxonomies
        ↓
проверять и опровергать архитектурные claims
```

## Архитектурная граница

```text
Problem-level Purpose and Candidate Semantic Obligations
→ Preregistered Conformance / Threat / Grounding Boundary
→ Independently Derived Bounded Realization
→ Replaceable Implementation or Falsification Instrument
→ Positive + Adversarial Negative Fixtures
→ Cross-lineage Semantic Comparison
→ Evidence
→ Outcome / Status / Maturity
```

Python, JSON, SHA-256, PostgreSQL, SQLite, graphs, vectors, LLM, обычное hardware, event sourcing, exact replay и CI являются заменяемыми research instruments. Они не являются постоянным Canon.

Текущая Python/PostgreSQL/SQLite lineage — **bounded reference laboratory**, а не окончательное определение Native Kernel. IAR-1 дополнительно показал, что полные A3 transition/outcome machine, A6 lifecycle graph, текущая Event/reducer/Receipt форма и exact reconstruction пока не обоснованы как universal minimum Kernel form.

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
Notion dashboard:       COMMITTED CHECKPOINT THROUGH PR #86
checkpoint role repair: COMPLETE / PR #87
```

Указанный exact committed Notion checkpoint является историческим. Более новый live Notion content нужно проверять напрямую и после material GitHub merges снова синхронизировать/read back. Исторические отчёты и proposals сохраняются, но не переопределяют current state.

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

ADR-0025, ADR-0026, IAR-1 и IAR-1-R1 не расширяют существующий runtime/evidence proof boundary.

## Три независимые линии

```text
H — Historical Recovery
  authentic v0.1.2.1 и оригинальные 44 теста
  NOT_FOUND_IN_ACCESSIBLE_SOURCES / OPEN / INDEPENDENT

C — Clean Reference Implementation
  P1–P5 + C4 + C5
  PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY

R — Post-Blueprint Validation
  A1–A10 + integrated review остаются provisional
  IAR-1 QUALIFYING / IAR-1-R1 COMPLETE
  ACTIVE / BPV1 PLAN NEXT / NO AUTOMATIC PROMOTION
```

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
```

## Активная архитектурная фаза

ADR-0025 установил blueprint-before-runtime. A1–A10 и первый integrated review остаются `DRAFTED / PROVISIONAL` architecture work.

ADR-0026 фиксирует operator-approved **Option D** validation route. IAR-1 завершил independent challenge, а IAR-1-R1 reconciled все десять findings без Final Canon promotion:

```text
A1–A10 provisional blueprint
→ integrated review                         COMPLETE / PROVISIONAL
→ operator post-blueprint decision          OPTION D / ADR-0026 / APPROVED
→ INDEPENDENT_ARCHITECTURE_REVIEW           COMPLETE / IAR-1 / QUALIFYING
→ REVIEW_FINDING_RECONCILIATION             COMPLETE / IAR-1-R1
→ BPV1_PLAN_AND_PREREGISTRATION             NEXT GATE
→ BPV-1 bounded cross-lineage falsification BLOCKED BY PREREGISTERED PLAN
→ A10 outcome classification
→ integrated re-review
→ отдельное последующее operator Canon/runtime decision
```

Текущие boundaries:

```text
independent architectural validation: IAR-1 QUALIFYING_REVIEW_COMPLETE
IAR-1 findings: 10 total / 7 BLOCKING / 3 MATERIAL
IAR-1-R1: COMPLETE / open blockers 0 / open material 0
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
runtime expansion: FROZEN
product runtime thaw: NO
A1-A10 Final Canon: NOT AUTHORIZED
production: false
```

IAR-1 **не** доказал правильность architecture. Он materially ослабил её. Текущий candidate minimum является problem-level: non-conflation representation/Claim с reality/truth; явные scope/Context/warrant/Authority assumptions там, где material; явные Unknown/uncertainty/unsupported states; accountable change/retention/loss для declared scope; preregistered equivalence/degradation/refutation conditions.

До BPV-1 execution план обязан зафиксировать `scenario_id`, purpose scope, mandatory obligations, applicability rules, mandatory observables, equivalence predicates, allowed declared losses, failure thresholds, hard refutation observations, grounding mode, threat model и oracle Authority. Post-execution изменение этих normative fields не может спасти run и требует нового experiment identity.

План: [English](docs/ARCHITECTURE_REFOUNDATION.md) · [Русский](docs/ARCHITECTURE_REFOUNDATION.ru.md).  
Blueprint decision: [`ADR-0025`](docs/adr/0025-blueprint-before-runtime-expansion.md).  
Post-blueprint decision: [`ADR-0026`](docs/adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md).  
Independent-review protocol: [English](docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md) · [Русский](docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md).  
IAR-1 result: [English](docs/reviews/IAR-1_RESULT.md) · [Русский](docs/reviews/IAR-1_RESULT.ru.md) · [JSON](docs/reviews/IAR-1_RESULT.json).  
IAR-1 reconciliation: [English](docs/reviews/IAR-1_RECONCILIATION.md) · [Русский](docs/reviews/IAR-1_RECONCILIATION.ru.md) · [JSON](docs/reviews/IAR-1_RECONCILIATION.json).  
Tracking: [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88).

Во время freeze разрешены architecture research, BPV-1 planning/preregistration, integrity, security, reproducibility, provenance, evidence-preservation, truth-surface и historical-recovery work. BPV-1 execution остаётся запрещённым до authoritative preregistered plan. Новые product semantic/runtime features не авторизованы.

## Pending decisions

```text
Issue #18 — license/publication
  PENDING_OPERATOR / selected_option: null
  блокирует open contributions и package publication

Issue #74 / ADR-0024 — reducer referential semantics
  PROPOSED / PENDING_OPERATOR / selected_option: null
  блокирует reducer-v2 work
```

Ни одно решение не принимается молча через ADR-0026 или IAR-1-R1. Track H source admission также остаётся operator-controlled.

Runtime work может быть пересмотрен только отдельным последующим operator decision после validation. Сам BPV-1 не является product runtime и не может разрешить reducer-v2 или другое runtime expansion.

## Быстрый старт для человека

Текущая laboratory требует Python 3.11 или 3.12:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_context.py --repo .
```

> **Предупреждение SQLite profile:** P5/C3/C4/C5 fail closed, если Python-процесс связан с SQLite ниже `3.51.3`. Не трактуй отказ system SQLite как semantic failure. Перед этими profile checks собери/используй pinned safe SQLite library.

Pinned-library setup, PostgreSQL DSN и полные команды P4/P5/C3/C4/C5 находятся в [`docs/QUICKSTART.ru.md`](docs/QUICKSTART.ru.md).