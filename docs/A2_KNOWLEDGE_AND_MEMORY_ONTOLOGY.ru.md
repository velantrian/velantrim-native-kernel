# 🧬 A2 — Онтология знания и памяти

**[English](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) · [Русский](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md)**

> **Deliverable:** `A2` плана [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.ru.md) (`ADR-0025`, [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88))  
> **Граница evidence:** только архитектурное исследование и предварительная онтология; без изменения runtime, contracts, evidence, assertion map, NK-EPI, maturity или production  
> **Review status:** первый drafted slice; ожидает independent review и integrated blueprint review вместе с A1 и A3–A10

## 1. Назначение и граница authority

Этот документ определяет технологически нейтральную рабочую онтологию понятий, которые Native Kernel должен уметь различать при представлении знания, памяти, поддержки, контекста, изменения, неопределённости и accountability.

Он **не** определяет Python classes, database tables, JSON objects, graph nodes, reducer state, Event envelopes, model prompts, embeddings или API. Он также не утверждает, что каждый термин обязан стать отдельным сохраняемым объектом. Будущий conforming substrate может сохранять различие через структуры, динамику, ограничения, процедуры или другой явно заявленный functional equivalent.

Классификации в этом документе предварительны:

- `CANDIDATE_PRIMITIVE` — сейчас выглядит достаточно несводимым, чтобы проверяться как архитектурный primitive;
- `DERIVED_CONCEPT` — сейчас требует relation или композиции других понятий;
- `OPEN_QUESTION` — различие необходимо, но его статус primitive/derived ещё не установлен.

`Primitive` здесь означает смысловое различие, а не class, row, opcode, field, token или физическую единицу хранения. Финальный статус Canon требует дальнейшего reconciliation через A3–A10, independent review, integrated blueprint review и operator decision.

## 2. Метод и проверка primitive

Candidate primitive должен выдержать следующие проверки:

1. **Substrate test:** определение не требует SQL, JSON, Python, LLM, embeddings, graph, digital bytes или конкретного процессора.
2. **Distinction test:** смешение с соседним понятием создаёт существенную semantic error.
3. **Minimality test:** понятие нельзя удалить, не заставив другой термин нести несовместимые значения.
4. **Role test:** смысл не является только механизмом текущей laboratory implementation.
5. **Counterexample test:** указан факт или дизайн, который способен ослабить primitive status.
6. **Translation test:** существенно разные substrates могут сохранить или явно перевести различие, не притворяясь идентичными.

Эти проверки не доказывают универсальность primitive. Они делают архитектурную гипотезу проверяемой и опровержимой.

## 3. Рассмотренные альтернативные структуры ontology

### 3.1 Линейный promotion pipeline

```text
Signal → Observation → Interpretation → Claim → Hypothesis → Belief → Knowledge
```

**Сильная сторона:** прост для объяснения и полезен в некоторых acquisition workflows.  
**Риск ошибки:** создаёт впечатление, что любой item движется вперёд, поздние стадии автоматически авторитетнее, а Knowledge производится одним необратимым pipeline. Testimony, унаследованные Records, formal derivation, memory recall, conflicting observations и revision не всегда следуют этому порядку.

**Решение A2:** оставить только как один возможный process view, но не как саму ontology.

### 3.2 Event-centred ontology

```text
Event → recorded Event → reducer → State → projection
```

**Сильная сторона:** соответствует текущей P1–C5 laboratory и делает change history явной.  
**Риск ошибки:** превращает одну implementation strategy в Canon, смешивает occurrence с его Record и предполагает, что State обязан быть reducer output.

**Решение A2:** отклонить как default ontology. Event остаётся открытым вопросом primitive status.

### 3.3 Relation-first semantic graph

```text
entities and roles connected by typed Relations
```

**Сильная сторона:** избегает единственного pipeline и выражает Provenance, Evidence, Conflict, Revision и Context как scoped relations.  
**Риск ошибки:** graph representation может скрыть различие между relation в represented reality, заявленной relation и сохранённым edge. Также она может превратить каждое понятие в node/edge только потому, что доступен graph engine.

**Решение A2:** использовать relation-first reasoning там, где оно полезно, не требуя graph substrate.

### 3.4 Stratified role ontology

A2 использует следующую организацию только как средство навигации:

```text
contact and capture
  Signal · Observation · Record

semantic position
  Proposition · Claim · Interpretation

epistemic position
  Hypothesis · Belief · Knowledge · Evidence · Uncertainty

origin, scope, and governance
  Source · Provenance · Context · Authority

continuity and change
  Memory · State · Change · Event · Revision · Supersession

relations and accountability
  Relation · Conflict · Contradiction · Receipt
```

**Сильная сторона:** сохраняет различия без обязательного единственного lifecycle или storage form.  
**Риск ошибки:** термины участвуют в нескольких strata; считать группы непересекающимися types было бы неверно.

**Рабочее решение:** применять структуру только для чтения. Группировка не является Canon и может быть заменена при integrated review.

## 4. Inventory ontology и предварительная классификация

