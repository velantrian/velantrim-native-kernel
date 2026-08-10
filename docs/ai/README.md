# 🤖 Native Kernel AI Context Pack

This directory is the mandatory continuity surface for AI agents, auditors, and maintainers.

## Required reading order

1. [`../../README.md`](../../README.md)
2. [`../../STATUS.md`](../../STATUS.md)
3. [`../../project-state.json`](../../project-state.json)
4. [`../../AGENTS.md`](../../AGENTS.md)
5. [`CURRENT_STATE.md`](CURRENT_STATE.md)
6. [`KNOWN_RISKS.md`](KNOWN_RISKS.md)
7. [`../../ROADMAP.md`](../../ROADMAP.md)
8. [`../ARCHITECTURE_REFOUNDATION.md`](../ARCHITECTURE_REFOUNDATION.md)
9. [`../A1_KERNEL_PURPOSE_AND_NON_GOALS.md`](../A1_KERNEL_PURPOSE_AND_NON_GOALS.md) and [`../A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md`](../A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md)
10. [`../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md`](../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) and [`../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md`](../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md)
11. [`../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md`](../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) and [`../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md`](../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md)
12. [`../A4_SEMANTIC_LAWS_AND_INVARIANTS.md`](../A4_SEMANTIC_LAWS_AND_INVARIANTS.md) and [`../A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md`](../A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md)
13. [`ISSUE_RECONCILIATION.md`](ISSUE_RECONCILIATION.md)
14. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)
15. affected Canon, contracts, ADRs, source, tests, workflows, and evidence
16. current GitHub and Notion state

Do not read every historical handoff before identifying the current task. Do not begin with random code search.

## Current boundary

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false
assertion map:              45 / 10 / 17 / 0
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

## Active architecture phase

```text
ADR-0025: ACCEPTED / OPERATOR APPROVED
Architecture Re-foundation: ACTIVE / BLUEPRINT-FIRST
runtime expansion: FROZEN
P1–C5 role: BOUNDED REFERENCE LABORATORY
blueprint content: A1-A4 DRAFTED / PROVISIONAL
next content slice: A5 — Identity / Time / Change
```

The full plan and drafted content are maintained in:

- [`../ARCHITECTURE_REFOUNDATION.md`](../ARCHITECTURE_REFOUNDATION.md)
- [`../ARCHITECTURE_REFOUNDATION.ru.md`](../ARCHITECTURE_REFOUNDATION.ru.md)
- [`../A1_KERNEL_PURPOSE_AND_NON_GOALS.md`](../A1_KERNEL_PURPOSE_AND_NON_GOALS.md)
- [`../A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md`](../A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md)
- [`../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md`](../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md)
- [`../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md`](../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md)
- [`../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md`](../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md)
- [`../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md`](../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md)
- [`../A4_SEMANTIC_LAWS_AND_INVARIANTS.md`](../A4_SEMANTIC_LAWS_AND_INVARIANTS.md)
- [`../A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md`](../A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md)
- [`../adr/0025-blueprint-before-runtime-expansion.md`](../adr/0025-blueprint-before-runtime-expansion.md)

A1, A2, A3, and A4 are drafted, provisional architecture slices. They are not independently approved, not integrated Canon, and remain subject to revision during A5–A10 and integrated review.

A2 preserves at least:

```text
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
```

A3 preserves at least:

```text
abstract machine ≠ runtime implementation
transition ≠ Event envelope
transition relation ≠ reducer
history visibility ≠ mandatory Event sourcing
admission ≠ truth
deterministic output ≠ true output
profile conformance ≠ production authorization
```

A4 drafts the first GitHub-resident semantic-law set as `nk-semantic-laws/A4-draft-1`, currently 28 candidate laws. The count is provisional. Each law has a statement, rationale, counterexample/falsifier, failure mode, observable obligation, and exception/open uncertainty. The earlier false Notion-only identity `nk-semantic-laws/0.1-draft` is not reused.

A4 additionally protects meaning across representation and substrate change, including semantic identity versus storage identity, Context/provenance/Authority scope, temporal distinctions, accountable revision and Supersession, Conflict versus resolution, derived views versus history, selection versus epistemic validity, bounded accountability versus correctness, and named equivalence versus assumed sameness.

No new semantic/runtime expansion is authorized before blueprint review. Existing code and evidence remain preserved and may receive bounded maintenance, integrity, reproducibility, provenance, and validator fixes.

The machine-readable freeze is enforced fail closed by [`../../tools/ai_context/validate_architecture_freeze.py`](../../tools/ai_context/validate_architecture_freeze.py) in AI-context CI. Removing ADR-0025 state, disabling the freeze, authorizing semantic/runtime expansion, losing A1–A10, changing completed content away from exact A1+A2+A3+A4, or bypassing separate operator review must fail validation.

