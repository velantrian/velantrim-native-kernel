# RFC-0002: Планирующий контракт PostgreSQL Reference Profile v0

- **RFC status:** `ACCEPTED`
- **Evidence level:** `REPOSITORY_REPRODUCED — P2 INTEGRATION`
- **Implementation status:** `PARTIAL — P1 SEMANTIC CORE + P2 APPEND/IDEMPOTENCY`
- **Operator approval:** `APPROVED`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Planning version:** `nk-pg-profile/0.1`
- **Текущая implementation version:** `0.2-p2`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Связано:** Issues #40, #43, #46; PR #47; ADR-0001, ADR-0009, ADR-0011…0016

## 1. Назначение и текущее решение

Определить первый clean implementation profile Native Kernel, реализующий принятые контракты на PostgreSQL без превращения PostgreSQL, Python, SQL tables или современного hardware в Architecture Canon.

```text
принятые архитектурные контракты
        ↓
принятый clean profile plan
        ↓
P1 profile-independent semantic core — merged и tested
        ↓
P2 PostgreSQL append/idempotency — partial и repository-integration-tested
        ↓
P3 replay/projections/Receipts — blocked by separate GO
        ↓
P4 conformance adapter — blocked
        ↓
P5 independent SQLite profile — blocked
```

Принятие P2 не разрешает следующие фазы и не устанавливает profile conformance.

## 2. Граница lineage

```text
native-kernel/postgresql-reference
≠ восстановленный v0.1.2.1
≠ оригинальный набор из 44 tests
≠ продолжение исторического prototype
```

Профиль использует clean evidence lineage. Issue #1 остаётся активным и независимым. Документ не объявляет исторический source глобально потерянным и не заменяет требования provenance.

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
| ADR-0015 | clean lineage принят; P1 разрешён |
| ADR-0016 | bounded P2 PostgreSQL append profile разрешён |
| registry `1.1.0` | stable assertion IDs и statuses |

`NK-EPI-001…008` и ADR-0008 остаются proposed. P2 их не реализует и не повышает статус.

## 4. Текущее реальное состояние

```text
RFC/profile plan:              ACCEPTED / APPROVED
P1 semantic core:              PARTIAL / REPOSITORY-TESTED
P2 PostgreSQL append profile:  PARTIAL / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections:         NOT_AUTHORIZED / NOT_IMPLEMENTED
Kernel runtime conformance:    UNSUPPORTED
C1/C2/C3:                      NOT_ESTABLISHED
```

Repository evidence для PR #47 head `e80492bcacde2ff2be3a2ee03aa5aa53a714d288`:

```text
P2 workflow run 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
AI context run 31151298002 — PASS
P1 semantic core и fixture integrity — PASS
```

Каждый P2 matrix job прошёл 9 unit tests, 5 PostgreSQL integration tests, 5 manifest tests, validator и compileall.

## 5. Архитектура профиля

```text
Command API
   ↓
Command canonicalization + validation       ← P1 partial
   ↓
Authority port                              ← P1 explicit adapter
   ↓
Append service                              ← P2 implemented
   ↓
PostgreSQL authoritative-history adapter    ← P2 partial
   ↓
Reducer + upcaster registry                 ← reducer core P1; upcasters absent
   ↓
Disposable projections                     ← P3 absent
   ↓
Receipt/evidence emitter                    ← P1 proof guards; operational P3 absent
   ↓
Conformance adapter                         ← P4 absent
```

### 5.1 Реализованный P1 semantic core

Package: `native_kernel.semantic_core`.

- canonical JSON subset `nk-id/1.0` и helpers `nkh1`/`nkc1`/`nkl1`;
- immutable semantic content, Claim identity, Command и logical Event objects;
- explicit deny-by-default authority policy;
- deterministic version-bound in-memory reducer;
- deletion/restriction state transitions;
- admission и deletion Receipt overclaim rejection;
- provisional `nkd0` command и `nks0` state digests.

`nkd0` и `nks0` остаются profile implementation details, а не принятыми cross-profile contracts.

### 5.2 Реализованный P2 PostgreSQL profile

Package: `native_kernel.postgresql_profile`.

Реализовано:

- lazy Psycopg connection boundary;
- numbered SQL migrations с SHA-256 checksum ledger;
- advisory transaction lock для migration bootstrap;
- Kernel instance registration и history head;
- durable writer owner/epoch/expiry lease;
- stale и expired token failures;
- atomic Event и idempotency persistence;
- same-key/same-digest original-result return;
- same-key/different-digest conflict rejection;
- rollback-safe instance-global и per-stream counters;
- exact canonical payload и Event-envelope bytes;
- fixture-compatible `nkp1` payload commitment и `nke1` global chain;
- stored-event consistency validation при idempotent read.

### 5.3 Authority boundary

Authority входит через explicit port до storage operation. Storage presence, authentication, model confidence, retrieval rank, utility или repetition не создают admission authority.

### 5.4 Storage adapter boundary

PostgreSQL отвечает за transactions, locks, Event persistence, idempotency records и writer epoch/lease state только в этом профиле.

SQL schema, indexes, generated IDs, constraints и query plans остаются profile details. P2 не отвечает за projections, replay/upcasters, deletion execution, network API или conformance.

## 6. Writer и transaction model

Version 0 сохраняет одного authoritative writer на Kernel instance.

Реализация:

1. проверяет explicit authority;
2. блокирует Kernel instance;
3. проверяет writer owner, epoch и expiry;
4. проверяет scoped idempotency `(instance_id, command_contract, key)`;
5. возвращает original result для same key + same digest;
6. отклоняет same key + different digest;
7. выделяет contiguous global и stream sequence;
8. строит canonical payload/envelope bytes и commitments;
9. append authoritative Event;
10. обновляет history и stream counters;
11. сохраняет idempotency result со ссылкой на Event;
12. выполняет atomic commit;
13. подтверждает только после commit.

