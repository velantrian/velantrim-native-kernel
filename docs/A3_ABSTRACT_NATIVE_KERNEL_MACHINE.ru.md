# 🧬 A3 — Абстрактная машина Native Kernel

**[English](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) · [Русский](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md)**

> **Deliverable:** `A3` blueprint [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.ru.md) (`ADR-0025`, [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88))  
> **Зависит от:** provisional [A1 — Purpose и Non-goals Kernel](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md) и [A2 — Онтология знания и памяти](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md)  
> **Граница evidence:** только архитектурное исследование и preliminary abstract-machine model; без изменения runtime, contracts, evidence, assertion map, NK-EPI, maturity или production  
> **Review status:** first drafted slice; ожидает independent review и integrated blueprint review вместе с A1–A2 и A4–A10

## 1. Назначение и граница authority

Этот документ предлагает минимальную meaning-level machine, которая может быть нужна Native Kernel, чтобы принимать material, сохранять distinctions, привязывать origin/scope, представлять epistemic positions, управлять Relations и Revisions, показывать Uncertainty/Conflict и создавать bounded accountability.

Слово **machine** здесь означает abstract system observable obligations и allowed transitions. Оно **не** означает:

- von Neumann processor;
- claim о Turing completeness;
- finite-state implementation;
- Python object graph;
- SQL transaction processor;
- Event-sourced reducer;
- graph database;
- LLM agent loop;
- один глобально materialized world State.

Conforming substrate может реализовать machine через symbolic Records, physical dynamics, human procedures, distributed protocols, analog adaptation или другой declared functional equivalent. Он обязан указать, какие distinctions/obligations сохраняет, approximates, externalizes или не поддерживает.

A3 не делает A1/A2 final Canon. Он использует provisional vocabulary, чтобы later review мог проверить operational coherence ontology, не позволяя current laboratory mechanics определить ответ.

## 2. Гипотеза machine и проверки

### 2.1 Предварительная гипотеза

Native Kernel можно специфицировать как **scoped obligation-and-transition system**:

```text
encounter или request
        ↓
explicitly scoped transition attempt
        ↓
updated logical configuration или declared non-change
        ↓
bounded outcome + failure/uncertainty visibility + accountability
```

Transition relation не обязана быть linear, globally ordered, deterministic, digital или physically stored как sequence Events.

### 2.2 Проверки

Model должен выдержать:

1. **Ontology test:** сохраняет A2 distinctions, а не смешивает их в current class.
2. **Substrate test:** остаётся meaningful без Python, SQL, JSON, Events, LLM, embeddings, digital bytes или specific processor.
3. **Non-pipeline test:** Interpretation, Evidence assessment, admission, Relation, Revision и selection могут происходить в разном порядке, повторяться, branching или оставаться unresolved.
4. **Authority test:** transition не получает truth authority только потому, что machine его выполнила.
5. **Failure test:** malformed, ambiguous, unauthorized, unsupported, partial или indeterminate operations остаются visible, а не превращаются в false success.
6. **History test:** Revision/Supersession не требуют silent overwrite previous positions.
7. **Unknown test:** missing/unresolved information не превращается в false.
8. **Equivalence test:** два contrasting substrates map to obligations через named equivalence, а не identical mechanics.
9. **Falsification test:** model указывает observations, показывающие over-specification, under-specification или implementation capture.

## 3. Рассмотренные структуры machine

### 3.1 Linear ingestion pipeline

```text
capture → classify → admit → relate → retrieve
```

**Сильная сторона:** простой implementation planning и operational observability.  
**Риск ошибки:** создаёт ложное впечатление, что любой item движется в одном направлении, получает final classification и обязан быть admitted до comparison или Revision.

**Решение A3:** полезно как workflow одного profile, отклонено как abstract machine.

### 3.2 Event-sourced transition machine

```text
command → Event → reducer → State → projection
```

