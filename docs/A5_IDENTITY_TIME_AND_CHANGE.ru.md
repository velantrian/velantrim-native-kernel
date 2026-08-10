# 🧬 A5 — Identity, Time и Change

**[English](./A5_IDENTITY_TIME_AND_CHANGE.md) · [Русский](./A5_IDENTITY_TIME_AND_CHANGE.ru.md)**

> **Deliverable:** `A5_IDENTITY_TIME_AND_CHANGE` blueprint [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.ru.md) под `ADR-0025` / [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Depends on:** provisional blueprint content A1–A4  
> **Evidence boundary:** только architecture research и provisional semantic obligations; без изменений runtime, contracts, evidence, assertion-map, NK-EPI, maturity или production  
> **Review status:** первый drafted slice; ожидает independent review и integrated A1–A10 review

```text
model_id: nk-identity-time-change/A5-draft-1
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
next_content_slice: A6_KNOWLEDGE_LIFECYCLE
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```

## 1. Purpose и authority boundary

A5 отвечает на meaning-level вопрос, который A2–A4 намеренно оставили открытым:

> Когда две representation, position, Record, occurrence или continuity являются тем же самым в объявленном смысле; когда они различны; как называются time и order; и что именно Change сохраняет либо создаёт?

A5 **не** определяет universal hash, UUID, row key, physical address, clock, Event envelope, reducer sequence, deletion engine или metaphysical theory identity. Он задаёт provisional vocabulary и discipline решения, которые later profile должен preserve, translate, approximate либо явно объявить unsupported.

Модель уточняет A4-L11…L19, не ослабляя их:

```text
semantic identity ≠ storage identity
equal bytes/hash/text ≠ universal semantic identity
one timestamp ≠ all temporal meaning
write order ≠ occurrence or causal order
Revision ≠ silent overwrite
Supersession ≠ deletion or falsity
representation change ≠ represented-world change
```

## 2. Model status и qualification rule

Identity в Native Kernel — **typed, scoped relation**, а не один global identifier. Утверждение sameness/difference неполно, пока не названы identity kind, Context, temporal scope, criterion, uncertainty и Authority там, где решение governed.

Candidate A5 rule допустим только если его можно выразить без обязательных Python, SQL, JSON, SHA-256, wall clock, Event sourcing, graph, LLM, embeddings или конкретной processor model.

Поэтому A5 отделяет semantic obligations от current reference encodings. Existing accepted contracts сохраняют historical validity в своём versioned scope; A5 не supersede молча accepted ADR и не переписывает evidence.

## 3. Identity kinds

A5 определяет семь provisional identity kinds. Это relations/questions, а не обязательные stored entities или enums.

| Kind | Вопрос | Explicit non-equivalence |
|---|---|---|
| `REFERENT_IDENTITY` | Относятся ли две representation к одному represented entity/process/referent в объявленном Context? | same referent ≠ same State или representation |
| `SEMANTIC_CONTENT_IDENTITY` | Несут ли две expression одинаковый declared semantic content/proposition под stated equivalence rule? | same content ≠ same Claim, Record, Source или occurrence |
| `CLAIM_POSITION_IDENTITY` | Это тот же source-/actor-bound assertion или epistemic position? | same text/content ≠ same act of claiming |
| `RECORD_IDENTITY` | Это тот же retained representation/Record под declared record-continuity rule? | copied bytes ≠ автоматически same Record |
| `LINEAGE_CONTINUITY_IDENTITY` | Принадлежат ли items одной declared continuity/revision family, оставаясь различимыми versions? | one lineage ≠ one version или one content identity |
| `OCCURRENCE_IDENTITY` | Представляют ли Records/Events/Observations один bounded occurrence или Change? | one occurrence ≠ one Event record; one Event ≠ one physical occurrence |
| `SUBSTRATE_LOCAL_IDENTITY` | Это тот же row, address, file, object, physical trace, process-local object или другой local carrier? | local/physical identity ≠ semantic identity |

Эти kinds могут различаться без contradiction. Два объекта могут иметь `SAME` semantic content и `DISTINCT` Record identity. Меняющийся человек или процесс может сохранять referent identity при изменении State. Migrated representation может менять substrate-local identity и сохранять declared semantic или lineage relation.

## 4. Typed identity relation

Provisional abstract relation:

```text
IDENTITY_RELATION(
  subject_a,
  subject_b,
  identity_kind,
  context,
  temporal_scope,
  criterion,
  authority_or_method,
  uncertainty
)
```

Profile может представить result иначе, но обязан preserve или явно map следующие semantic outcomes там, где distinction существенен:

```text
SAME
DISTINCT
CONTINUATION_OF
VERSION_OF
ALIAS_OF
MIGRATED_FROM
UNRESOLVED
```

`SAME` означает same **только под named identity relation**, а не universal ontological identity. `UNRESOLVED` обязателен, когда доступные criterion, Context, provenance или capability не позволяют warrant более сильный ответ. Ambiguous identity или collision обязаны сохранять candidates различимыми до authorized resolution/narrowing.

## 5. Continuity, versions, aliases и migration

Continuity не равна sameness. Successor может быть новой version или новой entity и всё равно принадлежать declared lineage.

A5 использует provisional distinctions:

```text
identity-preserving transformation
new version within declared lineage
new semantic entity with explicit predecessor/derivation relation
alias to an already distinguished identity
migration from one representation/profile to another
unresolved identity effect
```

Migration MUST указывать, какие identity kinds она заявляет preserved, какие меняет, и какие information loss/approximation возникают. Profile MUST NOT выводить semantic preservation только из equal bytes, equal hashes, successful deserialization, matching row keys или successful program execution.

Alias MUST NOT молча merge Provenance, Authority, temporal scope или independent occurrences. Несколько aliases могут обозначать одну entity под declared policy; похожие labels сами по себе не устанавливают aliasing.

## 6. Temporal dimensions

A5 определяет восемь provisional temporal dimensions, которые должны оставаться различимыми, когда это materially важно:

| Dimension | Meaning |
|---|---|
| `OCCURRENCE_TIME` | когда represented occurrence/change произошёл или заявляется как произошедший |
| `VALID_TIME` | interval/point, в котором represented proposition, State, rule, relation или position применяется |
| `OBSERVATION_TIME` | когда observer/Source получил или registered Observation/measurement |
| `ASSERTION_TIME` | когда actor/Source сделал или представлен как сделавший Claim/position |
| `RECORD_TIME` | когда representation стал retained Record в relevant system/process |
| `DECISION_TIME` | когда Authority или procedure принял решение |
| `EFFECTIVE_TIME` | когда decision, policy, Supersession, restriction или другой governed effect начинает/заканчивает действовать |
| `WRITE_COMMIT_TIME` | когда конкретная implementation физически/логически записала или committed representation |

Profile не обязан иметь восемь физических timestamp fields. Он обязан иметь declared mapping, сохраняющий нужные domain distinctions, или явно report loss/unsupported dimensions.

Time может выражаться instants, intervals, ranges, partial order, qualitative relations, uncertain bounds, counters, physical phases или иными substrate-specific mechanisms. A5 не требует globally synchronized clocks или UTC как universal substrate property.

## 7. Ordering model

Time values и order relations связаны, но не interchangeable. A5 различает как минимум:

```text
OCCURRENCE_ORDER
OBSERVATION_ORDER
CAUSAL_DEPENDENCY_ORDER
LINEAGE_ORDER
AUTHORITY_DECISION_ORDER
LOCAL_WRITE_COMMIT_ORDER
MIGRATION_SYNCHRONIZATION_ORDER
CONCURRENT / INCOMPARABLE / UNKNOWN_ORDER
```

Total order, введённый для storage или deterministic execution, не становится occurrence или causal order без отдельного warrant. В частности:

```text
A <write B
≠
A <causal B
```

Profiles могут использовать local total order, сохраняя тот факт, что некоторые represented relations concurrent, incomparable, uncertain или unknown.

## 8. Change classification и decision matrix

A5 классифицирует semantic effect Change независимо по identity kinds. Следующая matrix — provisional guidance, не universal automatic algorithm:

| Change | Default A5 interpretation |
|---|---|
| storage relocation / backend replacement | substrate-local identity меняется; semantic/lineage preservation требует declared mapping |
| re-encoding / serialization change | representation меняется; semantic content может сохраняться под named equivalence |
| exact copy | обычно новый Record/carrier; content может быть same; Provenance остаётся distinguishable |
| translation | новый Record/expression; semantic-content equivalence возможна, но должна быть declared/assessed |
| formatting или non-semantic typo correction | representation/Record version меняется; content identity domain-dependent и не assumed globally |
| semantic correction | обычно новая content/position version с explicit lineage; represented occurrence не обязан меняться |
| reinterpretation | новая Interpretation/position, linked к исходному Record/Observation где применимо |
| Revision | identity effect классифицируется явно; predecessor остаётся distinguishable, если нет authorized forgetting |
| Supersession | predecessor и successor distinct; replacement scope/effective time explicit |
| restriction | availability/access меняется; это само по себе не меняет truth, content identity или occurrence identity |
| logical erasure | disposition/availability change; не означает global physical deletion или falsity |
| physical/cryptographic erasure | уничтожает/делает carriers inaccessible в bounded proof scope; не стирает represented history задним числом |
| forgetting/loss | фиксирует authorized или unavoidable reduction availability/recoverability/continuity; не означает, что represented thing не существовал |
| represented-world change | represented State может меняться, а referent identity может сохраниться или нет по declared criterion |

Когда relevant несколько identity kinds, profile обязан report vector effects вместо одного `changed=true/false`.

## 9. Revision и Supersession

Semantic Revision требует, где materially важно:

```text
predecessor
successor or revised position
reason/basis
scope
Authority/method
temporal relation
relevant Evidence/Provenance
uncertainty
identity effect
```

Revision может сохранять один identity kind и создавать new version по другому. Silent in-place replacement, делающий predecessor неотличимым от never-existing history, не является accountable Revision, кроме explicit authorized forgetting/loss boundary.

Supersession означает scoped replacement/preference, а не deletion, falsity, universal invalidation или physical erasure. A5 не решает single-successor rules, cycle rules, self-supersession или reducer referential topology; они остаются вне slice, Issue #74 / ADR-0024 не затрагивается.

## 10. Restriction, erasure и forgetting

A5 сохраняет meanings раздельно:

```text
restriction
≠ logical erasure
≠ physical deletion
≠ cryptographic erasure
≠ semantic forgetting/loss
≠ falsity
```

Restriction меняет availability/permission. Logical erasure фиксирует semantic/disposition state в declared profile. Physical deletion и crypto-erasure — execution/proof questions. Forgetting — continuity/availability loss boundary и может существовать на substrate вообще без rows/files.

A5 не определяет operational deletion lifecycle, key hierarchy, backup handling, provider deletion или compliance semantics, принадлежащие Issue #16 и later lifecycle/profile work.

## 11. Relationship to existing contracts и reference laboratory

В repository уже есть accepted/versioned identity и Event contracts и bounded clean implementation. A5 не переписывает их history/evidence.

### Existing `nk-id/1.0`

`nk-id/1.0` использует strict UTF-8/NFC canonical JSON subset, SHA-256 domain separation, `nkh1`/`nkc1`/`nkl1` и identity-bearing `asserted_at` в current reference contract. Это valid versioned contract choices в объявленном scope. Они **не устанавливаются A5 как единственная physical realization semantic identity**.

A5 фиксирует reconciliation requirement для later integrated review:

```text
A5 meaning-level identity/time model
        ↓
versioned encoding/profile mappings
        ↓
existing nk-id/1.0 as one current mapping
```

ADR status здесь не меняется. Issue #14 остаётся open для semantic/profile separation, aliasing/migration, valid-time identity effects, hash agility, independent readers и cross-encoding equivalence.

### Existing `nk-event/1.0` и P1–C5

`global_seq`, `stream_seq`, commit order, Event envelopes, reducer replay и exact JSON/bytes остаются useful reference-laboratory mechanisms. Их ordering не является universal occurrence или causal order. Issue #15 остаётся owner portable history commitment и broader Event/replay threat models.

### Existing deletion state machine

Current deletion/restriction state machine — bounded profile realization. A5 импортирует только semantic distinctions restriction, logical erasure, physical deletion, crypto-erasure и forgetting; enum/operational workflow не universalized.

## 12. Failure и indeterminacy cases

Profile нарушает A5 draft obligation для declared mapping, если молча:

- использует row ID, memory address, hash, byte equality или object identity как все identity kinds;
- merge два independent Claims из-за одинакового text;
- считает copied Record тем же provenance-bearing occurrence без declared rule;
- превращает uncertain identity в `DISTINCT` или `SAME` ради convenience;
- меняет identifier/encoding при migration без aliases/lineage или loss disclosure;
- превращает один timestamp одновременно в occurrence, Observation, assertion, Record, decision, valid и write time там, где meanings различны;
- превращает write/serialization order в causality;
- overwrites revised position без visible lineage или authorized forgetting boundary;
- трактует Supersession как falsity или physical deletion;
- трактует restriction/forgetting как evidence, что represented entity никогда не существовала;
- заявляет exact replay или physical identity как единственный valid continuity mechanism.

## 13. Contrasting substrate mappings

### Manual archival and review process

Paper Records, signed provenance sheets, version labels, correction slips, effective-date registers, cross-references и retention decisions могут выражать distinct Record/content/lineage identities и temporal relations без hashes, SQL, Events или reducers.

### Adaptive analog or neuromorphic substrate

Continuity может переноситься changing physical dynamics, attractors, distributed traces или observable transformations. Exact immutable IDs или timestamps могут отсутствовать. Companion procedure может понадобиться для Provenance, identity decisions, partial order, revision lineage или accountable forgetting. Substrate, который не может expose эти declared distinctions, не может claim соответствующий A5 mapping только потому, что сохраняет memory-like influence.

### Conventional digital Event-sourced laboratory

Current laboratory может реализовать часть A5 relations через `nkh1`/`nkc1`/`nkl1`, timestamps, Event sequences, stored Claims, lineage references, reducer views и deletion states. Это одна named implementation family, а не A5 itself.

## 14. Falsification criteria и open questions

A5 должен быть revised, split или weakened, если integrated review покажет, что:

- proposed identity kinds не различают реальные случаи без circular definitions;
- materially different substrates сохраняют meaning, но не могут выразить required distinctions даже functional equivalent;
- один identity kind collapse в другой во всех useful cases;
- temporal model вынуждает digital-clock assumptions, ненужные для semantic preservation;
- order model не выражает legitimate concurrency/incomparability;
- migration с preserved declared meaning ошибочно считается identity loss только из-за changed bytes;
- forgetting невозможно выразить без retention content, которое policy требует unavailable;
- model не выражает uncertain/contested identity без false binary answer.

Open questions для later slices: domain-specific identity criteria, valid-time participation in Claim/content identity, identity evolving Contexts/Sources/Authorities, branching lineage policy, conflict-resolution effects on identity, minimum portable history commitment и cross-substrate equivalence thresholds.

## 15. Deferred responsibilities и completion boundary

A5 намеренно не решает:

- **A6:** complete knowledge lifecycle и state-transition vocabulary;
- **A7:** conflict taxonomy, resolution strategy, uncertainty algebra или belief-revision algorithms;
- **A8:** conformance/equivalence thresholds и formal substrate-independence profile requirements;
- **A9:** final module-by-module classification P1–C5;
- **A10:** integrated open-question/falsification registry;
- **Issue #14:** exact future encoding/hash migration contract details;
- **Issue #15:** append/idempotency/replay и portable Event/history commitment;
- **Issue #16:** physical/cryptographic deletion execution и retention mechanics;
- **Issue #74 / ADR-0024:** reducer-v2 referential/Supersession topology;
- **Issue #18:** license/publication;
- **Track H:** operator-controlled historical-source admission;
- runtime implementation, new Event vocabulary, new databases, LLM/vector adapters, maturity или production authorization.

First-draft completion test: model объясняет, какой identity relation задаётся, какой temporal/order relation используется, и сохраняет ли Change relation, создаёт version/entity, alias/migration, меняет availability или остаётся unresolved — без требования одного physical encoding.

A5 остаётся `DRAFTED / PROVISIONAL`. Independent review и integrated A1–A10 review остаются обязательными до Canon promotion или reopening runtime expansion.