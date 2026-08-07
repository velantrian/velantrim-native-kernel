# RFC-0002: Планирующий и implementation-контракт PostgreSQL Reference Profile v0

- **RFC status:** `ACCEPTED`
- **Evidence level:** `REPOSITORY_REPRODUCED — P3 INTEGRATION`
- **Implementation status:** `PARTIAL — P1 + P2 + BOUNDED P3`
- **Operator approval:** `APPROVED`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Planning version:** `nk-pg-profile/0.1`
- **Текущая implementation version:** `0.3-p3`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Связано:** Issues #40, #43, #46, #49; PRs #47, #50; ADR-0001, ADR-0009, ADR-0011…0017

## 1. Назначение и текущее решение

Определить первый clean implementation profile Native Kernel на PostgreSQL, не превращая PostgreSQL, Python, Psycopg, SQL tables, locks или современное hardware в Architecture Canon.

```text
принятые архитектурные контракты
        ↓
P1 profile-independent semantic core — merged и tested
        ↓
P2 PostgreSQL append/idempotency — repository-integration-tested
        ↓
P3 replay/projection rebuild/Receipts — repository-integration-tested
        ↓
P4 assertion-scoped conformance adapter — blocked до separate GO
        ↓
P5 independent SQLite profile — blocked до separate GO
```

P3 не разрешает P4/P5 и не устанавливает C1/C2/C3.

## 2. Граница lineage

```text
native-kernel/postgresql-reference
≠ recovered v0.1.2.1
≠ original 44-test suite
≠ продолжение исторического prototype
```

Issue #1 остаётся активным и независимым. RFC не объявляет исторический source глобально потерянным и не заменяет требования provenance.

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
| ADR-0016 | bounded P2 append/idempotency разрешён |
| ADR-0017 | bounded P3 replay/projection/Receipt разрешён |
| registry `1.1.0` | stable assertion IDs и statuses |

`NK-EPI-001…008` и ADR-0008 остаются proposed. P3 их не реализует и не повышает статус.

## 4. Текущее реальное состояние

```text
P1 semantic core:              PARTIAL / REPOSITORY-TESTED
P2 PostgreSQL append profile:  PARTIAL / REPOSITORY-INTEGRATION-TESTED
P3 replay/projection profile:  PARTIAL / REPOSITORY-INTEGRATION-TESTED
Physical deletion:             NOT_IMPLEMENTED
P4 conformance adapter:        NOT_AUTHORIZED / NOT_IMPLEMENTED
P5 independent SQLite:         NOT_AUTHORIZED / NOT_IMPLEMENTED
Kernel runtime conformance:    UNSUPPORTED
C1/C2/C3:                      NOT_ESTABLISHED
```

Начальное executable-head evidence P3:

```text
head 0f8fd4ffe5d5fb0d4bc01f3e441a053f691dbba3
P3 run 31171581859 — PASS
P2 regression run 31171581795 — PASS
P1 run 31171581787 — PASS
fixture run 31171581791 — PASS
PostgreSQL 16/18 × Python 3.11/3.12 — PASS
```

