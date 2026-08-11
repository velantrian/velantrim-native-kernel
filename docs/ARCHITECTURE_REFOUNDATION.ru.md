# 🧬 Переоснование архитектуры — Blueprint before Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **State:** `ACTIVE / POST-BLUEPRINT VALIDATION / BPV1 PREREGISTERED / EXECUTION ADMISSION NEXT / RUNTIME EXPANSION FROZEN`  
> **Blueprint decision:** [`ADR-0025`](./adr/0025-blueprint-before-runtime-expansion.md)  
> **Post-blueprint decision:** [`ADR-0026`](./adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md)  
> **Issue:** [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88)

## 1. Зачем нужна эта фаза

Native Kernel исследует technology-neutral architecture для meaning, memory, knowledge, provenance, uncertainty, change и accountability. Существующая линия **Python + PostgreSQL + SQLite** сохраняется как bounded reference laboratory, а не становится Canon только потому, что появилась первой.

```text
A1-A10 blueprint                                  COMPLETE / PROVISIONAL
→ integrated A1-A10 review                       COMPLETE / PROVISIONAL
→ operator post-blueprint decision               COMPLETE / OPTION D
→ independent architecture review                COMPLETE / IAR-1
→ review finding reconciliation                  COMPLETE / IAR-1-R1
→ BPV1 plan and preregistration                  COMPLETE / PR #110
→ BPV1 execution admission                       NEXT
→ bounded cross-lineage falsification            BLOCKED BY ADMISSION
```

## 2. Draft inventory

Все десять required blueprint slices существуют и остаются `DRAFTED / PROVISIONAL`. A10 сохраняет model identity `nk-open-questions-falsification/A10-draft-1`.

1. [A1 RU](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) / [EN](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md)
2. [A2 RU](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md) / [EN](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md)
3. [A3 RU](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md) / [EN](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md)
4. [A4 RU](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md) / [EN](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md)
5. [A5 RU](./A5_IDENTITY_TIME_AND_CHANGE.ru.md) / [EN](./A5_IDENTITY_TIME_AND_CHANGE.md)
6. [A6 RU](./A6_KNOWLEDGE_LIFECYCLE.ru.md) / [EN](./A6_KNOWLEDGE_LIFECYCLE.md)
7. [A7 RU](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md) / [EN](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md)
8. [A8 RU](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md) / [EN](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md)
9. [A9 RU](./A9_REFERENCE_LABORATORY_BOUNDARY.ru.md) / [EN](./A9_REFERENCE_LABORATORY_BOUNDARY.md)
10. [A10 RU](./A10_OPEN_QUESTIONS_AND_FALSIFICATION.ru.md) / [EN](./A10_OPEN_QUESTIONS_AND_FALSIFICATION.md)

## 3. Integrated и independent review lineage

Первый integrated review сохраняется как `nk-integrated-blueprint-review/A1-A10-review-1`, historical state `COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING`. Он reconciled семь cross-slice findings и в том проходе не нашёл remaining known blocking internal semantic contradiction. Это явно **не** independent validation.

Stable gate token: `INTEGRATED_A1_A10_REVIEW`.

После этого ADR-0026 авторизовал Option D. Qualifying independent challenge сохранён отдельно в IAR-1 result/reconciliation records:

- review process: `QUALIFYING_REVIEW_COMPLETE`;
- findings: `10 total / 7 BLOCKING / 3 MATERIAL`;
- reconciliation: `IAR-1-R1 / COMPLETE`;
- open blocking/material findings после reconciliation: `0 / 0`.

IAR-1 не утверждает blueprint. IAR-1-R1 не доказывает refined architecture; он фиксирует explicit provisional dispositions перед falsification.

## 4. Reconciled minimum architecture boundary

IAR-1 показал, что first blueprint всё ещё слишком формировался current laboratory даже после literal Python/SQL/Event disclaimers. Полный A2 inventory, A3 transition/outcome catalogue, A5 identity/time inventory, A6 lifecycle graph, Receipt-shaped accountability, Event-log-shaped history, exact replay и exact reconstruction поэтому остаются **reference taxonomies/capabilities**, а не universal minimum Kernel shape.

Меньший current candidate minimum является problem-level:

```text
representation / Claim не смешиваются молча с reality / truth
scope / Context / warrant-provenance / Authority assumptions явны, где material
Unknown / uncertainty / unsupported остаются явными
change / revision / supersession / retention / loss accountable для declared scope
equivalence / degradation / loss оцениваются по preregistered observables и failure rules
```

Future realization может использовать snapshots, witnesses, bounded summaries, procedural accounts или другой state/change model, если preregistered obligations его scope сохраняются.

## 5. Граница Reference Laboratory

P1–C5 остаётся `BOUNDED_REFERENCE_LABORATORY`. Python, PostgreSQL, SQLite, SQL, JSON, SHA-256, current Event/reducer/Receipt/sequence mechanisms, CI и evidence packaging остаются profile/laboratory mechanisms, если later architecture decision не установит иное.

