# IAR-1 — Follow-up позднего review

> **Record identity:** `nk-independent-architecture-review/IAR-1-late-followup-1`  
> **Status:** `CORRECTIVE FOLLOW-UP ACTIVE`  
> **Parent review:** `IAR-1`  
> **Parent reconciliation:** `IAR-1-R1`  
> **Parent merge:** `845f2c8e9322c5353f9d6b421e44d1da71b82f58`  
> **First corrective merge:** `e465b7019040913c3a5bd2d4344eb2dea74cc60c` (`PR #108`)  
> **Runtime expansion:** `FROZEN`

## 1. Почему существует этот follow-up

Финальный Codex reconciliation-quality re-review PR #107 был направлен на exact PR head `3ca47783cf1b4bde46158bce5aa183ceed82d0f5`, но опубликован уже после squash merge PR #107. Поэтому четыре actionable findings были обработаны отдельным bounded corrective PR, а не молча переписали уже merged chronology review.

Затем PR #108 получил дополнительные review findings. Его финальный exact-head Codex review был направлен на `157be487a6727cf0ec2a36988ad5ab203ba5e0b2` и опубликован только после squash merge PR #108 как `e465b7019040913c3a5bd2d4344eb2dea74cc60c`. Эти post-merge findings требуют второго bounded corrective follow-up до закрытия D3.

## 2. Поздние findings финального re-review PR #107

1. stale A9/A10/integrated-review workflow tests могли принять validation status до reconciliation;
2. current documentation indexes всё ещё описывали independent review как следующий gate;
3. IAR-1 independence-basis guard слишком зависел от prose;
4. inventory полей BPV-1 preregistration не применялся достаточно строго.

## 3. Дополнительные findings review-цикла PR #108

Более ранние findings PR #108 потребовали:

1. явных aggregate reconciliation-state assertions в A9/A10/integrated-review slice tests;
2. structured repository-visible independence evidence вместо generic `independence_basis` prose;
3. восстановления exact AI-context continuity markers;
4. current bilingual parity registration вместо obsolete pre-reconciliation literals;
5. exact reviewer actor token в evidence fixture;
6. обязательного CI execution independence-evidence validator и regression suite;
7. exact aggregate phase equality вместо substring matching;
8. привязки reviewer к exact GitHub review submission `4904562661` и его canonical identity digest.

Финальный exact-head review PR #108 добавил ещё три P2 findings:

9. exact review submission commit `925a33f33d1a252a71475d11d82edd2c53307dbb` должен быть cross-bound с `IAR-1_RESULT.json.review_request_commit`;
10. current EN/RU documentation indexes требуют fail-closed exact-gate registration, чтобы оба документа не могли одновременно откатиться к старому review gate;
11. mandatory IAR-1 input packet должен быть нормализован до конкретных named paths, а не опираться только на broad category labels.

## 4. Final corrective disposition

Поэтому второй corrective follow-up:

- сохраняет historical category attestation `IAR-1_RESULT.json.input_packet_read`, не переписывая source review evidence;
- добавляет `IAR-1_INPUT_PACKET_EVIDENCE.json`, разворачивающий mandatory named-file packet в 23 exact duplicate-free paths и явно фиксирующий отсутствие per-file reviewer access telemetry;
- проверяет существование этих paths на immutable reviewed commit, сохраняя честную границу P1-C5 exact-file telemetry (`NOT_AVAILABLE`);
- cross-bind exact review submission `4904562661` с `IAR-1_RESULT.json.review_request_commit`;
- сохраняет exact review-submission actor/commit/digest guard;
- регистрирует current docs-index gate в `tools/docs/current-gate-pairs-v1.json` через восемь exact required literals и три forbidden pre-reconciliation literals;
- проверяет этот current-gate registry уже обязательным bilingual-parity regression suite;
- оставляет BPV-1 execution заблокированным, а product runtime — frozen.

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