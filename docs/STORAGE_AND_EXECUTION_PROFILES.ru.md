# 🐘📦 Профили хранения и вычисления

**[English](./STORAGE_AND_EXECUTION_PROFILES.md) · [Русский](./STORAGE_AND_EXECUTION_PROFILES.ru.md)**

- **Статус решения:** `ACCEPTED`
- **Уровень доказательств:** `DOCUMENTED`
- **Статус реализации:** `NOT_STARTED`
- **Одобрение оператора:** `APPROVED`
- **Область:** направление современных профилей реализации; не Architecture Canon

> [!IMPORTANT]
> PostgreSQL и SQLite — заменяемые современные профили реализации. Ни одна из этих баз данных не определяет смысл Claim, Event, Relation, эпистемического состояния, конфликта, Projection или Receipt.

## 🧭 Решение в одной схеме

```text
🏛️ Architecture Canon
идентичность · история · provenance · время · конфликт · receipt
                              │
                              ▼
📐 Абстрактный контракт хранения
append · чтение истории · replay · verify · rebuild · migrate
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
🐘 PostgreSQL-профиль                 📦 SQLite-профиль
основной полный профиль              опциональный embedded-профиль
локальный или удалённый               локальный single-file deployment
конкурентный / server-oriented        компактный / reference / test
```

Текущее направление:

- 🐘 **PostgreSQL — основной полноценный современный профиль хранения** для серьёзного локального или серверного развёртывания.
- 📦 **SQLite сохраняется как опциональный embedded-, переносимый, reference-, test-, recovery- или constrained-device профиль.**
- 🧪 In-memory профиль может использоваться для узких детерминированных тестов.
- 🌌 Будущие профили могут использовать технологии и физические субстраты, которые вообще не похожи на SQL-базы.

Это выбор профиля реализации, а не утверждение, что PostgreSQL является самой архитектурой.

## 📴 Offline не означает SQLite

Полностью автономный компьютер может локально запускать все нужные компоненты:

```text
💻 Один локальный компьютер — интернет не требуется
│
├── 🤖 небольшая или крупная локальная модель
├── 🧬 реализация Native Kernel
├── 🐘 PostgreSQL на localhost
├── 🔎 локальные индексы и проекции
└── 📁 локальные документы и файлы моделей
```

PostgreSQL может работать как локальный server process, а не только как удалённая облачная база. Локальная модель взаимодействует с локальным Kernel-сервисом, а Kernel использует PostgreSQL через `localhost` без облака и интернета.

```text
Локальная модель
       │ запросы через объявленный Kernel interface
       ▼
Реализация Native Kernel
       │ контракт хранения
       ▼
PostgreSQL на localhost
```

Поэтому в архитектуре нельзя закреплять ложное равенство:

```text
❌ offline = SQLite
❌ online  = PostgreSQL
```

Более точное разделение:

```text
✅ полный локальный / серверный профиль = PostgreSQL
✅ компактный embedded-профиль          = SQLite
```

## ⚙️ Вычислительный профиль и профиль хранения независимы

Система должна разделять два выбора:

```text
🧠 Compute Profile
├── локальная небольшая модель
├── локальная крупная модель
├── удалённая модель
├── символический движок
└── будущий вычислительный субстрат

🗄️ Storage Profile
├── PostgreSQL
├── SQLite
├── in-memory test store
└── будущий субстрат хранения
```

Локальной LLM не требуется SQLite. Удалённой модели не обязательно нужен PostgreSQL. Выбор compute и storage ортогонален, если конкретный профиль реализации явно не документирует ограничение.

## 🔀 Profile Selector, а не маршрутизация базы для каждого запроса

Активный авторитетный профиль хранения обычно выбирается при запуске процесса, узла или deployment:

```yaml
storage:
  profile: postgresql
  connection: postgresql://localhost/native_kernel

compute:
  profile: local_model
```

или:

```yaml
storage:
  profile: sqlite
  path: ./native-kernel.db
```

```text
Запуск Kernel
      ↓
чтение объявленного профиля
      ↓
создание одного Storage Adapter
      ↓
использование одной авторитетной истории экземпляра
```

Обычный request router не должен распределять авторитетные записи между разными базами:

```text
❌ запрос A → SQLite
❌ запрос B → PostgreSQL
❌ запрос C → снова SQLite
```

Такой подход может разделить историю, изменить порядок событий, продублировать Claims и сделать источник истины неоднозначным.

## 🔄 Переключение профиля является миграцией

Замена авторитетного профиля хранения — это контролируемая миграция субстрата, а не обычное решение Router:

```text
1. остановить или оградить новые записи
2. зафиксировать source position и migration Receipt
3. экспортировать авторитетную историю в канонической interchange-форме
4. проверить identity, ordering, hashes, provenance и counts
5. импортировать историю в новый профиль
6. выполнить полный replay
7. сравнить объявленное семантическое состояние
8. активировать новый профиль
9. сохранить доказательства rollback
```

Требуется документированная семантическая эквивалентность, а не обязательное совпадение физических байтов:

