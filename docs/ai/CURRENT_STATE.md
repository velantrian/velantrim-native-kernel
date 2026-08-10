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

This file must not predict its own future merge SHA. GitHub live refs remain authoritative for `main`, PR heads, Actions, reviews and merge state.

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

The later Notion synchronization checkpoint does not rewrite or replace the earlier publication checkpoint. The repository-committed Notion synchronization checkpoint remains `70acd0da61fee19131947aa56125833adb156ced` from PR #86.

## Active architecture priority

```text
Architecture Re-foundation: ACTIVE / BLUEPRINT-FIRST
No new semantic/runtime expansion before blueprint gate completion.
```

The existing P1–C5 clean implementation remains a:

```text
BOUNDED REFERENCE LABORATORY
not architectural authority
not the final Native Kernel definition
```

The blueprint content A1–A6 is `DRAFTED / PROVISIONAL` and remains pending independent plus integrated A1–A10 review. The next bounded content slice is `A7 — Conflict, Uncertainty, and Revision`.

Required sequence:

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Knowledge and Memory Ontology              DRAFTED / PROVISIONAL
→ A3 Abstract Native Kernel Machine             DRAFTED / PROVISIONAL
→ A4 Semantic Laws and Invariants               DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        DRAFTED / PROVISIONAL
→ A7 Conflict / Uncertainty / Revision          NEXT BOUNDED SLICE
→ A8 Substrate-independence Contract
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ separate operator decision before runtime expansion
```

Drafted content:

- [A1 EN](../A1_KERNEL_PURPOSE_AND_NON_GOALS.md) / [RU](../A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md)
- [A2 EN](../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) / [RU](../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md)
- [A3 EN](../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) / [RU](../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md)
- [A4 EN](../A4_SEMANTIC_LAWS_AND_INVARIANTS.md) / [RU](../A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md)
- [A5 EN](../A5_IDENTITY_TIME_AND_CHANGE.md) / [RU](../A5_IDENTITY_TIME_AND_CHANGE.ru.md)
- [A6 EN](../A6_KNOWLEDGE_LIFECYCLE.md) / [RU](../A6_KNOWLEDGE_LIFECYCLE.ru.md)

## A6 candidate truth

`nk-knowledge-lifecycle/A6-draft-1` is a provisional meaning-level model. It defines the knowledge lifecycle as a labeled directed graph of nine recurring phases rather than a linear pipeline:

```text
ENCOUNTERED / RETAINED / POSITIONED / EPISTEMICALLY_WEIGHED / RELATIONALLY_INTEGRATED / IN_TENSION / REVISED_OR_SUPERSEDED / DISPOSED / ACCOUNTED
```

Each phase maps to one or more of A3's thirteen transition families; `DERIVE_BOUNDED_VIEW` and `SELECT_FOR_USE` are phase-referencing, not phase-changing. A typed `LIFECYCLE_TRANSITION` relation reuses A3's outcome vocabulary (`APPLIED`/`NO_CHANGE`/`QUARANTINED`/`REJECTED`/`PARTIAL`/`UNKNOWN`/`UNSUPPORTED`/`FAILED`) rather than inventing new terms.

A6 also separates:

```text
LIFECYCLE_TRANSITION_ORDER ≠ OCCURRENCE_ORDER ≠ CAUSAL_DEPENDENCY_ORDER ≠ LOCAL_WRITE_COMMIT_ORDER
```

and extends A3's eight dispositions with three closure kinds — `LOGICALLY_ERASED`, `PHYSICALLY_OR_CRYPTOGRAPHICALLY_ERASED`, `FORGOTTEN_OR_LOST` — resolving the erasure/forgetting distinctions A5 named but deferred.

Existing contracts are preserved rather than silently rewritten:

- the illustrative P1–C5 Event-to-phase mapping (`ADMIT`/`LINK`/`UTILIZED`/`SUPERSEDED`/`ERASED`) is non-canonical and authorizes no new Event verbs;
- `global_seq` / `stream_seq` remain reference-laboratory ordering mechanisms, not `LIFECYCLE_TRANSITION_ORDER` itself;
- Issue #14/#15/#16 retain their remaining contract/evidence scope;
- Issue #74 / ADR-0024, Issue #18 and Track H operator-controlled decisions remain untouched.

## Runtime freeze boundary

Allowed: architecture/ontology research; integrity/security/reproducibility/provenance fixes; evidence preservation; truth-surface/validator repair; historical recovery; isolated falsification experiments without promotion.

Not authorized: reducer v2, new semantic Event verbs, new databases/language profiles/LLM-vector adapters/ecosystem integrations, executable NK-EPI or Temporal runtime, full Admission lifecycle, operational deletion expansion, maturity promotion, production promotion.

## Current known gaps

- A1–A6 are drafted/provisional, not independently or integratively approved;
- A7–A10 remain incomplete;
- A5 identity criteria remain domain-scoped and some valid-time identity effects are explicitly unresolved;
- A6 lifecycle closure kinds remain pending A7's conflict-resolution model for successor/cycle rules;
- cross-substrate equivalence thresholds remain A8 work;
- conflict-resolution and belief-revision algorithms remain A7 work;
- current PostgreSQL/SQLite profiles share Python semantic lineage;
- NK-EPI executable support remains absent;
- physical/cryptographic deletion and production operations remain absent.

## Machine-readable state

```text
../../project-state.json
../../contracts/project-state-v2.schema.json
../../tools/ai_context/validate_project_state.py
../../tools/ai_context/validate_architecture_freeze.py
../../tools/ai_context/validate_context.py
```

GitHub remains authoritative for technical live state. Notion is synchronized only after confirmed authoritative merges and read-back; a later Notion state can be newer than the repository-committed non-self-referential checkpoint.
