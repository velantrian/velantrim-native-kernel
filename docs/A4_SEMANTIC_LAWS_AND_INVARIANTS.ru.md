# ⚖️ A4 — Семантические законы и инварианты

**[English](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md) · [Русский](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md)**

> **Deliverable:** `A4` плана [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.ru.md) (`ADR-0025`, [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88))  
> **Depends on:** provisional [A1](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md), [A2](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md) и [A3](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md)  
> **Law-set identity:** `nk-semantic-laws/A4-draft-1`  
> **Граница evidence:** только архитектурное исследование и provisional semantic obligations; без изменения runtime, contracts, evidence, assertion-map, NK-EPI, maturity или production  
> **Review status:** первый drafted slice; ожидает independent review и integrated blueprint review вместе с A1–A3 и A5–A10

## 1. Назначение и граница authority

A2 формулирует различия, которые Native Kernel может быть обязан представлять. A3 формулирует meaning-level transition obligations, способные работать поверх этих различий. A4 задаёт более узкий вопрос:

> **Какие semantic distinctions и правила сохранения нельзя молча схлопывать, повышать, стирать, расширять или переинтерпретировать, если meaning должен пережить смену representation и substrate?**

Law в этом документе — это **provisional meaning-level invariant**. Это не Python assertion, SQL constraint, Event verb, reducer rule, graph axiom, model prompt, serialization requirement, physical law и не утверждение об objective reality.

Слова `MUST`, `MUST NOT` и `REQUIRED` ниже описывают obligations именно этого **draft law set**. Final Canon они становятся только после independent и integrated A1–A10 review плюс последующего operator review, требуемого ADR-0025.

Этот draft сознательно не использует ранее ошибочный Notion-only label `nk-semantic-laws/0.1-draft`. Под этой identity никогда не существовало authoritative A4 law set. Этот файл — первый GitHub-resident A4 candidate и использует новую явную identity.

## 2. Тест допуска закона

Candidate входит в A4 только если выдерживает все следующие тесты:

1. **Meaning-preservation test:** нарушение способно молча изменить meaning представленной информации или силу её warrant.
2. **Substrate test:** statement выражается без обязательных Python, SQL, JSON, Event sourcing, graph, LLM, embeddings, digital bytes или конкретной processor model.
3. **Distinctness test:** это не просто A2 definition другими словами; law ограничивает то, что операции или mappings могут схлопнуть.
4. **Boundary test:** law не решает преждевременно detailed identity/time rules из A5, lifecycle rules из A6, conflict/revision algorithms из A7 или conformance thresholds из A8.
5. **Observable-obligation test:** profile способен сообщить, как он сохраняет, approximates, externalizes или не поддерживает law.
6. **Counterexample test:** существует хотя бы один failure case, раскрывающий нарушение.
7. **Revision test:** law остаётся versioned и falsifiable; A10 может ослабить, разделить, заменить или отклонить его.

## 3. Структура law set

First-draft set содержит **28 candidate laws**, организованных в шесть families:

```text
R — Representation and epistemic boundaries       A4-L01 … A4-L06
C — Context, provenance, and authority             A4-L07 … A4-L10
I — Identity, memory, time, and change             A4-L11 … A4-L19
T — Relations, conflict, and uncertainty           A4-L20 … A4-L22
V — Views, selection, and accountability           A4-L23 … A4-L25
S — Substrate, reproducibility, and conformance    A4-L26 … A4-L28
```

Число `28` не является сакральной целью. Это текущий deduplicated result reconciliation между A1 durable qualities, A2 non-equivalences, A3 machine obligations, существующими documentation targets NK-EPI и A4 plan. Integrated review может объединить или разделить laws, если их failure modes или observable obligations окажутся не независимыми.

## 4. Representation и epistemic boundaries

### A4-L01 — Representation не является represented reality

**Statement:** Representation, model, Record, State view, relation encoding или simulation MUST оставаться отличимыми от объекта, процесса, occurrence или relation, которые они представляют.

- **Rationale:** storage или успешное modelling могут сохранять полезную информацию, не устанавливая ontological identity с represented world.
- **Counterexample/falsifier:** map, graph edge или generated model ведут себя полезно, но позднее оказываются incomplete или wrong, тогда как represented situation существовала независимо.
- **Failure mode:** system рассматривает stored symbol или derived model как саму reality и передаёт downstream conclusions неоправданную certainty.
- **Observable obligation:** profiles MUST expose representation boundary и не описывать encoded presence как proof того, что represented state действительно holds.
- **Exception/open uncertainty:** A5/A8 могут разрешать identity claims в explicitly defined domains, но identity должна устанавливаться declared rule, а не предполагаться из representation.

