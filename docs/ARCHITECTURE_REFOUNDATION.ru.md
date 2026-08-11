# 🧬 Переоснование архитектуры — Blueprint before Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **State:** `ACTIVE / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`  
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
→ independent architecture review
→ bounded cross-lineage falsification только после review reconciliation
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

## 3. Integrated review

Первый integrated review сохраняется как:

- [Integrated A1–A10 Review RU](./INTEGRATED_A1_A10_REVIEW.ru.md)
- [English review](./INTEGRATED_A1_A10_REVIEW.md)
- completed gate identity: `INTEGRATED_A1_A10_REVIEW`
- review identity: `nk-integrated-blueprint-review/A1-A10-review-1`
- historical completion state: `COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING`

Review явно reconciles семь cross-slice findings вместо silent rewrite draft history. Ключевые current provisional interpretations:

```text
PHYSICALLY_ERASED ≠ CRYPTOGRAPHICALLY_ERASED
FORGOTTEN_OR_LOST не требует deliberate erasure method
A1 confidence wording → uncertainty + epistemic position
A10 outcome protocol = ровно пять declared outcomes
Conflict ≠ necessarily Contradiction
A6 lifecycle positions ≠ mandatory pipeline stages
```

После этих explicit reconciliation decisions review не нашёл remaining known blocking internal semantic contradiction в этом pass. Это всё ещё не independent validation.

## 4. Граница Reference Laboratory

P1–C5 остаётся `BOUNDED_REFERENCE_LABORATORY`. Python, PostgreSQL, SQLite, SQL, JSON, SHA-256, current Event/reducer/Receipt/sequence mechanisms, CI и evidence packaging остаются profile/laboratory mechanisms, если separate architecture decision не установит иное.

```text
useful implementation evidence ≠ architecture requirement
PostgreSQL ↔ SQLite C3 ≠ independent-language equivalence
substrate-independent specification ≠ universal portability proof
```

## 5. Runtime freeze

При freeze разрешены architecture research; independent architectural review; review reconciliation; integrity/security/reproducibility/provenance fixes; evidence preservation; truth/validator repair; historical recovery; а позднее — isolated falsification experiments, допущенные ADR-0026 без runtime promotion.

Автоматически не разрешены reducer-v2, new semantic Event verbs, product database/language/model/integration profiles, executable NK-EPI/Temporal/full Admission, deletion execution expansion, maturity или production promotion.

## 6. Pending operator-controlled decisions

- Issue #18 license/publication: unchanged / operator-controlled.
- Issue #74 / ADR-0024: `PROPOSED / PENDING_OPERATOR`; reducer-v2 unauthorized.
- ADR-0003: `PROPOSED / NOT_STARTED`.
- Track H source admission: operator-controlled.

## 7. Current progress

```text
Blueprint content: A1-A10 DRAFTED / PROVISIONAL
Integrated review: COMPLETED / PROVISIONAL
Operator post-blueprint decision: OPTION D / ADR-0026 / APPROVED
Next bounded gate: INDEPENDENT_ARCHITECTURE_REVIEW
Independent architectural validation: NOT ESTABLISHED
BPV-1: BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

## 8. Gate завершения blueprint

Исторический blueprint completion gate удовлетворён только в узком смысле: оператор через ADR-0026 выбрал следующую **validation** phase. Это не продвигает A1–A10 в Final Canon и не разрешает runtime thaw.

`OPERATOR_POST_BLUEPRINT_DECISION` остаётся частью recorded history и не является A11.

## 9. Post-blueprint validation gate

Активный independent-review protocol:

- [Independent Architecture Review Protocol RU](./INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md)
- [English protocol](./INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md)
- identity: `nk-independent-architecture-review/1`

Current sequence:

```text
INDEPENDENT_ARCHITECTURE_REVIEW
→ REVIEW_FINDING_RECONCILIATION
→ BPV-1 bounded cross-lineage falsification
→ A10 outcome classification
→ integrated re-review
→ separate later operator Canon/runtime decision
```

Сам факт существования protocol не означает completed independent review. BPV-1 остаётся blocked до qualifying independent review и reconciliation.