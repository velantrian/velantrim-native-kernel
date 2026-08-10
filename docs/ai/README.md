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
9. [`../A1_KERNEL_PURPOSE_AND_NON_GOALS.md`](../A1_KERNEL_PURPOSE_AND_NON_GOALS.md) / [`RU`](../A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md)
10. [`../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md`](../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) / [`RU`](../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md)
11. [`../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md`](../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) / [`RU`](../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md)
12. [`../A4_SEMANTIC_LAWS_AND_INVARIANTS.md`](../A4_SEMANTIC_LAWS_AND_INVARIANTS.md) / [`RU`](../A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md)
13. [`../A5_IDENTITY_TIME_AND_CHANGE.md`](../A5_IDENTITY_TIME_AND_CHANGE.md) / [`RU`](../A5_IDENTITY_TIME_AND_CHANGE.ru.md)
14. [`../A6_KNOWLEDGE_LIFECYCLE.md`](../A6_KNOWLEDGE_LIFECYCLE.md) / [`RU`](../A6_KNOWLEDGE_LIFECYCLE.ru.md)
15. [`../A7_CONFLICT_UNCERTAINTY_AND_REVISION.md`](../A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) / [`RU`](../A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md)
16. [`../A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md`](../A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) / [`RU`](../A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md)
17. [`../A9_REFERENCE_LABORATORY_BOUNDARY.md`](../A9_REFERENCE_LABORATORY_BOUNDARY.md) / [`RU`](../A9_REFERENCE_LABORATORY_BOUNDARY.ru.md)
18. [`ISSUE_RECONCILIATION.md`](ISSUE_RECONCILIATION.md)
19. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)
20. affected Canon/contracts/ADRs/source/tests/workflows/evidence and current GitHub/Notion state

Do not begin with random code search or historical handoffs before resolving current truth.

## Current boundary

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
clean_runtime_support:      PARTIAL
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
blueprint content: A1-A9 DRAFTED / PROVISIONAL
next content slice: A10 — Open Questions and Falsification
```

A1–A9 are drafted provisional architecture slices, not independent approval, integrated Canon, runtime evidence, or production authorization. The current candidate progression must remain exact; changing completed content away from exact A1+A2+A3+A4+A5+A6+A7+A8+A9 must fail continuity validation.

## A9 continuity boundary

A9 candidate model: `nk-reference-laboratory-boundary/A9-draft-1`.

```text
existing mechanism ≠ architecture requirement
useful evidence ≠ universal portability proof
profile-specific realization ≠ architectural defect
PostgreSQL ↔ SQLite C3 ≠ independent-language equivalence
C5 bounded rehearsal ≠ production readiness
repository-resident evidence ≠ independent custody
```

A9 role vocabulary is `ARCHITECTURE_PRESERVING_EVIDENCE`, `PROFILE_SPECIFIC_REALIZATION`, `PARTIAL_ARCHITECTURE_COVERAGE`, `FALSIFICATION_INSTRUMENT`, `LABORATORY_ONLY_CONSTRAINT`, and `NOT_ARCHITECTURE_EVIDENCE`.

P5/C3 supplies narrow storage-profile evidence inside a shared Python/conventional-digital lineage. It does not prove independent-computation-model or arbitrary-substrate equivalence. Current Event/reducer/hash/sequence/byte mechanisms remain valid laboratory mechanisms where versioned contracts require them, but A8 meaning preservation remains the architecture-level authority.

P4/C4/C5 are useful falsification/measurement surfaces. A9 does not delete profile-specific code: label it, preserve reproducibility/evidence lineage, and prevent silent Canon promotion.

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
→ A9 Reference Laboratory Boundary              DRAFTED / PROVISIONAL
→ A10 Open Questions and Falsification           NEXT BOUNDED SLICE
→ integrated blueprint review
→ separate operator decision before runtime expansion
```

## Runtime and operator boundaries

No new semantic/runtime expansion before blueprint gate completion.

```text
Issue #18: PENDING_OPERATOR — no license/publication selection
Issue #74 / ADR-0024: PROPOSED / PENDING_OPERATOR — reducer v1 immutable; reducer-v2 unauthorized
ADR-0003: PROPOSED / NOT_STARTED
Track H source admission: operator-controlled
```

## Track boundary

```text
H historical recovery: BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / bounded reference laboratory
R architecture re-foundation: ACTIVE / blueprint-first / no automatic promotion
```

## Checkpoint roles

```text
publication checkpoint:
  10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
manifest source / Notion synchronized descendant:
  70acd0da61fee19131947aa56125833adb156ced
```

The later Notion synchronization checkpoint does not rewrite or replace the earlier publication checkpoint. Live HEAD comes from Git/GitHub; committed state does not predict its own future merge or Notion synchronization identity.

## Automated guards

```bash
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
python -m unittest discover -s tests -p 'test_a8_substrate_independence_contract.py' -v
python -m unittest discover -s tests -p 'test_a9_reference_laboratory_boundary.py' -v
```

A9 drafting does not change runtime, evidence identities, assertion arithmetic, NK-EPI, maturity, or production status.