### A4-L02 — Observation, Claim и explanation остаются различными

**Statement:** Observation MUST NOT молча становиться Claim, а Observation или Claim MUST NOT молча становиться complete explanation.

- **Rationale:** registration, assertion и explanation несут различную нагрузку warrant и transformation.
- **Counterexample/falsifier:** sensor сообщает temperature; interpretation делает вывод о comfort; causal explanation связывает temperature с failing system. Они могут различаться, пока initial reading не меняется.
- **Failure mode:** acquisition напрямую повышается до asserted meaning или causal narrative без сохранения interpretive step.
- **Observable obligation:** profiles MUST уметь различать registered, asserted, interpreted и explanatory position либо явно сообщать, что distinction unsupported.
- **Exception/open uncertainty:** domains могут operationally объединять steps, но combined operation должна показывать, какие semantic roles были collapsed и по какой declared policy.

### A4-L03 — Claim, admission и availability не являются objective truth

**Statement:** Существование, storage, admission, acceptance, availability или operational use Claim MUST NOT само по себе устанавливать, что Claim objectively true.

- **Rationale:** handling decisions и epistemic evaluation — разные типы authority.
- **Counterexample/falsifier:** admitted historical Claim позднее superseded более сильным Evidence, но остаётся historically accessible.
- **Failure mode:** `stored`, `admitted`, `approved` или `available` становятся hidden truth flag.
- **Observable obligation:** profile MUST сохранять rule/status, вызвавшие admission/disposition, отдельно от epistemic support и truth claims.
- **Exception/open uncertainty:** некоторые formal systems могут определять truth относительно closed formal interpretation; такая scoped truth relation всё равно должна отличаться от mere admission.

### A4-L04 — Evidence является scoped role; Source или repetition сами по себе не Evidence

**Statement:** Evidence MUST представляться как role относительно question, Proposition, Claim, Hypothesis или decision. Source identity, reputation, copying, frequency, popularity или repetition MUST NOT сами по себе создавать independent Evidence.

- **Rationale:** один и тот же material может быть relevant для одного question и irrelevant для другого, а copied reports могут иметь одну dependency lineage.
- **Counterexample/falsifier:** одна статья, скопированная на тысячу сайтов, остаётся dependent reporting, а не тысячей independent observations.
- **Failure mode:** evidence strength автоматически растёт с duplicate count или Source prestige без declared bearing и independence model.
- **Observable obligation:** profiles MUST сохранять target, direction/type of bearing, provenance/dependence, Context и uncertainty Evidence либо раскрывать loss.
- **Exception/open uncertainty:** domain-specific evidence aggregation отложена до later contracts; A4 запрещает только silent equivalence между repetition/Source и Evidence.

### A4-L05 — Belief, Hypothesis и Knowledge остаются различными; semantic promotion явный

**Statement:** Belief, Hypothesis, Knowledge-candidate и другие epistemic roles MUST NOT молча повышаться друг в друга. Любая promotion или withdrawal MUST указывать warranting policy, Context, Authority, support, uncertainty и relevant counterevidence.

- **Rationale:** sincerity, usefulness, plausibility, confidence или fluency несут не ту же epistemic burden, что Knowledge под declared standard.
- **Counterexample/falsifier:** agent sincerely верит false proposition; LLM возвращает fluent answer с high confidence, но weak provenance.
- **Failure mode:** model confidence, consensus, storage duration, repeated use или workflow stage становятся implicit knowledge gate.
- **Observable obligation:** profiles MUST expose prior и resulting epistemic role плюс rule/authority transition.
- **Exception/open uncertainty:** останется ли `Knowledge` final Canon concept или profile-defined status, явно deferred до integrated review.

### A4-L06 — Unknown, missing, unsupported, partial и failed не являются False

**Statement:** Absence of information, unanswered questions, unsupported capability, incomplete operations, indeterminacy или execution failure MUST NOT молча кодироваться как semantic falsehood.

- **Rationale:** отсутствие warrant для `true` не является warrant для `false`.
- **Counterexample/falsifier:** profile не может observe phenomenon и записывает `false`; позднее capable profile наблюдает его без изменения represented reality.
- **Failure mode:** booleans, empty collections, nulls, timeouts или unsupported features стирают distinction между unknown и false.
- **Observable obligation:** profiles MUST сохранять explicit unknown/partial/unsupported/failure boundary там, где distinction material.
- **Exception/open uncertainty:** closed-world domain MAY определять absence-as-false только если rule, scope, completeness assumption и authority explicit.

