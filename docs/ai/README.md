<!-- H11_EXECUTION_ADMISSION_BLOCKED_CURRENT -->
# 🤖 Native Kernel AI Context Pack

This directory is the mandatory continuity surface for AI agents, auditors and maintainers.

> [!IMPORTANT]
> Resolve live GitHub state before mutation. The current repository-native gate is `A10_H11_EXECUTION_ADMISSION`; admission is `BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`; the qualifying reviewer/reproducer is `NOT_ESTABLISHED`; H11: `NOT_TESTED`; runtime expansion: `FROZEN`; Final Canon remains `DEFERRED / NOT AUTHORIZED`; production remains `false`. PR #131 is the open external review surface. No documentation, CI, owner review, model agreement or Notion read-back may manufacture H11 independence.

## Required reading order

`docs/ai/README.md` owns the canonical AI reading order. Other agent-facing files may add operating constraints, but should not invent a competing order.

1. [`../../project-state.json`](../../project-state.json) — exact machine state and checkpoint roles.
2. [`POST_RESIDUAL_A10_STATE.md`](POST_RESIDUAL_A10_STATE.md) — current long-horizon/H11 orientation overlay.
3. [`../research/H11_EXECUTION_ADMISSION.json`](../research/H11_EXECUTION_ADMISSION.json) — fail-closed admission record.
4. [`../research/H11_REVIEWER_REPRODUCER_QUALIFICATION.json`](../research/H11_REVIEWER_REPRODUCER_QUALIFICATION.json) — current qualification result.
5. [`CURRENT_STATE.md`](CURRENT_STATE.md) — current-only human/agent projection.
6. [`AUDIT_AND_FUTURE_WORK.md`](AUDIT_AND_FUTURE_WORK.md) — durable audit/future-work orientation; reconcile against live evidence before selecting work. It is not implementation authorization.
7. [`../../AGENTS.md`](../../AGENTS.md) — operating constraints and reserved decisions.
8. [`../../ARCHITECTURE.md`](../../ARCHITECTURE.md) — Formal Architecture entrypoint.
9. A1–A10 first-draft architecture documents under `docs/`.
10. [`../INTEGRATED_A1_A10_REVIEW.md`](../INTEGRATED_A1_A10_REVIEW.md) / [`RU`](../INTEGRATED_A1_A10_REVIEW.ru.md).
11. [`../reviews/IAR-1_RESULT.md`](../reviews/IAR-1_RESULT.md) / [`RU`](../reviews/IAR-1_RESULT.ru.md) + [`JSON`](../reviews/IAR-1_RESULT.json).
12. [`../reviews/IAR-1_RECONCILIATION.md`](../reviews/IAR-1_RECONCILIATION.md) / [`RU`](../reviews/IAR-1_RECONCILIATION.ru.md) + [`JSON`](../reviews/IAR-1_RECONCILIATION.json).
13. [`KNOWN_RISKS.md`](KNOWN_RISKS.md).
14. [`../../README.md`](../../README.md), [`../../STATUS.md`](../../STATUS.md) and [`../../ROADMAP.md`](../../ROADMAP.md) for human orientation and chronology.
15. Affected contracts, ADRs, runtime/tests/evidence, live PRs/issues/Actions/reviews, and corresponding existing Notion pages when synchronization is part of the task.

Do not start from a handoff alone. Do not treat an older human/history `NEXT` marker as current authority without reconciling it against live GitHub and machine/current-state surfaces.

The future-work ledger is a navigation and audit surface only. `future-work entry != implementation authorization`, `priority != authorization`, and the ledger never auto-selects the next milestone.

## 🏛 Formal Architecture resolution

The Formal Authority Core is not just the first A1–A10 draft sequence. Resolve architecture meaning through the complete accepted chain:

```text
ARCHITECTURE.md
→ A1–A10 first-draft provenance
→ Integrated A1–A10 Review
→ IAR-1 qualifying challenge
→ IAR-1 reconciliation
→ later accepted ADR / operator decisions for their explicit scope
```

A1–A10 first-draft provenance remains preserved. Where first-draft wording conflicts with IAR-1 reconciliation, `IAR-1-R1` is the current provisional interpretation unless a later accepted architecture authority explicitly supersedes it. Final Canon is still deferred.

The reconciliation deliberately narrowed several early structures:

- full A2 ontology inventory → reference taxonomy, not a universal minimum schema;
- A3 transition catalogue → reference taxonomy, not one universal machine shape;
- A5 identity/time inventories → scenario-selected analytical dimensions;
- A6 lifecycle positions → not a universal state machine;
- Receipt-shaped accountability → not universal;
- Event-log-shaped history → not universal;
- exact replay/reconstruction → optional unless a preregistered scope requires it.

Do not re-promote those first-draft structures merely because the bounded reference laboratory implements them.

