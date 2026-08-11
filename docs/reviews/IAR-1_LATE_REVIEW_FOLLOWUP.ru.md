# IAR-1 — Follow-up позднего review

> **Record identity:** `nk-independent-architecture-review/IAR-1-late-followup-1`  
> **Status:** `CORRECTIVE FOLLOW-UP ACTIVE`  
> **Parent review:** `IAR-1`  
> **Parent reconciliation:** `IAR-1-R1`  
> **Parent merge:** `845f2c8e9322c5353f9d6b421e44d1da71b82f58`  
> **Corrective PR:** `#108`  
> **Runtime expansion:** `FROZEN`

## 1. Почему существует этот follow-up

Финальный Codex reconciliation-quality re-review PR #107 был направлен на exact PR head `3ca47783cf1b4bde46158bce5aa183ceed82d0f5`, но опубликован уже после squash merge PR #107. Поэтому четыре actionable findings обрабатываются отдельным bounded corrective PR, а не молча переписывают уже merged chronology review.

Затем PR #108 получил ещё два P2 findings на своём первом reviewed head. Они являются частью той же corrective chronology и не исчезают после последующего thread resolution.

## 2. Поздние findings финального re-review PR #107

1. stale A9/A10/integrated-review workflow tests могли принять validation status до reconciliation;
2. current documentation indexes всё ещё описывали independent review как следующий gate;
3. IAR-1 independence-basis guard слишком зависел от prose;
4. inventory полей BPV-1 preregistration не применялся достаточно строго.

## 3. Дополнительные findings review PR #108

1. A9/A10/integrated-review slice tests должны явно проверять, что `post_blueprint_validation.status` содержит `RECONCILIATION_COMPLETE`;
2. generic padded `independence_basis` всё ещё мог пройти architecture-freeze validator, если validation gate не требует repository-visible structured independence evidence.

## 4. Corrective disposition

Поэтому follow-up:

- сохраняет historical состояния документов A9/A10/integrated-review, одновременно проверяя current machine gate;
- требует от slice tests явной проверки `RECONCILIATION_COMPLETE`;
- обновляет current documentation indexes до `IAR-1 complete / IAR-1-R1 complete / BPV1 plan next`;
- сохраняет exact preregistration field inventory и fail-closed проверки duplicate/missing fields;
- фиксирует repository-visible evidence разделения reviewer для IAR-1 в `docs/reviews/IAR-1_INDEPENDENCE_EVIDENCE.json`;
- проверяет эти evidence через `tools/ai_context/validate_iar1_independence_evidence.py` и regression suite;
- подключает independence-evidence validator/test к обязательному AI-context CI;
- восстанавливает historical reconciliation markers, требуемые current-truth validation.

## 5. Non-authorizations

Этот corrective follow-up **не** разрешает:

- BPV-1 implementation или execution;
- product runtime thaw;
- reducer v2;
- новые Event verbs;
- новый database/language/product profile;
- выбор license;
- Track H admission;
- Final Canon;
- maturity или production promotion.

Current next gate остаётся `BPV1_PLAN_AND_PREREGISTRATION`, а runtime expansion — `FROZEN`.