# IAR-1 — follow-up позднего финального re-review

**Назначение:** сохранить post-merge chronology финального Codex re-review PR #107 и bounded fixes, необходимые до начала D4.

Финальный re-review PR #107 был запрошен на exact head `3ca47783cf1b4bde46158bce5aa183ceed82d0f5`. Review-agent принял запрос до merge, но опубликовал submission уже после squash merge PR #107 в `845f2c8e9322c5353f9d6b421e44d1da71b82f58`.

Поздний review дал четыре actionable findings:

1. **P1 — stale workflow gate tests**: три test-файла всё ещё требовали pre-IAR machine state `INDEPENDENT_ARCHITECTURE_REVIEW / NOT_ESTABLISHED`.
2. **P2 — stale documentation indexes**: `docs/README.md`, `docs/README.ru.md`, `docs/adr/README.md` всё ещё представляли independent review как current next gate.
3. **P2 — insufficient independence evidence guard**: `validate_architecture_freeze.py` проверял identity/flags reviewer, но не требовал substantive `independence_basis` и recorded input packet до принятия `QUALIFYING_REVIEW_COMPLETE`.
4. **P2 — incomplete preregistration-field guard**: validator не требовал exact required field inventory, поэтому `threat_model`/`oracle_authority` могли исчезнуть незаметно.

Этот follow-up исправляет все четыре finding без изменения runtime, contracts, profile semantics, evidence bytes, исходных IAR-1 findings, substantive IAR-1-R1 dispositions или operator-controlled решений.

```text
runtime_expansion: FROZEN
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
next gate after follow-up: BPV1_PLAN_AND_PREREGISTRATION
product_runtime_thaw: NO
production_authorized: false
```

Наличие этого follow-up корректирует более раннее sync-утверждение, что дополнительного финального review submission не появилось. Historical Notion/Issue text сохраняется; после merge и post-merge validation этого follow-up новый corrective checkpoint должен его supersede.