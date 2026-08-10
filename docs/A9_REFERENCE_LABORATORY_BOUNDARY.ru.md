# A9 — Граница референсной лаборатории

**Состояние:** `DRAFTED / PROVISIONAL`  
**Идентификатор модели:** `nk-reference-laboratory-boundary/A9-draft-1`  
**Архитектурная фаза:** ADR-0025 / Issue #88  
**Предыдущий блок:** `A8_SUBSTRATE_INDEPENDENCE_CONTRACT`  
**Следующий содержательный блок:** `A10_OPEN_QUESTIONS_AND_FALSIFICATION`  
**Расширение runtime:** `FROZEN`

## 1. Назначение

A9 классифицирует существующую чистую линию реализации P1–C5 относительно A1–A8, не позволяя реализации захватить архитектуру.

Текущие механизмы Python, PostgreSQL, SQLite, Event, reducer, Receipt, CI и evidence сохраняются как ограниченная референсная лаборатория. Для каждого механизма A9 спрашивает:

1. какое архитектурное обязательство он действительно упражняет;
2. что он демонстрирует только для объявленного профиля и scope;
3. что остаётся частичным или неподдержанным;
4. что является лишь профильной реализацией;
5. что может служить инструментом фальсификации или регрессии;
6. что **не должно** автоматически становиться универсальным требованием Native Kernel.

A9 не удаляет, не переписывает, не ослабляет и не отменяет принятые implementation-contracts. Он классифицирует их архитектурную роль.

```text
существующий механизм
≠ архитектурное требование

полезное evidence
≠ доказательство универсальной переносимости

профильная реализация
≠ архитектурный дефект
```

## 2. Граница authority и evidence

Этот документ относится к архитектурному исследованию/governance. Он не:

- изменяет семантику `native_kernel/**`;
- изменяет принятые contracts или bytes evidence;
- разрешает reducer-v2, новые Event verbs, NK-EPI runtime, Temporal runtime, Admission lifecycle, расширение deletion execution, новые БД, языковые профили, model adapters, network/cloud wiring или production promotion;
- принимает ADR-0003;
- решает Issue #74 / ADR-0024;
- решает Issue #18 по лицензии/публикации;
- допускает operator-controlled источники Track H;
- меняет assertion arithmetic `45/10/17/0` или NK-EPI `0/0/8/0`;
- объявляет P1–C5 независимой implementation lineage в сильном cross-language/cross-hardware смысле;
- объявляет PostgreSQL и SQLite операционно эквивалентными.

## 3. Словарь классификации

A9 использует шесть ролей. Они классифицируют лабораторный механизм относительно A1–A8; это не состояния assertion map и не замена preservation states A8.

### `ARCHITECTURE_PRESERVING_EVIDENCE`

Механизм даёт ограниченное evidence того, что одно или несколько архитектурных обязательств могут быть реализованы без скрытой потери их смысла.

Эта метка никогда не означает, что сам механизм обязателен архитектурой.

### `PROFILE_SPECIFIC_REALIZATION`

Конкретный implementation choice, допустимый для своего профиля, но заменяемый в другой conforming realization.

### `PARTIAL_ARCHITECTURE_COVERAGE`

Механизм упражняет только часть архитектурного обязательства, оставляя существенные различия, состояния, threat cases, environments или authority-вопросы неподдержанными.

### `FALSIFICATION_INSTRUMENT`

Механизм/test/evidence способен обнаружить противоречие, скрытый semantic collapse, replay divergence, identity drift, потерю provenance, ошибку ordering или overclaim. Успешное прохождение полезно, но не доказывает всю архитектуру.

### `LABORATORY_ONLY_CONSTRAINT`

Требование обязательно для текущей versioned laboratory lineage или воспроизводимости её evidence, но не установлено как substrate-neutral Canon.

### `NOT_ARCHITECTURE_EVIDENCE`

Механизм может быть операционно полезен, однако одно его существование не поддерживает архитектурный conformance claim.

## 4. Правило классификации

Один механизм может иметь несколько ролей. Классификация всегда привязана к рассматриваемому архитектурному обязательству.

