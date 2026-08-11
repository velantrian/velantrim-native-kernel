# IAR-1 Late Review Follow-up

> **Record identity:** `nk-independent-architecture-review/IAR-1-late-followup-1`  
> **Status:** `CORRECTIVE FOLLOW-UP ACTIVE`  
> **Parent review:** `IAR-1`  
> **Parent reconciliation:** `IAR-1-R1`  
> **Parent merge:** `845f2c8e9322c5353f9d6b421e44d1da71b82f58`  
> **First corrective merge:** `e465b7019040913c3a5bd2d4344eb2dea74cc60c` (`PR #108`)  
> **Runtime expansion:** `FROZEN`

## 1. Why this follow-up exists

The final Codex reconciliation-quality re-review of PR #107 targeted exact PR head `3ca47783cf1b4bde46158bce5aa183ceed82d0f5` but published after PR #107 had already squash-merged. Four actionable findings were therefore handled in a separate bounded corrective PR rather than silently rewriting the merged review chronology.

PR #108 then received additional review findings. Its final exact-head Codex review targeted `157be487a6727cf0ec2a36988ad5ab203ba5e0b2` and was published only after PR #108 had squash-merged as `e465b7019040913c3a5bd2d4344eb2dea74cc60c`. Those post-merge findings require a second bounded corrective follow-up before D3 can close.

## 2. Late findings from PR #107 final re-review

1. stale A9/A10/integrated-review workflow tests could accept a pre-reconciliation validation status;
2. current documentation indexes still described independent review as the next gate;
3. the IAR-1 independence basis guard was too prose-dependent;
4. the BPV-1 preregistration field inventory was not enforced exactly enough.

## 3. Additional findings from PR #108 review cycle

Earlier PR #108 review findings required:

1. explicit aggregate reconciliation-state assertions in A9/A10/integrated-review slice tests;
2. structured repository-visible independence evidence rather than generic `independence_basis` prose;
3. restoration of exact AI-context continuity markers;
4. current bilingual parity registration rather than obsolete pre-reconciliation literals;
5. an exact reviewer actor token in the evidence fixture;
6. mandatory CI execution of the independence-evidence validator and regression suite;
7. exact aggregate phase equality rather than substring matching;
8. binding the reviewer to exact GitHub review submission `4904562661` and its canonical identity digest.

The final exact-head review of PR #108 added three further P2 findings:

9. exact review submission commit `925a33f33d1a252a71475d11d82edd2c53307dbb` must be cross-bound to `IAR-1_RESULT.json.review_request_commit`;
10. current EN/RU documentation indexes need a fail-closed exact-gate registration so both cannot regress together to the old review gate;
11. the mandatory IAR-1 input packet must be normalized to concrete named paths instead of relying only on broad category labels.

## 4. Final corrective disposition

The second corrective follow-up therefore:

- preserves the historical `IAR-1_RESULT.json.input_packet_read` category attestation rather than rewriting source review evidence;
- adds `IAR-1_INPUT_PACKET_EVIDENCE.json`, which expands the mandatory named-file packet to 23 exact, duplicate-free paths and explicitly records that per-file reviewer access telemetry was not exposed;
- verifies those paths existed at the immutable reviewed commit while keeping the P1-C5 exact-file telemetry boundary honest (`NOT_AVAILABLE`);
- cross-binds exact review submission `4904562661` to `IAR-1_RESULT.json.review_request_commit`;
- maintains the exact review-submission actor/commit/digest guard;
- registers the current docs-index gate in `tools/docs/current-gate-pairs-v1.json` with eight exact required literals and three forbidden pre-reconciliation literals;
- exercises that current-gate registry through the already mandatory bilingual-parity regression suite;
- leaves BPV-1 execution blocked and product runtime frozen.

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