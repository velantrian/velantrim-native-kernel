# 🧬 Velantrim Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

### Технологически нейтральная архитектура долговечного знания, памяти, изменений и объяснения

> **Текущее состояние:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Активная фаза:** `POST-BLUEPRINT VALIDATION / BPV1 PREREGISTERED / EXECUTION ADMISSION NEXT / RUNTIME EXPANSION FROZEN`

Velantrim Native Kernel исследует, какой смысл, identity, provenance, time, uncertainty, conflict, revision и explanation должны сохраняться при смене баз данных, языков, моделей, процессоров и носителей информации.

Это **не** ядро операционной системы, не database product, не LLM memory plugin, не vector store и не определение Python framework.

```text
сначала определить problem-level смысл и candidate obligations
        ↓
заранее зафиксировать scope, observables, threat/grounding assumptions и failure rules
        ↓
зафиксировать external oracle и admission boundary
        ↓
независимо вывести заменяемую bounded realization
        ↓
проверять и опровергать архитектурные claims
```

## Архитектурная граница

```text
Problem-level Purpose and Candidate Semantic Obligations
→ Preregistered Conformance / Threat / Grounding Boundary
→ BPV1 Execution Admission
→ Independently Derived Bounded Realization
→ Positive + Adversarial Negative Fixtures
→ Cross-lineage Semantic Comparison
→ Evidence
→ Outcome / Status / Maturity
```

Python, Rust, JSON, SHA-256, PostgreSQL, SQLite, graphs, vectors, LLM, обычное hardware, event sourcing, exact replay и CI являются заменяемыми research instruments. Они не являются постоянным Canon.

Текущая Python/PostgreSQL/SQLite lineage — **bounded reference laboratory**, а не окончательное определение Native Kernel. IAR-1 показал, что полные A3 transition/outcome machine, A6 lifecycle graph, текущая Event/reducer/Receipt форма и exact reconstruction не обоснованы как universal minimum Kernel form.

## Текущее состояние

```text
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
runtime expansion: FROZEN
```

C5 не повышает semantic assertions и не разрешает production.

## Модель checkpoint

Машиночитаемая правда записана в [`project-state.json`](project-state.json) по протоколу `nk-project-state/2`.

| Роль | Checkpoint |
|---|---|
| Publication checkpoint | `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c` |
| Runtime checkpoint | `675aa4b398a2fc0181dc71d38904a2d33a09f5f8` |
| Runtime integrity checkpoint | `a1cdc6d8f36d67f40f065641809bc6da463c10a4` |
| Evidence-producing checkpoint | `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7` |
| Источник manifest / Notion synchronized descendant | `70acd0da61fee19131947aa56125833adb156ced` |
| BPV-1 preregistration merge | `a538d7f1e28858a88b9ee777ac7d6e05b85943db` |

Эти role checkpoints остаются historical identities. Live `main` определяется через GitHub или checked-out Git ref; committed state не предсказывает SHA собственного будущего merge.

## Reconciliation правды

```text
machine-readable truth: historical reconciliation preserved
human-readable truth:   historical reconciliation preserved
IAR-1:                  QUALIFYING_REVIEW_COMPLETE
IAR-1-R1:               COMPLETE
BPV-1 plan:             PREREGISTERED / EXECUTION_NOT_AUTHORIZED
```

Более новый live Notion content нужно проверять напрямую и синхронизировать после material GitHub merges. Historical reports и proposals сохраняются, но не переопределяют current state.

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

ADR-0025, ADR-0026, IAR-1, IAR-1-R1 и BPV-1 preregistration не расширяют существующие runtime/evidence proof boundaries.

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
  BPV1-001 PREREGISTERED / EXECUTION ADMISSION NEXT
  NO AUTOMATIC PROMOTION
```

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
```

## Активная архитектурная фаза — Post-Blueprint Validation

ADR-0025 установил blueprint-before-runtime. ADR-0026 фиксирует operator-approved **Option D** validation route. IAR-1 завершил qualifying independent challenge; IAR-1-R1 reconciled все десять findings; PR #110 опубликовал preregistered BPV-1 plan.

