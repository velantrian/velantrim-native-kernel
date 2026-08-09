# 🧬 A2 — Knowledge and Memory Ontology

**[English](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) · [Русский](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md)**

> **Deliverable:** `A2` of the [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.md) blueprint (`ADR-0025`, [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88))  
> **Evidence boundary:** architecture research and provisional ontology only; no runtime, contract, evidence, assertion map, NK-EPI, maturity, or production change  
> **Review status:** first drafted slice; pending independent review and integrated blueprint review with A1 and A3–A10

## 1. Purpose and authority boundary

This document defines a technology-neutral working ontology for the concepts Native Kernel must be able to distinguish when representing knowledge, memory, support, context, change, uncertainty, and accountability.

It does **not** define Python classes, database tables, JSON objects, graph nodes, reducer state, Event envelopes, model prompts, embeddings, or APIs. It also does not claim that every term below must become a first-class stored object. A conforming future substrate may preserve a distinction through structures, dynamics, constraints, procedures, or another declared functional equivalent.

The classifications in this document are provisional:

- `CANDIDATE_PRIMITIVE` — presently appears irreducible enough to test as an architectural primitive;
- `DERIVED_CONCEPT` — presently requires a relation or composition of other concepts;
- `OPEN_QUESTION` — the distinction is required, but its primitive/derived status is not yet settled.

`Primitive` here means a meaning-level distinction, not a class, row, opcode, field, token, or physical storage unit. Final Canon status requires later reconciliation through A3–A10, independent review, integrated blueprint review, and operator decision.

## 2. Method and primitive test

A candidate primitive should survive the following tests:

1. **Substrate test:** its definition does not require SQL, JSON, Python, an LLM, embeddings, a graph, digital bytes, or a particular processor.
2. **Distinction test:** collapsing it into a neighbouring concept causes a material semantic error.
3. **Minimality test:** it cannot be removed without forcing another term to carry incompatible meanings.
4. **Role test:** its meaning is not merely the current laboratory mechanism that happens to implement it.
5. **Counterexample test:** the document identifies an observation or design that could weaken its primitive status.
6. **Translation test:** materially different substrates can preserve or explicitly translate the distinction without pretending to be identical.

These tests do not prove that a primitive is universal. They make the architectural hypothesis inspectable and falsifiable.

## 3. Alternative ontology structures considered

### 3.1 Linear promotion pipeline

```text
Signal → Observation → Interpretation → Claim → Hypothesis → Belief → Knowledge
```

**Strength:** easy to explain and useful for some acquisition workflows.  
**Failure risk:** suggests that every item moves forward, that later stages are automatically more authoritative, and that knowledge is produced by a single irreversible pipeline. Testimony, inherited records, formal derivation, memory recall, conflicting observations, and revision do not always follow this order.

**Decision for A2:** retain it only as one possible process view, not as the ontology itself.

### 3.2 Event-centred ontology

```text
Event → recorded Event → reducer → State → projection
```

**Strength:** matches the current P1–C5 laboratory and makes change history explicit.  
**Failure risk:** converts one implementation strategy into Canon, conflates occurrence with its record, and assumes that State must be reducer output.

**Decision for A2:** reject it as the default ontology. Event remains an open primitive question.

### 3.3 Relation-first semantic graph

```text
entities and roles connected by typed Relations
```

**Strength:** avoids a single pipeline and expresses provenance, evidence, conflict, revision, and context as scoped relations.  
**Failure risk:** a graph representation can hide the difference between a relation in represented reality, an asserted relation, and a stored edge. It can also turn every concept into a node/edge merely because a graph engine is available.

**Decision for A2:** use relation-first reasoning where helpful, without requiring a graph substrate.

### 3.4 Stratified role ontology

A2 uses the following organization as a drafting aid:

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

**Strength:** preserves distinctions without requiring a single lifecycle or storage form.  
**Failure risk:** terms can participate in several strata; treating the groups as disjoint types would be false.

**Working decision:** use this structure for navigation only. The grouping is not Canon and is explicitly open to replacement during integrated review.

## 4. Ontology inventory and provisional classification

| Concept | Provisional classification | Core reason |
|---|---|---|
| Signal | `CANDIDATE_PRIMITIVE` | detectable difference before assigned semantic content |
| Observation | `DERIVED_CONCEPT` | signal/contact registered under observer, method, and context |
| Record | `CANDIDATE_PRIMITIVE` | representation retained or made available for reference |
| Proposition | `CANDIDATE_PRIMITIVE` | assessable semantic content independent of assertion act |
| Claim | `DERIVED_CONCEPT` | proposition placed in an asserted or presented position |
| Interpretation | `DERIVED_CONCEPT` | meaning assignment under assumptions and context |
| Hypothesis | `DERIVED_CONCEPT` | provisional proposition organized for challenge or testing |
| Belief | `DERIVED_CONCEPT` | agent-relative commitment toward a proposition |
| Knowledge | `DERIVED_CONCEPT` | scoped epistemic position with declared support and authority rules |
| Memory | `OPEN_QUESTION` | continuity is required, but may be structure, process, capacity, or relation |
| Source | `CANDIDATE_PRIMITIVE` | attributed origin from which material is obtained |
| Evidence | `DERIVED_CONCEPT` | support/challenge role relative to a proposition and question |
| Provenance | `DERIVED_CONCEPT` | origin, custody, transformation, and gap relations over time |
| Context | `CANDIDATE_PRIMITIVE` | scope and conditions required to preserve meaning |
| Relation | `CANDIDATE_PRIMITIVE` | typed, scoped connection with declared semantics |
| State | `OPEN_QUESTION` | condition is required, but representation and derivation are not settled |
| Change | `CANDIDATE_PRIMITIVE` | scoped difference or transition under a comparator |
| Event | `OPEN_QUESTION` | useful representation of occurrence/change, not proven universal primitive |
| Conflict | `DERIVED_CONCEPT` | scoped tension among positions, requirements, or evidence |
| Contradiction | `DERIVED_CONCEPT` | strict incompatibility under aligned interpretation and scope |
| Uncertainty | `CANDIDATE_PRIMITIVE` | explicit limit on warranted discrimination or commitment |
| Revision | `DERIVED_CONCEPT` | reasoned change preserving declared lineage |
| Supersession | `DERIVED_CONCEPT` | scoped replacement relation without erasing history |
| Authority | `CANDIDATE_PRIMITIVE` | bounded capacity to assert, decide, admit, revise, or certify |
| Receipt | `DERIVED_CONCEPT` | bounded accountability representation of an operation or decision |

