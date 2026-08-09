# 🧬 A3 — Abstract Native Kernel Machine

**[English](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) · [Русский](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md)**

> **Deliverable:** `A3` of the [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.md) blueprint (`ADR-0025`, [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88))  
> **Depends on:** provisional [A1 — Kernel Purpose and Non-goals](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) and [A2 — Knowledge and Memory Ontology](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md)  
> **Evidence boundary:** architecture research and provisional abstract-machine model only; no runtime, contract, evidence, assertion-map, NK-EPI, maturity, or production change  
> **Review status:** first drafted slice; pending independent review and integrated blueprint review with A1–A2 and A4–A10

## 1. Purpose and authority boundary

This document proposes the smallest meaning-level machine that Native Kernel may need in order to receive material, preserve distinctions, attach origin and scope, represent epistemic positions, manage relations and revisions, expose uncertainty and conflict, and produce bounded accountability.

The word **machine** here means an abstract system of observable obligations and allowed transitions. It does **not** mean:

- a von Neumann processor;
- a Turing-completeness claim;
- a finite-state implementation;
- a Python object graph;
- a SQL transaction processor;
- an Event-sourced reducer;
- a graph database;
- an LLM agent loop;
- one globally materialized world State.

A conforming substrate may realize the machine through symbolic records, physical dynamics, human procedures, distributed protocols, analog adaptation, or another declared functional equivalent. It must state which distinctions and obligations it preserves, approximates, externalizes, or cannot support.

A3 does not make A1 or A2 final Canon. It uses their provisional vocabulary so that later review can test whether the ontology is operationally coherent without allowing current laboratory mechanics to define the answer.

## 2. Machine hypothesis and evaluation tests

### 2.1 Provisional hypothesis

Native Kernel can be specified as a **scoped obligation-and-transition system**:

```text
encounter or request
        ↓
explicitly scoped transition attempt
        ↓
updated logical configuration or declared non-change
        ↓
bounded outcome + failure/uncertainty visibility + accountability
```

The transition relation need not be linear, globally ordered, deterministic, digital, or physically stored as a sequence of Events.

### 2.2 Evaluation tests

The model must survive:

1. **Ontology test:** it preserves the A2 distinctions instead of collapsing them into one current class.
2. **Substrate test:** it remains meaningful without Python, SQL, JSON, Events, an LLM, embeddings, digital bytes, or a specific processor.
3. **Non-pipeline test:** interpretation, evidence assessment, admission, relation, revision, and selection can occur in different orders, repeat, branch, or remain unresolved.
4. **Authority test:** no transition obtains truth authority merely because the machine performed it.
5. **Failure test:** malformed, ambiguous, unauthorized, unsupported, partial, or indeterminate operations remain visible rather than becoming false success.
6. **History test:** revision and supersession do not require silent overwrite of prior positions.
7. **Unknown test:** missing or unresolved information is not converted to false.
8. **Equivalence test:** two contrasting substrates can map to the obligations through named equivalence rather than identical mechanics.
9. **Falsification test:** the model states observations that would show it is over-specified, under-specified, or implementation-captured.

## 3. Alternative machine structures considered

### 3.1 Linear ingestion pipeline

```text
capture → classify → admit → relate → retrieve
```

**Strength:** simple implementation planning and operational observability.  
**Failure risk:** falsely implies that every item follows one direction, receives a final classification, and becomes admitted before it can be compared or revised.

**A3 decision:** useful as one profile workflow, rejected as the abstract machine.

### 3.2 Event-sourced transition machine

```text
command → Event → reducer → State → projection
```

**Strength:** explicit history, deterministic replay, and bounded Receipts in the current P1–C5 laboratory.  
**Failure risk:** makes Event, global order, replay, reducer State, and append-only storage universal before A4–A8 establish whether they are semantic obligations.

**A3 decision:** valid laboratory mapping, rejected as the universal machine form.

### 3.3 Relation-centred semantic network

```text
represented items + typed Relations + constraints
```

**Strength:** supports plurality, provenance, conflict, context, and revision without a single lifecycle.  
**Failure risk:** stored edges can be mistaken for true Relations; temporal change, authority, and accountability can become implicit.

**A3 decision:** retain relation-centred reasoning, but require explicit transition and authority obligations.

### 3.4 Capability-and-obligation machine

