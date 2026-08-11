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
12. [`../adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md`](../adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md)
13. [`ISSUE_RECONCILIATION.md`](ISSUE_RECONCILIATION.md)
14. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)
15. affected contracts/ADRs/runtime/tests/evidence plus current GitHub/Notion live state

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
blueprint content: A1-A10 DRAFTED / PROVISIONAL
integrated review: COMPLETED / PROVISIONAL
post-blueprint choice: OPTION D
next gate: INDEPENDENT_ARCHITECTURE_REVIEW
independent architectural validation: NOT ESTABLISHED
BPV-1: BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION
```

The candidate blueprint inventory remains exact A1+A2+A3+A4+A5+A6+A7+A8+A9+A10. `INTEGRATED_A1_A10_REVIEW`, `OPERATOR_POST_BLUEPRINT_DECISION` and `INDEPENDENT_ARCHITECTURE_REVIEW` are gates/review records, not A11-style deliverables.

Integrated review identity: `nk-integrated-blueprint-review/A1-A10-review-1`. Independent-review protocol identity: `nk-independent-architecture-review/1`.

### Integrated reconciliation boundary

Current provisional semantics are governed by the integrated review where a first-draft wording conflicts:

```text
PHYSICALLY_ERASED ≠ CRYPTOGRAPHICALLY_ERASED
closure taxonomy = LOGICALLY_ERASED / PHYSICALLY_ERASED / CRYPTOGRAPHICALLY_ERASED / FORGOTTEN_OR_LOST
FORGOTTEN_OR_LOST does not require deliberate erasure method
A1 confidence wording means uncertainty + epistemic position, not mandatory scalar
A10 outcome protocol = SUPPORTED_FOR_SCOPE / WEAKENED / REFUTED / INDETERMINATE / NOT_TESTED
Conflict ≠ necessarily Contradiction
A6 lifecycle positions ≠ mandatory pipeline
```

Do not silently rewrite historical first-draft meaning. Cite the integrated finding (`IR-F01`…`IR-F07`) when applying a reconciliation.

The review pass found no known blocking internal semantic contradiction remaining after those explicit reconciliations, but independent architectural validation is **NOT ESTABLISHED**.

## Option D / independent-review hard stop

ADR-0026 selected:

```text
INDEPENDENT_ARCHITECTURE_REVIEW
→ REVIEW_FINDING_RECONCILIATION
→ BPV-1 bounded cross-lineage falsification
→ A10 outcome classification
→ integrated re-review
→ separate later operator Canon/runtime decision
```

The independent-review protocol does not complete the review. A qualifying reviewer must have a declared independence basis and must attack the architecture for hidden assumptions, unnecessary obligations, circularity, non-falsifiability and implementation capture.

If no qualifying reviewer exists, record `BLOCKED_NO_QUALIFYING_REVIEWER`; do not self-certify and do not skip to BPV-1.

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
python -m unittest discover -s tests -p 'test_independent_architecture_review_protocol.py' -v
python -m unittest discover -s tests -p 'test_integrated_a1_a10_review.py' -v
```

Passing these guards proves continuity constraints only; it is not independent architectural validation.