## 5. Context, provenance и authority

### A4-L07 — Meaning-relevant Context нельзя молча расширять или отбрасывать

**Statement:** Context dimensions, material для interpretation, validity, identity, relation semantics, authority или applicability, MUST оставаться attached или explicitly translated; narrower scoped position MUST NOT молча становиться universal.

- **Rationale:** одно expression может менять meaning между time, domain, jurisdiction, observer, assumptions, modality или task.
- **Counterexample/falsifier:** “it is safe” меняет truth value между dose или user; два temporal Claims кажутся contradictory только после удаления time scope.
- **Failure mode:** migration, summary, retrieval или normalization теряет scope и создаёт stronger или different Claim.
- **Observable obligation:** profiles MUST identify preserved Context, inferred Context, unknown Context и material loss/widening.
- **Exception/open uncertainty:** harmless Context omission domain-specific и должно оправдываться equivalence rule, а не предполагаться globally.

### A4-L08 — Provenance и provenance gaps остаются явными; transformation не является origin

**Statement:** Known origin, acquisition, custody, transformation, derivation и material provenance gaps MUST оставаться representable. Transformation, assembly, reconstruction, hash chain или successful reproduction MUST NOT сами по себе доказывать ultimate или original provenance.

- **Rationale:** continuity stories могут быть fabricated заполнением missing links удобными assumptions.
- **Counterexample/falsifier:** exact bytes подтверждают digest, пока authorship остаётся unknown; reconstructed artifact ведёт себя identically, но не устанавливает historical origin.
- **Failure mode:** missing lineage молча заменяется invented attribution, originlessness или preferred explanation.
- **Observable obligation:** profiles MUST expose known provenance links, contested alternatives, explicit gaps, transformation boundaries и completeness limits.
- **Exception/open uncertainty:** privacy-preserving provenance может намеренно скрывать details, но existence и scope hidden/redacted provenance должны отличаться от known completeness.

### A4-L09 — Authority является scoped и role-specific

**Statement:** Authority MUST представляться bounded by role, domain, Context, time, delegation и policy там, где material. Authority в одной role MUST NOT молча означать authority в другой; Source identity или technical permission MUST NOT становиться universal epistemic authority.

- **Rationale:** acquisition, interpretation, epistemic assessment, admission, relation, revision, access и conformance decisions имеют разные mandates.
- **Counterexample/falsifier:** administrator может удалить access, но не имеет authority объявить Claim false; sensor может быть authoritative measurement Source, но не policy authority.
- **Failure mode:** credentials, authorship, popularity или operator access становятся universal permission утверждать truth или переписывать meaning.
- **Observable obligation:** accountable operations MUST expose authority role и scope либо явно сообщать missing/contested authority.
- **Exception/open uncertainty:** profile может централизовать roles в одном actor, но role boundaries должны оставаться semantically identifiable.

### A4-L10 — Current inability не является universal impossibility

**Statement:** Failure текущего observer, method, profile, era или substrate observe, reproduce, represent, compute или verify что-либо MUST NOT молча становиться universal impossibility claim.

- **Rationale:** capability limits являются properties frames и methods, если не дан stronger formal argument.
- **Counterexample/falsifier:** earlier instrument не может resolve signal, который later instrument detects.
- **Failure mode:** `UNSUPPORTED`, `cannot verify` или `not observed` переписываются как `impossible` или `does not exist`.
- **Observable obligation:** impossibility claims MUST declare frame, assumptions, method и grounds; profile limits остаются profile limits.
- **Exception/open uncertainty:** formal impossibility/non-resolvability MAY быть represented внутри explicit formal system с assumptions и proof provenance.

## 6. Identity, memory, time и change

### A4-L11 — Semantic identity не является storage или physical identity

**Statement:** Semantic identity MUST NOT зависеть только от row identity, memory address, file path, process identity, storage location, database-generated identifier или другого substrate-local placement.

- **Rationale:** meaning должен переживать technology replacement, когда declared identity preserved.
- **Counterexample/falsifier:** Claim migrates из одного store в другой без изменения semantic referent или proposition.
- **Failure mode:** migration создаёт новую semantic entity только потому, что physical placement или backend identifier изменился.
- **Observable obligation:** profiles MUST state, какую identity relation они сохраняют и какие substrate-local identifiers non-semantic.
- **Exception/open uncertainty:** final semantic/content/Record/lineage identity rules принадлежат A5; A4 только запрещает unmarked collapse в physical identity.