The table records a hypothesis, not a frozen type system.

## 5. Contact and capture concepts

### 5.1 Signal

- **Classification:** `CANDIDATE_PRIMITIVE`.
- **Working definition:** a detectable difference, variation, pattern, or influence capable of reaching an observer or interface before the Kernel assigns it semantic content.
- **It is not:** an Observation, meaning, Claim, Evidence, or truth. Noise can be a Signal; a Signal can remain uninterpreted.
- **Neighbour distinction:** an Observation is a registered encounter with a Signal under a method and context. A Record is a representation retained for later reference.
- **Allowed relations:** may be detected by a Source or observer, registered as an Observation, represented by a Record, transformed, filtered, lost, or associated with uncertainty.
- **Identity and lifecycle note:** signal identity may depend on continuity, causal origin, sampling frame, or declared equivalence; identical measurements do not prove one signal origin.
- **Minimum semantic obligations:** preserve acquisition boundary, relevant scope, observer/interface, transformation or filtering when known, and uncertainty about origin or completeness.
- **Unresolved questions:** can a purely internal state difference count as a Signal without a sender; when do continuous dynamics contain distinct signals; is Signal needed in every profile?
- **Falsification/counterexample:** if two materially different substrates preserve every required observation and provenance distinction without any signal-level concept, primitive status weakens. Treating a high retrieval score as a Signal from reality is a category error because it is generated by an access process.

### 5.2 Observation

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** a bounded result of an observer, instrument, process, or interface registering something under a declared method, time, and context.
- **It is not:** the observed reality, a Claim that the interpretation is correct, an explanation, or automatically Evidence.
- **Neighbour distinction:** Signal is what can be encountered; Observation is the scoped registration. Interpretation assigns meaning. Claim presents a Proposition.
- **Allowed relations:** may be based on Signals or testimony, represented in Records, interpreted, cited as Evidence, challenged by another Observation, and linked to observer or method limits.
- **Identity and lifecycle note:** repeated observations may be distinct even when their recorded values match. Correction of a method or timestamp may revise the Observation record without changing the external occurrence.
- **Minimum semantic obligations:** identify observer/interface, method, temporal and spatial scope where relevant, conditions, uncertainty, and separation between raw registration and later interpretation.
- **Unresolved questions:** whether testimony is an Observation, a Claim, or both in different roles; whether observer-less physical traces qualify; which observations require identity across transformations.
- **Falsification/counterexample:** a thermometer reading of `20°C` does not itself assert that a room is comfortable or that the instrument is calibrated. If the ontology cannot represent that gap, Observation has been collapsed into Claim or Interpretation.

### 5.3 Record

- **Classification:** `CANDIDATE_PRIMITIVE`.
- **Working definition:** a representation intentionally retained, stabilized, or made available so that some content, occurrence, process, or decision can be referred to beyond its immediate encounter.
- **It is not:** the represented occurrence, Memory by itself, a Claim by itself, Evidence by itself, or an authoritative history merely because it persists.
- **Neighbour distinction:** Memory concerns continuity and potential reactivation across time; Record concerns retained representation. Receipt is a special bounded accountability Record.
- **Allowed relations:** may represent Observations, Signals, Claims, Events, States, decisions, or other Records; may have Sources, Provenance, Context, revisions, restrictions, and loss.
- **Identity and lifecycle note:** physical copies can be different Records of equivalent content. One Record can change format while preserving declared content identity, or preserve bytes while changing interpretation.
- **Minimum semantic obligations:** disclose represented subject, representation boundary, creator or acquisition source when known, temporal scope, transformations, integrity limits, and whether the Record is authoritative for any declared purpose.
- **Unresolved questions:** whether transient neural or analog traces are Records; how long retention must last; when a transformed representation becomes a new Record.
- **Falsification/counterexample:** a stored row that cannot be interpreted, traced, or distinguished from a cache may be persistence without a semantically adequate Record. Storage presence alone does not establish Memory or knowledge.

## 6. Semantic position concepts

### 6.1 Proposition

- **Classification:** `CANDIDATE_PRIMITIVE`.
- **Working definition:** semantic content that can, within a declared interpretation and scope, be assessed as holding, not holding, undecidable, ill-formed, or otherwise evaluable independently of who presents it.
- **It is not:** a sentence string, Claim act, belief, truth value, Record, or database field.
- **Neighbour distinction:** a Claim places a Proposition in an asserted or presented position. Interpretation determines what content a representation expresses.
- **Allowed relations:** may be expressed by multiple Records, asserted by Claims, supported or challenged by Evidence, held as a Belief, organized as a Hypothesis, contradicted by another Proposition, or scoped by Context.
- **Identity and lifecycle note:** paraphrases may express one Proposition; identical text may express different Propositions under different Contexts. Final identity criteria belong to A5.
- **Minimum semantic obligations:** preserve content, scope, relevant interpretation, quantification or modality where material, and distinction from its encoding and claimant.
- **Unresolved questions:** whether questions, commands, values, and non-propositional memories need parallel semantic categories; whether probabilistic content is one Proposition or a distribution over propositions.
- **Falsification/counterexample:** “The bank is closed” expresses different propositions when `bank` means a financial institution or river bank. Byte equality cannot be the sole proposition identity rule.

