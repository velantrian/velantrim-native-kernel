# A10 — Open Questions and Falsification

**State:** `DRAFTED / PROVISIONAL`  
**Model identity:** `nk-open-questions-falsification/A10-draft-1`  
**Architecture phase:** ADR-0025 / Issue #88  
**Previous slice:** `A9_REFERENCE_LABORATORY_BOUNDARY`  
**Next gate:** `INTEGRATED_A1_A10_REVIEW`  
**Runtime expansion:** `FROZEN`

## 1. Назначение

A10 завершает первый drafting-pass Architecture Re-foundation A1–A10: явно фиксирует неопределённости и определяет, каким evidence можно ослабить или опровергнуть важные гипотезы Native Kernel.

A10 — не каталог обещаний. Это **граница falsification**.

```text
architectural hypothesis
+ declared scope
+ observable obligation
+ counterexample / falsifier
+ evidence quality
→ SUPPORTED_FOR_SCOPE | WEAKENED | REFUTED | INDETERMINATE | NOT_TESTED
```

A10 не превращает blueprint в Canon. A1–A10 остаются `DRAFTED / PROVISIONAL` до integrated review и отдельного operator decision.

## 2. Граница evidence и Authority

A10 не:

- изменяет `native_kernel/**`, contracts, profiles, fixtures, evidence bytes или runtime behavior;
- разрешает reducer-v2, новые Event verbs, NK-EPI runtime, Temporal runtime, full Admission, расширение deletion execution, новые databases, language ports, model adapters, cloud/network wiring, maturity promotion или production authorization;
- решает Issue #18 license/publication;
- решает Issue #74 / ADR-0024;
- принимает ADR-0003;
- допускает operator-controlled Track H sources;
- меняет assertion arithmetic `45/10/17/0` или NK-EPI `0/0/8/0`;
- утверждает compatibility с arbitrary future substrates;
- трактует отсутствие falsifier как доказательство истины.

## 3. Словарь falsification

### `SUPPORTED_FOR_SCOPE`
Явный test или body of evidence выдержал конкретную попытку falsification в названном scope. Это bounded support, а не universal proof.

### `WEAKENED`
Evidence показывает, что гипотезе нужен более узкий scope, более сильные preconditions или исправленная терминология, но полного refutation ещё нет.

### `REFUTED`
Воспроизводимый counterexample нарушает обязательное semantic obligation внутри scope, где гипотеза заявляла сохранение.

### `INDETERMINATE`
Доступные observations не позволяют надёжно различить preservation и failure с достаточной confidence/Authority.

### `NOT_TESTED`
Нет qualifying falsification attempt. `NOT_TESTED ≠ SUPPORTED`.

Это A10 research outcomes; они не заменяют P4 assertion-map states или A8 preservation/conformance states.

## 4. Квалификация falsification test

Meaningful falsification record должен указывать:

1. **Hypothesis** — что может оказаться ложным.
2. **Scope** — где claim должен работать.
3. **Preserved obligation** — какая distinction/law/transition/lineage property из A1–A9 важна.
4. **Observable** — что реально можно наблюдать.
5. **Counterexample condition** — какое observation должно ослабить/refute claim.
6. **Authority и provenance** — кто/что получил observation и каким методом.
7. **Independence class** — same implementation lineage, independent language, independent team, independent custody, independent computation model или иной явно названный класс.
8. **Loss declaration** — что нельзя наблюдать или reconstruct.
9. **Outcome** — один A10 outcome с rationale.
10. **Reproduction path** — достаточно сведений для повторения попытки, где это возможно.

Test, который может только «пройти» и не имеет declared counterexample, не является A10 falsification test.

## 5. Основные гипотезы и falsifiers

