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
| [`../AGENTS.md`](../AGENTS.md) | mandatory repository instructions |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | compact AI continuity state |
| [`ai/KNOWN_RISKS.md`](./ai/KNOWN_RISKS.md) | active risks |
| [`adr/README.md`](./adr/README.md) | accepted and proposed decisions |
| [`../evidence/c5/README.md`](../evidence/c5/README.md) | immutable evidence boundaries |
| [`QUICKSTART.md`](./QUICKSTART.md) | reference-laboratory setup and tests |
| [`GLOSSARY.md`](./GLOSSARY.md) | terminology and required distinctions |

## Reading order

```text
STATUS and project-state
→ active ROADMAP
→ Architecture Re-foundation plan
→ relevant Canon and ADRs
→ only then reference runtime, tests, and evidence
```

Historical implementation records and research proposals are read only when relevant; they do not override the current blueprint phase.

## Current map

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY
R architecture re-foundation: ACTIVE / BLUEPRINT-FIRST

kernel runtime: C4
operational validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 / 0 / 8 / 0
production: NOT AUTHORIZED
```

## Active sequence

```text
A1 Purpose and Non-goals
→ A2 Knowledge and Memory Ontology
→ A3 Abstract Native Kernel Machine
→ A4 Semantic Laws and Invariants
→ A5 Identity / Time / Change
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
PostgreSQL + SQLite ≠ full substrate neutrality
C5 PASS ≠ production readiness
Unknown ≠ False
admission ≠ truth
logical ERASED ≠ physical deletion
public repository ≠ open-source license
future-facing design ≠ demonstrated future substrate support
```

Current technologies are replaceable research instruments, not Architecture Canon.