### 6.2 Claim

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** a scoped semantic position in which a Source, agent, process, or Record presents a Proposition as holding, worth considering, or attributable to that Source under declared Context and Authority.
- **It is not:** truth, Knowledge, Evidence, a stored object, or the Proposition itself.
- **Neighbour distinction:** Proposition is the assessable content; Claim includes the act or position of presenting it. Observation records encounter; an Observation may ground a Claim but is not automatically one.
- **Allowed relations:** asserted by a Source, expressed in a Record, interpreted from material, supported/challenged by Evidence, held as Belief, classified as Hypothesis, revised, superseded, conflicted, or included in a Receipt.
- **Identity and lifecycle note:** two Sources can make distinct Claims expressing the same Proposition. A Source may repeat one Claim or issue a new Claim; the distinction requires declared identity and context rules.
- **Minimum semantic obligations:** preserve Proposition, claimant/attribution when known, Context, temporal scope, asserted force, Authority boundary, provenance, and uncertainty about extraction or attribution.
- **Unresolved questions:** whether questions, explicit unknowns, commands, and observations remain Claim roles or separate top-level categories; whether anonymous Claims are allowed and how their authority is represented.
- **Falsification/counterexample:** a million repetitions of “X” remain Claims and do not make X true. If the architecture promotes a Claim by storage count or popularity alone, it has collapsed repetition into Evidence and Claim into truth.

### 6.3 Interpretation

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** an assignment of meaning, role, reference, or explanatory frame to a Signal, Observation, Record, Proposition, relation, or situation under declared assumptions and Context.
- **It is not:** the input itself, objective truth, a guarantee of correct understanding, or necessarily a Claim made with authority.
- **Neighbour distinction:** Observation registers; Interpretation assigns meaning; Claim presents a Proposition. A model output may propose an Interpretation but does not authorize it.
- **Allowed relations:** produced by an interpreter or procedure, based on Records or Observations, constrained by Context, compared with alternative Interpretations, revised, used to formulate Claims or Hypotheses, and qualified by Uncertainty.
- **Identity and lifecycle note:** the same input can sustain several interpretations. A changed assumption can create a new Interpretation without altering the original Record.
- **Minimum semantic obligations:** disclose interpreted material, interpreter or method when relevant, assumptions, Context, alternatives considered, uncertainty, and any transformation between input and expressed meaning.
- **Unresolved questions:** when an interpretation becomes a Claim; how non-symbolic substrates expose interpretive assumptions; whether some perception is interpretation before explicit representation.
- **Falsification/counterexample:** a shadow interpreted as a person and later as a tree shows that the Observation can persist while Interpretation changes. An ontology that overwrites the observation loses the distinction.

## 7. Epistemic position concepts

### 7.1 Hypothesis

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** one or more Propositions held provisionally as candidate descriptions, explanations, mechanisms, or predictions and organized so they can be challenged, compared, tested, or revised.
- **It is not:** a weak synonym for Claim, a Belief, Knowledge, speculation without scope, or a guarantee of empirical testability in every domain.
- **Neighbour distinction:** Claim presents content; Hypothesis gives it a provisional investigative role. Belief is agent commitment. Knowledge is a stronger derived epistemic position under declared standards.
- **Allowed relations:** proposed by a Source, motivated by Observations, supported/challenged by Evidence, compared with alternatives, contradicted under aligned scope, revised, retained unresolved, rejected, or superseded.
- **Identity and lifecycle note:** modification of predictions, mechanism, or scope may create a revised Hypothesis or a new one; lineage must remain explicit.
- **Minimum semantic obligations:** state proposition(s), scope, assumptions, expected observations or consequences where applicable, potential defeating evidence, uncertainty, and status without silent promotion.
- **Unresolved questions:** treatment of non-empirical hypotheses; minimum falsifiability; whether composite hypotheses need first-class structure.
- **Falsification/counterexample:** a statement protected from every possible counterexample may still be a worldview Claim but is not an empirically falsifiable Hypothesis in that frame.

### 7.2 Belief

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** an agent- or system-relative disposition of acceptance, reliance, or commitment toward a Proposition, possibly with degree, reasons, and uncertainty.
- **It is not:** Knowledge, truth, consensus, a Claim made publicly, or a confidence score detached from an identified believer and scope.
- **Neighbour distinction:** Claim is presented assertion; Belief is internal or attributed commitment. Knowledge requires additional declared justification and authority conditions.
- **Allowed relations:** held by an agent, based on Evidence or habit, expressed as a Claim, revised, contradicted by another Belief or Proposition, acted upon, and qualified by uncertainty or Context.
- **Identity and lifecycle note:** beliefs can persist while reasons change, or change while the expressed words stay the same. A belief state requires temporal and agent scope.
- **Minimum semantic obligations:** identify believer or attributed system, Proposition, degree or mode where material, reasons/evidence if known, Context, time, uncertainty, and revision lineage.
- **Unresolved questions:** whether a Kernel implementation itself can literally hold beliefs or only represent attributed beliefs; comparability of belief degree across substrates.
- **Falsification/counterexample:** a person can sincerely believe a false proposition. Therefore Belief cannot be defined as Knowledge or truth.