## Track boundary

```text
H historical recovery: BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / bounded reference laboratory
R architecture re-foundation: ACTIVE / blueprint-first / no automatic promotion
```

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
blueprint documentation ≠ runtime evidence
C2 ≠ C3 ≠ C4 ≠ C5
C5 bounded rehearsal ≠ production readiness
```

## Checkpoint roles

```text
publication checkpoint:
  10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
  PR #83 decision-package publication identity

manifest source / Notion synchronized descendant:
  70acd0da61fee19131947aa56125833adb156ced
  PR #86 merged, validated, synchronized, and read back
```

The later Notion checkpoint does not rewrite or replace the publication checkpoint. A committed state file references only already completed ancestors; it does not predict its own future merge SHA.

Live HEAD must be resolved through Git or GitHub. A descendant commit does not silently broaden earlier runtime, evidence, publication, or Notion proof.

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

Only after that review may downstream contract/runtime sequencing be reopened:

```text
reconcile contract families
→ NK-SAM and named equivalence
→ Event/history commitment if required by the integrated blueprint
→ ADR-0024 outcome if reducer work resumes
→ only then any reducer-v2 runtime
```

## Independent pending decisions

```text
Issue #18:
  license/publication PENDING_OPERATOR
  external contributions NOT ACCEPTED
  package publication NOT AUTHORIZED

Issue #74 / ADR-0024:
  PROPOSED / PENDING_OPERATOR
  reducer v1 IMMUTABLE
  reducer-v2 NOT AUTHORIZED
```

Architecture research does not silently decide either issue.

## Truth surfaces

```text
CURRENT STATE
  ../../STATUS.md
  ../../project-state.json
  CURRENT_STATE.md

ACTIVE ROADMAP
  ../../ROADMAP.md
  ../ARCHITECTURE_REFOUNDATION.md
  ../ARCHITECTURE_REFOUNDATION.ru.md

DRAFTED BLUEPRINT CONTENT
  ../A1_KERNEL_PURPOSE_AND_NON_GOALS.md
  ../A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md
  ../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md
  ../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md
  ../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md
  ../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md
  ../A4_SEMANTIC_LAWS_AND_INVARIANTS.md
  ../A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md

ACTIVE RISKS
  KNOWN_RISKS.md

RECONCILIATION RECORDS
  ISSUE_RECONCILIATION.md
  NOTION_HANDOFF.md

HISTORICAL RECORD
  implementation records
  accepted ADRs
  immutable evidence manifests
  Git history

PROPOSAL
  proposed ADRs
  research backlog
```

Historical chronology and proposals are not authoritative current state.

## Evidence route

```text
C5 plan and ADR-0021
→ implementation and final checkpoints
→ repository-resident exact ZIPs
→ strict bundle manifests and verifier
→ ADR-0023 safe-version additive identity
```

Evidence roots:

```text
../../evidence/c5/2026-08-07/manifest.json
../../evidence/c5/2026-08-08-adr0023/manifest.json
```

These archives are version-bound. ADR-0025 and A1–A4 do not expand their proof boundary.

## Source-of-truth order

1. exact code, tests, contracts, and retained artifact bytes;
2. exact-SHA CI jobs/logs and GitHub live refs, issues, and reviews;
3. `project-state.json`, `STATUS.md`, and `CURRENT_STATE.md`;
4. accepted ADRs and versioned contracts;
5. active blueprint plan and drafted research deliverables;
6. implementation and reconciliation records, work log, and PR/issue history;
7. Notion and historical chats.

## Automated guards

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_reconciliation.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
python -m unittest tests.test_a4_semantic_laws tests.test_a3_abstract_machine tests.test_architecture_freeze tests.test_ai_context_validator
```

## Historical records

Read only when relevant:

- [`P4_IMPLEMENTATION_RECORD.md`](P4_IMPLEMENTATION_RECORD.md)
- [`P5_IMPLEMENTATION_RECORD.md`](P5_IMPLEMENTATION_RECORD.md)
- [`C4_IMPLEMENTATION_RECORD.md`](C4_IMPLEMENTATION_RECORD.md)
- [`C5_IMPLEMENTATION_RECORD.md`](C5_IMPLEMENTATION_RECORD.md)
- [`WORK_LOG.md`](WORK_LOG.md)
- [`AUDIT_PLAYBOOK.md`](AUDIT_PLAYBOOK.md)

Historical records preserve provenance; they do not override current state.
