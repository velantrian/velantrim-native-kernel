# ⚖️ A7 — Конфликт, неопределённость и пересмотр

**[English](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) · [Русский](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md)**

> **Deliverable:** `A7_CONFLICT_UNCERTAINTY_AND_REVISION` blueprint [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.ru.md) по `ADR-0025` / [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Зависит от:** provisional A1–A6, особенно A3 `DETECT_TENSION` / `REVISE_OR_SUPERSEDE`, A4-L21/L22/L24, A5 identity/time/change и A6 `IN_TENSION` / `REVISED_OR_SUPERSEDED`  
> **Согласуется с:** accepted-семейством `NK-CFL` в `foundational-skeleton/1.0`; proposed ADR-0003 остаётся `PROPOSED`, ADR-0024 остаётся `PROPOSED / PENDING_OPERATOR`  
> **Evidence boundary:** только architecture research и provisional semantic obligations; никаких изменений runtime, acceptance контрактов, evidence, assertion-map, NK-EPI, maturity или production  
> **Review status:** первый drafted slice; ожидает independent review и integrated A1–A10 review

```text
model_id: nk-conflict-uncertainty-revision/A7-draft-1
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
next_content_slice: A8_SUBSTRATE_INDEPENDENCE_CONTRACT
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
ADR-0003 decision status: PROPOSED / UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```

## 1. Назначение и граница полномочий

A7 отвечает на один ограниченный вопрос:

> Как Native Kernel может представлять напряжение, неопределённость, конкурирующие позиции и обоснованный пересмотр, не превращая обнаружение в решение, неизвестность — в ложь, а удобный алгоритм — в semantic authority?

A7 — не универсальный truth engine и не модуль, который обязан всегда выбирать победителя. Корректным результатом может быть длительное `UNRESOLVED`, если недостаточно Evidence, Context, identity, interpretation, provenance, capability или Authority.

Обязательные non-equivalences:

```text
Conflict ≠ necessarily Contradiction
candidate tension ≠ established tension
established tension ≠ resolved tension
detection ≠ resolution
resolution-for-scope ≠ objective truth
Authority to resolve ≠ Authority to assert truth
uncertainty ≠ one universal confidence scalar
confidence score ≠ Evidence
newer ≠ more correct
majority ≠ truth
write order ≠ semantic precedence
retrieval rank ≠ epistemic validity
Revision ≠ silent overwrite
Supersession ≠ falsity or deletion
unresolved ≠ failed
unknown ≠ false
```

A7 уточняет accepted semantic boundary `NK-CFL`. Он не принимает ADR-0003, не разрешает Event verbs `CONFLICT_OPENED` / `CONFLICT_RESOLVED`, не реализует reducer-v2, не выбирает LWW/CRDT/OCC/CAS и не требует Bayesian, Dempster–Shafer, AGM, LLM, vector, SQL, graph или digital implementation.

## 2. Статус модели и правило допуска

Концепт A7 допустим только если он:

1. сохраняет A2-различия между Conflict, Contradiction, Uncertainty, Evidence, Authority, Revision и Supersession;
2. отображается на A3 transition obligations, не становясь обязательным API/Event/reducer-state;
3. соблюдает A4-L21, A4-L22 и A4-L24;
4. сохраняет A5 identity, temporal scope, order и explicit revision lineage;
5. согласуется с A6 lifecycle positions без создания второго lifecycle;
6. остаётся осмысленным на manual/procedural, adaptive/non-digital и conventional digital substrates;
7. содержит counterexamples и условия, при которых правильнее остаться undecided;
8. не решает молча ADR-0003, ADR-0024, Issue #18 или Track H.

Поэтому модель — это набор typed semantic positions и accountable decision relations, а не один обязательный conflict-object или числовой uncertainty calculus.

## 3. Три независимые оси напряжения

A7 хранит независимыми три оси:

```text
tension kind
    ≠
assessment status
    ≠
resolution status
```

### 3.1 Статус установления

| Status | Значение | Явная non-equivalence |
|---|---|---|
| `CANDIDATE` | материал указывает на возможное напряжение, но alignment/basis неполны | candidate ≠ established |
| `ESTABLISHED` | declared method/Authority имеет достаточные alignment и basis для данного tension kind | established ≠ resolved |
| `NOT_A_CONFLICT` | review показывает совместимость или apparent tension исчезает после исправления scope/identity/interpretation | not-a-conflict ≠ одна сторона false |
| `UNRESOLVED_ASSESSMENT` | Kernel не может обоснованно ни установить tension, ни снять его | unresolved assessment ≠ false |

`ESTABLISHED` всегда scoped к declared method, Context, identity relation, temporal alignment и Authority; это не универсальное метафизическое утверждение.

### 3.2 Статус решения

| Status | Значение | Явная non-equivalence |
|---|---|---|
| `UNRESOLVED` | authorized и warranted resolution не представлено | unresolved ≠ failure |
| `DEFERRED` | Authority/policy явно откладывает решение до условия, review или Evidence | deferred ≠ forgotten |
| `RESOLVED_FOR_SCOPE` | accountable decision определяет обработку tension для конкретного purpose/Context | resolved-for-scope ≠ objective truth |
| `REOPENED` | прежнее scoped resolution снова рассматривается из-за изменения basis, Context, Evidence, identity, policy или Authority | reopened ≠ history rewrite |

Профиль может кодировать эти смыслы иначе, но не должен сворачивать их в один `conflict=true/false` или `resolved=true/false`, когда различие существенно.

## 4. Таксономия напряжений

A7 уточняет accepted-инвентарь `NK-CFL` в provisional tension kinds:

| Tension kind | Главный вопрос | Default semantic handling |
|---|---|---|
| `DUPLICATE_DELIVERY` | повторно ли наблюдается тот же command/record/transition attempt? | применить idempotency/identity policy; repetition не создаёт epistemic conflict |
| `WRITE_VERSION_RACE` | несовместимы ли concurrent technical writes по profile contract? | хранить technical collision отдельно от semantic truth |
| `DIVERGENT_HISTORY` | расходятся ли lineages после declared common ancestor? | сохранять branches/provenance; merge policy explicit |
| `SEMANTIC_CONTRADICTION` | не могут ли aligned propositions/commitments совместно выполняться? | требуются aligned interpretation, scope, time, modality, assumptions |
| `TEMPORAL_MISMATCH` | вызвана ли apparent incompatibility разными temporal scopes/orders? | выровнять время до объявления contradiction |
| `SCOPE_MISMATCH` | сравниваются ли позиции вне совместимых Context/domain/jurisdiction/quantification? | сохранить scopes; false conflict может исчезнуть |
| `PROVENANCE_CONFLICT` | materially расходятся ли origin/custody/transformation accounts? | сохранить alternatives/gaps; не выдумывать continuity |
| `MEASUREMENT_DISAGREEMENT` | расходятся ли observations/measurements при разных method/frame/uncertainty? | сохранить method/frame и measurement uncertainty |
| `AUTHORITY_CONFLICT` | дают ли scoped Authorities несовместимые decisions или claims об authority? | показать role/scope/delegation; credentials не дают universal winner |
| `POLICY_CONFLICT` | требуют ли overlapping policies несовместимой обработки? | сравнить policy/version/effective scope |
| `EPISTEMIC_DISAGREEMENT` | различаются ли support/belief/hypothesis/knowledge positions без строгой contradiction? | сохранить разные Evidence/warrant positions |
| `PROJECTION_DRIFT` | расходится ли derived view с authoritative inputs/reconstruction contract? | derived-view integrity problem; history не переписывать |
| `UNCLASSIFIED_TENSION` | видно ли tension, которое пока нельзя безопасно классифицировать? | оставить explicit unknown, не форсировать class |

В taxonomy намеренно соседствуют technical и semantic tensions: архитектура должна сначала различить их. Technical collision не становится semantic contradiction, а semantic contradiction не сводится к storage ordering.

## 5. Alignment до Contradiction

`SEMANTIC_CONTRADICTION` требует достаточного alignment материально значимых измерений:

```text
semantic content / proposition identity
interpretation
Context and scope
temporal scope
modality / quantification
assumptions
referent or identity relation
Authority of the assessment
known uncertainty
```

Если alignment отсутствует, A7 требует `CANDIDATE`, `UNRESOLVED_ASSESSMENT` или более точный mismatch — например `TEMPORAL_MISMATCH` / `SCOPE_MISMATCH`.

Примеры:

- “door open at 09:00” и “door closed at 10:00” не contradiction только из-за различия текста;
- два temperature measurements могут расходиться из-за method, calibration, location или time;
- две policies могут конфликтовать operationally, хотя ни одна не является truth claim;
- два Sources могут иметь разные epistemic positions без logical negation.

Detector, который удаляет alignment Context и затем объявляет contradiction, нарушает A4-L21.

## 6. Typed uncertainty positions

A7 не определяет uncertainty одним scalar. Provisional relation:

```text
UNCERTAINTY_POSITION(
  subject_or_question,
  uncertainty_kind,
  basis_or_gap,
  context,
  provenance,
  temporal_binding,
  authority_or_method,
  dependency_information,
  status
)
```

Candidate uncertainty kinds:

| Kind | Значение |
|---|---|
| `EVIDENCE_GAP` | relevant support/challenge material отсутствует или недостаточен |
| `PROVENANCE_GAP` | origin/custody/transformation неполны или contested |
| `CONTEXT_GAP` | interpretation/applicability не хватает material scope |
| `TEMPORAL_GAP` | valid/occurrence/observation/assertion/effective timing недостаточно известен |
| `IDENTITY_GAP` | relevant A5 identity relation unresolved |
| `INTERPRETATION_GAP` | остаётся несколько material interpretations |
| `AUTHORITY_GAP` | нет adequate или uncontested Authority для решения |
| `CAPABILITY_GAP` | profile/observer не способен выполнить нужное discrimination |
| `DEPENDENCY_UNCERTAINTY` | independence/dependence Evidence неизвестна или частична |
| `MEASUREMENT_UNCERTAINTY` | measurement содержит declared method/frame/error/range limits |
| `UNCLASSIFIED_UNCERTAINTY` | uncertainty известно, но пока небезопасно классифицировать |

Probability, confidence score, interval, possibility set, qualitative label, physical distribution, human judgment или иной метод может представлять часть uncertainty position, но должен объяснять meaning, dependencies и limits. Model confidence не становится автоматически Evidence или Authority.

### 6.1 Комбинирование uncertainty

A7 намеренно не задаёт universal combination algebra. Комбинация требует named method/profile и сохранения materially relevant dependence/provenance:

```text
copied Evidence ≠ independent Evidence
multiple confidence values ≠ automatically combinable probabilities
missing evidence ≠ negative evidence
```

Если метод не оправдывает combined result, корректный outcome — explicit unresolved или partial position.

## 7. Tension position / семантический паттерн Conflict Set

A7 уточняет accepted `NK-CFL` Conflict Set pattern, не делая его обязательным root entity:

```text
TENSION_POSITION(
  tension_ref,
  participants,
  tension_kind,
  assessment_status,
  alignment_context,
  basis,
  provenance,
  temporal_scope,
  uncertainty_positions,
  detection_authority_or_method,
  resolution_status,
  resolution_ref_or_none
)
```

Minimum obligations:

- participants различимы по relevant A5 identity relations;
- detection basis и alignment assumptions inspectable;
- candidate/established/not-a-conflict/unresolved assessment не смешиваются;
- unresolved Evidence/provenance/Context/identity/Authority gaps остаются видимыми;
- resolution state не удаляет pre-resolution tension;
- reopening ссылается на prior resolution без overwrite;
- Receipt учитывает detection/resolution, но не доказывает truth.

Future profile может реализовать pattern records, relations, case file, dynamic state, distributed structure или другим declared equivalent.

## 8. Границы Authority для detection и resolution

A7 различает как минимум:

```text
detection Authority / method
≠ resolution Authority
≠ epistemic-assessment Authority
≠ operational-disposition Authority
≠ architecture/governance Authority
```

Method может deterministic обнаружить profile invariant violation без semantic resolution authority. Human reviewer может решать legal/operational policy в своей jurisdiction, не превращая спорное scientific proposition в objective truth. Operator может approve architecture decision без создания empirical Evidence.

Accountable `RESOLVED_FOR_SCOPE` должен называть, где применимо:

- tension;
- Authority role, actor/method, delegation, policy/version;
- purpose и Context;
- basis и Evidence;
- material exclusions/counterevidence;
- effective temporal scope;
- remaining uncertainty;
- resulting positions/handling;
- reversibility/review/reopening conditions;
- Receipt/accountability boundary.

Если adequate Authority отсутствует, `UNRESOLVED` или `DEFERRED` предпочтительнее invented authority.

## 9. Режимы решения без универсального winner algorithm

A7 допускает несколько meaning-level resolution modes:

| Mode | Значение | Boundary |
|---|---|---|
| `DISSOLVE_BY_ALIGNMENT` | corrected identity/time/scope/interpretation показывает, что apparent conflict не применим | не объявляет participant false |
| `RETAIN_PLURALITY` | несколько positions остаются представлены, потому что stronger warrant отсутствует или plurality легитимна | plurality ≠ merge |
| `PREFER_FOR_SCOPE` | Authority выбирает position для named purpose, сохраняя alternatives visible | preference ≠ universal truth |
| `REVISE_POSITION` | prior semantic/epistemic position изменяется с A5 lineage | revision ≠ overwrite |
| `SUPERSEDE_FOR_SCOPE` | successor заменяет predecessor для declared scope/effective time | supersession ≠ deletion/falsity; topology остаётся ADR-0024 |
| `DEFER_DECISION` | resolution отложено с reason/review condition | deferral ≠ failure |
| `NO_AUTHORIZED_RESOLUTION` | явно зафиксировано отсутствие достаточной Authority | no authority ≠ false |

Это semantic categories, не Event verbs и не mandatory enums. Mathematical merge, CRDT-like mechanism, voting, rules, proof, statistical inference, human review и другие техники допустимы лишь при explicit semantics/loss; technique не получает truth authority из факта implementation.

## 10. Revision и изменение belief/epistemic position

A7 уточняет A5 revision discipline:

```text
EPISTEMIC_REVISION(
  target,
  prior_position,
  resulting_position,
  tension_refs,
  basis_and_counterevidence,
  policy_or_method,
  authority,
  context,
  temporal_binding,
  uncertainty_before_after,
  identity_effect,
  reversibility
)
```

A7 не требует scalar belief strength или universal belief-revision calculus. Resulting position может strengthen, weaken, suspend, retain, retract, replace-for-scope или оставаться unresolved по declared domain policy; это descriptions, не mandatory enum.

Обязательные дисциплины:

- new Evidence может менять epistemic position, не меняя Observation/Record;
- changed Interpretation может revise Claim/Belief при сохранении исходного material;
- retraction не удаляет prior history;
- resolution decision может быть operationally binding и при этом epistemically uncertain;
- Authority может разрешить revision по policy, не доказывая proposition true;
- copied/repeated Claims не получают warrant от количества;
- revision сохраняет predecessor/successor lineage или явно использует authorized forgetting boundary.

Ни одно правило A7 не меняет `nk-p1-reducer/1` и не решает reducer-v2 successor/cycle rules.

## 11. Reversibility, reopening и право остаться undecided

A7 требует возможности оставаться undecided и, где существенно, reopen prior decision.

Resolution должно объявлять, является ли оно:

- reviewable/reversible при новых Evidence/Context;
- final только для named operational/legal/policy scope;
- irreversible по specific governing rule, причём irreversibility itself scoped/accountable.

`REOPENED` сохраняет prior `RESOLVED_FOR_SCOPE` и объясняет, почему прежнего basis недостаточно. Trigger может быть new Evidence, corrected provenance, changed identity alignment, policy, expired Authority, new capability или discovered omission.

Архитектура должна уметь выразить:

```text
“We do not currently know.”
“We cannot currently discriminate.”
“Both positions remain live for different scopes.”
“No authorized resolution exists.”
“The previous scoped resolution is under review.”
```

Отсутствие единственного winner не является failure Kernel.

## 12. Связь с A6 lifecycle

A7 не меняет девять phases A6, а уточняет переходы вокруг `IN_TENSION`, `EPISTEMICALLY_WEIGHED` и `REVISED_OR_SUPERSEDED`:

```text
DETECT_TENSION
    ↓
IN_TENSION
    ├─ insufficient basis/authority ──→ remain IN_TENSION / UNRESOLVED
    ├─ scope/time alignment dissolves tension ──→ RELATIONALLY_INTEGRATED or EPISTEMICALLY_WEIGHED
    ├─ scoped preference without semantic revision ──→ RELATIONALLY_INTEGRATED + resolution record
    └─ actual revision/supersession ──→ REVISED_OR_SUPERSEDED
```

Границы:

- `RESOLVED_FOR_SCOPE` не означает автоматически `REVISED_OR_SUPERSEDED`;
- `REVISED_OR_SUPERSEDED` требует A5 predecessor/successor или revised-position lineage;
- `ACCOUNT` может создать Receipt, но `ACCOUNTED ≠ true/correct`;
- tension может оставаться open indefinitely;
- reopening не стирает earlier lifecycle history.

## 13. Связь с существующими contracts, ADRs и reference laboratory

### 13.1 Accepted `NK-CFL`

A7 уточняет accepted family `NK-CFL` (`foundational-skeleton/1.0`), сохраняет `NK-CFL-001`…`NK-CFL-008` и детализирует candidate/established, uncertainty gaps, resolution Authority и reopening/revision. Это не создаёт executable support для assertions.

### 13.2 Proposed ADR-0003

ADR-0003 остаётся `PROPOSED / NOT_STARTED`. A7 использует совместимые research concepts — explicit conflict visibility и detection ≠ resolution — но не меняет decision status ADR-0003 и не принимает его proposed Conflict Set/Event lifecycle vocabulary.

### 13.3 Issue #74 / ADR-0024

A7 не решает:

- one-successor vs multi-successor Supersession topology;
- self-supersession;
- successor cycles;
- reducer-v2 version dispatch/migration.

Всё это остаётся Issue #74 / ADR-0024 `PROPOSED / PENDING_OPERATOR`. A7 требует лишь, чтобы future mechanism сохранял declared conflict/revision semantics/history.

### 13.4 P1–C5 bounded reference laboratory

В P1–C5 нет accepted A7 conflict lifecycle runtime. Event vocabulary остаётся:

```text
ADMIT · LINK · UTILIZED · SUPERSEDED · ERASED
```

`CONFLICT_OPENED`, `CONFLICT_REVIEWED`, `CONFLICT_RESOLVED`, `CONFLICT_REOPENED` не authorized Event verbs. `SUPERSEDED` остаётся laboratory mechanism в границах reducer-v1 evidence / Issue #74. Projection drift — derived-view integrity concept; A7 не меняет projection runtime.

Следовательно A7 — documentation/blueprint evidence, не runtime conformance evidence.

## 14. Failure и indeterminacy cases

A7 нарушается, если profile/future contract молча:

- превращает candidate tension в established без alignment/basis;
- превращает `UNRESOLVED_ASSESSMENT` или `UNRESOLVED` в false;
- выбирает winner только по newest write, highest rank, majority count, model confidence, storage order или retrieval relevance;
- объявляет temporal/scope mismatch contradiction после потери Context;
- усредняет incompatible positions и удаляет participants/provenance;
- выдумывает provenance/Authority ради заполнения поля;
- считает copied Evidence independent без dependence rule;
- использует uncertainty scalar без объяснения meaning/dependencies;
- resolves conflict без scope, basis, Authority и remaining uncertainty;
- overwrite prior positions/resolution вместо revision/reopening lineage;
- считает `RESOLVED_FOR_SCOPE` universal truth;
- считает `SUPERSEDE_FOR_SCOPE` deletion/falsity;
- импортирует ADR-0024 topology или proposed ADR-0003 Event names как accepted runtime;
- считает successful deterministic resolver proof of semantic correctness.

`UNKNOWN`, `PARTIAL`, `UNSUPPORTED`, `NO_AUTHORIZED_RESOLUTION` и long-lived unresolved plurality — legitimate outcomes.

## 15. Контрастные mappings на разные substrates

### Manual archival and review process

Review board хранит testimony/evidence packets раздельно, открывает conflict sheet при apparent incompatibility, держит `CANDIDATE` до alignment time/scope/identity, записывает provenance gaps и может оставить case `UNRESOLVED`. Scoped Authority позже принимает decision для defined purpose, сохраняя losing/unresolved material. New document может reopen case. Paper folders, signatures, correction slips и decision ledger сохраняют A7 obligations без SQL, Events, embeddings или numeric confidence.

### Adaptive analog or neuromorphic substrate

Competing attractors, distributed traces или dynamically stable alternatives могут представлять unresolved plurality без conflict rows. Uncertainty может быть ranges, competing dynamics или inability to stabilize discrimination, а не probability. Для A7 mapping substrate или companion accountability procedure должен раскрывать materially required participants, scope, uncertainty/basis, authority boundary и revision/reopening effects. Physical competition states не является автоматически semantic resolution.

### Conventional digital Event-sourced laboratory

Существующий P1–C5 позже может служить falsification instrument, но сегодня не реализует accepted A7 conflict lifecycle. Claims, provenance-bearing records, relations, Supersession history, reducer views и Receipts могут поддержать future experiments. A7 не добавляет conflict Event verbs, не меняет reducer semantics и не превращает PostgreSQL/SQLite ordering в resolution authority.

Эти mappings показывают только conceptual portability. Cross-substrate conformance принадлежит A8.

## 16. Falsification criteria и open questions

A7 следует revise/split/weaken, если integrated review покажет, что:

- candidate и established tension нельзя различить observable obligations на materially different substrates;
- taxonomy содержит практически неразличимые categories или пропускает recurrent irreducible type;
- `NOT_A_CONFLICT`, `UNRESOLVED_ASSESSMENT`, `UNRESOLVED`, `RESOLVED_FOR_SCOPE` невозможно держать semantically distinct;
- модель скрыто требует global confidence scale, probability calculus, graph, Event log или centralized reviewer;
- unresolved plurality можно сохранить только копированием implementation structure, а не meaning-level obligations;
- resolution Authority невозможно отличить от truth/evidence Authority без circular rules;
- reopening не может сохранить prior resolution history при lawful forgetting;
- paraconsistent, probabilistic, vague, multi-context или non-propositional tension вынужденно превращается в false contradiction;
- manual/adaptive mapping сохраняет смысл, но отвергается лишь из-за отсутствия current digital mechanics.

Open questions:

- должен ли minimal portable tension taxonomy быть меньше §4;
- formal logic families/paraconsistent handling;
- domain-specific quantitative uncertainty combination/dependence models;
- authority-conflict escalation/delegation semantics;
- reopening/finality policy в legal, operational, scientific, personal contexts;
- executable `NK-CFL` fixtures и возможная роль Issue #17 после blueprint review;
- lawful forgetting versus conflict/resolution history;
- A8 semantic equivalence для radically different uncertainty observables.

## 17. Deferred responsibilities и completion boundary

A7 намеренно не решает:

- **A8 — Substrate-independence Contract:** equivalence/conformance obligations и thresholds для A1–A7;
- **A9 — Reference Laboratory Boundary:** final module-by-module classification P1–C5;
- **A10 — Open Questions and Falsification:** integrated research/falsification registry;
- **ADR-0003:** acceptance/rejection/revision older proposed semantic-conflict ADR;
- **Issue #14:** future canonical identity/alias/migration details;
- **Issue #15:** portable history commitment и append/replay semantics;
- **Issue #16:** physical/cryptographic deletion и retention execution;
- **Issue #17:** executable conformance/fixture expansion;
- **Issue #74 / ADR-0024:** reducer-v2 referential/Supersession topology/migration;
- **Issue #18:** license/publication;
- **Track H:** operator-controlled historical-source admission;
- new Event vocabulary, OCC/CAS/CRDT/LWW selection, multi-writer protocol, new database/language/profile, LLM/vector adapters, runtime implementation, maturity promotion или production authorization.

First-draft completion test:

> Для disputed/uncertain position можно указать participants, tension kind, assessment status, alignment basis, uncertainty/provenance gaps, resolution status, Authority/policy/basis, resulting revision/non-revision effect и reopening conditions — без требования одного winner algorithm, confidence scalar, Event vocabulary или physical substrate.

A7 остаётся `DRAFTED / PROVISIONAL` до independent review, integrated A1–A10 review и последующего operator review по ADR-0025.