### 7.3 Knowledge

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** a scoped epistemic position in which a Proposition or Claim is treated as sufficiently supported, attributable, and usable under declared standards, Context, Authority, and uncertainty boundaries.
- **It is not:** objective truth, permanent certainty, stored data, high retrieval rank, repeated use, model confidence, consensus, or a special physical format.
- **Neighbour distinction:** Belief is commitment that may lack adequate support. Hypothesis remains provisional for challenge. Knowledge requires an explicit warranting policy and remains revisable.
- **Allowed relations:** derived from Claims, Evidence, Provenance, Context, and Authority; may be contested, revised, superseded, restricted, forgotten, or reclassified as unknown without erasing history.
- **Identity and lifecycle note:** knowledge status can change while Proposition identity remains. Different communities or systems may assign different knowledge status under explicit standards without creating different reality.
- **Minimum semantic obligations:** state scope/domain, proposition, support and counterevidence, provenance quality, authority/policy, uncertainty, temporal validity, review triggers, and reasons for admission or withdrawal.
- **Unresolved questions:** whether `Knowledge` should be Canon or only a policy-defined profile status; minimum justification; relation to truth; whether formal, empirical, practical, and cultural knowledge require separate criteria.
- **Falsification/counterexample:** a highly ranked embedding neighbour or fluent LLM answer may be relevant but unsupported. Any design requiring an LLM, embeddings, SQL, JSON, digital bytes, or a specific processor to instantiate Knowledge fails the substrate-neutrality test.

### 7.4 Evidence

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** a role assigned to material, observations, records, results, or relations when they bear on the support, challenge, discrimination, or testing of a Proposition, Claim, Hypothesis, decision, or question under a declared method and Context.
- **It is not:** a Source, truth, proof by mere existence, repetition, popularity, relevance score, or every Record associated with a Claim.
- **Neighbour distinction:** Source is attributed origin; Evidence is a scoped epistemic role. The same Source can supply several evidence items, and one Record can be Evidence for one question but irrelevant to another.
- **Allowed relations:** supports, challenges, corroborates, undercuts, discriminates among, or fails to bear on propositions; originates from Sources; is represented in Records; has Provenance and uncertainty.
- **Identity and lifecycle note:** copying evidence does not create independent evidence. Independent observations may share content while remaining distinct evidence due to separate provenance.
- **Minimum semantic obligations:** identify target question/proposition, direction and type of bearing, method, Source and Provenance, independence/dependence, Context, uncertainty, limitations, and counterevidence.
- **Unresolved questions:** evidence aggregation rules; domain-specific standards; whether absence is evidence; how causal dependence is represented across profiles.
- **Falsification/counterexample:** one article copied by one thousand sites is repeated reporting from one Source, not one thousand independent evidence items. Repetition alone is not Evidence.

### 7.5 Uncertainty

- **Classification:** `CANDIDATE_PRIMITIVE`.
- **Working definition:** an explicit limitation on warranted discrimination, precision, prediction, interpretation, attribution, or commitment within a declared scope.
- **It is not:** falsity, ignorance alone, probability alone, conflict, model confidence, or a reason to invent a missing answer.
- **Neighbour distinction:** unknown is one possible epistemic condition; Uncertainty describes type and boundary. Conflict can exist with high certainty; uncertainty can exist without conflict.
- **Allowed relations:** qualifies Observations, Interpretations, Evidence, Claims, Hypotheses, Beliefs, Knowledge, Provenance, State, Change, and Receipts; may arise from noise, ambiguity, missing data, disagreement, model limits, or future contingency.
- **Identity and lifecycle note:** uncertainty statements are scoped and time-relative; reductions or increases require preserved reasons and methods.
- **Minimum semantic obligations:** declare object, type/source, scope, scale or ordering when meaningful, assumptions, known limits, and whether values are comparable.
- **Unresolved questions:** universal uncertainty algebra; comparison across qualitative, probabilistic, interval, fuzzy, or non-numeric forms; whether uncertainty is a qualifier or entity.
- **Falsification/counterexample:** `unknown` cannot be encoded as `false` merely because a boolean field is convenient. If a substrate cannot preserve the distinction, it does not preserve the ontology under that mapping.

## 8. Origin, scope, and governance concepts

### 8.1 Source

- **Classification:** `CANDIDATE_PRIMITIVE`.
- **Working definition:** an attributed entity, process, instrument, artifact, environment, or account from which a Signal, Observation, Record, Claim, or other material is obtained.
- **It is not:** Evidence, authority, authenticity, provenance, or truth. A Source can be unknown, deceptive, transformed, composite, or itself derived from other Sources.
- **Neighbour distinction:** Provenance is the traceable history connecting Sources, transformations, custody, and gaps. Authority is scoped capacity; a Source can lack authority.
- **Allowed relations:** originates, transmits, records, quotes, transforms, or aggregates material; has identity uncertainty; participates in provenance; may be independent or dependent on another Source.
- **Identity and lifecycle note:** source identity can be physical, organizational, procedural, anonymous, composite, or uncertain. Aliasing and succession belong to A5.
- **Minimum semantic obligations:** preserve attributed identity or explicit unknown, acquisition route, temporal and domain scope, role, transformations, independence assumptions, and authenticity limits.
- **Unresolved questions:** whether environments and emergent processes count as Sources; source identity across organizational change; anonymous and privacy-preserving attribution.
- **Falsification/counterexample:** a reputable Source can make a mistaken Claim, and an unreliable Source can occasionally provide true information. Source reputation is not Evidence by itself.

