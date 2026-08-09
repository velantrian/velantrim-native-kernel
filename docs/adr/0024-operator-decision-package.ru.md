# ⚖️ Пакет operator decision по ADR-0024

**[English](./0024-operator-decision-package.md) · [Русский](./0024-operator-decision-package.ru.md)**

```yaml
document_role: OPERATOR_DECISION_PACKAGE
issue: 74
adr: ADR-0024
status_as_of: 2026-08-09
decision_state: PENDING_OPERATOR
selected_option: null
runtime_effect: REDUCER_V2_NOT_AUTHORIZED
```

> Этот пакет подготавливает финальное решение по versioned reducer referential semantics. Он не принимает ADR-0024 и не разрешает reducer-v2 runtime.

## 1. Подтверждённая проблема

Reducer v1 детерминирован для своего принятого порядка Events, но не обеспечивает более строгие referential rules, предлагаемые для будущих histories.

Текущие пробелы:

- `LINK` может ссылаться на Claims, которые никогда не были admitted;
- `UTILIZED` может ссылаться на unknown или erased Claims;
- `SUPERSEDED` может ссылаться на unknown successor, перезаписывать прежний successor, делать self-supersession или образовывать cycles;
- `ERASED` может ссылаться на unknown Claim;
- process-global reducer selection небезопасен, если разные histories требуют разных semantics.

Это реальный gap semantic contract, но не доказательство того, что существующие reducer-v1 histories недействительны по reducer v1.

## 2. Неизменяемая историческая граница

```text
reducer v1 history
≠ silently upgraded reducer v2 history
```

Существующие reducer-v1 histories, fixtures, state digests, Receipts и P1–C5 evidence продолжают интерпретироваться по опубликованному contract.

Для более строгой semantics нужны:

- новый reducer contract/version;
- явная binding history/instance;
- стабильные failure codes и locations;
- новые positive и negative fixtures;
- migration-assessment boundary;
- новая evidence identity;
- запрет переписывать historical evidence.

## 3. Варианты operator decision

### `ACCEPT`

Принять ADR-0024 в текущей редакции.

**Эффект:** разрешает contract-finalization в рамках существующего proposal, но сам по себе не разрешает runtime implementation, пока не завершены history commitment и version binding.

**Риск:** текущий ADR оставляет неявными exact failure codes, failure locations, duplicate `ADMIT`, repeated `ERASED`, restricted references и commitment dependency.

### `ACCEPT_WITH_CHANGES`

Принять архитектурное направление, но потребовать уточнения этого пакета до runtime work.

**Эффект:** сохраняет immutable v1 и разрешает финальный ADR, определяющий reducer v2, stable failures, per-history binding, bounded migration assessment и зависимости от NK-SAM/Event commitment.

**Техническая оценка:** это наиболее сильный engineering candidate, поскольку он закрывает ambiguity, не отказываясь от versioned-reducer direction.

### `REVISE`

Вернуть ADR-0024 на более широкую переработку.

**Эффект:** reducer-v2 runtime не начинается; proposal может изменить Event roles, relation semantics или migration architecture.

**Подходит, если:** оператор не согласен с referential enforcement внутри reducer или хочет сначала спроектировать Admission/typed relations.

### `REJECT`

Отклонить versioned stricter referential semantics.

**Эффект:** reducer v1 остаётся единственным accepted reducer; Issue #74 закрывается как rejected либо заменяется другим proposal.

**Риск:** unknown, erased и cyclic references остаются допустимыми accepted reducer, если их не отклоняет другой contract layer.

## 4. Техническая рекомендация — не решение

```text
recommended engineering option: ACCEPT_WITH_CHANGES
operator selection:             UNSET
```

Причины:

- immutable reducer v1 защищает historical evidence;
- reducer v2 — минимальный явный путь добавить stricter semantics без reinterpretation;
- per-history binding исключает process-global semantic drift;
- migration assessment классифицирует старые histories без их переписывания;
- stable failure codes позволяют сравнивать PostgreSQL, SQLite и будущие independent implementations;
- первый v2 slice может не включать полный Admission, Temporal и typed relations.

## 5. Обязательные изменения для `ACCEPT_WITH_CHANGES`

### 5.1. Порядок зависимостей

Reducer-v2 runtime остаётся заблокирован, пока:

1. не определены NK-SAM и named equivalence profiles;
2. portable Event/history commitment не отделён от operational/profile Receipts;
3. reducer, identity, encoding и schema versions не включены в declared commitment boundary;
4. не определена stable failure-location semantics.

### 5.2. Version binding

Reducer выбирается на уровне Kernel instance/history, а не process default.

Минимальная binding:

```text
instance_id
reducer_contract
reducer_version
Event contract/version
identity contract
encoding profile
```

History не может менять reducer interpretation после первого committed Event без accepted migration contract.

### 5.3. Reducer v1

`nk-p1-reducer/1` остаётся:

- читаемым;
- исполняемым для historical replay;
- immutable по смыслу;
- совместимым с существующими fixtures и evidence;
- способным содержать histories, не мигрируемые в v2.

### 5.4. Первый scope reducer v2

`nk-p1-reducer/2` обеспечивает только referential semantics для уже разрешённых Event roles.

Он не реализует:

- полный Admission workflow;
- truth evaluation;
- Temporal semantics;
- typed relation ontology;
- causal reasoning;
- operational deletion;
- distributed multi-writer behavior.

## 6. Предлагаемые решения по Event roles

Следующие defaults являются техническими рекомендациями и требуют operator acceptance.

### `ADMIT`

Рекомендуемые правила:

- первое valid admission создаёт admitted Claim state;
- полностью идентичное повторное admission детерминировано и idempotent;
- conflicting admission payload или incompatible admission reference завершается failure;
- admission erased/restricted Claim завершается failure, пока отдельный restoration contract не разрешит иное;
- reducer v2 проверяет существующий admission decision/reference, но не исполняет полный Admission lifecycle.

```yaml
duplicate_identical_admit: IDEMPOTENT_NO_STATE_CHANGE
conflicting_admit: FAILURE
admit_erased_claim: FAILURE
admit_restricted_claim: FAILURE
```

### `LINK`

Рекомендуемые правила:

- source существует и admitted;
- target существует и admitted;
- erased/restricted references завершаются failure, если Event contract явно не определяет historical-reporting role;
- generic self-links не запрещаются глобально;
- generic graph cycles не запрещаются глобально;
- relation-specific restrictions принадлежат будущему typed-relation contract.

```yaml
generic_self_link: ALLOWED
generic_cycle: ALLOWED
erased_reference: FAILURE
restricted_reference: FAILURE_BY_DEFAULT
```

### `UTILIZED`

Рекомендуемые правила:

- unknown Claim → failure;
- erased Claim → failure для current utilization;
- restricted Claim → failure, если Event не содержит явно разрешённый compatible scope;
- historical reporting прежнего использования — отдельная role, а не current `UTILIZED`.

```yaml
unknown_claim: FAILURE
erased_claim: FAILURE
restricted_claim: FAILURE_BY_DEFAULT
historical_use_reporting: SEPARATE_ROLE
```

### `SUPERSEDED`

Рекомендуемые правила:

- predecessor и successor существуют и admitted;
- оба допустимы для reference;
- predecessor ≠ successor;
- predecessor имеет только один active successor в v2;
- повтор того же predecessor→successor детерминирован и idempotent;
- замена существующего successor другим завершается failure;
- self-supersession завершается failure;
- двухузловые и длинные cycles завершаются failure;
- write order не является semantic truth.

```yaml
same_successor_repetition: IDEMPOTENT_NO_STATE_CHANGE
different_successor_overwrite: FAILURE
self_supersession: FAILURE
supersession_cycle: FAILURE
```

### `ERASED`

Рекомендуемые правила:

- unknown Claim → failure;
- первое valid erase переводит Claim в существующий logical-erasure state;
- repeated identical logical erase детерминирован и idempotent, Event остаётся видимым в history;
- restricted/retention-held cases следуют accepted deletion-state contract и могут дать restriction, pending или failure, но не ложный physical-deletion claim;
- reducer v2 никогда не заявляет physical или cryptographic deletion.

```yaml
unknown_claim: FAILURE
repeated_logical_erase: IDEMPOTENT_NO_STATE_CHANGE
physical_deletion_claim: FORBIDDEN
```

## 7. Предлагаемые stable failure-code families

Финальные имена фиксируются accepted contract.

