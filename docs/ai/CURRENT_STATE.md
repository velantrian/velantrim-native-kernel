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

The blueprint content A1–A8 is `DRAFTED / PROVISIONAL` and remains pending independent plus integrated A1–A10 review. The next bounded content slice is `A9 — Reference Laboratory Boundary`.

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
→ A9 Reference Laboratory Boundary              NEXT BOUNDED SLICE
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
- [A7 EN](../A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) / [RU](../A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md)
- [A8 EN](../A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) / [RU](../A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md)

## A8 candidate truth

`nk-substrate-independence/A8-draft-1` is a provisional meaning-level conformance model. It does not implement a new runtime profile or prove universal portability.

Its preservation states are:

```text
PRESERVED
PARTIAL
UNSUPPORTED
INDETERMINATE
LOSSY
```

Its ten preservation obligations (`A8-P01`…`A8-P10`) require materially applicable ontology distinctions, transition outcomes, A4 laws, typed identity, temporal/order meaning, lifecycle/history, conflict/uncertainty/revision, Context/Provenance/Source/Authority, bounded accountability, and explicit capability/loss declarations to survive mapping or have loss declared.

Equivalence remains multidimensional:

```text
PHYSICAL_IDENTITY
REPRESENTATION_EQUIVALENCE
SEMANTIC_OBLIGATION_EQUIVALENCE
BEHAVIORAL_CONFORMANCE_FOR_SCOPE
LINEAGE_CONTINUITY_EQUIVALENCE
```

Physical identity is neither necessary nor sufficient for semantic equivalence. Same final output does not establish full semantic equivalence.

A8 does not require a global clock or total causal order; materially relevant temporal/order relations may be represented by partial orders, intervals, uncertain bounds, counters, phases or other declared equivalents. Implementation/write order cannot silently become world or causal order.

A8 preserves A7 states by meaning rather than storage enum. A profile unable to distinguish unresolved/unknown from false is lossy for the relevant obligation and cannot claim full conformance for that scope.

Scoped conformance outcomes are `FULL_CONFORMANCE_FOR_SCOPE`, `BOUNDED_CONFORMANCE`, `NON_CONFORMANT_FOR_SCOPE`, and `INDETERMINATE_CONFORMANCE`.

```text
substrate-independent specification
≠ universal portability proof
```

A9 owns detailed P1–C5 mapping. No existing SQL/Event/reducer mechanism is promoted into Canon by A8, and no existing accepted/versioned contract is silently rewritten.

## Runtime freeze boundary

Allowed: architecture/ontology research; integrity/security/reproducibility/provenance fixes; evidence preservation; truth-surface/validator repair; historical recovery; isolated falsification experiments without promotion.

Not authorized: reducer v2, new semantic/conflict Event verbs, new databases/language profiles/LLM-vector adapters/ecosystem integrations, executable NK-EPI or Temporal runtime, full Admission lifecycle, operational deletion expansion, maturity promotion, production promotion.

## Current known gaps

- A1–A8 are drafted/provisional, not independently or integratively approved;
- A9–A10 remain incomplete;
- A8 conformance classes and preservation obligations remain provisional and require integrated review/falsification;
- no arbitrary future substrate support is demonstrated;
- detailed current-laboratory mapping remains A9 work;
- Issue #74 / ADR-0024 remains separately unresolved and operator-controlled;
- A7 uncertainty combination remains method/profile-specific rather than a universal algebra;
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