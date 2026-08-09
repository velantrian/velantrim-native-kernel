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
| [`ARCHITECTURE_REFOUNDATION.ru.md`](./ARCHITECTURE_REFOUNDATION.ru.md) | активный план архитектурного чертежа |
| [`ARCHITECTURE_REFOUNDATION.md`](./ARCHITECTURE_REFOUNDATION.md) | English blueprint plan |
| [`A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) | blueprint deliverable A1 (drafted) |
| [`A1_KERNEL_PURPOSE_AND_NON_GOALS.md`](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) | English blueprint deliverable A1 |
| [`../AGENTS.md`](../AGENTS.md) | обязательные инструкции репозитория |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | компактный AI continuity state |
| [`ai/KNOWN_RISKS.md`](./ai/KNOWN_RISKS.md) | active risks |
| [`adr/README.md`](./adr/README.md) | accepted и proposed decisions |
| [`../evidence/c5/README.md`](../evidence/c5/README.md) | immutable evidence boundaries |
| [`QUICKSTART.ru.md`](./QUICKSTART.ru.md) | setup и tests reference laboratory |
| [`GLOSSARY.ru.md`](./GLOSSARY.ru.md) | terminology и обязательные distinctions |

## Порядок чтения

```text
STATUS и project-state
→ active ROADMAP
→ план Architecture Re-foundation
→ релевантные Canon и ADR
→ только затем reference runtime, tests и evidence
```

Historical implementation records и research proposals читаются только при необходимости; они не переопределяют текущую blueprint phase.

## Текущая карта

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY
R architecture re-foundation: ACTIVE / BLUEPRINT-FIRST

kernel runtime: C4
operational validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production: NOT AUTHORIZED
```

## Активная последовательность

```text
A1 Purpose и Non-goals
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
→ отдельное operator decision до возобновления runtime expansion
```

ADR-0025 сохраняет существующую Python/PostgreSQL/SQLite реализацию как bounded laboratory и замораживает новое semantic/runtime expansion.

Issue #18 остаётся `PENDING_OPERATOR` для license/publication. ADR-0024 остаётся `PROPOSED / PENDING_OPERATOR` и продолжает блокировать reducer-v2, но не blueprint research.

## Обязательные различия

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

Current technologies являются заменяемыми research instruments, а не Architecture Canon.