### 8.2 Provenance

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** the scoped, traceable account of origins, acquisition, attribution, custody, transformations, derivations, actors, methods, and explicit gaps through which represented material reached its present form.
- **It is not:** one `source` field, authenticity, truth, ownership, a hash chain alone, or a complete causal history.
- **Neighbour distinction:** Source names an attributed origin; Provenance relates origins and transformations over time. Lineage tracks continuity among versions or derivatives and may be one part of Provenance.
- **Allowed relations:** connects Sources, Records, Claims, Interpretations, Evidence, revisions, transformations, Receipts, and authority decisions; may be partial, contested, unknown, or independently attested.
- **Identity and lifecycle note:** provenance accounts can themselves be Records and Claims with provenance. Corrections should extend or revise the account without erasing earlier assertions.
- **Minimum semantic obligations:** represent known links and gaps, transformation boundaries, attribution confidence, temporal order where known, contested alternatives, and scope of completeness.
- **Unresolved questions:** minimum portable provenance vocabulary; recursion and compression; privacy-preserving provenance; when a provenance account is materially equivalent after migration.
- **Falsification/counterexample:** a valid digest proves correspondence to bytes under an algorithm, not who created them or whether the provenance story is true. Hash chain is not complete provenance.

### 8.3 Context

- **Classification:** `CANDIDATE_PRIMITIVE`.
- **Working definition:** the bounded conditions, frame, domain, assumptions, participants, temporal/spatial scope, task, jurisdiction, or discourse needed to preserve or evaluate meaning.
- **It is not:** arbitrary metadata, a prompt window, retrieval result, user session, or permission to make meaning implicit.
- **Neighbour distinction:** Context scopes interpretation and validity; Provenance explains origin and transformation. Authority is valid only within Context.
- **Allowed relations:** scopes Propositions, Claims, Observations, Evidence, Relations, States, Conflicts, Contradictions, Knowledge, actions, and Receipts; can overlap, nest, conflict, or be unknown.
- **Identity and lifecycle note:** contexts can evolve; same labels do not guarantee same conditions. Mapping between contexts must disclose loss and assumptions.
- **Minimum semantic obligations:** expose dimensions material to meaning, distinguish explicit from inferred context, preserve unknown context, and prevent silent scope widening.
- **Unresolved questions:** minimal context model; context identity and inheritance; when omission is harmless; representation of tacit social or embodied context.
- **Falsification/counterexample:** “It is safe” can be true for one dose, user, place, or time and false for another. Treating the Claims as contradictory without Context creates a false contradiction.

### 8.4 Authority

- **Classification:** `CANDIDATE_PRIMITIVE`.
- **Working definition:** a bounded capacity or recognized entitlement to assert, classify, admit, decide, revise, restrict, certify, or act within a declared domain and Context.
- **It is not:** truth, expertise in every domain, Source identity, popularity, technical permission, or operator approval outside the declared scope.
- **Neighbour distinction:** Source indicates origin; Authority indicates a scoped role or power. Evidence can justify a decision but does not itself exercise Authority.
- **Allowed relations:** held, delegated, revoked, contested, scoped, or audited; governs admission, revision, supersession, access, decisions, and Receipts; may require evidence or procedure.
- **Identity and lifecycle note:** authority can attach to persons, institutions, procedures, communities, or formal rules and can change over time. Delegation and succession require explicit lineage.
- **Minimum semantic obligations:** identify holder or procedure, granted powers, domain, Context, temporal validity, delegation basis, constraints, conflict-of-authority rules, and revocation status.
- **Unresolved questions:** authority without centralized actors; plural and competing authorities; legitimacy versus technical authorization; cross-substrate representation of procedural authority.
- **Falsification/counterexample:** an administrator may have technical permission to edit a database but no epistemic authority to declare a scientific Claim true. Capability is not semantic Authority.

## 9. Continuity and change concepts

### 9.1 Memory

- **Classification:** `OPEN_QUESTION`.
- **Working definition:** a continuity-enabling capacity, structure, process, or relation through which aspects of prior encounters, states, meanings, skills, commitments, or changes remain available for later reactivation, comparison, influence, reconstruction, or accountable forgetting.
- **It is not:** merely a stored Record, an archive, a database, a Claim, retrieval success, exact replay, or permanent retention.
- **Neighbour distinction:** Record is retained representation; Memory includes continuity, availability, transformation, access conditions, and revision/forgetting. State is a condition at a scope/time, not continuity itself.
- **Allowed relations:** may retain or reconstruct Records, Claims, relations, procedures, States, Experiences, or effects; can consolidate, decay, distort, be revised, restricted, superseded, forgotten, or remain inaccessible.
- **Identity and lifecycle note:** memory identity can depend on continuity despite changing physical representation. Exact copied bytes may be a new Record without being the same memory relation or lived continuity.
- **Minimum semantic obligations:** declare what continuity is preserved, for whom/what, across what interval, with what provenance, transformations, access limits, uncertainty, forgetting/restriction status, and equivalence claim.
- **Unresolved questions:** whether Memory is primitive, emergent, or a family of concepts; whether memory requires retrieval; how procedural, affective, distributed, and non-symbolic memory map to Kernel obligations; relation to Identity.
- **Falsification/counterexample:** a backup containing unreadable bytes is a stored Record but may not provide usable Memory. Conversely, an adaptive analog system may preserve influence from the past without discrete records, weakening any definition that equates Memory with stored entries.

### 9.2 State

- **Classification:** `OPEN_QUESTION`.
- **Working definition:** a bounded characterization of the condition of an entity, relation, system, or represented domain at a declared time, interval, perspective, and level of abstraction.
- **It is not:** automatically reducer output, a database snapshot, current truth, complete reality, or one universal global state.
- **Neighbour distinction:** Record represents; State characterizes condition. Change is a difference or transition between conditions. A projection may encode a State view but does not define State universally.
- **Allowed relations:** applies to entities and relations; is observed, represented, derived, compared, revised, uncertain, valid in Context, and connected by Change or Event representations.
- **Identity and lifecycle note:** state equality depends on chosen observables and equivalence. Two substrates can be equivalent for one contract while physically different.
- **Minimum semantic obligations:** declare subject, dimensions, scope, time, observer/derivation, uncertainty, completeness, authority, and equivalence relation used for comparison.
- **Unresolved questions:** whether State is primitive or always a view; minimal state for the abstract machine; treatment of continuous, probabilistic, quantum, or distributed conditions.
- **Falsification/counterexample:** the P1–C5 reducer result is one profile-specific semantic State representation. A conforming analog substrate may preserve relevant conditions without replaying Events into a map, so reducer output cannot define State.

