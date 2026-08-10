# ⚖️ A4 — Semantic Laws and Invariants

**[English](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md) · [Русский](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md)**

> **Deliverable:** `A4` of the [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.md) blueprint (`ADR-0025`, [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88))  
> **Depends on:** provisional [A1](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md), [A2](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md), and [A3](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md)  
> **Law-set identity:** `nk-semantic-laws/A4-draft-1`  
> **Evidence boundary:** architecture research and provisional semantic obligations only; no runtime, contract, evidence, assertion-map, NK-EPI, maturity, or production change  
> **Review status:** first drafted slice; pending independent review and integrated blueprint review with A1–A3 and A5–A10

## 1. Purpose and authority boundary

A2 states the distinctions Native Kernel may need to represent. A3 states meaning-level transition obligations that may operate over those distinctions. A4 asks a narrower question:

> **Which semantic distinctions and preservation rules must not be silently collapsed, promoted, erased, widened, or reinterpreted if meaning is to survive changes of representation and substrate?**

A law in this document is therefore a **provisional meaning-level invariant**. It is not a Python assertion, SQL constraint, Event verb, reducer rule, graph axiom, model prompt, serialization requirement, physical law, or claim about objective reality.

The words `MUST`, `MUST NOT`, and `REQUIRED` below describe the obligations of this **draft law set**. They become final Canon only after independent and integrated A1–A10 review plus the later operator review required by ADR-0025.

This draft deliberately does not reuse the previously erroneous Notion-only label `nk-semantic-laws/0.1-draft`. No authoritative A4 law set existed under that identity. This file is the first GitHub-resident A4 candidate and uses a new explicit identity.

## 2. Law qualification test

A candidate belongs in A4 only if it survives all of these tests:

1. **Meaning-preservation test:** violating it can silently change what represented information means or how strongly it is warranted.
2. **Substrate test:** the statement can be expressed without requiring Python, SQL, JSON, Event sourcing, a graph, an LLM, embeddings, digital bytes, or one processor model.
3. **Distinctness test:** it is not merely an A2 definition restated as prose; it constrains what operations or mappings may collapse.
4. **Boundary test:** it does not prematurely decide detailed identity/time rules owned by A5, lifecycle rules owned by A6, conflict/revision algorithms owned by A7, or conformance thresholds owned by A8.
5. **Observable-obligation test:** a profile can disclose how it preserves, approximates, externalizes, or cannot support the law.
6. **Counterexample test:** at least one failure case can expose violation.
7. **Revision test:** the law remains versioned and falsifiable; A10 may weaken, split, replace, or reject it.

## 3. Law-set structure

The first-draft set contains **28 candidate laws** organized into six families:

```text
R — Representation and epistemic boundaries       A4-L01 … A4-L06
C — Context, provenance, and authority             A4-L07 … A4-L10
I — Identity, memory, time, and change             A4-L11 … A4-L19
T — Relations, conflict, and uncertainty           A4-L20 … A4-L22
V — Views, selection, and accountability           A4-L23 … A4-L25
S — Substrate, reproducibility, and conformance    A4-L26 … A4-L28
```

The number `28` is not a sacred target. It is the current deduplicated result of reconciling A1 durable qualities, A2 non-equivalences, A3 machine obligations, existing NK-EPI documentation targets, and the A4 plan. Integrated review may merge or split laws if their failure modes or observable obligations prove non-independent.

## 4. Representation and epistemic boundaries

### A4-L01 — Representation is not represented reality

**Statement:** A representation, model, Record, State view, relation encoding, or simulation MUST remain distinguishable from the object, process, occurrence, or relation it represents.

- **Rationale:** storage or successful modelling can preserve useful information without establishing ontological identity with the represented world.
- **Counterexample/falsifier:** a map, graph edge, or generated model behaves usefully but later proves incomplete or wrong while the represented situation existed independently.
- **Failure mode:** the system treats a stored symbol or derived model as reality itself and allows downstream conclusions to inherit unjustified certainty.
- **Observable obligation:** profiles MUST expose the representation boundary and must not describe encoded presence as proof that the represented state holds.
- **Exception/open uncertainty:** A5/A8 may permit identity claims under explicitly defined domains, but identity must be established by a declared rule rather than assumed from representation.