Пример:

```text
проверка SHA-256 Event chain
= ARCHITECTURE_PRESERVING_EVIDENCE
  для обнаружения изменения записанной истории в этой лаборатории

И
= PROFILE_SPECIFIC_REALIZATION
  потому что SHA-256 и сериализованная hash chain не являются универсальным Canon

И
= FALSIFICATION_INSTRUMENT
  потому что разрыв цепочки обнаруживает integrity divergence
```

Поэтому A9 отвергает одномерные формулы вроде «Event sourcing и есть архитектура» или «SQL не имеет значения». Правильный вопрос: какое смысловое обязательство реализуется, в каком scope и с какими ограничениями.

## 5. P1 — Semantic core

Текущий P1 содержит canonical identity helpers, Claim/domain objects, authority policy, deterministic in-memory reducer behavior, deletion/restriction transitions и bounded Receipts.

### Architecture-preserving evidence

P1 даёт ограниченное implementation evidence для:

- явной semantic identity вместо backend-row identity;
- отделения authority decisions от самого факта наличия данных;
- явных transition outcomes вместо silent mutation;
- явных restriction/deletion semantic states;
- Receipt overclaim guards;
- deterministic behavior в объявленном implementation contract.

Это согласуется с A1 purpose/non-goals, A2 semantic distinctions, A3 transition/accountability obligations, A4 laws, A5 scoped identity и частью A6 lifecycle/disposition.

### Profile-specific realization

Не становятся универсальными требованиями только потому, что их использует P1:

- Python objects/classes;
- Python 3.11–3.12;
- текущие canonical JSON/byte encodings;
- digest prefixes и provisional digests;
- одна reducer function;
- текущие enum/state representations.

### Partial coverage

P1 не устанавливает durable provenance, independent storage, cross-profile equivalence, physical deletion, полную temporal semantics, A7 conflict/uncertainty states или NK-EPI support.

## 6. P2 — PostgreSQL append/idempotency profile

P2 добавляет PostgreSQL persistence, writer lease/epoch fencing, append/idempotency behavior, sequence allocation, payload commitment и hash-chain history.

### Architecture-preserving evidence

P2 полезен как evidence того, что лаборатория способна сохранять:

- явную recorded-change lineage;
- idempotent command handling в указанном scope;
- различимость retry и конфликтующего повторного использования ключа;
- writer authority/fencing boundaries;
- ordered recorded history внутри лабораторного профиля;
- обнаруживаемые history-integrity violations внутри выбранной commitment scheme.

### Profile-specific realization

Заменяемыми механизмами остаются:

- PostgreSQL;
- SQL tables, row locks и transaction primitives;
- Psycopg;
- one-owner epoch lease representation;
- global/stream integer sequences;
- numbered SQL migrations;
- SHA-256 migration ledger;
- `nkp1` / `nke1` byte commitments;
- canonical Event-envelope bytes.

Будущий conforming profile может сохранить identity, causal/lineage relations, idempotency, authority и accountability другими физическими средствами.

### Laboratory-only constraints

Exact sequence allocation, текущий Event envelope и DB transactional behavior остаются обязательными для воспроизводимости P2–C5 evidence. Они не становятся автоматически требованиями A1–A8.

## 7. P3 — Replay, projections и Receipts

P3 добавляет deterministic upcasting, replay, projection rebuild, publication guards и persisted replay/rebuild Receipts.

### Architecture-preserving evidence

P3 даёт ограниченное evidence для:

- history-visible state reconstruction;
- явной lineage от recorded history к derived state;
- disposability/rebuildability derived state в текущем профиле;
- отклонения stale publication относительно объявленного history head;
- accountable reconstruction через bounded Receipts;
- отделения authoritative recorded history от disposable projections.

Это сильные лабораторные реализации A3 reconstruction/accountability, A4 history/view laws, A5 lineage и A6 revision/history obligations.

### Profile-specific realization

A1–A8 не требуют:

- Event replay from byte zero как единственного способа reconstruction;
- SQL projection tables;
- одной структуры upcaster registry;
- monotonic projection-generation integers;
- PostgreSQL `REPEATABLE READ`;
- exact Receipt JSON/bytes.