### A4-L12 — Equal bytes, hashes или text сами по себе не доказывают semantic identity

**Statement:** Byte equality, hash equality, text equality или equivalent low-level representation MUST NOT сами по себе доказывать sameness semantic entity, Source, continuity, Record, Claim act или Context.

- **Rationale:** identical encodings могут относиться к разным contexts или independent occurrences, тогда как разные encodings могут выражать equivalent semantic content.
- **Counterexample/falsifier:** два Sources независимо выпускают identical text; одна sentence имеет разные referents в разных Contexts.
- **Failure mode:** deduplication объединяет distinct provenance/identity positions или рассматривает format change как semantic change.
- **Observable obligation:** любая equality-to-identity promotion MUST называть identity criterion и scope.
- **Exception/open uncertainty:** content-addressed profiles могут определить content-identity relation из bytes/hashes, но MUST NOT молча расширять её до всех остальных identity relations.

### A4-L13 — Memory не является merely Record, archive, retrieval или exact replay

**Statement:** Memory MUST NOT определяться исключительно как persistent Records, archive size, retrieval success, cache presence или exact replay capability.

- **Rationale:** continuity может быть structural, procedural, adaptive, distributed, analog, reconstructed, restricted или partially inaccessible.
- **Counterexample/falsifier:** unreadable backup bytes persist без usable continuity; adaptive analog system сохраняет influence prior states без discrete stored records.
- **Failure mode:** database или retrieval index сами определяют universal memory ontology.
- **Observable obligation:** profiles, claiming Memory equivalence, MUST state, какую continuity, reactivation/influence, transformation, access, uncertainty и forgetting boundary они сохраняют.
- **Exception/open uncertainty:** Memory primitive, emergent или family of contracts остаётся open для A5/A6/A8.

### A4-L14 — Material temporal dimensions остаются различимыми

**Statement:** Occurrence/valid time, Observation time, Record/knowledge time, decision time, write/commit order и другие materially different temporal relations MUST NOT молча схлопываться в один overloaded timestamp или version.

- **Rationale:** chronology represented world и chronology representation — разные relations.
- **Counterexample/falsifier:** correction Record timestamp сегодня не переносит historical occurrence на сегодня.
- **Failure mode:** migration или querying путают when something held с when it was learned или written.
- **Observable obligation:** profiles MUST preserve или explicitly translate temporal dimensions, required declared domain, и disclose loss.
- **Exception/open uncertainty:** exact temporal model, naming, partial-order semantics и identity effects принадлежат A5.

### A4-L15 — Imposed storage или write order не является автоматически order represented reality

**Statement:** Total order, imposed для serialization, storage, replication, locking или deterministic execution, MUST NOT представляться как occurrence, causal или semantic order, если эта relation отдельно не warranted.

- **Rationale:** concurrent или incomparable changes могут быть serialized implementation для convenience.
- **Counterexample/falsifier:** два independent observations записаны sequentially только потому, что database обязана выбрать commit order.
- **Failure mode:** implementation sequence создаёт causality или precedence в represented domain.
- **Observable obligation:** profiles MUST name order relation, которая recorded, и отличать unknown/concurrent/incomparable order там, где required.
- **Exception/open uncertainty:** A5/A8 определят minimum order relations и acceptable translation across substrates.

### A4-L16 — Revision и semantic Change сохраняют explicit lineage

**Statement:** Когда represented position revised, corrected, transformed или replaced, relation predecessor/successor MUST оставаться explicit либо должна фиксироваться explicit authorized forgetting/loss boundary.

- **Rationale:** accountable change требует знать, что изменилось относительно чего.
- **Counterexample/falsifier:** medical recommendation обновлена; новая recommendation current, пока старая остаётся historically meaningful.
- **Failure mode:** successive versions detached, делая audit, comparison, conflict analysis и provenance reconstruction ambiguous.
- **Observable obligation:** profiles MUST expose predecessor/successor или equivalent continuity, scope/reason/authority change либо disclose lineage unsupported/lost.
- **Exception/open uncertainty:** detailed branching, aliasing, migration, successor multiplicity и identity preservation rules принадлежат A5/A7 и не решают ADR-0024.

### A4-L17 — Revision не является silent overwrite

**Statement:** Semantic Revision MUST NOT представляться только как in-place replacement, делающий prior position неотличимой от состояния, где она никогда не существовала.