### A4-L02 — Observation, Claim, and explanation remain distinct

**Statement:** An Observation MUST NOT silently become a Claim, and an Observation or Claim MUST NOT silently become a complete explanation.

- **Rationale:** registration, assertion, and explanation carry different warrant and transformation burdens.
- **Counterexample/falsifier:** a sensor reports a temperature; an interpretation infers comfort; a causal explanation attributes the temperature to a failing system. These may differ while the initial reading remains unchanged.
- **Failure mode:** acquisition is promoted directly into asserted meaning or causal narrative without preserving the interpretive step.
- **Observable obligation:** profiles MUST be able to identify whether a position is registered, asserted, interpreted, or explanatory, or explicitly report that a distinction is unsupported.
- **Exception/open uncertainty:** domains may combine steps operationally, but the combined operation must expose which semantic roles were collapsed and under which declared policy.

### A4-L03 — Claim, admission, and availability are not objective truth

**Statement:** The existence, storage, admission, acceptance, availability, or operational use of a Claim MUST NOT by itself establish that the Claim is objectively true.

- **Rationale:** handling decisions and epistemic evaluation are different kinds of authority.
- **Counterexample/falsifier:** an admitted historical Claim is later superseded by stronger evidence while remaining historically accessible.
- **Failure mode:** `stored`, `admitted`, `approved`, or `available` becomes a hidden truth flag.
- **Observable obligation:** a profile MUST preserve the rule or status that caused admission/disposition separately from epistemic support and truth claims.
- **Exception/open uncertainty:** some formal systems may define truth relative to a closed formal interpretation; that scoped truth relation must still be distinguished from mere admission.

### A4-L04 — Evidence is a scoped role; Source or repetition is not Evidence by itself

**Statement:** Evidence MUST be represented as a role relative to a question, Proposition, Claim, Hypothesis, or decision. Source identity, reputation, copying, frequency, popularity, or repetition MUST NOT create independent Evidence by themselves.

- **Rationale:** the same material may bear on one question and be irrelevant to another, and copied reports can share one dependency lineage.
- **Counterexample/falsifier:** one article copied to one thousand sites remains dependent reporting rather than one thousand independent observations.
- **Failure mode:** evidence strength rises automatically with duplicate count or Source prestige without a declared bearing and independence model.
- **Observable obligation:** profiles MUST preserve the target, direction/type of bearing, provenance/dependence, Context, and uncertainty of Evidence or disclose loss.
- **Exception/open uncertainty:** domain-specific evidence aggregation is deferred to later contracts; A4 only forbids silent equivalence between repetition/Source and Evidence.

### A4-L05 — Belief, Hypothesis, and Knowledge remain distinct; semantic promotion is explicit

**Statement:** Belief, Hypothesis, Knowledge-candidate, and other epistemic roles MUST NOT be silently promoted into one another. Any promotion or withdrawal MUST identify the warranting policy, Context, Authority, support, uncertainty, and relevant counterevidence.

- **Rationale:** sincerity, usefulness, plausibility, confidence, or fluency do not carry the same epistemic burden as knowledge under a declared standard.
- **Counterexample/falsifier:** an agent sincerely believes a false proposition; an LLM returns a fluent answer with high confidence but weak provenance.
- **Failure mode:** model confidence, consensus, storage duration, repeated use, or workflow stage becomes an implicit knowledge gate.
- **Observable obligation:** profiles MUST expose the prior and resulting epistemic role and the rule/authority for the transition.
- **Exception/open uncertainty:** whether `Knowledge` remains a final Canon concept or a profile-defined status is explicitly deferred to integrated review.

### A4-L06 — Unknown, missing, unsupported, partial, and failed are not False

**Statement:** Absence of information, unanswered questions, unsupported capability, incomplete operations, indeterminacy, or execution failure MUST NOT be silently encoded as semantic falsehood.

