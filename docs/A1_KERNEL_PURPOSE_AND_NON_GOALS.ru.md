# 🎯 A1 — Purpose и Non-goals Kernel

**[English](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) · [Русский](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md)**

> **Deliverable:** `A1` плана [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.ru.md) (`ADR-0025`, [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88))
> **Граница evidence:** только архитектурное исследование и определение; без изменения runtime, contracts, evidence, assertion map, NK-EPI, maturity или production
> **Review status:** первый drafted slice; ожидает independent review и integrated blueprint review вместе с A2–A10

## 1. Что это за документ

Этот документ отвечает на критерий завершения `A1`, установленный планом Architecture Re-foundation:

> Читатель отличает архитектуру от продукта, базы данных, framework, cognitive system и storage engine без обращения к текущему коду.

Документ определяет проблему, которую изучает Native Kernel, что означает слово `Kernel` в этом проекте, какие долговечные свойства обязана сохранять реализация Kernel, что явно находится вне Kernel, и границу с Titan, Crystal, Mentaury, операционными системами, базами данных и model runtimes.

Документ не определяет онтологию (`A2`), абстрактную машину (`A3`), семантические законы (`A4`) или любой последующий deliverable. Там, где здесь используется термин, который позднее будет определён точнее, он используется неформально и помечен как предварительный.

## 2. Проблема, которую изучает Native Kernel

Системы хранения знаний обычно начинаются с доступной machinery, а не с явно поставленного вопроса:

```text
доступна relational database → memory становится tables и rows
доступен graph engine        → knowledge становится vertices и edges
доступен vector index        → meaning становится numerical proximity
доступен LLM API             → reasoning становится тем, что вернёт этот provider
```

Каждый выбор может быть полезен. Проблема в том, что временная структура выбранной технологии молча становится постоянным определением того, чем *является* claim, факт, memory, identity или truth. Когда технология меняется, система вынуждена переписать не только storage и execution, но и понимание того, что означала сохранённая информация.

Native Kernel существует, чтобы изучать другой, явный вопрос:

> **Что должно оставаться верным в представлении claim, его evidence, истории изменений и связанной с ним confidence, чтобы тот же смысл пережил смену storage, языка, процессора или вычислительной парадигмы?**

Это исследовательский вопрос о представлении и инвариантах, а не обязательство создать выпущенный продукт, database engine или AI-систему.

## 3. Что означает `Kernel` в этом проекте

Внутри Native Kernel `Kernel` обозначает:

```text
минимальный, технологически нейтральный набор semantic obligations,
которому должна удовлетворять любая конкретная реализация
claim/knowledge management, чтобы называться conforming
Native Kernel implementation, вместе с абстрактной машиной
и законами, делающими эти obligations проверяемыми.
```

Kernel в этом смысле ближе к абстрактной instruction set architecture для meaning, чем к исполняемому артефакту. Это контракт, которому многие разные, взаимно несовместимые реализации могут удовлетворять по-своему, оставаясь сравнимыми через заявленное equivalence.

Kernel не является:

- одной конкретной запущенной программой;
- конкретным file format, schema или wire protocol;
- library, SDK или framework, поставляемым как исходный код;
- Python/PostgreSQL/SQLite reference laboratory, находящейся сейчас в этом репозитории.

Reference laboratory (`P1`–`C5`) — это одна попытка, частичное, ограниченное выражение гипотетических Kernel obligations. Это evidence о том, реализуемы ли и проверяемы ли эти obligations. Это не сам Kernel, и его текущая форма не должна задним числом определять Kernel только потому, что была написана первой. `A9` подробно классифицирует каждый модуль laboratory относительно этой границы.

## 4. Долговечные свойства, которые обязан сохранять Kernel

Ниже — текущий, версионированный, пересматриваемый candidate-список того, что обязана сохранять conforming реализация независимо от substrate. `A4` сформулирует их как нумерованные семантические законы с counterexamples и failure modes; этот раздел только называет их и объясняет, почему каждое является candidate.