```text
useful implementation evidence ≠ architecture requirement
PostgreSQL ↔ SQLite C3 ≠ independent-language equivalence
bounded accountability ≠ exact reconstruction
history visibility ≠ mandatory Event sourcing
local conformance ≠ composition/federation conformance
substrate-independent specification ≠ universal portability proof
```

## 6. Runtime freeze

При freeze разрешены architecture research; execution-admission packaging, выведенный из frozen BPV-1 plan; integrity/security/reproducibility/provenance fixes; evidence preservation; truth/validator repair; historical recovery; и later isolated falsification execution только после отдельного admission.

Не разрешены: subject implementation/execution до admission; reducer-v2; new semantic Event verbs; product database/language/model/integration profiles; executable NK-EPI/Temporal/full Admission; deletion execution expansion; Final Canon; maturity/production promotion.

## 7. Pending operator-controlled decisions

- Issue #18 license/publication: unchanged / operator-controlled.
- Issue #74 / ADR-0024: `PROPOSED / PENDING_OPERATOR`; reducer-v2 unauthorized.
- ADR-0003: `PROPOSED / NOT_STARTED`.
- Track H source admission: operator-controlled.

## 8. Current progress

```text
Blueprint content: A1-A10 DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY
Integrated review: COMPLETED / PROVISIONAL
Operator post-blueprint decision: OPTION D / ADR-0026 / APPROVED
Independent architecture review: IAR-1 / QUALIFYING_REVIEW_COMPLETE
IAR-1 findings: 10 total / 7 BLOCKING / 3 MATERIAL
Review finding reconciliation: IAR-1-R1 / COMPLETE
Open BLOCKING findings: 0
Open MATERIAL findings: 0
BPV-1 plan: BPV1-001-cross-lineage-bounded-accountability-v1 / PREREGISTERED
Authoritative plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
BPV-1 execution-admission package merge: 6027eec73f11c4626be5553de7e79f827be2c81d
Next bounded gate: BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION
BPV-1 execution: ADMITTED_FOR_EXPERIMENT_ONLY
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

## 9. BPV-1 preregistration and execution-admission gate

Authoritative plan: [BPV1_PREREGISTRATION RU](./research/BPV1_PREREGISTRATION.ru.md) / [EN](./research/BPV1_PREREGISTRATION.md) / [JSON](./research/BPV1_PREREGISTRATION.json). Он merged PR #110 как `a538d7f1e28858a88b9ee777ac7d6e05b85943db`.

До execution он freeze ровно следующие поля:

```text
scenario_id
purpose_scope
mandatory_obligations
applicability_rules
mandatory_observables
equivalence_predicates
allowed_declared_losses
failure_thresholds
hard_refutation_observations
grounding_mode
threat_model
oracle_authority
```

`BPV1-001` задаёт single-node, non-composed, conventional-digital, cross-language Rust falsification instrument с bounded durable semantic state и без authoritative per-operation Event log. Rust — только experimental instrument, не Canon и не product profile. Independent team/custody и independent computation model имеют статус `NOT_ESTABLISHED`.

Post-execution изменение normative fields инвалидирует run и требует нового scenario identity.

Gate execution-admission, `BPV1_EXECUTION_ADMISSION`, теперь `COMPLETE`: PR #112 (merge `6027eec73f11c4626be5553de7e79f827be2c81d`) связал frozen plan/digest, machine-readable fixtures, standalone evaluator tests, pinned Rust toolchain/source boundary и static no-product-integration audit до любого subject execution. Он допускает только BPV1-001 subject implementation/execution; product runtime integration остаётся не авторизованным.

## 10. Required threat and grounding boundary

Preregistered plan объявляет protected meanings, trust assumptions и adversarial cases, включая forgery, truncation, rollback, equivocation, withheld counterevidence и unavailable/forged Authority, где применимо.

Context/Provenance/Authority evaluation использует explicit finite grounding mode вместо infinite recursive metadata. Physical/cryptographic erasure находится вне scope BPV1-001 из-за отсутствия independently observable physical-substrate erasure channel; более сильный erasure claim из этого эксперимента выводить нельзя.

## 11. Current sequence и hard stop

```text
IAR-1 qualifying review                       COMPLETE
IAR-1-R1 reconciliation                       COMPLETE
BPV1_PLAN_AND_PREREGISTRATION                 COMPLETE / PR #110
BPV1_EXECUTION_ADMISSION                      COMPLETE / PR #112
BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION     NEXT
BPV-1 bounded cross-lineage falsification     ADMITTED_FOR_EXPERIMENT_ONLY
A10 outcome classification                    BLOCKED BY BPV-1
integrated re-review                           BLOCKED BY OUTCOMES
separate operator Canon/runtime decision      BLOCKED BY RE-REVIEW
```

`BPV1_EXECUTION_ADMISSION` допустил только bounded preregistered BPV1-001 falsification instrument's subject implementation/execution. Это не A11, не product runtime thaw, не Final Canon и не production authorization.

### Historical IAR-1-R1 publication-time markers

Следующие строки сохраняются только как historical R1 publication-time state и **не описывают current gate**:

```text
Next bounded gate: BPV1_PLAN_AND_PREREGISTRATION
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
```
