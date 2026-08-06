# 🧬 Фундаментальный каркас контрактов

**[English](./FOUNDATIONAL_CONTRACT_SKELETON.md) · [Русский](./FOUNDATIONAL_CONTRACT_SKELETON.ru.md)**

- **Статус решения:** `PROPOSED`
- **Уровень доказательств:** `DOCUMENTED`
- **Статус реализации:** `NOT_STARTED`
- **Одобрение оператора:** `PENDING`
- **Версия черновика:** `foundational-skeleton/0.1`
- **Трек:** `Foundational Architecture / Abstract Contracts`
- **Область:** нейтрально к технологиям, хранилищам, моделям, runtime, аппаратуре и мировоззрению
- **Влияние на Issue #1:** `NONE`

> [!IMPORTANT]
> Этот документ описывает архитектурный скелет, а не готовую работающую машину. Нормативные слова относятся только к предлагаемой контрактной границе. Они не становятся принятым Canon, поведением runtime или доказательством соответствия, пока связанный ADR не принят и необходимые артефакты не созданы.

## 1. Назначение

Native Kernel сначала нужен точный скелет, а уже потом полный runtime.

Скелет должен сохранять смысл при замене реализаций и не позволять одному перегруженному объекту, схеме базы данных, модели, event bus или процессору незаметно стать самой архитектурой.

Предложение делит фундамент на шесть семейств контрактов:

```text
🧩 Семантические роли
        ↓
🧬 Идентичность и каноническое кодирование
        ↓
📜 Событие / наблюдение / записанное изменение
        ↓
🛡️ Полномочия и допуск
        ↓
⚔️ Конфликт и явная неизвестность
        ↓
🔄 Соответствие и семантическая эквивалентность
```

Эти семейства связаны, но не взаимозаменяемы:

```text
семантическое содержание
≠ утверждение конкретного источника
≠ наблюдение
≠ доказательство
≠ решение о допуске
≠ производное эпистемическое состояние
≠ строка или объект конкретной реализации
```

## 2. Место в архитектуре Native Kernel

```text
Архитектурный Canon
        ↓
Фундаментальный каркас контрактов
        ↓
Версионируемые нормативные контракты и fixtures
        ↓
Заменяемые профили реализации
        ↓
Воспроизводимые доказательства
```

Этот документ не заменяет [`ARCHITECTURE.md`](../ARCHITECTURE.md), [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) или предложение о границах мира и знания. Он задаёт устойчивую карту, на которую смогут ссылаться эти документы, будущие схемы, fixtures и профили.

## 3. Общая контрактная оболочка

Каждое фундаментальное семейство контрактов ДОЛЖНО уметь объявить или перевести следующий смысл там, где он применим:

| Поле смысла | Обязательный вопрос |
|---|---|
| **Идентичность контракта** | Какое семейство, assertion и версия действуют? |
| **Семантическая область** | Какой домен, субъект, юрисдикция, tenant, проект или мировоззренческая рамка описываются? |
| **Актор / источник** | Кто или что создало, наблюдало, утверждало, преобразовало, допустило или разрешило? |
| **Provenance** | Какие источники, методы, преобразования и пробелы известны? |
| **Временной смысл** | Когда это было действительно, наблюдалось, записано, допущено, пересмотрено или ограничено? |
| **Полномочие** | Какое полномочие было применено, в какой области и по какой policy? |
| **Lineage** | Какую предыдущую запись это продолжает, исправляет, уточняет или заменяет? |
| **Evidence / основание** | Какие кандидаты доказательств или основания решения учитывались? |
| **Граница Receipt** | Что Receipt способен доказать, а что остаётся недоказанным? |
| **Профиль / версия** | Какая реализация и версия контракта создали представление? |

Это семантическая оболочка, а не зафиксированная JSON-схема. Профиль может представлять поля иначе, только если сохраняет заявленный смысл и conformance mapping.

---

# 4. Семейство I — Семантическая модель объектов 🧩

**ID семейства:** `NK-SEM`

## 4.1 Проблема

Текущая архитектура использует `Claim` как долговременную семантическую запись. Без более точных различий один объект можно одновременно принять за содержание, утверждение, наблюдение, доказательство, гипотезу и допущенное знание.

## 4.2 Предлагаемое правило

`Claim` остаётся корневой долговременной записью, пока будущий ADR не докажет необходимость нового корневого примитива. Claim ДОЛЖЕН сохранять или переводить семантическую роль представленного содержания.