- **Rationale:** lack of warrant for `true` is not warrant for `false`.
- **Counterexample/falsifier:** a profile cannot observe a phenomenon and records `false`; a later capable profile observes it without any change in represented reality.
- **Failure mode:** booleans, empty collections, nulls, timeouts, or unsupported features erase the distinction between unknown and false.
- **Observable obligation:** profiles MUST preserve an explicit unknown/partial/unsupported/failure boundary where the distinction is material.
- **Exception/open uncertainty:** a closed-world domain MAY define absence-as-false only when that rule, scope, completeness assumption, and authority are explicit.

## 5. Context, provenance, and authority

### A4-L07 — Meaning-relevant Context cannot be silently widened or discarded

**Statement:** Context dimensions material to interpretation, validity, identity, relation semantics, authority, or applicability MUST remain attached or explicitly translated; a narrower scoped position MUST NOT silently become universal.

- **Rationale:** the same expression can change meaning across time, domain, jurisdiction, observer, assumptions, modality, or task.
- **Counterexample/falsifier:** “it is safe” changes truth value across dose or user; two temporal Claims appear contradictory only after time scope is discarded.
- **Failure mode:** migration, summary, retrieval, or normalization drops scope and creates a stronger or different Claim.
- **Observable obligation:** profiles MUST identify preserved Context, inferred Context, unknown Context, and material loss or widening.
- **Exception/open uncertainty:** harmless Context omission is domain-specific and must be justified by an equivalence rule rather than assumed globally.

### A4-L08 — Provenance and provenance gaps remain explicit; transformation is not origin

**Statement:** Known origin, acquisition, custody, transformation, derivation, and material provenance gaps MUST remain representable. A transformation, assembly, reconstruction, hash chain, or successful reproduction MUST NOT by itself prove ultimate or original provenance.

- **Rationale:** continuity stories can be fabricated by filling missing links with convenient assumptions.
- **Counterexample/falsifier:** exact bytes verify a digest while authorship remains unknown; a reconstructed artifact behaves identically but does not establish historical origin.
- **Failure mode:** missing lineage is silently replaced by invented attribution, originlessness, or a preferred explanation.
- **Observable obligation:** profiles MUST expose known provenance links, contested alternatives, explicit gaps, transformation boundaries, and completeness limits.
- **Exception/open uncertainty:** privacy-preserving provenance may intentionally hide details, but the existence and scope of hidden/redacted provenance must remain distinguishable from known completeness.

### A4-L09 — Authority is scoped and role-specific

**Statement:** Authority MUST be represented as bounded by role, domain, Context, time, delegation, and policy where material. Authority in one role MUST NOT silently imply authority in another; Source identity or technical permission MUST NOT become universal epistemic authority.

- **Rationale:** acquisition, interpretation, epistemic assessment, admission, relation, revision, access, and conformance decisions have different mandates.
- **Counterexample/falsifier:** an administrator may delete access but lack authority to declare a Claim false; a sensor may be an authoritative measurement Source but not a policy authority.
- **Failure mode:** possession of credentials, authorship, popularity, or operator access becomes a universal permission to assert truth or rewrite meaning.
- **Observable obligation:** accountable operations MUST expose the authority role and scope used or explicitly report missing/contested authority.
- **Exception/open uncertainty:** a profile may centralize roles in one actor, but role boundaries must remain semantically identifiable.

### A4-L10 — Current inability is not universal impossibility

**Statement:** Failure of a current observer, method, profile, era, or substrate to observe, reproduce, represent, compute, or verify something MUST NOT silently become a universal impossibility claim.

- **Rationale:** capability limits are properties of frames and methods unless a stronger formal argument is supplied.
- **Counterexample/falsifier:** an earlier instrument cannot resolve a signal that a later instrument detects.
- **Failure mode:** `UNSUPPORTED`, `cannot verify`, or `not observed` is rewritten as `impossible` or `does not exist`.
- **Observable obligation:** impossibility claims MUST declare the frame, assumptions, method, and grounds; profile limits remain profile limits.
- **Exception/open uncertainty:** formal impossibility/non-resolvability MAY be represented within an explicit formal system with assumptions and proof provenance.

## 6. Identity, memory, time, and change

### A4-L11 — Semantic identity is not storage or physical identity

