# 🧬 A8 — Substrate-Independence Contract

**[English](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) · [Русский](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md)**

> **Deliverable:** `A8_SUBSTRATE_INDEPENDENCE_CONTRACT` of the [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.md) blueprint under `ADR-0025` / [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Depends on:** provisional A1–A7 blueprint content, especially A4 substrate/conformance laws, A5 identity/time/change, A6 lifecycle, and A7 conflict/uncertainty/revision  
> **Evidence boundary:** architecture research and provisional conformance obligations only; no runtime, accepted-contract, evidence, assertion-map, NK-EPI, maturity, or production change  
> **Review status:** first drafted slice; pending independent review and integrated A1–A10 review

```text
model_id: nk-substrate-independence/A8-draft-1
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
next_content_slice: A9_REFERENCE_LABORATORY_BOUNDARY
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```

## 1. Purpose and authority boundary

A8 answers one bounded question:

> What must remain semantically true of an implementation when its physical carrier, representation, execution model, storage model, or computational substrate differs radically from another implementation?

A8 turns the meaning-level obligations drafted in A1–A7 into a **mapping and conformance contract**. It does not require identical machinery. It requires a profile to show which architecture distinctions it preserves, how it exposes them, where it loses them, and what conformance claim is therefore warranted.

The central boundary is:

```text
substrate-independent specification
≠
universal portability proof
```

A8 does not claim that every present or future substrate can implement Native Kernel. A substrate that cannot preserve a required distinction may still be useful, but it must disclose that limitation and must not claim full semantic equivalence.

## 2. Definition of substrate independence

For A8, **substrate independence** means:

> the Native Kernel architecture is stated in terms of meaning-level distinctions, relations, transitions, preservation obligations, explicit losses, and observable conformance criteria whose satisfaction does not depend on one mandatory physical representation or execution mechanism.

It does **not** mean that implementation constraints disappear. Every implementation has a substrate. A substrate may make some obligations easy, costly, approximate, externally mediated, or impossible.

A conforming mapping therefore separates:

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

A named functional equivalent is acceptable only when it preserves the required semantic effect. Renaming a lost distinction is not equivalence.

## 3. Architecture-preserving mapping

A8 uses the provisional specification relation:

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

This is specification notation, not a required object, schema, API, row, Event, graph node, register, or wire format.

The mapping has five preservation states:

| State | Meaning | Conformance effect |
|---|---|---|
| `PRESERVED` | the required distinction/effect is represented without known material semantic loss in the declared scope | may support full conformance for that obligation |
| `PARTIAL` | a bounded subset is faithful while a material remainder is explicit | cannot be represented as full preservation |
| `UNSUPPORTED` | the profile cannot realize the obligation in the declared scope | full conformance for that scope is unavailable |
| `INDETERMINATE` | available evidence cannot establish preservation or loss strongly enough | conformance claim must remain unresolved |
| `LOSSY` | a known approximation or collapse changes or removes material semantic information | loss must be explicit; full semantic equivalence is forbidden |

These states are **not** the repository assertion-map arithmetic and do not promote any existing assertion. They classify one A8 mapping claim.

```text
cannot preserve a required distinction
→ declare PARTIAL / UNSUPPORTED / INDETERMINATE / LOSSY
→ do not claim full equivalence
```

## 4. Mandatory preserved semantic obligations

A profile claiming full A8 conformance for a declared scope must preserve, directly or by declared functional equivalent, all materially applicable obligations below.

| ID | Obligation | Minimum preservation requirement |
|---|---|---|
| `A8-P01` | ontology distinctions | material A2 distinctions such as Observation/Claim, Evidence/Source, Knowledge/Belief, Record/represented reality, Conflict/Contradiction remain distinguishable where applicable |
| `A8-P02` | abstract transition semantics | A3 transition intent, preconditions/postconditions, non-change, failure, unknown, partial and unsupported outcomes remain expressible without silently converting them into success/false |
| `A8-P03` | semantic laws | applicable A4 laws remain true of the mapping; the profile does not obtain exemptions merely because its mechanism differs |
| `A8-P04` | typed/scoped identity | A5 identity kinds and uncertainty about identity are preserved or explicitly translated; substrate-local identity does not become semantic identity |
| `A8-P05` | temporal and ordering meaning | materially relevant A5 temporal dimensions/orders remain distinguishable; implementation order is not promoted to world/causal order |
| `A8-P06` | lifecycle and history meaning | A6 phases/transition meanings, lineage, disposition and closure distinctions remain observable without requiring one storage state machine |
| `A8-P07` | conflict/uncertainty/revision meaning | A7 assessment/resolution distinctions, typed uncertainty, plurality, scoped resolution, revision lineage and reopening remain preservable |
| `A8-P08` | Context, Provenance, Source and Authority | material scope, origin/transformation/gaps and role-bounded Authority survive mapping or loss is explicit |
| `A8-P09` | bounded accountability | accountable decisions, transformations, omissions, failures and losses can be explained to the declared boundary without implying truth/completeness |
| `A8-P10` | capability and loss declaration | unsupported, partial, indeterminate or lossy obligations remain first-class limitations rather than hidden approximations |

An obligation can be inapplicable only under an explicit domain/scope argument. “Our substrate has no field for it” is not an applicability argument.

## 5. Allowed implementation variation

A profile may freely differ in, among other things:

- physical memory or carrier;
- layout and topology;
- serialization or absence of serialization;
- identifier encoding;
- programming language;
- instruction sequence;
- data structure;
- storage engine or absence of a database;
- indexing and retrieval mechanism;
- persistence mechanism;
- synchronization strategy;
- parallelism/concurrency model;
- distribution/centralization;
- representation of time;
- representation of uncertainty;
- representation of state/history;
- hardware and processor model.

Variation is allowed **because it is subordinate to preservation**, not because implementation details are irrelevant.

## 6. Representation is not semantic equivalence

A8 distinguishes at least five questions that must not be collapsed into one equality predicate:

| Relation | Question |
|---|---|
| `PHYSICAL_IDENTITY` | Is the physical carrier/state the same? |
| `REPRESENTATION_EQUIVALENCE` | Are encodings/structures equivalent under a declared representation rule? |
| `SEMANTIC_OBLIGATION_EQUIVALENCE` | Are the required meaning-level distinctions and effects preserved? |
| `BEHAVIORAL_CONFORMANCE_FOR_SCOPE` | Do observable operations satisfy the same declared architecture obligations for the tested scope? |
| `LINEAGE_CONTINUITY_EQUIVALENCE` | Is required predecessor/derivation/migration continuity preserved? |

These relations may disagree.

```text
physical identity
is neither necessary nor sufficient
for semantic equivalence
```

Equal bytes, hashes, text, rows, graph topology, memory addresses, or output strings do not by themselves prove semantic equivalence. Different bytes, IDs, storage layouts, timings, or physical states do not by themselves prove semantic non-equivalence.

## 7. Identity portability

A8 inherits A5's typed/scoped identity model. A migration or cross-substrate comparison must name the identity relation being preserved.

A profile must not infer:

```text
same storage key → same referent
same hash → same Claim position
same bytes → same Record occurrence
new address → new semantic entity
```

A cross-substrate mapping may preserve `SEMANTIC_CONTENT_IDENTITY` while changing `RECORD_IDENTITY` and `SUBSTRATE_LOCAL_IDENTITY`. It may preserve `LINEAGE_CONTINUITY_IDENTITY` without claiming exact content identity. Unresolved identity remains an allowed outcome.

If a substrate cannot expose the distinction between semantic and substrate-local identity, the mapping is at least `LOSSY` for A8-P04.

## 8. Time and ordering portability

A8 does not require:

- a universal global clock;
- synchronized wall-clock timestamps;
- one total write order;
- infinite temporal precision;
- instantaneous synchronization;
- one global sequence number.

A profile may use instants, intervals, uncertain bounds, counters, causal relations, partial orders, phases, local clocks, qualitative before/after, or another mapping.

What it must preserve is the **meaning of materially required relations** from A5:

```text
write/commit order
≠ occurrence order
≠ observation order
≠ causal/dependency order
≠ semantic precedence
```

If the substrate can represent only a partial order, that is not a defect by itself. If it forces incomparable events into a total order for execution, the imposed order must not silently become causal/world order.

## 9. Memory and lifecycle portability

Memory is not required to be a file, row, byte sequence, Event log, snapshot, or replayable reducer state.

A substrate may preserve memory through:

- durable symbolic records;
- distributed relations;
- adaptive physical traces;
- stable/recurring dynamics;
- externalized procedures;
- reconstructible transformations;
- hybrid mechanisms.

A profile claiming A8-P06 must still preserve materially required continuity, lifecycle position/effect, provenance, lineage, revision/disposition meaning and declared forgetting/loss boundaries.

`history visibility` does not imply mandatory Event sourcing. A non-Event-sourced profile can conform if it preserves the required historical distinctions and accountability. Conversely, an append-only Event log that loses Context or lineage can be non-conformant despite perfect replay.

## 10. Conflict, uncertainty, and revision portability

A8 preserves A7 architecture states by meaning, not literal encoding.

A profile need not store exact strings such as:

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

It must be able to represent the **distinctions those states express** when materially applicable.

Required boundaries remain:

```text
Conflict ≠ necessarily Contradiction
Detection ≠ Resolution
Resolution-for-scope ≠ Objective Truth
Uncertainty ≠ one universal confidence scalar
Revision ≠ overwrite
```

A substrate that can represent only `true/false` and therefore converts `UNRESOLVED` or `UNRESOLVED_ASSESSMENT` into one side is `LOSSY` and cannot claim full A8-P07 preservation.

## 11. Context, Provenance, Authority, and lineage preservation

Migration or translation must preserve materially relevant:

- Context/scope and known widening/narrowing;
- Source attribution and uncertainty;
- Provenance origin, custody/transformation/derivation, contested alternatives and gaps;
- Authority role, scope, delegation/policy and temporal applicability;
- predecessor/successor/derivation/migration lineage.

A profile may redact details under a governed policy, but `redacted/withheld` must remain distinguishable from `known complete`, `unknown`, and `nonexistent` when that distinction matters.

A successful transfer that strips provenance is not full semantic preservation merely because content survives.

## 12. Accountability and explainability obligation

A8 does not require one universal Receipt format, durable log, explainability algorithm, or human-readable trace for every internal microstep.

It requires that a profile can produce a bounded account, directly or through an admissible companion mechanism, for materially accountable operations such as:

- semantic transformation;
- identity/equivalence decision;
- scoped resolution;
- Revision/Supersession;
- restriction/disposition/forgetting declaration;
- migration;
- capability failure or declared loss.

The account must identify enough Context, method/Authority, basis, effect, limitations and uncertainty to test the conformance claim.

```text
accountability ≠ correctness
explanation ≠ truth proof
```

## 13. Capability declarations and explicit degradation

Every A8 profile should publish a capability declaration for the scope it claims. The declaration may be a document, manifest, procedural certificate, formal proof, test report, or another inspectable equivalent.

For each required obligation it must state:

```text
obligation
scope
realization/equivalent
preservation state
observable check/evidence
known loss
uncertainty
```

A limitation is not itself an architecture failure when honestly scoped. The failure is to hide a material limitation while claiming stronger equivalence.

Examples:

- a substrate may be `PRESERVED` for typed identity but `PARTIAL` for provenance custody;
- it may be `UNSUPPORTED` for physical-erasure verification while preserving logical disposition;
- a cross-language translator may be `INDETERMINATE` for one semantic-content equivalence class pending review;
- a boolean-only device may be `LOSSY` for unresolved epistemic states.

## 14. Conformance outcomes

A8 uses four provisional outcome classes for a **named scope**:

| Outcome | Meaning |
|---|---|
| `FULL_CONFORMANCE_FOR_SCOPE` | all materially applicable A8-P01…P10 obligations are `PRESERVED` with sufficient observable basis |
| `BOUNDED_CONFORMANCE` | a narrower explicitly named subset/scope is preserved, while excluded/limited obligations are declared and no broader claim is made |
| `NON_CONFORMANT_FOR_SCOPE` | one or more materially required obligations are known `LOSSY`/`UNSUPPORTED` for the claimed scope or a required distinction is silently collapsed |
| `INDETERMINATE_CONFORMANCE` | evidence is insufficient to establish either preservation or non-conformance |

`BOUNDED_CONFORMANCE` is not a loophole for calling a partial implementation “fully Native Kernel”. Its scope must be explicit enough that a reviewer can see which obligations are outside the claim.

Profile conformance remains distinct from production authorization, safety, security, performance, legal compliance, or operational equivalence.

## 15. Cross-substrate equivalence criteria

Two profiles `A` and `B` may be considered semantically equivalent **for a named scope and observation boundary** only if:

1. the same materially applicable A8-P01…P10 obligations are preserved;
2. their declared identity mappings agree where the scope requires agreement, or differences are explicitly classified;
3. temporal/order relations required by the scope are preserved without manufactured causality;
4. lifecycle, conflict, uncertainty, revision and disposition distinctions produce compatible meaning-level effects;
5. Context, Provenance, Authority and lineage loss does not differ materially without disclosure;
6. observable outcomes distinguish unknown/partial/unsupported/failure from false/success in compatible ways;
7. any lossy approximation is outside the equivalence claim or causes the claim to be weakened;
8. the evidence/checking procedure is itself declared.

Same final output alone is insufficient. Different internal dynamics alone do not defeat equivalence.

A8 deliberately does not require a single universal equivalence algorithm. Domain-specific equivalence predicates may exist under this contract.

## 16. Lossy mappings and migration discipline

A migration is not successful merely because data arrived or a program ran.

A migration must identify:

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

Material untranslatable distinctions must remain explicit. A target may retain an opaque source artifact or external companion record to avoid semantic loss, but reliance on that companion becomes part of the declared profile boundary.

## 17. Failure modes and counterexamples

### Counterexample A — content preserved, Provenance deleted

A system migrates every Claim text correctly but drops Source and Provenance.

**Result:** not full-conformant for a scope requiring A8-P08. Content preservation does not compensate for provenance loss.

### Counterexample B — different bytes and IDs, preserved meaning

Two substrates use different encodings and local identifiers but preserve referent/semantic identity relations, Context, Provenance, lineage, temporal meaning, uncertainty and observable transition obligations.

**Result:** encoding difference alone does not establish non-equivalence.

### Counterexample C — newest record becomes truth

A profile resolves every conflict by choosing the latest local write and represents it as the true world state.

**Result:** non-conformant. Local write order has been promoted into semantic precedence and A7 resolution into truth.

### Counterexample D — `UNRESOLVED` cannot be represented

A device permits only binary true/false and maps all unresolved positions to `false`.

**Result:** `LOSSY` A8-P02/A8-P07 mapping; full conformance is forbidden unless the declared scope genuinely excludes that distinction.

### Counterexample E — non-Event-sourced history

A profile uses versioned procedural records and lineage relations rather than Event sourcing, while preserving required predecessor history, Context, Authority, uncertainty, revisions and accountable outcomes.

**Result:** absence of Event sourcing is not non-conformance.

### Counterexample F — exact replay but lost Context

A system can replay byte-identical state but strips the scope under which Claims were valid.

**Result:** reproducibility of representation does not establish semantic equivalence; A8-P01/P03/P08 are violated.

### Counterexample G — deterministic agreement by silent collapse

Two implementations always produce the same boolean answer because both convert `UNKNOWN` to `false`.

**Result:** behavioral equality of a defective projection does not establish Native Kernel conformance.

## 18. Contrasting illustrative mappings

These examples test the contract. They are not claims of implemented support.

### Manual archival and review process

Paper records, cross-references, provenance sheets, correction/supersession annotations, scoped decisions and review ledgers can preserve many obligations without software, SQL, digital hashes, or Event sourcing. Conformance depends on the semantics and controls actually preserved, not the medium.

### Adaptive analog or neuromorphic substrate

A future adaptive physical system might encode continuity in changing dynamics rather than discrete records. It could qualify only if required identity, provenance, temporal/order, uncertainty, revision and accountability distinctions are observable directly or through a declared companion procedure. “It remembers” is not enough to establish A8 conformance.

### Conventional digital Event-sourced laboratory

The current Python/PostgreSQL/SQLite laboratory can be mapped against A8 through its existing versioned contracts, Events, reducers, receipts and tests. Those mechanisms are illustrative profile choices. A9 owns the detailed classification of which P1–C5 mechanisms actually satisfy, partially satisfy, or fail the A1–A8 blueprint.

## 19. Explicit non-claims and non-requirements

A8 does **not** require as universal Canon:

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

A8 also does not claim:

```text
substrate independence ≠ proof that every substrate can conform
future-facing architecture ≠ implemented neuromorphic/analog/quantum profile
semantic equivalence ≠ physical identity
same output ≠ full semantic equivalence
full conformance ≠ production authorization
public repository ≠ open-source license
A8 draft ≠ independent approval ≠ integrated Canon
```

No quantum, neuromorphic, analog, or other future implementation is claimed to exist by this document.

## 20. Existing contracts, operator boundaries, and A9 boundary

Existing accepted/versioned contracts remain valid within their historical scope. A8 does not rewrite them merely because they use current digital mechanisms.

- `nk-id/1.0`, `nk-event/1.0`, reducers, hash chains, SQL profiles and evidence remain current reference-laboratory mechanisms pending A9 mapping;
- Issue #14/#15/#16/#17 retain their existing scopes;
- Issue #18 remains operator-controlled; no license is selected and public visibility is not called open-source permission;
- Issue #74 / ADR-0024 remains `PROPOSED / PENDING_OPERATOR`; reducer v1 remains immutable and reducer-v2 is unauthorized;
- ADR-0003 remains proposed and A8 creates no conflict Event vocabulary;
- Track H source admission remains operator-controlled;
- runtime expansion remains `FROZEN`.

A8 asks **what a conforming implementation must preserve**. A9 separately asks **how the existing P1–C5 laboratory maps to that blueprint**. A8 therefore uses the laboratory only illustratively and does not grade its modules here.

## 21. Open questions and falsification boundary

A8 must be revised, weakened, split, or rejected if later evidence shows, for example, that:

- A8-P01…P10 cannot be observed or tested without importing one current implementation mechanism;
- semantic preservation cannot be distinguished from representation equality in a useful, non-circular way;
- the same required meaning can be faithfully realized on a substrate that cannot satisfy an A8 requirement even through a declared functional equivalent;
- bounded accountability necessarily requires a stronger universal history commitment than A8 currently states;
- probabilistic/analog continuity makes the proposed equivalence boundary incoherent rather than merely different in representation;
- legitimate forgetting cannot coexist with the lineage/accountability obligations as stated;
- the conformance outcome classes permit misleading claims that cannot be falsified.

These and other unresolved questions move forward to A10 rather than being hidden as solved facts.

## 22. Completion boundary

First-draft completion test:

> Given two radically different implementations, a reviewer can name which Native Kernel obligations must be preserved, distinguish physical/representation equality from semantic and behavioral equivalence, identify declared loss or unsupported capability, and determine whether a scoped conformance claim is warranted without referring to PostgreSQL schemas, Python classes, JSON bytes, Event sourcing, or one processor model.

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
