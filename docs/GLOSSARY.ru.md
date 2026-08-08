# 📖 Глоссарий Native Kernel

**[English](./GLOSSARY.md) · [Русский](./GLOSSARY.ru.md)**

> Этот глоссарий предназначен для входа в проект. При сокращениях и расхождениях авторитетны Architecture Canon, принятые ADR и нормативные контракты.

## Основные семантические термины

| Термин | Краткое определение | Важная граница |
|---|---|---|
| **Claim** | Неизменяемая семантическая единица с объявленной ролью, стабильной identity и полями provenance; роли могут включать proposition, observation, measurement, interpretation, hypothesis, question или explicit unknown. | Claim не становится автоматически истинным, актуальным, авторизованным или свободным от конфликта. |
| **Claim identity** | Детерминированная identity, полученная по версионированному canonicalization contract. | Совпадение identity не доказывает истину или подлинность источника. |
| **Content hash** | Версионированный digest canonical semantic content. | Равные hashes означают равные canonical bytes по объявленному контракту, а не одинаковое происхождение в мире. |
| **Lineage** | Стабильная связь непрерывности для ревизий и связанной семантической истории. | Lineage не является identity, владением, личностью или доказательством причинности. |
| **Event** | Append-only запись принятого запроса на переход состояния: `ADMIT`, `LINK`, `UTILIZED`, `SUPERSEDED`, `ERASED`. | Event фиксирует принятую системой историю, а не непосредственную реальность. |
| **Event Envelope** | Версионированная структура с identity, order, actor/authority, временем, payload и hash-chain commitments. | Валидный envelope не делает payload истинным. |
| **Reducer** | Детерминированная функция восстановления semantic state из упорядоченных Events. | Reducer v1 исторически стабилен; более строгие referential rules только предложены в ADR-0024. |
| **Semantic State** | Детерминированный результат reducer для объявленной версии. | Текущий runtime state ещё не является полной executable epistemic model. |
| **Epistemic State** | Архитектурное представление того, что поддержано, спорно, неизвестно, restricted, superseded или иначе ограничено. | `NK-EPI` остаётся `0/8 SUPPORTED`; полный epistemic layer нельзя описывать как реализованный. |
| **Unknown** | Явное отсутствие обоснованного ответа или разрешённого состояния. | Unknown не равно false, rejected, erased, unavailable или unsupported. |
| **Conflict Set** | Намеренно сохранённая группа несовместимых или спорных Claims. | Conflict lifecycle остаётся архитектурной/контрактной работой; reducer v1 не строит полный Conflict Set runtime. |
| **Superseded** | Записанная связь, по которой у Claim объявлен successor. | Superseded не означает erased, false, физически удалённый или автоматически разрешённый конфликт. |
| **Erased** | Семантический Event/state marker в текущей ограниченной реализации. | Он не доказывает physical, cryptographic, backup-wide или globally complete deletion. |
| **Relation / Link** | Типизированная семантическая связь между Claims. | Название relation само по себе не доказывает causality, symmetry, transitivity или acyclicity. |

## Хранение, replay и evidence

| Термин | Краткое определение | Важная граница |
|---|---|---|
| **Architecture Canon** | Технологически независимые инварианты, которые реализации обязаны сохранять. | Python, SQL, JSON, современные процессоры и базы данных не являются Canon. |
| **Abstract Contract** | Версионированное проверяемое обязательство, независимое от одного implementation profile. | Документация сама по себе не является implementation или evidence. |
| **Implementation Profile** | Конкретная реализация принятых контрактов; сейчас PostgreSQL и SQLite profiles. | Profile может добавлять operational limits, но не должен переопределять semantic meaning. |
| **Authoritative history** | Принятая упорядоченная Event sequence для одного Kernel instance. | Один instance не должен случайно менять authoritative store от запроса к запросу. |
| **Replay** | Детерминированное восстановление из authoritative Events. | Успех replay не доказывает истину источника, полное deletion или production safety. |
| **Projection** | Перестраиваемое производное представление: tables, indexes, search или graph structures. | Projection disposable и не должна незаметно становиться truth authority. |
| **Receipt** | Ограниченная аудируемая запись inputs, decisions, inclusions, exclusions, limits и evidence references. | Receipt объясняет bounded operation, но не является сертификатом окончательной истины. |
| **Provenance** | Записанные ссылки на source, actor, authority, time и transformations. | Provenance может быть неполным или ложным без независимой проверки. |
| **Canonical bytes** | Точное byte-представление по объявленному canonicalization contract. | Canonicalization даёт детерминированное сравнение, но не предотвращает injection и не доказывает authenticity. |
| **Golden vector** | Фиксированный input с ожидаемым byte/digest/identity output для воспроизведения другой реализацией. | Golden vectors проверяют объявленные случаи, а не все inputs и не любое будущее hardware. |
| **Evidence bundle** | Сохранённые в репозитории artifacts, manifests и hashes, привязанные к точным runs и commits. | Хранение не расширяет evidence за пределы producing checkpoint и не создаёт independent custody. |

## Governance и maturity

| Термин | Краткое определение | Важная граница |
|---|---|---|
| **Decision status** | Состояние предложения: `PROPOSED`, `ACCEPTED`, rejected или другое governance-состояние. | Acceptance — операторское решение, а не доказательство implementation. |
| **Implementation status** | Наличие кода в объявленном scope на точном SHA. | Implemented не означает автоматически tested, wired, enabled или observed. |
| **Evidence level** | Ограниченная стадия reproduction/evaluation: C2, C3, C4 или C5. | Более высокий label не отменяет explicit unsupported assertions. |
| **C3** | Cross-profile comparison по byte, structural, semantic и behavioural classes. | C3 не означает operational equivalence или доказанную произвольную substrate neutrality. |
| **C4** | Offline shadow evaluation на ограниченной recorded workload. | C4 не является live production shadowing или authority promotion. |
| **C5** | Bounded synthetic operational rehearsal по объявленному plan и matrix. | C5 не является production readiness, live traffic, compliance или multi-region reliability. |
| **Track H** | Историческое восстановление заявленного `v0.1.2.1` и оригинального test suite. | Clean implementation не выдаётся за восстановленный historical source. |
| **Track C** | Clean implementation lineage текущих contracts и profiles. | Track C не разрешает authenticity Track H. |
| **Track R** | Long-horizon research proposals. | Research text не является Canon, accepted decision или runtime authorization. |
| **Operator approval** | Явное разрешение maintainer на решение или promotion. | Согласие AI, review comments и passing tests не заменяют operator authority. |

## Неэквивалентности, которые нужно сохранять

```text
Claim               ≠ truth
Event               ≠ reality
Identity            ≠ authenticity
Lineage             ≠ personhood
Unknown             ≠ false
Superseded          ≠ erased
Projection          ≠ authority
Receipt             ≠ truth certificate
Canonicalization    ≠ security validation
Repository evidence ≠ independent custody
C3                  ≠ operational equivalence
C4                  ≠ live production shadow
C5                  ≠ production readiness
Public repository   ≠ open-source license
Research proposal   ≠ accepted contract
Accepted ADR        ≠ implemented runtime
```
