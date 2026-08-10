# 🧬 A8 — Контракт независимости от substrate

**[English](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) · [Русский](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md)**

> **Deliverable:** `A8_SUBSTRATE_INDEPENDENCE_CONTRACT` blueprint [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.ru.md) под `ADR-0025` / [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Depends on:** provisional A1–A7, особенно A4 substrate/conformance laws, A5 identity/time/change, A6 lifecycle и A7 conflict/uncertainty/revision  
> **Evidence boundary:** только architecture research и provisional conformance obligations; без runtime, accepted-contract, evidence, assertion-map, NK-EPI, maturity или production change  
> **Review status:** первый drafted slice; ожидает independent review и integrated A1–A10 review

```text
model_id: nk-substrate-independence/A8-draft-1
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
next_content_slice: A9_REFERENCE_LABORATORY_BOUNDARY
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```

## 1. Назначение и граница authority

A8 отвечает на один bounded вопрос:

> Что должно оставаться семантически истинным о реализации, когда её физический carrier, representation, execution model, storage model или вычислительный substrate радикально отличаются от другой реализации?

A8 превращает meaning-level obligations A1–A7 в **mapping и conformance contract**. Он не требует одинаковой machinery. Он требует, чтобы profile показывал, какие architecture distinctions он сохраняет, каким способом их проявляет, где теряет и какой conformance claim вследствие этого оправдан.

Центральная граница:

```text
substrate-independent specification
≠
universal portability proof
```

A8 не заявляет, что каждый нынешний или будущий substrate способен реализовать Native Kernel. Substrate, неспособный сохранить required distinction, всё ещё может быть полезным, но обязан раскрыть limitation и не может заявлять full semantic equivalence.

## 2. Определение substrate independence

Для A8 **substrate independence** означает:

> архитектура Native Kernel формулируется через meaning-level distinctions, relations, transitions, preservation obligations, explicit losses и observable conformance criteria, выполнение которых не зависит от одного обязательного physical representation или execution mechanism.

Это **не** означает отсутствие implementation constraints. У каждой реализации есть substrate. Он может делать некоторые obligations простыми, дорогими, approximate, externalized или impossible.

Поэтому conforming mapping разделяет:

```text
architecture obligation
        ↓
declared realization / functional equivalent
        ↓
observable preservation evidence
        ↓
explicit limitation or loss, if any
        ↓
scoped conformance claim
```

Named functional equivalent допустим только тогда, когда сохраняет required semantic effect. Переименование потерянного distinction не является equivalence.

## 3. Architecture-preserving mapping

A8 использует provisional relation specification:

```text
SUBSTRATE_MAPPING(
  profile,
  architecture_obligation,
  realization_or_equivalent,
  preservation_state,
  context_and_scope,
  observable_check,
  declared_loss_or_none,
  uncertainty,
  authority_for_claim
)
```

Это specification notation, а не required object, schema, API, row, Event, graph node, register или wire format.

Mapping имеет пять preservation states:

| State | Значение | Влияние на conformance |
|---|---|---|
| `PRESERVED` | required distinction/effect представлен без известной material semantic loss в declared scope | может поддерживать full conformance для obligation |
| `PARTIAL` | bounded subset faithful, material remainder explicit | нельзя представлять как full preservation |
| `UNSUPPORTED` | profile не способен реализовать obligation в declared scope | full conformance для scope недоступен |
| `INDETERMINATE` | evidence недостаточно, чтобы установить preservation или loss | conformance claim остаётся unresolved |
| `LOSSY` | известная approximation/collapse изменяет либо удаляет material semantic information | loss explicit; full semantic equivalence запрещена |

Эти states **не** являются repository assertion-map arithmetic и не повышают ни один existing assertion. Они классифицируют один A8 mapping claim.

```text
cannot preserve a required distinction
→ declare PARTIAL / UNSUPPORTED / INDETERMINATE / LOSSY
→ do not claim full equivalence
```

## 4. Обязательные semantic preservation obligations

Profile, заявляющий full A8 conformance в declared scope, обязан сохранить напрямую или через declared functional equivalent все materially applicable obligations ниже.

| ID | Obligation | Minimum preservation requirement |
|---|---|---|
| `A8-P01` | ontology distinctions | material A2 distinctions, например Observation/Claim, Evidence/Source, Knowledge/Belief, Record/represented reality, Conflict/Contradiction, остаются distinguishable где применимо |
| `A8-P02` | abstract transition semantics | A3 transition intent, preconditions/postconditions, non-change, failure, unknown, partial и unsupported outcomes remain expressible без silent conversion в success/false |
| `A8-P03` | semantic laws | applicable A4 laws остаются true для mapping; profile не получает exemption только из-за другой machinery |
| `A8-P04` | typed/scoped identity | A5 identity kinds и uncertainty identity сохраняются/translated; substrate-local identity не становится semantic identity |
| `A8-P05` | temporal and ordering meaning | materially relevant A5 temporal dimensions/orders остаются distinguishable; implementation order не promoted к world/causal order |
| `A8-P06` | lifecycle and history meaning | A6 phases/transition meanings, lineage, disposition и closure distinctions remain observable без обязательной one storage state machine |
| `A8-P07` | conflict/uncertainty/revision meaning | A7 assessment/resolution distinctions, typed uncertainty, plurality, scoped resolution, revision lineage и reopening remain preservable |
| `A8-P08` | Context, Provenance, Source and Authority | material scope, origin/transformation/gaps и role-bounded Authority переживают mapping либо loss explicit |
| `A8-P09` | bounded accountability | accountable decisions, transformations, omissions, failures и losses объяснимы до declared boundary без implication truth/completeness |
| `A8-P10` | capability and loss declaration | unsupported, partial, indeterminate или lossy obligations остаются first-class limitations, а не hidden approximations |

Obligation может быть inapplicable только по explicit domain/scope argument. “У нашего substrate нет такого field” не является applicability argument.

## 5. Допустимая implementation variation

Profile может свободно отличаться по:

- physical memory/carrier;
- layout/topology;
- serialization или отсутствию serialization;
- identifier encoding;
- programming language;
- instruction sequence;
- data structure;
- storage engine или отсутствию database;
- indexing/retrieval mechanism;
- persistence mechanism;
- synchronization strategy;
- parallelism/concurrency model;
- distribution/centralization;
- representation of time;
- representation of uncertainty;
- representation of state/history;
- hardware/processor model.

Variation разрешена **потому, что подчинена preservation**, а не потому, что implementation details не имеют значения.

## 6. Representation не равна semantic equivalence

A8 различает минимум пять вопросов, которые нельзя схлопывать в один equality predicate:

| Relation | Вопрос |
|---|---|
| `PHYSICAL_IDENTITY` | одинаков ли physical carrier/state? |
| `REPRESENTATION_EQUIVALENCE` | эквивалентны ли encodings/structures по declared representation rule? |
| `SEMANTIC_OBLIGATION_EQUIVALENCE` | сохранены ли required meaning-level distinctions/effects? |
| `BEHAVIORAL_CONFORMANCE_FOR_SCOPE` | удовлетворяют ли observable operations тем же declared architecture obligations в tested scope? |
| `LINEAGE_CONTINUITY_EQUIVALENCE` | сохранена ли required predecessor/derivation/migration continuity? |

Эти relations могут расходиться.

```text
physical identity
is neither necessary nor sufficient
for semantic equivalence
```

Equal bytes, hashes, text, rows, graph topology, memory addresses или output strings сами по себе не доказывают semantic equivalence. Different bytes, IDs, storage layouts, timings или physical states сами по себе не доказывают semantic non-equivalence.

## 7. Portability identity

A8 наследует typed/scoped identity model A5. Migration или cross-substrate comparison обязаны назвать identity relation, preservation которой заявляется.

Profile не должен выводить:

```text
same storage key → same referent
same hash → same Claim position
same bytes → same Record occurrence
new address → new semantic entity
```

Cross-substrate mapping может preserve `SEMANTIC_CONTENT_IDENTITY`, меняя `RECORD_IDENTITY` и `SUBSTRATE_LOCAL_IDENTITY`. Он может preserve `LINEAGE_CONTINUITY_IDENTITY` без claim exact content identity. Unresolved identity остаётся allowed outcome.

Если substrate не способен expose distinction между semantic и substrate-local identity, mapping как минимум `LOSSY` для A8-P04.

## 8. Portability time и ordering

A8 не требует:

- universal global clock;
- synchronized wall-clock timestamps;
- one total write order;
- infinite temporal precision;
- instantaneous synchronization;
- one global sequence number.

Profile может использовать instants, intervals, uncertain bounds, counters, causal relations, partial orders, phases, local clocks, qualitative before/after или другой mapping.

Сохраняться должен **meaning materially required relations** из A5:

```text
write/commit order
≠ occurrence order
≠ observation order
≠ causal/dependency order
≠ semantic precedence
```

Если substrate может представить только partial order, это не defect само по себе. Если execution вынуждает incomparable events в total order, imposed order не должен молча становиться causal/world order.

## 9. Portability memory и lifecycle

Memory не обязана быть file, row, byte sequence, Event log, snapshot или replayable reducer state.

Substrate может сохранять memory через:

- durable symbolic records;
- distributed relations;
- adaptive physical traces;
- stable/recurring dynamics;
- externalized procedures;
- reconstructible transformations;
- hybrid mechanisms.

Profile, заявляющий A8-P06, обязан сохранять materially required continuity, lifecycle position/effect, Provenance, lineage, revision/disposition meaning и declared forgetting/loss boundaries.

`history visibility` не означает mandatory Event sourcing. Non-Event-sourced profile может conform, если сохраняет required historical distinctions/accountability. И наоборот, append-only Event log, потерявший Context или lineage, может быть non-conformant даже при perfect replay.

## 10. Portability conflict, uncertainty и revision

A8 сохраняет architecture states A7 по meaning, а не literal encoding.

Profile не обязан физически хранить exact strings:

```text
CANDIDATE
ESTABLISHED
NOT_A_CONFLICT
UNRESOLVED_ASSESSMENT
UNRESOLVED
DEFERRED
RESOLVED_FOR_SCOPE
REOPENED
```

Но он обязан уметь представить **distinctions, которые они выражают**, когда materially applicable.

Границы сохраняются:

```text
Conflict ≠ necessarily Contradiction
Detection ≠ Resolution
Resolution-for-scope ≠ Objective Truth
Uncertainty ≠ one universal confidence scalar
Revision ≠ overwrite
```

Substrate, способный представить только `true/false` и поэтому переводящий `UNRESOLVED`/`UNRESOLVED_ASSESSMENT` в одну сторону, является `LOSSY` и не может заявлять full A8-P07 preservation.

## 11. Preservation Context, Provenance, Authority и lineage

Migration/translation обязан preserve materially relevant:

- Context/scope и known widening/narrowing;
- Source attribution и uncertainty;
- Provenance origin, custody/transformation/derivation, contested alternatives и gaps;
- Authority role, scope, delegation/policy и temporal applicability;
- predecessor/successor/derivation/migration lineage.

Profile может redact details по governed policy, но `redacted/withheld` должен оставаться distinguishable от `known complete`, `unknown` и `nonexistent`, когда distinction material.

Successful transfer, stripping Provenance, не является full semantic preservation только потому, что content survived.

## 12. Accountability и explainability obligation

A8 не требует одного universal Receipt format, durable log, explainability algorithm или human-readable trace каждого internal microstep.

Он требует, чтобы profile мог предоставить bounded account напрямую или через admissible companion mechanism для materially accountable operations, например:

- semantic transformation;
- identity/equivalence decision;
- scoped resolution;
- Revision/Supersession;
- restriction/disposition/forgetting declaration;
- migration;
- capability failure или declared loss.

Account должен содержать достаточно Context, method/Authority, basis, effect, limitations и uncertainty для проверки conformance claim.

```text
accountability ≠ correctness
explanation ≠ truth proof
```

## 13. Capability declarations и explicit degradation

Каждый A8 profile должен публиковать capability declaration для claimed scope. Это может быть document, manifest, procedural certificate, formal proof, test report или другой inspectable equivalent.

Для каждого required obligation нужно указывать:

```text
obligation
scope
realization/equivalent
preservation state
observable check/evidence
known loss
uncertainty
```

Limitation сама по себе не architecture failure, если честно scoped. Failure — скрыть material limitation, заявив stronger equivalence.

Примеры:

- substrate может быть `PRESERVED` для typed identity и `PARTIAL` для Provenance custody;
- `UNSUPPORTED` для physical-erasure verification, сохраняя logical disposition;
- cross-language translator может быть `INDETERMINATE` для одного semantic-content equivalence class до review;
- boolean-only device может быть `LOSSY` для unresolved epistemic states.

## 14. Conformance outcomes

A8 использует четыре provisional outcome classes для **named scope**:

| Outcome | Значение |
|---|---|
| `FULL_CONFORMANCE_FOR_SCOPE` | все materially applicable A8-P01…P10 obligations имеют `PRESERVED` и достаточный observable basis |
| `BOUNDED_CONFORMANCE` | более узкий explicit subset/scope preserved, excluded/limited obligations declared и broader claim не делается |
| `NON_CONFORMANT_FOR_SCOPE` | один или несколько materially required obligations known `LOSSY`/`UNSUPPORTED` для claimed scope либо required distinction silently collapsed |
| `INDETERMINATE_CONFORMANCE` | evidence недостаточно, чтобы установить preservation или non-conformance |

`BOUNDED_CONFORMANCE` — не loophole для названия partial implementation “fully Native Kernel”. Scope должен быть достаточно explicit, чтобы reviewer видел obligations вне claim.

Profile conformance остаётся distinct от production authorization, safety, security, performance, legal compliance или operational equivalence.

## 15. Cross-substrate equivalence criteria

Два profiles `A` и `B` могут считаться semantically equivalent **для named scope и observation boundary** только если:

1. сохраняют те же materially applicable A8-P01…P10 obligations;
2. declared identity mappings согласуются там, где scope требует agreement, либо differences explicitly classified;
3. temporal/order relations required by scope preserved без manufactured causality;
4. lifecycle, conflict, uncertainty, revision и disposition distinctions produce compatible meaning-level effects;
5. Context, Provenance, Authority и lineage loss не различаются materially без disclosure;
6. observable outcomes совместимо различают unknown/partial/unsupported/failure от false/success;
7. lossy approximation находится вне equivalence claim либо ослабляет claim;
8. evidence/checking procedure itself declared.

Same final output insufficient. Different internal dynamics alone do not defeat equivalence.

A8 намеренно не требует single universal equivalence algorithm. Domain-specific equivalence predicates допустимы под этим contract.

## 16. Lossy mappings и migration discipline

Migration не считается successful только потому, что data arrived или program ran.

Migration должен назвать:

```text
source profile + version/scope
target profile + version/scope
identity relations claimed preserved
Context / Provenance / Authority mapping
temporal/order mapping
lifecycle/history mapping
conflict/uncertainty/revision mapping
known losses / approximations
verification method
resulting conformance scope
```

Material untranslatable distinctions остаются explicit. Target может сохранять opaque source artifact или external companion record, чтобы избежать semantic loss, но зависимость от companion входит в declared profile boundary.

## 17. Failure modes и counterexamples

### Counterexample A — content preserved, Provenance deleted

System корректно migrates Claim text, но удаляет Source/Provenance.

**Result:** не full-conformant для scope, требующего A8-P08. Content preservation не компенсирует Provenance loss.

### Counterexample B — different bytes и IDs, meaning preserved

Два substrates используют разные encodings/local IDs, но сохраняют referent/semantic identity relations, Context, Provenance, lineage, temporal meaning, uncertainty и observable transition obligations.

**Result:** encoding difference сама по себе не устанавливает non-equivalence.

### Counterexample C — newest record становится truth

Profile решает каждый conflict выбором latest local write и представляет его как true world state.

**Result:** non-conformant. Local write order promoted в semantic precedence, A7 resolution — в truth.

### Counterexample D — `UNRESOLVED` невозможно представить

Device поддерживает только binary true/false и maps unresolved positions в `false`.

**Result:** `LOSSY` A8-P02/A8-P07 mapping; full conformance запрещён, если declared scope действительно не исключает distinction.

### Counterexample E — history без Event sourcing

Profile использует versioned procedural Records/lineage relations вместо Event sourcing, сохраняя predecessor history, Context, Authority, uncertainty, revisions и accountable outcomes.

**Result:** absence Event sourcing само по себе не non-conformance.

### Counterexample F — exact replay, потерян Context

System replay byte-identical state, но strips scope, в котором Claims были valid.

**Result:** reproducibility representation не устанавливает semantic equivalence; A8-P01/P03/P08 нарушены.

### Counterexample G — deterministic agreement через silent collapse

Две implementations всегда дают одинаковый boolean, потому что обе convert `UNKNOWN` в `false`.

**Result:** behavioral equality defective projection не устанавливает Native Kernel conformance.

## 18. Contrasting illustrative mappings

Эти примеры тестируют contract и не являются claims implemented support.

### Manual archival and review process

Paper Records, cross-references, Provenance sheets, correction/Supersession annotations, scoped decisions и review ledgers могут preserve многие obligations без software, SQL, digital hashes или Event sourcing. Conformance определяется реально сохранённой semantics/controls, а не medium.

### Adaptive analog or neuromorphic substrate

Будущая adaptive physical system может кодировать continuity changing dynamics, а не discrete Records. Она может qualify только если required identity, Provenance, temporal/order, uncertainty, revision и accountability distinctions observable напрямую или через declared companion procedure. “Она помнит” недостаточно для A8 conformance.

### Conventional digital Event-sourced laboratory

Current Python/PostgreSQL/SQLite laboratory можно map к A8 через existing versioned contracts, Events, reducers, Receipts и tests. Эти mechanisms illustrative profile choices. A9 владеет detailed classification, какие P1–C5 mechanisms действительно satisfy/partially satisfy/fail A1–A8 blueprint.

## 19. Explicit non-claims и non-requirements

A8 **не** требует как universal Canon:

```text
binary representation
von Neumann CPU
silicon
RAM
files
JSON
UTF-8
SHA-256
SQL
PostgreSQL
SQLite
graph database
vector database
Event sourcing
append-only Event log
reducer
global_seq
stream_seq
wall-clock timestamps
floating point
LLM
embeddings
transformer
Python
Rust
network
cloud
centralized execution
```

A8 также не утверждает:

```text
substrate independence ≠ proof that every substrate can conform
future-facing architecture ≠ implemented neuromorphic/analog/quantum profile
semantic equivalence ≠ physical identity
same output ≠ full semantic equivalence
full conformance ≠ production authorization
public repository ≠ open-source license
A8 draft ≠ independent approval ≠ integrated Canon
```

Никакая quantum, neuromorphic, analog или другая future implementation этим документом не заявляется существующей.

## 20. Existing contracts, operator boundaries и A9 boundary

Existing accepted/versioned contracts remain valid в historical scope. A8 не переписывает их только потому, что они используют current digital mechanisms.

- `nk-id/1.0`, `nk-event/1.0`, reducers, hash chains, SQL profiles и evidence остаются current reference-laboratory mechanisms до A9 mapping;
- Issue #14/#15/#16/#17 сохраняют existing scopes;
- Issue #18 operator-controlled; license не выбирается, public visibility не называется open-source permission;
- Issue #74 / ADR-0024 остаётся `PROPOSED / PENDING_OPERATOR`; reducer v1 immutable, reducer-v2 unauthorized;
- ADR-0003 остаётся proposed, A8 не создаёт conflict Event vocabulary;
- Track H source admission operator-controlled;
- runtime expansion остаётся `FROZEN`.

A8 спрашивает **что conforming implementation обязана preserve**. A9 отдельно спросит **как current P1–C5 laboratory отображается на blueprint**. Поэтому A8 использует laboratory только illustratively и не grade модули здесь.

## 21. Open questions и falsification boundary

A8 должен быть revised/weakened/split/rejected, если later evidence покажет, например, что:

- A8-P01…P10 невозможно observe/test без импорта current implementation mechanism;
- semantic preservation невозможно полезно и нециркулярно отличить от representation equality;
- один и тот же required meaning faithfully реализуется на substrate, который не может satisfy A8 requirement даже через declared functional equivalent;
- bounded accountability обязательно требует более сильного universal history commitment, чем утверждает A8;
- probabilistic/analog continuity делает proposed equivalence boundary incoherent, а не просто representation-different;
- legitimate forgetting не совместимо с lineage/accountability obligations;
- conformance outcome classes допускают misleading unfalsifiable claims.

Эти и другие unresolved questions переходят в A10, а не скрываются как solved facts.

## 22. Completion boundary

First-draft completion test:

> Для двух радикально разных implementations reviewer может назвать obligations Native Kernel, которые должны быть preserved, отличить physical/representation equality от semantic/behavioral equivalence, увидеть declared loss/unsupported capability и определить, warranted ли scoped conformance claim, без обращения к PostgreSQL schema, Python classes, JSON bytes, Event sourcing или одной processor model.

```text
deliverable: A8_SUBSTRATE_INDEPENDENCE_CONTRACT
model_id: nk-substrate-independence/A8-draft-1
state: DRAFTED
review: PENDING independent review and integrated blueprint review with A1-A10
next_content_slice: A9_REFERENCE_LABORATORY_BOUNDARY
runtime expansion: FROZEN
P1-C5 role: BOUNDED_REFERENCE_LABORATORY
production_authorized: false
assertion map: UNCHANGED
NK-EPI: UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H: UNCHANGED
```