**Statement:** Semantic identity MUST NOT depend solely on row identity, memory address, file path, process identity, storage location, database-generated identifier, or other substrate-local placement.

- **Rationale:** meaning should survive technology replacement when declared identity is preserved.
- **Counterexample/falsifier:** a Claim migrates from one store to another without changing its semantic referent or proposition.
- **Failure mode:** migration creates a new semantic entity merely because physical placement or backend identifier changed.
- **Observable obligation:** profiles MUST state which identity relation they preserve and which substrate-local identifiers are non-semantic.
- **Exception/open uncertainty:** final semantic/content/record/lineage identity rules belong to A5; A4 only forbids unmarked collapse into physical identity.

### A4-L12 — Equal bytes, hashes, or text do not alone prove semantic identity

**Statement:** Byte equality, hash equality, text equality, or equivalent low-level representation MUST NOT by itself prove sameness of semantic entity, Source, continuity, Record, Claim act, or Context.

- **Rationale:** identical encodings may refer to different contexts or independent occurrences, while different encodings may express equivalent semantic content.
- **Counterexample/falsifier:** two Sources independently issue identical text; one sentence has different referents under different Contexts.
- **Failure mode:** deduplication merges distinct provenance/identity positions or treats format change as semantic change.
- **Observable obligation:** any equality-to-identity promotion MUST name the identity criterion and scope.
- **Exception/open uncertainty:** content-addressed profiles may define a content-identity relation from bytes/hashes, but MUST NOT silently widen it into all other identity relations.

### A4-L13 — Memory is not merely Record, archive, retrieval, or exact replay

**Statement:** Memory MUST NOT be defined solely as persistent Records, archive size, retrieval success, cache presence, or exact replay capability.

- **Rationale:** continuity may be structural, procedural, adaptive, distributed, analog, reconstructed, restricted, or partially inaccessible.
- **Counterexample/falsifier:** unreadable backup bytes persist without usable continuity; an adaptive analog system preserves influence from prior states without discrete stored records.
- **Failure mode:** a database or retrieval index self-defines as the universal memory ontology.
- **Observable obligation:** profiles claiming Memory equivalence MUST state what continuity, reactivation/influence, transformation, access, uncertainty, and forgetting boundary they preserve.
- **Exception/open uncertainty:** whether Memory is primitive, emergent, or a family of contracts remains open for A5/A6/A8.

### A4-L14 — Material temporal dimensions remain distinguishable

**Statement:** Occurrence/valid time, Observation time, Record/knowledge time, decision time, write/commit order, and other materially different temporal relations MUST NOT be silently collapsed into one overloaded timestamp or version.

- **Rationale:** chronology of the represented world and chronology of representation are different relations.
- **Counterexample/falsifier:** correcting a Record timestamp today does not move the historical occurrence to today.
- **Failure mode:** migration or querying confuses when something held with when it was learned or written.
- **Observable obligation:** profiles MUST preserve or explicitly translate the temporal dimensions required by the declared domain and disclose loss.
- **Exception/open uncertainty:** the exact temporal model, naming, partial-order semantics, and identity effects are owned by A5.

### A4-L15 — Imposed storage or write order is not automatically the order of represented reality

**Statement:** A total order imposed for serialization, storage, replication, locking, or deterministic execution MUST NOT be represented as occurrence, causal, or semantic order unless that relation is separately warranted.

- **Rationale:** concurrent or incomparable changes can be serialized by an implementation for convenience.
- **Counterexample/falsifier:** two independent observations are written sequentially because one database must choose a commit order.
- **Failure mode:** implementation sequence manufactures causality or precedence in the represented domain.
- **Observable obligation:** profiles MUST name the order relation being recorded and distinguish unknown/concurrent/incomparable order where required.
- **Exception/open uncertainty:** A5/A8 will define minimum order relations and acceptable translation across substrates.

### A4-L16 — Revision and semantic Change preserve explicit lineage

**Statement:** When a represented position is revised, corrected, transformed, or replaced, the relationship between predecessor and successor MUST remain explicit or an explicit authorized forgetting/loss boundary MUST be recorded.