| ID | Provisional hypothesis | Что ослабит или опровергнет | Current status |
|---|---|---|---|
| `A10-H01` | Core semantic distinctions можно специфицировать независимо от одной representation/storage technology. | Обязательная A1–A7 distinction не выражается в materially different realization без collapse meaning, который architecture требует сохранить. | `NOT_TESTED` across independent computation models |
| `A10-H02` | Explicit history/accountability не требует именно Event sourcing. | Любой жизнеспособный non-event-sourced mapping неизбежно теряет required change lineage/accountability или фактически вынужден заново создать эквивалент Event log. | `NOT_TESTED` |
| `A10-H03` | Scoped identity/lineage continuity может пережить representation migration. | Mapping сохраняет declared semantics, но required identity/continuation relations невозможно обосновать без physical identity исходного формата. | `PARTIALLY_SUPPORTED` только current same-lineage mappings; не universal claim |
| `A10-H04` | Unknown, uncertainty и unresolved plurality можно сохранить без одного universal confidence scalar. | Required decision/accountability scenario невозможно представить без silent collapse uncertainty в scalar или binary truth. | `NOT_TESTED` across independent models |
| `A10-H05` | Revision/supersession может сохранять prior epistemic lineage без silent overwrite. | Conforming bounded-memory realization не может сохранить required accountability без unbounded retention superseded state. | `NOT_TESTED` |
| `A10-H06` | Forgetting/disposal можно представлять без невозможных claims о physical substrate state. | Architecture не может различить logical disposal, inaccessible state и actual physical/cryptographic erasure без retention запрещённого proof material. | `OPEN / INDETERMINATE` |
| `A10-H07` | Independent-language implementations дают более сильное portability evidence, чем PostgreSQL↔SQLite в одной Python lineage. | Реализации совпадают лишь из-за скрытых shared representation assumptions или расходятся по A1–A8 obligations при совпавших fixtures. | `NOT_TESTED`; stronger evidence class, не sufficient proof |
| `A10-H08` | Non-address-based substrate может сохранять semantic identity/history через relational/dynamical continuity вместо stable byte addresses. | Analog/neuromorphic mapping не может предоставить достаточно устойчивую lineage, Context, Authority или accountability. | `NOT_TESTED` |
| `A10-H09` | Probabilistic substrates можно оценивать bounded statistical conformance без превращения uncertainty в failure. | Required semantic distinctions нельзя отделить от observational noise или tests становятся non-falsifiable, потому что любое divergence объясняется probability. | `NOT_TESTED` |
| `A10-H10` | Storage и computation mechanisms могут меняться независимо внутри declared semantic constraints. | Изменение одной оси неизбежно меняет semantic law/identity relation/authority rule, который считался substrate-neutral. | `PARTIALLY_SUPPORTED` только для storage profiles |
| `A10-H11` | Laboratory mechanisms могут оставаться reproducible, не превращаясь в Architecture Canon. | Сохранение accepted evidence reproducibility требует сделать profile-specific bytes/SQL/Python универсальными architecture obligations. | `SUPPORTED_FOR_SCOPE` как governance discipline; не substrate proof |
| `A10-H12` | Conformance может быть scoped и loss-aware вместо binary universal compatibility. | Реальные mappings не позволяют meaningful заявлять partial/lossy/indeterminate preservation. | `NOT_TESTED` broadly |

`PARTIALLY_SUPPORTED` здесь — descriptive prose current research context, а не новый machine-readable assertion state.

## 6. Registry открытых вопросов

### `A10-Q01` — Minimum explicit change history
Какова минимальная структура для accountability, если realization не event-sourced?

Candidate answer должен различать как минимум: что изменилось, relevant identity/lineage, Context, Authority где применимо, и достаточно temporal/causal relation, чтобы исключить silent overwrite.

### `A10-Q02` — Reconstruction без exact replay
Если exact replay невозможен, что считать reconstruction-equivalent evidence? Candidates: certified snapshots + lineage proofs, reversible state transitions, independently checkable derivations или bounded audit witnesses. Ничто из этого пока не Canon.

### `A10-Q03` — Identity на lossy substrates
Сколько lineage можно потерять, прежде чем `CONTINUATION_OF` или `SAME` в declared identity relation станет необоснованным?

### `A10-Q04` — Independent-language evidence threshold
Достаточна ли одна independent-language implementation для усиления A8 claim? Ответ A10: **она сильнее same-language profile comparison, но сама по себе недостаточна**. Independence team, representation assumptions, computation model и custody могут быть отдельными измерениями.

