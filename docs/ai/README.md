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
14. [`../research/BPV1_PREREGISTRATION.md`](../research/BPV1_PREREGISTRATION.md) / [`RU`](../research/BPV1_PREREGISTRATION.ru.md) + [`JSON`](../research/BPV1_PREREGISTRATION.json)
15. [`../adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md`](../adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md)
16. [`ISSUE_RECONCILIATION.md`](ISSUE_RECONCILIATION.md)
17. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)
18. affected contracts/ADRs/runtime/tests/evidence plus current GitHub/Notion live state

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
BPV-1 plan: PREREGISTERED / EXECUTION_NOT_AUTHORIZED
plan_id: BPV1-001-cross-lineage-bounded-accountability-v1
plan_merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
next gate: BPV1_EXECUTION_ADMISSION
BPV-1 execution: BLOCKED_PENDING_EXECUTION_ADMISSION
```

The candidate blueprint inventory remains exact A1+A2+A3+A4+A5+A6+A7+A8+A9+A10. Integrated review, operator decision, independent review, reconciliation, preregistration and execution admission are gates/review records, not A11-style blueprint deliverables.

## Current reconciliation hierarchy

```text
A1-A10 first-draft provenance
→ integrated review IR-F01..IR-F07
→ IAR-1 independent challenge
→ IAR-1-R1 provisional reconciliation overlay
→ BPV1-001 frozen preregistration
```

IAR-1-R1 intentionally weakens several prior candidate structures: A3/A6 are reference taxonomies; A5 identity/time inventories are scenario-selected analytical dimensions; bounded accountability is separate from exact replay; Source/Evidence/Provenance/Authority is a non-conflation rule rather than mandatory four-field storage; erasure claims require threat-scoped evidence; grounding must terminate explicitly; local conformance does not imply composition/federation.

The qualifying review and preregistered plan do **not** prove the architecture correct.

## BPV1_EXECUTION_ADMISSION hard stop

PR #110 made the plan authoritative; it did **not** authorize execution. The next gate must bind before any subject implementation/execution:

```text
authoritative preregistration + frozen digest
machine-readable fixtures derived only from the plan
standalone evaluator/oracle tested before subject execution
pinned Rust toolchain + experimental source boundary
static audit proving no product runtime/profile integration
```

The twelve preregistered normative fields are immutable under `BPV1-001-cross-lineage-bounded-accountability-v1`. Post-execution rescoping requires a new scenario identity.

Rust is an experimental cross-language falsification instrument only. It is not Canon or a product runtime profile; independent team/custody and independent computation model remain `NOT_ESTABLISHED`.

```text
runtime thaw: NO
BPV-1 execution: BLOCKED_PENDING_EXECUTION_ADMISSION
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
historical manifest source / committed Notion descendant:
  70acd0da61fee19131947aa56125833adb156ced
BPV-1 preregistration merge:
  a538d7f1e28858a88b9ee777ac7d6e05b85943db
```

The later Notion synchronization checkpoint does not rewrite or replace the earlier publication checkpoint. Live HEAD comes from Git/GitHub; committed state does not predict its own future merge/Notion identity.

## Automated guards

```bash
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_bpv1_preregistration.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
python -m unittest discover -s tests -p 'test_architecture_freeze.py' -v
python -m unittest discover -s tests -p 'test_bpv1_preregistration.py' -v
python -m unittest discover -s tests -p 'test_integrated_a1_a10_review.py' -v
```

Passing these guards proves continuity constraints only; it is not proof that the reconciled architecture or BPV-1 is correct.
