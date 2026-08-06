# 🧬 Контракт идентичности и канонического кодирования v1

- **Контракт:** `nk-id/1.0-proposed`
- **Решение:** `PROPOSED`
- **Evidence:** `LOCALLY_TESTED` только для reference canonicalizer и vectors
- **Runtime:** `NOT_IMPLEMENTED`
- **Issue:** #14

## Назначение

Определить идентичность, которая не зависит навсегда от базы данных, языка или layout объектов.

```text
content identity ≠ Claim identity ≠ lineage identity ≠ Event identity ≠ storage identity
```

## Канонический subset

Identity-bearing objects используют UTF-8 JSON:

1. строки и ключи уже нормализованы в Unicode NFC;
2. ключи объектов сортируются лексикографически;
3. незначащие пробелы не записываются;
4. разрешены integers и booleans;
5. binary floating-point запрещён;
6. decimal quantities передаются строкой по grammar конкретного поля;
7. явный `null` запрещён — optional field пропускается;
8. timestamp в identity имеет форму `YYYY-MM-DDTHH:MM:SSZ`;
9. новые identity-bearing fields требуют новой версии контракта.

## Домены и идентификаторы

| Идентичность | Domain prefix | Внешний вид |
|---|---|---|
| Content | `nk-id-content-v1\0` | `nkh1:<sha256>` |
| Claim | `nk-id-claim-v1\0` | `nkc1:<sha256>` |
| Lineage | `nk-id-lineage-v1\0` | `nkl1:<sha256>` |

`content_hash` определяет заявленное смысловое содержание. `claim_id` определяет source-bound assertion через `content_hash`, `source_ref`, `source_record_id` и `asserted_at`. `lineage_id` выводится независимо из явных namespace и seed. Backend row ID не заменяет ни один из этих идентификаторов.

## Collision и migration

- одинаковый identifier при разных canonical bytes — hard collision incident;
- записи нельзя незаметно объединять или перезаписывать;
- migration создаёт проверяемые aliases старой и новой версии;
- исходные identifiers и bytes сохраняются, если это допускает retention policy;
- смена hash требует нового prefix и domain.

## Граница доказательства

Python canonicalizer и fixtures показывают детерминированность только для заявленных vectors. Они не доказывают cross-language equivalence, storage portability или использование контракта историческим `v0.1.2.1`. Для C3 нужны две существенно независимые реализации.

# 📜 Контракт atomic append, ordering и replay v1

- **Контракт:** `nk-event/1.0-proposed`
- **Решение:** `PROPOSED`
- **Evidence:** `LOCALLY_TESTED` только для fixture integrity
- **Runtime:** `NOT_IMPLEMENTED`
- **Issue:** #15

## Writer model

Версия 1 задаёт **одного авторитетного writer**. Multi-writer не входит в эту версию и не выводится автоматически из hash chain.

```text
command intent
→ schema validation
→ authority check
→ idempotency decision
→ atomic history append
→ durability acknowledgement
→ disposable projections
→ replay Receipt
```

## Idempotency

- первый валидный command создаёт ровно один Event;
- retry с тем же canonical command digest возвращает исходный append result;
- тот же key с другим digest отклоняется как `IDEMPOTENCY_CONFLICT`;
- read-time deduplication не считается durable idempotency.

## Ordering

`global_seq` и `stream_seq` непрерывны в объявленном single-writer scope. Timestamp не заменяет sequence order. Valid time, observation time и record time не смешиваются.

## Event envelope

Envelope связывает command identity, idempotency key, stream, sequence, actor, authority, recorded time, event type, schema version, payload commitment и previous global hash. Словарь остаётся:

```text
ADMIT · LINK · UTILIZED · SUPERSEDED · ERASED
```

## Atomicity и projections

Authoritative append и durable idempotency record составляют одну atomic boundary. Projection обновляется после append. Ошибка projection остаётся видимой и устраняется destroy/rebuild, но не переписывает committed history.

## Граница integrity

SHA-256 chain помогает обнаружить изменение, truncation или reordering в проверяемой последовательности. Он не доказывает происхождение, не защищает от привилегированного переписывания, не реализует consensus и не подтверждает внешний timestamp.

## Replay

Replay начинается с пустого derived state, читает `global_seq`, использует заявленные schema upcasters и reducer version и создаёт evidence record. Unsupported version завершается явной ошибкой.

# 🔒 Контракт deletion, restriction и retention v1

- **Контракт:** `nk-deletion/1.0-proposed`
- **Решение:** `PROPOSED`
- **Evidence:** `LOCALLY_TESTED` только для state-machine fixtures
- **Runtime:** `NOT_IMPLEMENTED`
- **Issue:** #16

## Главное различие

```text
логический Event ERASED
≠ ограничение доступа
≠ физическое удаление
≠ crypto-erasure
≠ доказательство глобального удаления
```

Append-only architecture не отменяет legal или contractual deletion obligations.

## Data-location inventory

Профиль обязан учесть authoritative payloads, projections, caches, FTS/graph/vector indexes, external model requests, exports, Receipts, Shadow datasets, backups, replicas, migration artifacts, logs, dumps и dead-letter stores. Unknown locations остаются явными.

## State machine

```text
ACTIVE ↔ RESTRICTED
ACTIVE/RESTRICTED → ERASE_REQUESTED → ERASURE_IN_PROGRESS
ERASURE_IN_PROGRESS → PARTIALLY_ERASED → retry
ERASURE_IN_PROGRESS → CRYPTO_ERASED | PHYSICALLY_ERASED
допустимый этап → RETENTION_HOLD или FAILED_RETRYABLE
```

Retention hold блокирует destructive completion, но не расширяет право доступа.

## Restore rule

Восстановленный backup остаётся в quarantine, пока не применены restriction и erasure records. Данные нельзя делать queryable раньше актуального deletion state.

## Crypto-erasure

Нужны scope-specific key separation, документированная hierarchy, evidence уничтожения и описание residual metadata. Нельзя молча уничтожать unrelated records через общий ключ.

## Receipt boundary

Deletion Receipt перечисляет verified, pending и unknown locations, policy, authority, attempts, provider acknowledgements и limits. Он не заявляет complete global erasure.

# 🧪 Протокол executable conformance fixtures v1

- **Контракт:** `nk-fixtures/1.0-proposed`
- **Решение:** `PROPOSED`
- **Tooling:** `IMPLEMENTED / LOCALLY_TESTED`
- **Kernel runtime conformance:** `UNSUPPORTED`
- **Issue:** #17

## Артефакты

`contracts/registry.json` хранит stable assertion IDs и status. `contracts/schemas/` содержит neutral JSON schemas. `contracts/fixtures/` содержит identity, event, deletion и epistemic corpora.

Fixture указывает version, expected result и equivalence class. Unsupported assertion нельзя silently skip.

## Equivalence

- **byte** — одинаковые canonical bytes или identifier;
- **structural** — одинаковые обязательные поля и связи;
- **semantic** — сохранён смысл identity, scope, authority, time, conflict и unknown;
- **behavioural** — одинаковые observable outcomes в ограниченной workload.

## Runner

```bash
python tools/conformance/runner.py validate
```

Проверяются registry uniqueness, identity vectors, event chain, deletion transitions и positive/negative coverage `NK-EPI-001..008`.

External adapter запускается через `adapter --output ... -- <command>` и получает путь к manifest. Ошибка процесса, malformed JSON, missing support state или silent skip считаются failure.

## Граница evidence

Встроенный Python profile — reader fixture integrity, а не Kernel implementation. PASS не доказывает runtime. Для C2 нужен committed CI result, для C3 — две существенно независимые implementation profiles.
