# 🧬 Переоснование архитектуры — Blueprint before Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **State:** `ACTIVE / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`  
> **Decision:** [`ADR-0025`](./adr/0025-blueprint-before-runtime-expansion.md)  
> **Issue:** [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Граница evidence:** только architecture research/governance; без runtime, evidence, maturity или production promotion

## 1. Зачем нужна эта фаза

Native Kernel должен сохранять meaning, memory, knowledge, provenance, uncertainty, Change и accountability независимо от одного current technology stack. Существующая линия **Python + PostgreSQL + SQLite** сохраняется как bounded reference laboratory, но не становится permanent Canon только потому, что появилась первой.

```text
meaning / ontology / laws
        ↓
abstract Kernel machine
        ↓
identity / time / lifecycle / conflict models
        ↓
substrate-independence contract
        ↓
reference-laboratory boundary
        ↓
open questions / falsification
        ↓
integrated review + separate operator decision
```

## 2. Граница фазы

Этой фазе принадлежат ontology, semantic laws, abstract-machine obligations, identity/time/change, lifecycle, conflict/uncertainty/revision, substrate-independent obligations, mapping reference profiles, explicit unknowns и falsification criteria.

Ей не принадлежат new reducer, Event vocabulary, database, language port, LLM/vector adapter, product integration, performance-driven semantic change, production deployment или proof, что arbitrary future substrates уже conform.

## 3. Обязательные deliverables

### A1 — Purpose и Non-goals Kernel
**Status:** `DRAFTED / PROVISIONAL` — [RU](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) / [EN](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md).

### A2 — Knowledge and Memory Ontology
**Status:** `DRAFTED / PROVISIONAL` — [RU](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md) / [EN](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md).

### A3 — Абстрактная машина Native Kernel
**Status:** `DRAFTED / PROVISIONAL` — [RU](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md) / [EN](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md).

### A4 — Semantic Laws and Invariants
**Status:** `DRAFTED / PROVISIONAL` — [RU](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md) / [EN](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md). Candidate `nk-semantic-laws/A4-draft-1` содержит 28 provisional laws.

### A5 — Модель Identity, Time и Change
**Status:** `DRAFTED / PROVISIONAL` — [RU](./A5_IDENTITY_TIME_AND_CHANGE.ru.md) / [EN](./A5_IDENTITY_TIME_AND_CHANGE.md). Candidate `nk-identity-time-change/A5-draft-1`.

### A6 — Knowledge Lifecycle
**Status:** `DRAFTED / PROVISIONAL` — [RU](./A6_KNOWLEDGE_LIFECYCLE.ru.md) / [EN](./A6_KNOWLEDGE_LIFECYCLE.md). Candidate `nk-knowledge-lifecycle/A6-draft-1`.

### A7 — Conflict, Uncertainty и Revision Model
**Status:** `DRAFTED / PROVISIONAL` — [RU](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md) / [EN](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md). Candidate `nk-conflict-uncertainty-revision/A7-draft-1`.

### A8 — Substrate-independence Contract
**Status:** `DRAFTED / PROVISIONAL` — [RU](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md) / [EN](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md). Candidate `nk-substrate-independence/A8-draft-1` определяет сохранение meaning-level obligations, а не physical sameness. `substrate-independent specification ≠ universal portability proof`.

### A9 — Граница Reference Laboratory

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A9_REFERENCE_LABORATORY_BOUNDARY.ru.md) / [EN](./A9_REFERENCE_LABORATORY_BOUNDARY.md). Candidate `nk-reference-laboratory-boundary/A9-draft-1`.

A9 классифицирует P1–C5 mechanisms относительно A1–A8 через шесть scoped roles:

```text
ARCHITECTURE_PRESERVING_EVIDENCE
PROFILE_SPECIFIC_REALIZATION
PARTIAL_ARCHITECTURE_COVERAGE
FALSIFICATION_INSTRUMENT
LABORATORY_ONLY_CONSTRAINT
NOT_ARCHITECTURE_EVIDENCE
```

Один mechanism может иметь несколько roles. Current Python/PostgreSQL/SQLite/Event/reducer/Receipt/hash/sequence/CI mechanisms сохраняют validity внутри accepted versioned laboratory contracts, не становясь universal Canon.

P5/C3 — реальное, но узкое evidence replaceable storage-profile realization внутри общей Python/conventional-digital lineage:

```text
PostgreSQL ↔ SQLite C3
= useful cross-profile evidence
≠ independent-language equivalence
≠ independent-computation-model equivalence
≠ arbitrary-substrate portability proof
```

A9 также устанавливает preservation rule:

```text
profile-specific
→ label correctly
→ preserve reproducibility
→ keep evidence lineage
→ prevent silent Canon promotion
≠ delete or rewrite automatically
```

