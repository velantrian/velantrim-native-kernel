# IAR-1 Late Review Follow-up

> **Record identity:** `nk-independent-architecture-review/IAR-1-late-followup-1`  
> **Status:** `CORRECTIVE FOLLOW-UP ACTIVE`  
> **Parent review:** `IAR-1`  
> **Parent reconciliation:** `IAR-1-R1`  
> **Parent merge:** `845f2c8e9322c5353f9d6b421e44d1da71b82f58`  
> **Corrective PR:** `#108`  
> **Runtime expansion:** `FROZEN`

## 1. Why this follow-up exists

The final Codex reconciliation-quality re-review of PR #107 targeted exact PR head `3ca47783cf1b4bde46158bce5aa183ceed82d0f5` but published after PR #107 had already squash-merged. Four actionable findings were therefore handled in a separate bounded corrective PR rather than silently rewriting the merged review chronology.

PR #108 then received two additional P2 findings on its own first reviewed head. Those are part of the same corrective chronology and are not erased by later thread resolution.

## 2. Late findings from PR #107 final re-review

1. stale A9/A10/integrated-review workflow tests could accept a pre-reconciliation validation status;
2. current documentation indexes still described independent review as the next gate;
3. the IAR-1 independence basis guard was too prose-dependent;
4. the BPV-1 preregistration field inventory was not enforced exactly enough.

## 3. Additional findings from PR #108 review

1. A9/A10/integrated-review slice tests needed an explicit assertion that `post_blueprint_validation.status` contains `RECONCILIATION_COMPLETE`;
2. a generic padded `independence_basis` string could still satisfy the architecture-freeze validator unless repository-visible structured independence evidence was enforced by the validation gate.

## 4. Corrective disposition

The follow-up therefore:

- preserves historical A9/A10/integrated-review document states while asserting the current machine gate;
- requires the slice tests to verify `RECONCILIATION_COMPLETE` explicitly;
- refreshes current documentation indexes to `IAR-1 complete / IAR-1-R1 complete / BPV1 plan next`;
- preserves exact preregistration field inventory and fail-closed duplicate/missing-field checks;
- records repository-visible IAR-1 reviewer-separation evidence in `docs/reviews/IAR-1_INDEPENDENCE_EVIDENCE.json`;
- validates that evidence with `tools/ai_context/validate_iar1_independence_evidence.py` and its regression suite;
- wires the independence-evidence validator/test into mandatory AI-context CI;
- restores the historical reconciliation markers required by current-truth validation.

## 5. Non-authorizations

This corrective follow-up does **not** authorize:

- BPV-1 implementation or execution;
- product runtime thaw;
- reducer v2;
- new Event verbs;
- a new database/language/product profile;
- license selection;
- Track H admission;
- Final Canon;
- maturity or production promotion.

Current next gate remains `BPV1_PLAN_AND_PREREGISTRATION`, and runtime expansion remains `FROZEN`.