```text
logical configuration facets
+ typed transition families
+ explicit preconditions/postconditions
+ declared failure outcomes
+ authority and uncertainty boundaries
```

**Strength:** separates meaning-level obligations from physical realization and permits symbolic, procedural, analog, distributed, or hybrid profiles.  
**Failure risk:** can become so abstract that it is unfalsifiable or so broad that every system appears conforming.

**Working decision:** use this structure provisionally and constrain it through observable obligations, negative cases, substrate mappings, and later A4/A8 contracts.

## 4. Abstract machine model

### 4.1 Logical configuration notation

For specification only, let a scoped Kernel configuration be:

```text
K = ⟨B, R, I, C, P, E, L, U, G, V, D, A, O⟩
```

where each symbol names a **logical facet**, not a table, collection class, graph, physical register, or required stored object.

A transition attempt is written:

```text
τ : ⟨K, request, declared context, declared authority/policy⟩
      ↦ ⟨K′, outcome, bounded accountability⟩
```

or:

```text
τ ↦ DECLARED_FAILURE | DECLARED_UNKNOWN | NO_AUTHORIZED_CHANGE
```

`K` and `K′` are scoped characterizations used to state obligations. They are not claims that reality has one complete global State, that every substrate materializes snapshots, or that transition execution is reducer replay.

### 4.2 Configuration facets

| Symbol | Facet | Minimum meaning | It is not |
|---|---|---|---|
| `B` | boundary encounters | material or influence presented to a Kernel boundary, including explicit absence/unknown where declared | automatically an Observation, Record, or Claim |
| `R` | retained representations | Records or functional equivalents available for reference under declared limits | Memory as a whole; truth; one database |
| `I` | identity and equivalence positions | scoped assertions, hypotheses, or unknowns about sameness, difference, aliasing, continuity, and reference | byte equality; final A5 identity law |
| `C` | Context bindings | conditions and scope needed to interpret or evaluate represented material | prompt window or arbitrary metadata |
| `P` | Source and Provenance bindings | attributed origin, acquisition, transformation, custody, and explicit gaps | authenticity or truth proof |
| `E` | semantic and epistemic positions | Proposition, Claim, Interpretation, Hypothesis, Belief, Knowledge-candidate, and Evidence-role assignments | objective truth or one confidence score |
| `L` | Relations | typed, scoped connection positions among distinguishable relata | graph edges that are true by storage |
| `U` | Uncertainty and tension register | explicit uncertainty, candidate/established Conflict, Contradiction assessments, and unresolved plurality | automatic resolution or false-by-default |
| `G` | governance and Authority | declared powers, policies, delegations, restrictions, and contested authority relevant to operations | universal legitimacy or technical permission alone |
| `V` | revision and Supersession lineage | explicit relations between prior and later representations or positions | silent overwrite or deletion |
| `D` | disposition and availability | handling status for operational availability, quarantine, restriction, historical-only access, or declared absence | epistemic truth status or final A6 lifecycle |
| `A` | accountability | Receipts or functional equivalents for accountable operations, decisions, failures, and omissions | proof that an outcome is true or complete |
| `O` | open obligations | unresolved questions, unsupported mappings, pending decisions, incomplete operations, and declared loss | hidden backlog or implicit false |

A profile may combine, distribute, or externalize facets. It may not claim full A3 conformance while silently dropping a required distinction.

### 4.3 Requests and outcomes

A request may originate from a person, instrument, process, environment, another system, or an internal condition. Request identity and authority are separate questions.

An outcome must be classifiable as at least one of:

- `APPLIED` — the declared semantic effect is represented;
- `NO_CHANGE` — the request was evaluated and no semantic effect was authorized or required;
- `QUARANTINED` — material remains isolated pending missing scope, authority, interpretation, or safety conditions;
- `REJECTED` — a declared policy or precondition forbids the requested effect;
- `PARTIAL` — only a bounded subset is represented, with missing effects explicit;
- `UNKNOWN` — the machine cannot warrant a stronger result;
- `UNSUPPORTED` — the profile lacks the required capability or faithful mapping;
- `FAILED` — execution or representation did not satisfy declared obligations.

These are abstract operation outcomes, not final knowledge lifecycle states. A6 may refine or replace them.

## 5. Transition families

Transition families describe meaning-level obligations. They are not mandatory API methods, Event verbs, commands, classes, or a single ordered pipeline.

### 5.1 `ENCOUNTER`