**Сильная сторона:** explicit history, deterministic replay и bounded Receipts в current P1–C5 laboratory.  
**Риск ошибки:** делает Event, global order, replay, reducer State и append-only storage universal до того, как A4–A8 определят semantic obligations.

**Решение A3:** valid laboratory mapping, отклонено как universal machine form.

### 3.3 Relation-centred semantic network

```text
represented items + typed Relations + constraints
```

**Сильная сторона:** поддерживает plurality, Provenance, Conflict, Context и Revision без single lifecycle.  
**Риск ошибки:** stored edges могут приниматься за true Relations; temporal Change, Authority и accountability становятся implicit.

**Решение A3:** сохранить relation-centred reasoning, но требовать explicit transition и Authority obligations.

### 3.4 Capability-and-obligation machine

```text
logical configuration facets
+ typed transition families
+ explicit preconditions/postconditions
+ declared failure outcomes
+ authority and uncertainty boundaries
```

**Сильная сторона:** отделяет meaning-level obligations от physical realization и допускает symbolic, procedural, analog, distributed или hybrid profiles.  
**Риск ошибки:** model может стать настолько abstract, что нефальсифицируема, либо настолько широка, что любая system выглядит conforming.

**Рабочее решение:** использовать provisional structure и ограничивать её observable obligations, negative cases, substrate mappings и later A4/A8 contracts.

## 4. Модель abstract machine

### 4.1 Нотация logical configuration

Только для specification введём scoped Kernel configuration:

```text
K = ⟨B, R, I, C, P, E, L, U, G, V, D, A, O⟩
```

Каждый symbol означает **logical facet**, а не table, collection class, graph, physical register или required stored object.

Transition attempt записывается:

```text
τ : ⟨K, request, declared context, declared authority/policy⟩
      ↦ ⟨K′, outcome, bounded accountability⟩
```

или:

```text
τ ↦ DECLARED_FAILURE | DECLARED_UNKNOWN | NO_AUTHORIZED_CHANGE
```

`K` и `K′` — scoped characterizations для specification. Они не утверждают, что reality имеет complete global State, любой substrate materializes snapshots или transition execution является reducer replay.

### 4.2 Facets configuration

| Symbol | Facet | Минимальный смысл | Чем не является |
|---|---|---|---|
| `B` | boundary encounters | material/influence, presented Kernel boundary, включая explicit absence/unknown | автоматически Observation, Record или Claim |
| `R` | retained representations | Records/functional equivalents, доступные для reference при declared limits | Memory целиком; truth; одна database |
| `I` | identity/equivalence positions | scoped assertions, hypotheses или unknown о sameness, difference, aliasing, continuity и reference | byte equality; final A5 identity law |
| `C` | Context bindings | conditions/scope для Interpretation/evaluation material | prompt window или arbitrary metadata |
| `P` | Source/Provenance bindings | attributed origin, acquisition, transformation, custody и explicit gaps | authenticity/truth proof |
| `E` | semantic/epistemic positions | Proposition, Claim, Interpretation, Hypothesis, Belief, Knowledge-candidate и Evidence-role assignments | objective truth или один confidence score |
| `L` | Relations | typed, scoped connection positions между distinguishable relata | graph edges, true by storage |
| `U` | Uncertainty/tension register | explicit Uncertainty, candidate/established Conflict, Contradiction assessments и unresolved plurality | automatic resolution или false-by-default |
| `G` | governance/Authority | declared powers, policies, delegations, restrictions и contested Authority | universal legitimacy или technical permission alone |
| `V` | Revision/Supersession lineage | explicit Relations между prior/later representations или positions | silent overwrite/deletion |
| `D` | disposition/availability | handling status для operational availability, quarantine, restriction, historical-only access или declared absence | epistemic truth status или final A6 lifecycle |
| `A` | accountability | Receipts/functional equivalents для operations, decisions, failures и omissions | proof outcome true/complete |
| `O` | open obligations | unresolved questions, unsupported mappings, pending decisions, incomplete operations и declared loss | hidden backlog или implicit false |