| Понятие | Предварительная классификация | Основная причина |
|---|---|---|
| Signal | `CANDIDATE_PRIMITIVE` | различимое изменение до назначения semantic content |
| Observation | `DERIVED_CONCEPT` | signal/contact, зарегистрированный observer, method и Context |
| Record | `CANDIDATE_PRIMITIVE` | representation, удерживаемое или доступное для reference |
| Proposition | `CANDIDATE_PRIMITIVE` | оцениваемое semantic content независимо от assertion act |
| Claim | `DERIVED_CONCEPT` | Proposition, помещённое в asserted/presented position |
| Interpretation | `DERIVED_CONCEPT` | assignment meaning при assumptions и Context |
| Hypothesis | `DERIVED_CONCEPT` | provisional Proposition для challenge или testing |
| Belief | `DERIVED_CONCEPT` | agent-relative commitment к Proposition |
| Knowledge | `DERIVED_CONCEPT` | scoped epistemic position с declared support и Authority rules |
| Memory | `OPEN_QUESTION` | continuity необходима, но может быть structure, process, capacity или relation |
| Source | `CANDIDATE_PRIMITIVE` | attributed origin полученного материала |
| Evidence | `DERIVED_CONCEPT` | support/challenge role относительно Proposition и вопроса |
| Provenance | `DERIVED_CONCEPT` | relations origin, custody, transformation и gaps во времени |
| Context | `CANDIDATE_PRIMITIVE` | scope и conditions, необходимые для сохранения meaning |
| Relation | `CANDIDATE_PRIMITIVE` | typed scoped connection с declared semantics |
| State | `OPEN_QUESTION` | condition необходимо различать, но representation/derivation не определены |
| Change | `CANDIDATE_PRIMITIVE` | scoped difference или transition по comparator |
| Event | `OPEN_QUESTION` | полезное представление occurrence/change, но не доказанный universal primitive |
| Conflict | `DERIVED_CONCEPT` | scoped tension между positions, requirements или Evidence |
| Contradiction | `DERIVED_CONCEPT` | strict incompatibility при aligned interpretation и scope |
| Uncertainty | `CANDIDATE_PRIMITIVE` | явная граница warranted discrimination или commitment |
| Revision | `DERIVED_CONCEPT` | reasoned Change с сохранённым lineage |
| Supersession | `DERIVED_CONCEPT` | scoped replacement relation без стирания history |
| Authority | `CANDIDATE_PRIMITIVE` | bounded capacity assert/decide/admit/revise/certify |
| Receipt | `DERIVED_CONCEPT` | bounded accountability representation операции или решения |

Таблица фиксирует гипотезу, а не frozen type system.

## 5. Понятия contact и capture

### 5.1 Signal

- **Классификация:** `CANDIDATE_PRIMITIVE`.
- **Рабочее определение:** обнаружимое различие, изменение, pattern или influence, способное достичь observer/interface до назначения semantic content.
- **Чем не является:** Observation, meaning, Claim, Evidence или truth. Noise может быть Signal; Signal может остаться uninterpreted.
- **Отличие от соседних понятий:** Observation — зарегистрированная встреча с Signal при method и Context. Record — representation, удержанное для последующего обращения.
- **Допустимые связи:** может быть detected Source/observer, зарегистрирован как Observation, представлен Record, transformed, filtered, lost или связан с Uncertainty.
- **Identity и lifecycle:** identity Signal может зависеть от continuity, causal origin, sampling frame или declared equivalence; одинаковые measurements не доказывают один origin.
- **Минимальные semantic obligations:** сохранить acquisition boundary, scope, observer/interface, известные transformations/filtering и uncertainty происхождения/полноты.
- **Открытые вопросы:** считается ли purely internal state difference Signal без sender; как выделять signals в continuous dynamics; нужен ли Signal каждому profile?
- **Falsification/counterexample:** если разные substrates сохраняют все необходимые distinctions Observation и Provenance без signal-level concept, primitive status ослабевает. High retrieval score не является Signal от reality: он создан access process.

### 5.2 Observation

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** bounded result регистрации чего-либо observer, instrument, process или interface при declared method, time и Context.
- **Чем не является:** observed reality, Claim о правильности Interpretation, explanation или автоматически Evidence.
- **Отличие от соседних понятий:** Signal — то, что может быть встречено; Observation — scoped registration. Interpretation назначает meaning. Claim представляет Proposition.
- **Допустимые связи:** может основываться на Signals/testimony, быть представлено Records, interpreted, использовано как Evidence, challenged другим Observation и связано с observer/method limits.
- **Identity и lifecycle:** повторные observations могут быть различными при одинаковом value. Исправление method/timestamp может revisе Observation Record без изменения external occurrence.
- **Минимальные semantic obligations:** observer/interface, method, temporal/spatial scope, conditions, uncertainty и разделение raw registration от later interpretation.
- **Открытые вопросы:** является ли testimony Observation, Claim или разными roles; допускаются ли observer-less traces; какие observations требуют identity через transformations?
- **Falsification/counterexample:** thermometer reading `20°C` не утверждает, что room comfortable или instrument calibrated. Неспособность представить gap означает смешение Observation с Claim/Interpretation.

### 5.3 Record

- **Классификация:** `CANDIDATE_PRIMITIVE`.
- **Рабочее определение:** representation, намеренно retained, stabilized или сделанное available, чтобы content, occurrence, process или decision можно было refer после непосредственной встречи.
- **Чем не является:** represented occurrence, Memory само по себе, Claim, Evidence или authoritative history только из-за persistence.
- **Отличие от соседних понятий:** Memory касается continuity и potential reactivation; Record — retained representation. Receipt — специальный accountability Record.
- **Допустимые связи:** представляет Observations, Signals, Claims, Events, States, decisions или другие Records; имеет Sources, Provenance, Context, revisions, restrictions и loss.
- **Identity и lifecycle:** физические copies могут быть разными Records эквивалентного content. Record может сменить format, сохранив content identity, либо сохранить bytes при изменившейся Interpretation.
- **Минимальные semantic obligations:** represented subject, representation boundary, creator/acquisition Source, temporal scope, transformations, integrity limits и declared authority purpose.
- **Открытые вопросы:** являются ли transient neural/analog traces Records; минимальная длительность retention; когда transformed representation становится новым Record?
- **Falsification/counterexample:** stored row без interpretability, traceability или отличия от cache может быть persistence без semantically adequate Record. Storage presence не создаёт Memory или Knowledge.

## 6. Понятия semantic position

