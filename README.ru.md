# 🧬 Velantrim Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

### Технологически нейтральная архитектура долговечного знания, памяти, изменений и объяснения

> **Текущее состояние:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Активная фаза:** `POST-BLUEPRINT VALIDATION / D5-R1 QUALIFIED / D6 A10 HYPOTHESIS CLASSIFICATION NEXT / RUNTIME EXPANSION FROZEN`

Velantrim Native Kernel исследует, какой семантический смысл, identity, provenance, time, uncertainty, conflict, revision и explanation должны сохраняться при смене баз данных, языков, моделей, процессоров и носителей информации.

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
проверять и пытаться опровергнуть архитектурные claims
        ↓
классифицировать только реально проверенные гипотезы
```

## Архитектурная граница

```text
Problem-level Purpose and Candidate Semantic Obligations
→ Preregistered Conformance / Threat / Grounding Boundary
→ BPV1 Execution Admission
→ Independently Derived Bounded Realization
→ External Evidence Qualification
→ Frozen Oracle Evaluation
→ A10 Hypothesis Classification
→ Integrated Re-review
→ Separate Operator Canon/Runtime Decision
```

Python, Rust, JSON, SHA-256, PostgreSQL, SQLite, graphs, vectors, LLM, обычное hardware, event sourcing, exact replay и CI являются заменяемыми research instruments. Они не являются постоянным Canon.

Текущая Python/PostgreSQL/SQLite lineage — **bounded reference laboratory**, а не окончательное определение Native Kernel. IAR-1 показал, что полные A3 transition/outcome machine, A6 lifecycle graph, текущая Event/reducer/Receipt форма и exact reconstruction не обоснованы как universal minimum Kernel form.

## Текущее состояние

```text
clean_runtime_support:      PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
runtime expansion: FROZEN
P1-C5 role: BOUNDED_REFERENCE_LABORATORY
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
| Источник manifest / исторический Notion-synchronized descendant | `70acd0da61fee19131947aa56125833adb156ced` |
| BPV-1 preregistration merge | `a538d7f1e28858a88b9ee777ac7d6e05b85943db` |
| D5 execution merge | `a191e9c868c14af34a269dcdfae44406f1013bda` |
| D5-R1 qualification merge | `3856740570620fb2243e2f0da76359281ec4068f` |

Эти role checkpoints остаются historical identities. Live `main` определяется через GitHub или checked-out Git ref; committed state не предсказывает SHA собственного будущего merge.

## Reconciliation правды

```text
IAR-1:                    QUALIFYING_REVIEW_COMPLETE
IAR-1-R1:                 COMPLETE
BPV-1 plan:               PREREGISTERED / EXECUTION_NOT_AUTHORIZED
execution admission:      COMPLETE / BPV1-001 ONLY
D5 execution:             COMPLETE
D5-R1 qualification:      COMPLETE / QUALIFIED
qualified oracle outcome: SUPPORTED_FOR_SCOPE / 12-of-12 mandatory fixtures PASS
next gate:                D6_A10_HYPOTHESIS_CLASSIFICATION
D6:                       NOT_STARTED
```

Live Notion нужно читать напрямую. Текущий Option D plan откладывает синхронизацию D5/D5-R1/D6 до consolidated D8; до этого GitHub остаётся authoritative technical truth.

## Текущая карта evidence

В репозитории сохранены две неизменяемые C5 evidence identities:

```text
evidence/c5/2026-08-07/manifest.json
evidence/c5/2026-08-08-adr0023/manifest.json
```

BPV1-001 D5-R1 qualification evidence отдельно сохранено в:

```text
experiments/bpv1/BPV1-001/results/d5-r1/
```

Историческое D5 evidence из PR #114 не переписано.

ADR-0023 устанавливает linked SQLite `3.51.3` как текущий WAL floor. Исторические SQLite `3.45.1` artifacts остаются неизменными и version-bound.