**Purpose:** expose material or influence to the Kernel boundary without prematurely classifying it.

- **Preconditions:** a boundary/interface is declared; available Source, time, method, and Context are supplied or explicitly unknown.
- **Postconditions:** a bounded encounter is distinguishable from later Observation, Interpretation, Claim, Evidence, and admission; acquisition uncertainty is visible.
- **Allowed outcomes:** `APPLIED`, `QUARANTINED`, `PARTIAL`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** converting every input packet directly into a Claim collapses encounter into assertion.

### 5.2 `REGISTER`

**Purpose:** create or recognize a Record/functional equivalent that can be referenced beyond the immediate encounter.

- **Preconditions:** represented subject/boundary is stated; retention or reference Authority exists; known transformations and integrity limits are available.
- **Postconditions:** representation identity or an explicit identity gap exists; Source/Provenance/Context uncertainty remains attached; storage does not imply admission or Memory.
- **Allowed outcomes:** `APPLIED`, `QUARANTINED`, `REJECTED`, `PARTIAL`, `UNKNOWN`, `FAILED`.
- **Failure/counterexample:** persistence of opaque bytes without interpretable boundary or lineage may be storage but not an adequate Record.

### 5.3 `IDENTIFY_OR_DISTINGUISH`

**Purpose:** state whether represented items, referents, versions, or continuities are the same, different, related, ambiguous, or unresolved under a declared criterion.

- **Preconditions:** candidate relata and comparison criterion are explicit; relevant Context, time, and Authority are declared.
- **Postconditions:** identity/equivalence position and uncertainty are represented without merging Records or referents by convenience.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `QUARANTINED`, `PARTIAL`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** equal hashes or equal text do not prove semantic, source, or continuity identity.

### 5.4 `BIND_SCOPE_AND_ORIGIN`

**Purpose:** attach Context, Source, Provenance, temporal scope, and Authority to material or positions.

- **Preconditions:** target is distinguishable; bindings are attributable; known gaps and contested alternatives can be represented.
- **Postconditions:** scope and origin are explicit or explicitly unknown; later operations can detect missing/changed bindings; no authenticity or truth promotion occurs.
- **Allowed outcomes:** `APPLIED`, `PARTIAL`, `UNKNOWN`, `QUARANTINED`, `FAILED`.
- **Failure/counterexample:** inventing an absent Source so that a required field is non-null converts unknown provenance into false provenance.

### 5.5 `INTERPRET_AND_CLASSIFY_ROLE`

**Purpose:** assign a meaning or semantic role such as Observation, Proposition, Claim, Interpretation, Hypothesis, question, instruction, or unknown.

- **Preconditions:** represented material and interpretive Context are available; interpreter/method and assumptions are attributable where material.
- **Postconditions:** role assignment is represented as an Interpretation/position with alternatives and uncertainty; original material remains distinguishable.
- **Allowed outcomes:** `APPLIED`, `PARTIAL`, `QUARANTINED`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** a model label stored without assumptions or alternatives does not become the intrinsic type of the material.

### 5.6 `ASSESS_EPISTEMIC_POSITION`

**Purpose:** assess support, challenge, dependence, uncertainty, belief attribution, hypothesis status, or policy-defined knowledge candidacy.

- **Preconditions:** target Proposition/Claim/question is explicit; Evidence roles, Sources, Provenance, Context, counterevidence, and warranting policy are available or their gaps are declared.
- **Postconditions:** the scoped assessment, reasons, uncertainty, and authority are represented; repetition, relevance, confidence, or admission alone cannot promote Knowledge.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `PARTIAL`, `UNKNOWN`, `QUARANTINED`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** one Source copied many times remains dependent evidence, not independent corroboration.

### 5.7 `DECIDE_DISPOSITION`

**Purpose:** determine whether material or a position is operationally available, quarantined, restricted, rejected, historical-only, or otherwise handled under declared policy.

- **Preconditions:** applicable policy, Authority, purpose, Context, and relevant risks are declared; epistemic status and operational utility remain distinguishable.
- **Postconditions:** disposition, scope, reason, authority, effective time, and review conditions are explicit; admission does not become truth.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `QUARANTINED`, `REJECTED`, `PARTIAL`, `UNKNOWN`, `FAILED`.
- **Failure/counterexample:** allowing an item in retrieval because it is useful does not establish that its Claim is valid.

### 5.8 `RELATE`