- **Rationale:** silent overwrite уничтожает evidence epistemic change и может fabricated более чистую historical narrative.
- **Counterexample/falsifier:** Claim меняется после contrary Evidence; later reader должен отличать revision от original unchanged Claim, если только authorized forgetting boundary не применяется.
- **Failure mode:** current value storage стирает fact, reason, authority или uncertainty change.
- **Observable obligation:** profiles MUST сохранять history visibility или A8-approved functional equivalent, sufficient отличить accountable revision от never-existed history.
- **Exception/open uncertainty:** A4 не требует append-only storage, Event sourcing, immutable bytes или permanent retention content, который policy законно требует forget.

### A4-L18 — Supersession не является deletion и не является falsity

**Statement:** Supersession MUST представлять scoped replacement или preference без silent implication, что predecessor erased, physically deleted, globally false или historically invalid.

- **Rationale:** older position может оставаться true как historical documentation, перестав governing current practice.
- **Counterexample/falsifier:** old standard superseded новой version, но остаётся accurate statement earlier standard.
- **Failure mode:** `superseded` трактуется как `false` или content disappearance, разрушая historical interpretation.
- **Observable obligation:** profiles MUST сохранять supersession scope/effective relation отдельно от deletion, restriction, truth assessment и historical access.
- **Exception/open uncertainty:** physical/cryptographic deletion и forgetting semantics остаются отдельными; reducer-v2 successor topology остаётся operator-controlled через Issue #74/ADR-0024.

### A4-L19 — Change representation не означает автоматически change represented occurrence

**Statement:** Correcting, migrating, re-encoding, reinterpreting, annotating или reclassifying representation MUST NOT само по себе утверждать, что represented object или historical occurrence изменились.

- **Rationale:** representational Change и represented Change — разные semantic relations.
- **Counterexample/falsifier:** исправление typo или timezone в Record меняет Record, оставляя original occurrence unchanged.
- **Failure mode:** metadata edits переписывают represented history или запускают false causal/temporal conclusions.
- **Observable obligation:** profiles MUST distinguish representational change от asserted change represented reality там, где difference matters.
- **Exception/open uncertainty:** некоторые operations намеренно меняют оба слоя; они должны заявить оба effects, а не выводить один из другого.

## 7. Relations, conflict и uncertainty

### A4-L20 — Relation representation не является represented relation reality; similarity сама по себе не semantic relation

**Statement:** Stored edge, association, co-occurrence, vector similarity, proximity score, shared identifier или inferred link MUST NOT молча становиться semantic Relation вроде `SAME_AS`, `CAUSES`, `SUPPORTS` или `CONTRADICTS` без declared interpretation, scope, provenance и authority.

- **Rationale:** access и representation mechanisms создают полезные associations, которые могут не hold в represented reality.
- **Counterexample/falsifier:** два documents являются embedding-neighbours, но обсуждают mutually unrelated causes.
- **Failure mode:** graph topology или retrieval similarity сами повышаются до ontological или causal truth.
- **Observable obligation:** profiles MUST identify relation type/roles/direction/scope и whether it is asserted, observed, inferred или merely access-derived.
- **Exception/open uncertainty:** domain relation vocabularies и topology constraints deferred до contracts/A7/A8.

### A4-L21 — Conflict не обязательно Contradiction; scope должен быть aligned

**Statement:** Conflict MUST NOT классифицироваться как strict Contradiction, пока relevant interpretation, scope, time, modality, assumptions и compared propositions недостаточно aligned для warranted incompatibility.

- **Rationale:** tension может возникать из evidence, goals, authority, context mismatch или temporal change без logical negation.
- **Counterexample/falsifier:** “open at 09:00” и “closed at 10:00” различаются, но не contradictory under aligned time.
- **Failure mode:** detectors создают contradictions, отбрасывая Context или считая low similarity/difference negation.
- **Observable obligation:** contradiction assessments MUST expose alignment basis и uncertainty; broader conflicts остаются typed как conflicts.
- **Exception/open uncertainty:** logic family, graded contradiction, paraconsistency и domain conflict taxonomies принадлежат A7.

### A4-L22 — Conflict detection не является conflict resolution; unresolved plurality остаётся видимой

**Statement:** Detecting Conflict, Contradiction, competing Evidence, authority disagreement или unresolved plurality MUST NOT молча выбирать winner, усреднять positions, удалять alternatives или imply resolution.

- **Rationale:** detection и resolution требуют different authority и warrant.
- **Counterexample/falsifier:** два credible observations остаются unresolved, потому что available Evidence не discriminates между ними.
- **Failure mode:** ranker, reducer, majority vote, newest-write rule или model confidence молча закрывают conflict.
- **Observable obligation:** profiles MUST сохранять unresolved participants, conflict basis, uncertainty и resolution status до authorized resolution/revision.
- **Exception/open uncertainty:** resolution strategies, reversibility и belief revision — responsibilities A7.