Не-event-sourced система может conform, если сохраняет необходимые history, lineage, accountability и reconstruction-equivalent obligations и честно объявляет потери.

## 8. P4 — Assertion-scoped conformance evidence

P4 формирует полный набор из 72 assertion results и traceability для PostgreSQL profile.

### Architecture-preserving evidence

P4 прежде всего является **measurement and falsification instrument**. Он демонстрирует дисциплину:

- перечислять supported, partial и unsupported claims;
- связывать support claim с checks и environment metadata;
- не допускать silent promotion неподдержанных assertions;
- отличать repository reproduction от более сильных conformance levels.

Это поддерживает A4 anti-overclaim laws и A8 explicit degradation/accountability.

### Boundary

Assertion registry P4 сам по себе не является architecture ontology. A1–A8 остаются смысловым authority blueprint. Существующие assertion IDs продолжают описывать laboratory evidence surface и не переписываются ретроактивно через A9.

## 9. P5 — SQLite profile и C3 comparison

P5 добавляет независимо реализованный SQLite storage profile внутри той же Python lineage, history import и cross-profile comparator.

### Architecture-preserving evidence

P5/C3 важен, потому что показывает сохранение части semantic/behavioral obligations при смене storage profile:

- PostgreSQL и SQLite дают equivalent declared semantic outcomes в поддерживаемых comparison scenarios;
- SQL dialect, schema layout, locking strategy и server topology могут различаться при сохранении выбранных meaning-level results;
- profile-local identifiers/timestamps могут различаться без обязательного нарушения semantic equivalence;
- cross-profile comparison обнаруживает semantic drift.

Это реальное architecture-preserving evidence для **replaceable storage-profile realization в узкой общей language lineage**.

### Критическое ограничение

P5 не устанавливает сильную substrate independence, потому что PostgreSQL и SQLite разделяют существенные assumptions:

- Python language/runtime;
- conventional digital memory и CPU execution;
- общий semantic-core/reducer model;
- текущую Event vocabulary и canonical encodings;
- связанные test harnesses и repository custody.

Следовательно:

```text
PostgreSQL ↔ SQLite C3
= полезное cross-profile evidence
≠ independent-language equivalence
≠ independent-computation-model equivalence
≠ arbitrary-substrate portability proof
```

### A9 reinterpretation exact-byte equivalence

P5 использует BYTE/STRUCTURAL/SEMANTIC/BEHAVIOURAL comparison classes. Exact bytes остаются валидным требованием там, где они явно нужны versioned laboratory contract, особенно при verification импортированной authoritative history.

A9 не обобщает это на все substrates. На уровне архитектуры управляет A8: разные bytes могут сохранять смысл, а одинаковые bytes сами по себе не доказывают semantic equivalence.

## 10. C4 — Offline shadow evaluation

C4 проверяет уже поддерживаемую C3 assertion surface на approved synthetic offline workload без authoritative writes и side effects.

### Architecture-preserving role

C4 преимущественно **falsification and bounded behavioral-evidence instrument**. Он способен обнаружить:

- divergence при scenario execution;
- accidental authority promotion;
- hidden side effects;
- inconsistencies evidence/reporting;
- regression supported assertions.

### Boundary

C4 не является live production shadowing, external authority, доказательством правильности решений, privacy/compliance evidence или архитектурным требованием иметь «shadow evaluator» на каждом будущем substrate.

## 11. C5 — Bounded operational rehearsal

C5 запускает synthetic ephemeral scenarios категорий security, privacy, recovery, rollback, incident, reliability и resilience и сохраняет repository-resident evidence bundles.

### Architecture-preserving role

C5 даёт bounded evidence сохранения заявленного поведения и evidence boundaries в контролируемых operational scenarios. Durable evidence bundles полезны для reproducibility и последующей falsification.

### Boundary

C5 не устанавливает:

- production readiness;
- live-user-data safety;
- cloud/IAM correctness;
- high availability;
- physical deletion;
- compliance;
- ecosystem authority;
- independent custody;
- universal runtime или substrate conformance.