- **Rationale:** accountable change requires knowing what changed relative to what.
- **Counterexample/falsifier:** a medical recommendation is updated; the new recommendation is current while the old one remains historically meaningful.
- **Failure mode:** successive versions are detached, making audit, comparison, conflict analysis, and provenance reconstruction ambiguous.
- **Observable obligation:** profiles MUST expose predecessor/successor or equivalent continuity and the scope/reason/authority of the change, or disclose that lineage is unsupported/lost.
- **Exception/open uncertainty:** detailed branching, aliasing, migration, successor multiplicity, and identity preservation rules belong to A5/A7 and do not decide ADR-0024.

### A4-L17 — Revision is not silent overwrite

**Statement:** A semantic Revision MUST NOT be represented solely as an in-place replacement that makes the prior position indistinguishable from a state in which it never existed.

- **Rationale:** silent overwrite destroys evidence of epistemic change and can fabricate a cleaner historical narrative.
- **Counterexample/falsifier:** a Claim changes after contrary Evidence; a later reader must be able to distinguish revision from an original unchanged Claim unless an authorized forgetting boundary applies.
- **Failure mode:** current value storage erases the fact, reason, authority, or uncertainty of change.
- **Observable obligation:** profiles MUST preserve history visibility or an A8-approved functional equivalent sufficient to distinguish accountable revision from never-existed history.
- **Exception/open uncertainty:** A4 does not require append-only storage, Event sourcing, immutable bytes, or permanent retention of content that policy lawfully requires to forget.

### A4-L18 — Supersession is not deletion and is not falsity

**Statement:** Supersession MUST represent scoped replacement or preference without silently implying that the predecessor is erased, physically deleted, globally false, or historically invalid.

- **Rationale:** an older position can remain true as historical documentation while no longer governing current practice.
- **Counterexample/falsifier:** an old standard is superseded by a new version but remains an accurate statement of the earlier standard.
- **Failure mode:** `superseded` is treated as `false` or content disappearance, destroying historical interpretation.
- **Observable obligation:** profiles MUST preserve the supersession scope/effective relation separately from deletion, restriction, truth assessment, and historical access.
- **Exception/open uncertainty:** physical/cryptographic deletion and forgetting semantics remain separate concerns; reducer-v2 successor topology remains operator-controlled through Issue #74/ADR-0024.

### A4-L19 — Change in representation is not automatically change in the represented occurrence

**Statement:** Correcting, migrating, re-encoding, reinterpreting, annotating, or reclassifying a representation MUST NOT by itself assert that the represented object or historical occurrence changed.

- **Rationale:** representational Change and represented Change are distinct semantic relations.
- **Counterexample/falsifier:** fixing a typo or timezone in a Record modifies the Record while leaving the original occurrence unchanged.
- **Failure mode:** metadata edits rewrite represented history or trigger false causal/temporal conclusions.
- **Observable obligation:** profiles MUST distinguish representational change from asserted change in represented reality where the difference matters.
- **Exception/open uncertainty:** some operations intentionally change both; they must state both effects rather than infer one from the other.

## 7. Relations, conflict, and uncertainty

### A4-L20 — Relation representation is not represented relation reality; similarity is not semantic relation by itself

**Statement:** A stored edge, association, co-occurrence, vector similarity, proximity score, shared identifier, or inferred link MUST NOT silently become a semantic Relation such as `SAME_AS`, `CAUSES`, `SUPPORTS`, or `CONTRADICTS` without declared interpretation, scope, provenance, and authority.

- **Rationale:** access and representation mechanisms create useful associations that may not hold in represented reality.
- **Counterexample/falsifier:** two documents are embedding-neighbours but discuss mutually unrelated causes.
- **Failure mode:** graph topology or retrieval similarity self-promotes into ontological or causal truth.
- **Observable obligation:** profiles MUST identify relation type/roles/direction/scope and whether it is asserted, observed, inferred, or merely access-derived.
- **Exception/open uncertainty:** domain relation vocabularies and topology constraints are deferred to contracts/A7/A8.

### A4-L21 — Conflict is not necessarily Contradiction; scope must align

**Statement:** Conflict MUST NOT be classified as strict Contradiction unless relevant interpretation, scope, time, modality, assumptions, and compared propositions are sufficiently aligned to warrant incompatibility.

