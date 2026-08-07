# RFC-0002: Планирующий и implementation-контракт PostgreSQL Reference Profile v0

- **RFC status:** `ACCEPTED`
- **Evidence level:** `REPOSITORY_REPRODUCED — P4 ASSERTION-SCOPED C2 ON PREVIOUS HEAD`
- **Implementation status:** `PARTIAL — P1 + P2 + P3 + P4`
- **Operator approval:** `APPROVED`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Planning version:** `nk-pg-profile/0.1`
- **Текущая implementation version:** `0.4-p4`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Связано:** Issues #40, #43, #46, #49, #55; PRs #47, #50, #56; ADR-0001, ADR-0009, ADR-0011…0018

## 1. Назначение и текущее решение

Определить первый clean implementation profile Native Kernel на PostgreSQL, не превращая PostgreSQL, Python, Psycopg, SQL tables, locks или современное hardware в Architecture Canon.

```text
принятые архитектурные контракты
        ↓
P1 profile-independent semantic core — merged
        ↓
P2 PostgreSQL append/idempotency — merged
        ↓
P3 replay/projection rebuild/Receipts — merged
        ↓
P4 assertion-scoped conformance — разрешён и реализован в PR #56
        ↓
P5 independent SQLite profile — заблокирован до отдельного GO
```

P4 не разрешает P5 и не устанавливает C3.

## 2. Граница lineage

```text
native-kernel/postgresql-reference
≠ recovered v0.1.2.1
≠ original 44-test suite
≠ продолжение исторического prototype
```

Issue #1 остаётся активным и независимым. Этот RFC не объявляет исторический source глобально потерянным и не заменяет требования provenance.

## 3. Принятые входы

| Вход | Обязательный смысл |
|---|---|
| ADR-0001 | Canon отделён от implementation profiles |
| ADR-0009 | PostgreSQL — preferred full profile; SQLite остаётся optional |
| ADR-0011 / `nk-id/1.0` | canonical identity и migration/collision rules |
| ADR-0012 / `nk-event/1.0` | single-writer append, idempotency, order и replay boundary |
| ADR-0013 / `nk-deletion/1.0` | deletion, restriction, retention и proof limits |
| ADR-0014 / `nk-fixtures/1.0` | executable fixture и evidence protocol |
| ADR-0015 | clean lineage принят; P1 разрешён |
| ADR-0016 | bounded P2 append/idempotency profile разрешён |
| ADR-0017 | bounded P3 replay/projection/Receipt profile разрешён |
| ADR-0018 | P4 assertion-scoped conformance разрешён |
| registry `1.1.0` | стабильные 72 assertion IDs и decision statuses |

`NK-EPI-001…008` и ADR-0008 остаются proposed. P4 выдаёт для них `UNSUPPORTED`, но не принимает и не повышает их статус.

## 4. Текущая реальность

```text
P1 semantic core:              PARTIAL / REPOSITORY-TESTED
P2 PostgreSQL append profile:  PARTIAL / REPOSITORY-INTEGRATION-TESTED
P3 replay/projection profile:  PARTIAL / REPOSITORY-INTEGRATION-TESTED
P4 conformance adapter:        PARTIAL / C2 REPOSITORY-REPRODUCED
support_state:                 PARTIAL
P5 independent SQLite:         NOT_AUTHORIZED / NOT_IMPLEMENTED
C3/C4/C5:                      NOT_ESTABLISHED
Physical deletion:             NOT_IMPLEMENTED
```

Карта поддержки P4:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

Top-level C2 относится только к 41 assertion result со статусом `SUPPORTED` в exact report.

## 5. Архитектура профиля

```text
Command canonicalization + validation       ← P1
Authority port                              ← P1
PostgreSQL append/idempotency                ← P2
Authoritative Event history                 ← P2
Explicit UpcasterRegistry                   ← P3
Persisted replay from empty                 ← P3
Disposable semantic-state projection        ← P3
Replay/Projection Rebuild Receipts           ← P3
Assertion-scoped conformance adapter         ← P4
Independent second profile                   ← P5 отсутствует
```

### 5.1 P1 semantic core

Пакет: `native_kernel.semantic_core`.

- canonical JSON и identity helpers;
- immutable semantic objects;
- explicit authority boundary;
- deterministic reducer;
- deletion/restriction transitions и Receipt overclaim guards;
- deterministic upcaster registry;
- canonical semantic-state decoder.

`nkd0` и `nks0` остаются деталями clean profile, пока не приняты отдельно.

### 5.2 P2 authoritative append

Пакет: `native_kernel.postgresql_profile`.

- lazy Psycopg boundary;
- numbered SQL migrations и checksum ledger;
- Kernel instance/history head;
- writer owner/epoch/expiry lease;
- atomic Event + idempotency transaction;
- rollback-safe global и stream counters;
- canonical payload/envelope bytes;
- commitments `nkp1` и `nke1`;
- stored-event consistency validation.

### 5.3 P3 persisted replay и projections

Для одного выбранного Kernel instance P3:

1. открывает repeatable-read snapshot;
2. фиксирует authoritative head;
3. проверяет Event count, sequence и canonical commitments;
4. проверяет одну global hash chain от `GENESIS`;
5. проводит schema versions через explicit upcaster path;
6. выполняет P1 reduction from empty;
7. формирует bounded Replay Receipt;
8. сравнивает captured head под lock перед публикацией projection;
9. атомарно commits rebuild Receipt и disposable projection.

Удаление projection не удаляет Events или committed Receipt history и не сбрасывает generation lineage.

### 5.4 Граница P3 Receipts