Synthetic operational rehearsal — это **laboratory evidence**, а не architecture authority.

## 12. Матрица классификации механизмов

| Laboratory mechanism | A1–A8 obligation exercised | A9 role | Architectural requirement? |
|---|---|---|---|
| Explicit Claim/semantic identity | scoped identity and semantic distinction | `ARCHITECTURE_PRESERVING_EVIDENCE` + `PARTIAL_ARCHITECTURE_COVERAGE` | смысловое обязательство да; текущий encoding ID нет |
| Python domain objects | representation ontology/transition concepts | `PROFILE_SPECIFIC_REALIZATION` | нет |
| Current Event vocabulary | explicit change/history в P1–C5 | `LABORATORY_ONLY_CONSTRAINT` + `PROFILE_SPECIFIC_REALIZATION` | exact verbs/envelope нет |
| Deterministic reducer v1 | reproducible declared transition result | `ARCHITECTURE_PRESERVING_EVIDENCE` + `LABORATORY_ONLY_CONSTRAINT` | exact reducer нет |
| PostgreSQL append store | durable recorded history / authority fencing | `PROFILE_SPECIFIC_REALIZATION` | нет |
| SQLite embedded store | alternate storage realization | `PROFILE_SPECIFIC_REALIZATION` | нет |
| PostgreSQL↔SQLite comparator | semantic drift detection | `FALSIFICATION_INSTRUMENT` + `ARCHITECTURE_PRESERVING_EVIDENCE` | реализация comparator нет |
| Hash chain | bounded recorded-history integrity detection | `PROFILE_SPECIFIC_REALIZATION` + `FALSIFICATION_INSTRUMENT` | SHA/hash chain нет |
| Global/stream sequence | deterministic laboratory ordering | `LABORATORY_ONLY_CONSTRAINT` | global integer order нет |
| Replay from Events | laboratory reconstruction/lineage | `ARCHITECTURE_PRESERVING_EVIDENCE` + `PROFILE_SPECIFIC_REALIZATION` | именно Event replay нет |
| Rebuildable projections | authoritative/derived state separation | `ARCHITECTURE_PRESERVING_EVIDENCE` | смысловая separation да; SQL mechanism нет |
| Receipts | bounded accountability | `ARCHITECTURE_PRESERVING_EVIDENCE` | accountability да; encoding Receipt нет |
| P4 assertion reports | explicit support/degradation accounting | `FALSIFICATION_INSTRUMENT` | exact schema нет |
| C4 shadow workload | side-effect/authority/regression probing | `FALSIFICATION_INSTRUMENT` | нет |
| C5 rehearsal | controlled operational falsification/evidence | `FALSIFICATION_INSTRUMENT` + `PARTIAL_ARCHITECTURE_COVERAGE` | нет |
| GitHub Actions matrices | reproducibility в declared environments | `FALSIFICATION_INSTRUMENT` | нет |
| Repository evidence ZIPs | preservation exact historical evidence bytes | `LABORATORY_ONLY_CONSTRAINT` | нет |

## 13. Coverage summary A1–A8

### A1 — purpose and non-goals

Лаборатория показывает реализуемость meaning/provenance/history-oriented kernel на текущих технологиях. Она не доказывает hardware/computational-substrate neutrality.

### A2 — ontology

Часть A2 concepts имеет текущие representations, но laboratory object models не покрывают полную ontology A2 и могут не представлять различия, которые не требовались текущими runtime contracts. Отсутствие поля в runtime не доказывает ненужность concept.

### A3 — abstract machine

P1–P5 упражняют многие transition/accountability patterns, но command/Event/reducer structure — лишь одна mapping. Transition families A3 не обязаны соответствовать Event verbs один-к-одному.

### A4 — semantic laws

Лаборатория содержит полезные anti-overclaim, identity, history, provenance и derived-view guards. Она не исполняет все 28 A4 laws на независимых substrates.

### A5 — identity, time and change

Canonical IDs, sequences и timestamps дают partial mappings. Лаборатория не реализует все typed identity relations и temporal dimensions A5. Write order нельзя использовать как замену occurrence/causal/semantic precedence.

