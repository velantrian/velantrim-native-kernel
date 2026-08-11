# IAR-1 — результат независимого архитектурного ревью

**Результат процесса:** `QUALIFYING_REVIEW_COMPLETE`  
**Протокол:** `nk-independent-architecture-review/1`  
**Протокол результата:** `nk-independent-architecture-review-result/1`  
**Проверенный commit архитектуры:** `2dd51723e30d5f3c5e86268365bf4cf7639b5e9a`  
**Review surface:** PR #107  
**Reviewer:** `github-codex-review-agent`  
**Тип reviewer:** `AGENT`  
**Runtime:** `FROZEN`  
**BPV-1:** `BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION`

## Основание независимости

Reviewer является отдельным GitHub review-agent. В repository-visible contributor/collaborator history присутствует только `velantrian`; reviewer не участвовал в написании A1–A10 или `nk-integrated-blueprint-review/A1-A10-review-1`, получил неизменяемый объект проверки только после публикации и использовал текущий P1–C5 runtime лишь как контекст для поиска implementation capture, а не как архитектурный oracle.

Это удовлетворяет требованию concrete separation протокола для **этого review**. Это не означает, что будущая реализация BPV-1 автоматически станет независимой только из-за другого языка или инструмента.

## Полнота ревью

- обязательный input packet прочитан: **YES**;
- Q1–Q12: **покрыты полностью**;
- итоговый register: **10 findings**;
- `BLOCKING`: **7** — `IAR-F01`, `IAR-F02`, `IAR-F03`, `IAR-F05`, `IAR-F07`, `IAR-F08`, `IAR-F09`;
- `MATERIAL`: **3** — `IAR-F04`, `IAR-F06`, `IAR-F10`;
- product runtime остаётся `FROZEN`;
- BPV-1 должен оставаться заблокированным до reconciliation.

GitHub review comments являются исходным review evidence. `docs/reviews/IAR-1_RESULT.json` — машиночитаемая транскрипция и guard-surface.

## Сводка Q1–Q12

### Q1 — минимальный Kernel

Защищаемый минимум меньше полной таксономии A1–A10: нужны неслияние representation/Claim с reality/truth, явные scope/Context/warrant, явная uncertainty, accountable change/loss и заранее объявленные правила equivalence/capability. Полные инвентари A2, A3 и A6 пока не доказаны как необходимые архитектурные формы.

### Q2 — независимость от event sourcing

Append-only Events и exact replay сами по себе не обязательны. Но прежние требования accountability/reconstruction могли фактически заставлять воспроизводить эквивалент event log, если не разделить state accountability, revision lineage и reconstruction.

### Q3 — bounded memory

При конечной памяти можно сохранить scoped current claims, uncertainty, summarized provenance, declared loss и bounded decision accounts. Нельзя обещать бесконечное exact reconstruction, постоянную видимость всех predecessors и неограниченное reopening без retention budget или ослабления обязательства.

### Q4 — identity

Stable bytes, hashes и global IDs не являются универсальным требованием. При этом draft всё ещё сильнее необходимого предполагает стабильные различимые relata и continuity evidence; часть identity kinds должна остаться аналитическим языком, а не обязательным inventory conformance.

### Q5 — time/order

Universal total order не требуется, но lineage предполагает локально согласованный predecessor/successor relation. Требуется лишь минимальный partial order для заявленного causal/lineage scope; полный набор временных измерений не должен считаться универсально обязательным.

### Q6 — epistemic separation

Source, Provenance и Authority могут быть ролями/procedures, не текущими полями. Evidence может быть derived. Portable obligation — не смешивать смысловые роли там, где они материальны, а не хранить четыре обязательных first-class объекта.

### Q7 — conflict/uncertainty

Unresolved plurality и non-scalar uncertainty жизнеспособны. `Conflict ≠ Contradiction` остаётся слишком гибким без preregistered proposition identity, logic/conflict relation, Context/time alignment, assessment Authority и допустимых unresolved outcomes.

### Q8 — deletion/forgetting

Restriction, logical erasure, physical erasure, cryptographic erasure и forgetting различимы как типы утверждений. Но physical/crypto erasure требует threat-scoped external evidence; forgetting — утверждение об epistemic accessibility, а не доказательство глобального несуществования.