Final PR head должен повторить затронутые checks после documentation/evidence изменений.

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
Assertion-scoped conformance adapter         ← P4 отсутствует
Independent second profile                   ← P5 отсутствует
```

### 5.1 P1 semantic core

Package: `native_kernel.semantic_core`.

- canonical JSON и identity helpers;
- immutable semantic objects;
- explicit authority boundary;
- deterministic reducer;
- deletion/restriction transitions и Receipt overclaim guards;
- standard-library deterministic upcaster registry;
- canonical semantic-state decoder.

`nkd0` и `nks0` остаются clean-profile details до отдельного повышения статуса.

### 5.2 P2 authoritative append

Package: `native_kernel.postgresql_profile`.

- lazy Psycopg boundary;
- numbered SQL migrations и checksum ledger;
- Kernel instance/history head;
- writer owner/epoch/expiry lease;
- atomic Event + idempotency transaction;
- rollback-safe global и stream counters;
- canonical payload/envelope bytes;
- `nkp1` и `nke1` commitments;
- stored-event consistency validation.

### 5.3 P3 persisted replay

Для одного выбранного Kernel instance P3:

1. открывает repeatable-read read-only snapshot;
2. фиксирует `last_global_seq` и `last_event_hash`;
3. требует совпадения Event count/max sequence с instance head;
4. читает каждый Event от sequence `1` через P2 commitment checks;
5. требует единую `prev_global_hash` chain от `GENESIS`;
6. проводит Event через explicit deterministic upcaster path;
7. выполняет reduction from empty заявленным P1 reducer;
8. требует совпадения final replay hash с captured head;
9. создаёт bounded state digest и Replay Receipt.

Missing, duplicate, cyclic, invalid или non-progressing upcaster paths завершаются explicit failure.

### 5.4 Disposable projection rebuild

`semantic-state` projection — заменяемая read model, а не authoritative history.

```text
verified replay snapshot
→ lock Kernel instance row
→ compare current sequence/hash head
→ reject stale snapshot при history advance
→ allocate monotonic generation из committed rebuild Receipts
→ insert Receipt
→ upsert projection
→ atomic commit
```

Удаление projection удаляет только disposable row. Оно не удаляет authoritative Events или Receipt history и не сбрасывает generation lineage.

### 5.5 Граница operational Receipt

P3 сохраняет canonical Receipts для `REPLAY` и `PROJECTION_REBUILD`.

Они могут подтверждать только:

- выбранный instance и наблюдаемый Event range;
- наблюдаемый final Event hash;
- reducer и target schema version;
- resulting state digest;
- projection name/generation;
- declared proof limitations.

Они не могут заявлять:

- truth записанных Claims;
- external authenticity, signatures или notarization;
- отсутствие любого privileged rewrite до snapshot;
- complete Event Integrity при любом threat model;
- physical deletion bytes/backups/exports/logs/keys;
- C1/C2/C3 или production durability/security/privacy/compliance.

## 6. Writer и transaction model

P2 append сохраняет одного authoritative writer owner/epoch lease на instance. P3 не меняет append и не вводит multi-writer consensus.

Replay читает stable snapshot. Receipt/projection publication выполняется отдельной write transaction с locked instance-head comparison, чтобы stale state не публиковался как current.

## 7. Граница determinism и integrity

P3 проверяет:

- contiguous selected-instance global sequence;
- per-stream sequence через reducer;
- canonical stored payload/envelope bytes;
- `nkp1` payload и `nke1` Event commitments;
- contiguous global hash chain;
- explicit schema path;
- reducer version и canonical state digest;
- projection/Receipt canonical bytes при load.

Это integrity signals, а не external authentication или защита от любого privileged rewrite.

## 8. Граница deletion

P1 моделирует semantic deletion/restriction state. P2/P3 сохраняют Events, projections и Receipts. Они не удаляют primary bytes, backups, indexes, provider data, logs, exports или encryption keys.

Physical/cryptographic deletion требует отдельного решения и operational design.

## 9. Machine-readable manifests

Сохраняются отдельные phase records:

1. `profile-manifest.json` — P0 planning snapshot;
2. `p1-manifest.json` — P1 boundary;
3. `p2-manifest.json` — P2 append evidence;
4. `p3-manifest.json` — P3 replay/projection/Receipt evidence.

P3 manifest:

```text
implementation: PARTIAL
evidence: REPOSITORY_REPRODUCED_P3_INTEGRATION
runtime conformance: UNSUPPORTED
C1/C2/C3: NOT_ESTABLISHED
```

Все 72 assertions остаются runtime `UNSUPPORTED` до P4 complete assertion-scoped report.

## 10. Test и fault matrix

### P3 semantic tests

- identity/multi-step upcasting;
- missing/duplicate/cyclic/invalid path rejection;
- canonical state round-trip;
- canonical bounded Receipt;
- Receipt overclaim и operation-shape rejection.

### P3 PostgreSQL integration tests

- persisted replay равен direct P1 reduction;
- Replay Receipt persistence/reload;
- projection rebuild determinism;
- destroy/rebuild с monotonic generation;
- injected precommit failure сохраняет previous projection;
- history advancement отклоняет stale publication;
- stored Event canonical corruption detection;
- projection corruption detection;
- Receipt corruption detection;
- explicit upcaster path requirement;
- P2 regression suite.

## 11. Evidence promotion

| Level | Gate | Текущее состояние |
|---|---|---|
| P0 planning | accepted plan/manifests | complete |
| P1 semantics | bounded deterministic core | repository tested |
| P2 append | declared DB matrix | repository reproduced |
| P3 replay/projection | declared DB matrix и fault scenarios | repository reproduced |
| C1 | complete declared assertion evidence | not established |
| C2 | pinned reproducibility/artifacts/traceability | not established |
| C3 | materially independent second profile | not established |
| C4/C5 | Shadow/operational evidence | not established |

P3 integration не называется C1/C2, потому что P4 assertion-scoped evidence отсутствует.

## 12. Security, licensing и dependencies

Psycopg остаётся lazy profile dependency и не vendored. Issue #18 остаётся открытым.

Operational claims требуют credential/role design, backup/restore evidence, provider behavior, performance limits, incident fencing, log redaction и deletion/retention controls.

## 13. Implementation sequence

```text
P0 — accepted RFC + planning manifest              COMPLETE
P1 — semantic core                                 MERGED / REPOSITORY-TESTED
P2 — PostgreSQL append/idempotency                  PARTIAL / INTEGRATION-TESTED
P3 — persisted replay/projection/Receipts           PARTIAL / INTEGRATION-TESTED
P4 — assertion-scoped conformance adapter           BLOCKED / SEPARATE GO
P5 — independent SQLite profile                     BLOCKED / SEPARATE GO
```

## 14. Оставшиеся решения

1. separate P4 operator GO;
2. complete assertion-to-runtime evidence mapping;
3. neutral export/migration encoding;
4. physical/cryptographic deletion design;
5. Issue #18 license/contribution terms;
6. performance и operational fault evidence;
7. independent P5 profile до C3.

## 15. Принятые границы

- [x] clean profile и lineage приняты;
- [x] P1 отдельно разрешён и tested;
- [x] P2 отдельно разрешён и repository-integration-tested;
- [x] P3 отдельно разрешён и repository-integration-tested;
- [x] Receipt non-claims и stale-head guard сохранены;
- [x] Issue #1 separation explicit;
- [ ] P4/P5 получают separate GO.

```text
RFC: ACCEPTED
P1/P2/P3 implementation: PARTIAL
P3 integration: REPOSITORY_REPRODUCED
Complete assertion conformance: ABSENT
C1/C2/C3: NOT ESTABLISHED
```