### A6 — lifecycle

Admission, supersession, restriction, erasure и accounting mechanisms упражняют часть lifecycle positions. Они не являются полной runtime state machine A6 и не должны автоматически становиться ею: A6 — meaning-level model.

### A7 — conflict, uncertainty and revision

Current runtime имеет лишь partial conflict/revision representation и не реализует полную taxonomy tension/assessment/resolution или typed uncertainty model A7. Отсутствующий support должен оставаться явным и не выводиться из generic contradiction links/reducer behavior.

### A8 — substrate independence

P5 даёт ограниченное storage-profile evidence. Лаборатория не устанавливает полную A8 conformance для independent languages, hardware, memory models, analog/neuromorphic systems, quantum systems или неизвестных будущих substrates.

## 14. Failure и overclaim cases

Следующие трактовки не conform A9:

1. «PostgreSQL primary, значит SQL — Canon».
2. «SQLite совпал с PostgreSQL, значит substrate independence доказана».
3. «Exact Event bytes совпали, значит semantic equivalence доказана».
4. «Event bytes различаются, значит semantic equivalence невозможна».
5. «Reducer reconstructs state, значит каждому будущему substrate нужен reducer».
6. «Event log сохраняет history, значит каждый future substrate обязан быть event-sourced».
7. «C5 проходит synthetic security scenarios, значит production security установлена».
8. «Concept не имеет P1–C5 field, значит он не относится к architecture».
9. «Механизм profile-specific, значит его следует удалить».
10. «Operator approval P1–C5 является independent evidence архитектурной истины».
11. «Repository-resident evidence — это independent custody».
12. «Current assertion arithmetic оценивает blueprint A1–A8 целиком».

## 15. Правило сохранения существующей лаборатории

A9 не требует удалять код только потому, что mechanism profile-specific.

```text
profile-specific
→ правильно обозначить
→ сохранить reproducibility
→ сохранить evidence lineage
→ не допустить silent Canon promotion
≠ автоматически удалить или переписать
```

Принятые laboratory contracts продолжают быть binding в своём versioned scope, пока отдельно не изменены через decision process.

## 16. Связь с pending decisions

- Issue #18 остаётся operator-controlled; A9 не выбирает license/publication.
- Issue #74 / ADR-0024 остаётся `PROPOSED / PENDING_OPERATOR`; reducer v1 immutable, reducer-v2 unauthorized.
- ADR-0003 остаётся `PROPOSED / NOT_STARTED`.
- Track H source admission остаётся operator-controlled.
- Issues #14/#15/#16/#17 сохраняют текущий implementation/evidence scope.

A9 classification не предрешает ни одно из этих решений.

## 17. Open questions, отложенные до A10

A9 выявляет, но не решает:

- минимальный не-event-sourced equivalent explicit change history;
- minimum accountability, если exact replay невозможен;
- требуемую степень lineage continuity на lossy/probabilistic substrates;
- достаточно ли independent-language implementation для более сильной substrate-independence evidence;
- что в analog/neuromorphic realization считается persistent identity/history equivalent;
- как доказать forgetting, если substrate не показывает exact retained bytes;
- как falsify conformance при inherently probabilistic observations;
- нужно ли часть текущих accepted contracts позже переклассифицировать из architecture contracts в profile contracts.

Это область `A10_OPEN_QUESTIONS_AND_FALSIFICATION` и integrated A1–A10 review.

## 18. First-draft completion test

Bounded drafting A9 завершён, если reviewer может взять mechanism P1–C5 и определить:

1. какое obligation A1–A8 он упражняет;
2. является ли он architecture-preserving evidence, profile-specific, partial, falsification instrument, laboratory-only constraint или not architecture evidence;
3. что current evidence действительно демонстрирует;
4. чего оно **не** демонстрирует;
5. обязательно ли замена mechanism изменит смысл Native Kernel.

Для основных P1–C5 mechanisms, перечисленных выше, этот тест выполнен.

Final acceptance остаётся pending: independent review, A10, integrated A1–A10 reconciliation и отдельное operator decision до любого runtime thaw.
