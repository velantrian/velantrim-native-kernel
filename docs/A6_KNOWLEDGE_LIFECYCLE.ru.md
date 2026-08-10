# 🧬 A6 — Жизненный цикл знания

**[English](./A6_KNOWLEDGE_LIFECYCLE.md) · [Русский](./A6_KNOWLEDGE_LIFECYCLE.ru.md)**

> **Deliverable:** `A6_KNOWLEDGE_LIFECYCLE` блюпринта [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.ru.md) под `ADR-0025` / [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88)
> **Depends on:** provisional A1–A5 blueprint content, в частности тринадцать transition families из A3 и identity/time/change model из A5
> **Evidence boundary:** только architecture research и provisional semantic obligations; без runtime, contract, evidence, assertion-map, NK-EPI, maturity или production change
> **Review status:** первый drafted slice; ожидает independent review и integrated A1–A10 review

```text
model_id: nk-knowledge-lifecycle/A6-draft-1
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
next_content_slice: A7_CONFLICT_UNCERTAINTY_AND_REVISION
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```

## 1. Purpose и граница authority

A6 отвечает на один bounded вопрос: через какие повторяющиеся конфигурации проходит knowledge-bearing item после первого encounter, и что легитимирует переход из одной конфигурации в другую? A6 не определяет, что такое Claim или Record (это A2), какие transitions поддерживает abstract Kernel machine (A3), какие laws ограничивают эти transitions (A4), или какое identity/time relation держится через transition (A5). A6 стоит поверх них и называет повторяющуюся, reviewable *форму* жизни knowledge item.

Обязательные non-equivalences:

```text
lifecycle phase ≠ storage status column
closure ≠ deletion of history
one Event ≠ one lifecycle transition
lifecycle position ≠ epistemic validity
lifecycle order ≠ occurrence order ≠ causal order ≠ write-commit order
frequent access ≠ lifecycle advancement
recency ≠ lifecycle advancement
model confidence ≠ lifecycle advancement
retrieval rank ≠ lifecycle advancement
```

Lifecycle authority обязана восходить к явному `DECIDE_DISPOSITION`, `ASSESS_EPISTEMIC_POSITION`, `RELATE`, `DETECT_TENSION`, `REVISE_OR_SUPERSEDE` или `ACCOUNT` transition (A3) с named Authority или method (A4), никогда — к storage presence, retrieval rank, repetition, model confidence, recency или usefulness самим по себе.

## 2. Model status и qualification rule

Lifecycle моделируется как labeled directed graph над phases, а не как линейный pipeline: candidate phase квалифицируется только если она называет повторяющуюся конфигурацию, которая (a) отображается на одну или несколько A3 transition families, (b) имеет minimum obligation, отличимый от любой другой phase, и (c) scoped per A5 identity kind, а не предполагается global.

Поскольку phases scoped per identity kind, один и тот же underlying item может находиться в разных phases одновременно под разными A5 identity relations — например `RELATIONALLY_INTEGRATED` под `RECORD_IDENTITY`, оставаясь `IN_TENSION` под `CLAIM_POSITION_IDENTITY`. A6 не требует одной collapsed phase на item.

## 3. Lifecycle phases

| Phase | A3 transition family | Minimum obligation | Explicit non-equivalence |
|---|---|---|---|
| `ENCOUNTERED` | `ENCOUNTER` | Signal или Observation зарегистрированы как present для Kernel | encountered ≠ retained ≠ believed |
| `RETAINED` | `REGISTER` | item имеет Record со scope и origin | retained ≠ admitted as true |
| `POSITIONED` | `IDENTIFY_OR_DISTINGUISH`, `BIND_SCOPE_AND_ORIGIN`, `INTERPRET_AND_CLASSIFY_ROLE` | item имеет named identity relation (A5), scope/origin binding и classified role | positioned ≠ epistemically weighed |
| `EPISTEMICALLY_WEIGHED` | `ASSESS_EPISTEMIC_POSITION` | назначена explicit epistemic position (граница Belief/Hypothesis/Knowledge из A2) | weighed ≠ permanently settled |
| `RELATIONALLY_INTEGRATED` | `RELATE`, `DECIDE_DISPOSITION` | item имеет named relations к другим items и current disposition (A3 §6) | integrated ≠ conflict-free |
| `IN_TENSION` | `DETECT_TENSION` | назван открытый Conflict, Contradiction или scope mismatch против item | tension ≠ falsity of either side |
| `REVISED_OR_SUPERSEDED` | `REVISE_OR_SUPERSEDE` | существует named successor или correction relation под A5 Revision/Supersession | superseded ≠ erased or false |
| `DISPOSED` | `DECIDE_DISPOSITION` | назначен closure kind (§7) с named Authority или method | disposed ≠ forgotten |
| `ACCOUNTED` | `ACCOUNT` | существует Receipt, называющий, что произошло и под какой Authority | accounted ≠ correct or true |