PostgreSQL sequences не используются для authoritative counters, потому что rollback не возвращает потреблённые значения. Обычные rows и locks сохраняют проверенный contiguous-order invariant.

Projection work выполняется после transaction и остаётся P3.

## 7. Граница deterministic reducer

P1 реализует logical reduction с:

- reducer version `nk-p1-reducer/1`;
- Event schema version `1`;
- contiguous global/per-stream checks;
- vocabulary `ADMIT`, `LINK`, `UTILIZED`, `SUPERSEDED`, `ERASED`;
- sorted immutable state structures;
- explicit unsupported-version/sequence failures.

P2 сохраняет Events, но не выполняет authoritative replay, corruption-wide scans, upcasting, crash recovery или projection rebuild.

## 8. Граница deletion и Receipt

P1 реализует deletion/restriction transitions и Receipt overclaim guards. P2 не удаляет реальные bytes, backups, indexes, exports, provider data или encryption keys.

Operational deletion и provider/location evidence требуют отдельной будущей работы.

## 9. Machine-readable manifests

Сохраняются три отдельные записи:

1. `profile-manifest.json` — historical P0 planning snapshot;
2. `p1-manifest.json` — P1 implementation/evidence state;
3. `p2-manifest.json` — P2 append/idempotency implementation и repository matrix evidence.

P2 manifest фиксирует:

```text
implementation: PARTIAL
integration: PASS_REPOSITORY_CI
runtime conformance: UNSUPPORTED
C1/C2/C3: NOT_ESTABLISHED
```

Все 72 contract assertions остаются `UNSUPPORTED` для runtime conformance до P4 с complete assertion-scoped evidence.

```text
implemented code path
≠ assertion-level profile support claim
```

## 10. Test и fault matrix

### P1 — реализован

- identity golden/invalid vectors;
- semantic content/Claim identity separation;
- command canonicalization;
- float/null/non-NFC rejection;
- authority allow/deny;
- Receipt overclaim rejection;
- reducer determinism и sequence/version failures;
- deletion fixture paths и forbidden transitions;
- forbidden database/network imports.

### P2 — реализован и repository-tested

- migration и instance-registration idempotency;
- migration checksum drift detection;
- lease busy/release/monotonic epoch fencing;
- first append;
- same-digest retry;
- conflicting idempotency-key reuse;
- transaction rollback before commit;
- rollback-safe sequence reuse;
- concurrent same-digest append с одним Event;
- canonical payload/envelope и fixture hash commitments;
- P1 lazy-dependency boundary.

### P3–P5 — не разрешены

Replay/rebuild, operational Receipts, complete conformance adapter и independent SQLite comparison остаются будущими фазами.

## 11. Evidence promotion

| Level | Gate PostgreSQL profile | Текущее состояние |
|---|---|---|
| Planning/P0 | accepted profile plan и manifest | complete |
| Implementation evidence | bounded code, tests и explicit failures | P1/P2 partial |
| P2 integration evidence | declared PostgreSQL/Python matrix | repository reproduced |
| C1 | profile runtime с complete declared assertion evidence | not established |
| C2 | committed profile, pinned environment, CI, artifacts и traceability | not established |
| C3 | independent second profile сохраняет declared equivalence | not established |
| C4 | approved Offline Shadow | not established |
| C5 | bounded operational security/privacy/incident evidence | not established |

P2 integration намеренно не называется C1: P4 assertion-scoped conformance adapter отсутствует.

## 12. Security, licensing и dependencies

P2 объявляет Psycopg как profile integration dependency; он lazy-loaded и не vendored. Issue #18 остаётся открытым для publication, contribution и licensing terms.

Operational claims по-прежнему требуют credential handling, least-privilege roles, backup/restore evidence, log redaction, incident fencing, provider behavior и deletion/retention controls.

## 13. Implementation sequence

```text
P0 — accepted RFC + planning manifest              COMPLETE
P1 — profile-independent semantic core             MERGED / REPOSITORY-TESTED
P2 — PostgreSQL append/idempotency adapter          PARTIAL / INTEGRATION-TESTED
P3 — replay, projection rebuild and Receipts        BLOCKED / SEPARATE GO
P4 — conformance adapter and assertion evidence     BLOCKED / SEPARATE GO
P5 — independent SQLite profile для C3 research     BLOCKED / SEPARATE GO
```

## 14. Оставшиеся решения

1. отдельный P3 operator GO;
2. reducer/upcaster persistence и replay API;
3. projection checkpoint/rebuild protocol;
4. neutral export encoding;
5. deletion execution scope и evidence;
6. Issue #18 license/contribution terms;
7. operational fault, performance и backup/restore evidence;
8. future P4 assertion support policy.

## 15. Принятые границы

- [x] profile ID, version и clean lineage приняты;
- [x] profile manifests и assertion mapping reviewed;
- [x] transaction/idempotency boundaries приняты;
- [x] test/fault matrix принята;
- [x] Issue #1 separation explicit;
- [x] P1 получает separate GO и реализован;
- [x] P2 получает separate GO и repository-integration-tested;
- [ ] P3 или последующая работа получает separate GO.

```text
RFC: ACCEPTED
P1/P2 implementation: PARTIAL
P2 integration: REPOSITORY_REPRODUCED
Complete Kernel profile: ABSENT
Kernel runtime conformance: UNSUPPORTED
```