P4/C4/C5 остаются полезными measurement/falsification instruments; C5 остаётся synthetic bounded operational evidence, а не production или independent-custody evidence.

**First-draft completion test:** выполнен для principal P1–C5 mechanisms. Reviewer может определить A1–A8 obligation, A9 role, actual proof boundary, non-proof boundary и понять, обязана ли замена mechanism изменить meaning Native Kernel.

### A10 — Open Questions и Falsification Criteria

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A10_OPEN_QUESTIONS_AND_FALSIFICATION.ru.md) / [EN](./A10_OPEN_QUESTIONS_AND_FALSIFICATION.md). Candidate `nk-open-questions-falsification/A10-draft-1`.

A10 фиксирует major unproved hypotheses, falsifiers, weakening conditions, open questions, evidence-independence dimensions, contrasting substrate thought experiments и stop conditions. Он различает `SUPPORTED_FOR_SCOPE`, `WEAKENED`, `REFUTED`, `INDETERMINATE`, `NOT_TESTED`; это research outcomes, а не замена P4/A8 states.

A10 явно включает minimum non-event-sourced history/accountability, reconstruction без exact replay, lossy identity continuity, independent-language evidence thresholds, analog/neuromorphic persistence, probabilistic conformance, forgetting/physical-deletion observability, bounded-memory auditability, decentralized Authority, non-classical computation и evidence independence.

**First-draft completion test:** выполнен как falsification/open-question inventory. Гипотезы этим не доказаны. Final acceptance всё ещё требует integrated A1–A10 review и отдельного operator decision.

## 4. Последовательность работы

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Ontology                                   DRAFTED / PROVISIONAL
→ A3 Abstract Machine                           DRAFTED / PROVISIONAL
→ A4 Semantic Laws                              DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        DRAFTED / PROVISIONAL
→ A7 Conflict / Uncertainty / Revision          DRAFTED / PROVISIONAL
→ A8 Substrate-independence Contract            DRAFTED / PROVISIONAL
→ A9 Reference Laboratory Boundary              DRAFTED / PROVISIONAL
→ A10 Open Questions and Falsification           DRAFTED / PROVISIONAL
→ integrated A1-A10 review                     NEXT GATE
→ separate operator decision before runtime expansion
```

Later review может refine earlier drafts только явно; он не может silently redefine их.

## 5. Research method

Каждый deliverable должен содержать definitions, non-equivalences, candidate formal model, counterexamples/failure cases, unresolved questions, mapping к existing contracts/runtime, contrasting substrate mappings, review status и evidence boundary.

Sources, papers, existing systems и AI analysis являются inputs и не становятся Canon автоматически.

## 6. Runtime freeze policy

Разрешены architecture research; integrity/security/reproducibility/provenance repair; evidence preservation; current-truth/validator repair; historical recovery; isolated falsification experiments без runtime promotion.

Не разрешены без separate operator decision: new semantic runtime features, reducer v2, new Event vocabulary, new databases/language profiles/model adapters/ecosystem integrations, executable NK-EPI/Temporal/full Admission, operational deletion expansion, maturity promotion или production authorization.

## 7. Связь с existing contracts и pending decisions

A10 не меняет ADR statuses или historical evidence. Issue #14/#15/#16/#17 сохраняют existing scopes. Issue #18 остаётся operator-controlled для license/publication. Issue #74 / ADR-0024 остаётся `PROPOSED / PENDING_OPERATOR`; reducer v1 immutable, reducer-v2 unauthorized. ADR-0003 остаётся `PROPOSED / NOT_STARTED`. Track H source admission остаётся operator-controlled.

```text
A1-A10 drafted blueprint
→ integrated A1-A10 review
→ existing contracts reconciled within declared scope
→ separate operator decision
≠ silent retroactive rewrite
≠ automatic runtime thaw
```

## 8. Gate завершения blueprint

Blueprint не завершён только из-за наличия документов. Draft inventory теперь содержит все A1–A10 deliverables, но blueprint acceptance по-прежнему требует terminology reconciliation, explicit contradictions/unknowns, labelled implementation assumptions, falsification coverage, existing-contract mapping, contrasting substrate thought experiments, critical integrated review и separate operator decision для любой next phase.

## 9. Текущий прогресс

```text
Architecture Re-foundation decision: established by ADR-0025
Blueprint plan: this document
Blueprint content: A1-A10 DRAFTED / PROVISIONAL
Next bounded gate: INTEGRATED_A1_A10_REVIEW
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

Drafting A1–A10 не устанавливает independent approval, integrated Canon, runtime implementation, arbitrary future-substrate support или production readiness.