## 8. Views, selection и accountability

### A4-L23 — Derived views не переписывают history и не становятся universal State

**Statement:** Projection, summary, cache, index, query result, reconstructed view или другой derived State MUST оставаться linked к inputs/method/scope и MUST NOT молча заменять represented history или объявлять себя one complete world State.

- **Rationale:** derived material shaped selection, abstraction, staleness и method.
- **Counterexample/falsifier:** две legitimate queries выводят разные scoped State views из одного retained material.
- **Failure mode:** disposable projection становится authoritative, потому что она fast, convenient, current-looking или deterministic.
- **Observable obligation:** profiles MUST disclose derivation scope, inputs, method/profile, material omissions, staleness/uncertainty и reconstruction/equivalence boundary.
- **Exception/open uncertainty:** reconstructability через replay, recomputation, reversible dynamics или иной functional equivalent deferred до A8.

### A4-L24 — Retrieval, ranking, selection, utility, recency и disposition не являются epistemic validity

**Statement:** Relevance, similarity, rank, activation, frequency of use, utility outcome, recency, operational availability, admission, quarantine или selection MUST NOT independently определять, является ли Claim epistemically valid или Knowledge.

- **Rationale:** access optimization и task usefulness отвечают на другие questions, чем support и truth.
- **Counterexample/falsifier:** top search result obsolete или false; useful heuristic works, опираясь на false explanation.
- **Failure mode:** retrieval score, “charge”, newest-write, user preference или successful outcome становятся hidden evidence.
- **Observable obligation:** profiles MUST keep selection/disposition signals distinct от epistemic assessments и preserve unsupported/contested labels через selection.
- **Exception/open uncertainty:** Evidence utility может bear на practical Claims, если explicitly modelled как Evidence этого question; utility не является evidence unrelated truth Claims by default.

### A4-L25 — Receipt и bounded accountability не являются correctness, completeness или truth

**Statement:** Receipt, audit record, explanation, trace, proof-of-execution или reproducibility record MUST NOT certify semantic truth, task sufficiency, completeness, compliance или correctness лишь своим существованием.

- **Rationale:** perfectly recorded process может выполнять flawed method, omit relevant inputs или действовать по false Claims.
- **Counterexample/falsifier:** deterministic Receipt faithfully records selection, пропустившую critical Evidence.
- **Failure mode:** auditability путается с correctness, а partial failures или exclusions исчезают из account.
- **Observable obligation:** accountability outputs MUST state scope, inputs, methods, exclusions, authority, failures, uncertainty и known limitations where material.
- **Exception/open uncertainty:** stronger proofs/certificates могут быть defined later contracts, но их exact claim boundary должна быть explicit и separately evidenced.

## 9. Substrate, reproducibility и conformance

### A4-L26 — History visibility required; Event sourcing, reducer replay и global total order не universal mechanisms

**Statement:** Profile MUST preserve enough change/history visibility, чтобы отличать accountable revision, lineage и relevant prior positions, либо explicitly disclose inability. A4 **не** требует Event sourcing, append-only serialized logs, reducer replay, immutable rows или one global total order как universal mechanisms.

- **Rationale:** history visibility — semantic objective; current Event/reducer machinery — лишь одна implementation strategy.
- **Counterexample/falsifier:** manual archival process или adaptive substrate сохраняет accountable prior-state relations без serialized Events.
- **Failure mode:** P1–C5 mechanics копируются в Canon по inertia, исключая materially different substrates, способные сохранять ту же obligation.
- **Observable obligation:** profiles MUST state functional mechanism, через который relevant prior positions/change lineage remain inspectable, и какие history information могут быть lost или forgotten.
- **Exception/open uncertainty:** minimum portable history commitment, replay/reconstruction equivalents и lawful forgetting trade-offs принадлежат A8/A10.

### A4-L27 — Determinism и reproducibility не являются truth или physical identity; equivalence named

**Statement:** Deterministic execution MUST NOT imply true output. Reproducibility MUST NOT требовать identical physical states или bytes, если named profile этого не требует. Любой cross-run или cross-substrate equivalence claim MUST state observables, tolerated variation, ordering assumptions, uncertainty и loss.