Replay и Projection Rebuild Receipts могут доказывать только заявленную операцию, selected instance, Event range/head, reducer/schema versions, state digest, projection identity/generation и proof limitations.

Они не доказывают truth, external authenticity, complete Event Integrity, physical deletion, C-levels или production guarantees.

### 5.5 P4 assertion-scoped adapter

P4 использует `nk-evidence-report/1` и выдаёт все 72 registry IDs ровно по одному разу.

```text
registry + fixture pack
→ semantic checks
→ PostgreSQL checks
→ assertion result map
→ evidence references + limitations
→ strict report validation
→ repository artifact
```

Каждый результат имеет один статус:

- `SUPPORTED` — bounded assertion behavior прямо воспроизведён;
- `PARTIAL` — значимая часть воспроизведена, но остаётся явный gap;
- `UNSUPPORTED` — достаточной исполняемой поддержки нет или assertion proposed;
- `FAILED` — обязательный заявленный check выполнен и упал.

Assertion нельзя скрыть или повысить через prose.

## 6. Исполняемые checks P4

Profile-neutral checks:

- registry version/coverage/decision status;
- identity golden vectors и invalid canonical inputs;
- semantic roles, explicit scope и source-bound Claim identity;
- explicit deny-by-default authority;
- Admission/Deletion Receipt proof limits;
- deterministic reduction и explicit sequence/schema failures;
- semantic deletion/restriction transitions.

PostgreSQL checks:

- migration idempotency;
- writer lease/epoch fencing;
- append, retry и conflicting idempotency reuse;
- rollback-safe contiguous ordering;
- persisted replay равен direct reduction;
- projection destroy/rebuild и monotonic generation;
- stale-head rejection;
- stored canonical corruption detection.

Эти checks не создают отсутствующие conflict, restore, deletion-worker, cross-project или cross-profile механизмы.

## 7. Граница C1, C2 и C3

Conformance остаётся assertion-scoped.

- C1: локально выполненные commands/failures с записанным evidence;
- C2: exact repository reproduction с committed implementation, environment, CI traceability и retained artifacts;
- C3: materially independent profile плюс declared equivalence и comparison evidence.

```text
support_state: PARTIAL
kernel_runtime_conformance: C2
```

Такая комбинация корректна: C2 относится только к `SUPPORTED` assertion results. `PARTIAL` и `UNSUPPORTED` остаются вне supported set.

```text
C2 в четырёх Python/PostgreSQL combinations
≠ четыре независимых профиля
≠ C3
```

## 8. Первоначальное P4 evidence

Evidence head:

```text
93710131fffdea7d9a586cc05e7f258c07fae707
```

```text
P4 run 31175767586 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
P1/P2/P3 regressions — PASS
4 retained JSON evidence artifacts
```

Первый failure run `31175593261` сохранён как negative evidence. Полный C1 report прошёл, но standalone adapter не добавил repository root в `sys.path`. CLI bootstrap исправлен без ослабления checks или validation.

Exact artifact digests записаны в `docs/ai/P4_IMPLEMENTATION_RECORD.md`.

## 9. Правила evidence report

Valid P4 report обязан:

1. использовать `nk-evidence-report/1`;
2. называть `native-kernel/postgresql-reference`;
3. сохранять `support_state: PARTIAL`;
4. выдавать все 72 assertion IDs ровно один раз;
5. совпадать с guarded support counts;
6. требовать evidence для каждого supported/partial result;
7. ссылаться только на passed checks в том же report;
8. включать limitations для каждого result;
9. сохранять все proposed `NK-EPI` как unsupported;
10. явно указывать, что C2 не является C3, truth, authenticity, deletion или production proof.

Repository C2 дополнительно требует non-local commit/run/environment metadata и retained artifacts.

## 10. Технологическая нейтральность

PostgreSQL, Psycopg, Python, JSONB, SQL tables, row locks и GitHub Actions — технологии профиля.

Семантическими/контрактными остаются:

- stable Claim identity roles;
- distinction authority и admission;
- Event meaning и order obligations;
- deterministic reduction;
- deletion/restriction proof limits;
- Receipt/report boundaries;
- assertion support states и equivalence classes.

P4 C2 не превращает технологии профиля в Canon.

## 11. Явные non-goals

- нет P5 SQLite implementation;
- нет C3 cross-profile equivalence;
- нет physical или cryptographic deletion execution;
- нет truth, signature, notarization или external-authenticity certification;
- нет C4/C5 или production claim;
- нет network API;
- нет Titan, Mentaury или Crystal runtime wiring;
- нет `v0.1.2.1` recovery claim;
- нет ADR-0008 или `NK-EPI` promotion;
- нет package publication decision по Issue #18.

## 12. Оставшиеся gaps

- complete conflict representation/resolution;
- identity migration/alias adjudication;
- restore-before-visibility enforcement;
- durable deletion execution по locations/backups/keys;
- cross-project authority adapter;
- independent second profile;
- scale, failover, backup/restore и managed-provider evidence;
- long-term artifact retention.

## 13. Lifecycle фаз

```text
P0 — RFC и planning manifest                       COMPLETE
P1 — profile-independent semantic core              MERGED
P2 — PostgreSQL append/idempotency                   MERGED
P3 — replay/projection rebuild/Receipts              MERGED
P4 — assertion-scoped conformance                    ACTIVE / PARTIAL / C2 EVIDENCE
P5 — independent SQLite profile / C3 research        BLOCKED / SEPARATE GO
```

## 14. Следующий gate

P5 требует отдельного явного operator GO. Любое заявление C3 должно назвать materially independent implementation, declared equivalence classes, allowed differences, exact comparison commands и retained evidence.
