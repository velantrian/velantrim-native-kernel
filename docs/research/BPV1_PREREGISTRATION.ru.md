# BPV-1 — Preregistration cross-lineage bounded-accountability

**[English](./BPV1_PREREGISTRATION.md) · [Русский](./BPV1_PREREGISTRATION.ru.md)**

> **Protocol:** `nk-bpv1-preregistration/1`  
> **Scenario:** `BPV1-001-cross-lineage-bounded-accountability-v1`  
> **Статус после authoritative merge:** `PREREGISTERED / EXECUTION_NOT_AUTHORIZED`  
> **Роль:** `FALSIFICATION_INSTRUMENT_ONLY`  
> **Architecture checkpoint:** `c5d76fe281606edc0053bd7fc65167ebdfa50992`  
> **Runtime expansion:** `FROZEN`

## 1. Назначение

BPV-1 — не ещё один runtime Native Kernel. Это bounded попытка заставить provisional architecture **провалиться**, если её обязательства на самом деле зависят от нынешней реализации.

Сценарий задаёт один узкий вопрос:

> Могут ли reconciled minimum obligations Native Kernel сохраниться в существенно другой single-node реализации, написанной не на Python, **без** Event sourcing как authoritative history model и с bounded retained durable experimental state, при этом сохраняя declared accountability и loss semantics?

Положительный результат будет более сильным evidence, чем PostgreSQL↔SQLite внутри одной Python lineage, но **не** докажет universal substrate independence, independent team/custody, поддержку будущего hardware, Final Canon, production readiness или пригодность как product runtime.

Primary A10 targets: `A10-H02`, `A10-H05`. Secondary: `A10-H01`, `A10-H04`, `A10-H07`, `A10-H12`. Сценарий также должен дать конкретное evidence для `A10-Q01`, `Q02`, `Q04`, `Q10`, `Q13`, `Q14`, `Q18`.

## 2. Граница experimental lineage

Планируемый subject — **experimental Rust instrument**.

Rust выбран только как materially different implementation-language lineage. Он не становится требованием Canon и не становится product profile из-за использования в этом эксперименте.

Реализация должна самостоятельно вывести state/change/history representation из problem-level obligations этого preregistration. Нельзя:

- зависеть от `native_kernel/**` как runtime code;
- механически переводить текущие Python domain classes;
- использовать текущий Event envelope как native history representation;
- использовать текущий reducer как semantic engine;
- копировать текущую SQL schema как native state shape;
- использовать текущий Receipt shape как conformance oracle;
- требовать exact replay или global total order только потому, что это делает laboratory.

Предполагаемая state model — bounded current state + lineage summaries + explicit loss witnesses. Authoritative per-operation append-only Event log запрещён. Малый bounded crash journal разрешён только как recovery mechanism, максимум восемь entries, и не может определять semantic history.

Implementation остаётся conventional digital computation и находится в том же repository custody. Independent team/custody и independent computation model в BPV1-001 **не установлены**.

## 3. Замороженная workload

Bounded-memory workload фиксируется до реализации:

```text
active claim slots: 32
revision cycles: 16
scripted mutations: 512
measurement checkpoints: 128 / 256 / 512 mutations
compaction: after every revision cycle
durable experimental-state cap: 262,144 bytes
retained detailed predecessors: <= 64
loss witnesses: <= 32
authoritative per-operation append log: forbidden
bounded crash journal: <= 8 entries; not semantic Authority
```

“Bounded memory” здесь означает **bounded retained durable experimental semantic state**, а не process RSS или поведение allocator.

На финальном checkpoint:

```text
durable_bytes_at_512 <= durable_bytes_at_256 * 1.25 + 4096
```

Это threshold конкретного сценария, а не универсальный закон Native Kernel.

## 4. Exact preregistration fields

Следующие двенадцать полей нормативны и ровно соответствуют inventory из IAR-1-R1. Любое post-execution изменение normative field инвалидирует run для заявленного scope и требует новый scenario identity.

### 4.1 `scenario_id`

`BPV1-001-cross-lineage-bounded-accountability-v1`

### 4.2 `purpose_scope`

Single-node, non-composed, conventional-digital falsification scenario. Проверяется только cross-language + different history/state-model preservation.

Явные non-claims:

- production readiness;
- universal substrate portability;
- independent team/custody;
- analog/neuromorphic/probabilistic support;
- composition/federation;
- physical/cryptographic erasure proof;
- performance superiority;
- product-runtime suitability.

### 4.3 `mandatory_obligations`

Для declared scope должны сохраниться все пункты:

1. Representation или Claim не приравниваются молча к reality/objective truth.
2. Material Context, warrant/provenance и scoped Authority остаются inspectable без обязательной текущей Python field layout.
3. Unknown, uncertainty и unsupported остаются representable без coercion в False или fabricated certainty.
4. Revision, supersession, retention и loss остаются accountable для declared retained scope без silent overwrite.
5. Equivalence, degradation и loss классифицируются preregistered oracle, а не self-report реализации.
6. `CURRENT_ACCOUNTABILITY` доступен для каждого retained active claim slot.
7. `DECLARED_RETENTION_SCOPE` explicit и machine-observable.
8. `LOSS_WITNESS` существует всякий раз, когда detail compacted за пределами retained scope.
9. Unresolved plurality сохраняется, если preregistered Authority rule не выбирает winner.
10. Всё это достигается без canonical per-operation Event log или exact replay как authoritative history.

### 4.4 `applicability_rules`

Applicable:

- single-node / non-composed;
- bounded durable semantic state;
- non-event-sourced authoritative history;
- independent implementation language: Rust.

Declared limitations:

- same repository custody;
- independent team не установлен;
- independent computation model не установлен;
- mandatory только identity/time dimensions, прямо названные fixture.

`NOT_APPLICABLE` с preregistered rationale:

- physical erasure — нет independently observable physical-erasure channel;
- cryptographic erasure — нет key-destruction substrate claim;
- composition/federation — separate capability class;
- exact replay и global total order — не universal requirements этого сценария.

Изменение applicability после начала execution инвалидирует run для заявленного scope.

### 4.5 `mandatory_observables`

External evaluator должен видеть без implementation-private semantic authority:

- current claim/proposition state и epistemic position;
- material Source/Evidence/Provenance/Authority distinctions там, где fixture делает их значимыми;
- Context binding;
- retained revision/supersession relation;
- declared retention scope;
- bounded loss witness после compaction;
- unresolved plurality, если winner не разрешён;
- explicit `LOSSY`, `UNSUPPORTED`, `INDETERMINATE`;
- durable state size и retained detail/witness counts на 128/256/512 mutations;
- наличие/отсутствие authoritative per-operation append log;
- rollback/truncation и forged-Authority failure semantics;
- evaluator-owned conformance result.

### 4.6 `equivalence_predicates`

Machine-readable plan фиксирует predicates `EQ01`–`EQ10`.

Главное правило: semantic equivalence — scoped и meaning-level. Совпадение bytes, IDs, storage layout, write sequence, Event envelope, reducer state, Receipt bytes или SQL schema не является ни необходимым, ни достаточным.

Full conformance запрещён, если final values совпадают, но materially расходятся provenance, Authority, Context, uncertainty или declared-loss semantics.

### 4.7 `allowed_declared_losses`

Разрешена явная потеря:

- exact bytes/storage addresses superseded detail вне retained scope;
- per-operation write chronology вне retained accountability scope;
- exact replay;
- native A3 transition и A6 lifecycle representations;
- current Event/reducer/Receipt/SQL/ID/hash forms;
- A5 identity/time dimensions, не названных fixture;
- superseded detail после compaction, **только** при valid bounded `LOSS_WITNESS`;
- bounded crash-journal entries после recovery, если они не являются semantic history.

Никакой loss внутри declared retained accountability scope не может быть silent.

### 4.8 `failure_thresholds`

Semantic failures не усредняются баллами.

```text
semantic hard failures allowed: 0
mandatory fixture failures allowed: 0
Unknown→False coercions allowed: 0
silent retained-scope losses allowed: 0
unauthorized conflict-winner selections allowed: 0
material role collapses allowed: 0
authoritative per-operation append log: forbidden
durable state cap: 262,144 bytes
retained detailed predecessors: <= 64
loss witnesses: <= 32
required mutations: 512
required measurement checkpoints: 3
```

