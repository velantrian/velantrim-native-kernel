# 📚 Native Kernel Documentation

**[English](./README.md) · [Русский](./README.ru.md)**

> **Current boundary:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Active phase:** `ARCHITECTURE RE-FOUNDATION / BLUEPRINT-FIRST / RUNTIME EXPANSION FROZEN`

## Start here

| Document | Role |
|---|---|
| [`../STATUS.md`](../STATUS.md) | authoritative human current state |
| [`../project-state.json`](../project-state.json) | committed machine state (`nk-project-state/2`) |
| [`../ROADMAP.md`](../ROADMAP.md) | active sequence and authorization boundaries |
| [`ARCHITECTURE_REFOUNDATION.md`](./ARCHITECTURE_REFOUNDATION.md) | active blueprint plan |
| [`ARCHITECTURE_REFOUNDATION.ru.md`](./ARCHITECTURE_REFOUNDATION.ru.md) | Russian blueprint plan |
| [`A1_KERNEL_PURPOSE_AND_NON_GOALS.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) | blueprint deliverable A1 (drafted / provisional) |
| [`A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) | Russian blueprint deliverable A1 |
| [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) | blueprint deliverable A2 (drafted / provisional) |
| [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md) | Russian blueprint deliverable A2 |
| [`A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md`](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) | blueprint deliverable A3 (drafted / provisional) |
| [`A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md`](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md) | Russian blueprint deliverable A3 |
| [`A4_SEMANTIC_LAWS_AND_INVARIANTS.md`](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md) | blueprint deliverable A4 (drafted / provisional) |
| [`A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md`](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md) | Russian blueprint deliverable A4 |
| [`../AGENTS.md`](../AGENTS.md) | mandatory repository instructions |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | compact AI continuity state |
| [`ai/KNOWN_RISKS.md`](./ai/KNOWN_RISKS.md) | active risks |
| [`adr/README.md`](./adr/README.md) | accepted and proposed decisions |
| [`../evidence/c5/README.md`](../evidence/c5/README.md) | immutable evidence boundaries |
| [`QUICKSTART.md`](./QUICKSTART.md) | reference-laboratory setup and tests |
| [`GLOSSARY.md`](./GLOSSARY.md) | onboarding terminology; provisional A2–A4 distinctions take precedence for blueprint review |

## Reading order

```text
STATUS and project-state
→ active ROADMAP
→ Architecture Re-foundation plan
→ A1, A2, A3, and A4 provisional blueprint deliverables
→ relevant Canon and ADRs
→ only then reference runtime, tests, and evidence
```

Historical implementation records and research proposals are read only when relevant; they do not override the current blueprint phase.

## Current map

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

A4 law-set candidate: `nk-semantic-laws/A4-draft-1`, currently 28 provisional candidate laws. The count is reviewable and does not imply executable support.

## Active sequence

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
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
→ separate operator decision before runtime expansion
```

ADR-0025 preserves the existing Python/PostgreSQL/SQLite implementation as a bounded laboratory while freezing new semantic/runtime expansion.

Issue #18 remains `PENDING_OPERATOR` for license/publication. ADR-0024 remains `PROPOSED / PENDING_OPERATOR` and continues to block reducer-v2, not blueprint research.

## Required distinctions

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

Current technologies are replaceable research instruments, not Architecture Canon.
