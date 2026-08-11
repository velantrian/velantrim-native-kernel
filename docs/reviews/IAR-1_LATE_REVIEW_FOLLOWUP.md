# IAR-1 — Late Final Re-review Follow-up

**Purpose:** preserve the post-merge chronology of the final Codex re-review of PR #107 and the bounded fixes required before D4 may begin.

The final re-review request on PR #107 targeted exact head `3ca47783cf1b4bde46158bce5aa183ceed82d0f5`. It was accepted before merge but published its review submission only after PR #107 had already merged as `845f2c8e9322c5353f9d6b421e44d1da71b82f58`.

That late review produced four actionable findings:

1. **P1 — stale workflow gate tests**: `test_a9_reference_laboratory_boundary.py`, `test_a10_open_questions_falsification.py`, and `test_integrated_a1_a10_review.py` still required the pre-IAR `INDEPENDENT_ARCHITECTURE_REVIEW / NOT_ESTABLISHED` machine state.
2. **P2 — stale documentation indexes**: `docs/README.md`, `docs/README.ru.md`, and `docs/adr/README.md` still presented independent review as the current next gate.
3. **P2 — insufficient independence evidence guard**: `validate_architecture_freeze.py` checked reviewer identity/flags but did not require substantive `independence_basis` or the recorded input packet before accepting `QUALIFYING_REVIEW_COMPLETE`.
4. **P2 — incomplete preregistration-field guard**: the validator checked that preregistration existed but did not enforce the exact required field inventory, allowing fields such as `threat_model` or `oracle_authority` to disappear silently.

This follow-up fixes all four without changing runtime, contracts, profile semantics, evidence bytes, IAR-1 source findings, IAR-1-R1 substantive dispositions, or operator-controlled decisions.

```text
runtime_expansion: FROZEN
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
next gate after this follow-up: BPV1_PLAN_AND_PREREGISTRATION
product_runtime_thaw: NO
production_authorized: false
```

The existence of this follow-up corrects the earlier synchronization statement that no further final review submission had appeared. Historical Notion/Issue text is preserved; a new corrective checkpoint must supersede it after this follow-up merges and passes post-merge validation.