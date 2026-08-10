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
14. [`ISSUE_RECONCILIATION.md`](ISSUE_RECONCILIATION.md)
15. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)
16. affected Canon/contracts/ADRs/source/tests/workflows/evidence
17. current GitHub and Notion state

Do not begin with random code search or historical handoffs before resolving current truth.

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
blueprint content: A1-A5 DRAFTED / PROVISIONAL
next content slice: A6 — Knowledge Lifecycle
```

A1–A5 are drafted provisional architecture slices, not independent approval, integrated Canon, runtime evidence, or production authorization. The current candidate progression must remain exact; changing completed content away from exact A1+A2+A3+A4+A5 must fail continuity validation.

## A5 continuity boundary

A5 candidate model: `nk-identity-time-change/A5-draft-1`.

```text
identity is typed + scoped
same content ≠ same Claim ≠ same Record ≠ same occurrence
semantic identity ≠ substrate-local identity
equal bytes/hash/text ≠ universal semantic identity
occurrence/valid/Observation/assertion/Record/decision/effective/write time remain distinguishable
write/commit order ≠ occurrence order ≠ causal order
Revision ≠ silent overwrite
Supersession ≠ deletion or falsity
restriction ≠ logical erasure ≠ physical deletion ≠ crypto-erasure ≠ forgetting
```

Identity kinds currently drafted:

```text
REFERENT_IDENTITY
SEMANTIC_CONTENT_IDENTITY
CLAIM_POSITION_IDENTITY
RECORD_IDENTITY
LINEAGE_CONTINUITY_IDENTITY
OCCURRENCE_IDENTITY
SUBSTRATE_LOCAL_IDENTITY
```

Possible scoped results include `SAME`, `DISTINCT`, `CONTINUATION_OF`, `VERSION_OF`, `ALIAS_OF`, `MIGRATED_FROM`, and `UNRESOLVED`.

The draft deliberately reconciles rather than silently supersedes existing accepted/versioned contracts:

```text
A5 meaning-level identity/time model
        ↓
versioned encoding/profile mappings
        ↓
existing nk-id/1.0 as one current mapping
```

`nk-id/1.0` UTF-8/NFC/JSON/SHA-256 details remain a current versioned reference contract, not the only universal substrate realization. `global_seq`/`stream_seq` remain reference-laboratory ordering. Existing deletion-state enums remain bounded profile mechanisms.

## Active sequence

```text
A1 Purpose and Non-goals                         DRAFTED / PROVISIONAL
→ A2 Knowledge and Memory Ontology              DRAFTED / PROVISIONAL
→ A3 Abstract Native Kernel Machine             DRAFTED / PROVISIONAL
→ A4 Semantic Laws and Invariants               DRAFTED / PROVISIONAL
→ A5 Identity / Time / Change                   DRAFTED / PROVISIONAL
→ A6 Knowledge Lifecycle                        NEXT BOUNDED SLICE
→ A7 Conflict / Uncertainty / Revision
→ A8 Substrate-independence Contract
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ separate operator decision before runtime expansion
```

## Runtime and operator boundaries

No new semantic/runtime expansion before blueprint gate completion.

```text
Issue #18: PENDING_OPERATOR — no license/publication selection
Issue #74 / ADR-0024: PROPOSED / PENDING_OPERATOR — reducer v1 immutable; reducer-v2 unauthorized
Track H source admission: operator-controlled
```

Architecture research does not silently decide these boundaries. Issue #14/#15/#16 retain their existing versioned contract and remaining evidence scopes.

## Track boundary

```text
H historical recovery: BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / bounded reference laboratory
R architecture re-foundation: ACTIVE / blueprint-first / no automatic promotion
```

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
reference laboratory ≠ final architecture
blueprint documentation ≠ runtime evidence
C5 bounded rehearsal ≠ production readiness
```

## Checkpoint roles

```text
publication checkpoint:
  10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c

manifest source / Notion synchronized descendant:
  70acd0da61fee19131947aa56125833adb156ced
```

The later Notion synchronization checkpoint does not rewrite or replace the earlier publication checkpoint. Live HEAD comes from Git/GitHub; committed state does not predict its own future merge or Notion synchronization identity.

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
  ../A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md
  ../A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md
  ../A4_SEMANTIC_LAWS_AND_INVARIANTS.md
  ../A5_IDENTITY_TIME_AND_CHANGE.md
  plus Russian counterparts
```

Historical records, proposals and Notion do not override current GitHub truth.

## Source-of-truth order

1. exact code/tests/contracts/artifact bytes;
2. exact-SHA CI and live GitHub refs/issues/reviews;
3. `project-state.json`, `STATUS.md`, `CURRENT_STATE.md`;
4. accepted ADRs/versioned contracts;
5. active blueprint plan and drafted research deliverables;
6. implementation/reconciliation history;
7. Notion and chats.

## Automated guards

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_reconciliation.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
python -m unittest discover -s tests -p 'test_a5_identity_time_change.py' -v
```

A5 drafting does not change runtime, evidence identities, assertion arithmetic, NK-EPI, maturity, or production status.
