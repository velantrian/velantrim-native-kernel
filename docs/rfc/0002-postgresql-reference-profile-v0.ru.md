# RFC-0002: PostgreSQL Reference Profile v0 — планирование и implementation contract

- **RFC status:** `ACCEPTED`
- **Evidence level:** `REPOSITORY_REPRODUCED — POSTGRESQL C2 + SQLITE C2 + CROSS-PROFILE C3 ON PREVIOUS HEAD`
- **Implementation status:** `PARTIAL — P1 + P2 + P3 + P4 + P5`
- **Operator approval:** `APPROVED`
- **PostgreSQL profile:** `native-kernel/postgresql-reference@0.4-p4`
- **SQLite comparison profile:** `native-kernel/sqlite-embedded@0.5-p5`
- **Lineages:** `clean/postgresql-reference/0.1`, `clean/sqlite-embedded/0.1`
- **Связано:** Issues #40, #43, #46, #49, #55, #58; PRs #47, #50, #56, #59; ADR-0001, ADR-0009, ADR-0011…0019

## 1. Назначение

Определить первый clean implementation lifecycle Native Kernel, не превращая PostgreSQL, SQLite, Python, Psycopg, SQL layouts, locks, files или текущие вычислители в Architecture Canon.

```text
accepted architecture contracts
        ↓
P1 profile-independent semantic core
        ↓
P2 PostgreSQL append/idempotency
        ↓
P3 replay/projection rebuild/Receipts
        ↓
P4 PostgreSQL assertion-scoped C2
        ↓
P5 independent SQLite profile + assertion-scoped C3
```

P5 проверяет ограниченную technology-neutral гипотезу на двух materially different storage profiles. Он не разрешает C4/C5, production, deletion execution или ecosystem wiring.

## 2. Граница lineage

```text
clean/postgresql-reference/0.1
clean/sqlite-embedded/0.1
≠ recovered v0.1.2.1
≠ original 44-test suite
≠ continuation исторического prototype
```

Issue #1 остаётся активным и независимым. Этот RFC не объявляет исторический source глобально потерянным и не заменяет требования provenance.

## 3. Принятые inputs

| Input | Обязательный смысл |
|---|---|
| ADR-0001 | Canon отделён от implementation profiles |
| ADR-0009 | PostgreSQL full profile; SQLite embedded profile |
| ADR-0011 / `nk-id/1.0` | canonical identity |
| ADR-0012 / `nk-event/1.0` | single-writer append, idempotency, order и replay |
| ADR-0013 / `nk-deletion/1.0` | deletion/restriction/retention meaning и proof limits |
| ADR-0014 / `nk-fixtures/1.0` | executable fixture/evidence protocol |
| ADR-0015…0018 | authorization и границы P1–P4 |
| ADR-0019 | authorization P5 SQLite и assertion-scoped C3 |
| registry `1.1.0` | стабильные 72 assertion IDs и decisions |

`NK-EPI-001…008` и ADR-0008 остаются `PROPOSED`. Оба profile reports и C3 сохраняют их `UNSUPPORTED`.

## 4. Текущая реальность

```text
P1 semantic core:              PARTIAL / REPOSITORY-TESTED
P2 PostgreSQL append:          PARTIAL / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections:         PARTIAL / REPOSITORY-INTEGRATION-TESTED
P4 PostgreSQL conformance:     PARTIAL / C2 REPOSITORY-REPRODUCED
P5 SQLite profile:             PARTIAL / C2 REPOSITORY-REPRODUCED ON EVIDENCE HEAD
Cross-profile comparison:      PARTIAL / C3 REPOSITORY-REPRODUCED ON EVIDENCE HEAD
support_state:                 PARTIAL
C4/C5/production:              NOT_ESTABLISHED / NOT_AUTHORIZED
Physical deletion:             NOT_IMPLEMENTED
```

Single-profile maps:

```text
41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
```

Cross-profile map:

```text
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
```

C2/C3 labels относятся только к results со статусом `SUPPORTED` в exact reports.

## 5. Архитектура и ownership

```text
Command canonicalization / semantic reducer      ← P1
PostgreSQL authoritative append/idempotency       ← P2
PostgreSQL replay/projections/Receipts             ← P3
PostgreSQL complete assertion report               ← P4
Independent SQLite append/replay/projections       ← P5
PostgreSQL↔SQLite equivalence comparator           ← P5
```

### P1 semantic core