- **Rationale:** deterministic procedures могут deterministically обрабатывать false inputs, тогда как probabilistic/analog systems могут сохранять declared semantic equivalence без bit identity.
- **Counterexample/falsifier:** два substrates дают semantically equivalent bounded outcomes через разные physical states; deterministic algorithm повторяет одну wrong classification.
- **Failure mode:** byte identity рассматривается как единственная conformance model либо deterministic output повышается до truth.
- **Observable obligation:** profiles MUST name equivalence relation и disclose non-equivalence/irreproducibility вместо generic sameness.
- **Exception/open uncertainty:** concrete equivalence levels и thresholds принадлежат A8.

### A4-L28 — Optimization, migration и profile substitution не должны молча менять meaning; conformance не production authorization

**Statement:** Performance optimization, compression, migration, storage replacement, language/runtime change, model substitution, hardware change или profile replacement MUST NOT молча изменять accepted semantic distinctions или obligations. Любые meaning change, approximation, unsupported capability или loss MUST быть declared. Passing named conformance profile MUST NOT само по себе imply production readiness или universal substrate support.

- **Rationale:** technology replacement — central stress test Native Kernel; optimization pressure не должна становиться semantic authority.
- **Counterexample/falsifier:** faster index теряет provenance/conflict status; migrated system сохраняет content, но схлопывает `unknown` в `false`.
- **Failure mode:** semantic drift скрывается как backend migration, optimization или “equivalent” implementation change.
- **Observable obligation:** migration/profile reports MUST identify preserved obligations, approximations, losses, unsupported laws и named equivalence/conformance scope.
- **Exception/open uncertainty:** A8 определяет formal substrate-independence contract и conformance levels; production authorization остаётся отдельным governance/evidence decision.

## 10. Cross-law consequences

Law set подразумевает несколько higher-level disciplines, не создавая новых independent laws:

```text
stored          ≠ true
selected        ≠ valid
newer           ≠ more correct
deterministic   ≠ true
audited         ≠ correct
superseded      ≠ false
unavailable     ≠ nonexistent
unsupported     ≠ impossible
same bytes      ≠ same semantic identity
same meaning    ≠ same physical representation
history visible ≠ mandatory Event sourcing
conformant      ≠ production-authorized
```

Эти compact formulas — explanatory aliases. Numbered `A4-Lxx` statements являются authoritative units этого draft.

## 11. Связь с A2 ontology

A4 не заменяет A2 definitions. Он ограничивает, как A2 roles могут transformed или collapsed:

| A2 area | Principal A4 laws |
|---|---|
| Signal / Observation / Record | L01, L02, L06, L19 |
| Proposition / Claim / Interpretation | L01–L03, L05, L07 |
| Hypothesis / Belief / Knowledge / Evidence / Uncertainty | L04–L06, L22, L24 |
| Source / Provenance / Context / Authority | L07–L10 |
| Memory / State / Change / Event / Revision / Supersession | L11–L19, L23, L26 |
| Relation / Conflict / Contradiction | L20–L22 |
| Receipt | L25 |

Этот mapping не делает каждую A2 classification final.

## 12. Связь с A3 abstract machine

Laws ограничивают A3 transition families, не превращая их в APIs или Event verbs:

| A3 transition family | Principal A4 laws |
|---|---|
| `ENCOUNTER` / `REGISTER` | L01, L02, L06–L08, L11–L13 |
| `IDENTIFY_OR_DISTINGUISH` | L07, L11, L12, L14, L15 |
| `BIND_SCOPE_AND_ORIGIN` | L07–L10 |
| `INTERPRET_AND_CLASSIFY_ROLE` | L01–L07 |
| `ASSESS_EPISTEMIC_POSITION` | L03–L06, L09, L24 |
| `DECIDE_DISPOSITION` | L03, L06, L09, L24 |
| `RELATE` | L01, L07, L20 |
| `DETECT_TENSION` | L06, L07, L21, L22 |
| `REVISE_OR_SUPERSEDE` | L14–L19, L22, L26 |
| `DERIVE_BOUNDED_VIEW` | L23, L26–L28 |
| `SELECT_FOR_USE` | L03–L06, L24, L25 |
| `ACCOUNT` | L25, L27, L28 |

Profile может combine transitions, но не может claim full preservation, молча нарушая law, relevant combined operation.

## 13. Контрастные substrate thought experiments

### 13.1 Manual archival and review process

Human-operated archive может сохранять A4 obligations через labelled documents, provenance sheets, scoped authority, revision ledgers, uncertainty markers и explicit conflict files. У него может не быть SQL, hashes, reducer или replay engine. Он fails A4 там, где required distinctions/accountability становятся uninspectable, а не потому, что у него нет digital Event sourcing.