Profile может combine, distribute или externalize facets. Он не может заявлять full A3 conformance, silently dropping required distinction.

### 4.3 Requests и outcomes

Request может происходить от person, instrument, process, environment, another system или internal condition. Request identity и Authority — разные вопросы.

Outcome должен классифицироваться как минимум одним значением:

- `APPLIED` — declared semantic effect представлен;
- `NO_CHANGE` — request оценён, semantic effect не authorized/required;
- `QUARANTINED` — material isolated до появления missing scope, Authority, Interpretation или safety conditions;
- `REJECTED` — declared policy/precondition запрещает effect;
- `PARTIAL` — представлен bounded subset, missing effects explicit;
- `UNKNOWN` — machine не может warrant stronger result;
- `UNSUPPORTED` — profile не имеет capability/faithful mapping;
- `FAILED` — execution/representation не удовлетворило obligations.

Это abstract operation outcomes, не final knowledge lifecycle states. A6 может их refine/replace.

## 5. Семейства transitions

Transition families описывают meaning-level obligations. Это не mandatory API methods, Event verbs, commands, classes или single ordered pipeline.

### 5.1 `ENCOUNTER`

**Назначение:** expose material/influence Kernel boundary без premature classification.

- **Preconditions:** boundary/interface declared; available Source, time, method, Context supplied или explicitly unknown.
- **Postconditions:** bounded encounter отличим от later Observation, Interpretation, Claim, Evidence и admission; acquisition Uncertainty visible.
- **Allowed outcomes:** `APPLIED`, `QUARANTINED`, `PARTIAL`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** conversion каждого input packet прямо в Claim смешивает encounter и assertion.

### 5.2 `REGISTER`

**Назначение:** create/recognize Record или functional equivalent, доступный для reference после immediate encounter.

- **Preconditions:** represented subject/boundary stated; retention/reference Authority exists; known transformations/integrity limits available.
- **Postconditions:** representation identity или explicit identity gap exists; Source/Provenance/Context Uncertainty attached; storage не означает admission/Memory.
- **Allowed outcomes:** `APPLIED`, `QUARANTINED`, `REJECTED`, `PARTIAL`, `UNKNOWN`, `FAILED`.
- **Failure/counterexample:** opaque persisted bytes без interpretable boundary/lineage могут быть storage, но не adequate Record.

### 5.3 `IDENTIFY_OR_DISTINGUISH`

**Назначение:** state, являются ли represented items/referents/versions/continuities same, different, related, ambiguous или unresolved при declared criterion.

- **Preconditions:** candidate relata/comparison criterion explicit; relevant Context, time, Authority declared.
- **Postconditions:** identity/equivalence position и Uncertainty represented без merge Records/referents by convenience.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `QUARANTINED`, `PARTIAL`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** equal hashes/text не доказывают semantic, Source или continuity identity.

### 5.4 `BIND_SCOPE_AND_ORIGIN`

**Назначение:** attach Context, Source, Provenance, temporal scope и Authority к material/positions.

- **Preconditions:** target distinguishable; bindings attributable; known gaps/contested alternatives representable.
- **Postconditions:** scope/origin explicit или explicitly unknown; later operations detect missing/changed bindings; no authenticity/truth promotion.
- **Allowed outcomes:** `APPLIED`, `PARTIAL`, `UNKNOWN`, `QUARANTINED`, `FAILED`.
- **Failure/counterexample:** invented absent Source ради non-null field превращает unknown Provenance в false Provenance.

### 5.5 `INTERPRET_AND_CLASSIFY_ROLE`

**Назначение:** assign meaning/semantic role: Observation, Proposition, Claim, Interpretation, Hypothesis, question, instruction или unknown.