**Purpose:** represent a typed, scoped Relation position among distinguishable relata.

- **Preconditions:** relata, relation semantics, direction/arity, Context, time, Source/Authority, and uncertainty are stated.
- **Postconditions:** the relation Claim is distinguishable from represented reality and from its physical encoding; unsupported transitivity/symmetry is not inferred.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `PARTIAL`, `UNKNOWN`, `QUARANTINED`, `FAILED`.
- **Failure/counterexample:** vector similarity or co-occurrence cannot silently become `SAME_AS`, `CAUSES`, or `SUPPORTS`.

### 5.9 `DETECT_TENSION`

**Purpose:** identify possible or established Conflict, Contradiction, scope mismatch, provenance disagreement, authority conflict, or unresolved plurality.

- **Preconditions:** compared positions and relevant interpretation, Context, time, modality, and assumptions are sufficiently explicit; missing alignment remains visible.
- **Postconditions:** tension type, basis, participants, uncertainty, and candidate/established status are represented; no automatic winner or resolution is implied.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `PARTIAL`, `UNKNOWN`, `QUARANTINED`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** “open at 09:00” and “closed at 10:00” must not be labelled contradictory when temporal scopes differ.

### 5.10 `REVISE_OR_SUPERSEDE`

**Purpose:** change a representation or epistemic position while preserving accountable lineage and scope.

- **Preconditions:** predecessor is identifiable; proposed successor/change, reason, Evidence, Authority, Context, and effective scope are declared.
- **Postconditions:** prior position remains historically distinguishable or an explicit lawful-forgetting boundary is recorded; successor and replacement scope are explicit; unresolved conflicts persist visibly.
- **Allowed outcomes:** `APPLIED`, `NO_CHANGE`, `REJECTED`, `PARTIAL`, `UNKNOWN`, `QUARANTINED`, `FAILED`.
- **Failure/counterexample:** overwriting a Claim in place without lineage is not accountable revision. A3 does not decide ADR-0024 referential rules or reducer-v2 topology.

### 5.11 `DERIVE_BOUNDED_VIEW`

**Purpose:** construct a scoped characterization, projection, summary, State view, or comparison from available material.

- **Preconditions:** requested scope, selection rules, method/profile, inputs, omissions, equivalence criterion, and uncertainty treatment are declared.
- **Postconditions:** view remains linked to inputs and method; incompleteness and staleness are visible; the view does not rewrite represented history or become universal State.
- **Allowed outcomes:** `APPLIED`, `PARTIAL`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** reducer output is one laboratory view; it cannot define State for every substrate merely because it is deterministic.

### 5.12 `SELECT_FOR_USE`

**Purpose:** select material for a query, task, decision, or Context without confusing relevance with epistemic validity.

- **Preconditions:** query/task, requester Authority, Context, access restrictions, selection method, and relevant time boundary are declared.
- **Postconditions:** selected items, ranking/ordering if any, exclusions, uncertainty, and selection method are accountable; unsupported material remains labelled.
- **Allowed outcomes:** `APPLIED`, `PARTIAL`, `UNKNOWN`, `REJECTED`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** the top retrieval result can be false, superseded, or merely lexically similar; selection rank is not Knowledge.

### 5.13 `ACCOUNT`

**Purpose:** emit or make available a bounded Receipt/functional equivalent for an accountable operation, decision, failure, or non-action.

- **Preconditions:** operation identity/scope and available actor, input, method, authority, output, exclusion, failure, and limitation information are distinguishable.
- **Postconditions:** the Receipt states what happened or could not be established, under which boundary; it does not certify truth, completeness, or correctness by existence.
- **Allowed outcomes:** `APPLIED`, `PARTIAL`, `UNKNOWN`, `UNSUPPORTED`, `FAILED`.
- **Failure/counterexample:** a Receipt that omits rejected inputs or a partial failure can falsely imply a complete operation.

## 6. Handling dispositions

A3 needs a minimum way to express operational handling without finalizing the A6 knowledge lifecycle.