`DERIVE_BOUNDED_VIEW` и `SELECT_FOR_USE` являются **phase-referencing, not phase-changing**: они читают текущую phase одного или нескольких items, чтобы построить bounded view или сделать selection, но само их выполнение не перемещает item между phases. View над `IN_TENSION` items не разрешает tension.

## 4. Typed lifecycle transition relation

A6 определяет одно typed relation вместо изобретения per-phase transition vocabulary:

```text
LIFECYCLE_TRANSITION(subject, from_phase, to_phase, transition_family, context, authority_or_method, temporal_binding, identity_effect, uncertainty)
```

- `subject` — item под named A5 identity relation, а не bare storage row;
- `from_phase` / `to_phase` — элементы §3, либо `NONE` для первого transition в `ENCOUNTERED`;
- `transition_family` — A3 family, произведшая move (mapping §3);
- `context` — A2 Context, под которым transition оценивался;
- `authority_or_method` — named Authority или deterministic method (A4), легитимировавший move;
- `temporal_binding` — какое A5 temporal dimension (`DECISION_TIME`, `EFFECTIVE_TIME`, `RECORD_TIME` и т.д.) датирует transition;
- `identity_effect` — A5 identity outcome, который transition производит над subject, если применимо;
- `uncertainty` — оспаривается ли сам transition или является provisional.