### 13.2 Adaptive analog or neuromorphic substrate

Adaptive physical system может сохранять continuity и influence prior states без discrete Records каждого transition. Чтобы claim A4 preservation, он всё равно должен expose или externally account materially required distinctions — uncertainty, authority, provenance gaps, revision lineage или declared loss — через accepted functional mapping. Exact byte replay не предполагается.

### 13.3 Conventional digital Event-sourced laboratory

Текущий P1–C5 Python/PostgreSQL/SQLite lineage может map многие A4 obligations через Events, reducer state, projections, Receipts и explicit profiles. Этот mapping остаётся bounded laboratory. Его Event vocabulary, serialization, global/local sequencing, SQL schemas и reducer mechanics не повышаются до A4 laws только потому, что executable сегодня.

## 14. Failure patterns, которые должен раскрывать A4

Profile или document нарушает intent этого draft, когда он:

- equates persistence с truth или Knowledge;
- fabricates Source/Context/provenance ради schema;
- превращает `unknown`, `unsupported` или failure в `false`;
- treats repetition, popularity, model confidence, relevance, recency или utility как Evidence сами по себе;
- merges semantic identity с backend identity;
- treats write order как reality/causal order;
- rewrites prior epistemic positions без accountable lineage;
- equates Supersession с deletion или falsity;
- turns similarity или stored edges в semantic/causal Relations без interpretation;
- detects Conflict и молча resolves его;
- lets projections или summaries become authoritative history;
- treats Receipts или deterministic replay как correctness proof;
- requires Event sourcing только потому, что reference laboratory его использует;
- claims substrate neutrality без named preserved obligations и disclosed loss;
- treats conformance или test success как production authorization.

## 15. Что A4 сознательно оставляет later deliverables

A4 не решает:

- exact semantic/content/Record/lineage identity rules (`A5`);
- exact temporal algebra, clock model, valid-time model или concurrency model (`A5`);
- lifecycle state names и transitions (`A6`);
- conflict-resolution, uncertainty-combination или belief-revision algorithms (`A7`);
- formal equivalence levels, portability thresholds, replay/reconstruction requirements или conformance profiles (`A8`);
- module-by-module classification P1–C5 (`A9`);
- final falsification program или unresolved architectural questions (`A10`);
- reducer-v2 referential rules, cycle semantics или migration policy (`Issue #74 / ADR-0024`);
- license/publication terms (`Issue #18`);
- Track H historical-source admission;
- runtime implementation, new Event vocabulary, new databases, independent-language ports, LLM/vector adapters, ecosystem integration, maturity promotion или production authorization.

## 16. Review и falsification questions

Integrated review должен challenge как минимум:

1. Являются ли какие-либо два A4 laws observationally indistinguishable и поэтому duplicates?
2. Не smuggles ли какой-либо law Event-sourcing, database, serialization, digital или processor assumption в Canon?
3. Могут ли manual/procedural и non-digital/adaptive mapping оба сохранить law без pretend identical mechanics?
4. Не принадлежит ли какой-либо law полностью A5–A8 вместо ограничения этих deliverables?
5. Может ли system нарушить law и всё равно выглядеть locally successful? Если нет, law может быть unfalsifiable или vacuous.
6. Конфликтует ли lawful forgetting с history/accountability requirements и explicit ли boundary?
7. Не трактуются ли `Knowledge`, `Memory`, `State` или `Event` как более final, чем разрешает A2?
8. Может ли profile честно сообщить `UNSUPPORTED`, не будучи ошибочно classified как `false` или globally non-conforming вне named level?

## 17. Non-claims

```text
28 candidate laws ≠ eternal or final law count
A4 draft ≠ independently approved Canon
semantic law ≠ runtime assertion
A4-Lxx ≠ executable NK-EPI support
history visibility ≠ mandatory Event sourcing
identity law ≠ hash/serialization identity specification
revision law ≠ reducer-v2 authorization
substrate-neutral statement ≠ demonstrated arbitrary-substrate support
profile conformance ≠ production authorization
this document ≠ decision on Issue #18 or ADR-0024
```

Существующий assertion map остаётся `45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED`. `NK-EPI` остаётся `0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED`. A4 documentation не повышает ни один из них.

## 18. Status

```text
deliverable: A4_SEMANTIC_LAWS_AND_INVARIANTS
law_set: nk-semantic-laws/A4-draft-1
law_count: 28
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
review: PENDING independent review and integrated blueprint review with A1-A3 and A5-A10
next_content_slice: A5_IDENTITY_TIME_AND_CHANGE
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```