| Свойство | Почему это candidate obligation |
|---|---|
| **Semantic identity** | Claim не должен становиться другим claim только потому, что переместилась его storage row, file location или process |
| **Explicit change** | Revision, supersession, restriction и erasure должны оставаться видимыми операциями, а не молчаливым overwrite |
| **Provenance** | Откуда взялся claim и как он был трансформирован, должно оставаться прикреплённым к claim, а не выводиться постфактум |
| **Lineage** | Связанные версии и derivations claim должны оставаться прослеживаемыми друг к другу |
| **Temporal meaning** | Время, когда нечто было верно, время observation и время record должны оставаться различимыми, а не сливаться в один timestamp |
| **Epistemic state** | Supported, inferred, contested, unknown и rejected claims должны оставаться различимыми между собой и от truth |
| **Conflict visibility** | Противоречие должно оставаться видимым, пока явный процесс его не разрешит; оно не должно молча усредняться, отбрасываться или перезаписываться |
| **Reconstructability** | Disposable derived state должен быть воспроизводим из сохранённого authoritative material по заявленному правилу equivalence |
| **Bounded accountability** | Selection, omission, transformation или отказ должны быть объяснимы через bounded record, без claim, что этот record доказывает полноту или truth |
| **Declared equivalence under substrate change** | Переход на другой storage, язык или процессор должен сохранять именованный, протестированный уровень semantic equivalence, а не предполагаемый |

Это гипотезы под активным исследованием, а не устоявшаяся математика. Каждая остаётся открытой для пересмотра, замены или отклонения через явное architecture decision, и `A10` будет отслеживать falsification condition для каждой из них.

## 5. Что находится вне Kernel

Kernel не определяет и не должен определяться:

- конкретной database, file format, serialization или wire protocol;
- конкретным programming language, runtime или processor architecture;
- конкретным retrieval algorithm, ranking function или embedding model;
- конкретным LLM, prompting strategy или agent orchestration pattern;
- application-level функциями, такими как user interfaces, notifications или workflow automation;
- performance targets, throughput numbers или latency budgets;
- deployment topology, multi-tenancy или operational infrastructure;
- legal, licensing или compliance certification;
- production-readiness, security hardening или incident response процессами.

Это законные заботы implementation profile, deployment или продукта, построенного поверх conforming Kernel. Это не свойства, которые сама Kernel-архитектура утверждает, требует или запрещает на уровне Canon.

## 6. Граница с Titan, Crystal и Mentaury

Native Kernel — одно из нескольких независимых research- и product-направлений Velantrim. `docs/VELANTRIM_ECOSYSTEM.md` подробно определяет карту межпроектных отношений; этот раздел повторяет только ту часть, которая относится к определению самого Kernel.

```text
🧬 Native Kernel   — substrate-neutral архитектура для claims, evidence, provenance,
                     времени, конфликта, revision и bounded explanation
🔱 Titan           — cognition, orchestration, retrieval, инструменты и агенты
💎 Crystal         — verifiable memory, evidence, trust и audit продукт
⭐️ Mentaury Soul   — цифровая индивидуальность, identity continuity, отношения,
                     commitments и управляемое развитие
```

- Native Kernel не является скрытым storage layer, memory backend или truth authority для Titan, Crystal или Mentaury.
- Titan может оценивать идеи Kernel как источник workload или через ограниченный, проверенный адаптер. Такая оценка не делает runtime Titan runtime-ом Kernel и не делает evidence Kernel evidence-ом Titan.
- Crystal продолжает определять и развивать собственный Canon, evidence model и grant-facing продукт независимо от того, существует ли Native Kernel или меняется ли он.
- Kernel claim, event, projection или Receipt не становится Mentaury identity, relationship, commitment или continuity record только потому, что существует. Identity continuity — собственная исследовательская проблема Mentaury, а не export Kernel.
- Ни одна capability, credential, consent или authority не наследуется между этими проектами неявно. Любая будущая интеграция требует собственного ограниченного ADR/RFC, явного контракта equivalence, тестов, threat/privacy review и отдельного одобрения оператора — именно так, как уже требует `VELANTRIM_ECOSYSTEM.md`.

## 7. Граница с операционными системами, базами данных и model runtimes