- **Preconditions:** represented material/interpretive Context available; interpreter/method и assumptions attributable where material.
- **Postconditions:** role assignment represented как Interpretation/position с alternatives/Uncertainty; original material distinguishable.
- **Allowed outcomes:** `APPLIED`, `PARTIAL`, `QUARANTINED`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** model label без assumptions/alternatives не становится intrinsic type material.

### 5.6 `ASSESS_EPISTEMIC_POSITION`

**Назначение:** assess support, challenge, dependence, Uncertainty, Belief attribution, Hypothesis status или policy-defined Knowledge candidacy.

- **Preconditions:** target Proposition/Claim/question explicit; Evidence roles, Sources, Provenance, Context, counterevidence, warranting policy available или gaps declared.
- **Postconditions:** scoped assessment, reasons, Uncertainty, Authority represented; repetition, relevance, confidence/admission alone cannot promote Knowledge.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `PARTIAL`, `UNKNOWN`, `QUARANTINED`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** один Source, copied many times, остаётся dependent Evidence, а не independent corroboration.

### 5.7 `DECIDE_DISPOSITION`

**Назначение:** определить operational availability, quarantine, restriction, rejection, historical-only или другое handling по declared policy.

- **Preconditions:** applicable policy, Authority, purpose, Context, risks declared; epistemic status и operational utility distinct.
- **Postconditions:** disposition, scope, reason, Authority, effective time/review conditions explicit; admission не становится truth.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `QUARANTINED`, `REJECTED`, `PARTIAL`, `UNKNOWN`, `FAILED`.
- **Failure/counterexample:** item allowed in retrieval из-за usefulness не делает его Claim valid.

### 5.8 `RELATE`

**Назначение:** represent typed, scoped Relation position among distinguishable relata.

- **Preconditions:** relata, relation semantics, direction/arity, Context, time, Source/Authority, Uncertainty stated.
- **Postconditions:** relation Claim distinguishable from represented reality и physical encoding; unsupported transitivity/symmetry not inferred.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `PARTIAL`, `UNKNOWN`, `QUARANTINED`, `FAILED`.
- **Failure/counterexample:** vector similarity/co-occurrence cannot silently become `SAME_AS`, `CAUSES` или `SUPPORTS`.

### 5.9 `DETECT_TENSION`

**Назначение:** identify possible/established Conflict, Contradiction, scope mismatch, Provenance disagreement, Authority Conflict или unresolved plurality.

- **Preconditions:** compared positions и relevant Interpretation, Context, time, modality, assumptions sufficiently explicit; missing alignment visible.
- **Postconditions:** tension type, basis, participants, Uncertainty, candidate/established status represented; no automatic winner/resolution.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `PARTIAL`, `UNKNOWN`, `QUARANTINED`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** “open at 09:00” и “closed at 10:00” нельзя назвать contradictory при different temporal scopes.

### 5.10 `REVISE_OR_SUPERSEDE`

**Назначение:** change representation/epistemic position с accountable lineage/scope.

- **Preconditions:** predecessor identifiable; proposed successor/change, reason, Evidence, Authority, Context/effective scope declared.
- **Postconditions:** prior position historically distinguishable или explicit lawful-forgetting boundary recorded; successor/replacement scope explicit; unresolved Conflicts visible.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `REJECTED`, `PARTIAL`, `UNKNOWN`, `QUARANTINED`, `FAILED`.
- **Failure/counterexample:** overwrite Claim in place without lineage не accountable Revision. A3 не решает ADR-0024 referential rules/reducer-v2 topology.

### 5.11 `DERIVE_BOUNDED_VIEW`

**Назначение:** construct scoped characterization, projection, summary, State view или comparison из available material.

- **Preconditions:** requested scope, selection rules, method/profile, inputs, omissions, equivalence criterion и Uncertainty treatment declared.
- **Postconditions:** view linked to inputs/method; incompleteness/staleness visible; view не rewrites represented history и не становится universal State.
- **Allowed outcomes:** `APPLIED`, `PARTIAL`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** reducer output — один laboratory view; determinism не определяет State для every substrate.