### 9.3 Change

- **Classification:** `CANDIDATE_PRIMITIVE`.
- **Working definition:** a scoped difference, transition, transformation, appearance, disappearance, or reclassification between conditions under a declared comparator, temporal relation, and Context.
- **It is not:** necessarily an Event object, an overwrite, progress, causal explanation, or a change in represented reality merely because a Record changed.
- **Neighbour distinction:** State characterizes condition; Change relates conditions. Event is one possible representation of an occurrence or registered change. Revision is a semantically governed kind of change.
- **Allowed relations:** changes State, Record, Claim status, Belief, Knowledge, Provenance, Authority, Context, or Memory; may be observed, recorded, caused, contested, reversed, or uncertain.
- **Identity and lifecycle note:** the same transition can be decomposed into several changes or aggregated as one depending on scope. Comparator and granularity must be explicit.
- **Minimum semantic obligations:** identify subject, before/after or equivalent distinction, time/order, comparator, scope, uncertainty, reversibility where relevant, and difference between represented and representational change.
- **Unresolved questions:** whether change can be primitive without state; representation of continuous change; causal versus descriptive change; minimum ordering across substrates.
- **Falsification/counterexample:** correcting a timestamp changes a Record without proving that the represented occurrence changed. An ontology that cannot separate the two produces historical falsehoods.

### 9.4 Event

- **Classification:** `OPEN_QUESTION`.
- **Working definition:** a bounded representation or identification of an occurrence, action, transition, or registered change considered as a distinguishable unit under a declared Context and granularity.
- **It is not:** the occurrence itself, automatically append-only, a serialized envelope, a database row, truth, or a universal primitive merely because P1–C5 uses Event sourcing.
- **Neighbour distinction:** Change is a semantic difference or transition; Event packages an occurrence/change as a unit. Record is the retained representation of that Event. State need not be reduced from Events.
- **Allowed relations:** may represent Changes, actions, observations, decisions, revisions, or supersession; can have Sources, Provenance, Context, order, causal claims, uncertainty, and Receipts.
- **Identity and lifecycle note:** Event identity depends on granularity and boundary. One occurrence can be represented by many Event records; one Event can summarize many changes.
- **Minimum semantic obligations:** declare represented occurrence/change, boundary, time/order limits, participants/authority where relevant, provenance, uncertainty, and distinction between occurrence and record.
- **Unresolved questions:** whether every conforming Kernel requires Events; whether continuous or state-based substrates need a functional equivalent; minimum history visibility without event sourcing.
- **Falsification/counterexample:** if two substantially different substrate models preserve explicit change, provenance, revision, and accountability without event units, universal primitive status is refuted. P1–C5 proves only that Events are useful in that laboratory.

### 9.5 Revision

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** an explicit, reasoned modification of a Record, Interpretation, Claim, Belief, Knowledge position, Context assignment, or provenance account while preserving the relation to what was previously held or represented.
- **It is not:** silent overwrite, deletion, contradiction resolution by fiat, or necessarily Supersession.
- **Neighbour distinction:** Revision changes an item or position with lineage; Supersession declares a scoped successor/replacement. Correction is one possible revision reason.
- **Allowed relations:** revises interpretations, claims, beliefs, knowledge status, records, provenance, context, or uncertainty; cites reasons/evidence/authority; may lead to supersession or coexistence.
- **Identity and lifecycle note:** some revisions preserve semantic identity; others create a new item linked by lineage. A5 must define the boundary.
- **Minimum semantic obligations:** preserve prior state or an accountable equivalent, successor/revised content, reason, authority, time/order, affected scope, evidence, uncertainty, and reversibility.
- **Unresolved questions:** identity-preserving versus identity-creating revision; revision of non-symbolic memory; whether all revisions require durable history.
- **Falsification/counterexample:** replacing a Claim in place with no trace is not accountable Revision because the system cannot distinguish correction from manipulation.

### 9.6 Supersession

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** an explicit, scoped relation declaring that a later item, version, position, or rule replaces an earlier one for a stated purpose while the earlier history and its former scope remain identifiable.
- **It is not:** erasure, proof that the earlier item was false, universal invalidation, physical deletion, or automatic conflict resolution.
- **Neighbour distinction:** Revision is the change process; Supersession is a replacement relation. Contradiction can exist without supersession, and supersession can occur without contradiction.
- **Allowed relations:** links Records, Claims, Interpretations, policies, States, or knowledge positions; may be partial, contested, revoked, or chained; has Authority and Context.
- **Identity and lifecycle note:** successor identity must be distinguishable from lineage identity. Multiple scoped successors may be legitimate; global single-successor semantics are not assumed.
- **Minimum semantic obligations:** identify predecessor, successor, scope, reason, Authority, effective time/order, retained historical accessibility, and unresolved conflicts.
- **Unresolved questions:** multiple successors, branches, cycles, revocation, and migration semantics. Issue #74/ADR-0024 remains separate and is not decided here.
- **Falsification/counterexample:** a newer medical guideline can supersede an older one for current practice while the older record remains true as historical documentation. Superseded does not mean false or erased.

## 10. Relations and accountability concepts

