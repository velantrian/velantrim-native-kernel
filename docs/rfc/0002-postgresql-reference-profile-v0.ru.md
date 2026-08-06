# RFC-0002: Планирующий контракт PostgreSQL Reference Profile v0

- **RFC status:** `PROPOSED / DOCUMENTED_ONLY`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Operator approval:** `PENDING`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Planning version:** `nk-pg-profile/0.1-proposed`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Связано:** Issue #40, ADR-0001, ADR-0009, ADR-0011…0014

## 1. Назначение

Определить первый clean implementation profile Native Kernel на PostgreSQL, не превращая PostgreSQL, Python, SQL tables или сегодняшнее железо в Architecture Canon.

```text
принятые архитектурные контракты
        ↓
спецификация clean PostgreSQL profile
        ↓
отдельные implementation PR
        ↓
local evidence
        ↓
repository reproduction
        ↓
будущий независимый SQLite profile
        ↓
возможное C3 comparison
```

RFC является planning contract. Он не содержит Kernel runtime и не разрешает implementation без отдельного решения.

## 2. Граница lineage

```text
native-kernel/postgresql-reference
≠ восстановленный v0.1.2.1
≠ оригинальные 44 tests
≠ продолжение исторического prototype
```

Профиль начинает новую чистую evidence lineage. Issue #1 остаётся активным и независимым. RFC не объявляет исторический source глобально потерянным и не заменяет provenance requirements.

Каждый будущий implementation artifact обязан указывать:

- profile ID/version;
- source commit;
- contract registry version;
- schema и reducer versions;
- environment и commands;
- evidence level;
- unsupported assertions и known limits.

## 3. Принятые входные решения

| Решение | Обязательный смысл |
|---|---|
| ADR-0001 | Canon отделён от implementation profiles |
| ADR-0009 | PostgreSQL — preferred full profile; SQLite остаётся optional |
| ADR-0011 / `nk-id/1.0` | canonical identity, collision и migration |
| ADR-0012 / `nk-event/1.0` | single-writer append, idempotency, ordering и replay |
| ADR-0013 / `nk-deletion/1.0` | deletion/restriction/retention и proof limits |
| ADR-0014 / `nk-fixtures/1.0` | executable fixtures и evidence protocol |
| registry `1.1.0` | stable assertion IDs и statuses |

`NK-EPI-001…008` остаётся proposed. Профиль может сообщать эти assertions как unsupported/experimental, но не принимать ADR-0008 автоматически.

## 4. Non-goals

RFC не определяет и не заявляет:

- production readiness;
- multi-writer consensus;
- universal SQL schema;
- PostgreSQL semantics как Canon;
- live Titan, Mentaury или Crystal integration;
- legal compliance или global deletion proof;
- C2/C3 из документации;
- historical compatibility с `v0.1.2.1`;
- вечный programming language или PostgreSQL major.

## 5. Архитектура профиля

```text
Command API
   ↓
Command canonicalization + validation
   ↓
Authority port
   ↓
Append service
   ↓
PostgreSQL authoritative-history adapter
   ↓
Reducer + upcaster registry
   ↓
Disposable projections
   ↓
Receipt/evidence emitter
   ↓
Conformance adapter
```

### 5.1 Semantic core

Semantic core владеет identity algorithms, command/Event domain objects, reducer/upcaster interfaces, deletion transitions, Receipt boundaries и profile-independent errors.

Он не импортирует PostgreSQL driver и не выдаёт table/row ID как semantic identity.

### 5.2 Authority port

Authority входит через явный port. Deterministic local policy adapter допустим для тестов, но storage presence, authentication, model confidence, retrieval rank или repeated use не создают admission authority.

### 5.3 Storage adapter

PostgreSQL adapter отвечает за:

- transactions и locks;
- authoritative Event persistence;
- idempotency records;
- writer epoch/lease;
- replay reads;
- projection offsets/rebuild metadata;
- profile-local diagnostics.

SQL schema, indexes, generated IDs, constraints и query plans остаются profile details.

### 5.4 Reducer и projections

Reducers — deterministic functions с явными versions. Projections disposable и восстанавливаются из authoritative history.

Projection failure не откатывает, не редактирует и не скрывает committed Event.

### 5.5 Evidence emitter

Профиль создаёт machine-readable evidence reports, совместимые с `nk-evidence-report/1`. Unsupported assertions остаются видимыми.

## 6. Writer и transaction model

Planning v0 использует одного authoritative writer на Kernel instance.

Future implementation должна установить writer boundary через explicit process/instance lease или эквивалентный profile-local mechanism. Нельзя считать PostgreSQL сам по себе доказательством safe multi-writer.

### Atomic command path

В одной database transaction:

1. проверить writer epoch/lease;
2. canonicalize command и вычислить digest;
3. найти scoped idempotency key;
4. для same key + same digest вернуть original result;
5. same key + different digest отклонить;
6. выделить contiguous `global_seq` и stream sequence;
7. append authoritative Event;
8. записать idempotency result со ссылкой на Event;
9. commit;
10. подтвердить durability только после commit.

Projection work выполняется после authoritative transaction.

### Failure behaviour

| Failure | Outcome |
|---|---|
| validation/authority failure | no append |
| duplicate same digest | original result, no second Event |
| duplicate different digest | explicit idempotency conflict |
| transaction rollback | no visible Event/success |
| projection failure after commit | Event остаётся authoritative; projection behind |
| unsupported schema/reducer | replay explicit stop |
| writer epoch mismatch | append rejected |