- **Rationale:** tension can arise from evidence, goals, authority, context mismatch, or temporal change without logical negation.
- **Counterexample/falsifier:** “open at 09:00” and “closed at 10:00” differ but are not contradictory under aligned time.
- **Failure mode:** detectors manufacture contradictions by discarding Context or treating low similarity/difference as negation.
- **Observable obligation:** contradiction assessments MUST expose the alignment basis and uncertainty; broader conflicts remain typed as such.
- **Exception/open uncertainty:** logic family, graded contradiction, paraconsistency, and domain conflict taxonomies belong to A7.

### A4-L22 — Conflict detection is not conflict resolution; unresolved plurality remains visible

**Statement:** Detecting Conflict, Contradiction, competing Evidence, authority disagreement, or unresolved plurality MUST NOT silently select a winner, average positions, delete alternatives, or imply resolution.

- **Rationale:** detection and resolution require different authority and warrant.
- **Counterexample/falsifier:** two credible observations remain unresolved because available Evidence cannot discriminate between them.
- **Failure mode:** a ranker, reducer, majority vote, newest-write rule, or model confidence silently closes the conflict.
- **Observable obligation:** profiles MUST preserve unresolved participants, conflict basis, uncertainty, and resolution status until an authorized resolution/revision is represented.
- **Exception/open uncertainty:** resolution strategies, reversibility, and belief revision are A7 responsibilities.

## 8. Views, selection, and accountability

### A4-L23 — Derived views do not rewrite history or become universal State

**Statement:** A projection, summary, cache, index, query result, reconstructed view, or other derived State MUST remain linked to its inputs/method/scope and MUST NOT silently replace the represented history or declare itself the one complete world State.

- **Rationale:** derived material is shaped by selection, abstraction, staleness, and method.
- **Counterexample/falsifier:** two legitimate queries derive different scoped State views from the same retained material.
- **Failure mode:** disposable projection becomes authoritative because it is fast, convenient, current-looking, or deterministic.
- **Observable obligation:** profiles MUST disclose derivation scope, inputs, method/profile, material omissions, staleness/uncertainty, and reconstruction/equivalence boundary.
- **Exception/open uncertainty:** whether reconstructability is required through replay, recomputation, reversible dynamics, or another functional equivalent is deferred to A8.

### A4-L24 — Retrieval, ranking, selection, utility, recency, and disposition are not epistemic validity

**Statement:** Relevance, similarity, rank, activation, frequency of use, utility outcome, recency, operational availability, admission, quarantine, or selection MUST NOT independently determine whether a Claim is epistemically valid or Knowledge.

- **Rationale:** access optimization and task usefulness answer different questions from support and truth.
- **Counterexample/falsifier:** the top search result is obsolete or false; a useful heuristic works while resting on a false explanation.
- **Failure mode:** retrieval score, “charge”, newest-write, user preference, or successful outcome becomes hidden evidence.
- **Observable obligation:** profiles MUST keep selection/disposition signals distinct from epistemic assessments and preserve unsupported/contested labels through selection.
- **Exception/open uncertainty:** Evidence about utility may bear on practical Claims if explicitly modelled as Evidence for that question; utility is not evidence for unrelated truth Claims by default.

### A4-L25 — Receipt and bounded accountability are not correctness, completeness, or truth

**Statement:** A Receipt, audit record, explanation, trace, proof-of-execution, or reproducibility record MUST NOT certify semantic truth, task sufficiency, completeness, compliance, or correctness merely by existing.

- **Rationale:** a perfectly recorded process can execute a flawed method, omit relevant inputs, or act on false Claims.
- **Counterexample/falsifier:** a deterministic Receipt faithfully records a selection that omitted critical Evidence.
- **Failure mode:** auditability is confused with correctness and partial failures or exclusions disappear from the account.
- **Observable obligation:** accountability outputs MUST state their scope, inputs, methods, exclusions, authority, failures, uncertainty, and known limitations where material.
- **Exception/open uncertainty:** stronger proofs/certificates may be defined by later contracts, but their exact claim boundary must be explicit and separately evidenced.

