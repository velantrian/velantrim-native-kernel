# 📍 Native Kernel Current State

```yaml
document_role: CURRENT_STATE
status_as_of: 2026-08-10
authoritative_machine_source: ../../project-state.json
machine_protocol: nk-project-state/2
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
live_head_source: GitHub API or checked-out Git ref
machine_truth_reconciliation_merge: d9eee591de308a689ace940c2efe58c9e8a137f2
human_truth_reconciliation_merge: 07549a0cd952b4e06b61ef24d21b2dcdbc9f861d
publication_checkpoint: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
runtime_checkpoint: 675aa4b398a2fc0181dc71d38904a2d33a09f5f8
runtime_integrity_checkpoint: a1cdc6d8f36d67f40f065641809bc6da463c10a4
evidence_producing_checkpoint: 296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
manifest_generated_from: 70acd0da61fee19131947aa56125833adb156ced
notion_synchronized_through: 70acd0da61fee19131947aa56125833adb156ced
active_architecture_decision: ADR-0025
active_architecture_issue: 88
```

> This page contains current repository truth only. Historical implementation and review chronology remains available through linked records and Git history.

## Current boundary

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

```text
C5 bounded rehearsal ≠ production readiness
repository-resident evidence ≠ independent custody
logical ERASED ≠ physical deletion
public repository ≠ open-source license
```

No AI agent may select the license or accept ADR-0024 for the operator.

The later Notion synchronization checkpoint does not rewrite or replace the earlier publication checkpoint.

## Active architecture priority

```text
Architecture Re-foundation: ACTIVE / BLUEPRINT-FIRST
No new semantic/runtime expansion before blueprint gate completion.
```

ADR-0025 is `ACCEPTED / DOCUMENTED / PARTIAL / OPERATOR APPROVED`.

The existing P1–C5 clean implementation is preserved as a:

```text
BOUNDED REFERENCE LABORATORY
not architectural authority
not the final Native Kernel definition
```

Plan and drafted content:

- [Architecture Re-foundation — English](../ARCHITECTURE_REFOUNDATION.md)
- [Переоснование архитектуры — Русский](../ARCHITECTURE_REFOUNDATION.ru.md)
- [ADR-0025](../adr/0025-blueprint-before-runtime-expansion.md)
- [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88)
- [A1 — Kernel Purpose and Non-goals — English](../A1_KERNEL_PURPOSE_AND_NON_GOALS.md)
- [A1 — Purpose и Non-goals Kernel — Русский](../A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md)
- [A2 — Knowledge and Memory Ontology — English](../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md)
- [A2 — Онтология знания и памяти — Русский](../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md)
- [A3 — Abstract Native Kernel Machine — English](../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md)
- [A3 — Абстрактная машина Native Kernel — Русский](../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md)

Required sequence:

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Knowledge and Memory Ontology              DRAFTED / PROVISIONAL
→ A3 Abstract Native Kernel Machine             DRAFTED / PROVISIONAL
→ A4 Semantic Laws and Invariants               NEXT BOUNDED SLICE
→ A5 Identity / Time / Change
→ A6 Knowledge Lifecycle
→ A7 Conflict / Uncertainty / Revision
→ A8 Substrate-independence Contract
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ separate operator decision before runtime expansion
```

The blueprint content A1–A3 is `DRAFTED / PROVISIONAL` and remains pending independent review plus integrated review with A4–A10. The next bounded content slice is `A4 — Semantic Laws and Invariants`.

A2 provisionally distinguishes Signal, Observation, Record, Proposition, Claim, Interpretation, Hypothesis, Belief, Knowledge, Memory, Evidence, Source, Provenance, Context, Relation, State, Change, Event, Conflict, Contradiction, Uncertainty, Revision, Supersession, Authority, and Receipt without copying current Python classes, SQL schemas, or Event-sourced laboratory mechanics into Canon.

A3 provisionally defines a scoped obligation-and-transition machine with thirteen logical configuration facets and thirteen transition families. It preserves abstract machine ≠ runtime implementation, transition ≠ Event envelope, transition relation ≠ reducer, history visibility ≠ mandatory Event sourcing, admission ≠ truth, and profile conformance ≠ production authorization.

## Runtime freeze boundary

Allowed:

- architecture and ontology research;
- integrity, security, reproducibility, and provenance fixes;
- evidence preservation;
- validator and current-truth repair;
- historical recovery;
- isolated experiments that falsify a blueprint assumption without runtime promotion.

Not authorized:

- reducer v2 or new semantic Event verbs;
- new databases, language ports, LLM/vector adapters, or ecosystem integrations;
- executable NK-EPI, Temporal, full Admission, or operational deletion;
- performance-driven semantic changes;
- maturity or production promotion.

## Three independent tracks

```text
H — Historical Recovery
  authentic v0.1.2.1 + original 44 tests
  BLOCKED / ACTIVE EVIDENCE-RECOVERY
  NOT_FOUND_IN_ACCESSIBLE_SOURCES

