# RFC-0002: Планирующий контракт PostgreSQL Reference Profile v0

- **RFC status:** `ACCEPTED`
- **Evidence level:** `LOCALLY_TESTED — ТОЛЬКО P1`
- **Implementation status:** `PARTIAL — P1 SEMANTIC CORE`
- **Operator approval:** `APPROVED`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Planning version:** `nk-pg-profile/0.1`
- **Текущая implementation version:** `0.1-p1`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Связано:** Issue #40, Issue #43, ADR-0001, ADR-0009, ADR-0011…0015

## 1. Назначение и принятое решение

Определить первый clean implementation profile Native Kernel, способный в будущем реализовать принятые контракты на PostgreSQL, не превращая PostgreSQL, Python, SQL tables или современное железо в Architecture Canon.

Оператор принял clean lineage и разрешил только P1:

```text
принятые архитектурные контракты
        ↓
принятый clean profile plan
        ↓
P1 profile-independent semantic core — реализован и локально проверен
        ↓
P2 PostgreSQL adapter — заблокирован до отдельного GO
        ↓
P3 replay/projections/Receipts — заблокирован
        ↓
P4 conformance adapter/CI — заблокирован
        ↓
P5 независимый SQLite profile — заблокирован
```

Принятие RFC не разрешает следующие фазы и не устанавливает profile conformance.

## 2. Граница lineage

```text
native-kernel/postgresql-reference
≠ восстановленный v0.1.2.1
≠ оригинальный набор из 44 tests
≠ продолжение исторического prototype
```

Профиль использует новую чистую evidence lineage. Issue #1 остаётся активным и независимым. RFC не объявляет исторический source глобально потерянным и не заменяет требования provenance.

Каждый implementation artifact обязан указывать profile/version, source commit, registry version, environment, commands, evidence level, unsupported assertions и known limits.

## 3. Принятые входные решения

| Решение | Обязательный смысл |
|---|---|
| ADR-0001 | Canon отделён от implementation profiles |
| ADR-0009 | PostgreSQL — preferred full profile; SQLite остаётся optional |
| ADR-0011 / `nk-id/1.0` | canonical identity, collision и migration rules |
| ADR-0012 / `nk-event/1.0` | single-writer append, idempotency, ordering и replay boundary |
| ADR-0013 / `nk-deletion/1.0` | deletion/restriction/retention и proof limits |
| ADR-0014 / `nk-fixtures/1.0` | executable fixtures и evidence protocol |
| ADR-0015 | clean lineage принят; bounded P1 implementation разрешён |
| registry `1.1.0` | stable assertion IDs и statuses |

`NK-EPI-001…008` и ADR-0008 остаются proposed. P1 их не реализует и не повышает статус.

## 4. Текущее реальное состояние

```text
RFC/profile plan:              ACCEPTED / APPROVED
P1 semantic core:              PARTIAL / LOCALLY_TESTED
PostgreSQL adapter:            NOT_STARTED / NOT_AUTHORIZED
Durable authoritative history: NOT_IMPLEMENTED
Kernel runtime conformance:    UNSUPPORTED
C1/C2/C3:                      NOT_ESTABLISHED
Repository Actions result:     NOT_RECORDED
```

Локальное evidence P1:

```text
20 semantic-core tests PASS
4 P1-manifest tests PASS
Python compileall PASS
standard-library-only boundary verified
```

Локальный PASS подтверждает только заявленные P1 code paths.

## 5. Архитектура профиля

```text
Command API
   ↓
Command canonicalization + validation       ← P1 partial
   ↓
Authority port                              ← P1 deterministic local adapter
   ↓
Append service                              ← P2 отсутствует
   ↓
PostgreSQL authoritative-history adapter    ← P2 отсутствует
   ↓
Reducer + upcaster registry                 ← P1 reducer core partial
   ↓
Disposable projections                     ← P3 отсутствуют
   ↓
Receipt/evidence emitter                    ← P1 proof guards partial
   ↓
Conformance adapter                         ← P4 отсутствует
```

### 5.1 Реализованный P1 semantic core

Package: `native_kernel.semantic_core`.

Реализовано на Python 3.11+ только со standard library:

- canonical JSON subset `nk-id/1.0` и helpers `nkh1`/`nkc1`/`nkl1`;
- immutable semantic content, Claim identity, command и logical Event objects;
- explicit deny-by-default authority policy;
- deterministic version-bound in-memory reducer;
- deletion/restriction state transitions;
- admission и deletion Receipt overclaim rejection;
- provisional `nkd0` command и `nks0` state digests.

`nkd0` и `nks0` — implementation details clean profile, а не принятые cross-profile identity contracts.

### 5.2 Явно отсутствует в P1

P1 не содержит PostgreSQL/SQLite imports, SQL schema, driver, migration framework, append store, durable idempotency, writer lease persistence, projection persistence, network API или cross-project integration.

Logical reducer не является authoritative event store и не доказывает durable replay.

### 5.3 Authority boundary

Authority входит через явный port. Static policy P1 deterministic и deny-by-default. Storage presence, authentication, model confidence, retrieval rank, utility и repeated use не создают admission authority.

### 5.4 Storage adapter boundary

Будущий PostgreSQL adapter может отвечать за transactions, locks, authoritative Event persistence, idempotency records, writer epoch/lease, replay reads, projection offsets и diagnostics.

SQL schema, indexes, generated IDs, constraints и query plans остаются profile details. P2 требует отдельного operator GO.

## 6. Writer и transaction model для будущего P2

Version 0 сохраняет одного authoritative writer на Kernel instance.