## 7. Profile-local storage map

Initial implementation может использовать структуры, эквивалентные:

| Logical structure | Role |
|---|---|
| profile metadata | profile/version, registry version, writer epoch |
| commands/idempotency | digest, key scope, original result |
| authoritative events | immutable ordered envelopes |
| reducer versions | upcaster/reducer compatibility |
| projection offsets | disposable read-model progress |
| deletion work | requests, attempts, locations, residual limits |
| evidence records | replay/rebuild/migration Receipts |

Названия tables/columns ненормативны. Semantic IDs независимы от surrogate DB keys.

## 8. Capability manifest

Manifest обязан указывать для каждого contract family:

- contract version;
- planning state;
- implementation phase;
- explicitly unsupported assertions;
- evidence level;
- known operational limits.

`PLANNED` и `DEFERRED` — planning terms, а не conformance results. Runtime evidence report использует только принятую status vocabulary.

## 9. Deletion и data locations

Профиль обязан учитывать:

- authoritative payloads;
- command/idempotency data;
- projections/indexes;
- evidence records/exports;
- logs/dead-letter data;
- backups, replicas и migration artifacts.

Первые runtime stages могут поддерживать только logical restriction и fixture-scoped deletion. Physical deletion, provider deletion, backup expiry и crypto-erasure остаются unsupported до implementation/evidence.

Receipt перечисляет verified, pending и unknown locations.

## 10. Replay и rebuild

Replay experiment обязан:

1. начать с пустого derived-state store;
2. читать Events по `global_seq`;
3. проверять payload/chain commitments;
4. применять declared upcasters/reducer version;
5. явно останавливаться на unsupported version/corruption;
6. создать state digest, counts, offsets и limitations;
7. сравнить expected outputs;
8. повторить после удаления projections.

Fixture integrity не заменяет этот experiment.

## 11. Migration boundary

```text
fence writes
→ source position
→ neutral history export
→ identity/order/commitment verification
→ target import
→ replay from empty
→ declared equivalence comparison
→ activate or rollback
→ migration Receipt
```

Future SQLite profile читает ту же neutral history и contract versions. Physical SQL equality не требуется; semantic/behavioural equivalence обязательна.

## 12. Test и fault matrix

### P1 — Semantic core

- identity golden/invalid vectors;
- command canonicalization;
- reducer determinism;
- unsupported version failures;
- deletion transitions;
- Receipt overclaim rejection.

### P2 — PostgreSQL adapter

- first append;
- same-digest retry;
- conflicting key reuse;
- transaction rollback;
- sequence contiguity;
- writer-epoch rejection;
- concurrent attempts внутри single-writer boundary;
- projection failure after commit.

### P3 — Replay/rebuild

- replay from empty;
- destroy/rebuild projections;
- truncated/reordered history;
- modified payload commitment;
- unsupported upcaster/reducer;
- interrupted rebuild и resume/rollback.

### P4 — Conformance adapter

- все 72 assertion IDs ровно один раз;
- unsupported visible;
- exact profile/environment/commit metadata;
- machine-readable artifact;
- CI reproduction на exact SHA.

### P5 — Cross-profile

- independently developed SQLite adapter;
- shared neutral history;
- declared byte/structural/semantic/behavioural comparison;
- никакого C3 до review различий и limits.

## 13. Evidence promotion

| Level | Gate |
|---|---|
| C0 | merged profile manifest/assertion mapping |
| C1 | local implementation с commands/failures |
| C2 | committed code, pinned environment, CI, artifacts, traceability |
| C3 | independent SQLite/other profile сохраняет declared equivalence |
| C4 | approved Offline Shadow workload/Receipts |
| C5 | bounded operational security/privacy/rollback/incident evidence |

Acceptance RFC разрешает planning, но не повышает evidence автоматически.

## 14. Packaging/environment

Future implementation PR фиксирует или объявляет runtime range, PostgreSQL major(s), driver/migration tool, startup path, schema migration ID, test/conformance commands и operating assumptions.

RFC не выбирает вечный environment.

## 15. Security/incident boundaries

До operational claims нужны credentials/secrets, least-privilege roles, backup/restore threat review, log redaction, corruption response, fence/disable procedure, migration rollback, deletion/retention review и incident Receipts.

## 16. Implementation sequence

```text
P0 — RFC + planning manifest
P1 — profile-independent semantic core
P2 — PostgreSQL append/idempotency adapter
P3 — reducer, projection rebuild, Receipts
P4 — conformance adapter + repository CI
P5 — independent SQLite profile для C3 research
```

Каждый stage — отдельный PR. Runtime нельзя называть recovered `v0.1.2.1`.

## 17. Open decisions

1. language/package layout;
2. PostgreSQL version matrix;
3. writer lease/epoch mechanism;
4. neutral export encoding;
5. initial reducer/state model;
6. first projections;
7. minimum deletion scope для C1/C2;
8. dependency/license constraints;
9. можно ли начинать runtime при активном Issue #1.

## 18. Acceptance gate

- [ ] operator принимает profile ID/version/clean lineage;
- [ ] manifest/assertion mapping reviewed;
- [ ] transaction/idempotency/replay boundaries accepted;
- [ ] test/fault matrix accepted;
- [ ] deletion/security non-claims accepted;
- [ ] Issue #1 separation explicit;
- [ ] runtime implementation получает отдельный GO.

До этого:

```text
RFC: PROPOSED
Implementation: NOT_STARTED
Evidence: DOCUMENTED
Kernel runtime: ABSENT
```