## 9. Substrate, reproducibility, and conformance

### A4-L26 — History visibility is required; Event sourcing, reducer replay, and global total order are not universal mechanisms

**Statement:** A profile MUST preserve enough change/history visibility to distinguish accountable revision, lineage, and relevant prior positions, or explicitly disclose inability. A4 does **not** require Event sourcing, append-only serialized logs, reducer replay, immutable rows, or one global total order as universal mechanisms.

- **Rationale:** history visibility is a semantic objective; current Event/reducer machinery is only one implementation strategy.
- **Counterexample/falsifier:** a manual archival process or adaptive substrate preserves accountable prior-state relations without serialized Events.
- **Failure mode:** P1–C5 mechanics are copied into Canon by inertia, excluding materially different substrates that could preserve the same obligation.
- **Observable obligation:** profiles MUST state the functional mechanism by which relevant prior positions/change lineage remain inspectable and which history information can be lost or forgotten.
- **Exception/open uncertainty:** minimum portable history commitment, replay/reconstruction equivalents, and lawful forgetting trade-offs belong to A8/A10.

### A4-L27 — Determinism and reproducibility are not truth or physical identity; equivalence is named

**Statement:** Deterministic execution MUST NOT imply true output. Reproducibility MUST NOT require identical physical states or bytes unless a named profile says so. Any cross-run or cross-substrate equivalence claim MUST state observables, tolerated variation, ordering assumptions, uncertainty, and loss.

- **Rationale:** deterministic procedures can deterministically process false inputs, while probabilistic or analog systems can preserve a declared semantic equivalence without bit identity.
- **Counterexample/falsifier:** two substrates produce semantically equivalent bounded outcomes through different physical states; one deterministic algorithm repeats the same wrong classification.
- **Failure mode:** byte identity is treated as the only conformance model or deterministic output is promoted to truth.
- **Observable obligation:** profiles MUST name the equivalence relation and disclose non-equivalence/irreproducibility rather than claiming generic sameness.
- **Exception/open uncertainty:** concrete equivalence levels and thresholds are A8 responsibilities.

### A4-L28 — Optimization, migration, and profile substitution must not silently change meaning; conformance is not production authorization

**Statement:** Performance optimization, compression, migration, storage replacement, language/runtime change, model substitution, hardware change, or profile replacement MUST NOT silently alter accepted semantic distinctions or obligations. Any change in meaning, approximation, unsupported capability, or loss MUST be declared. Passing a named conformance profile MUST NOT by itself imply production readiness or universal substrate support.

- **Rationale:** technology replacement is the central stress test of Native Kernel; optimization pressure must not become semantic authority.
- **Counterexample/falsifier:** a faster index drops provenance or conflict status; a migrated system preserves content but collapses `unknown` into `false`.
- **Failure mode:** semantic drift is hidden as a backend migration, optimization, or “equivalent” implementation change.
- **Observable obligation:** migration/profile reports MUST identify preserved obligations, approximations, losses, unsupported laws, and the named equivalence/conformance scope.
- **Exception/open uncertainty:** A8 defines the formal substrate-independence contract and conformance levels; production authorization remains a separate governance/evidence decision.

## 10. Cross-law consequences

The law set implies several higher-level disciplines without creating new independent laws:

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

These compact formulas are explanatory aliases. The numbered `A4-Lxx` statements are the authoritative units of this draft.

## 11. Relationship to A2 ontology

A4 does not replace A2 definitions. It constrains how A2 roles may be transformed or collapsed:

| A2 area | Principal A4 laws |
|---|---|
| Signal / Observation / Record | L01, L02, L06, L19 |
| Proposition / Claim / Interpretation | L01–L03, L05, L07 |
| Hypothesis / Belief / Knowledge / Evidence / Uncertainty | L04–L06, L22, L24 |
| Source / Provenance / Context / Authority | L07–L10 |
| Memory / State / Change / Event / Revision / Supersession | L11–L19, L23, L26 |
| Relation / Conflict / Contradiction | L20–L22 |
| Receipt | L25 |

This mapping does not declare every A2 classification final.