### 10.1 Relation

- **Classification:** `CANDIDATE_PRIMITIVE`.
- **Working definition:** a typed, directed or otherwise structured, scoped connection asserted, observed, inferred, or defined between distinguishable relata under declared semantics.
- **It is not:** a graph edge, similarity score, causal proof, symmetric association, or truth merely because a label exists.
- **Neighbour distinction:** Conflict and Contradiction are specialized derived relations. Provenance is a family of origin/transformation relations. A stored link is a Record of a relation claim.
- **Allowed relations:** can connect any ontology concepts where the relation family declares domain, range, direction, scope, temporal meaning, authority, and uncertainty.
- **Identity and lifecycle note:** relation identity may include relata, type, direction, Context, time, and claimant. Equivalent labels do not guarantee equivalent semantics.
- **Minimum semantic obligations:** define relation meaning, relata roles, directionality, arity, scope, temporal validity, source/authority, uncertainty, and properties such as symmetry or transitivity only when justified.
- **Unresolved questions:** first-class versus asserted propositions; n-ary and higher-order relations; topology constraints; relation identity across migration.
- **Falsification/counterexample:** a vector similarity of 0.9 does not establish `CAUSES`, `SUPPORTS`, or `SAME_AS`. Retrieval association is not a semantic Relation unless explicitly interpreted and governed.

### 10.2 Conflict

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** a scoped condition in which claims, propositions, evidence, interpretations, requirements, authorities, actions, or states cannot be jointly accepted, satisfied, relied upon, or applied without unresolved tension under the relevant Context.
- **It is not:** necessarily logical Contradiction, error, falsity, disagreement by itself, or something that must be automatically resolved.
- **Neighbour distinction:** Contradiction is a stricter semantic incompatibility under aligned meaning, scope, and time. Conflict can arise from competing goals, evidence quality, authority, resources, or context mismatch.
- **Allowed relations:** exists among Claims, Evidence, Interpretations, Beliefs, Authorities, policies, actions, States, or Memories; can be detected, contested, explained, deferred, revised, or resolved by Authority.
- **Identity and lifecycle note:** a conflict depends on participants, dimensions, scope, and time. Reframing Context can dissolve a false conflict without changing the underlying Claims.
- **Minimum semantic obligations:** identify participants, conflict dimension, overlap assumptions, Context, evidence, uncertainty, detection method, resolution authority, and unresolved status.
- **Unresolved questions:** minimal conflict taxonomy; candidate versus established conflict; conflicts across incomparable contexts; conflict persistence and closure evidence.
- **Falsification/counterexample:** two eyewitnesses reporting different shirt colours may conflict due to lighting or memory without expressing formal negations. Conflict does not automatically mean contradiction.

### 10.3 Contradiction

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** a strict incompatibility between Propositions or commitments such that, under the same relevant interpretation, scope, time, modality, and assumptions, they cannot jointly hold or be satisfied.
- **It is not:** mere difference, low similarity, competing preferences, independent alternatives, temporal change, or conflict caused only by missing Context.
- **Neighbour distinction:** Conflict is broader. Contradiction requires semantic alignment sufficient to justify incompatibility.
- **Allowed relations:** relates Propositions, Claims, rules, or commitments; may be asserted, detected, challenged, scoped, resolved by revision, or retained unresolved.
- **Identity and lifecycle note:** contradiction identity depends on the proposition pair/set and alignment Context. Changing time or modality may remove the contradiction rather than resolve it.
- **Minimum semantic obligations:** expose the propositions, logical/semantic basis, aligned Context, time, modality, assumptions, uncertainty, and authority of the contradiction judgment.
- **Unresolved questions:** logic families; paraconsistent handling; graded or probabilistic contradiction; contradictions involving vague predicates; cross-language equivalence.
- **Falsification/counterexample:** “The door is open at 09:00” and “The door is closed at 10:00” are not contradictory when temporal scopes differ. A detector that ignores time produces false contradiction.

### 10.4 Receipt

- **Classification:** `DERIVED_CONCEPT`.
- **Working definition:** a bounded accountability Record describing a particular operation, decision, selection, transformation, refusal, revision, or result, including relevant inputs, exclusions, methods, authority, limits, and references.
- **It is not:** truth certificate, complete explanation, proof that the operation was correct, Evidence by default, compliance certification, or deletion proof.
- **Neighbour distinction:** Record is general retained representation. Receipt has an accountability role. Provenance may be included in a Receipt but is broader than one operation.
- **Allowed relations:** documents actions, decisions, selections, revisions, Events, Evidence considered, Context, Authority, outcomes, errors, and limitations; may itself become Evidence about process if independently verified.
- **Identity and lifecycle note:** Receipt identity should bind operation scope and declared content under a profile-specific commitment. Reissued or corrected Receipts require explicit relation.
- **Minimum semantic obligations:** identify operation, time/order, actor/authority, inputs and exclusions, method/profile, outputs, uncertainty, failures, limitations, and integrity/provenance boundary.
- **Unresolved questions:** minimum receipt across non-digital substrates; privacy and selective disclosure; durability; whether a receipt can exist without a persistent log.
- **Falsification/counterexample:** a Receipt showing that a search selected three Records does not prove those Records were sufficient, true, or the best possible selection. Receipt replayability is not epistemic validity.

## 11. Required non-equivalences

The following are mandatory distinctions for this provisional ontology and candidates for later A4 laws:

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

Additional consequences:

- a Claim may be true, false, partly applicable, context-dependent, undecidable, or not yet evaluated;
- a Source can be authoritative in one Context and irrelevant in another;
- Evidence can support one Proposition and challenge another;
- a Record can persist without remaining accessible as Memory;
- useful retrieval can surface false, superseded, or irrelevant-to-truth material;
- missing information remains unknown unless justified negative Evidence exists;
- revision changes an epistemic or representational position without rewriting prior history;
- authority can authorize a decision without making its premises objectively true.

