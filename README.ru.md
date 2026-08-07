# Velantrim Native Kernel

> **Зрелость:** `RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

Velantrim Native Kernel — технологически нейтральная архитектура сохранения смысловой идентичности, записанных изменений, полномочий, конфликтов, воспроизводимости и доказательств через заменяемые профили хранения и вычислений.

```text
Архитектурный Canon
→ принятые абстрактные контракты
→ заменяемые профили реализации
→ точные тесты и evidence
```

PostgreSQL, SQLite, Python, LLM, embeddings, графы, CPU, GPU и будущие субстраты — инструменты, а не постоянное определение Kernel.

## Текущая реализация

```text
Profile ID:       native-kernel/postgresql-reference
Evidence lineage: clean/postgresql-reference/0.1
Version:          0.2-p2
```

### P1 — независимое semantic core

`native_kernel.semantic_core` реализует:

- canonical JSON и идентичности `nkh1` / `nkc1` / `nkl1`;
- immutable semantic objects и Commands;
- explicit deny-by-default authority;
- детерминированный логический reducer;
- состояния restriction/deletion;
- ограниченные admission/deletion Receipts.

### P2 — PostgreSQL append/idempotency profile

`native_kernel.postgresql_profile` добавляет ограниченный storage profile:

```text
явное полномочие
→ DB-backed writer owner/epoch fence
→ durable scoped idempotency
→ rollback-safe global/stream counters
→ atomic Event + idempotency commit
→ canonical payload/envelope bytes
→ nkp1 / nke1 integrity chain
```

Профильные решения:

- PostgreSQL `16–18`;
- Psycopg `>=3.3,<3.4`, lazy import;
- Python `>=3.11,<3.13`;
- нумерованные SQL migrations с SHA-256 ledger;
- один authoritative writer lease на Kernel instance.

Это детали профиля, а не Architecture Canon.

## Граница доказательств

Локально зафиксировано:

```text
9 P2 unit tests PASS
5 P2 manifest tests PASS
manifest validator PASS
compileall PASS
5 PostgreSQL integration tests DECLARED / NOT RUN — нет локального PostgreSQL DSN
repository workflow result NOT_RECORDED
```

Следовательно:

```text
P2-код существует
≠ PostgreSQL integration доказана
≠ replay/projection runtime
≠ assertion-level conformance
≠ C1/C2/C3
≠ production durability/security/privacy guarantee
```

Все 72 registry assertions остаются runtime `UNSUPPORTED` до P4.

## Контракты

Приняты:

- `nk-id/1.0` — canonical identity;
- `nk-event/1.0` — single-writer append, idempotency, ordering и replay boundary;
- `nk-deletion/1.0` — restriction/deletion/retention semantics;
- `nk-fixtures/1.0` — executable evidence protocol.

Основные документы:

- [`STATUS.md`](STATUS.md)
- [`ARCHITECTURE.md`](ARCHITECTURE.md)
- [`docs/contracts/NORMATIVE_CONTRACTS_V1.ru.md`](docs/contracts/NORMATIVE_CONTRACTS_V1.ru.md)
- [`docs/rfc/0002-postgresql-reference-profile-v0.ru.md`](docs/rfc/0002-postgresql-reference-profile-v0.ru.md)
- [`docs/adr/0016-authorize-p2-postgresql-append-profile.md`](docs/adr/0016-authorize-p2-postgresql-append-profile.md)
- [`native_kernel/postgresql_profile/README.md`](native_kernel/postgresql_profile/README.md)

## Проверка

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_postgresql_profile_unit.py' -v
python -m unittest discover -s tests -p 'test_p2_manifest.py' -v
python tools/profiles/validate_p2_manifest.py
```

PostgreSQL integration:

```bash
python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
NK_TEST_POSTGRES_DSN='postgresql://...' \
  python -m unittest discover -s tests -p 'test_postgresql_profile_integration.py' -v
```

## Что отсутствует

- P3 projections/rebuild и replay/upcasters;
- operational replay/deletion Receipts;
- физическое или криптографическое удаление;
- network API;
- P4 conformance adapter;
- P5 independent SQLite profile;
- C1/C2/C3;
- решение по публикации/лицензии Issue #18;
- runtime wiring Titan, Mentaury или Crystal;
- восстановление исторического `v0.1.2.1` и исходных 44 тестов.

## Граница source recovery

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 остаётся независимым. `NOT_FOUND_IN_ACCESSIBLE_SOURCES` не означает `GLOBALLY_LOST`.