C — Clean Reference Implementation
  P1–P5 + C4 + C5
  PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY

R — Architecture Re-foundation
  A1–A10 blueprint
  ACTIVE / BLUEPRINT-FIRST / NO AUTOMATIC RUNTIME PROMOTION
```

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
blueprint documentation ≠ implementation evidence
future-facing design ≠ demonstrated future substrate support
```

## Checkpoint model

```text
GitHub API / checked-out ref
        ↓ resolves live HEAD

project-state.json
        ↓ records verified checkpoint roles and active research phase

runtime checkpoint
runtime-integrity checkpoint
evidence-producing checkpoint
publication checkpoint
Notion synchronized descendant checkpoint
```

The publication checkpoint remains `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c`. The latest repository-committed Notion synchronization checkpoint remains `70acd0da61fee19131947aa56125833adb156ced` from PR #86. This repository state does not predict its own future corrective merge SHA or claim that a future post-merge Notion reconciliation already occurred.

A descendant commit does not invalidate earlier evidence, but it also does not broaden that evidence or rewrite an earlier publication identity.

## Existing runtime boundary

```text
P1 semantic core:                    MERGED / REPOSITORY-TESTED
P2 PostgreSQL append:                MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay, projection and Receipts:  MERGED / REPOSITORY-INTEGRATION-TESTED
P4 PostgreSQL assertion profile:     MERGED / PARTIAL / C2
P5 SQLite and profile comparison:    MERGED / PARTIAL / C2 + C3
C4 offline shadow evaluation:        MERGED / PARTIAL
C5 bounded operational rehearsal:    MERGED / PARTIAL / SYNTHETIC
```

The current SQLite WAL floor remains linked SQLite `3.51.3`. Historical SQLite `3.45.1` evidence remains immutable and version-bound.

## Independent pending decisions

| Decision | State | Effect |
|---|---|---|
| Issue #18 — license/publication terms | `PENDING_OPERATOR / selected_option: null` | no license change; external contributions and package publication remain unauthorized |
| Issue #74 / ADR-0024 — reducer referential semantics | `PROPOSED / PENDING_OPERATOR / selected_option: null` | reducer v1 remains immutable; reducer-v2 remains unauthorized |

Architecture Re-foundation can proceed without deciding either one. Issue #18 still gates open publication/collaboration terms. ADR-0024 still gates reducer-v2 if that path is reopened after blueprint review.

## Current known gaps

- `A1`, `A2`, and `A3` are drafted/provisional and remain pending independent plus integrated blueprint review;
- A2 primitive/derived/open classifications are hypotheses, not final Canon;
- A3 is a provisional abstract-machine proposal, not final Canon or runtime evidence;
- semantic laws remain the next bounded architecture slice and are not yet a reconciled formal A4 set;
- identity, time, change, lifecycle, conflict, uncertainty, and revision models remain partial;
- substrate-independence obligations and falsification criteria remain incomplete;
- Glossary and older architecture prose still contain laboratory-shaped compact definitions that require later integrated reconciliation, not silent rewriting in A2/A3;
- reducer v1 has known referential gaps, but runtime work is frozen;
- current PostgreSQL and SQLite profiles share Python semantic lineage;
- NK-EPI assertions have no executable support;
- physical/cryptographic deletion and production operations remain absent.

## Machine-readable state

```text
project-state.json
contracts/project-state-v2.schema.json
contracts/registry.json
tools/ai_context/validate_project_state.py
tools/ai_context/validate_reconciliation.py
tools/ai_context/validate_architecture_freeze.py
tools/ai_context/validate_context.py
```

GitHub remains authoritative for live refs, issues, PRs, Actions, code, contracts, tests, and evidence. Notion carries orientation and history and must be synchronized only after confirmed merge results.

## Historical records

- [`C5_IMPLEMENTATION_RECORD.md`](C5_IMPLEMENTATION_RECORD.md)
- [`../adr/0023-harden-sqlite-wal-and-event-integrity.md`](../adr/0023-harden-sqlite-wal-and-event-integrity.md)
- [`../../evidence/c5/README.md`](../../evidence/c5/README.md)
- [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)

Historical records are version-bound evidence and chronology, not current-state authority.