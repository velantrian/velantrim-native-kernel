# 🧬 Переоснование архитектуры — Blueprint before Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **State:** `ACTIVE / POST-BLUEPRINT VALIDATION / IAR-1 RECONCILED / BPV1 PLAN NEXT / RUNTIME EXPANSION FROZEN`  
> **Blueprint decision:** [`ADR-0025`](./adr/0025-blueprint-before-runtime-expansion.md)  
> **Post-blueprint decision:** [`ADR-0026`](./adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md)  
> **Issue:** [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88)

## 1. Зачем нужна эта фаза

Native Kernel исследует technology-neutral architecture для meaning, memory, knowledge, provenance, uncertainty, change и accountability. Существующая линия **Python + PostgreSQL + SQLite** сохраняется как bounded reference laboratory, а не становится Canon только потому, что появилась первой.

```text
A1 purpose / non-goals
→ A2 ontology
→ A3 abstract machine
→ A4 semantic laws
→ A5 identity / time / change
→ A6 lifecycle
→ A7 conflict / uncertainty / revision
→ A8 substrate-independence
→ A9 reference-laboratory boundary
→ A10 open questions / falsification
→ integrated A1-A10 review
→ operator post-blueprint decision
→ independent architecture review             COMPLETE / IAR-1
→ review finding reconciliation               COMPLETE / IAR-1-R1
→ BPV1 plan and preregistration               NEXT
→ bounded cross-lineage falsification         BLOCKED UNTIL PLAN IS AUTHORITATIVE
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

Первый integrated review сохраняется как:

- [Integrated A1–A10 Review RU](./INTEGRATED_A1_A10_REVIEW.ru.md)
- [English review](./INTEGRATED_A1_A10_REVIEW.md)
- identity: `nk-integrated-blueprint-review/A1-A10-review-1`
- historical state: `COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING`

Integrated review reconciled семь cross-slice findings и в том проходе не нашёл remaining known blocking internal semantic contradiction. Он был явно **не** independent validation.

После этого ADR-0026 авторизовал Option D. Qualifying independent challenge теперь сохранён отдельно:

- [IAR-1 result RU](./reviews/IAR-1_RESULT.ru.md) / [EN](./reviews/IAR-1_RESULT.md) / [JSON](./reviews/IAR-1_RESULT.json)
- [IAR-1 reconciliation RU](./reviews/IAR-1_RECONCILIATION.ru.md) / [EN](./reviews/IAR-1_RECONCILIATION.md) / [JSON](./reviews/IAR-1_RECONCILIATION.json)
- review process outcome: `QUALIFYING_REVIEW_COMPLETE`
- findings: `10 total / 7 BLOCKING / 3 MATERIAL`
- reconciliation identity: `IAR-1-R1`
- reconciliation state: `COMPLETE`

IAR-1 не утверждает blueprint. Он его атакует. IAR-1-R1 не доказывает refined architecture; он фиксирует explicit provisional dispositions, необходимые перед falsification planning.

## 4. Reconciled minimum architecture boundary

IAR-1 показал, что first blueprint всё ещё слишком формировался current laboratory даже после literal Python/SQL/Event disclaimers. Поэтому следующее является **reference taxonomy**, а не universal minimum Kernel shape:

- полный A2 inventory;
- A3 `K → K′`, fixed transition-family catalogue и common outcome vocabulary;
- полный A5 seven-identity/eight-time inventory как mandatory whole;
- A6 nine lifecycle positions;
- Receipt-shaped accountability;
- Event-log-shaped history;
- exact replay/exact reconstruction.

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

При freeze разрешены architecture research; BPV-1 plan/preregistration; integrity/security/reproducibility/provenance fixes; evidence preservation; truth/validator repair; historical recovery; и later isolated falsification execution только после того, как его preregistered plan станет authoritative.

Автоматически не разрешены: BPV-1 execution до такого plan; reducer-v2; new semantic Event verbs; product database/language/model/integration profiles; executable NK-EPI/Temporal/full Admission; deletion execution expansion; Final Canon; maturity/production promotion.

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
Next bounded gate: BPV1_PLAN_AND_PREREGISTRATION
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

## 9. BPV-1 preregistration gate

Исходный independent-review protocol сохраняется как normative review method:

- [Independent Architecture Review Protocol RU](./INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md)
- [English protocol](./INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md)
- identity: `nk-independent-architecture-review/1`

Его header описывает publication-time state самого protocol и является historical относительно уже завершённого IAR-1. Current live review outcome записан в IAR-1 result/reconciliation records и `project-state.json`.

Перед BPV-1 implementation/execution authoritative plan обязан preregister:

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

Implementation под тестом не может после execution решать свой normative oracle. Post-execution изменения mandatory obligations, applicability, equivalence predicates или failure thresholds инвалидируют run для заявленного scope и требуют нового experiment identity.

## 10. Required threat and grounding boundary

Где materially relevant, BPV-1 planning объявляет protected meanings, trust roots/assumptions и adversarial cases, включая forgery, fork, truncation, rollback, equivocation, withheld counterevidence, unavailable/colluding witnesses и compromised certifier.

Context/Provenance/Authority chains обязаны завершаться через explicit finite grounding mode:

```text
EXTERNALLY_ATTESTED_ROOT
EXPLICIT_ASSUMED_ROOT
BOUNDED_RECURSIVE_CLOSURE
DECLARED_CYCLE
TERMINAL_UNKNOWN_OR_GAP
```

Physical/cryptographic erasure нельзя продвигать из unverified self-assertion; при отсутствии sufficient threat-scoped evidence правильный outcome остаётся `INDETERMINATE`.

## 11. Current sequence и hard stop

```text
IAR-1 qualifying review                       COMPLETE
IAR-1-R1 reconciliation                       COMPLETE
BPV1_PLAN_AND_PREREGISTRATION                 NEXT
BPV-1 bounded cross-lineage falsification     BLOCKED_PENDING_PREREGISTERED_PLAN
A10 outcome classification                    BLOCKED BY BPV-1
integrated re-review                           BLOCKED BY OUTCOMES
separate operator Canon/runtime decision      BLOCKED BY RE-REVIEW
```

`BPV1_PLAN_AND_PREREGISTRATION` разрешает только design/preregistration. Это не A11, не experiment execution, не runtime thaw, не Final Canon и не production authorization.