### 5.12 `SELECT_FOR_USE`

**Назначение:** select material для query, task, decision или Context без смешения relevance с epistemic validity.

- **Preconditions:** query/task, requester Authority, Context, access restrictions, selection method и relevant time boundary declared.
- **Postconditions:** selected items, ranking/ordering, exclusions, Uncertainty, selection method accountable; unsupported material labelled.
- **Allowed outcomes:** `APPLIED`, `PARTIAL`, `UNKNOWN`, `REJECTED`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** top retrieval result может быть false, superseded или lexically similar; selection rank не Knowledge.

### 5.13 `ACCOUNT`

**Назначение:** emit/make available bounded Receipt/functional equivalent для operation, decision, failure или non-action.

- **Preconditions:** operation identity/scope и available actor, input, method, Authority, output, exclusion, failure, limitation info distinguishable.
- **Postconditions:** Receipt states what happened/could not be established и boundary; не certifies truth/completeness/correctness by existence.
- **Allowed outcomes:** `APPLIED`, `PARTIAL`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** Receipt без rejected inputs/partial failure может falsely imply complete operation.

## 6. Handling dispositions

A3 нужна minimum expressiveness operational handling без finalization A6 knowledge lifecycle.

| Disposition | Смысл в A3 | Явно не означает |
|---|---|---|
| `PENDING` | требуется additional Interpretation, scope, Authority или Evidence | false/rejected |
| `AVAILABLE` | usable для declared purpose under policy | true, Knowledge, unrestricted/permanent |
| `QUARANTINED` | isolated pending stated condition/investigation | disproved/erased |
| `RESTRICTED` | availability limited policy, Authority, safety, privacy или law | physically deleted/epistemically invalid |
| `REJECTED` | requested admission/use/change not authorized under rule | Proposition objectively false |
| `HISTORICAL_ONLY` | retained for lineage/accountability, not current operational use | erased/irrelevant to all questions |
| `UNAVAILABLE` | not accessible in present scope из-за loss, restriction, absence или unsupported mapping | known not to exist |
| `UNKNOWN` | stronger disposition cannot be warranted | `false`, `none` или empty storage |

Это provisional handling terms. A6 может split/rename/reject их.

## 7. Discipline preconditions и postconditions

Каждый profile-defined transition должен declare:

### Preconditions

- target/request identity или explicit ambiguity;
- required Context/temporal scope;
- relevant Source/Provenance availability;
- required Authority/policy;
- required capabilities/supported equivalence profile;
- known Uncertainty/Conflict;
- safety, privacy, access, retention constraints где relevant.

### Postconditions

- exact semantic effect или explicit non-effect;
- changed/unchanged configuration facets;
- newly introduced Uncertainty, loss или approximation;
- lineage к prior positions;
- Authority/policy used;
- partial/failed operations и unresolved obligations;
- bounded accountability для later inspection.

Profile может group transition families в one operation, но не скрывать applied/skipped/approximated/failed obligations.

## 8. Inventory failures и indeterminacy

| Failure/indeterminacy | Required machine response |
|---|---|
| malformed/uninterpretable material | preserve failure boundary; не fabricate semantic content |
| unknown/contested Source | represent unknown/alternatives; не invent attribution |
| Provenance gap | expose gap и affected confidence/Authority |
| ambiguous identity/collision | keep candidates distinct до authorized resolution/scope |
| insufficient Context | quarantine, narrow Claim или return unknown; не silently widen scope |
| absent/contested Authority | no authorized semantic Change; record refusal/pending где accountable |
| incompatible policies/Authorities | represent governance Conflict; не choose by implementation priority |
| dependent/repeated Evidence | preserve dependence; copies не independent support |
| unresolved Conflict/Contradiction | keep plurality visible; resolution needs declared procedure/Authority |
| unsupported transition/profile capability | return `UNSUPPORTED`, disclose loss; не emulate silently |
| partial physical execution | expose `PARTIAL`/`FAILED`; no success Receipt for unapplied effects |
| non-reproducible Interpretation/selection | disclose method, variability, Uncertainty; no deterministic equivalence claim |
| stale/incomplete derived view | expose source checkpoint/scope/omissions |
| unavailable Receipt capability | no full accountability equivalence claim for operation |
| restricted/forgotten material | do not reconstruct/reveal content to satisfy replay/accountability |