Концептуальные роли:

| Роль | Смысл | Не должна незаметно становиться |
|---|---|---|
| **Proposition** | семантическое содержание в заявленной области | утверждением источника или истиной |
| **Assertion** | актор/источник утверждает proposition | проверенным наблюдением или допущенным знанием |
| **Observation** | получен сигнал, свидетельство, trace или результат | полным объяснением |
| **Measurement** | значение получено объявленным методом, рамкой, шкалой и моделью неопределённости | контекстно-свободным фактом |
| **Interpretation** | смысл назначен при указанных предположениях | самим наблюдением |
| **Hypothesis** | проверяемый или анализируемый кандидат объяснения | установленным объяснением |
| **Question** | явно нерешённая информационная потребность | ложным утверждением |
| **Evidence reference** | артефакт или trace, значимый для оценки | автоматическим доказательством или полномочием |

Эти роли МОГУТ выражаться через `claim_kind`, типизированные связи, mapping профиля или другой версионируемый контракт. В этом предложении они не являются обязательным enum.

## 4.3 Предлагаемые assertions

| Assertion ID | Обязательный смысл |
|---|---|
| `NK-SEM-001` | семантическое содержание отличимо от утверждения конкретного источника |
| `NK-SEM-002` | наблюдение и измерение сохраняют смысл метода и provenance |
| `NK-SEM-003` | интерпретация и гипотеза отличимы от наблюдения |
| `NK-SEM-004` | релевантность evidence не устанавливает истину автоматически |
| `NK-SEM-005` | вопрос или неизвестность не кодируются незаметно как false |
| `NK-SEM-006` | состояние допуска не выводится только из роли или наличия в хранилище |
| `NK-SEM-007` | scope и domain Claim остаются явными, когда влияют на смысл |
| `NK-SEM-008` | перевод ролей между профилями объявлен и проверяем |

## 4.4 Anti-Canon

Это семейство не требует:

- универсальной онтологии;
- одного навсегда зафиксированного списка Claim kinds;
- LLM-классификатора;
- graph database;
- обязательной отдельной таблицы `Proposition`, `Observation` или `Evidence`;
- нового event verb;
- утверждения, что текущий словарь полон.

---

# 5. Семейство II — Идентичность и каноническое кодирование 🧬

**ID семейства:** `NK-ID`

## 5.1 Необходимые уровни идентичности

Профиль ДОЛЖЕН различать или явно сопоставлять:

```text
идентичность содержания
≠ идентичность Claim
≠ идентичность lineage
≠ идентичность Event
≠ идентичность хранилища
```

| Идентичность | Предлагаемая ответственность |
|---|---|
| **Content identity** | определяет каноническое семантическое содержание по объявленному content contract |
| **Claim identity** | определяет долговременную запись Claim с указанным identity-bearing scope |
| **Lineage identity** | объединяет явное семейство продолжения/ревизии, не отождествляя все версии |
| **Event identity** | определяет один записанный переход или результат append-попытки |
| **Storage identity** | локальная строка, объект, shard, адрес или backend key; недостаточна как семантическая идентичность |

## 5.2 Предлагаемые assertions

| Assertion ID | Обязательный смысл |
|---|---|
| `NK-ID-001` | backend-generated ID не является единственным источником семантической идентичности |
| `NK-ID-002` | identity-bearing поля объявлены для каждой версии контракта |
| `NK-ID-003` | правила канонического кодирования детерминированы внутри объявленной версии |
| `NK-ID-004` | правила Unicode, чисел, времени, null, порядка, omission и неоднозначности явны |
| `NK-ID-005` | hash использует объявленный алгоритм, domain и version separation |
| `NK-ID-006` | collision не может незаметно перезаписать или объединить разные записи |
| `NK-ID-007` | migration и aliasing идентичности сохраняют проверяемый lineage |
| `NK-ID-008` | независимые профили могут проверить одинаковые golden и invalid vectors |