Future implementation обязана:

1. проверить writer epoch/lease;
2. canonicalize command и вычислить digest;
3. проверить scoped idempotency key;
4. для same key + same digest вернуть original result;
5. same key + different digest отклонить;
6. выделить contiguous global/stream sequence;
7. append authoritative Event;
8. сохранить idempotency result со ссылкой на Event;
9. commit atomically;
10. подтвердить durability только после commit.

Projection work выполняется после authoritative transaction. P1 не реализует этот durable path.

## 7. Граница deterministic reducer

P1 реализует deterministic logical reduction с:

- reducer version `nk-p1-reducer/1`;
- поддерживаемой Event schema version `1`;
- проверкой contiguous global и per-stream sequence;
- только принятой Event vocabulary: `ADMIT`, `LINK`, `UTILIZED`, `SUPERSEDED`, `ERASED`;
- отсортированными immutable state structures;
- явным failure на unsupported versions или sequence gaps.

Это executable reducer semantics, но не durable replay, corruption detection, upcasting, crash recovery или projection rebuild evidence.

## 8. Граница deletion и Receipt

P1 реализует принятый граф deletion/restriction transitions и отклоняет запрещённые переходы. Он также отклоняет Receipts, которые:

- заявляют complete global erasure;
- помечают одну location одновременно verified и pending;
- не указывают proof limitations при pending locations;
- заявляют, что admission authority устанавливает truth.

P1 не удаляет реальные bytes, backups, indexes, provider data или encryption keys.

## 9. Machine-readable manifests

Сохраняются две отдельные записи:

1. `profile-manifest.json` — неизменяемый P0 planning snapshot до operator GO;
2. `p1-manifest.json` — принятое P1 implementation/evidence state.

P1 manifest фиксирует Python/stdlib scope, 20 semantic tests, compile evidence, запрещённые P2 capabilities и независимость Issue #1.

Все 72 contract assertions остаются `UNSUPPORTED` для runtime conformance до будущего P4 conformance adapter с assertion-scoped evidence.

```text
implemented code path
≠ assertion-level profile support claim
```

## 10. Test и fault matrix

### P1 — реализован и локально проверен

- identity golden/invalid vectors;
- разделение semantic content и Claim identity;
- command canonicalization и digest determinism;
- rejection float/null/non-NFC;
- explicit authority allow/deny;
- admission Receipt overclaim rejection;
- reducer determinism;
- global/stream sequence failures;
- unsupported schema/reducer failures;
- deletion fixture paths и forbidden transitions;
- deletion Receipt proof limits;
- отсутствие forbidden database/network imports.

### P2 — не разрешён

- first durable append;
- same-digest retry;
- conflicting idempotency-key reuse;
- transaction rollback;
- sequence allocation under concurrency;
- writer-epoch rejection;
- projection failure after commit.

### P3–P5 — не разрешены

Replay/rebuild, conformance adapter, repository reproduction и independent SQLite comparison остаются будущими отдельно управляемыми фазами.

## 11. Evidence promotion

| Level | Gate PostgreSQL profile | Текущее состояние |
|---|---|---|
| Planning/P0 | accepted profile plan и manifest | complete |
| Local implementation evidence | bounded code, commands, tests и failures | только P1 partial |
| C1 | profile-level local runtime с assertion evidence | not established |
| C2 | committed profile, pinned environment, CI, artifacts, traceability | not established |
| C3 | independent second profile сохраняет declared equivalence | not established |
| C4 | approved Offline Shadow | not established |
| C5 | bounded operational security/privacy/incident evidence | not established |

P1 намеренно не называется C1: durable profile runtime и assertion-scoped conformance adapter отсутствуют.

## 12. Security, licensing и dependencies

P1 не добавляет external dependencies и не публикует package. Issue #18 остаётся открытым для publication, contribution и licensing terms.

До P2 или operational claims необходимо определить PostgreSQL/driver versions, migration tooling, credentials, least-privilege roles, backup/restore risks, log redaction, incident fencing и deletion/retention controls.

## 13. Implementation sequence

```text
P0 — accepted RFC + planning manifest              COMPLETE
P1 — profile-independent semantic core             PARTIAL / LOCALLY_TESTED
P2 — PostgreSQL append/idempotency adapter          BLOCKED / SEPARATE GO
P3 — replay, projection rebuild and Receipts        BLOCKED
P4 — conformance adapter and repository evidence    BLOCKED
P5 — independent SQLite profile для C3 research     BLOCKED
```

## 14. Оставшиеся решения

1. отдельный P2 operator GO;
2. PostgreSQL version, driver и migration matrix;
3. writer lease/epoch mechanism;
4. neutral export encoding;
5. initial persistent reducer/projection design;
6. minimum deletion scope для будущего evidence;
7. Issue #18 license/contribution terms;
8. exact repository workflow evidence.

## 15. Принятые границы

- [x] operator принимает profile ID, version и clean lineage;
- [x] profile manifest и assertion mapping reviewed;
- [x] transaction/idempotency/replay boundaries приняты как будущие P2/P3 obligations;
- [x] test/fault matrix принята;
- [x] deletion/security non-claims приняты;
- [x] Issue #1 separation explicit;
- [x] bounded P1 runtime implementation получает отдельный GO;
- [ ] P2 или последующая runtime работа получает отдельный GO.

```text
RFC: ACCEPTED
P1 implementation: PARTIAL / LOCALLY_TESTED
Durable Kernel profile: ABSENT
Kernel runtime conformance: UNSUPPORTED
```