Outcome transition переиспользует существующий A3 vocabulary, а не изобретает новые термины: `APPLIED`, `NO_CHANGE`, `QUARANTINED`, `REJECTED`, `PARTIAL`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`. `FAILED` или `UNSUPPORTED` lifecycle transition не должен молча оставлять `to_phase` заполненным.

## 5. Non-linearity: branching, looping и plurality

Lifecycle graph — не прямая линия от `ENCOUNTERED` до `ACCOUNTED`:

- **Looping** — item может вернуться из `IN_TENSION` в `RELATIONALLY_INTEGRATED`, или из `RELATIONALLY_INTEGRATED` обратно в `EPISTEMICALLY_WEIGHED`, столько раз, сколько появляются новые Evidence или Relations;
- **Branching** — один `ENCOUNTERED` Signal может произвести несколько `RETAINED` Records под разными scopes, каждый прогрессирующий независимо;
- **Concurrency** — две Authorities могут вести transitions над одним item в перекрывающееся время; A6 требует, чтобы transition называл, какая Authority действовала, а не что действовать может только одна;
- **Simultaneity across identity kinds** — как отмечено в §2, item может находиться в разных phases одновременно под разными A5 identity relations;
- **Open unresolved residency** — item может оставаться неопределённо долго в `IN_TENSION` или `EPISTEMICALLY_WEIGHED`; A6 не требует eventual resolution.

## 6. Lifecycle order

```text
LIFECYCLE_TRANSITION_ORDER ≠ OCCURRENCE_ORDER ≠ CAUSAL_DEPENDENCY_ORDER ≠ LOCAL_WRITE_COMMIT_ORDER
```

Порядок, в котором производятся записи `LIFECYCLE_TRANSITION`, — отдельное ordering relation от A5 orders, на которые оно ссылается. Transition, записанный позже в `LOCAL_WRITE_COMMIT_ORDER`, может нести более раннюю `EFFECTIVE_TIME`, а `REVISE_OR_SUPERSEDE` transition может разрешать Conflict, чей `OCCURRENCE_ORDER` предшествует transitions, уже помеченным `ACCOUNTED`. A6 не требует совпадения этих orders.

## 7. Disposition and closure kinds

A3 §6 уже определяет восемь dispositions (`PENDING`, `AVAILABLE`, `QUARANTINED`, `RESTRICTED`, `REJECTED`, `HISTORICAL_ONLY`, `UNAVAILABLE`, `UNKNOWN`). A6 расширяет этот набор тремя closure kinds, разрешающими erasure/forgetting distinctions, которые A5 §10 назвал, но отложил:

| Closure kind | Minimum obligation | Explicit non-equivalence |
|---|---|---|
| `LOGICALLY_ERASED` | item помечен non-available для ordinary use, пока его Record остаётся inspectable под Authority | logically erased ≠ physically or cryptographically erased |
| `PHYSICALLY_OR_CRYPTOGRAPHICALLY_ERASED` | байты или ключ, необходимый для их восстановления, уничтожены под named method | physically erased ≠ merely restricted or logically erased |
| `FORGOTTEN_OR_LOST` | item больше не reconstructible из accessible sources, без зафиксированного deliberate erasure method | forgotten/lost ≠ globally lost; `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST` (A5/Track H) |

`DISPOSED` phase transition (§3) обязан называть одну из восьми A3 dispositions и, если применимо, один из этих трёх closure kinds. Disposition и closure kind — независимые оси: `RESTRICTED` может сочетаться, а может и не сочетаться с `LOGICALLY_ERASED`.

## 8. Revision and Supersession как lifecycle transitions

`REVISE_OR_SUPERSEDE` (A3), ведущий к transition в `REVISED_OR_SUPERSEDED` (§3), — это lifecycle-level формулировка требований Revision и Supersession из A5 §9: Record предшественника сохраняется, `LINEAGE_CONTINUITY_IDENTITY` преемника называет предшественника, а `REVISED_OR_SUPERSEDED` никогда сам по себе не подразумевает `LOGICALLY_ERASED` или `FORGOTTEN_OR_LOST`.

A6 явно откладывает следующее к Issue #74 / ADR-0024:

- может ли superseded item иметь более одного successor;
- разрешены ли supersession cycles или обязаны быть rejected;
- может ли item superseded самого себя под corrected identity binding.

Reducer v1 остаётся immutable, а reducer-v2 topology остаётся unauthorized; A6 не решает эти вопросы, а только называет, где lifecycle model ожидает их решения.

## 9. Relationship to existing contracts и reference laboratory

Следующая таблица illustrative и **non-canonical**: она отображает существующий P1–C5 Event vocabulary на A6 phases, чтобы поведение reference laboratory можно было читать против model, а не чтобы model получила authority переопределить laboratory.

| P1–C5 Event vocabulary | Illustrative A6 phase | Non-canonical note |
|---|---|---|
| `ADMIT` | `RETAINED` → `POSITIONED` | admission — laboratory-specific method, а не universal transition family |
| `LINK` | `RELATIONALLY_INTEGRATED` | `nk-p1-reducer/1` link semantics — одна profile realization `RELATE` |
| `UTILIZED` | referenced через `SELECT_FOR_USE` | utilization — phase-referencing, not phase-changing (§3) |
| `SUPERSEDED` | `REVISED_OR_SUPERSEDED` | текущая reducer supersession semantics остаётся `Issue #74 / ADR-0024` `PROPOSED / PENDING_OPERATOR` |
| `ERASED` | `DISPOSED` с `LOGICALLY_ERASED` | текущий `ERASED` state остаётся bounded profile mechanism по `Issue #16`; он не promoted к `PHYSICALLY_OR_CRYPTOGRAPHICALLY_ERASED` |

Этот mapping не авторизует новые Event verbs. `CONFLICT_OPENED` и `CONFLICT_RESOLVED` остаются frozen и unauthorized до A7. Он не меняет claims `global_seq` или `stream_seq`, которые остаются reference-laboratory ordering mechanisms, а не самим `LIFECYCLE_TRANSITION_ORDER` (§6). Он не расширяет deletion-execution scope `Issue #16`.

## 10. Failure and indeterminacy cases

- `LIFECYCLE_TRANSITION`, записанный без `authority_or_method`, невалиден, а не молча `APPLIED`;
- item, никогда не покидающий `ENCOUNTERED`, — legitimate, indefinitely stable state, а не ошибка;
- два concurrent transitions, называющие разные значения `to_phase` для одного subject и Context, должны быть записаны как `IN_TENSION`, а не молча arbitrated по write order;
- transition, чей `temporal_binding` не может быть resolved, обязан записать `UNKNOWN`, а не default timestamp;
- `FORGOTTEN_OR_LOST` никогда не должен выводиться только из absence в одном accessible index;
- retry `FAILED` transition обязан произвести новую запись `LIFECYCLE_TRANSITION`, а не silent overwrite неудавшейся;
- `DISPOSED` item, запрошенный снова без новых Evidence, не должен молча re-enter `EPISTEMICALLY_WEIGHED`;
- closure kind (§7), применённый без named method, невалиден;
- phase state, прочитанный через `DERIVE_BOUNDED_VIEW`, не должен кэшироваться дольше Context, который его произвёл, без re-derivation.