### 6.1 Proposition

- **Классификация:** `CANDIDATE_PRIMITIVE`.
- **Рабочее определение:** semantic content, которое в declared interpretation/scope может оцениваться как holding, not holding, undecidable, ill-formed или иначе evaluable независимо от того, кто его представляет.
- **Чем не является:** sentence string, Claim act, Belief, truth value, Record или database field.
- **Отличие от соседних понятий:** Claim помещает Proposition в asserted/presented position. Interpretation определяет, какое content выражает representation.
- **Допустимые связи:** выражается несколькими Records, asserted Claims, supported/challenged Evidence, held as Belief, organized as Hypothesis, contradicted другим Proposition, scoped Context.
- **Identity и lifecycle:** paraphrases могут выражать одно Proposition; одинаковый text — разные Propositions в разных Contexts. Финальные criteria принадлежат A5.
- **Минимальные semantic obligations:** content, scope, relevant interpretation, quantification/modality и отличие от encoding/claimant.
- **Открытые вопросы:** нужны ли parallel categories для questions, commands, values и non-propositional memory; probabilistic content — одно Proposition или distribution?
- **Falsification/counterexample:** “The bank is closed” выражает разные Propositions для financial bank и river bank. Byte equality не может быть единственным identity rule.

### 6.2 Claim

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** scoped semantic position, в котором Source, agent, process или Record представляет Proposition как holding, worth considering или attributable этому Source при declared Context и Authority.
- **Чем не является:** truth, Knowledge, Evidence, stored object или само Proposition.
- **Отличие от соседних понятий:** Proposition — assessable content; Claim включает act/position представления. Observation регистрирует encounter; оно может ground Claim, но не становится им автоматически.
- **Допустимые связи:** asserted Source, expressed Record, interpreted из material, supported/challenged Evidence, held Belief, classified Hypothesis, revised, superseded, conflicted или included Receipt.
- **Identity и lifecycle:** два Sources могут делать разные Claims с одним Proposition. Source может повторить Claim или создать новый; требуются declared identity/context rules.
- **Минимальные semantic obligations:** Proposition, claimant/attribution, Context, temporal scope, asserted force, Authority boundary, Provenance и extraction/attribution uncertainty.
- **Открытые вопросы:** остаются ли questions, explicit unknowns, commands, observations Claim roles или отдельными categories; допускаются ли anonymous Claims?
- **Falsification/counterexample:** миллион повторений “X” остаётся Claims и не делает X true. Promotion по storage count/popularity смешивает repetition с Evidence и Claim с truth.

### 6.3 Interpretation

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** assignment meaning, role, reference или explanatory frame для Signal, Observation, Record, Proposition, Relation или situation при declared assumptions и Context.
- **Чем не является:** сам input, objective truth, гарантия correct understanding или обязательно authoritative Claim.
- **Отличие от соседних понятий:** Observation регистрирует; Interpretation назначает meaning; Claim представляет Proposition. Model output может предложить Interpretation, но не authorize её.
- **Допустимые связи:** produced interpreter/procedure, based on Records/Observations, constrained Context, compared alternatives, revised, used для Claims/Hypotheses, qualified Uncertainty.
- **Identity и lifecycle:** один input допускает несколько Interpretations. Changed assumption создаёт новую Interpretation, не меняя original Record.
- **Минимальные semantic obligations:** interpreted material, interpreter/method, assumptions, Context, alternatives, Uncertainty и transformations input→meaning.
- **Открытые вопросы:** когда Interpretation становится Claim; как non-symbolic substrates expose assumptions; является ли perception Interpretation до explicit representation?
- **Falsification/counterexample:** shadow сначала interpreted как person, затем tree: Observation сохраняется, Interpretation меняется. Overwrite Observation теряет distinction.

## 7. Понятия epistemic position

### 7.1 Hypothesis

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** одно или несколько Propositions, удерживаемых provisionally как candidate descriptions, explanations, mechanisms или predictions и организованных для challenge, comparison, testing или Revision.
- **Чем не является:** слабый synonym Claim, Belief, Knowledge, speculation без scope или гарантия empirical testability во всех domains.
- **Отличие от соседних понятий:** Claim представляет content; Hypothesis задаёт provisional investigative role. Belief — commitment agent. Knowledge — более сильная derived position по declared standards.
- **Допустимые связи:** proposed Source, motivated Observations, supported/challenged Evidence, compared alternatives, contradicted under aligned scope, revised, unresolved, rejected или superseded.
- **Identity и lifecycle:** изменение predictions/mechanism/scope создаёт revised Hypothesis или новую с explicit lineage.
- **Минимальные semantic obligations:** propositions, scope, assumptions, expected observations/consequences, defeating evidence, Uncertainty и status без silent promotion.
- **Открытые вопросы:** non-empirical hypotheses; minimum falsifiability; first-class structure composite hypotheses.
- **Falsification/counterexample:** statement, защищённое от любого counterexample, может быть worldview Claim, но не empirically falsifiable Hypothesis в этом frame.

### 7.2 Belief

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** agent/system-relative disposition acceptance, reliance или commitment к Proposition, возможно с degree, reasons и Uncertainty.
- **Чем не является:** Knowledge, truth, consensus, публичный Claim или confidence score без identified believer/scope.
- **Отличие от соседних понятий:** Claim — presented assertion; Belief — internal/attributed commitment. Knowledge требует дополнительных justification и Authority conditions.
- **Допустимые связи:** held agent, based Evidence/habit, expressed Claim, revised, contradicted другим Belief/Proposition, acted upon, scoped Context/Uncertainty.
- **Identity и lifecycle:** Belief может сохраняться при смене reasons или меняться при неизменных words; требует agent/time scope.
- **Минимальные semantic obligations:** believer/system, Proposition, degree/mode, reasons/Evidence, Context, time, Uncertainty и revision lineage.
- **Открытые вопросы:** может ли Kernel implementation буквально hold beliefs или только represent attributed beliefs; cross-substrate degree comparability.
- **Falsification/counterexample:** человек может искренне верить false Proposition. Belief нельзя определять как Knowledge или truth.