Failure может стать Record/Evidence about process, но не Evidence unrelated world Claim.

## 9. Determinism, reproducibility и non-determinism

### 9.1 Deterministic boundary

Transition называется deterministic только относительно declared:

- inputs и identity;
- configuration scope;
- policy/Authority state;
- algorithm/procedure version;
- ordering/time assumptions;
- external dependencies;
- equivalence criterion.

Determinism procedure не означает truth inputs/Interpretation.

### 9.2 Reproducible boundary

Два executions могут быть reproducibly equivalent без identical physical states/bytes, если named profile определяет:

- observable outputs;
- tolerated variation;
- preserved semantic distinctions;
- ordering guarantees;
- loss/Uncertainty disclosure.

A3 не задаёт thresholds; это должен сделать A8.

### 9.3 Legitimately non-deterministic или interpretive operations

Следующие могут оставаться non-deterministic, plural, probabilistic, human-mediated или substrate-dependent:

- perception/segmentation continuous input;
- Interpretation;
- identity matching under ambiguity;
- Evidence weighting;
- Hypothesis generation;
- Conflict detection under vague language;
- selection/ranking;
- Authority decisions;
- reconstruction from incomplete Memory.

Они не запрещены. Требуются declared variability, method, alternatives, Uncertainty/accountability. Non-determinism нельзя скрывать deterministic-looking Receipt.

### 9.4 Irreproducible boundary

Если profile не сохраняет enough input, method, policy или outcome information для declared equivalence, operation классифицируется irreproducible/unsupported, а не replayable.

## 10. Границы Authority

| Authority role | Может authorize | Не authorize автоматически |
|---|---|---|
| boundary/acquisition Authority | accepting contact from interface/Source | truth, admission, unrestricted retention |
| representation Authority | creating/correcting Record under procedure | represented reality или Source authenticity |
| identity Authority | identity/equivalence decision в domain | identity in every Context/substrate |
| interpretive Authority | applying declared interpretation framework | objective truth/exclusive meaning |
| epistemic Authority | applying warranting standard в domain | universal infallibility/operational use |
| admission/disposition Authority | availability, quarantine, restriction/rejection for purpose | Claim truth/permanent retention |
| relation Authority | asserting/accepting Relation under vocabulary | causal proof/unsupported transitivity |
| Revision/Supersession Authority | changing scoped position with lineage | erasing history/deciding ADR-0024 |
| access/forgetting Authority | restricting availability/authorizing forgetting | proof physical deletion без separate evidence |
| conformance Authority | certifying profile against named obligations | production readiness, truth или ecosystem legitimacy |

Authority может быть distributed, procedural, contested, delegated, time-limited или absent. Abstract machine enforces/exposes declared boundaries; inherent truth Authority у неё нет.

## 11. Ordering, history, concurrency и partial order

A3 не требует one global total order.

Profile должен declare supported ordering relations:

- occurrence order;
- Observation/registration order;
- causal/dependency order;
- Revision/Supersession lineage;
- Authority decision order;
- local write/commit order;
- cross-substrate synchronization order;
- unknown/concurrent order.

Transitions могут быть concurrent, incomparable или later reconciled. Profile-imposed total order для convenience не является order represented reality.

