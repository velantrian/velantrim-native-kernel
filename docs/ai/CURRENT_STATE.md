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
clean_runtime_support:      PARTIAL
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
BOUNDED REFERENCE LABORATORY
```

The blueprint content A1–A9 is `DRAFTED / PROVISIONAL` and remains pending independent plus integrated A1–A10 review. The next bounded content slice is `A10 — Open Questions and Falsification`.

Required sequence:

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Knowledge and Memory Ontology              DRAFTED / PROVISIONAL
→ A3 Abstract Native Kernel Machine             DRAFTED / PROVISIONAL
→ A4 Semantic Laws and Invariants               DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        DRAFTED / PROVISIONAL
→ A7 Conflict / Uncertainty / Revision          DRAFTED / PROVISIONAL
→ A8 Substrate-independence Contract            DRAFTED / PROVISIONAL
→ A9 Reference Laboratory Boundary              DRAFTED / PROVISIONAL
→ A10 Open Questions and Falsification           NEXT BOUNDED SLICE
→ integrated blueprint review
→ separate operator decision before runtime expansion
```

Drafted A9: [EN](../A9_REFERENCE_LABORATORY_BOUNDARY.md) / [RU](../A9_REFERENCE_LABORATORY_BOUNDARY.ru.md).

## A9 candidate truth

`nk-reference-laboratory-boundary/A9-draft-1` classifies current P1–C5 mechanisms rather than changing them.

```text
ARCHITECTURE_PRESERVING_EVIDENCE
PROFILE_SPECIFIC_REALIZATION
PARTIAL_ARCHITECTURE_COVERAGE
FALSIFICATION_INSTRUMENT
LABORATORY_ONLY_CONSTRAINT
NOT_ARCHITECTURE_EVIDENCE
```

Key bounded finding:

```text
PostgreSQL ↔ SQLite C3
= useful cross-profile evidence
≠ independent-language equivalence
≠ independent-computation-model equivalence
≠ arbitrary-substrate portability proof
```

The two profiles share Python, conventional digital execution, semantic-core/reducer assumptions, current Event/encoding conventions, related test harnesses and repository custody. Current exact-byte requirements remain valid only where versioned laboratory contracts explicitly require them. A8 remains architecture authority: different bytes may preserve meaning, and equal bytes alone do not prove semantic equivalence.

P4/C4/C5 remain valuable measurement/falsification instruments. C5 remains synthetic bounded operational rehearsal, not production security/privacy/HA/compliance/independent custody evidence.

Profile-specific code is preserved rather than deleted merely for being profile-specific: label correctly, preserve reproducibility and evidence lineage, prevent silent Canon promotion.

## Runtime freeze boundary

Allowed: architecture/ontology research; integrity/security/reproducibility/provenance fixes; evidence preservation; truth-surface/validator repair; historical recovery; isolated falsification experiments without promotion.

Not authorized: reducer v2, new semantic/conflict Event verbs, new databases/language profiles/LLM-vector adapters/ecosystem integrations, executable NK-EPI or Temporal runtime, full Admission lifecycle, operational deletion expansion, maturity promotion, production promotion.

## Current known gaps

- A1–A9 are drafted/provisional, not independently or integratively approved;
- A10 remains incomplete;
- P5/C3 is not independent-language or arbitrary-substrate evidence;
- no arbitrary future substrate support is demonstrated;
- Issue #74 / ADR-0024 remains separately unresolved and operator-controlled;
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