### 7.3 Knowledge

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** scoped epistemic position, в которой Proposition/Claim считается sufficiently supported, attributable и usable при declared standards, Context, Authority и uncertainty boundaries.
- **Чем не является:** objective truth, permanent certainty, stored data, high retrieval rank, repeated use, model confidence, consensus или special physical format.
- **Отличие от соседних понятий:** Belief может не иметь adequate support. Hypothesis остаётся provisional. Knowledge требует explicit warranting policy и остаётся revisable.
- **Допустимые связи:** derived из Claims, Evidence, Provenance, Context и Authority; может быть contested, revised, superseded, restricted, forgotten или reclassified unknown без erasing history.
- **Identity и lifecycle:** knowledge status может измениться при том же Proposition. Communities/systems могут различаться по explicit standards без создания разной reality.
- **Минимальные semantic obligations:** scope/domain, Proposition, support/counterevidence, provenance quality, Authority/policy, Uncertainty, temporal validity, review triggers и reasons admission/withdrawal.
- **Открытые вопросы:** является ли Knowledge Canon или policy-defined profile status; minimum justification; relation to truth; separate criteria formal/empirical/practical/cultural knowledge.
- **Falsification/counterexample:** embedding neighbour или fluent LLM answer может быть relevant, но unsupported. Design, требующий LLM, embeddings, SQL, JSON, digital bytes или specific processor для Knowledge, проваливает substrate-neutrality test.

### 7.4 Evidence

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** role, назначенная material, Observations, Records, results или Relations, когда они влияют на support, challenge, discrimination или testing Proposition, Claim, Hypothesis, decision или question при declared method и Context.
- **Чем не является:** Source, truth, proof по существованию, repetition, popularity, relevance score или любой Record рядом с Claim.
- **Отличие от соседних понятий:** Source — attributed origin; Evidence — scoped epistemic role. Один Source даёт несколько evidence items; один Record Evidence для одного question и irrelevant для другого.
- **Допустимые связи:** supports, challenges, corroborates, undercuts, discriminates или fails to bear; originates Sources; represented Records; имеет Provenance/Uncertainty.
- **Identity и lifecycle:** copying Evidence не создаёт independent Evidence. Independent observations могут иметь одинаковое content, но distinct provenance.
- **Минимальные semantic obligations:** target question/Proposition, direction/type, method, Source/Provenance, independence, Context, Uncertainty, limitations и counterevidence.
- **Открытые вопросы:** aggregation rules; domain standards; absence as Evidence; causal dependence across profiles.
- **Falsification/counterexample:** одна article, скопированная тысячей sites, — repeated reporting одного Source, а не тысяча independent evidence items. Repetition ≠ Evidence.

### 7.5 Uncertainty

- **Классификация:** `CANDIDATE_PRIMITIVE`.
- **Рабочее определение:** explicit limitation warranted discrimination, precision, prediction, Interpretation, attribution или commitment в declared scope.
- **Чем не является:** falsity, ignorance alone, probability alone, Conflict, model confidence или разрешение invent missing answer.
- **Отличие от соседних понятий:** unknown — возможное epistemic condition; Uncertainty описывает type/boundary. Conflict может быть при высокой certainty; uncertainty — без Conflict.
- **Допустимые связи:** qualifies Observations, Interpretations, Evidence, Claims, Hypotheses, Beliefs, Knowledge, Provenance, State, Change и Receipts; возникает из noise, ambiguity, missing data, disagreement, model limits или future contingency.
- **Identity и lifecycle:** uncertainty statements scoped/time-relative; изменение требует reasons/methods.
- **Минимальные semantic obligations:** object, type/source, scope, scale/ordering, assumptions, limits и comparability.
- **Открытые вопросы:** universal uncertainty algebra; comparison qualitative/probabilistic/interval/fuzzy/non-numeric forms; qualifier или entity.
- **Falsification/counterexample:** `unknown` нельзя encode как `false` ради boolean convenience. Substrate, не сохраняющий различие, не сохраняет ontology mapping.

## 8. Понятия origin, scope и governance

### 8.1 Source

- **Классификация:** `CANDIDATE_PRIMITIVE`.
- **Рабочее определение:** attributed entity, process, instrument, artifact, environment или account, из которого получен Signal, Observation, Record, Claim или material.
- **Чем не является:** Evidence, Authority, authenticity, Provenance или truth. Source может быть unknown, deceptive, transformed, composite или derived.
- **Отличие от соседних понятий:** Provenance — history Sources, transformations, custody и gaps. Authority — scoped capacity; Source может не иметь Authority.
- **Допустимые связи:** originates, transmits, records, quotes, transforms, aggregates; имеет identity uncertainty; участвует Provenance; independent/dependent от другого Source.
- **Identity и lifecycle:** Source identity physical, organizational, procedural, anonymous, composite или uncertain. Aliasing/succession принадлежат A5.
- **Минимальные semantic obligations:** attributed identity/unknown, acquisition route, temporal/domain scope, role, transformations, independence assumptions и authenticity limits.
- **Открытые вопросы:** environments/emergent processes как Sources; identity при organizational change; anonymous/privacy-preserving attribution.
- **Falsification/counterexample:** reputable Source может ошибиться, unreliable Source иногда сообщить true. Reputation Source не Evidence сама по себе.

