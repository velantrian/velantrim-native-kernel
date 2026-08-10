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
11. [`ISSUE_RECONCILIATION.md`](ISSUE_RECONCILIATION.md)
12. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)
13. affected contracts/ADRs/runtime/tests/evidence plus current GitHub/Notion live state

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
Architecture Re-foundation: ACTIVE / BLUEPRINT-FIRST
blueprint content: A1-A10 DRAFTED / PROVISIONAL
integrated review: COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING
next content slice: OPERATOR_POST_BLUEPRINT_DECISION
```

The candidate progression must remain exact; changing completed content away from exact A1+A2+A3+A4+A5+A6+A7+A8+A9+A10 must fail continuity validation.

Integrated review identity: `nk-integrated-blueprint-review/A1-A10-review-1`.

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

## Operator and runtime hard stop

```text
OPERATOR_POST_BLUEPRINT_DECISION is NEXT
OPERATOR_POST_BLUEPRINT_DECISION ≠ A11
integrated review complete ≠ operator acceptance
integrated review complete ≠ runtime thaw
```

No AI agent may choose the next architecture/runtime phase for the operator.

```text
Issue #18: PENDING_OPERATOR — no license/publication selection
Issue #74 / ADR-0024: PROPOSED / PENDING_OPERATOR — reducer-v2 unauthorized
ADR-0003: PROPOSED / NOT_STARTED
Track H source admission: operator-controlled
```

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
python -m unittest discover -s tests -p 'test_integrated_a1_a10_review.py' -v
```