History visibility требует declared functional obligation, но A3 не решает, должны ли это быть append-only Events, versioned Records, reversible procedures, physical traces или другой A8-approved equivalent.

## 12. Queries, views, selections и explanations

Machine должна различать четыре roles:

```text
query/task
≠ selected material
≠ derived view
≠ epistemic judgment
```

Bounded explanation/Receipt раскрывает, где material:

- request/Context;
- inputs considered/excluded;
- selection/derivation method;
- Authority/policy;
- relevant Provenance;
- Uncertainty, Conflicts, unsupported operations;
- outcome/non-effect;
- checkpoint/temporal boundary;
- limitations/alternative Interpretations.

Concise Receipt может reference другие Records вместо повторения forbidden/restricted content. Accountability не требует expose content, которое policy требует forget/withhold.

## 13. Substrate mappings

### 13.1 Manual archival и deliberative substrate

Human institution использует paper Records, signed Source attributions, index references, quarantine folders, revision slips, authority registers и decision Receipts.

Possible mapping:

- `R`: paper/physical Records;
- `P/C`: source sheets/context annotations;
- `I/L/E/U`: index cards/deliberative decisions;
- `V`: correction/Supersession slips;
- `D`: physical access zones/handling rules;
- `A`: signed operation/decision Receipts.

Он сохраняет многие A3 obligations без digital Events/reducers. Weaknesses: slow comparison, incomplete global search, limited reproducibility. Limits disclosed, а не treated as absence machine.

### 13.2 Adaptive analog или neuromorphic substrate

Physical adaptive system сохраняет prior influence в changing dynamics, attractors или distributed traces, не discrete rows.

Possible mapping:

- Memory/availability через stable/metastable dynamics;
- Interpretation/selection как physical transformations;
- configuration facets observable только probes/companion procedures;
- explicit Provenance, Authority, Revision lineage, Receipts могут требовать attached representational layer.

Если substrate не может expose Provenance gaps, distinguish Revision from overwrite или provide bounded accountability high-impact operations, он может реализовать useful memory dynamics, но не full A3 conformance.

### 13.3 Conventional digital Event-sourced laboratory

Current P1–C5 profile maps:

- commands/Events к некоторым transition attempts/recorded Changes;
- reducer Semantic State к одному `DERIVE_BOUNDED_VIEW` result;
- stored Claims к broad representation container;
- typed links к Relation positions;
- retrieval charge к one selection mechanism;
- Receipts к accountability outputs.

Mapping valuable/testable, но остаётся one profile. Event vocabulary, append-only history, SQL persistence, Python classes, deterministic reducer replay и exact JSON/bytes не universal A3 requirements без later A4/A8 decision.

## 14. Mapping boundary с P1–C5

| A3 obligation | P1–C5 laboratory mechanism | Boundary |
|---|---|---|
| explicit representation | `Claim` object/stored payload | broad container, not final ontology |
| transition visibility | Event envelope/verbs | useful profile mechanism, not universal transition form |
| bounded ordering | append sequence/profile ordering | not represented-reality total order |
| derived view | deterministic reducer Semantic State | one scoped State representation |
| Relations | typed link Events/state | stored relation position, not truth proof |
| selection | charge/retrieval | relevance mechanism only |
| Revision/Supersession | versioning/Event semantics | ADR-0024/reducer-v2 unresolved/unauthorized |
| accountability | Receipt artifacts | bounded process Evidence, not epistemic proof |
| cross-profile equivalence | PostgreSQL/SQLite comparison | shared Python lineage/named current contracts only |

A3 не меняет эти mechanisms/evidence.

## 15. Обязательные non-equivalences

