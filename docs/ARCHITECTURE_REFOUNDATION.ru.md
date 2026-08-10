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

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) / [EN](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md). Определяет Kernel problem, durable qualities, non-goals и ecosystem boundaries.

### A2 — Knowledge and Memory Ontology

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md) / [EN](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md). Определяет technology-neutral semantic distinctions, не превращая current storage/runtime representations в Canon.

### A3 — Абстрактная машина Native Kernel

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md) / [EN](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md). Определяет provisional meaning-level configuration facets, transition families, failure/indeterminacy handling, Authority boundaries, order/concurrency и contrasting substrate mappings. `transition ≠ Event envelope`; `State ≠ reducer output` universally.

### A4 — Semantic Laws and Invariants

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md) / [EN](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md). Candidate `nk-semantic-laws/A4-draft-1` содержит 28 provisional laws, защищающих representation/epistemic boundaries, Context/Provenance/Authority, identity/time/change, conflict/uncertainty, views/accountability и substrate/conformance distinctions.

### A5 — Модель Identity, Time и Change

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A5_IDENTITY_TIME_AND_CHANGE.ru.md) / [EN](./A5_IDENTITY_TIME_AND_CHANGE.md). Candidate `nk-identity-time-change/A5-draft-1` делает identity typed/scoped relation, отделяет semantic от substrate-local identity, различает materially relevant temporal/order relations и требует explicit lineage/loss при migration/revision.

### A6 — Knowledge Lifecycle

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A6_KNOWLEDGE_LIFECYCLE.ru.md) / [EN](./A6_KNOWLEDGE_LIFECYCLE.md). Candidate `nk-knowledge-lifecycle/A6-draft-1` моделирует lifecycle как non-linear graph meaning-level positions/transitions, а не один storage-state pipeline; Event sourcing не universalized.

### A7 — Conflict, Uncertainty и Revision Model

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md) / [EN](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md). Candidate `nk-conflict-uncertainty-revision/A7-draft-1` сохраняет tension kind, assessment status и resolution status независимыми; сохраняет typed uncertainty, unresolved plurality, scoped resolution, revision lineage и reopening без выбора universal winner algorithm.

### A8 — Substrate-independence Contract

**Status:** `DRAFTED / PROVISIONAL` — [RU](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md) / [EN](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md). Ожидает independent review и integrated A1–A10 review.

A8 вводит candidate model `nk-substrate-independence/A8-draft-1` и отвечает, что radically different implementations обязаны сохранять, чтобы оставаться сравнимыми как реализации Native Kernel.

Provisional mapping relation:

```text
SUBSTRATE_MAPPING(
  profile,
  architecture_obligation,
  realization_or_equivalent,
  preservation_state,
  context_and_scope,
  observable_check,
  declared_loss_or_none,
  uncertainty,
  authority_for_claim
)
```

Preservation states: `PRESERVED`, `PARTIAL`, `UNSUPPORTED`, `INDETERMINATE`, `LOSSY`. Это mapping states, не assertion-map arithmetic. Known inability сохранить materially required distinction обязана ослаблять или ломать conformance claim, а не silently approximated.

A8 определяет десять provisional preservation obligations (`A8-P01`…`A8-P10`), охватывающих A2 ontology distinctions, A3 transition semantics, A4 laws, A5 identity/time/order, A6 lifecycle/history, A7 conflict/uncertainty/revision, Context/Provenance/Source/Authority, bounded accountability и explicit capability/loss declarations.

Он различает:

```text
PHYSICAL_IDENTITY
REPRESENTATION_EQUIVALENCE
SEMANTIC_OBLIGATION_EQUIVALENCE
BEHAVIORAL_CONFORMANCE_FOR_SCOPE
LINEAGE_CONTINUITY_EQUIVALENCE
```

Physical identity не является ни необходимым, ни достаточным условием semantic equivalence. Equal bytes/hashes/output сами по себе не доказывают semantic equivalence, а different IDs/encodings/carriers сами по себе не доказывают non-equivalence.

A8 допускает разные physical memory, layouts, languages, data structures, persistence, synchronization, parallelism, time representation, uncertainty representation и hardware, если required meaning сохраняется. Он не требует SQL, JSON, SHA-256, Event sourcing, reducers, global sequence numbers, synchronized wall clocks, LLM, embeddings, Python, network, cloud, silicon, RAM или одной processor model.