```text
одна авторитетная история
        ↓
PostgreSQL reducer path
        ↓
семантическое состояние A

та же авторитетная история
        ↓
SQLite reducer path
        ↓
семантическое состояние B

требование: A ≡ B по объявленному conformance rule
```

## 🐘 Почему PostgreSQL — основной полный профиль

PostgreSQL лучше подходит, когда реализации нужны:

- несколько параллельных readers или writers;
- постоянно работающий локальный сервис;
- несколько агентов, процессов, пользователей или устройств;
- транзакционная целостность связанных операций;
- роли, права и операционная изоляция;
- крупная история событий и сложные temporal queries;
- JSON, рекурсивные запросы, full-text search и расширения;
- backup, restore, replication и зрелые операционные инструменты;
- путь от одного локального компьютера к удалённому серверу без изменения семантических контрактов.

Компьютер, способный запускать локальную модель, обычно способен запускать и локальный PostgreSQL. Поэтому PostgreSQL разумно использовать как основной laboratory- и deployment-профиль полной системы.

## 📦 Почему SQLite остаётся полезным

SQLite сохраняет более узкую, но полноценную роль:

- embedded desktop- и mobile-приложения;
- компактные single-process инструменты;
- переносимые snapshots и демонстрации;
- детерминированные fixtures и CI-тесты;
- recovery- и diagnostic-утилиты;
- ограниченные устройства;
- установки, где отдельный database service сознательно нежелателен.

SQLite — не ухудшенная версия архитектуры. Это другой операционный профиль с меньшим envelope конкурентности и администрирования.

## 🧩 Граница адаптера

Kernel-семантика должна зависеть от абстрактного контракта, а не от деталей SQL-диалекта:

```text
StorageContract
├── append_event(...)
├── read_authoritative_history(...)
├── verify_integrity(...)
├── load_projection_source(...)
├── record_migration_receipt(...)
└── expose_declared_capabilities(...)
```

Возможные реализации:

```text
PostgreSQLStorageAdapter
SQLiteStorageAdapter
InMemoryTestAdapter
FutureSubstrateAdapter
```

Backend-generated row IDs, SQL-таблицы, foreign keys, indexes, WAL-настройки, extensions и transaction syntax должны оставаться деталями реализации, пока отдельный cross-profile contract явно не поднимет конкретное поведение выше границы адаптера.

## 🔒 Инварианты

1. PostgreSQL — предпочтительный текущий полный профиль, но не постоянный Canon.
2. SQLite является опциональным и не равен offline-режиму.
3. Один экземпляр Kernel имеет одну объявленную авторитетную историю, если отдельно не определён distributed-history protocol.
4. Compute routing не должен незаметно менять storage authority.
5. Router может выбирать compute- или retrieval-механизм, но не чередовать авторитетные хранилища без протокола.
6. Миграция профиля должна иметь Receipt, проверяться, воспроизводиться и допускать rollback там, где он заявлен.
7. PostgreSQL- и SQLite-профили должны сохранять одинаковые объявленные семантические контракты.
8. Cache, replica, snapshot и Projection нельзя путать с авторитетной историей.
9. Локальная модель может полностью автономно работать с локальным PostgreSQL.
10. Будущие субстраты допускаются через conformance, а не через сходство с SQL.

## 🧪 Какие доказательства нужны до заявлений о реализации

В публичном `main` пока нет runtime, реализующего это решение. Для будущего заявления о профиле потребуются как минимум:

- committed `StorageContract` или эквивалентный interface;
- один канонический fixture истории событий;
- ожидаемое reduced semantic state;
- PostgreSQL replay- и rebuild-тесты;
- SQLite replay- и rebuild-тесты, если заявляется SQLite;
- cross-profile semantic-equivalence tests;
- migration- и rollback-тесты;
- failure cases для duplicate, ordering, interruption и corruption;
- явные Receipts миграции и восстановления;
- документированные операционные ограничения каждого профиля.

> Одна работающая PostgreSQL-реализация докажет PostgreSQL-профиль. Она не докажет storage neutrality. Для нейтральности нужен хотя бы ещё один существенно отличный соответствующий профиль или эквивалентные cross-substrate доказательства.

## 🚫 Что это решение не делает

Документ не:

- требует PostgreSQL в каждой реализации;
- требует SQLite в каждом продукте;
- определяет production schema;
- превращает PostgreSQL extension в Canon;
- задаёт distributed consensus или offline multi-writer synchronization;
- заявляет, что runtime уже существует в `main`;
- обязывает Titan, Crystal, Mentaury или другой проект следовать этому выбору.

## 📚 Связанные документы

- [`FOUNDATIONAL_INTENT.ru.md`](./FOUNDATIONAL_INTENT.ru.md)
- [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md)
- [`INTEGRATION_BOUNDARIES.md`](./INTEGRATION_BOUNDARIES.md)
- [`adr/0001-architecture-canon-vs-implementation-profiles.md`](./adr/0001-architecture-canon-vs-implementation-profiles.md)
- [`adr/0009-postgresql-primary-sqlite-optional-profile.md`](./adr/0009-postgresql-primary-sqlite-optional-profile.md)