| Disposition | Meaning in A3 | Explicit non-meaning |
|---|---|---|
| `PENDING` | additional interpretation, scope, authority, or Evidence is required | false or rejected |
| `AVAILABLE` | usable for a declared purpose under policy | true, Knowledge, unrestricted, or permanent |
| `QUARANTINED` | isolated pending a stated condition or investigation | disproved or erased |
| `RESTRICTED` | availability is limited by policy, Authority, safety, privacy, or law | physically deleted or epistemically invalid |
| `REJECTED` | requested admission/use/change was not authorized under a stated rule | proposition is objectively false |
| `HISTORICAL_ONLY` | retained for lineage/accountability but not current operational use | erased or irrelevant to all questions |
| `UNAVAILABLE` | not accessible in the present scope, whether by loss, restriction, absence, or unsupported mapping | known not to exist |
| `UNKNOWN` | no stronger disposition can be warranted | `false`, `none`, or empty storage |

These are provisional handling terms. A6 may split, rename, or reject them.

## 7. Precondition and postcondition discipline

Every profile-defined transition must declare:

### Preconditions

- target and request identity or explicit ambiguity;
- required Context and temporal scope;
- relevant Source/Provenance availability;
- required Authority and policy;
- required capabilities and supported equivalence profile;
- known uncertainty and conflict;
- safety, privacy, access, and retention constraints where relevant.

### Postconditions

- exact semantic effect or explicit non-effect;
- changed and unchanged configuration facets;
- newly introduced uncertainty, loss, or approximation;
- lineage to prior positions;
- Authority and policy used;
- partial/failed operations and unresolved obligations;
- bounded accountability sufficient for later inspection.

A profile may group several transition families into one operation, but it must not hide which obligations were applied, skipped, approximated, or failed.

## 8. Failure and indeterminacy inventory

| Failure/indeterminacy | Required machine response |
|---|---|
| malformed or uninterpretable material | preserve failure boundary; do not fabricate semantic content |
| unknown or contested Source | represent unknown/alternatives; do not invent attribution |
| Provenance gap | expose the gap and affected confidence/authority |
| ambiguous identity or collision | keep candidates distinct until an authorized criterion resolves or scopes the ambiguity |
| insufficient Context | quarantine, narrow the Claim, or return unknown; do not silently widen scope |
| absent or contested Authority | no authorized semantic change; record refusal/pending state where accountable |
| incompatible policies or authorities | represent governance Conflict; do not pick a winner by implementation priority |
| dependent/repeated Evidence | preserve dependence; do not count copies as independent support |
| unresolved Conflict or Contradiction | keep plurality visible; resolution requires declared procedure/Authority |
| unsupported transition/profile capability | return `UNSUPPORTED` and disclose loss; do not emulate silently |
| partial physical execution | expose `PARTIAL`/`FAILED`; do not issue a success Receipt for unapplied effects |
| non-reproducible interpretation or selection | disclose method, variability, and uncertainty; do not claim deterministic equivalence |
| stale or incomplete derived view | expose source checkpoint/scope and omissions |
| unavailable Receipt capability | profile cannot claim full accountability equivalence for the affected operation |
| restricted or forgotten material | do not reconstruct or reveal content merely to satisfy replay/accountability claims |

A failure may itself become a Record or Evidence about process, but failure existence is not Evidence for an unrelated world Claim.

## 9. Determinism, reproducibility, and non-determinism

### 9.1 Deterministic boundary

A transition may be called deterministic only relative to declared:

- inputs and their identity;
- configuration scope;
- policy and Authority state;
- algorithm/procedure version;
- ordering and time assumptions;
- external dependencies;
- equivalence criterion.

Determinism of a procedure does not imply truth of its inputs or interpretation.

### 9.2 Reproducible boundary

Two executions may be reproducibly equivalent without identical physical states or bytes if a named profile defines:

- observable outputs;
- tolerated variation;
- preserved semantic distinctions;
- ordering guarantees;
- loss and uncertainty disclosure.

A3 does not define those profile thresholds; A8 must.

### 9.3 Legitimately non-deterministic or interpretive operations

The following may remain non-deterministic, plural, probabilistic, human-mediated, or substrate-dependent:

- perception and segmentation of continuous input;
- interpretation;
- identity matching under ambiguity;
- Evidence weighting;
- hypothesis generation;
- Conflict detection under vague language;
- selection/ranking;
- Authority decisions;
- reconstruction from incomplete Memory.

Such operations are not forbidden. They require declared variability, method, alternatives, uncertainty, and accountability. Non-determinism must not be hidden behind a deterministic-looking Receipt.

### 9.4 Irreproducible boundary

If a profile cannot preserve enough input, method, policy, or outcome information to support its declared equivalence, it must classify the operation as irreproducible or unsupported rather than claim replay.