Если mandatory observable нельзя независимо оценить, соответствующий predicate получает `INDETERMINATE`, а не PASS.

### 4.9 `hard_refutation_observations`

Plan фиксирует `HR01`–`HR10`. Среди них:

- необходимость authoritative unbounded/per-operation Event log для required accountability ослабляет/опровергает `A10-H02` для scope;
- невозможность compaction с сохранением current accountability, retention scope и truthful loss witness ослабляет/опровергает `A10-H05`;
- forced Unknown→False или unresolved plurality→winner опровергает `A10-H04` для scope;
- необходимость current A3/A6/Event/reducer/Receipt shape для minimum ослабляет `A10-H01` и не позволяет считать эти структуры independently rediscovered;
- одинаковые final values при materially different provenance/Authority/uncertainty/loss refute full semantic equivalence fixture;
- копирование current Python conceptual/runtime structures инвалидирует intended evidence class для `A10-H07`;
- silent retained-scope loss refutes bounded-accountability conformance;
- silent acceptance rollback/truncation/forged Authority refutes соответствующий protected meaning;
- post-execution изменение normative rules инвалидирует run;
- oracle, зависящий от implementation-private self-report, делает run non-qualifying.

### 4.10 `grounding_mode`

`EXPLICIT_ASSUMED_ROOT`.

BPV1 fixture/oracle package — explicit experimental root, а не objective world truth. Provenance/Authority chains заканчиваются на этом root или `TERMINAL_UNKNOWN_OR_GAP`; hidden infinite grounding не допускается.

### 4.11 `threat_model`

Protected meanings:

- declared provenance и scoped Authority basis;
- current accountability внутри retained scope;
- revision/supersession relation;
- declared retention/loss boundary;
- conformance observations/evidence.

Mandatory adversarial cases: forgery, truncation, rollback, equivocation, withheld counterevidence, unavailable witness, forged Authority/provenance.

Colluding-witness, compromised external certifier и physical-residue cases — `NOT_APPLICABLE` для BPV1-001 с explicit rationale в machine plan.

### 4.12 `oracle_authority`

`BPV1-ORACLE-001`.

После merge `docs/research/BPV1_PREREGISTRATION.json` становится normative experiment-oracle source только для BPV1-001.

Implementation under test не может изменять oracle или определять expected results.

Перед execution отдельный `BPV1_EXECUTION_ADMISSION` должен связать:

- authoritative preregistration;
- frozen digest;
- machine-readable fixture/oracle package, derived только из этого plan;
- standalone evaluator tests, зелёные до subject execution;
- pinned Rust toolchain и experimental source boundary;
- static proof, что instrument не интегрирован в product runtime/profile paths.

## 5. Fixture families

Пререгистрированы двенадцать обязательных fixture families:

```text
BPV1-FX01  Unknown ≠ False
BPV1-FX02  role non-conflation
BPV1-FX03  Context binding
BPV1-FX04  revision / supersession
BPV1-FX05  unresolved plurality
BPV1-FX06  bounded compaction + LOSS_WITNESS
BPV1-FX07  truncation / rollback
BPV1-FX08  forged Authority
BPV1-FX09  withheld counterevidence
BPV1-FX10  declared loss / unsupported / indeterminate
BPV1-FX11  non-Event accountability
BPV1-FX12  hidden semantic divergence despite matching final values
```

Execution-admission package может сделать эти fixtures machine-executable, но не может менять их semantic purpose или normative predicates под тем же scenario identity.

## 6. A10 outcome discipline

Разрешены только:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

`NOT_TESTED ≠ SUPPORTED`.

Положительный BPV1 result усилит только tested scope. Он не доказывает future substrates, universal portability, Final Canon или production readiness.

## 7. Execution hard stop

Merge этого preregistration **не** разрешает D5 execution.

После authoritative merge состояние должно стать:

```text
BPV-1 plan: PREREGISTERED / AUTHORITATIVE
next gate: BPV1_EXECUTION_ADMISSION
BPV-1 execution: BLOCKED_PENDING_EXECUTION_ADMISSION
runtime expansion: FROZEN
product runtime thaw: NO
production: false
```

D5 начинается только после отдельного admission checkpoint. Любая implementation/execution BPV1-001 до этого gate — process failure, а не experimental evidence.