### `A10-Q05` — Analog persistence
Какой observable делает analog state persistent memory/identity carrier при отсутствии exact bytes и stable addresses?

### `A10-Q06` — Neuromorphic continuity
Могут ли distributed synaptic/dynamical patterns сохранять lineage и revision accountability без требования one neuron/synapse = one Record?

### `A10-Q07` — Probabilistic conformance
Какой statistical test, confidence protocol и repeated-trial boundary достаточны для falsification preservation claim, не превращая model confidence в Evidence или truth?

### `A10-Q08` — Forgetting proof
Как показать, что information больше не semantically recoverable, не сохраняя content/secret, отсутствие которого требуется доказать?

### `A10-Q09` — Physical deletion observability
Если substrate не раскрывает physical residue, какие claims должны оставаться `INDETERMINATE`, а не повышаться от logical deletion до physical erasure?

### `A10-Q10` — Bounded memory versus auditability
Какая информация обязана пережить compaction/forgetting, чтобы accountability оставалась meaningful? Unbounded history retention не считается universally possible или desirable.

### `A10-Q11` — Causal order без global sequence
Какова минимальная causal/lineage relation, если total global order отсутствует?

### `A10-Q12` — Authority на decentralized substrates
Как представить Authority при отсутствии single writer, database transaction, process owner или global lock?

### `A10-Q13` — Derived-state boundary
Как substrate отличает authoritative retained meaning от disposable/derived views без database-like storage layers?

### `A10-Q14` — Semantic equivalence observables
Какие observable obligations достаточны для `FULL_CONFORMANCE_FOR_SCOPE`, а какие equal outputs всё ещё могут скрывать loss provenance/uncertainty/Authority?

### `A10-Q15` — Contract reclassification
Какие accepted current contracts относятся к architecture contracts, какие к profile contracts, а какие смешивают слои и позднее должны быть разделены без переписывания historical evidence?

### `A10-Q16` — Quantum или non-classical computation
Current blueprint evidence не устанавливает useful Native Kernel mapping на quantum computation. Что будет persistent identity, observation history и reproducible accountability, если measurement меняет state? Это open research question, а не roadmap promise.

### `A10-Q17` — Self-modifying realization
Как realization меняет собственные mechanisms, сохраняя semantic contract, lineage change и Authority самого изменения?

### `A10-Q18` — Evidence independence
Какое минимальное сочетание independent implementation, reviewer, custody и environment нужно, прежде чем claim можно назвать independently validated?

## 7. Falsifiers повторяющихся overclaims

Следующие observations обязаны ослаблять/refute соответствующий overclaim:

1. **Universal portability:** independent realization не сохраняет required distinction → universal wording надо сузить/отозвать.
2. **Semantic equivalence:** outputs совпадают, но provenance/Authority/uncertainty materially различаются → full semantic equivalence не доказана.
3. **Identity:** IDs совпадают, но lineage/referent relation расходится → identifier equality недостаточно.
4. **History:** final state совпадает, но required revision/supersession history невосстановима → history/accountability conformance fails.
5. **Deletion:** наблюдается logical inaccessibility, physical residue не проверяется → physical erasure остаётся indeterminate.
6. **Conflict resolution:** implementation выбирает winner там, где architecture допускает unresolved plurality → нет evidence universal winner rule.
7. **Determinism:** repeatability существует только из-за shared deterministic runtime → substrate-independent determinism не установлена.
8. **Production:** synthetic C5 scenarios pass → production safety/readiness всё ещё не установлена.
9. **Independent evidence:** два profiles разделяют core language, team, harness и custody → это не independent lineage в strong sense.
10. **Future substrate:** mapping/test отсутствует → compatibility остаётся `NOT_TESTED`, а не предполагается.

## 8. Contrasting substrate thought experiments

Это falsification aids, а не implementation commitments.

### 8.1 Eventless state-transition archive