Точные канонические bytes, normalization policy, hash agility и migration rules остаются в [Issue #14](https://github.com/velantrian/velantrim-native-kernel/issues/14). Этот каркас фиксирует разделение, а не окончательный алгоритм.

## 5.3 Anti-Canon

Идентичность НЕ ДОЛЖНА навсегда зависеть от:

- PostgreSQL sequence;
- SQLite rowid;
- Python object identity;
- недокументированной сериализации одной JSON-библиотеки;
- embedding одного model provider;
- native memory layout одного процессора.

---

# 6. Семейство III — Событие, наблюдение и записанное изменение 📜

**ID семейства:** `NK-EVT`

## 6.1 Четыре различных слоя

Native Kernel ДОЛЖЕН сохранять различие:

```text
🌍 событие в представляемом мире
👁️ наблюдение или измерение этого события
💾 запись системой
⚖️ решение о допуске или полномочии относительно записи
```

Это семантические слои. Они не являются предлагаемым расширением принятого исследовательского event vocabulary.

## 6.2 Граница command-to-history

Будущий implementation contract должен явно описывать:

```text
command intent
→ validation
→ authorization / admission eligibility
→ durable idempotency decision
→ atomic append result
→ declared ordering
→ reducer input
→ derived state / projection
→ Receipt
```

## 6.3 Предлагаемые assertions

| Assertion ID | Обязательный смысл |
|---|---|
| `NK-EVT-001` | событие представляемого мира не отождествляется с записью системы о нём |
| `NK-EVT-002` | observation time, record time, valid time и write order не смешиваются незаметно |
| `NK-EVT-003` | commands и записанные Events отличимы |
| `NK-EVT-004` | семантика duplicate command и scope idempotency объявлены |
| `NK-EVT-005` | append acknowledgement указывает достигнутую durability и atomicity |
| `NK-EVT-006` | ordering rules детерминированы в заявленной writer model |
| `NK-EVT-007` | версии reducer и schema привязаны к replay evidence |
| `NK-EVT-008` | ошибка projection не может незаметно переписать authoritative history |
| `NK-EVT-009` | correction, supersession, restriction и erasure остаются явными переходами |
| `NK-EVT-010` | пределы tamper, truncation, reordering и fork объявлены в threat model |

Детальный append/idempotency/ordering/crash/replay contract остаётся в [Issue #15](https://github.com/velantrian/velantrim-native-kernel/issues/15).

## 6.4 Граница текущего словаря

Текущий документированный исследовательский словарь остаётся:

```text
ADMIT · LINK · UTILIZED · SUPERSEDED · ERASED
```

Термины `OBSERVED`, `CONFLICT_OPENED` или `POLICY_CHANGED` не принимаются как event verbs этим документом. Новые verbs требуют отдельного решения и анализа совместимости.

---

# 7. Семейство IV — Полномочия и допуск 🛡️

**ID семейства:** `NK-AUT`

## 7.1 Проблема

Система может записывать многое, но это не даёт каждому актору, модели, источнику, retrieval result или связанному проекту право менять допущенное эпистемическое состояние.

## 7.2 Authority Envelope

Каждый авторитетный переход ДОЛЖЕН уметь указать или перевести **Authority Envelope** со следующим смыслом, где применимо:

```text
actor / system reference
role или authority kind
authority domain и scope
policy reference и version
decision reference
basis / evidence references
delegation chain
temporal validity или expiry
constraints и known limits
```

Это не обязательная storage schema. Это минимальное семантическое объяснение, почему переход был разрешён.

## 7.3 Виды полномочий

Профиль МОЖЕТ различать:

- полномочие наблюдения;
- полномочие источника/утверждения;
- operational append authority;
- admission authority;
- epistemic promotion authority;
- conflict-resolution authority;
- deletion/restriction authority;
- architecture/governance authority.

Эти полномочия НЕ ДОЛЖНЫ автоматически наследоваться друг от друга.

## 7.4 Предлагаемые assertions

| Assertion ID | Обязательный смысл |
|---|---|
| `NK-AUT-001` | наличие в хранилище не означает admission |
| `NK-AUT-002` | retrieval, ranking, utility, confidence, repetition или model output не означают authority |
| `NK-AUT-003` | authority kind, scope, policy и actor остаются проверяемыми |
| `NK-AUT-004` | delegation явен и не может незаметно расширять scope |
| `NK-AUT-005` | operator approval остаётся отдельным от empirical evidence |
| `NK-AUT-006` | cross-project данные не наследуют authority через общие термины или ссылки |
| `NK-AUT-007` | deletion/restriction decision указывает authorization и proof limits |
| `NK-AUT-008` | admission Receipt фиксирует границу решения, не заявляя истину сверх evidence |

## 7.5 Граница экосистемы

- Titan cognition или tool output — вход, а не автоматический admission.
- Crystal evidence или TruthGate semantics не становятся обязательным компонентом Kernel.
- Mentaury identity/continuity authority не наследуется Kernel Events.
- История Kernel не становится универсальным truth authority всей экосистемы.

---

# 8. Семейство V — Конфликт и явная неизвестность ⚔️

**ID семейства:** `NK-CFL`

## 8.1 Классы конфликтов

Профиль ДОЛЖЕН различать применимые классы вместо одного общего флага:

```text
duplicate delivery
write-version race
divergent history
semantic contradiction
temporal mismatch
scope mismatch
provenance conflict
measurement disagreement
policy conflict
epistemic disagreement
projection drift
```

## 8.2 Паттерн Conflict Set

Будущий Conflict Set contract ДОЛЖЕН уметь сохранять:

- вовлечённые Claims, Events, histories, policies или projections;
- класс конфликта и основу обнаружения;
- candidate или established status;
- directionality и scope;
- provenance и временной контекст;
- нерешённые вопросы и отсутствующие evidence;
- reviewer/authority decisions;
- историю resolution, deferral, reopening и supersession;
- Receipts и known limits.

Conflict Set — предлагаемый семантический паттерн, а не обязательная корневая сущность или event vocabulary.

## 8.3 Дисциплина unknown

```text
unknown
≠ false
≠ unsupported certainty
≠ conflict resolution
≠ permission to invent provenance
```

Корректное состояние МОЖЕТ оставаться нерешённым при недостатке evidence или различии scopes.

## 8.4 Предлагаемые assertions

| Assertion ID | Обязательный смысл |
|---|---|
| `NK-CFL-001` | candidate conflict отличим от established conflict |
| `NK-CFL-002` | detection отличим от resolution |
| `NK-CFL-003` | write order не определяет semantic correctness сам по себе |
| `NK-CFL-004` | несовместимые Claims могут оставаться видимыми без принудительного победителя |
| `NK-CFL-005` | temporal, scope, provenance и policy mismatch остаются проверяемыми |
| `NK-CFL-006` | unknown и missing evidence остаются явными |
| `NK-CFL-007` | resolution указывает authority, policy, basis, scope и историю |
| `NK-CFL-008` | перевод профиля не может незаметно удалить нерешённый конфликт |

Семейство развивает структуру вокруг ADR-0003, не принимая конкретные OCC, CRDT, LWW, multi-writer или human-review реализации.

---

# 9. Семейство VI — Соответствие и семантическая эквивалентность 🔄

**ID семейства:** `NK-EQV`

## 9.1 Реестр контрактов

Каждый зрелый contract assertion ДОЛЖЕН иметь traceability через registry:

| Поле registry | Смысл |
|---|---|
| `contract_family` | например `NK-ID` |
| `contract_version` | версия нормативного контракта |
| `assertion_id` | стабильный assertion identifier |
| `required_semantics` | смысл, который нужно сохранить |
| `equivalence_class` | byte, structural, semantic или behavioural |
| `fixture_ids` | valid, invalid, replay, conflict, temporal, epistemic или deletion vectors |
| `profile_mapping` | runtime/schema symbols, реализующие или переводящие assertion |
| `evidence_record` | точный commit, command, environment, result и limits |
| `support_state` | supported, unsupported, partial или failed; без скрытого skip |

## 9.2 Предлагаемые assertions

| Assertion ID | Обязательный смысл |
|---|---|
| `NK-EQV-001` | каждый conformance claim называет contract и assertion version |
| `NK-EQV-002` | equivalence определена, а не используется как маркетинговое слово |
| `NK-EQV-003` | разрешённые и запрещённые различия явны |
| `NK-EQV-004` | unsupported assertions остаются видимыми |
| `NK-EQV-005` | fixture и evidence records указывают точные версии repository/profile |
| `NK-EQV-006` | projection destroy/rebuild evidence отличается от identity или deletion evidence |
| `NK-EQV-007` | для cross-profile C3 нужны два существенно разных профиля |
| `NK-EQV-008` | Receipt указывает proof boundary и известные omissions |

## 9.3 Уровни эквивалентности

```text
byte equality
    ⊂ structural comparison
        ⊂ semantic comparison
            ⊂ bounded behavioural comparison
```

Это концептуальная, а не автоматическая вложенность. Semantic comparison может разрешать разные bytes, а behavioural equality не доказывает одинаковое внутреннее представление.

Семейство напрямую связано с [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) и [Issue #17](https://github.com/velantrian/velantrim-native-kernel/issues/17).

---

# 10. Сквозные измерения

Шесть семейств используют пять измерений, которые ДОЛЖНЫ оставаться явными там, где применимы.

## 10.1 Provenance

Provenance включает источники, акторов, методы, преобразования, версии policy/profile, известные пробелы и спорные версии. Missing provenance остаётся пробелом, а не выдуманной непрерывностью.

## 10.2 Время

Профили ДОЛЖНЫ сохранять или переводить применимые оси:

- represented-world или valid time;
- observation/measurement time;
- source publication time;
- record/ingestion time;
- admission/decision time;
- revision/supersession time;
- retention/restriction/erasure time;
- deterministic write order.

Не каждый профиль обязан материализовать каждую ось, но omission и approximation должны быть объявлены.

## 10.3 Scope

Смысл или полномочие могут зависеть от domain, subject, jurisdiction, project, tenant, worldview frame, observer, method или temporal interval. Scope НЕ ДОЛЖЕН незаметно расширяться.

## 10.4 Receipt

Receipt — подотчётная запись обработки. Он может показывать inputs, decisions, exclusions, conflicts, source range, profile versions и limits. Сам по себе он не доказывает truth, completeness, authenticity, deletion или task sufficiency.

## 10.5 Удаление и ограничение

Логическое состояние `ERASED` не является полным доказательством удаления. Physical deletion, restriction, retention, backup expiry, downstream propagation, crypto-erasure и residual metadata остаются отдельным technology-neutral контрактом в [Issue #16](https://github.com/velantrian/velantrim-native-kernel/issues/16).

---

# 11. Сквозной поток

```text
Источник / актор / сенсор / модель / документ
                │
                ▼
🧩 Объявляется семантическая роль
   proposition / assertion / observation / hypothesis / question / evidence reference
                │
                ▼
🧬 Контракт идентичности выводит или проверяет identity
   content / Claim / lineage / Event / storage distinction
                │
                ▼
📜 Контракт записи добавляет явное изменение
   command / idempotency / ordering / schema / replay boundary
                │
                ▼
🛡️ Контракт authority оценивает допустимый переход
   actor / scope / policy / delegation / basis
                │
                ▼
⚔️ Reducer сохраняет state, conflict и unknown
   без silent winner / invented provenance / false certainty
                │
                ▼
🧾 Receipt фиксирует процесс и proof limits
                │
                ▼
🔄 Conformance registry связывает смысл с fixtures и evidence
```

# 12. Anti-Canon

Это предложение не делает постоянной архитектурой:

- Python, Rust, SQL, PostgreSQL, SQLite, files, graphs, vectors, FTS, LLMs, CPU, GPU или будущие substrates;
- одну class hierarchy или database schema;
- универсальную онтологию;
- одну multi-writer consistency model;
- одну truth-scoring formula;
- одну human или AI authority implementation;
- фиксированный event vocabulary сверх уже принятых записей;
- один deletion mechanism;
- одно определение сознания, жизни, реальности или ultimate origin.

# 13. Связь с существующим governance

| Область | Основная запись |
|---|---|
| Canon и implementation profiles | ADR-0001 |
| Явность конфликта | ADR-0003 |
| Rebuild-first conformance | ADR-0004 |
| Размещение causal relations | ADR-0006 |
| Approval и evidence | ADR-0007 |
| World и epistemic boundaries | ADR-0008 + `NK-EPI-001…008` |
| Storage profiles | ADR-0009 |
| Этот six-family skeleton | предложение ADR-0010 |
| Детали canonical identity | Issue #14 |
| Детали append/replay | Issue #15 |
| Детали deletion/restriction | Issue #16 |
| Executable conformance | Issue #17 |

Issue #1 не изменяется. Документ нельзя описывать как восстановленный дизайн или evidence `v0.1.2.1`.

# 14. Следующие gates

1. Рассмотреть и принять, отклонить или изменить ADR-0010.
2. Поддерживать семантическую синхронность английской и русской версий.
3. Определить точный identity contract и vectors в Issue #14.
4. Определить command/event integrity contract в Issue #15.
5. Определить deletion и restriction semantics в Issue #16.
6. Создать versioned fixture schemas и registry records в Issue #17.
7. Требовать отдельные ADR, когда деталь меняет Canon, event vocabulary, authority, identity-bearing fields или equivalence guarantees.
8. Не заявлять implementation, testing, wiring, activation, observation или portability без точного repository evidence.
