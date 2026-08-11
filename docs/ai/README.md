# 🤖 Native Kernel AI Context Pack

This directory is the mandatory continuity surface for AI agents, auditors and maintainers.

## Required reading order

1. [`../../README.md`](../../README.md)
2. [`../../STATUS.md`](../../STATUS.md)
3. [`../../project-state.json`](../../project-state.json)
4. [`../../AGENTS.md`](../../AGENTS.md)
5. [`CURRENT_STATE.md`](CURRENT_STATE.md)
6. [`KNOWN_RISKS.md`](KNOWN_RISKS.md)
7. [`../../ROADMAP.md`](../../ROADMAP.md)
8. [`../ARCHITECTURE_REFOUNDATION.md`](../ARCHITECTURE_REFOUNDATION.md)
9. A1–A10 bilingual first-draft documents
10. [`../INTEGRATED_A1_A10_REVIEW.md`](../INTEGRATED_A1_A10_REVIEW.md) / [`RU`](../INTEGRATED_A1_A10_REVIEW.ru.md)
11. [`../INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md`](../INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md) / [`RU`](../INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md)
12. [`../reviews/IAR-1_RESULT.md`](../reviews/IAR-1_RESULT.md) / [`RU`](../reviews/IAR-1_RESULT.ru.md) + [`JSON`](../reviews/IAR-1_RESULT.json)
13. [`../reviews/IAR-1_RECONCILIATION.md`](../reviews/IAR-1_RECONCILIATION.md) / [`RU`](../reviews/IAR-1_RECONCILIATION.ru.md) + [`JSON`](../reviews/IAR-1_RECONCILIATION.json)
14. [`../adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md`](../adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md)
15. [`ISSUE_RECONCILIATION.md`](ISSUE_RECONCILIATION.md)
16. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)
17. affected contracts/ADRs/runtime/tests/evidence plus current GitHub/Notion live state

Do not start from a handoff alone; resolve live GitHub/Notion truth first.

## Current boundary

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
production_authorized: false
assertion map: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
runtime expansion: FROZEN
P1-C5: BOUNDED REFERENCE LABORATORY
```

## Architecture phase

```text
ADR-0025: ACCEPTED / OPERATOR APPROVED
ADR-0026: ACCEPTED / OPERATOR APPROVED
blueprint content: A1-A10 DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY
integrated review: COMPLETED / PROVISIONAL
IAR-1: QUALIFYING_REVIEW_COMPLETE
IAR-1 findings: 10 total / 7 BLOCKING / 3 MATERIAL
IAR-1-R1 reconciliation: COMPLETE
open BLOCKING findings: 0
open MATERIAL findings: 0
next gate: BPV1_PLAN_AND_PREREGISTRATION
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
```

The candidate blueprint inventory remains exact A1+A2+A3+A4+A5+A6+A7+A8+A9+A10. `INTEGRATED_A1_A10_REVIEW`, `OPERATOR_POST_BLUEPRINT_DECISION`, `INDEPENDENT_ARCHITECTURE_REVIEW` and `BPV1_PLAN_AND_PREREGISTRATION` are gates/review records, not A11-style deliverables.

Integrated review identity: `nk-integrated-blueprint-review/A1-A10-review-1`. Independent-review protocol identity: `nk-independent-architecture-review/1`. IAR-1 reconciliation identity: `IAR-1-R1`.

## Current reconciliation hierarchy

Apply the following order when first-draft wording conflicts:

```text
A1-A10 first draft provenance
→ integrated review IR-F01..IR-F07
→ IAR-1 independent challenge
→ IAR-1-R1 provisional reconciliation overlay
```

IAR-1-R1 intentionally weakens several prior candidate structures:

- A3 transition families/outcomes are reference taxonomy, not mandatory Kernel shape;
- A6 lifecycle positions are reference taxonomy, not mandatory Kernel shape;
- A5 identity/time inventories are scenario-selected analytical dimensions, not universal latent inventory;
- bounded accountability is separated from exact reconstruction/replay;
- Source/Evidence/Provenance/Authority separation is a semantic non-conflation rule, not a mandatory four-field storage schema;
- physical/cryptographic erasure claims require threat-scoped evidence beyond self-assertion;
- Context/Provenance/Authority chains require an explicit finite grounding mode;
- local scoped conformance does not imply composition/federation conformance.

The independent review is qualifying, but that does **not** prove the architecture correct.

## BPV-1 planning hard stop

BPV-1 execution remains forbidden until an authoritative plan preregisters:

```text
scenario_id
purpose_scope
mandatory_obligations
applicability_rules
mandatory_observables
equivalence_predicates
allowed_declared_losses
failure_thresholds
hard_refutation_observations
grounding_mode
threat_model
oracle_authority
```

Post-execution changes to mandatory obligations, applicability, equivalence predicates or failure thresholds invalidate the run for the claimed scope and require a new experiment identity.

The implementation under test must not serve as its own semantic oracle. A different language is insufficient if the experiment simply ports A3/A6/Event/reducer/Receipt structures.

```text
runtime thaw: NO
reducer v2: NOT AUTHORIZED
new Event verbs: NOT AUTHORIZED
new product DB/language/runtime profile: NOT AUTHORIZED
NK-EPI runtime: NOT AUTHORIZED
Final Canon: NOT AUTHORIZED
production: false
```

Issue #18, Issue #74/ADR-0024, ADR-0003 and Track H authority remain unchanged.

## Checkpoint roles

```text
publication checkpoint:
  10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
manifest source / Notion synchronized descendant:
  70acd0da61fee19131947aa56125833adb156ced
```

The later Notion synchronization checkpoint does not rewrite or replace the earlier publication checkpoint. Live HEAD comes from Git/GitHub; committed state does not predict its own future merge/Notion identity.

## Automated guards

```bash
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
python -m unittest discover -s tests -p 'test_architecture_freeze.py' -v
python -m unittest discover -s tests -p 'test_independent_architecture_review_protocol.py' -v
python -m unittest discover -s tests -p 'test_integrated_a1_a10_review.py' -v
```

Passing these guards proves continuity constraints only; it is not proof that the reconciled architecture or a future BPV-1 is correct.