```text
NK-RED-UNKNOWN-SOURCE
NK-RED-UNKNOWN-TARGET
NK-RED-UNKNOWN-CLAIM
NK-RED-ERASED-REFERENCE
NK-RED-RESTRICTED-REFERENCE
NK-RED-ADMISSION-CONFLICT
NK-RED-SELF-SUPERSESSION
NK-RED-SUCCESSOR-CONFLICT
NK-RED-SUPERSESSION-CYCLE
NK-RED-UNKNOWN-ERASE
NK-RED-REDUCER-VERSION-MISMATCH
NK-RED-ENCODING-PROFILE-MISMATCH
```

Stable output:

```text
failure_code
failure_location
Event index
global_seq, when committed
reducer contract/version
state-before-failure digest
proof boundary
```

Message text может меняться; machine code и location semantics остаются стабильными внутри contract version.

## 8. Migration decision

Рекомендуемый первый scope:

```text
CONTINUE_V1
START_NEW_V2_INSTANCE
ASSESS_V1_MIGRATABILITY
```

Не разрешено в первом slice:

```text
SILENT_V1_TO_V2_UPGRADE
AUTOMATIC_HISTORY_REWRITE
AUTOMATIC_EVENT_TRANSFORMATION
```

Допустимые assessment outcomes:

```text
VALID_UNDER_V1_AND_MIGRATABLE
VALID_UNDER_V1_WITH_DECLARED_V2_FAILURES
VALID_UNDER_V1_NON_MIGRATABLE_TO_V2
INVALID_UNDER_DECLARED_V1_CONTRACT
UNDETERMINED
```

`NON_MIGRATABLE_TO_V2` не делает valid v1 history недействительной.

## 9. Обязательные fixtures

Positive:

- first admission;
- duplicate identical admission;
- valid LINK;
- valid utilization;
- valid supersession;
- repeated identical supersession;
- valid erase;
- repeated logical erase.

Negative:

- conflicting admission;
- LINK missing source/target;
- LINK erased/restricted source/target;
- UTILIZED unknown/erased/restricted;
- SUPERSEDED unknown predecessor/successor;
- self-supersession;
- successor overwrite;
- two-node и long cycles;
- ERASED unknown;
- reducer-version substitution;
- encoding-profile substitution;
- disagreement failure location между profiles.

## 10. Cross-profile acceptance

PostgreSQL, SQLite и будущие independent implementations должны давать эквивалентные результаты по named profiles:

- state equivalence для successful histories;
- trace/failure equivalence для rejected histories;
- Receipt equivalence для bounded proof output.

Они обязаны совпадать по:

```text
failure code
failure location
Event index
global sequence, when applicable
reducer version
state-before-failure digest
```

Shared Python code позволяет сравнивать PostgreSQL/SQLite, но не доказывает independent implementation neutrality.

## 11. Operator selections

```yaml
adr_0024_decision: UNSELECTED
v1_immutability: REQUIRED
v2_instance_history_binding: UNSELECTED
duplicate_admit_policy: UNSELECTED
restricted_reference_policy: UNSELECTED
same_successor_repetition: UNSELECTED
different_successor_overwrite: UNSELECTED
repeated_erase_policy: UNSELECTED
stable_failure_codes: UNSELECTED
migration_scope: UNSELECTED
nk_sam_dependency: UNSELECTED
event_commitment_dependency: UNSELECTED
runtime_authorized_after_decision: false
```

## 12. Acceptance gates после operator decision

При `ACCEPT` или `ACCEPT_WITH_CHANGES`:

1. финализировать ADR-0024;
2. зафиксировать failure codes и Event-role rules;
3. определить NK-SAM/equivalence dependency;
4. определить Event/history commitment dependency;
5. обновить registry и schemas без assertion promotion;
6. создать отдельный reducer-v2 semantic-core PR;
7. создать отдельный PostgreSQL/SQLite integration PR;
8. создать новые fixtures и evidence identity;
9. сохранить reducer-v1 reader и historical evidence;
10. синхронизировать GitHub и Notion после merge.

## 13. Что доказывает пакет

Только то, что technical choices, dependencies, recommended defaults и unresolved operator selections записаны явно.

## 14. Чего пакет не доказывает

Он не принимает ADR-0024, не разрешает reducer v2, не меняет reducer v1, не устанавливает Admission/Temporal semantics, не повышает assertions и не создаёт evidence.