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

The blueprint content A1–A10 is `DRAFTED / PROVISIONAL` and remains pending independent plus integrated A1–A10 review. The next bounded gate is `INTEGRATED_A1_A10_REVIEW`.

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
→ A10 Open Questions and Falsification           DRAFTED / PROVISIONAL
→ integrated A1-A10 review                     NEXT GATE
→ separate operator decision before runtime expansion
```

Drafted A10: [EN](../A10_OPEN_QUESTIONS_AND_FALSIFICATION.md) / [RU](../A10_OPEN_QUESTIONS_AND_FALSIFICATION.ru.md).

## A10 candidate truth

`nk-open-questions-falsification/A10-draft-1` makes the remaining uncertainty explicit and falsifiable rather than promoting unknowns.

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

`NOT_TESTED ≠ SUPPORTED`. These are A10 research outcomes, not P4 assertion-map replacements and not A8 conformance states.

A10 records twelve major hypotheses and eighteen open questions. The high-risk unresolved boundaries include minimum explicit history without Event sourcing, reconstruction without exact replay, lossy identity continuity, independent-language evidence thresholds, analog/neuromorphic continuity, probabilistic conformance, forgetting/physical deletion observability, bounded-memory auditability, causal order without global sequence, decentralized Authority, non-classical computation, self-modifying realizations and evidence independence.

A10 thought experiments are falsification aids only: eventless archives, distributed neuromorphic memory, lossy bounded-memory agents, probabilistic realizations and independent-language digital profiles. They are not implementation commitments.

A10 stop conditions require reopening assumptions when a reproducible falsifier refutes a scoped hypothesis, blueprint terminology conflicts materially, a conformance test has no possible failure condition, or runtime work is needed merely to make an architecture claim appear true.

## Runtime freeze boundary

Allowed: architecture/ontology research; integrity/security/reproducibility/provenance fixes; evidence preservation; truth-surface/validator repair; historical recovery; isolated falsification experiments without promotion.

Not authorized: reducer v2, new semantic/conflict Event verbs, new databases/language profiles/LLM-vector adapters/ecosystem integrations, executable NK-EPI or Temporal runtime, full Admission lifecycle, operational deletion expansion, maturity promotion, production promotion.

## Current known gaps

- A1–A10 are drafted/provisional, not independently or integratively approved;
- integrated A1–A10 review remains incomplete;
- P5/C3 is not independent-language or arbitrary-substrate evidence;
- no arbitrary future substrate support is demonstrated;
- Issue #74 / ADR-0024 remains separately unresolved and operator-controlled;
- current PostgreSQL/SQLite profiles share Python semantic lineage;
- NK-EPI executable support remains absent;
- physical/cryptographic deletion and production operations remain absent;
- A10-H01–H10 remain unproved across independent computation models.

## Machine-readable state

```text
../../project-state.json
../../contracts/project-state-v2.schema.json
../../tools/ai_context/validate_project_state.py
../../tools/ai_context/validate_architecture_freeze.py
../../tools/ai_context/validate_context.py
```

GitHub remains authoritative for technical live state. Notion is synchronized only after confirmed authoritative merges and read-back; a later Notion state can be newer than the repository-committed non-self-referential checkpoint.