## 11. Contrasting substrate mappings

### Manual archival and review process

Физический registry office получает paper filing (`ENCOUNTERED`), проштамповывает и раскладывает его под номером дела (`RETAINED`), клерк identifies сторону и classifies тип документа (`POSITIONED`), проверяющий офицер отмечает, является ли это sworn statement или пометкой на полях (`EPISTEMICALLY_WEIGHED`), документ cross-referenced к related case files (`RELATIONALLY_INTEGRATED`), более поздняя filing противоречит ему, и обе помечаются (`IN_TENSION`), решение судьи supersedes более раннюю filing, пока original остаётся в case file (`REVISED_OR_SUPERSEDED`), дело закрывается и архивируется под retention policy (`DISPOSED`), а closure логируется в ledger офиса (`ACCOUNTED`). Никакой database не существует; каждый `authority_or_method` — named human role.

### Adaptive analog or neuromorphic substrate

Непрерывно меняющийся analog trace, пересекающий detection threshold, — это `ENCOUNTER` субстрата; `RETAINED` может соответствовать изменению synaptic weight, а не discrete row; `POSITIONED` и `EPISTEMICALLY_WEIGHED` могут быть continuous, а не step function, поэтому `authority_or_method` transition обязан уметь называть threshold-crossing rule, а не atomic write; `REVISED_OR_SUPERSEDED` может соответствовать weight decay, конкурирующему с reinforcement, а не discrete successor record. A6 не требует, чтобы phases были discrete storage states, чтобы быть meaningful.

### Conventional digital Event-sourced laboratory

Это текущий P1–C5 profile: `ADMIT` Event перемещает item к `RETAINED`/`POSITIONED`, `LINK` Event способствует `RELATIONALLY_INTEGRATED`, а reducer-derived state материализует current phase. Таблица §9 даёт illustrative, non-canonical mapping; ничто здесь не re-authorizes reducer-v2 или новые Event verbs.

## 12. Falsification criteria и open questions

A6 был бы ослаблен или refuted evidence, показывающим, что:

- повторяющиеся конфигурации не могут быть названы независимо от одной storage schema через три contrasting substrates из §11;
- phase не может быть определена без collapsing различных A5 identity kinds в одну;
- `LIFECYCLE_TRANSITION_ORDER` на практике не может быть kept distinct от `LOCAL_WRITE_COMMIT_ORDER` ни в одном implementable substrate;
- три closure kinds (§7) не могут быть distinguished в substrate, не имеющем отдельного понятия key destruction;
- looping/branching/concurrency (§5) не могут быть представлены без unbounded числа дополнительных phases, defeating qualification rule из §2.

Open questions, отложенные к later work:

- какое минимальное число closure kinds потребуется, когда появится conflict-resolution model A7;
- требует ли A8 более сильного cross-substrate equivalence claim для `authority_or_method`, чем "named";
- меняет ли reference-laboratory classification A9 какую-либо строку illustrative table §9.

## 13. Deferred responsibilities and completion boundary

A6 явно не решает и откладывает к:

- **A7 — Conflict, Uncertainty, and Revision**: conflict taxonomy, resolution Authority и belief-revision policy, на которые в конечном счёте опираются transitions `IN_TENSION` и `REVISE_OR_SUPERSEDE`;
- **A8 — Substrate-independence Contract**: cross-substrate conformance thresholds для lifecycle phases и closure kinds;
- **A9 — Reference Laboratory Boundary**: является ли illustrative P1–C5 mapping из §9 example, experiment или legacy evidence;
- **A10 — Open Questions and Falsification**: registry unresolved architecture questions, поднятых этим и другими slices;
- **Issue #14**: canonical identity encoding, используемый для binding `subject` в `LIFECYCLE_TRANSITION`;
- **Issue #15**: portable history commitment для последовательности записей `LIFECYCLE_TRANSITION`;
- **Issue #16**: execution physical or cryptographic erasure через actual storage locations;
- **Issue #74 / ADR-0024**: reducer-v2 topology и successor/cycle rules для `REVISED_OR_SUPERSEDED` (§8);
- **Issue #18**: license and publication terms;
- **Track H**: operator-controlled historical source admission.

A6 не авторизует runtime implementation, new Event vocabulary, new databases, LLM/vector adapters, а также maturity или production authorization. Он не меняет assertion map, NK-EPI status или любой существующий accepted ADR.