## 10. Authority boundaries

| Authority role | May authorize | Does not automatically authorize |
|---|---|---|
| boundary/acquisition Authority | accepting contact from an interface or Source | truth, admission, unrestricted retention |
| representation Authority | creating/correcting a Record under a procedure | represented reality or Source authenticity |
| identity Authority | deciding identity/equivalence within a domain | identity in every Context or substrate |
| interpretive Authority | applying a declared interpretation framework | objective truth or exclusive meaning |
| epistemic Authority | applying a warranting standard in a domain | universal infallibility or operational use |
| admission/disposition Authority | availability, quarantine, restriction, or rejection for a purpose | Claim truth or permanent retention |
| relation Authority | asserting/accepting a Relation under a vocabulary | causal proof or unsupported transitivity |
| revision/Supersession Authority | changing a scoped position with lineage | erasing history or deciding ADR-0024 |
| access/forgetting Authority | restricting availability or authorizing forgetting under policy | proof of physical deletion unless separately evidenced |
| conformance Authority | certifying a profile against named obligations | production readiness, truth, or ecosystem legitimacy |

Authority may be distributed, procedural, contested, delegated, time-limited, or absent. The abstract machine enforces and exposes declared authority boundaries; it has no inherent authority to declare Claims true.

## 11. Ordering, history, concurrency, and partial order

A3 does not require one global total order.

A profile must declare which ordering relations it supports, such as:

- occurrence order;
- Observation or registration order;
- causal or dependency order;
- revision/Supersession lineage;
- authority decision order;
- local write/commit order;
- cross-substrate synchronization order;
- unknown or concurrent order.

Two transitions may be concurrent, incomparable, or later reconciled. A profile that imposes a total order for convenience must not claim that the imposed order is the order of represented reality.

History visibility requires a declared functional obligation, but A3 does not yet decide whether that obligation must be append-only Events, versioned Records, reversible procedures, physical traces, or another A8-approved equivalent.

## 12. Queries, views, selections, and explanations

The machine must keep four roles distinct:

```text
query/task
≠ selected material
≠ derived view
≠ epistemic judgment
```

A bounded explanation or Receipt should disclose, where material:

- request and Context;
- inputs considered and excluded;
- selection/derivation method;
- Authority and policy;
- relevant Provenance;
- uncertainty, conflicts, and unsupported operations;
- outcome and non-effect;
- checkpoint or temporal boundary;
- limitations and alternative interpretations.

A concise Receipt may reference other Records rather than repeat forbidden or restricted content. Accountability does not require exposing content that policy requires the system to forget or withhold.

## 13. Substrate mappings

### 13.1 Manual archival and deliberative substrate

A human institution uses paper Records, signed Source attributions, index references, quarantine folders, revision slips, authority registers, and decision Receipts.

Possible mapping:

- `R`: paper/physical Records;
- `P/C`: source sheets and contextual annotations;
- `I/L/E/U`: index cards and deliberative decisions;
- `V`: correction and Supersession slips;
- `D`: physical access zones and handling rules;
- `A`: signed operation/decision receipts.

It can preserve many A3 obligations without digital Events or reducers. Weaknesses may include slow comparison, incomplete global search, and limited reproducibility. Those limitations must be disclosed rather than treated as non-existence of the machine.

### 13.2 Adaptive analog or neuromorphic substrate

A physical adaptive system retains prior influence in changing dynamics, attractors, or distributed traces rather than discrete rows.

Possible mapping:

- Memory/availability may be realized through stable or metastable dynamics;
- interpretation and selection may be physical transformations;
- configuration facets may be observable only through probes or companion procedures;
- explicit Provenance, Authority, revision lineage, and Receipts may require an attached representational layer.

If the substrate cannot expose provenance gaps, distinguish revision from overwrite, or provide bounded accountability for high-impact operations, it may implement useful memory dynamics but cannot claim full A3 conformance.

### 13.3 Conventional digital Event-sourced laboratory

The current P1–C5 profile maps:

- commands/Events to some transition attempts and recorded changes;
- reducer Semantic State to one `DERIVE_BOUNDED_VIEW` result;
- stored Claims to a broad representation container;
- typed links to Relation positions;
- retrieval charge to one selection mechanism;
- Receipts to accountability outputs.