## 12. Relationship to A3 abstract machine

The laws constrain A3 transition families without turning them into APIs or Event verbs:

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

A profile may combine transitions, but it cannot claim full preservation while silently violating a law relevant to the combined operation.

## 13. Contrasting substrate thought experiments

### 13.1 Manual archival and review process

A human-operated archive can preserve A4 obligations through labelled documents, provenance sheets, scoped authority, revision ledgers, uncertainty markers, and explicit conflict files. It may have no SQL, hashes, reducer, or replay engine. It fails A4 only where required distinctions or accountability become uninspectable, not because it lacks digital Event sourcing.

### 13.2 Adaptive analog or neuromorphic substrate

An adaptive physical system may preserve continuity and influence from prior states without discrete Records for every transition. To claim A4 preservation it must still expose or externally account for materially required distinctions—such as uncertainty, authority, provenance gaps, revision lineage, or declared loss—through an accepted functional mapping. Exact byte replay is not assumed.

### 13.3 Conventional digital Event-sourced laboratory

The current P1–C5 Python/PostgreSQL/SQLite lineage can map many A4 obligations through Events, reducer state, projections, Receipts, and explicit profiles. That mapping remains one bounded laboratory. Its Event vocabulary, serialization, global/local sequencing, SQL schemas, and reducer mechanics are not promoted into A4 laws merely because they are executable today.

## 14. Failure patterns A4 is designed to expose

A profile or document violates the intent of this draft when it:

- equates persistence with truth or Knowledge;
- fabricates Source/Context/provenance to satisfy a schema;
- turns `unknown`, `unsupported`, or failure into `false`;
- treats repetition, popularity, model confidence, relevance, recency, or utility as Evidence by themselves;
- merges semantic identity with backend identity;
- treats write order as reality/causal order;
- rewrites prior epistemic positions without accountable lineage;
- equates Supersession with deletion or falsity;
- turns similarity or stored edges into semantic/causal Relations without interpretation;
- detects Conflict and silently resolves it;
- lets projections or summaries become authoritative history;
- treats Receipts or deterministic replay as correctness proof;
- requires Event sourcing only because the reference laboratory uses it;
- claims substrate neutrality without naming preserved obligations and disclosed loss;
- treats conformance or test success as production authorization.

## 15. What A4 intentionally leaves to later deliverables

A4 does not settle:

- exact semantic/content/Record/lineage identity rules (`A5`);
- exact temporal algebra, clock model, valid-time model, or concurrency model (`A5`);
- lifecycle state names and transitions (`A6`);
- conflict-resolution, uncertainty-combination, or belief-revision algorithms (`A7`);
- formal equivalence levels, portability thresholds, replay/reconstruction requirements, or conformance profiles (`A8`);
- module-by-module classification of P1–C5 (`A9`);
- final falsification program or unresolved architectural questions (`A10`);
- reducer-v2 referential rules, cycle semantics, or migration policy (`Issue #74 / ADR-0024`);
- license/publication terms (`Issue #18`);
- Track H historical-source admission;
- runtime implementation, new Event vocabulary, new databases, independent-language ports, LLM/vector adapters, ecosystem integration, maturity promotion, or production authorization.

## 16. Review and falsification questions

Integrated review should challenge at least:

1. Are any two A4 laws observationally indistinguishable and therefore duplicates?
2. Does any law smuggle an Event-sourcing, database, serialization, digital, or processor assumption into Canon?
3. Can a manual/procedural and a non-digital/adaptive mapping each preserve the law without pretending to use identical mechanics?
4. Does any law belong entirely to A5–A8 instead of constraining them?
5. Can a system violate the law while still appearing locally successful? If not, the law may be unfalsifiable or vacuous.
6. Does lawful forgetting conflict with history/accountability requirements, and is the boundary explicit rather than hidden?
7. Are `Knowledge`, `Memory`, `State`, or `Event` being treated as more final than A2 permits?
8. Can a profile report `UNSUPPORTED` honestly without being misclassified as `false` or non-conforming outside the named level?

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

The existing assertion map remains `45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED`. `NK-EPI` remains `0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED`. A4 documentation does not promote either.

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