### 8.2 Provenance

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** scoped traceable account origins, acquisition, attribution, custody, transformations, derivations, actors, methods и explicit gaps, через которые material достиг present form.
- **Чем не является:** один `source` field, authenticity, truth, ownership, hash chain alone или complete causal history.
- **Отличие от соседних понятий:** Source называет origin; Provenance связывает origins/transformations во времени. Lineage — возможная часть Provenance.
- **Допустимые связи:** Sources, Records, Claims, Interpretations, Evidence, revisions, transformations, Receipts и authority decisions; partial, contested, unknown или independently attested.
- **Identity и lifecycle:** provenance accounts сами являются Records/Claims с Provenance. Corrections extend/revise, не стирая earlier assertions.
- **Минимальные semantic obligations:** known links/gaps, transformation boundaries, attribution confidence, temporal order, contested alternatives и completeness scope.
- **Открытые вопросы:** portable vocabulary; recursion/compression; privacy-preserving provenance; material equivalence после migration.
- **Falsification/counterexample:** valid digest доказывает correspondence bytes алгоритму, но не creator или truth provenance story. Hash chain ≠ complete Provenance.

### 8.3 Context

- **Классификация:** `CANDIDATE_PRIMITIVE`.
- **Рабочее определение:** bounded conditions, frame, domain, assumptions, participants, temporal/spatial scope, task, jurisdiction или discourse, необходимые для preservation/evaluation meaning.
- **Чем не является:** arbitrary metadata, prompt window, retrieval result, user session или разрешение оставить meaning implicit.
- **Отличие от соседних понятий:** Context scopes Interpretation/validity; Provenance explains origin/transformation. Authority действительна только в Context.
- **Допустимые связи:** scopes Propositions, Claims, Observations, Evidence, Relations, States, Conflicts, Contradictions, Knowledge, actions, Receipts; overlaps, nests, conflicts или unknown.
- **Identity и lifecycle:** Contexts evolve; одинаковые labels не гарантируют same conditions. Mapping раскрывает loss/assumptions.
- **Минимальные semantic obligations:** material dimensions, explicit vs inferred context, unknown context и запрет silent scope widening.
- **Открытые вопросы:** minimal model; identity/inheritance; harmless omission; tacit social/embodied context.
- **Falsification/counterexample:** “It is safe” различается по dose/user/place/time. Contradiction без Context может быть ложной.

### 8.4 Authority

- **Классификация:** `CANDIDATE_PRIMITIVE`.
- **Рабочее определение:** bounded capacity или recognized entitlement assert, classify, admit, decide, revise, restrict, certify или act в declared domain/Context.
- **Чем не является:** truth, expertise everywhere, Source identity, popularity, technical permission или operator approval вне scope.
- **Отличие от соседних понятий:** Source — origin; Authority — scoped role/power. Evidence может justify decision, но не exercise Authority.
- **Допустимые связи:** held, delegated, revoked, contested, scoped, audited; governs admission, Revision, Supersession, access, decisions, Receipts; может требовать Evidence/procedure.
- **Identity и lifecycle:** относится к persons, institutions, procedures, communities, formal rules; меняется во времени. Delegation/succession требуют lineage.
- **Минимальные semantic obligations:** holder/procedure, powers, domain, Context, temporal validity, delegation basis, constraints, authority-conflict rules, revocation.
- **Открытые вопросы:** authority без central actors; competing authorities; legitimacy vs technical authorization; procedural authority across substrates.
- **Falsification/counterexample:** database admin имеет technical permission, но не epistemic Authority объявлять scientific Claim true. Capability ≠ Authority.

## 9. Понятия continuity и change

### 9.1 Memory

- **Классификация:** `OPEN_QUESTION`.
- **Рабочее определение:** continuity-enabling capacity, structure, process или relation, благодаря которым aspects prior encounters, States, meanings, skills, commitments или Changes остаются доступны для later reactivation, comparison, influence, reconstruction или accountable forgetting.
- **Чем не является:** просто stored Record, archive, database, Claim, retrieval success, exact replay или permanent retention.
- **Отличие от соседних понятий:** Record — retained representation; Memory включает continuity, availability, transformation, access conditions и Revision/forgetting. State — condition, не continuity.
- **Допустимые связи:** retains/reconstructs Records, Claims, Relations, procedures, States, Experiences/effects; consolidates, decays, distorts, revised, restricted, superseded, forgotten или inaccessible.
- **Identity и lifecycle:** Memory identity может сохраняться при changed physical representation. Exact copied bytes — новый Record, не обязательно та же memory relation/lived continuity.
- **Минимальные semantic obligations:** что сохраняется, для кого/чего, interval, Provenance, transformations, access limits, Uncertainty, forgetting/restriction status и equivalence claim.
- **Открытые вопросы:** primitive/emergent/family; требует ли retrieval; procedural, affective, distributed, non-symbolic Memory; relation to Identity.
- **Falsification/counterexample:** backup unreadable bytes — stored Record, но не usable Memory. Adaptive analog system сохраняет past influence без discrete records, опровергая Memory=stored entry.

### 9.2 State

- **Классификация:** `OPEN_QUESTION`.
- **Рабочее определение:** bounded characterization condition entity, Relation, system или represented domain при declared time/interval, perspective и abstraction level.
- **Чем не является:** автоматически reducer output, database snapshot, current truth, complete reality или universal global state.
- **Отличие от соседних понятий:** Record представляет; State характеризует condition. Change связывает conditions. Projection может encode State view, но не определяет State universally.
- **Допустимые связи:** applies entities/Relations; observed, represented, derived, compared, revised, uncertain, valid Context и connected Change/Event representations.
- **Identity и lifecycle:** State equality зависит от observables/equivalence. Substrates могут быть contract-equivalent и physically different.
- **Минимальные semantic obligations:** subject, dimensions, scope, time, observer/derivation, Uncertainty, completeness, Authority и equivalence relation.
- **Открытые вопросы:** primitive или view; minimal abstract-machine state; continuous/probabilistic/quantum/distributed conditions.
- **Falsification/counterexample:** P1–C5 reducer result — profile-specific Semantic State. Analog substrate может сохранять relevant conditions без replay Events в map; reducer output не определяет State.