### Q9 — conformance

Representation-independent conformance возможен только при внешнем preregistered scenario-to-obligation oracle: mandatory observables, applicability, equivalence и failure thresholds фиксируются до implementation. Profile не должен выбирать их после результата.

### Q10 — capture лабораторией

Главные риски recapture — не только Python/SQL: A3 command/outcome algebra, transition records, reducer-like reconstruction boundary, Receipts, lineage model, current IDs, exact fixtures и deterministic expected outputs.

### Q11 — независимая реализация

Cross-lineage realization должна независимо вывести state/change model, identifiers, storage/history strategy, result vocabulary, fixtures и semantic oracle из problem-level obligations. Смена языка при копировании A3/A6 — только порт.

### Q12 — условия опровержения

Минимально необходимо заранее признать:

1. non-event realization сохраняет минимальную цель, но не A3/A6 каталоги → ослабить каталоги;
2. bounded compaction сохраняет current semantics + loss witness, но не superseded detail → ослабить universal reconstructability;
3. final outputs совпадают, но materially различаются provenance/uncertainty/Authority → full semantic equivalence refuted for scope;
4. opaque substrate не даёт независимого evidence physical erasure → результат `INDETERMINATE` для этого scope.

## Findings

| ID | Severity | Исходный status | Рекомендация | BPV-1 | Суть |
|---|---|---|---|---|---|
| IAR-F01 | BLOCKING | OPEN | CLARIFY | BLOCKS | conformance scope/oracle может меняться post hoc |
| IAR-F02 | BLOCKING | OPEN | SPLIT | BLOCKS | A3/A6 несут форму текущей лаборатории |
| IAR-F03 | BLOCKING | OPEN | SPLIT | BLOCKS | bounded accountability не отделён от reconstruction |
| IAR-F04 | MATERIAL | OPEN | SPLIT | SHOULD_INFORM | identity/time inventory сильнее необходимого |
| IAR-F05 | BLOCKING | OPEN | CLARIFY | BLOCKS | epistemic/conflict границы недостаточно operationalized |
| IAR-F06 | MATERIAL | OPEN | SPLIT | SHOULD_INFORM | erasure assertion смешан с verified substrate condition |
| IAR-F07 | BLOCKING | OPEN | TEST | BLOCKS | недостаточная защита от post-hoc rescoping |
| IAR-F08 | BLOCKING | OPEN | SPLIT | BLOCKS | отсутствует architecture-level threat model |
| IAR-F09 | BLOCKING | OPEN | CLARIFY | BLOCKS | Context/Provenance/Authority может рекурсировать бесконечно |
| IAR-F10 | MATERIAL | OPEN | TEST | SHOULD_INFORM | composition/federation не определены |

Исходный review register не переписывается: его findings сохраняются как review-local `OPEN`. Их последующее разрешение записано отдельно в `IAR-1-R1`.

## Candidate claims, пережившие challenge

Как **кандидаты**, а не Final Canon:

- representation ≠ represented reality;
- Claim ≠ truth;
- Unknown ≠ False;
- Context, Provenance и Authority scoped;
- implementation/write order ≠ causal/semantic precedence;
- Revision, Supersession и erasure неэквивалентны;
- loss и conformance должны быть явными.

## Что остаётся provisional

- полный A2 ontology;
- A3 transition/outcome machine;
- A4 law package как единый обязательный набор;
- A5 identity/time taxonomy;
- A6 lifecycle graph;
- universal reconstruction/history;
- full A8 equivalence;
- independently verifiable erasure;
- широкая substrate independence.

## Gate

```text
independent_review_status: QUALIFYING_REVIEW_COMPLETE
finding_reconciliation: REQUIRED
open BLOCKING findings at review time: 7
BPV-1: BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION
runtime_expansion: FROZEN
product_runtime_thaw: NO
A1-A10: DRAFTED / PROVISIONAL
production_authorized: false
```

Следующий документ `IAR-1_RECONCILIATION` фиксирует отдельные архитектурные dispositions; сам факт qualifying review ничего не промоутит автоматически.
