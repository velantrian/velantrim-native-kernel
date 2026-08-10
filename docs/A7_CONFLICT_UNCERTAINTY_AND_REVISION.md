# ⚖️ A7 — Conflict, Uncertainty, and Revision

**[English](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) · [Русский](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md)**

> **Deliverable:** `A7_CONFLICT_UNCERTAINTY_AND_REVISION` of the [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.md) blueprint under `ADR-0025` / [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Depends on:** provisional A1–A6 blueprint content, especially A3 `DETECT_TENSION` / `REVISE_OR_SUPERSEDE`, A4-L21/L22/L24, A5 identity/time/change, and A6 `IN_TENSION` / `REVISED_OR_SUPERSEDED`  
> **Reconciles with:** accepted `NK-CFL` family in `foundational-skeleton/1.0`; proposed ADR-0003 remains `PROPOSED`, ADR-0024 remains `PROPOSED / PENDING_OPERATOR`  
> **Evidence boundary:** architecture research and provisional semantic obligations only; no runtime, contract acceptance, evidence, assertion-map, NK-EPI, maturity, or production change  
> **Review status:** first drafted slice; pending independent review and integrated A1–A10 review

```text
model_id: nk-conflict-uncertainty-revision/A7-draft-1
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
next_content_slice: A8_SUBSTRATE_INDEPENDENCE_CONTRACT
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
ADR-0003 decision status: PROPOSED / UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```

## 1. Purpose and authority boundary

A7 answers one bounded question:

> How can Native Kernel represent tension, uncertainty, competing positions, and reasoned revision without converting detection into resolution, uncertainty into falsehood, or a convenient algorithm into semantic authority?

A7 is not a universal truth engine and not a module that must always choose a winner. A valid outcome may remain unresolved indefinitely when evidence, Context, identity, interpretation, provenance, capability, or Authority is insufficient.

Required non-equivalences:

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

A7 refines the accepted `NK-CFL` semantic boundary. It does not accept proposed ADR-0003, authorize `CONFLICT_OPENED` / `CONFLICT_RESOLVED` Event verbs, implement reducer-v2, select LWW/CRDT/OCC/CAS, or require a Bayesian, Dempster–Shafer, AGM, LLM, vector, SQL, graph, or digital implementation.

## 2. Model status and qualification rule

A candidate A7 concept qualifies only if it:

1. preserves A2 distinctions among Conflict, Contradiction, Uncertainty, Evidence, Authority, Revision, and Supersession;
2. maps to A3 transition obligations without becoming a mandatory API/Event/reducer state;
3. obeys A4-L21, A4-L22, and A4-L24;
4. preserves A5 identity, temporal scope, order, and explicit revision lineage;
5. composes with A6 lifecycle positions without inventing a second lifecycle;
6. remains meaningful across manual/procedural, adaptive/non-digital, and conventional digital substrates;
7. exposes counterexamples and conditions under which the model should remain undecided;
8. does not silently settle ADR-0003, ADR-0024, Issue #18, or Track H.

The model is therefore a set of typed semantic positions and accountable decision relations, not one mandatory conflict object or numeric uncertainty calculus.

## 3. Three independent axes of tension

A7 keeps three axes independent:

```text
tension kind
    ≠
assessment status
    ≠
resolution status
```

### 3.1 Assessment status

| Status | Meaning | Explicit non-equivalence |
|---|---|---|
| `CANDIDATE` | available material suggests a possible tension, but alignment or basis is incomplete | candidate ≠ established |
| `ESTABLISHED` | the declared method/Authority has enough alignment and basis to warrant the named tension kind | established ≠ resolved |
| `NOT_A_CONFLICT` | review shows the compared positions are compatible or the apparent tension dissolves under corrected scope/identity/interpretation | not-a-conflict ≠ one side false |
| `UNRESOLVED_ASSESSMENT` | the Kernel cannot warrant candidate dismissal or establishment | unresolved assessment ≠ false |

`ESTABLISHED` is scoped to the declared method, Context, identity relation, temporal alignment, and Authority. It is not a universal metaphysical statement.

### 3.2 Resolution status

| Status | Meaning | Explicit non-equivalence |
|---|---|---|
| `UNRESOLVED` | no authorized and warranted resolution is represented | unresolved ≠ failure |
| `DEFERRED` | a declared Authority/policy intentionally postpones resolution pending a condition, review, or evidence | deferred ≠ forgotten |
| `RESOLVED_FOR_SCOPE` | an accountable decision specifies how the tension is handled for a named purpose/Context | resolved-for-scope ≠ objective truth |
| `REOPENED` | a prior scoped resolution is again under review because basis, Context, evidence, identity, policy, or Authority changed | reopened ≠ history rewrite |

A profile may encode these meanings differently, but may not collapse them into one `conflict=true/false` or `resolved=true/false` flag when the distinction matters.

## 4. Tension taxonomy

A7 refines the accepted `NK-CFL` inventory into candidate tension kinds. The inventory is provisional and may be split or merged during integrated review.

| Tension kind | Core question | Default semantic handling |
|---|---|---|
| `DUPLICATE_DELIVERY` | Is the same command/record/transition attempt being observed again? | apply idempotency/identity policy; do not create epistemic conflict by repetition |
| `WRITE_VERSION_RACE` | Are concurrent technical writes incompatible under a profile contract? | preserve technical failure/branching separately from semantic truth |
| `DIVERGENT_HISTORY` | Do lineages share a declared ancestor and then diverge? | retain branches and provenance; merge policy is explicit |
| `SEMANTIC_CONTRADICTION` | Can aligned propositions/commitments not jointly hold? | require aligned interpretation, scope, time, modality, assumptions |
| `TEMPORAL_MISMATCH` | Does apparent incompatibility arise from different temporal scopes/orders? | correct alignment before declaring contradiction |
| `SCOPE_MISMATCH` | Are positions being compared outside compatible Context/domain/jurisdiction/quantification? | preserve scopes; may dissolve false conflict |
| `PROVENANCE_CONFLICT` | Do origin/custody/transformation accounts disagree materially? | preserve alternatives and gaps; do not invent continuity |
| `MEASUREMENT_DISAGREEMENT` | Do observations/measurements differ under potentially different methods, frames, or uncertainty? | preserve method/frame and measurement uncertainty |
| `AUTHORITY_CONFLICT` | Do different scoped Authorities issue incompatible decisions or claims about authority? | expose role/scope/delegation; no credential-based universal winner |
| `POLICY_CONFLICT` | Do applicable policies prescribe incompatible handling under overlapping scope? | require policy/version/effective-scope comparison |
| `EPISTEMIC_DISAGREEMENT` | Do support, belief, hypothesis, or knowledge positions differ without strict contradiction? | retain different Evidence/warrant positions |
| `PROJECTION_DRIFT` | Does a derived view disagree with its declared authoritative inputs/reconstruction contract? | treat as derived-view integrity problem; do not rewrite history |
| `UNCLASSIFIED_TENSION` | Is material tension visible but not safely classifiable yet? | retain explicit unknown instead of forcing a class |

The taxonomy deliberately mixes technical and semantic tensions because the architecture must distinguish them before choosing a response. A technical collision must not silently become a semantic contradiction, and a semantic contradiction must not be reduced to storage ordering.

## 5. Alignment before contradiction

A `SEMANTIC_CONTRADICTION` assessment requires sufficient alignment of at least the materially relevant dimensions:

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

If alignment is missing, A7 requires `CANDIDATE` or `UNRESOLVED_ASSESSMENT`, or a more specific mismatch such as `TEMPORAL_MISMATCH` or `SCOPE_MISMATCH`.

Examples:

- “door open at 09:00” and “door closed at 10:00” are not a contradiction merely because the text differs;
- two temperature measurements can disagree because method, calibration, location, or time differs;
- two policies can conflict operationally even when neither makes a truth claim;
- two Sources can hold different epistemic positions without expressing logical negations.

A detector that drops alignment Context and then reports contradiction violates A4-L21.

## 6. Typed uncertainty positions

A7 does not define uncertainty as one scalar. It defines a provisional typed relation:

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

Candidate uncertainty kinds include:

| Kind | Meaning |
|---|---|
| `EVIDENCE_GAP` | relevant support/challenge material is missing or insufficient |
| `PROVENANCE_GAP` | origin/custody/transformation is incomplete or contested |
| `CONTEXT_GAP` | interpretation/applicability lacks material scope |
| `TEMPORAL_GAP` | valid/occurrence/observation/assertion/effective timing is insufficiently known |
| `IDENTITY_GAP` | the relevant A5 identity relation is unresolved |
| `INTERPRETATION_GAP` | more than one material interpretation remains plausible/available |
| `AUTHORITY_GAP` | no adequate or uncontested Authority exists for the attempted decision |
| `CAPABILITY_GAP` | the profile/observer cannot make the required discrimination |
| `DEPENDENCY_UNCERTAINTY` | Evidence independence/dependence is unknown or only partly known |
| `MEASUREMENT_UNCERTAINTY` | a measurement carries declared method/frame/error or range limits |
| `UNCLASSIFIED_UNCERTAINTY` | uncertainty is known to exist but not safely classifiable |

A probability, confidence score, interval, possibility set, qualitative label, physical distribution, human judgment, or another method may represent part of an uncertainty position. Such a method must declare what the value means, what dependencies it assumes, and what it cannot justify. A model confidence number is not automatically Evidence or Authority.

### 6.1 Combining uncertainty

A7 intentionally provides no universal combination algebra. Combining uncertainty requires a named method/profile and must preserve materially relevant dependence and provenance. In particular:

```text
copied Evidence ≠ independent Evidence
multiple confidence values ≠ automatically combinable probabilities
missing evidence ≠ negative evidence
```

If the method cannot justify a combined result, the correct result is an explicit unresolved or partial position.

## 7. Tension position / Conflict Set semantic pattern

A7 refines the accepted `NK-CFL` Conflict Set pattern without making it a mandatory root entity:

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

- participants remain individually identifiable under relevant A5 identity relations;
- detection basis and alignment assumptions are inspectable;
- candidate/established/not-a-conflict/unresolved assessment remain distinct;
- unresolved Evidence, provenance, Context, identity, or Authority gaps remain visible;
- resolution state does not silently erase the pre-resolution tension;
- reopening can refer to the prior resolution without rewriting it;
- a Receipt can account for detection or resolution but does not prove truth.

A future profile can realize this pattern as records, relations, a case file, dynamic state, a distributed structure, or another declared equivalent.

## 8. Authority boundaries for detection and resolution

A7 distinguishes at least these authority roles where material:

```text
detection Authority / method
≠ resolution Authority
≠ epistemic-assessment Authority
≠ operational-disposition Authority
≠ architecture/governance Authority
```

A method may deterministically detect a profile-level invariant violation without having semantic resolution authority. A human reviewer may have authority to decide a legal or operational policy for a specific jurisdiction without thereby making a disputed scientific proposition objectively true. An operator may approve an architecture decision without creating empirical Evidence.

An accountable `RESOLVED_FOR_SCOPE` decision must identify, where material:

- tension being addressed;
- Authority role, actor/method, delegation, and policy/version;
- purpose and Context;
- basis and Evidence considered;
- material exclusions/counterevidence;
- effective temporal scope;
- uncertainty remaining after the decision;
- resulting positions or handling;
- reversibility/review/reopening conditions;
- Receipt/accountability boundary.

If no adequate Authority exists, `UNRESOLVED` or `DEFERRED` is valid and preferred to invented authority.

## 9. Resolution modes without a universal winner algorithm

A7 permits several semantic resolution modes without requiring any one algorithm:

| Mode | Meaning | Boundary |
|---|---|---|
| `DISSOLVE_BY_ALIGNMENT` | corrected identity/time/scope/interpretation shows the apparent conflict does not apply | does not declare either participant false |
| `RETAIN_PLURALITY` | multiple positions remain simultaneously represented because no stronger warrant exists or plurality is legitimate | plurality ≠ merge |
| `PREFER_FOR_SCOPE` | an Authority selects one position for a named purpose while alternatives remain historically/semantically visible | preference ≠ universal truth |
| `REVISE_POSITION` | a prior semantic/epistemic position is explicitly changed with A5 lineage | revision ≠ overwrite |
| `SUPERSEDE_FOR_SCOPE` | a successor replaces a predecessor for declared scope/effective time | supersession ≠ deletion/falsity; topology remains ADR-0024 |
| `DEFER_DECISION` | resolution is intentionally postponed with a reason/review condition | deferral ≠ failure |
| `NO_AUTHORIZED_RESOLUTION` | the system explicitly records that no actor/method has sufficient Authority | no authority ≠ false |

These are meaning-level categories, not Event verbs or required enums. A profile can use a mathematical merge, CRDT-like mechanism, voting, rules, proof, statistical inference, human review, or another technique only if the resulting semantics and loss are declared. The technique itself does not acquire truth authority by implementation.

## 10. Revision and belief/epistemic change

A7 refines A5 revision discipline for tensions and uncertainty. A reasoned epistemic revision can be expressed provisionally as:

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

A7 does not require a scalar belief strength or a universal belief-revision calculus. The resulting position may strengthen, weaken, suspend, retain, retract, replace-for-scope, or remain unresolved according to a declared domain policy; those effects are descriptions, not a mandatory stored enum.

Required disciplines:

- new Evidence can change an epistemic position without changing the underlying Observation/Record;
- a changed Interpretation can revise a Claim/Belief while preserving the original material;
- retraction does not delete prior history;
- a resolution decision can be operationally binding yet epistemically uncertain;
- authority can authorize a revision under policy without proving the revised proposition true;
- copied/repeated Claims do not gain warrant by count alone;
- a revision must preserve relevant predecessor/successor lineage or explicitly invoke an authorized forgetting boundary.

No A7 rule changes the existing `nk-p1-reducer/1` semantics or decides reducer-v2 successor/cycle rules.

## 11. Reversibility, reopening, and remaining undecided

A7 requires the ability to remain undecided and, where material, to reopen a prior decision.

A resolution should declare whether it is:

- reviewable/reversible under new Evidence or Context;
- final only for a named operational/legal/policy scope;
- irreversible under a specific governing rule, with that irreversibility itself scoped and accountable.

A `REOPENED` tension preserves the prior `RESOLVED_FOR_SCOPE` record and explains why the prior resolution is no longer sufficient. Reopening may be triggered by new Evidence, corrected provenance, changed identity alignment, changed policy, expired Authority, newly available capability, or discovered omission.

The architecture must permit:

```text
“We do not currently know.”
“We cannot currently discriminate.”
“Both positions remain live for different scopes.”
“No authorized resolution exists.”
“The previous scoped resolution is under review.”
```

None of these states is a failure of the Kernel merely because a single winner is absent.

## 12. Relationship to A6 lifecycle

A7 does not change A6's nine phases. It refines transitions around `IN_TENSION`, `EPISTEMICALLY_WEIGHED`, and `REVISED_OR_SUPERSEDED`:

```text
DETECT_TENSION
    ↓
IN_TENSION
    ├─ insufficient basis/authority ──→ remain IN_TENSION / UNRESOLVED
    ├─ scope/time alignment dissolves tension ──→ RELATIONALLY_INTEGRATED or EPISTEMICALLY_WEIGHED
    ├─ scoped preference without semantic revision ──→ RELATIONALLY_INTEGRATED + resolution record
    └─ actual revision/supersession ──→ REVISED_OR_SUPERSEDED
```

Important boundaries:

- a `RESOLVED_FOR_SCOPE` decision does not automatically imply `REVISED_OR_SUPERSEDED`;
- entering `REVISED_OR_SUPERSEDED` requires the A5 predecessor/successor or revised-position lineage;
- `ACCOUNT` may record a Receipt for detection/resolution/reopening, but `ACCOUNTED ≠ true/correct`;
- a tension can remain open indefinitely;
- reopening does not erase the earlier lifecycle history.

## 13. Relationship to existing contracts, ADRs, and reference laboratory

### 13.1 Accepted `NK-CFL`

A7 is a refinement of the already accepted `NK-CFL` family (`foundational-skeleton/1.0`). It preserves `NK-CFL-001`…`NK-CFL-008` and makes the candidate/established distinction, uncertainty gaps, resolution Authority, and reopening/revision model more explicit. It does not create new executable support claims for those assertions.

### 13.2 Proposed ADR-0003

ADR-0003 remains `PROPOSED / NOT_STARTED`. A7 reuses compatible research concepts such as explicit conflict visibility and separation of detection from resolution, but this document does **not** change ADR-0003 decision status or accept its proposed Conflict Set/Event lifecycle vocabulary.

### 13.3 Issue #74 / ADR-0024

A7 does not decide:

- one-successor versus multi-successor Supersession topology;
- self-supersession;
- successor cycles;
- reducer-v2 version dispatch or migration.

Those remain Issue #74 / ADR-0024 `PROPOSED / PENDING_OPERATOR`. A7 only requires any future topology/resolution mechanism to preserve declared conflict/revision semantics and history.

### 13.4 P1–C5 bounded reference laboratory

The current P1–C5 laboratory has no accepted A7 conflict lifecycle runtime. Current Event vocabulary remains:

```text
ADMIT · LINK · UTILIZED · SUPERSEDED · ERASED
```

`CONFLICT_OPENED`, `CONFLICT_REVIEWED`, `CONFLICT_RESOLVED`, and `CONFLICT_REOPENED` are not authorized Event verbs. Current `SUPERSEDED` remains a laboratory mechanism under reducer-v1 evidence and Issue #74 boundaries. Projection drift remains a derived-view integrity concept; A7 does not modify projection runtime.

Therefore A7 is documentation/blueprint evidence only, not runtime conformance evidence.

## 14. Failure and indeterminacy cases

A profile or later contract violates A7's provisional intent if it silently:

- classifies a candidate tension as established without alignment/basis;
- converts `UNRESOLVED_ASSESSMENT` or `UNRESOLVED` to false;
- uses newest write, highest rank, majority count, model confidence, storage order, or retrieval relevance as semantic winner by itself;
- labels temporal/scope mismatch as contradiction after dropping Context;
- averages incompatible positions and discards participants/provenance;
- invents provenance or Authority to close a required field;
- treats copied Evidence as independent Evidence without a dependence rule;
- uses one uncertainty scalar without declaring its meaning/dependencies;
- resolves a conflict without naming scope, basis, Authority, and remaining uncertainty;
- rewrites prior positions or a prior resolution instead of preserving revision/reopening lineage;
- treats `RESOLVED_FOR_SCOPE` as universal truth;
- treats `SUPERSEDE_FOR_SCOPE` as deletion or falsity;
- imports ADR-0024 topology or proposed ADR-0003 Event names as accepted runtime;
- claims that a successful deterministic resolver proves semantic correctness.

`UNKNOWN`, `PARTIAL`, `UNSUPPORTED`, `NO_AUTHORIZED_RESOLUTION`, or long-lived unresolved plurality are legitimate outcomes when honestly warranted.

## 15. Contrasting substrate mappings

### Manual archival and review process

A review board keeps separate testimony and evidence packets, opens a conflict sheet when positions appear incompatible, marks the sheet `CANDIDATE` until time/scope/identity are aligned, records provenance gaps, and may leave the case `UNRESOLVED`. A scoped Authority can later issue a decision for a defined purpose while retaining the losing and unresolved material. A new document can reopen the case. Paper folders, signatures, correction slips, and a decision ledger can preserve the A7 obligations without SQL, Events, embeddings, or numeric confidence.

### Adaptive analog or neuromorphic substrate

Competing attractors, distributed traces, or dynamically stable alternatives may encode unresolved plurality without discrete conflict rows. Uncertainty may appear as ranges, competing dynamics, or inability to stabilize a discrimination rather than one probability. To claim an A7 mapping, the substrate or companion accountability procedure must still expose the materially required participants, scope, uncertainty/basis, authority boundary, and revision/reopening effects. Physical competition between states does not by itself constitute semantic resolution.

### Conventional digital Event-sourced laboratory

The existing P1–C5 implementation can be used later as a falsification instrument, but today it does not implement an accepted A7 conflict lifecycle. It can preserve Claims, provenance-bearing records, relations, Supersession history, reducer views, and Receipts; those mechanisms may support future experiments. A7 does not add conflict Event verbs, change reducer semantics, or promote PostgreSQL/SQLite ordering into resolution authority.

These mappings demonstrate conceptual portability only. They are not cross-substrate conformance evidence; A8 owns that question.

## 16. Falsification criteria and open questions

A7 should be revised, split, or weakened if integrated review shows that:

- candidate and established tensions cannot be distinguished through observable obligations across materially different substrates;
- the taxonomy produces categories that cannot be distinguished in practice or omits a recurrent irreducible tension type;
- `NOT_A_CONFLICT`, `UNRESOLVED_ASSESSMENT`, `UNRESOLVED`, and `RESOLVED_FOR_SCOPE` cannot be kept semantically distinct;
- the model secretly requires a single global confidence scale, probability calculus, graph, Event log, or centralized reviewer;
- preserving unresolved plurality requires copying implementation structure rather than meaning-level obligations;
- resolution Authority cannot be distinguished from truth/evidence Authority without circular rules;
- reopening cannot preserve prior resolution history without violating lawful forgetting boundaries;
- the model cannot represent legitimate paraconsistent, probabilistic, vague, multi-context, or non-propositional tensions without forcing false contradiction;
- a manual/procedural or adaptive/non-digital mapping can preserve all required meaning but is rejected only because it lacks current digital mechanics.

Open questions retained for A8–A10 and focused future work include:

- whether a minimal portable tension taxonomy should be smaller than §4;
- formal logic families and paraconsistent handling;
- domain-specific quantitative uncertainty combination and independence models;
- authority-conflict escalation and delegation semantics;
- exact reopening/finality policy across legal, operational, scientific, and personal contexts;
- executable `NK-CFL` fixture design and whether it belongs under Issue #17 after blueprint review;
- how lawful forgetting interacts with preserved conflict and resolution history;
- how A8 should compare semantic equivalence when substrates expose uncertainty through materially different observables.

## 17. Deferred responsibilities and completion boundary

A7 intentionally does not decide:

- **A8 — Substrate-independence Contract:** equivalence/conformance obligations and thresholds for preserving A1–A7 semantics across substrates;
- **A9 — Reference Laboratory Boundary:** final module-by-module classification of P1–C5 against the blueprint;
- **A10 — Open Questions and Falsification:** integrated research-question/falsification registry;
- **ADR-0003:** acceptance/rejection/revision of the older proposed semantic-conflict ADR;
- **Issue #14:** future canonical identity/alias/migration contract details;
- **Issue #15:** portable history commitment and append/replay semantics;
- **Issue #16:** physical/cryptographic deletion and retention execution;
- **Issue #17:** executable conformance/fixture expansion;
- **Issue #74 / ADR-0024:** reducer-v2 referential/Supersession topology and migration;
- **Issue #18:** license/publication terms;
- **Track H:** operator-controlled historical-source admission;
- new Event vocabulary, OCC/CAS/CRDT/LWW selection, multi-writer protocol, new database/language/profile, LLM/vector adapters, runtime implementation, maturity promotion, or production authorization.

First-draft completion test:

> Given a disputed or uncertain position, a reviewer can identify the participants, tension kind, assessment status, alignment basis, uncertainty/provenance gaps, resolution status, Authority/policy/basis, resulting revision or non-revision effect, and reopening conditions — while the model remains meaningful without requiring one winner algorithm, one confidence scalar, one Event vocabulary, or one physical substrate.

A7 remains `DRAFTED / PROVISIONAL` until independent review, integrated A1–A10 review, and the later operator review required by ADR-0025.