Система хранит certified state snapshots + typed change witnesses, но не canonical Event log. Проверяется, сохраняются ли change lineage, Authority, Context, revision и reconstruction. Если нет — H02 ослабевает.

### 8.2 Distributed neuromorphic memory

Meaning переносится distributed changing patterns без stable row/byte address. Проверяется, можно ли выразить referent/semantic identity, lineage, uncertainty и revision без fiction one neuron/synapse = one Record. Failure ослабляет H08.

### 8.3 Lossy bounded-memory agent

Старые детали compact/forgotten. Проверяется, сохраняется ли required accountability и uncertainty о lost material без fabricated exact history. Failure ослабляет H05/H06/H10.

### 8.4 Probabilistic realization

Повторные executions дают distribution valid outputs, а не один deterministic byte sequence. Проверяется conformance по invariant semantic obligations и сохраняется ли falsifiability реального divergence. Если любой failure можно списать на noise, H09 не квалифицируется.

### 8.5 Independent-language digital profile

Вторая implementation создаётся без импорта Python domain classes/serializer code. Совпадение current fixtures сильнее P5/C3, но hidden shared ontology/fixture assumptions всё равно должны быть accounted. Это не доказывает arbitrary-substrate portability.

## 9. Stop conditions

Architecture work должен остановиться и открыть earlier assumptions для review, если:

- A4 semantic law нельзя согласовать с A1–A3 purpose/ontology/machine;
- A5 identity/time rules делают A6 lifecycle или A7 revision accountability внутренне невозможными;
- A8 conformance требует physical sameness, которое A1/A2 отвергают;
- A9 показывает, что allegedly architectural requirement не имеет meaning-level justification кроме implementation convenience;
- A10 falsifier reproducibly refutes hypothesis внутри claimed scope;
- два blueprint documents используют один term с materially incompatible meanings;
- proposed conformance test не имеет possible failure condition;
- runtime work нужен лишь для того, чтобы architecture claim выглядел true.

Stop означает: записать contradiction, явно сузить/revise hypothesis, сохранить history и выполнить review. Не silent edit prior claims.

## 10. Связь с current P1–C5 evidence

Current laboratory evidence полезно главным образом для regression и bounded falsification:

- P1–P3 могут falsify отдельные identity/history/accountability assumptions внутри current profile;
- P4 выявляет assertion overclaim;
- P5/C3 выявляет storage-profile semantic drift;
- C4 выявляет side effects/authority drift в offline scenarios;
- C5 выявляет bounded operational regressions.

Ни одно из них не даёт strong evidence H01–H10 across independent computation models.

## 11. Связь с pending decisions

A10 не предрешает:

- Issue #18 license/publication;
- Issue #74 / ADR-0024 reducer-v2 topology;
- ADR-0003 runtime conflict semantics;
- Track H source admission;
- future language/storage/hardware profiles.

Open-question registry может позже информировать решения, но не authorizes их.

## 12. First-draft completion test

A10 drafting complete, когда reviewer может:

1. определить основные unproved architecture hypotheses;
2. найти минимум один meaningful falsifier/weakening condition для каждой major hypothesis;
3. отличить `NOT_TESTED` и `INDETERMINATE` от support;
4. найти minimum-history, identity, forgetting, probabilistic-conformance, independent-evidence и non-classical-substrate questions;
5. увидеть explicit stop conditions для возврата к A1–A9 assumptions;
6. подтвердить, что A10 не authorizes runtime expansion или operator-reserved decisions.

Для этого draft тест выполнен как **first drafting pass**. Он не устанавливает истинность open hypotheses.

## 13. Gate после A10

После drafting A10 inventory становится:

```text
A1–A10: DRAFTED / PROVISIONAL
next gate: INTEGRATED_A1_A10_REVIEW
runtime expansion: FROZEN
reference laboratory: BOUNDED
production authorization: false
```

Integrated review должен reconcile terminology, contradictions, duplicate concepts, cross-document dependencies, current contract mappings и falsification coverage across A1–A10. Только после него operator отдельно решает, разрешена ли какая-либо следующая architecture/runtime phase.
