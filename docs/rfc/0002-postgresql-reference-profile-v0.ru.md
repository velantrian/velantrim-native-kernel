# RFC-0002: PostgreSQL Reference Profile v0

- **Статус:** `ACCEPTED`
- **Operator approval:** `APPROVED`
- **Текущая фаза:** `P2 PARTIAL / REPOSITORY-INTEGRATION-TESTED`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Profile version:** `0.2-p2`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Связано:** ADR-0001, ADR-0009, ADR-0011–0016, Issues #1, #18, #46 и PR #47

## Назначение и граница

Это первая clean full-profile lineage. Она не является реконструкцией или переименованием отсутствующего `v0.1.2.1`.

```text
clean reference profile
≠ recovered historical source
≠ Architecture Canon
≠ automatic C1/C2/C3
```

PostgreSQL tables, Psycopg, Python modules, locks, indexes и migrations — заменяемые детали профиля.

## Состояние фаз

| Фаза | Состояние |
|---|---|
| P0 profile plan | accepted / complete |
| P1 semantic core | merged / repository-tested |
| P2 authoritative append/idempotency | partial / repository-integration-tested |
| P3 replay/projections/Receipts | not authorized |
| P4 conformance adapter | not authorized |
| P5 independent SQLite profile | not authorized |

## P2 technology profile

```text
PostgreSQL compatibility: 16–18
Repository matrix:        PG16/18 × Python3.11/3.12
Driver:                   psycopg >=3.3,<3.4
Migration strategy:       numbered SQL + SHA-256 ledger
Writer strategy:          durable owner/epoch lease per instance
Counter strategy:         row-locked transactional counters
```

Driver загружается лениво, поэтому P1 остаётся standard-library-only.

## Транзакционная модель

```text
Command
→ explicit authority
→ lock instance
→ validate writer owner/epoch/expiry
→ inspect durable idempotency
   ├── same digest → original committed Event
   └── different digest → IDEMPOTENCY_CONFLICT
→ allocate contiguous global/stream numbers
→ canonical payload/envelope bytes
→ append Event and advance counters
→ persist idempotency result
→ commit
→ acknowledge
```

Idempotency scope: `(instance_id, command_contract, idempotency_key)`.

Authoritative counters хранятся в обычных таблицах, а не PostgreSQL sequences, чтобы rollback не создавал видимые разрывы ordering.

## Integrity и migrations

P2 хранит JSONB, exact canonical payload/envelope bytes, `nkp1`, `nke1`, previous global hash и writer epoch. Hash chain — сигнал целостности, а не authentication.

Migrations используют `NNNN_name.sql`, SHA-256 ledger и transaction advisory lock. Drift применённой версии вызывает явную ошибку.

## Repository evidence

PR #47 evidence head `e80492bcacde2ff2be3a2ee03aa5aa53a714d288`:

```text
P2 run 31151297646 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
AI context run 31151298002 — PASS
P1 and fixture integrity — PASS
```

Каждый P2 job прошёл unit, manifest, compile и пять integration scenarios: migration idempotency, lease fencing, retry/conflict atomicity, rollback-safe sequence reuse и concurrent same-digest append.

## Граница evidence

```text
P2 integration REPOSITORY_REPRODUCED
≠ P3 replay/projection runtime
≠ operational deletion
≠ P4 conformance
≠ C1/C2/C3
≠ production operations guarantee
```

Все 72 assertion-level runtime statuses остаются `UNSUPPORTED` до P4.

## Следующий gate

P3 требует отдельного operator GO и нового Issue/PR.