### 9.3 Change

- **Классификация:** `CANDIDATE_PRIMITIVE`.
- **Рабочее определение:** scoped difference, transition, transformation, appearance, disappearance или reclassification между conditions при declared comparator, temporal relation и Context.
- **Чем не является:** обязательно Event object, overwrite, progress, causal explanation или world change только потому, что changed Record.
- **Отличие от соседних понятий:** State — condition; Change связывает conditions. Event — возможное representation occurrence/change. Revision — governed kind of Change.
- **Допустимые связи:** changes State, Record, Claim status, Belief, Knowledge, Provenance, Authority, Context или Memory; observed, recorded, caused, contested, reversed или uncertain.
- **Identity и lifecycle:** transition может decomposed/aggregated по scope; comparator/granularity explicit.
- **Минимальные semantic obligations:** subject, before/after equivalent, time/order, comparator, scope, Uncertainty, reversibility и world-vs-record change.
- **Открытые вопросы:** Change без State; continuous change; causal vs descriptive; minimum ordering across substrates.
- **Falsification/counterexample:** correction timestamp меняет Record, не occurrence. Неспособность различить создаёт historical falsehood.

### 9.4 Event

- **Классификация:** `OPEN_QUESTION`.
- **Рабочее определение:** bounded representation/identification occurrence, action, transition или registered Change как distinguishable unit при declared Context/granularity.
- **Чем не является:** occurrence itself, автоматически append-only, serialized envelope, database row, truth или universal primitive только из-за P1–C5 Event sourcing.
- **Отличие от соседних понятий:** Change — semantic difference/transition; Event package occurrence/change as unit. Record удерживает representation Event. State не обязан reduced from Events.
- **Допустимые связи:** represents Changes, actions, Observations, decisions, Revisions, Supersession; имеет Sources, Provenance, Context, order, causal Claims, Uncertainty, Receipts.
- **Identity и lifecycle:** зависит от granularity/boundary. Одно occurrence — many Event records; один Event summary — many changes.
- **Минимальные semantic obligations:** represented occurrence/change, boundary, time/order limits, participants/Authority, Provenance, Uncertainty и occurrence-vs-record distinction.
- **Открытые вопросы:** нужен ли Event каждому Kernel; functional equivalent continuous/state substrates; history visibility без Event sourcing.
- **Falsification/counterexample:** если разные substrate models сохраняют explicit Change, Provenance, Revision, accountability без event units, universal primitive refuted. P1–C5 доказывает только laboratory utility.

### 9.5 Revision

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** explicit reasoned modification Record, Interpretation, Claim, Belief, Knowledge position, Context assignment или provenance account с сохранением relation к previous representation/position.
- **Чем не является:** silent overwrite, deletion, Conflict resolution by fiat или обязательно Supersession.
- **Отличие от соседних понятий:** Revision — process Change with lineage; Supersession — scoped successor/replacement relation. Correction — возможная reason.
- **Допустимые связи:** revises Interpretations, Claims, Beliefs, Knowledge status, Records, Provenance, Context, Uncertainty; cites reasons/Evidence/Authority; leads Supersession/coexistence.
- **Identity и lifecycle:** часть Revisions сохраняет identity, часть создаёт new item linked lineage. Boundary — A5.
- **Минимальные semantic obligations:** prior state/accountable equivalent, revised content, reason, Authority, time/order, scope, Evidence, Uncertainty, reversibility.
- **Открытые вопросы:** identity-preserving/creating; non-symbolic Memory revision; durable history requirement.
- **Falsification/counterexample:** in-place replace Claim без trace — не accountable Revision, поскольку correction неотличима от manipulation.

### 9.6 Supersession

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** explicit scoped relation, объявляющая later item/version/position/rule replacement earlier one для stated purpose при identifiable earlier history/former scope.
- **Чем не является:** erasure, proof earlier false, universal invalidation, physical deletion или automatic Conflict resolution.
- **Отличие от соседних понятий:** Revision — change process; Supersession — replacement relation. Contradiction может быть без Supersession и наоборот.
- **Допустимые связи:** Records, Claims, Interpretations, policies, States, Knowledge positions; partial, contested, revoked, chained; has Authority/Context.
- **Identity и lifecycle:** successor identity отличается lineage identity. Multiple scoped successors могут быть valid; global single successor не assumed.
- **Минимальные semantic obligations:** predecessor, successor, scope, reason, Authority, effective time/order, retained history и unresolved Conflicts.
- **Открытые вопросы:** branches, cycles, revocation, migration. Issue #74/ADR-0024 остаётся отдельным и не решается A2.
- **Falsification/counterexample:** новая medical guideline supersedes old for current practice, но old Record остаётся true historical documentation. Superseded ≠ false/erased.

## 10. Понятия relations и accountability

### 10.1 Relation

- **Классификация:** `CANDIDATE_PRIMITIVE`.
- **Рабочее определение:** typed, directed или иначе structured scoped connection, asserted, observed, inferred или defined между distinguishable relata при declared semantics.
- **Чем не является:** graph edge, similarity score, causal proof, symmetric association или truth по одному label.
- **Отличие от соседних понятий:** Conflict/Contradiction — specialized derived Relations. Provenance — family origin/transformation Relations. Stored link — Record relation Claim.
- **Допустимые связи:** соединяет ontology concepts при declared domain/range, direction, scope, temporal meaning, Authority, Uncertainty.
- **Identity и lifecycle:** включает relata, type, direction, Context, time, claimant. Equivalent labels не гарантируют semantics.
- **Минимальные semantic obligations:** meaning, relata roles, directionality, arity, scope, temporal validity, Source/Authority, Uncertainty и justified properties symmetry/transitivity.
- **Открытые вопросы:** first-class vs asserted Propositions; n-ary/higher-order; topology constraints; identity across migration.
- **Falsification/counterexample:** vector similarity 0.9 не устанавливает `CAUSES`, `SUPPORTS`, `SAME_AS`. Retrieval association ≠ semantic Relation без Interpretation/governance.

