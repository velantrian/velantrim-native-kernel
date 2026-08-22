# ⚖️ Пакет operator decision по ADR-0024

**[English](./0024-operator-decision-package.md) · [Русский](./0024-operator-decision-package.ru.md)**

```yaml
document_role: OPERATOR_DECISION_PACKAGE
document_state: DECIDED
issue: 74
adr: ADR-0024
status_as_of: 2026-08-22
decision_state: OPERATOR_APPROVED
selected_option: ACCEPT_WITH_CHANGES
operator: '@velantrian'
decision_date: 2026-08-22
runtime_effect: REDUCER_V2_NOT_AUTHORIZED
```

> Теперь этот пакет хранит provenance операторского решения по ADR-0024. Нормативный принятый contract находится в `0024-version-reducer-referential-semantics.md`. Принятие ADR не разрешает реализацию reducer-v2.

## Решение

```text
ACCEPT_WITH_CHANGES
```

Оператор принял направление versioned reducer с ограниченными уточнениями, подготовленными этим пакетом.

## Принятые настройки

```yaml
v1_immutability: REQUIRED
v2_instance_history_binding: REQUIRED
duplicate_admit_policy: IDEMPOTENT_NO_STATE_CHANGE
restricted_reference_policy: FAILURE_BY_DEFAULT
same_successor_repetition: IDEMPOTENT_NO_STATE_CHANGE
different_successor_overwrite: FAILURE
self_supersession: FAILURE
supersession_cycle: FAILURE
repeated_erase_policy: IDEMPOTENT_NO_STATE_CHANGE
physical_deletion_claim: FORBIDDEN
stable_failure_codes: REQUIRED
migration_scope:
  - CONTINUE_V1
  - START_NEW_V2_INSTANCE
  - ASSESS_V1_MIGRATABILITY
nk_sam_dependency: REQUIRED_BEFORE_RUNTIME_AUTHORIZATION
event_commitment_dependency: REQUIRED_BEFORE_RUNTIME_AUTHORIZATION
runtime_authorized_after_decision: false
```

## Историческая граница

`nk-p1-reducer/1` остаётся читаемым, replayable и неизменяемым по смыслу. Существующие P1-C5 evidence остаются reducer-v1-bounded evidence. History v1 нельзя молча повысить, переписать или переинтерпретировать как v2.

## Принятый первый scope v2 contract

Будущий v2 contract ограничен referential semantics уже разрешённых Event roles. Он не получает полный Admission, truth evaluation, Temporal semantics, typed relation ontology, causal reasoning, physical deletion, distributed multi-writer behavior или ecosystem authority.

Generic LINK self-reference и generic graph cycles остаются допустимыми в base reducer; relation-specific ограничения остаются за пределами этого contract. Unknown/erased references завершаются failure по принятым strict rules; restricted references по умолчанию дают failure, если нет отдельно принятого compatible scope. Self-supersession, successor overwrite и successor cycles дают failure.

## Stable failure families

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

Stable output rejected history должен связывать failure code/location, Event index, global sequence при наличии, reducer contract/version, state-before-failure digest и proof boundary.

## Migration boundary

Разрешённый первый scope:

```text
CONTINUE_V1
START_NEW_V2_INSTANCE
ASSESS_V1_MIGRATABILITY
```

Не разрешено:

```text
SILENT_V1_TO_V2_UPGRADE
AUTOMATIC_HISTORY_REWRITE
AUTOMATIC_EVENT_TRANSFORMATION
```

## Runtime authorization остаётся закрытой

До отдельной авторизации reducer-v2 runtime репозиторий должен определить требуемую NK-SAM/named-equivalence dependency, portable Event/history commitment boundary, version binding, stable failure-location semantics, exact fixtures/evidence identity и rollback/migration behavior.

Это решение не разрешает implementation, schema changes, H11 execution, Final Canon, runtime thaw, production, assertion promotion или переинтерпретацию historical evidence.

## Закрытие decision package

Прежняя recommendation и unresolved selections этого пакета заменены операторским решением выше. Нормативные детали зафиксированы в accepted ADR-0024. Любое существенное расширение требует нового явного architecture/operator decision, а не переинтерпретации этого пакета.
