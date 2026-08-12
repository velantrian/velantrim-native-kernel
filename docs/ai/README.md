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
15. [`../research/BPV1_D5_R1_QUALIFICATION.md`](../research/BPV1_D5_R1_QUALIFICATION.md) / [`RU`](../research/BPV1_D5_R1_QUALIFICATION.ru.md)
16. [`../adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md`](../adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md)
17. [`ISSUE_RECONCILIATION.md`](ISSUE_RECONCILIATION.md)
18. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)
19. affected contracts/ADRs/runtime/tests/evidence plus current GitHub/Notion live state

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
BPV-1 execution-admission package merge: 6027eec73f11c4626be5553de7e79f827be2c81d
D5 execution: COMPLETE / a191e9c868c14af34a269dcdfae44406f1013bda
D5-R1 qualification: COMPLETE / QUALIFIED / 3856740570620fb2243e2f0da76359281ec4068f
qualified outcome: SUPPORTED_FOR_SCOPE / 12-of-12 mandatory fixtures PASS
next gate: D6_A10_HYPOTHESIS_CLASSIFICATION
D6: NOT_STARTED
BPV-1 execution authorization lane: ADMITTED_FOR_EXPERIMENT_ONLY
```

The candidate blueprint inventory remains exact A1+A2+A3+A4+A5+A6+A7+A8+A9+A10. Integrated review, operator decision, independent review, reconciliation, preregistration, execution admission, D5 execution and D5-R1 qualification are gates/evidence records, not A11-style blueprint deliverables.

## Current reconciliation hierarchy

```text
A1-A10 first-draft provenance
→ integrated review IR-F01..IR-F07
→ IAR-1 independent challenge
→ IAR-1-R1 provisional reconciliation overlay
→ BPV1-001 frozen preregistration
→ D5 execution evidence
→ D5-R1 external qualification evidence
→ D6 A10 hypothesis classification NEXT
```

IAR-1-R1 intentionally weakens several prior candidate structures: A3/A6 are reference taxonomies; A5 identity/time inventories are scenario-selected analytical dimensions; bounded accountability is separate from exact replay; Source/Evidence/Provenance/Authority is a non-conflation rule rather than mandatory four-field storage; erasure claims require threat-scoped evidence; grounding must terminate explicitly; local conformance does not imply composition/federation.

The qualifying review and scoped BPV1 result do **not** prove the architecture universally correct.

## D5-R1 evidence qualification

The authoritative D5 execution from PR #114 is preserved. PR #115 added a new evidence identity rather than rewriting historical results.

```text
Rust subject → raw facts
raw facts + external source audit → external qualifier
external qualifier → nk-bpv1-observations/1
unchanged frozen evaluator → SUPPORTED_FOR_SCOPE
```

The qualifier does not read the frozen fixture expected outcomes, does not inspect implementation-private runtime state, and does not accept structural oracle fields as Rust-subject self-report. The specific HR10 self-report path identified after D5 is therefore removed for this experiment evidence path.

Additional corrective tests cover evidence/epistemic-position corruption and bounded witness storage. The preregistered workload, scenario identity, plan digest, oracle, thresholds and HR01–HR10 remain unchanged.

Rust remains an experimental cross-language falsification instrument only. It is not Canon or a product runtime profile; independent team/custody and independent computation model remain `NOT_ESTABLISHED`.

```text
runtime thaw: NO
BPV-1 execution authorization lane: ADMITTED_FOR_EXPERIMENT_ONLY
D5 execution: COMPLETE
D5-R1 qualification: QUALIFIED
D6: NOT_STARTED
product runtime integration: NOT AUTHORIZED
reducer v2: NOT AUTHORIZED
new Event verbs: NOT AUTHORIZED
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
BPV-1 preregistration merge:
  a538d7f1e28858a88b9ee777ac7d6e05b85943db
D5 execution merge:
  a191e9c868c14af34a269dcdfae44406f1013bda
D5-R1 qualification merge:
  3856740570620fb2243e2f0da76359281ec4068f
```

Live HEAD comes from Git/GitHub; committed state does not predict its own future merge/Notion identity.

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
python -m unittest discover -s tests -p 'test_bpv1_subject.py' -v
```

Passing these guards proves continuity constraints only; it is not proof that the reconciled architecture or BPV-1 is universally correct.

## Notion boundary

Notion is intentionally still at the earlier D4.5 checkpoint; D5/D5-R1/D6 sync is deferred to Option D D8 unless live governance says otherwise. GitHub remains authoritative for current technical truth.
