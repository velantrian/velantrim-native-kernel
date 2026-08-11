# Протокол независимого архитектурного review

**Состояние:** `AUTHORIZED / REVIEW NOT YET ESTABLISHED`  
**Идентичность протокола:** `nk-independent-architecture-review/1`  
**Управляющее решение:** `ADR-0026`  
**Архитектурный issue:** `#88`  
**Предмет review:** provisional blueprint A1–A10 + integrated reconciliation  
**Runtime expansion:** `FROZEN`

## 1. Цель

Этот протокол определяет, как Native Kernel должен получить архитектурный review, который содержательно независим от той линии авторства, которая подготовила A1–A10 и выполнила первый integrated review.

Цель — не одобрение. Цель — **найти причины, по которым blueprint может быть неверным, чрезмерно определённым, нефальсифицируемым, захваченным текущей реализацией, внутренне циклическим или недостаточно переносимым**, до проектирования bounded cross-lineage эксперимента.

Review по этому протоколу сам по себе не продвигает Canon, runtime, maturity или production status.

## 2. Граница полномочий review

Квалифицирующий reviewer должен иметь заявленную идентичность и основание независимости, показывающее, что он не являлся автором проверяемого набора A1–A10 или `nk-integrated-blueprint-review/A1-A10-review-1`.

Запись review должна содержать:

```yaml
reviewer_identity: <declared>
reviewer_kind: HUMAN | AGENT | TEAM | OTHER
independence_basis: <почему reviewer содержательно отделён от линии авторства>
prior_authorship_of_A1_A10: false
prior_authorship_of_integrated_review: false
review_scope: A1-A10 + integrated reconciliation
review_mode: ADVERSARIAL_FALSIFICATION
current_runtime_used_as_architectural_oracle: false
```

Свежая сессия модели, другая модель или другой человек не становятся автоматически независимыми только по названию. В записи должно быть объяснено конкретное разделение, которое важно для review.

Если содержательная независимость не может быть установлена, фиксируется:

```text
INDEPENDENT_REVIEW_STATUS = BLOCKED_NO_QUALIFYING_REVIEWER
```

Самосертификация запрещена.

## 3. Обязательный пакет входных материалов

Reviewer должен получить архитектурные truth surfaces, а не только handoff-summary. Reviewer обязан прочитать `AGENTS.md`, а затем следовать актуальному mandatory orientation order, указанному там.

Минимальный пакет:

1. `AGENTS.md`
2. `README.md`
3. `STATUS.md`
4. `project-state.json`
5. `docs/ai/README.md`
6. `docs/ai/CURRENT_STATE.md`
7. `docs/ai/KNOWN_RISKS.md`
8. `ROADMAP.md`
9. `docs/ARCHITECTURE_REFOUNDATION.md`
10. английские документы A1–A10
11. `docs/INTEGRATED_A1_A10_REVIEW.md`
12. `docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md`
13. `docs/A9_REFERENCE_LABORATORY_BOUNDARY.md`
14. `docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.md`
15. `docs/adr/0025-blueprint-before-runtime-expansion.md`
16. `docs/adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md`
17. достаточный контекст P1–C5 contracts/evidence для обнаружения implementation capture, но без превращения этой реализации в нормативный authority.

Русские переводы могут использоваться как параллельная поверхность чтения, но не должны молча менять semantic status.

## 4. Мандат reviewer

Reviewer прямо поручается атаковать blueprint, а не делать его более убедительным.

Review должен пытаться найти:

- скрытую зависимость от Python, SQL, event sourcing, exact replay, JSON, SHA-256, текущих ID-схем, reducer semantics или conventional digital hardware;
- concepts, которые являются удобствами реализации, замаскированными под архитектуру;
- obligations, которые сильнее, чем требуется;
- concepts, которые можно удалить без потери смысла проекта;
- circular definitions или определения, зависящие от собственных выводов;
- нефальсифицируемые claims;
- конфликты между A1–A10, пропущенные первым integrated review;
- места, где могут неправильно схлопываться `Unknown`, `False`, `Unsupported`, `Indeterminate`, `Conflict`, `Contradiction`, `Resolution`, `Authority`, `Evidence`, `Source`, `Identity`, `Revision`, `Supersession`, `Deletion`, `Erasure` или `Forgetting`;
- portability claims, которые нельзя превратить в scoped preservation/loss tests;
- предположения о необходимости unbounded memory, global ordering, exact historical replay или permanent identifiers;
- obligations, которые не переживают lossy/probabilistic/bounded representations;
- противоречия между semantic accountability и forgetting/deletion;
- места, где laboratory evidence используется как доказательство архитектуры вместо bounded evidence.

## 5. Обязательные вопросы

Review должен ответить finding-ами либо явным `NO_FINDING_FOR_SCOPE` как минимум на следующие вопросы.

### Q1 — Минимальное ядро

Каков минимальный набор obligations, который всё ещё заслуживает имени Native Kernel? Какие concepts A1–A10 — полезная taxonomy, но не архитектурная необходимость?

### Q2 — Независимость от event sourcing

Можно ли определить accountability, revision lineage и reconstruction без превращения append-only Event history или exact replay в universal requirement?

### Q3 — Bounded memory

Какие obligations переживают finite storage, lossy compaction, forgetting или partial retention? Какие — нет?

### Q4 — Identity

Не зависит ли identity model сильнее заявленного от stable bytes, hashes, global IDs или exact state continuity?

### Q5 — Time и ordering

Достаточны ли различия occurrence, observation, write, causal и semantic precedence и не являются ли они циклическими? Не протаскивается ли total order через текущую machinery?

### Q6 — Epistemic separation

Могут ли Source, Evidence, Provenance и Authority оставаться различными в радикально другой реализации, или часть различий зависит от текущей data model?

