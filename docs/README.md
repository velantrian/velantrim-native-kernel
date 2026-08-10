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
| [`A1_KERNEL_PURPOSE_AND_NON_GOALS.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) | A1 drafted / provisional |
| [`A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md`](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) | A2 drafted / provisional |
| [`A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md`](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) | A3 drafted / provisional |
| [`A4_SEMANTIC_LAWS_AND_INVARIANTS.md`](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md) | A4 drafted / provisional |
| [`A5_IDENTITY_TIME_AND_CHANGE.md`](./A5_IDENTITY_TIME_AND_CHANGE.md) | A5 drafted / provisional |
| [`A5_IDENTITY_TIME_AND_CHANGE.ru.md`](./A5_IDENTITY_TIME_AND_CHANGE.ru.md) | Russian A5 |
| [`A6_KNOWLEDGE_LIFECYCLE.md`](./A6_KNOWLEDGE_LIFECYCLE.md) | A6 drafted / provisional |
| [`A6_KNOWLEDGE_LIFECYCLE.ru.md`](./A6_KNOWLEDGE_LIFECYCLE.ru.md) | Russian A6 |
| [`A7_CONFLICT_UNCERTAINTY_AND_REVISION.md`](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) | A7 drafted / provisional |
| [`A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md`](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md) | Russian A7 |
| [`A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md`](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) | A8 drafted / provisional |
| [`A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md`](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md) | Russian A8 |
| [`../AGENTS.md`](../AGENTS.md) | mandatory repository instructions |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | compact AI continuity state |
| [`ai/KNOWN_RISKS.md`](./ai/KNOWN_RISKS.md) | active risks |
| [`adr/README.md`](./adr/README.md) | accepted/proposed decisions |
| [`../evidence/c5/README.md`](../evidence/c5/README.md) | immutable evidence boundaries |
| [`QUICKSTART.md`](./QUICKSTART.md) | reference-laboratory setup/tests |
| [`GLOSSARY.md`](./GLOSSARY.md) | onboarding terminology; provisional A2–A8 blueprint distinctions take precedence during integrated review |

## Reading order

```text
STATUS + project-state
→ active ROADMAP
→ Architecture Re-foundation plan
→ A1–A8 provisional blueprint deliverables
→ relevant Canon and ADRs
→ only then reference runtime, tests and evidence
```

## Current map

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY
R architecture re-foundation: ACTIVE / BLUEPRINT-FIRST

blueprint content: A1-A8 DRAFTED / PROVISIONAL
next content slice: A9 REFERENCE LABORATORY BOUNDARY
kernel runtime: C4
operational validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production: NOT AUTHORIZED
```

A4 law-set candidate is `nk-semantic-laws/A4-draft-1` with 28 provisional laws. A5 candidate is `nk-identity-time-change/A5-draft-1`. A6 candidate is `nk-knowledge-lifecycle/A6-draft-1`. A7 candidate is `nk-conflict-uncertainty-revision/A7-draft-1`. A8 candidate is `nk-substrate-independence/A8-draft-1`, defining explicit preservation/loss mappings, multidimensional equivalence, scoped conformance and the boundary `substrate-independent specification ≠ universal portability proof`.

## Active sequence

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Knowledge and Memory Ontology              DRAFTED / PROVISIONAL
→ A3 Abstract Native Kernel Machine             DRAFTED / PROVISIONAL
→ A4 Semantic Laws and Invariants               DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        DRAFTED / PROVISIONAL
→ A7 Conflict / Uncertainty / Revision          DRAFTED / PROVISIONAL
→ A8 Substrate-independence Contract            DRAFTED / PROVISIONAL
→ A9 Reference Laboratory Boundary              NEXT BOUNDED SLICE
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ separate operator decision before runtime expansion
```

ADR-0025 preserves the current implementation as a bounded laboratory and freezes semantic/runtime expansion. Issue #18 remains `PENDING_OPERATOR`; Issue #74 / ADR-0024 remains `PROPOSED / PENDING_OPERATOR`; ADR-0003 remains `PROPOSED / NOT_STARTED`.

## Required distinctions

```text
reference laboratory ≠ final architecture
blueprint documentation ≠ implementation evidence
Architecture ≠ implementation
representation ≠ represented reality
Observation ≠ Claim
Claim ≠ Truth
Evidence ≠ Source
Repetition ≠ Evidence
Belief ≠ Knowledge
Memory ≠ merely a stored Record
retrieval relevance ≠ epistemic validity
Unknown ≠ False
Unsupported ≠ False
Conflict ≠ necessarily Contradiction
Detection ≠ Resolution
Resolution-for-scope ≠ Objective Truth
Uncertainty ≠ one universal confidence scalar
confidence score ≠ Evidence
semantic identity ≠ storage identity
equal bytes/hash/text ≠ universal semantic identity
write order ≠ occurrence order ≠ observation order ≠ causal order ≠ semantic precedence
Revision ≠ overwrite
Supersession ≠ deletion or falsity
restriction ≠ logical erasure ≠ physical deletion ≠ cryptographic erasure ≠ forgetting
transition ≠ Event envelope
transition relation ≠ reducer
history visibility ≠ mandatory Event sourcing
profile conformance ≠ production authorization
physical identity ≠ semantic equivalence
same output ≠ full semantic equivalence
substrate-independent specification ≠ universal portability proof
C5 PASS ≠ production readiness
public repository ≠ open-source license
```

Current technologies remain replaceable research instruments, not Architecture Canon.