## 12. Candidate relation grammar

The ontology can be provisionally expressed as roles and relations rather than a mandatory object hierarchy:

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

This grammar is descriptive, not an API, schema, storage model, or final formal logic.

## 13. Substrate thought experiments

### 13.1 Manual archival practice

A human team uses paper observations, signed testimony, index cards, cross-references, correction slips, and a decision ledger. It can distinguish Source, Record, Claim, Evidence, revision, supersession, and Receipt without SQL, JSON, an LLM, or digital Events. The profile may be slow and weakly reproducible, but the ontology remains intelligible.

### 13.2 Adaptive analog or neuromorphic substrate

A system preserves prior influence through changing physical dynamics rather than discrete stored rows. It may support Memory and State through stable attractors or adaptive traces, while changes are not naturally represented as append-only Event envelopes. A conforming mapping must expose which distinctions are preserved, approximated, or lost; it must not pretend that analog dynamics are serialized Events.

### 13.3 Conventional digital laboratory

The current P1–C5 implementation represents broad semantic roles inside `Claim`, records mutations as Events, derives reducer State, and emits Receipts. This is a valid bounded profile for testing some distinctions. It does not prove that its object boundaries are the ontology or that all future substrates must reproduce its mechanics.

These thought experiments demonstrate conceptual portability only. They are not implementation or conformance evidence.

## 14. Mapping to the current P1–C5 reference laboratory

| Laboratory concept | A2 interpretation | Boundary |
|---|---|---|
| `Claim` object | profile container that can encode Record, Proposition, Claim, Observation, Interpretation, Hypothesis, question, or unknown roles | current class shape is not the ontology |
| Event verbs | profile mechanism for explicit Change, relation, utilization, Supersession, and erasure markers | Event sourcing is not made universal |
| reducer Semantic State | one deterministic profile representation of State | State is not defined as reducer output |
| typed links | profile representation of Relation claims | edge existence does not prove relation truth |
| charge/retrieval | relevance and selection mechanism | relevance is not epistemic validity |
| Receipt | bounded accountability Record | Receipt is not truth or completeness proof |
| evidence bundles | evidence about exact repository runs | repository artifacts are not ontology-level Evidence for arbitrary world Claims |

No laboratory contract, history, fixture, evidence artifact, or assertion is changed by A2.

## 15. Open questions carried forward

1. Is Memory one primitive or a family covering retained representation, learned disposition, procedural capacity, and identity continuity?
2. Can Proposition identity be preserved without stable symbols or serialized content?
3. Is State fundamental, observer-relative, or always a derived view?
4. Is Event required for accountability, or can continuous/process substrates provide another explicit-change equivalent?
5. Which relation semantics are universal enough for Canon, and which must remain domain contracts?
6. What minimum standards distinguish Knowledge from justified Belief without claiming infallible truth?
7. Can Authority be represented without importing one legal or institutional worldview?
8. How can provenance remain useful while respecting privacy, forgetting, and restricted disclosure?
9. Which uncertainty forms can be compared across deterministic, probabilistic, analog, and social systems?
10. How should non-propositional content—skills, sensations, images, values, questions, and commands—relate to this ontology?
11. Which concepts require stable identity, and which can exist only as transient roles or relations?
12. Which current Glossary definitions must be reclassified after A3–A10 without rewriting P1–C5 history?

These questions remain explicit. A2 does not resolve A3 abstract-machine design, A4 laws, A5 identity/time, A6 lifecycle, or A7 revision policy.

## 16. Falsification criteria for A2

A2 should be revised or rejected if independent review demonstrates any of the following:

- a concept classified as primitive can be removed across contrasting substrates without loss of required distinctions;
- two concepts cannot be distinguished by any observable obligation or counterexample;
- a definition requires a current implementation mechanism to remain meaningful;
- the ontology cannot represent an observation without turning it into a Claim;
- the ontology cannot represent unsupported, false, disputed, or unknown Claims;
- Evidence cannot be separated from Source, repetition, or retrieval rank;
- Memory cannot include non-record-based continuity or accountable forgetting;
- State or Event definitions force event sourcing into every profile;
- Knowledge requires a model, encoding, database, or processor;
- Context cannot prevent false contradiction or silent scope widening;
- revision or supersession requires deleting prior history;
- authority silently becomes truth authority;
- the English/Russian pair develops materially incompatible classifications.

## 17. Non-goals

A2 does not:

- design tables, indexes, schemas, graph shapes, or storage layouts;
- design APIs, commands, wire protocols, or serialization;
- create or design reducer v2;
- select canonical bytes, JSON, hashes, or identity encoding;
- assert that Event sourcing or append-only history is universally required;
- bind the ontology to Titan, Crystal, Mentaury, or another ecosystem project;
- add LLM, embedding, vector, model-provider, or prompt assumptions;
- promote maturity, production readiness, or substrate-neutrality evidence;
- change runtime, contracts, evidence bundles, assertion map, or NK-EPI support;
- resolve Issue #18 or accept/reject ADR-0024;
- expand P1–C5 runtime semantics;
- define A3 abstract machine states or transitions;
- define A4 numbered laws;
- define A5 identity/time rules;
- define A6 lifecycle admission policy;
- define A7 conflict-resolution or belief-revision algorithm;
- claim that the provisional classifications are final Canon.

## 18. Status

```text
deliverable: A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
review: PENDING independent review and integrated blueprint review with A1 and A3-A10
next_content_slice: A3_ABSTRACT_NATIVE_KERNEL_MACHINE
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```