### Q7 — Conflict и uncertainty

Сохраняет ли модель unresolved plurality без universal winner или scalar confidence? Есть ли случаи, где `Conflict ≠ Contradiction` становится неоднозначным?

### Q8 — Deletion и forgetting

Достаточно ли операционально различимы logical erasure, physical erasure, cryptographic erasure, restriction и forgetting, чтобы claims были falsifiable?

### Q9 — Conformance

Можно ли тестировать A8 conformance, не воспроизводя текущие representation choices? Где preservation criteria слишком расплывчаты для falsification?

### Q10 — Захват reference laboratory

Какие механизмы P1–C5 наиболее вероятно смогут вернуть Canon под контроль текущей реализации по инерции, несмотря на A9?

### Q11 — Независимая реализация

Что genuinely cross-lineage implementation должна сознательно не переиспользовать, чтобы будущий experiment не стал обычным портом Python-модели?

### Q12 — Refutation conditions

Назвать минимум три наблюдения, которые должны заставить проект ослабить или опровергнуть крупный architecture claim, а не переопределять тест до прохождения.

## 6. Формат finding

Каждый material finding получает стабильный локальный ID:

```text
IAR-F01
IAR-F02
...
```

Обязательные поля:

```yaml
finding_id: IAR-FNN
severity: BLOCKING | MATERIAL | MODERATE | MINOR
status: OPEN | RESOLVED
affected_slices: [A1, ...]
claim_or_obligation: <точный предмет>
finding: <что неверно или недостаточно обосновано>
counterexample_or_reasoning: <конкретная атака>
implementation_capture_risk: NONE | LOW | MEDIUM | HIGH
falsifiability_impact: NONE | LOW | MEDIUM | HIGH
recommended_disposition: REMOVE | WEAKEN | SPLIT | CLARIFY | TEST | RETAIN
bpv1_dependency: BLOCKS | SHOULD_INFORM | NONE
reconciliation_record: <обязательно при status=RESOLVED>
```

Finding не закрывается только потому, что текущие авторы с ним не согласны. Reconciliation обязан фиксировать rationale и evidence boundary. Назначенный recommended disposition сам по себе не означает resolution.

## 7. Правила severity

### `BLOCKING`

Используется, когда finding делает BPV-1 self-confirming, архитектуру incoherent или не позволяет отличить успех от провала.

Примеры:

- supposedly substrate-neutral obligation скрыто требует текущую Event/reducer модель;
- experiment не способен falsify claim, который должен тестировать;
- два core obligations несовместимы для заявленного scope.

Неразрешённый `BLOCKING` finding **всегда блокирует BPV-1**. Пока он имеет `status: OPEN`, его `bpv1_dependency` обязан быть `BLOCKS`. `TEST`, `RETAIN` или любой другой recommended disposition сам по себе не может обойти этот gate.

### `MATERIAL`

Finding способен существенно изменить Canon candidates или experiment design, но не делает всю validation phase недействительной.

### `MODERATE`

Значимая неоднозначность или неполная boundary, исправимая без перестройки центральной архитектуры.

### `MINOR`

Wording/indexing clarity без material semantic change.

## 8. Обязательные anti-confirmation rules

Reviewer не должен:

- считать текущие passing tests доказательством правильности архитектуры;
- выводить architecture necessity из существующей code structure;
- требовать identical bytes как доказательство semantic equivalence, если byte identity не является claim под тестом;
- повышать `NOT_TESTED` до support;
- превращать отсутствие counterexample в universal proof;
- закрывать философские open questions одним определением;
- предполагать, что будущий substrate обязан походить на database или event log;
- считать один только другой programming language достаточным доказательством cross-lineage independence.

## 9. Process outcomes review

Review получает один из process outcomes:

```text
QUALIFYING_REVIEW_COMPLETE
BLOCKED_NO_QUALIFYING_REVIEWER
INCOMPLETE_REVIEW
REVIEW_INVALIDATED_BY_INDEPENDENCE_FAILURE
```

Это статусы процесса review, а не A10 hypothesis outcomes.

Квалифицирующий review обязан выдать:

- reviewer identity и independence basis;
- reviewed commit SHA;
- identity/list входного пакета;
- register findings;
- явные ответы Q1–Q12;
- список stable candidate claims;
- список claims, которые должны остаться provisional;
- blocking/material findings, формирующие BPV-1;
- явную фиксацию, что product runtime остаётся frozen.

`QUALIFYING_REVIEW_COMPLETE` означает, что процесс review завершён по этому протоколу. Это **не означает**, что findings reconciled или что BPV-1 допущен.

## 10. Reconciliation gate перед BPV-1

BPV-1 остаётся `BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION`, пока:

- review не стал qualifying;
- каждый `BLOCKING` finding не имеет `status: RESOLVED` с конкретной reconciliation record;
- каждый unresolved `BLOCKING` finding, если он существует, сохраняет `bpv1_dependency: BLOCKS` и тем самым удерживает BPV-1 blocked;
- каждый `MATERIAL` finding не reconciled либо явно перенесён в experiment как falsification dependency;
- success/failure criteria experiment не записаны до implementation;
- ни один current runtime component не стал молча experiment oracle.

Нет исключения, позволяющего перенести open `BLOCKING` finding в BPV-1 просто как test target. Сначала blocker должен быть разрешён достаточно, чтобы experiment был non-self-confirming, architecture-coherent и способен различать success/failure.

## 11. Что доказывает завершение

Завершённый qualifying review доказывает только то, что архитектура прошла документированную независимую adversarial-проверку по этому protocol.

Он **не доказывает**:

- правильность A1–A10;
- universal portability;
- реализуемость на любом substrate;
- успех BPV-1;
- возможность runtime thaw;
- возможность finalize Canon;
- production readiness.