```text
abstract machine ≠ runtime implementation
logical configuration K ≠ complete world State
transition ≠ Event envelope
transition relation ≠ reducer
history visibility ≠ mandatory Event sourcing
Record registration ≠ admission
admission ≠ truth
available ≠ Knowledge
selected/relevant ≠ epistemically valid
deterministic output ≠ true output
reproducible ≠ physically identical
Relation position ≠ represented relation reality
conflict detection ≠ conflict resolution
revision ≠ silent overwrite
Supersession ≠ deletion
Receipt ≠ proof of correctness
unknown/unsupported/failed ≠ false
Authority in one role ≠ authority in every role
profile conformance ≠ production authorization
```

## 16. Перенесённые открытые вопросы

1. Какие configuration facets truly minimal, а какие derived без semantic loss?
2. Каждый accountable transition должен durable Receipt или profiles могут aggregate low-risk operations?
3. Каков minimum history visibility без replay?
4. Может ли non-symbolic substrate expose Context/Provenance без companion symbolic layer?
5. Admission — Kernel primitive, policy-layer operation или A6 derived lifecycle concept?
6. Какие transitions требуют atomic semantic effect и что означает partial application substrate-neutrally?
7. Как represent concurrent/incomparable/cyclic Revision lineages без premature ADR-0024 decision?
8. Какие Authority roles universal/domain-specific?
9. Может ли operation быть deterministic при contested identity/Interpretation/Authority inputs?
10. Какие equivalence observations sufficient для manual, analog, probabilistic, quantum, distributed profiles?
11. Какие forgetting forms совместимы с accountable history без retaining forbidden content?
12. Требует ли full A3 conformance всех transition families или A8 capability classes?
13. Как A3 связан с non-propositional skill, affective, sensorimotor или embodied Memory?
14. Какие failure outcomes externally observable, а какие only authorized auditor?

## 17. Falsification criteria для A3

A3 должен быть revised/rejected, если review показывает:

- machine не может represent Observation без conversion to Claim;
- transition necessarily requires Event envelope, reducer, global log, SQL row, JSON object или digital processor;
- `K` понимается только как fully materialized global State;
- transition families force one linear lifecycle или не выражают branching, repetition, quarantine, unresolved plurality;
- admission, retrieval, deterministic derivation или Authority silently becomes truth;
- failures/unsupported capabilities не distinct from false;
- Revision requires silent overwrite или Supersession requires deletion;
- contrasting substrates не map obligations без pretending identical mechanics;
- arbitrary system claims conformance by renaming operations без observable obligations;
- required facet removable across substrates без loss A1/A2 distinction;
- full conformance requires exposing content, которое lawful forgetting/restriction требует withhold;
- EN/RU pair develops different transition, Authority или failure semantics.

## 18. Non-goals

A3 не:

- проектирует tables, schemas, indexes, object models, graph shapes или storage layouts;
- определяет API, commands, Event verbs, wire protocols, serialization, canonical bytes или hashes;
- implements/specifies reducer v2;
- требует Event sourcing, append-only logs, global total order, snapshots или replay как only history model;
- определяет final A4 semantic laws;
- решает A5 identity/time/change rules;
- определяет final A6 knowledge lifecycle;
- определяет A7 conflict-resolution или belief-revision algorithms;
- определяет A8 conformance levels/equivalence thresholds;
- связывает machine с Titan, Crystal, Mentaury, LLM, embeddings, SQL, JSON, Python или particular processor;
- меняет runtime, contracts, fixtures, evidence, assertions, NK-EPI, maturity или production status;
- решает Issue #18, Issue #74 / ADR-0024 или Track H source acceptance;
- утверждает conformance paper, analog, neuromorphic, quantum, biological или future substrates;
- promotes A1–A3 to final Canon до independent/integrated review.

## 19. Статус

```text
deliverable: A3_ABSTRACT_NATIVE_KERNEL_MACHINE
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
machine_form: SCOPED OBLIGATION-AND-TRANSITION SYSTEM
review: PENDING independent review and integrated blueprint review with A1-A2 and A4-A10
next_content_slice: A4_SEMANTIC_LAWS_AND_INVARIANTS
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```