```text
repository-resident evidence
≠ independent custody
≠ complete authenticity
≠ live-data safety
≠ physical deletion
≠ production readiness
SUPPORTED_FOR_SCOPE
≠ universal substrate portability proof
```

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
  BPV1-001 D5 COMPLETE / D5-R1 QUALIFIED
  D6 A10 HYPOTHESIS CLASSIFICATION NEXT
  NO AUTOMATIC PROMOTION
```

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
```

## Активная архитектурная фаза — Post-Blueprint Validation

ADR-0025 установил blueprint-before-runtime. ADR-0026 фиксирует operator-approved **Option D** validation route. IAR-1 завершил qualifying independent challenge; IAR-1-R1 reconciled все десять findings; PR #110 опубликовал preregistered BPV-1 plan; PR #112 + PR #113 завершили execution admission; PR #114 выполнил D5; PR #115 квалифицировал evidence path.

```text
A1–A10 provisional blueprint
→ integrated review                         COMPLETE / PROVISIONAL
→ operator post-blueprint decision          OPTION D / ADR-0026 / APPROVED
→ INDEPENDENT_ARCHITECTURE_REVIEW           COMPLETE / IAR-1 / QUALIFYING
→ REVIEW_FINDING_RECONCILIATION             COMPLETE / IAR-1-R1
→ BPV1_PLAN_AND_PREREGISTRATION             COMPLETE / PR #110
→ BPV1_EXECUTION_ADMISSION                  COMPLETE / PR #112 + #113
→ BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION COMPLETE / PR #114
→ D5_R1_EVIDENCE_QUALIFICATION              COMPLETE / PR #115
→ D6_A10_HYPOTHESIS_CLASSIFICATION          NEXT / NOT STARTED
→ integrated re-review
→ consolidated authoritative synchronization
→ отдельное последующее operator Canon/runtime decision
```

Текущие boundaries:

```text
BPV-1 plan: BPV1-001-cross-lineage-bounded-accountability-v1 / PREREGISTERED
plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
frozen plan digest: 7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0
D5 execution merge: a191e9c868c14af34a269dcdfae44406f1013bda
D5-R1 qualification merge: 3856740570620fb2243e2f0da76359281ec4068f
external qualification: QUALIFIED
frozen-oracle outcome: SUPPORTED_FOR_SCOPE
mandatory fixtures: 12/12 PASS
next gate: D6_A10_HYPOTHESIS_CLASSIFICATION
D6: NOT_STARTED
runtime expansion: FROZEN
product runtime thaw: NO
A1-A10 Final Canon: NOT AUTHORIZED
production: false
```

D5-R1 устраняет найденный HR10 subject-self-report adjudication path: Rust-subject теперь выдаёт raw facts, а oracle-facing structural facts выводятся отдельным qualifier, который не читает fixture expectations. Неизменённый frozen evaluator остаётся adjudicator. Integrity coverage теперь включает evidence и epistemic position, а retained loss-witness storage внутренне bounded с bounded rollup.

Это всё ещё **не** устанавливает independent implementation team/custody или independent computation model. BPV1-001 остаётся conventional-digital, single-node, non-composed scoped evidence.

D6 должен классифицировать только реально adjudicated A10 hypotheses. Aggregate `SUPPORTED_FOR_SCOPE` нельзя механически переносить на hypotheses, отмеченные как informative или not tested.

План: [English](docs/ARCHITECTURE_REFOUNDATION.md) · [Русский](docs/ARCHITECTURE_REFOUNDATION.ru.md).  
BPV-1 preregistration: [English](docs/research/BPV1_PREREGISTRATION.md) · [Русский](docs/research/BPV1_PREREGISTRATION.ru.md) · [JSON](docs/research/BPV1_PREREGISTRATION.json).  
D5-R1 qualification: [English](docs/research/BPV1_D5_R1_QUALIFICATION.md) · [Русский](docs/research/BPV1_D5_R1_QUALIFICATION.ru.md).  
Tracking: [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88).

Во время freeze разрешены architecture research, D6/D7/D8 validation work, integrity/security/reproducibility/provenance repair, evidence preservation, truth-surface repair и historical recovery. Product semantic/runtime expansion остаётся unauthorized.

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