```text
A1–A10 provisional blueprint
→ integrated review                         COMPLETE / PROVISIONAL
→ operator post-blueprint decision          OPTION D / ADR-0026 / APPROVED
→ INDEPENDENT_ARCHITECTURE_REVIEW           COMPLETE / IAR-1 / QUALIFYING
→ REVIEW_FINDING_RECONCILIATION             COMPLETE / IAR-1-R1
→ BPV1_PLAN_AND_PREREGISTRATION             COMPLETE / PR #110
→ BPV1_EXECUTION_ADMISSION                  COMPLETE / PR #112
→ BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION NEXT GATE
→ BPV-1 bounded cross-lineage falsification ADMITTED_FOR_EXPERIMENT_ONLY
→ A10 outcome classification
→ integrated re-review
→ отдельное последующее operator Canon/runtime decision
```

Текущие boundaries:

```text
independent architectural validation: IAR-1 QUALIFYING_REVIEW_COMPLETE
IAR-1 findings: 10 total / 7 BLOCKING / 3 MATERIAL
IAR-1-R1: COMPLETE / open blockers 0 / open material 0
BPV-1 plan: BPV1-001-cross-lineage-bounded-accountability-v1 / PREREGISTERED / EXECUTION_NOT_AUTHORIZED
plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
execution-admission package merge: 6027eec73f11c4626be5553de7e79f827be2c81d
next gate: BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION
BPV-1 execution: ADMITTED_FOR_EXPERIMENT_ONLY
runtime expansion: FROZEN
product runtime thaw: NO
A1-A10 Final Canon: NOT AUTHORIZED
production: false
```

IAR-1 **не** доказал правильность architecture. Текущий candidate minimum остаётся problem-level: non-conflation representation/Claim с reality/truth; явные scope/Context/warrant/Authority assumptions там, где material; явные Unknown/uncertainty/unsupported states; accountable change/retention/loss для declared scope; preregistered equivalence/degradation/refutation conditions.

Plan freeze все двенадцать IAR-1-R1 normative fields до execution. Post-execution изменения не могут спасти run; они требуют нового experiment identity.

BPV1 execution admission всё ещё должен связать frozen plan digest, machine-readable fixtures, standalone evaluator tests, pinned Rust toolchain/source boundary и static no-product-integration audit. Rust — experimental instrument, не Canon и не product runtime profile.

План: [English](docs/ARCHITECTURE_REFOUNDATION.md) · [Русский](docs/ARCHITECTURE_REFOUNDATION.ru.md).  
BPV-1 preregistration: [English](docs/research/BPV1_PREREGISTRATION.md) · [Русский](docs/research/BPV1_PREREGISTRATION.ru.md) · [JSON](docs/research/BPV1_PREREGISTRATION.json).  
Tracking: [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88).

Во время freeze разрешены architecture research, execution-admission packaging, integrity/security/reproducibility/provenance repair, evidence preservation, truth-surface repair и historical recovery. BPV-1 subject implementation/execution остаётся запрещённым до отдельного admission. Product semantic/runtime expansion остаётся unauthorized.

## Pending decisions

```text
Issue #18 — license/publication
  PENDING_OPERATOR / selected_option: null

Issue #74 / ADR-0024 — reducer referential semantics
  PROPOSED / PENDING_OPERATOR / selected_option: null
```

Ни одно решение не принимается молча через ADR-0026 или BPV-1. Track H source admission остаётся operator-controlled.

## Historical R1 gate markers

Эти exact строки сохраняются только ради publication-time continuity R1-era documentation registry и **не описывают current state**:

```text
BPV1_PLAN_AND_PREREGISTRATION
BLOCKED_PENDING_PREREGISTERED_PLAN
```

## Быстрый старт для человека

Текущая laboratory требует Python 3.11 или 3.12:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_bpv1_preregistration.py --repo .
python tools/ai_context/validate_context.py --repo .
```

> **Предупреждение SQLite profile:** P5/C3/C4/C5 fail closed, если Python-процесс связан с SQLite ниже `3.51.3`. Не трактуй отказ system SQLite как semantic failure. Перед этими profile checks собери/используй pinned safe SQLite library.

Pinned-library setup, PostgreSQL DSN и полные команды P4/P5/C3/C4/C5 находятся в [`docs/QUICKSTART.ru.md`](docs/QUICKSTART.ru.md).