## 📍 Current boundary

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
production_authorized: false
assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
P1–C5: BOUNDED_REFERENCE_LABORATORY
selected family: A10-H11
current gate: A10_H11_EXECUTION_ADMISSION
admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
reviewer/reproducer: NOT_ESTABLISHED
H11: NOT_TESTED
implementation/execution: NOT AUTHORIZED
runtime expansion: FROZEN
Final Canon: DEFERRED / NOT AUTHORIZED
production: false
```

The committed H11 current-truth binding is PR #130 / `e36b7f45410d74b8a65406bff6fdd6d070fa96b0`. It is a role-specific checkpoint, not a prediction of live `main`. Later documentation or validation-machinery descendants do not automatically change the H11 gate.

## 🔬 H11 frozen boundary

```text
plan: H11-001-c5-lab-canon-separation-v1
plan SHA-256: 60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914
frozen subject: native-kernel/c5/2026-08-08-adr0023
required oracle: INDEPENDENT_SEMANTIC_ORACLE
hard failure: UNJUSTIFIED_CANON_DEPENDENCY
```

H11 asks whether exact laboratory reproducibility can remain dependent on profile-specific mechanisms without those mechanisms being elevated into universal Architecture authority.

```text
exact lab bytes ≠ Architecture Canon
profile-specific mechanism ≠ universal semantic obligation
preregistration ≠ execution admission
blocked admission ≠ INDETERMINATE
execution admission ≠ execution
NOT_TESTED ≠ SUPPORTED
A10-H11 ≠ composition/federation
```

The existing Codex review is useful technical review but is `NOT_ESTABLISHED_FOR_H11_REVIEW_ROLE`. Qualification requires externally authenticated, repository-visible evidence sufficient to evaluate identity, authorship independence, custody independence, conflicts/material dependence, frozen-input scope and private-state boundaries. A qualifying result would still require a separate execution-admission reassessment before H11 execution.

## 📊 A10 evidence position

```text
SUPPORTED_FOR_SCOPE:
  A10-H01 / A10-H02 / A10-H04 / A10-H05 / A10-H07 / A10-H12

NOT_TESTED:
  A10-H03 / A10-H06 / A10-H08 / A10-H09 / A10-H10 / A10-H11
```

RAVP-001 records the recommended research order `H11 → H03 → H10 → H06 → H09 → H08`. That order is planning guidance only: it does not automatically authorize the next family when the previous family completes. Each residual family remains subject to the bounded plan/admission/authorization required for its own scope.

Residual-family outcomes feed a later integrated reassessment, not a predetermined Canon result. Final Canon remains a separate operator decision and may be frozen for a bounded version, kept provisional, narrowed, revised, require additional evidence, or reject a claim for the relevant scope.

The BPV-1 Rust subject remains an experimental cross-language falsification instrument only. External qualification removed a specific self-report path for that evidence lineage, but independent team/custody and independent computation-model evidence remain `NOT_ESTABLISHED`.

## 📜 Historical/current separation

Current-facing agent surfaces must not require obsolete gates to masquerade as current state merely to preserve chronology.

Historical D5/D6/D7/D8, ADR-0027, RAVP, family-selection and preregistration checkpoints remain available in:

- `STATUS.md` and `ROADMAP.md` for human chronology;
- `docs/research/**` and `docs/reviews/**` for research/review records;
- `evidence/**` for evidence identities;
- `docs/ai/WORK_LOG.md` and reconciliation/handoff records where applicable;
- Git history for exact historical repository bytes.

When those files contain old values such as former `NEXT` or `NOT_STARTED` markers, treat them as chronology unless the current machine/current-state surfaces still select them. Do not copy such literals back into current-only files solely for compatibility validation.

## 🔐 Runtime and operator boundary

Allowed while runtime is frozen:

- truth-surface, integrity, security and provenance repair;
- evidence preservation;
- reviewer/reproducer qualification work that does not execute H11;
- historical recovery work that does not admit operator-controlled sources;
- research admission/preregistration work only when the active gate explicitly authorizes it.

Not automatically authorized:

- H11 implementation/execution, dependency-graph execution or semantic adjudication while admission is blocked;
- preregistration/execution of H03/H06/H08/H09/H10;
- reducer v2 or new semantic Event verbs;
- product runtime integration;
- new product database/language/hardware profiles;
- physical/cryptographic deletion claims not backed by their required evidence;
- Final Canon, runtime thaw or production promotion.

Reserved operator decisions remain:

```text
Issue #18 — license/publication/contribution regime
Issue #74 / ADR-0024 — future reducer referential semantics
Track H recovered-source admission
Final Canon
runtime thaw
production authorization
```

## ✅ Verification

At minimum for current truth / architecture-routing changes:

```bash
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_residual_a10_plan.py --repo .
python tools/ai_context/validate_h11_family_selection.py --repo .
python tools/ai_context/validate_h11_preregistration.py --repo .
python tools/ai_context/validate_h11_execution_admission.py --repo .
python tools/ai_context/validate_reconciliation.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
```

Run additional P4/P5/C3/C4/C5/BPV1 gates when changed-file scope triggers them. A skipped test is not PASS. An unavailable environment is `NOT_EXECUTED`.

Passing continuity/documentation guards proves only that routing and declared boundaries are internally consistent. It does not qualify an H11 reviewer, execute H11, prove universal substrate neutrality, thaw runtime or authorize production.