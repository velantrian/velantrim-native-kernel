# 📚 Документация Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

> **Текущая граница:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Активная фаза:** `ARCHITECTURE RE-FOUNDATION / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`

## Начать здесь

| Документ | Роль |
|---|---|
| [`../STATUS.md`](../STATUS.md) | authoritative human current state |
| [`../project-state.json`](../project-state.json) | committed machine state (`nk-project-state/2`) |
| [`../ROADMAP.md`](../ROADMAP.md) | active sequence и authorization boundaries |
| [`ARCHITECTURE_REFOUNDATION.ru.md`](./ARCHITECTURE_REFOUNDATION.ru.md) | активный план архитектурного blueprint |
| [`ARCHITECTURE_REFOUNDATION.md`](./ARCHITECTURE_REFOUNDATION.md) | English blueprint plan |
| [`A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) | blueprint deliverable A1 (drafted / provisional) |
| [`A1_KERNEL_PURPOSE_AND_NON_GOALS.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) | English blueprint deliverable A1 |
| [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md) | blueprint deliverable A2 (drafted / provisional) |
| [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) | English blueprint deliverable A2 |
| [`A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md`](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md) | blueprint deliverable A3 (drafted / provisional) |
| [`A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md`](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) | English blueprint deliverable A3 |
| [`A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md`](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md) | blueprint deliverable A4 (drafted / provisional) |
| [`A4_SEMANTIC_LAWS_AND_INVARIANTS.md`](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md) | English blueprint deliverable A4 |
| [`../AGENTS.md`](../AGENTS.md) | обязательные инструкции репозитория |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | компактный AI continuity state |
| [`ai/KNOWN_RISKS.md`](./ai/KNOWN_RISKS.md) | active risks |
| [`adr/README.md`](./adr/README.md) | accepted и proposed decisions |
| [`../evidence/c5/README.md`](../evidence/c5/README.md) | immutable evidence boundaries |
| [`QUICKSTART.ru.md`](./QUICKSTART.ru.md) | setup и tests reference laboratory |
| [`GLOSSARY.ru.md`](./GLOSSARY.ru.md) | onboarding terminology; provisional distinctions A2–A4 имеют приоритет в blueprint review |

## Порядок чтения

```text
STATUS и project-state
→ active ROADMAP
→ план Architecture Re-foundation
→ provisional deliverables A1, A2, A3 и A4
→ релевантные Canon и ADR
→ только затем reference runtime, tests и evidence
```

Historical implementation records и research proposals читаются только при необходимости; они не переопределяют текущую blueprint phase.

## Текущая карта

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY
R architecture re-foundation: ACTIVE / BLUEPRINT-FIRST

blueprint content: A1-A4 DRAFTED / PROVISIONAL
next content slice: A5 IDENTITY / TIME / CHANGE
kernel runtime: C4
operational validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production: NOT AUTHORIZED
```

A4 law-set candidate: `nk-semantic-laws/A4-draft-1`, сейчас 28 provisional candidate laws. Count reviewable и не означает executable support.

## Активная последовательность

```text
A1 Purpose и Non-goals                           DRAFTED / PROVISIONAL
→ A2 Knowledge and Memory Ontology              DRAFTED / PROVISIONAL
→ A3 Abstract Native Kernel Machine             DRAFTED / PROVISIONAL
→ A4 Semantic Laws and Invariants               DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   NEXT BOUNDED SLICE
→ A6 Knowledge Lifecycle
→ A7 Conflict / Uncertainty / Revision
→ A8 Substrate-independence Contract
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ отдельное operator decision до возобновления runtime expansion
```

ADR-0025 сохраняет существующую Python/PostgreSQL/SQLite реализацию как bounded laboratory и замораживает новое semantic/runtime expansion.

Issue #18 остаётся `PENDING_OPERATOR` для license/publication. ADR-0024 остаётся `PROPOSED / PENDING_OPERATOR` и продолжает блокировать reducer-v2, но не blueprint research.

## Обязательные различия

```text
reference laboratory ≠ final architecture
blueprint documentation ≠ implementation evidence
Observation ≠ Claim
Claim ≠ Truth
Evidence ≠ Source
Repetition ≠ Evidence
Belief ≠ Knowledge
Memory ≠ merely a stored Record
retrieval relevance ≠ epistemic validity
Conflict ≠ necessarily Contradiction
Unknown ≠ False
Event usage in P1-C5 ≠ Event as universal primitive
State ≠ necessarily reducer output
Knowledge ≠ LLM / embeddings / SQL / JSON / specific processor
abstract machine ≠ runtime implementation
transition ≠ Event envelope
transition relation ≠ reducer
history visibility ≠ mandatory Event sourcing
admission ≠ truth
semantic identity ≠ storage identity
write order ≠ represented-world order
Revision ≠ silent overwrite
Supersession ≠ deletion or falsity
Receipt/accountability ≠ correctness or truth
profile conformance ≠ production authorization
C5 PASS ≠ production readiness
logical ERASED ≠ physical deletion
public repository ≠ open-source license
future-facing design ≠ demonstrated future substrate support
```

Current technologies являются заменяемыми research instruments, а не Architecture Canon.