This mapping is valuable and testable. It remains one profile: Event vocabulary, append-only history, SQL persistence, Python classes, deterministic reducer replay, and exact JSON/bytes are not universal A3 requirements unless later A4/A8 review establishes specific obligations.

## 14. Mapping boundary with P1–C5

| A3 obligation | P1–C5 laboratory mechanism | Boundary |
|---|---|---|
| explicit representation | `Claim` object and stored payload | broad container, not final ontology |
| transition visibility | Event envelope and verbs | useful profile mechanism, not universal transition form |
| bounded ordering | append sequence/profile ordering | not represented-reality total order |
| derived view | deterministic reducer Semantic State | one scoped State representation |
| Relations | typed link Events/state | stored relation position, not truth proof |
| selection | charge/retrieval | relevance mechanism only |
| Revision/Supersession | versioning and Event semantics | ADR-0024/reducer-v2 remains unresolved and unauthorized |
| accountability | Receipt artifacts | bounded process evidence, not epistemic proof |
| cross-profile equivalence | PostgreSQL/SQLite comparison | shared Python lineage and named current contracts only |

A3 changes none of these mechanisms or their evidence.

## 15. Required non-equivalences

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

## 16. Open questions carried forward

1. Which configuration facets are truly minimal and which can be derived without semantic loss?
2. Must every accountable transition produce a durable Receipt, or can profiles aggregate low-risk operations?
3. What minimum history visibility is required when a substrate cannot provide replay?
4. Can a non-symbolic substrate expose Context and Provenance without a companion symbolic layer?
5. Is admission a Kernel primitive, a policy-layer operation, or an A6 derived lifecycle concept?
6. Which transitions require atomic semantic effect, and what is the substrate-neutral meaning of partial application?
7. How should concurrent, incomparable, or cyclic revision lineages be represented without deciding ADR-0024 prematurely?
8. Which authority roles are universal and which are domain-specific?
9. Can an operation be deterministic while identity, interpretation, or Authority inputs remain contested?
10. What equivalence observations are sufficient for manual, analog, probabilistic, quantum, or distributed profiles?
11. Which forms of forgetting can coexist with accountable history without retaining forbidden content?
12. Does full A3 conformance require all transition families, or should A8 define capability classes?
13. How should A3 interact with non-propositional skill, affective, sensorimotor, or embodied Memory?
14. Which failure outcomes must be externally observable versus inspectable only by an authorized auditor?

## 17. Falsification criteria for A3

A3 should be revised or rejected if review demonstrates that:

- the machine cannot represent an Observation without turning it into a Claim;
- a transition necessarily requires an Event envelope, reducer, global log, SQL row, JSON object, or digital processor;
- `K` can only be understood as one fully materialized global State;
- the transition families force one linear lifecycle or cannot express branching, repetition, quarantine, and unresolved plurality;
- admission, retrieval, deterministic derivation, or Authority silently becomes truth;
- failures or unsupported capabilities cannot remain distinct from false;
- revision requires silent overwrite or Supersession requires deletion;
- two contrasting substrates cannot map to the obligations without pretending identical mechanics;
- any system can claim conformance merely by renaming arbitrary operations, with no observable obligations;
- a required facet can be removed across contrasting substrates without loss of an A1/A2 distinction;
- full conformance requires exposing content that lawful forgetting/restriction requires withholding;
- the English/Russian pair develops materially different transition, authority, or failure semantics.

## 18. Non-goals

A3 does not:

- design tables, schemas, indexes, object models, graph shapes, or storage layouts;
- define APIs, commands, Event verbs, wire protocols, serialization, canonical bytes, or hashes;
- implement or specify reducer v2;
- require Event sourcing, append-only logs, global total order, snapshots, or replay as the only history model;
- define final A4 semantic laws;
- settle A5 identity, time, or change rules;
- define the final A6 knowledge lifecycle;
- define A7 conflict-resolution or belief-revision algorithms;
- define A8 conformance levels or profile equivalence thresholds;
- bind the machine to Titan, Crystal, Mentaury, an LLM, embeddings, SQL, JSON, Python, or a particular processor;
- change current runtime, contracts, fixtures, evidence, assertions, NK-EPI, maturity, or production status;
- decide Issue #18, Issue #74 / ADR-0024, or Track H source acceptance;
- claim that paper, analog, neuromorphic, quantum, biological, or future substrates already conform;
- promote A1–A3 to final Canon before independent and integrated review.

## 19. Status

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
