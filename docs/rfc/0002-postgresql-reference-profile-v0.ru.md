# RFC-0002: PostgreSQL Reference Profile v0

- **Статус:** `ACCEPTED`
- **Operator approval:** `APPROVED`
- **Текущая фаза:** `P2 PARTIAL IMPLEMENTATION`
- **Profile ID:** `native-kernel/postgresql-reference`
- **Profile version:** `0.2-p2`
- **Evidence lineage:** `clean/postgresql-reference/0.1`
- **Связано:** ADR-0001, ADR-0009, ADR-0011–0016, Issues #1, #18 и #46

## Назначение

Определить и реализовать первую clean full-profile lineage без реконструкции или переименования отсутствующего исторического checkpoint `v0.1.2.1`.

```text
clean reference profile
≠ recovered historical source
≠ Architecture Canon
≠ automatic C1/C2/C3
```

## Архитектурная граница

Профиль реализует принятые абстрактные контракты. PostgreSQL tables, Psycopg, Python modules, locks, indexes и migrations — заменяемые детали профиля.

## Состояние фаз

| Фаза | Состояние |
|---|---|
| P0 profile plan | accepted / complete |
| P1 semantic core | merged / locally tested |
| P2 authoritative append/idempotency | authorized / partial branch implementation |
| P3 replay/projections/Receipts | not authorized |
| P4 conformance adapter | not authorized |
| P5 independent SQLite profile | not authorized |

## Технологический профиль P2

```text
PostgreSQL compatibility: 16–18
CI service matrix:        16 and 18
Python:                   >=3.11,<3.13
Driver:                   psycopg >=3.3,<3.4
Migration strategy:       numbered SQL + SHA-256 ledger
Writer strategy:          durable owner/epoch lease per instance
Counter strategy:         row-locked transactional counters
```

Driver загружается лениво, поэтому `native_kernel.semantic_core` остаётся standard-library-only.

## Транзакционная модель

```text
Command
→ explicit authority check
→ lock Kernel instance
→ validate writer owner/epoch/expiry
→ inspect durable idempotency key
   ├── same digest → original committed Event
   └── different digest → IDEMPOTENCY_CONFLICT
→ allocate contiguous global/stream numbers
→ canonical payload/envelope bytes
→ append Event
→ update counters/history head
→ persist idempotency result
→ commit
→ acknowledge
```

Idempotency scope:

```text
(instance_id, command_contract, idempotency_key)
```

PostgreSQL sequences не используются для authoritative counters, потому что rollback не возвращает sequence values и создавал бы видимые разрывы.

## Writer fencing

`kernel_instances.writer_epoch` монотонен. Lease хранит owner, epoch и expiry. Append/renew/release требуют совпадающий непросроченный token. Новый владелец или reacquisition увеличивает epoch.

Это single-writer fencing, а не distributed consensus.

## Integrity

P2 хранит JSONB payload, точные canonical payload/envelope bytes, `nkp1`, `nke1`, previous global hash и writer epoch. Hash chain — сигнал целостности, а не authentication или защита от любого privileged rewrite.

## Migrations

Файлы используют `NNNN_name.sql`; точные SHA-256 и name записываются в migration ledger. Изменение применённых bytes вызывает явный drift failure. Advisory transaction lock сериализует bootstrap и ledger.

## Evidence

```text
9 P2 unit tests PASS
5 P2 manifest tests PASS
validator и compileall PASS
5 PostgreSQL integration tests declared
local PostgreSQL integration NOT RUN — no DSN/server
repository CI NOT_RECORDED
```

Integration suite проверяет migration/instance idempotency, lease fencing, append/retry/conflict, rollback sequence и concurrent same-digest append.

## Не входит в P2

P3 projections/replay, operational Receipts, deletion execution, network API, P4 conformance, P5 SQLite, C1/C2/C3, production guarantees, ecosystem wiring и source recovery.

Все 72 assertion-level runtime results остаются `UNSUPPORTED` до P4.

## Promotion gate

P2 можно назвать PostgreSQL-integrated только после exact PostgreSQL 16/18 runs. P3 требует отдельного operator GO и нового Issue/PR.
