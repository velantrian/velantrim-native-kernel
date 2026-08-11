# IAR-1 — reconciliation архитектурных findings

**Reconciliation identity:** `IAR-1-R1`  
**Протокол:** `nk-independent-architecture-review-reconciliation/1`  
**Input review:** `IAR-1 / QUALIFYING_REVIEW_COMPLETE`  
**Состояние архитектуры:** `PROVISIONAL_RECONCILED`  
**Runtime:** `FROZEN`  
**Следующий gate после authoritative merge:** `BPV1_PLAN_AND_PREREGISTRATION`  
**BPV-1 execution:** `NOT AUTHORIZED`

## 1. Зачем нужна reconciliation

IAR-1 показал, что часть привлекательных структур A1–A10 всё ещё была сильнее имеющегося evidence. Эта reconciliation не защищает старую форму. Она намеренно **уменьшает и разделяет** provisional architecture, чтобы BPV-1 мог реально её опровергнуть, а не просто воспроизвести Python/Event/reducer lineage.

A1–A10 сохраняются как first-draft provenance. Если этот документ противоречит их формулировке, `IAR-1-R1` является текущим provisional overlay до integrated re-review или отдельного operator Canon decision.

## 2. Меньший минимальный Kernel

Текущий minimum candidate ограничен problem-level obligations:

1. representation и Claim не смешиваются молча с represented reality или truth;
2. scope, Context, warrant/provenance и Authority assumptions явны там, где это materially relevant;
3. `Unknown`, uncertainty и unsupported states могут существовать без coercion к `False`;
4. change, revision, supersession, retention и loss accountable для объявленного scope;
5. equivalence, capability, degradation и loss оцениваются по preregistered observables и failure conditions.

Следующее остаётся полезной **reference taxonomy**, но не universal minimum shape:

- полный A2 ontology inventory;
- A3 `K → K′`, fixed transition catalogue и common outcome vocabulary;
- A5 seven identity kinds/eight temporal dimensions как обязательный единый inventory;
- A6 nine lifecycle positions;
- Receipt-shaped accountability;
- Event-log-shaped history;
- exact reconstruction/replay.

Future realization может использовать snapshots, witnesses, procedural accounts, bounded summaries или иной state/change model, если сохраняет preregistered obligations своего scope.

## 3. Preregistered conformance oracle

До реализации BPV-1 план обязан зафиксировать:

```text
scenario_id
purpose_scope
mandatory_obligations
applicability_rules
mandatory_observables
equivalence_predicates
allowed_declared_losses
failure_thresholds
hard_refutation_observations
grounding_mode
threat_model
oracle_authority
```

Правила:

- implementation под тестом не решает после исполнения, какие обязательства были mandatory;
- `NOT_APPLICABLE` требует preregistered rationale;
- post-execution изменение obligations/applicability/equivalence/failure thresholds **делает run недействительным для заявленного scope**;
- новый scope = новый experiment identity; старый result сохраняется;
- full conformance требует сохранения каждого mandatory obligation, а не только совпадения final outputs.

Это закрывает `IAR-F01` и `IAR-F07`.

## 4. Accountability без universal Event sourcing / exact reconstruction

Accountability и reconstructability разделяются.

Candidate required classes:

- `CURRENT_ACCOUNTABILITY` — current scoped position и material warrant/loss state inspectable;
- `DECLARED_RETENTION_SCOPE` — объявлено, какая historical detail сохраняется и в каком budget;
- `LOSS_WITNESS` — compaction/forgetting вне retention scope оставляет явную границу loss, чтобы silent overwrite не выдавался за сохранённую историю.

Optional capabilities, если scenario не требует их заранее:

- `EXACT_RECONSTRUCTION`;
- permanent predecessor visibility;
- exact replay;
- complete provenance forever;
- unbounded reopening.

Compaction вне retention scope может быть conformant. Silent overwrite внутри retained accountability scope — нет.

Это закрывает `IAR-F02` и `IAR-F03`.

## 5. Identity, time, order

A5 taxonomies остаются analytical vocabulary. Scenario объявляет только те identity relations и temporal/order dimensions, которые действительно material.

Реализация не обязана экспонировать все семь identity kinds или восемь temporal dimensions. Неподдержанная необходимая distinction должна дать `PARTIAL`, `LOSSY`, `UNSUPPORTED` или `INDETERMINATE`, а не скрываться.

Global total order не вводится. При необходимости lineage требуется лишь минимальный local partial order, делающий заявленный predecessor/successor или causal relation осмысленным.

Это закрывает `IAR-F04`.

## 6. Epistemic roles и conflict

Portable requirement — **non-conflation semantic roles**, не mandatory storage fields.

Source, Provenance и Authority могут быть procedural/relational/external-witness representations. Evidence может быть derived.

Каждый conflict/contradiction scenario заранее объявляет:

```text
proposition_identity_predicate
logic_or_conflict_relation
context_alignment_rule
temporal_alignment_rule
assessment_authority
allowed_unresolved_outcomes
```

`Conflict` остаётся более широкой tension category. `Contradiction` зависит от logic/scope. После исполнения нельзя спасать failed case переименованием в context mismatch или другой Authority decision, если это не было preregistered.

Это закрывает `IAR-F05`.

## 7. Deletion, erasure, forgetting

Разделяются три evidence layers:

1. **logical disposition claim** — restriction/logical erasure внутри semantic system;
2. **substrate-condition claim** — physical/cryptographic erasure при объявленном observation boundary/threat model;
3. **epistemic accessibility claim** — forgetting/loss относительно accessible sources и retained evidence.

Physical/cryptographic erasure нельзя повысить из self-assertion. Требуется threat-scoped evidence с отдельно объявленной verification Authority. При недостатке evidence результат `INDETERMINATE`.

Forgetting никогда не доказывает global nonexistence.

Это закрывает `IAR-F06`.

## 8. Architecture-level threat model

Перед тестом accountable provenance/history/conformance scenario объявляет protected meanings, trust roots/assumptions, adversary capabilities и failure semantics.

Где relevant, negative cases включают:

- forged Source/provenance/Authority;
- history fork;
- truncation;
- rollback;
- equivocation;
- withheld counterevidence;
- unavailable witness;
- colluding witness;
- compromised conformance certifier.

Architecture не требует единого crypto mechanism. Она требует явных trust assumptions и failure/uncertainty semantics.

Это закрывает `IAR-F08`.

## 9. Finite grounding Context / Provenance / Authority

Evaluation chain обязан иметь один явный finite grounding mode:

- `EXTERNALLY_ATTESTED_ROOT`;
- `EXPLICIT_ASSUMED_ROOT`;
- `BOUNDED_RECURSIVE_CLOSURE`;
- `DECLARED_CYCLE`;
- `TERMINAL_UNKNOWN_OR_GAP`.

Infinite recursion не усиливает support. Cycles, assumptions и terminal gaps являются частью meaning и остаются inspectable.

Это закрывает `IAR-F09`.

## 10. Composition — отдельный capability class

Base substrate-independence claims сужаются до **scoped, non-composed realizations**.

Local conformance не означает federation/composition conformance. Future composed test отдельно определяет:

- overlapping Contexts;
- identity disagreement;
- provenance union/loss;
- Authority conflict;
- concurrency;
- partial failure;
- правила сохранения plurality или projection в common scope.

Base architecture не подразумевает centralized coordinator.

Это закрывает `IAR-F10` без ложного заявления, что distributed composition уже решён.

## 11. Hard refutation observations для BPV-1

BPV-1 preregistration обязан сохранить их без ослабления либо сделать строже:

1. non-event realization сохраняет minimum purpose, но не A3/A6 catalogues → **ослабить catalogues, не отвергать realization**;
2. bounded compaction сохраняет current semantics + loss witness, но не superseded detail → **ослабить universal reconstructability/history**;
3. profiles совпадают по final output, но materially различаются provenance/uncertainty/Authority → **full semantic equivalence refuted for scope**;
4. opaque substrate не даёт independent physical-erasure evidence → **physical erasure = `INDETERMINATE` для scope**;
5. post-execution изменение obligations/applicability/equivalence/failure thresholds → **старый run нельзя спасать; нужен новый experiment identity**.

## 12. Dispositions

| Finding | D3 status | Архитектурный эффект |
|---|---|---|
| IAR-F01 | RESOLVED | external preregistered conformance oracle |
| IAR-F02 | RESOLVED | A3/A6/current laboratory shape → reference taxonomy |
| IAR-F03 | RESOLVED | bounded accountability отделён от exact reconstructability |
| IAR-F04 | RESOLVED | identity/time → scenario-required dimensions |
| IAR-F05 | RESOLVED | epistemic/conflict tests получают preregistered boundaries |
| IAR-F06 | RESOLVED | erasure claim отделён от substrate evidence |
| IAR-F07 | RESOLVED | hard refutations + no post-hoc rescue |
| IAR-F08 | RESOLVED | threat/trust boundary добавлен |
| IAR-F09 | RESOLVED | finite grounding modes добавлены |
| IAR-F10 | RESOLVED | composition становится отдельным capability class |

Machine authority: `docs/reviews/IAR-1_RECONCILIATION.json`.

## 13. Gate после reconciliation

```text
IAR-1: QUALIFYING_REVIEW_COMPLETE
IAR-1-R1: COMPLETE
open BLOCKING findings: 0
open MATERIAL findings: 0
A1-A10: DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY
BPV-1 plan: NEXT
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
runtime_expansion: FROZEN
product_runtime_thaw: NO
production_authorized: false
```

Эта reconciliation не доказывает правильность refined architecture. Она делает следующий falsification experiment способным потерпеть неудачу по правилам, заданным **до** implementation.