- **Операционная система.** Kernel не управляет процессами, scheduling, memory allocation, device drivers или файловой системой. Операционная система может размещать implementation profile; сама по себе она не является заботой Kernel.
- **База данных.** База данных (relational, document, graph, key-value или vector) может служить durable store для authoritative history или derived projections одного implementation profile. Kernel не требует конкретной database, не предполагает SQL и не рассматривает transaction- или consistency-модель какой-либо database как требование Canon, а не как деталь реализации, подлежащую явному отображению (`A8`).
- **Model runtime.** LLM, embedding model или другой machine-learning runtime может использоваться implementation profile для интерпретации, суммирования, предложения или ранжирования candidate-информации. Kernel не требует существования model runtime, не рассматривает output модели как admitted knowledge по умолчанию и не делегирует epistemic classification (claim, evidence, conflict, uncertainty) confidence score модели. `docs/WORLD_AND_EPISTEMIC_BOUNDARIES.md` уже фиксирует конкретные failure modes epistemic boundary, которые это исключает; этот раздел лишь формулирует architectural boundary, которая их мотивирует.
- **Knowledge graph, search index или memory framework.** Любой из них может реализовать одну projection или access path поверх Kernel-conformant history. Ни один из них не является самим Kernel, и ни один не может молча стать authoritative source of truth вместо retained history, из которой он выведен.

## 8. Non-goals этого документа и Kernel на данном этапе

Этот документ не:

- определяет онтологию primitives знания и памяти (`A2`);
- определяет states и transitions абстрактной машины Kernel (`A3`);
- формулирует семантические законы с counterexamples и failure modes (`A4`);
- определяет identity, time или change формально (`A5`);
- определяет lifecycle знания (`A6`);
- определяет семантику conflict, uncertainty или revision (`A7`);
- определяет substrate-independence contract (`A8`);
- классифицирует существующую reference laboratory модуль за модулем (`A9`);
- перечисляет открытые вопросы и falsification criteria (`A10`);
- авторизует, возобновляет или проектирует новый runtime, версию reducer, database profile или ecosystem integration;
- меняет assertion map, support state `NK-EPI`, maturity `C4`/`C5` или production authorization;
- решает `Issue #18` (license/publication) или `ADR-0024` (reducer referential semantics);
- утверждает, что долговечные свойства из раздела 4 доказаны — только то, что они являются текущими candidate obligations под активным исследованием.

Kernel на этом этапе blueprint — это поставленная проблема, рабочее определение термина, candidate-список долговечных свойств и явный набор границ. Это ещё не абстрактная машина, не набор законов и не implementation requirement.

## 9. Связь с существующими документами

- [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md) описывает ту же мотивацию в форме essay и остаётся валидным background reading; этот документ — версионированный, отслеживаемый blueprint deliverable, который план Architecture Re-foundation требует под точным именем `A1_KERNEL_PURPOSE_AND_NON_GOALS`.
- [`ARCHITECTURE_REFOUNDATION.md`](./ARCHITECTURE_REFOUNDATION.md) определяет последовательность из десяти deliverables и completion gate, которому должен удовлетворять этот документ для `A1`.
- [`VELANTRIM_ECOSYSTEM.md`](./VELANTRIM_ECOSYSTEM.md) определяет полный межпроектный integration-boundary контракт, упомянутый в разделе 6.
- [`WORLD_AND_EPISTEMIC_BOUNDARIES.md`](./WORLD_AND_EPISTEMIC_BOUNDARIES.md) определяет failure modes epistemic boundary, упомянутые в разделе 7.
- [`../ARCHITECTURE.md`](../ARCHITECTURE.md) описывает текущую форму Canon, произведённую reference laboratory; раздел 3 этого документа объясняет, почему эта форма — evidence, а не определение Kernel.

## 10. Открытые вопросы, переносимые дальше

Следующие вопросы отмечены здесь, потому что возникли при написании `A1`, но принадлежат последующим deliverables и не отвечаются здесь:

- Какие из свойств раздела 4 действительно substrate-independent obligations, а какие — артефакты практики event sourcing? (`A4`, `A8`)
- Может ли "bounded accountability" быть удовлетворена вообще без durable log? (`A6`, `A8`)
- Нужен ли границе Titan/Crystal/Mentaury из раздела 6 отдельный контракт для каждого проекта или один общий межпроектный контракт? (будущий ecosystem RFC, вне этого blueprint)

## 11. Non-claims

```text
этот документ ≠ онтология, абстрактная машина или семантические законы
названное в разделе 4 свойство ≠ доказательство, что оно достижимо
этот документ ≠ разрешение возобновить runtime, reducer или profile work
этот документ ≠ решение по Issue #18 или ADR-0024
этот документ ≠ evidence, что какой-либо будущий substrate уже соответствует
```

## 12. Статус

```text
deliverable: A1_KERNEL_PURPOSE_AND_NON_GOALS
state: DRAFTED
review: PENDING independent review и integrated blueprint review вместе с A2-A10
next_content_slice: A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY
runtime, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
```
