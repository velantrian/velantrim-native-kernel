# 🧬 Architecture Re-foundation — Blueprint before Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **State:** `ACTIVE / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`  
> **Decision:** [`ADR-0025`](./adr/0025-blueprint-before-runtime-expansion.md)  
> **Issue:** [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88)

## 1. Why this phase exists

Native Kernel studies a technology-neutral architecture for meaning, memory, knowledge, provenance, uncertainty, change and accountability. The existing **Python + PostgreSQL + SQLite** lineage is retained as a bounded reference laboratory rather than promoted into Canon because it exists first.

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
```

## 2. Draft inventory

All ten required blueprint slices exist and remain `DRAFTED / PROVISIONAL`. A10 retains model identity `nk-open-questions-falsification/A10-draft-1`.

1. [A1](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) / [RU](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md)
2. [A2](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) / [RU](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md)
3. [A3](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) / [RU](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md)
4. [A4](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md) / [RU](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md)
5. [A5](./A5_IDENTITY_TIME_AND_CHANGE.md) / [RU](./A5_IDENTITY_TIME_AND_CHANGE.ru.md)
6. [A6](./A6_KNOWLEDGE_LIFECYCLE.md) / [RU](./A6_KNOWLEDGE_LIFECYCLE.ru.md)
7. [A7](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) / [RU](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md)
8. [A8](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) / [RU](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md)
9. [A9](./A9_REFERENCE_LABORATORY_BOUNDARY.md) / [RU](./A9_REFERENCE_LABORATORY_BOUNDARY.ru.md)
10. [A10](./A10_OPEN_QUESTIONS_AND_FALSIFICATION.md) / [RU](./A10_OPEN_QUESTIONS_AND_FALSIFICATION.ru.md)

## 3. Integrated review

The first integrated review is now recorded as:

- [Integrated A1–A10 Review](./INTEGRATED_A1_A10_REVIEW.md)
- [Russian review](./INTEGRATED_A1_A10_REVIEW.ru.md)
- completed gate identity: `INTEGRATED_A1_A10_REVIEW`
- review identity: `nk-integrated-blueprint-review/A1-A10-review-1`
- state: `COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING`

The review explicitly reconciles seven cross-slice findings rather than silently rewriting draft history. Key current provisional interpretations include:

```text
PHYSICALLY_ERASED ≠ CRYPTOGRAPHICALLY_ERASED
FORGOTTEN_OR_LOST does not require a deliberate erasure method
A1 confidence wording → uncertainty + epistemic position
A10 outcome protocol = exactly five declared outcomes
Conflict ≠ necessarily Contradiction
A6 lifecycle positions ≠ mandatory pipeline stages
```

After those explicit reconciliation decisions, the review found no known blocking internal semantic contradiction remaining in this pass. This is not independent validation.

## 4. Reference laboratory boundary

P1–C5 remains `BOUNDED_REFERENCE_LABORATORY`. Python, PostgreSQL, SQLite, SQL, JSON, SHA-256, current Event/reducer/Receipt/sequence mechanisms, CI and evidence packaging remain profile/laboratory mechanisms unless a separate architecture decision establishes otherwise.

```text
useful implementation evidence ≠ architecture requirement
PostgreSQL ↔ SQLite C3 ≠ independent-language equivalence
substrate-independent specification ≠ universal portability proof
```

## 5. Runtime freeze

Allowed while frozen: architecture research; integrity/security/reproducibility/provenance fixes; evidence preservation; truth/validator repair; historical recovery; isolated falsification experiments without runtime promotion.

Not authorized automatically: reducer-v2, new semantic Event verbs, new databases/language profiles/model adapters/integrations, executable NK-EPI/Temporal/full Admission, deletion execution expansion, maturity or production promotion.

## 6. Pending operator-controlled decisions

- Issue #18 license/publication: unchanged / operator-controlled.
- Issue #74 / ADR-0024: `PROPOSED / PENDING_OPERATOR`; reducer-v2 unauthorized.
- ADR-0003: `PROPOSED / NOT_STARTED`.
- Track H source admission: operator-controlled.

## 7. Current progress

```text
Blueprint content: A1-A10 DRAFTED / PROVISIONAL
Integrated review: COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING
Next bounded gate: OPERATOR_POST_BLUEPRINT_DECISION
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
Independent architectural validation: NOT ESTABLISHED
```

## 8. Blueprint completion gate

The draft inventory and first integrated review are complete as provisional architecture work. Acceptance is still not automatic: `OPERATOR_POST_BLUEPRINT_DECISION` is the next gate, not A11 and not runtime permission. The integrated review does not choose the next phase.