### 10.2 Conflict

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** scoped condition, где Claims, Propositions, Evidence, Interpretations, requirements, Authorities, actions или States нельзя jointly accept/satisfy/rely/apply без unresolved tension в relevant Context.
- **Чем не является:** обязательно logical Contradiction, error, falsity, disagreement alone или то, что must auto-resolve.
- **Отличие от соседних понятий:** Contradiction строже при aligned meaning/scope/time. Conflict возникает из goals, Evidence quality, Authority, resources или Context mismatch.
- **Допустимые связи:** между Claims, Evidence, Interpretations, Beliefs, Authorities, policies, actions, States, Memories; detected, contested, explained, deferred, revised, resolved by Authority.
- **Identity и lifecycle:** зависит от participants, dimensions, scope/time. Reframing Context может dissolve false conflict без changes Claims.
- **Минимальные semantic obligations:** participants, dimension, overlap assumptions, Context, Evidence, Uncertainty, detection method, resolution Authority и unresolved status.
- **Открытые вопросы:** taxonomy; candidate vs established; incomparable contexts; persistence/closure evidence.
- **Falsification/counterexample:** eyewitnesses disagree shirt colour из-за lighting/memory без formal negations. Conflict ≠ automatically Contradiction.

### 10.3 Contradiction

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** strict incompatibility Propositions/commitments, которые при одинаковых relevant interpretation, scope, time, modality и assumptions не могут jointly hold/satisfy.
- **Чем не является:** mere difference, low similarity, preferences, independent alternatives, temporal change или Conflict только из missing Context.
- **Отличие от соседних понятий:** Conflict шире. Contradiction требует semantic alignment достаточного для incompatibility.
- **Допустимые связи:** relates Propositions, Claims, rules, commitments; asserted, detected, challenged, scoped, resolved Revision или retained unresolved.
- **Identity и lifecycle:** зависит от proposition set и alignment Context. Change time/modality может remove contradiction, не resolve её.
- **Минимальные semantic obligations:** propositions, logical/semantic basis, aligned Context, time, modality, assumptions, Uncertainty и Authority judgment.
- **Открытые вопросы:** logic families; paraconsistent handling; graded/probabilistic; vague predicates; cross-language equivalence.
- **Falsification/counterexample:** “door open 09:00” и “closed 10:00” не contradictory. Detector ignoring time создаёт false contradiction.

### 10.4 Receipt

- **Классификация:** `DERIVED_CONCEPT`.
- **Рабочее определение:** bounded accountability Record конкретной operation, decision, selection, transformation, refusal, Revision или result с relevant inputs, exclusions, methods, Authority, limits и references.
- **Чем не является:** truth certificate, complete explanation, proof correctness, Evidence by default, compliance certification или deletion proof.
- **Отличие от соседних понятий:** Record general; Receipt имеет accountability role. Provenance может быть внутри Receipt, но шире одной operation.
- **Допустимые связи:** documents actions, decisions, selections, Revisions, Events, considered Evidence, Context, Authority, outcomes, errors, limitations; может стать Evidence о process при verification.
- **Identity и lifecycle:** bind operation scope/content по profile commitment. Reissued/corrected Receipts требуют explicit relation.
- **Минимальные semantic obligations:** operation, time/order, actor/Authority, inputs/exclusions, method/profile, outputs, Uncertainty, failures, limitations, integrity/Provenance boundary.
- **Открытые вопросы:** minimum receipt non-digital substrates; privacy/selective disclosure; durability; Receipt без persistent log.
- **Falsification/counterexample:** Receipt выбора трёх Records не доказывает sufficient, true или best selection. Replayability ≠ epistemic validity.

## 11. Обязательные non-equivalences

Следующие distinctions обязательны для provisional ontology и являются candidates для A4 laws:

```text
Observation ≠ Claim
Claim ≠ Truth
Evidence ≠ Source
Repetition ≠ Evidence
Belief ≠ Knowledge
Memory ≠ merely a stored Record
retrieval relevance ≠ epistemic validity
Conflict ≠ necessarily Contradiction
Unknown ≠ False
Event usage in P1–C5 ≠ Event as universal primitive
State ≠ necessarily reducer output
Knowledge ≠ LLM / embeddings / SQL / JSON / specific processor
```

Следствия:

- Claim может быть true, false, partly applicable, context-dependent, undecidable или not evaluated;
- Source может иметь Authority в одном Context и быть irrelevant в другом;
- Evidence может support одно Proposition и challenge другое;
- Record может persist, но перестать быть accessible Memory;
- useful retrieval может вернуть false, superseded или truth-irrelevant material;
- missing information остаётся unknown без justified negative Evidence;
- Revision меняет epistemic/representational position без rewriting prior history;
- Authority может authorize decision, не делая premises objectively true.

## 12. Candidate relation grammar

Ontology предварительно выражается через roles/relations, а не mandatory object hierarchy:

```text
Source --emits/transmits--> Signal
Observer/Method --registers--> Observation
Record --represents--> Observation | Proposition | Claim | State | Change | Event
Claim --asserts/presents--> Proposition
Interpretation --assigns-meaning-to--> Signal | Observation | Record
Evidence --supports/challenges--> Proposition | Claim | Hypothesis
Belief --commits-agent-to--> Proposition
Knowledge --classifies-under-policy--> Proposition | Claim
Provenance --traces--> Source | Record | Transformation | Claim
Context --scopes--> every semantic or epistemic relation
Revision --changes-with-lineage--> Record | Interpretation | Claim | Belief | Knowledge
Supersession --replaces-for-scope--> prior item
Conflict --relates-in-tension--> positions or requirements
Contradiction --strictly-incompatible-with--> aligned Proposition
Receipt --accounts-for--> operation or decision
```

Grammar descriptive, а не API, schema, storage model или final formal logic.

## 13. Substrate thought experiments

### 13.1 Manual archival practice

Human team использует paper observations, signed testimony, index cards, cross-references, correction slips и decision ledger. Он различает Source, Record, Claim, Evidence, Revision, Supersession и Receipt без SQL, JSON, LLM или digital Events. Profile может быть медленным и weakly reproducible, но ontology остаётся понятной.

### 13.2 Adaptive analog или neuromorphic substrate

System сохраняет past influence через changing physical dynamics, а не discrete stored rows. Memory/State могут поддерживаться stable attractors/adaptive traces, а Changes не обязаны быть append-only Event envelopes. Conforming mapping раскрывает preserved/approximated/lost distinctions и не называет analog dynamics serialized Events.

### 13.3 Conventional digital laboratory

Текущая P1–C5 implementation помещает широкие semantic roles в `Claim`, records mutations как Events, derives reducer State и emits Receipts. Это valid bounded profile для testing части distinctions. Он не доказывает, что object boundaries являются ontology или future substrates обязаны повторять mechanics.

Thought experiments демонстрируют conceptual portability, но не implementation/conformance evidence.

## 14. Mapping к текущей P1–C5 reference laboratory

| Laboratory concept | Интерпретация A2 | Граница |
|---|---|---|
| `Claim` object | profile container для Record, Proposition, Claim, Observation, Interpretation, Hypothesis, question или unknown roles | current class shape не ontology |
| Event verbs | profile mechanism explicit Change, Relation, utilization, Supersession, erasure markers | Event sourcing не становится universal |
| reducer Semantic State | deterministic profile representation State | State не определяется reducer output |
| typed links | profile representation Relation claims | edge existence не доказывает relation truth |
| charge/retrieval | relevance/selection mechanism | relevance не epistemic validity |
| Receipt | bounded accountability Record | не truth/completeness proof |
| evidence bundles | evidence exact repository runs | artifacts не ontology-level Evidence arbitrary world Claims |

A2 не меняет laboratory contract, history, fixture, evidence artifact или assertion.

## 15. Перенесённые открытые вопросы

1. Memory — один primitive или family retained representation, learned disposition, procedural capacity и identity continuity?
2. Может ли Proposition identity сохраняться без stable symbols/serialized content?
3. State fundamental, observer-relative или always derived view?
4. Нужен ли Event для accountability или continuous/process substrates дают explicit-change equivalent?
5. Какие Relation semantics достаточно universal для Canon?
6. Какие minimum standards отличают Knowledge от justified Belief без infallible truth?
7. Может ли Authority представляться без импорта одной legal/institutional worldview?
8. Как сохранить Provenance при privacy, forgetting и restricted disclosure?
9. Какие Uncertainty forms сравнимы между deterministic, probabilistic, analog и social systems?
10. Как non-propositional content — skills, sensations, images, values, questions, commands — связано с ontology?
11. Какие concepts требуют stable identity, а какие существуют как transient roles/relations?
12. Какие current Glossary definitions должны быть reclassified после A3–A10 без rewriting P1–C5 history?

Вопросы остаются explicit. A2 не решает A3 machine, A4 laws, A5 identity/time, A6 lifecycle или A7 revision policy.

## 16. Falsification criteria для A2

A2 должен быть пересмотрен или отклонён, если independent review покажет:

- primitive можно удалить across contrasting substrates без потери distinctions;
- concepts нельзя различить observable obligation/counterexample;
- definition требует current implementation mechanism;
- ontology превращает Observation в Claim;
- нельзя представить unsupported, false, disputed или unknown Claims;
- Evidence нельзя отделить от Source, repetition или retrieval rank;
- Memory исключает non-record continuity/accountable forgetting;
- State/Event forced event sourcing в каждый profile;
- Knowledge требует model, encoding, database или processor;
- Context не предотвращает false contradiction/silent scope widening;
- Revision/Supersession требуют delete prior history;
- Authority молча становится truth authority;
- EN/RU pair получает incompatible classifications.

## 17. Non-goals

A2 не:

- проектирует tables, indexes, schemas, graph shapes или storage layouts;
- проектирует API, commands, wire protocols или serialization;
- создаёт или проектирует reducer v2;
- выбирает canonical bytes, JSON, hashes или identity encoding;
- утверждает universal Event sourcing/append-only history;
- связывает ontology с Titan, Crystal, Mentaury или другим ecosystem project;
- добавляет LLM, embedding, vector, model-provider или prompt assumptions;
- повышает maturity, production readiness или substrate-neutrality evidence;
- меняет runtime, contracts, evidence bundles, assertion map или NK-EPI support;
- решает Issue #18 или принимает/отклоняет ADR-0024;
- расширяет P1–C5 runtime semantics;
- определяет A3 machine states/transitions;
- определяет A4 numbered laws;
- определяет A5 identity/time rules;
- определяет A6 admission lifecycle;
- определяет A7 Conflict resolution или Belief Revision algorithm;
- объявляет provisional classifications финальным Canon.

## 18. Статус

```text
deliverable: A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
review: PENDING independent review and integrated blueprint review with A1 and A3-A10
next_content_slice: A3_ABSTRACT_NATIVE_KERNEL_MACHINE
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```