Scoped conformance outcomes: `FULL_CONFORMANCE_FOR_SCOPE`, `BOUNDED_CONFORMANCE`, `NON_CONFORMANT_FOR_SCOPE`, `INDETERMINATE_CONFORMANCE`.

```text
substrate-independent specification
≠ universal portability proof
```

A8 не утверждает, что neuromorphic, analog, quantum или arbitrary future implementation уже существует или conforms. Detailed grading P1–C5 намеренно deferred к A9.

**First-draft completion test:** выполнен для bounded drafting scope: для двух radically different implementations reviewer может определить, какие meaning obligations должны preserved, отличить representation/physical equality от semantic equivalence, увидеть explicit degradation и scope conformance claim без PostgreSQL schemas, Python classes, JSON bytes, Event sourcing или одной processor model. Final acceptance всё ещё требует independent и integrated review.

### A9 — Граница Reference Laboratory

**Status:** `NEXT BOUNDED SLICE`.

Классифицировать **Python + PostgreSQL + SQLite** P1–C5 mechanisms против A1–A8: что является architecture-preserving evidence, что partial, что profile-specific, что falsification instrument, а что не architecture requirement. Ничего не удаляется/переписывается только из-за profile-specific classification.

### A10 — Open Questions и Falsification Criteria

Зафиксировать unresolved architecture questions и evidence, способное weaken/refute major hypotheses, включая limits cross-substrate equivalence, minimum history/accountability equivalents, analog/neuromorphic continuity, forgetting без forbidden retention и unresolved conformance boundaries.

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
→ A9 Reference Laboratory Boundary              NEXT BOUNDED SLICE
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ separate operator decision before runtime expansion
```

Later slices могут refine earlier drafts только явно; они не могут silently redefine их.

## 5. Research method

Каждый deliverable должен содержать definitions, non-equivalences, candidate formal model, counterexamples/failure cases, unresolved questions, mapping к existing contracts/runtime, contrasting substrate mappings, review status и evidence boundary.

Sources, papers, existing systems и AI analysis являются inputs и не становятся Canon автоматически.

## 6. Runtime freeze policy

Разрешены architecture research; integrity/security/reproducibility/provenance repair; evidence preservation; current-truth/validator repair; historical recovery; isolated falsification experiments без runtime promotion.

Не разрешены без separate operator decision: new semantic runtime features, reducer v2, new Event vocabulary, new databases/language profiles/model adapters/ecosystem integrations, executable NK-EPI/Temporal/full Admission, operational deletion expansion, maturity promotion или production authorization.

## 7. Связь с existing contracts и pending decisions

A8 не меняет ADR statuses или historical evidence. Issue #14/#15/#16/#17 сохраняют existing scopes. Issue #18 остаётся operator-controlled для license/publication. Issue #74 / ADR-0024 остаётся `PROPOSED / PENDING_OPERATOR`; reducer v1 immutable, reducer-v2 unauthorized. ADR-0003 остаётся `PROPOSED / NOT_STARTED`. Track H source admission остаётся operator-controlled.

```text
A1-A8 blueprint obligations
→ A9 reference-laboratory classification
→ A10 open questions / falsification
→ integrated review
→ existing contracts reconciled within declared scope
≠ silent retroactive rewrite
```

## 8. Gate завершения blueprint

Blueprint не завершён только из-за наличия документов. Gate завершения blueprint требует всех A1–A10 deliverables, terminology reconciliation, explicit contradictions/unknowns, labelled implementation assumptions, falsification criteria, existing-contract mapping, contrasting substrate thought experiments, critical review, integrated review и separate operator decision для next phase.

## 9. Текущий прогресс

```text
Architecture Re-foundation decision: established by ADR-0025
Blueprint plan: this document
Blueprint content: A1-A8 DRAFTED / PROVISIONAL; A9-A10 NOT YET COMPLETE
Next bounded slice: A9 REFERENCE LABORATORY BOUNDARY
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

Drafting A1–A8 не устанавливает independent approval, integrated Canon, runtime implementation, arbitrary future-substrate support или production readiness.