`native_kernel.semantic_core` владеет canonical JSON/identity, immutable semantic objects, authority boundaries, deterministic reduction, deletion/restriction transitions, Receipt guards, upcasting и state decoding.

### PostgreSQL profile

`native_kernel.postgresql_profile` владеет migrations, writer fencing, Event/idempotency persistence, rollback-safe ordering, commitments/hash chain, verified replay, projections, bounded Receipts и complete P4 report.

### SQLite profile

`native_kernel.sqlite_profile` независимо владеет:

- stdlib `sqlite3` schema и migrations;
- WAL/foreign-key/synchronous configuration;
- `BEGIN IMMEDIATE` single-writer envelope;
- owner/epoch/expiry fencing;
- append/idempotency/order/hash-chain behavior;
- replay, projections и bounded Receipts;
- exact PostgreSQL authoritative-history import;
- SQLite profile report и C3 comparison.

SQLite не вызывает PostgreSQL append, replay, projection или Receipt adapters.

## 6. Single-profile C2

`nk-evidence-report/1` выдаёт каждый registry ID ровно один раз со status, passed checks и limitations.

PostgreSQL и SQLite single-profile maps зафиксированы как `41/13/18/0`.

```text
C2
≠ поддержка всех 72
≠ C3
≠ truth/authenticity
≠ physical deletion
```

## 7. P5 cross-profile comparison

P5 использует отдельный protocol `nk-equivalence-report/1`.

```text
shared accepted contracts + fixture pack
→ independent PostgreSQL execution
→ independent SQLite execution
→ normalized observable outcomes
→ replay/projection/Receipt comparison
→ exact PostgreSQL Event import into SQLite
→ 72 assertion results
```

Equivalence classes:

| Класс | Сравнение |
|---|---|
| `BYTE` | canonical identity и exact imported Event bytes/hash chain |
| `STRUCTURAL` | required contract/report fields |
| `SEMANTIC` | reducer/projection state и Receipt proof boundaries |
| `BEHAVIOURAL` | accepted/rejected commands, idempotency, fencing и order |

Cross-profile evidence повышает только:

```text
NK-SEM-008
NK-ID-008
NK-EQV-002
NK-EQV-003
```

## 8. Допустимые и недопустимые различия

Допустимые:

- SQL dialect/schema/index layout;
- server topology против embedded file;
- row locks против `BEGIN IMMEDIATE`;
- independently generated Event IDs/timestamps;
- IAM/network/replication/failover/concurrency/administration;
- non-semantic metadata и query plans.

Недопустимые:

- canonical identity и Command digest;
- payload meaning и declared order;
- hash-chain validity;
- reducer/projection canonical state;
- idempotency/stale-writer/corruption outcomes;
- Receipt proof fields;
- exact bytes/hash commitments при authoritative-history import.

## 9. Первоначальное P5 evidence

```text
Evidence head: d43a6ed28232e9fc8b62f84d9025386fb8bce6f7
P5/C3 run:    31181341275 — PASS
P4 run:       31181341370 — PASS
P1 run:       31181341405 — PASS
Fixtures:     31181340889 — PASS
```

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Каждый из четырёх artifacts содержит PostgreSQL P4, SQLite P5 и C3 comparison reports. Один архив был скачан и проверен отдельно.

## 10. Evidence boundaries

```text
C3 для 45 SUPPORTED assertions
≠ все 72 supported
≠ exhaustive equivalence
≠ PostgreSQL/SQLite operational equivalence
≠ truth/authenticity
≠ physical deletion
≠ complete conflict handling
≠ C4/C5
≠ production readiness
```

Approval, code presence, local run или manifest count не являются достаточным repository evidence.

## 11. Явно отсутствует

- complete conflict representation/resolution;
- physical/cryptographic deletion workers;
- restore-before-visibility enforcement;
- cross-project authority adapter;
- network API;
- C4 shadow workload evaluation;
- C5 operational security/privacy/incident evidence;
- production HA/backup/restore/compliance guarantees;
- Titan/Mentaury/Crystal runtime wiring;
- historical source recovery;
- package-publication decision по Issue #18.

## 12. Финализация и дальнейшие gates

PR #59 должен повторить P5/C3, P4, P1, fixtures и AI-context checks на одном final exact documentation head и сохранить четыре artifacts перед merge.

Любая последующая работа C4, C5, production, deletion execution или ecosystem integration требует нового explicit operator GO и отдельного evidence plan.
