# 🧬 A5 — Identity, Time, and Change

**[English](./A5_IDENTITY_TIME_AND_CHANGE.md) · [Русский](./A5_IDENTITY_TIME_AND_CHANGE.ru.md)**

> **Deliverable:** `A5_IDENTITY_TIME_AND_CHANGE` of the [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.md) blueprint under `ADR-0025` / [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88)  
> **Depends on:** provisional A1–A4 blueprint content  
> **Evidence boundary:** architecture research and provisional semantic obligations only; no runtime, contract, evidence, assertion-map, NK-EPI, maturity, or production change  
> **Review status:** first drafted slice; pending independent review and integrated A1–A10 review

```text
model_id: nk-identity-time-change/A5-draft-1
state: DRAFTED
classification: PROVISIONAL / TECHNOLOGY-NEUTRAL / SUBSTRATE-NEUTRAL
next_content_slice: A6_KNOWLEDGE_LIFECYCLE
runtime, contracts, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
Issue #18, Issue #74 / ADR-0024, Track H operator-controlled sources: UNCHANGED
```

## 1. Purpose and authority boundary

A5 answers a meaning-level question left deliberately open by A2–A4:

> When are two representations, positions, records, occurrences, or continuations the same in a declared sense; when are they different; how are time and order named; and what does a change preserve or create?

A5 does **not** define a universal hash, UUID, row key, physical address, clock, Event envelope, reducer sequence, deletion engine, or metaphysical identity theory. It defines a provisional vocabulary and decision discipline that a later profile must preserve, translate, approximate, or explicitly declare unsupported.

The model refines A4-L11…L19 without weakening them. In particular:

```text
semantic identity ≠ storage identity
equal bytes/hash/text ≠ universal semantic identity
one timestamp ≠ all temporal meaning
write order ≠ occurrence or causal order
Revision ≠ silent overwrite
Supersession ≠ deletion or falsity
representation change ≠ represented-world change
```

## 2. Model status and qualification rule

Identity in Native Kernel is a **typed, scoped relation**, not one global identifier. A statement of sameness or difference is incomplete unless it names the identity kind, Context, temporal scope, criterion, uncertainty, and Authority where a decision is governed.

A candidate A5 rule qualifies only if it can be expressed without requiring Python, SQL, JSON, SHA-256, a wall clock, Event sourcing, a graph, an LLM, embeddings, or one processor model.

A5 therefore distinguishes semantic obligations from current reference encodings. Existing accepted contracts remain historically valid under their own versioned scope; A5 does not silently supersede an accepted ADR or rewrite evidence.

## 3. Identity kinds

A5 defines seven provisional identity kinds. They are relations/questions, not mandatory stored entities or enums.

| Kind | Question | Explicit non-equivalence |
|---|---|---|
| `REFERENT_IDENTITY` | Do two representations concern the same represented entity/process/referent in the declared Context? | same referent ≠ same State or representation |
| `SEMANTIC_CONTENT_IDENTITY` | Do two expressions carry the same declared semantic content/proposition under a stated equivalence rule? | same content ≠ same Claim, Record, Source, or occurrence |
| `CLAIM_POSITION_IDENTITY` | Is this the same source-/actor-bound assertion or epistemic position? | same text/content ≠ same act of claiming |
| `RECORD_IDENTITY` | Is this the same retained representation/record under a declared record-continuity rule? | copied bytes ≠ automatically same Record |
| `LINEAGE_CONTINUITY_IDENTITY` | Do items belong to one declared continuity/revision family while remaining distinguishable versions? | one lineage ≠ one version or one content identity |
| `OCCURRENCE_IDENTITY` | Do records/events/observations represent the same bounded occurrence or change? | one occurrence ≠ one Event record; one Event ≠ one physical occurrence |
| `SUBSTRATE_LOCAL_IDENTITY` | Is this the same row, address, file, object, physical trace, process-local object, or equivalent local carrier? | local/physical identity ≠ semantic identity |

These kinds can disagree without contradiction. Two objects may have `SAME` semantic content and `DISTINCT` Record identity. A changing person or process may preserve referent identity while State changes. A migrated representation may have different substrate-local identity while preserving a declared semantic or lineage relation.

## 4. Typed identity relation

The provisional abstract relation is:

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

A profile may represent the result differently, but must preserve or explicitly map these semantic outcomes where the distinction matters:

```text
SAME
DISTINCT
CONTINUATION_OF
VERSION_OF
ALIAS_OF
MIGRATED_FROM
UNRESOLVED
```

`SAME` means same **under the named identity relation**, never universal ontological identity. `UNRESOLVED` is required when the available criterion, Context, provenance, or capability cannot warrant a stronger answer. Ambiguous identity or collision must keep candidates distinguishable until an authorized criterion resolves or narrows the ambiguity.

## 5. Continuity, versions, aliases, and migration

Continuity is not identical to sameness. A successor can be a new version or new entity and still belong to a declared lineage.

A5 uses the following provisional distinctions:

```text
identity-preserving transformation
new version within declared lineage
new semantic entity with explicit predecessor/derivation relation
alias to an already distinguished identity
migration from one representation/profile to another
unresolved identity effect
```

Migration MUST state which identity kinds it claims to preserve, which it changes, and what information is lost or approximated. A profile MUST NOT infer semantic preservation solely from equal bytes, equal hashes, successful deserialization, matching row keys, or successful program execution.

An alias MUST NOT silently merge provenance, authority, temporal scope, or independent occurrences. Multiple aliases may identify one entity under a declared policy; two similar labels do not by themselves establish aliasing.

## 6. Temporal dimensions

A5 defines eight provisional temporal dimensions that must remain distinguishable when material:

| Dimension | Meaning |
|---|---|
| `OCCURRENCE_TIME` | when a represented occurrence/change happened or is asserted to have happened |
| `VALID_TIME` | interval/point during which a represented proposition, State, rule, relation, or position applies |
| `OBSERVATION_TIME` | when an observer/source acquired or registered an Observation/measurement |
| `ASSERTION_TIME` | when an actor/Source made or is represented as making a Claim/position |
| `RECORD_TIME` | when a representation became a retained Record in the relevant system/process |
| `DECISION_TIME` | when an Authority or procedure made a decision |
| `EFFECTIVE_TIME` | when a decision, policy, Supersession, restriction, or other governed effect begins/ends applying |
| `WRITE_COMMIT_TIME` | when a particular implementation physically/logically wrote or committed a representation |

A profile does not need eight physical timestamp fields. It needs a declared mapping that preserves the temporal distinctions required by its domain or explicitly reports loss/unsupported dimensions.

Time may be represented by instants, intervals, ranges, partial order, qualitative relations, uncertain bounds, counters, physical phases, or other substrate-specific mechanisms. A5 does not require globally synchronized clocks or UTC as a universal substrate property.

## 7. Ordering model

Time values and order relations are related but not interchangeable. A5 distinguishes at least:

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

A total order imposed for storage or deterministic execution does not become occurrence or causal order without separate warrant. In particular:

```text
A <write B
≠
A <causal B
```

Profiles may use total order locally while preserving that some represented relations are concurrent, incomparable, uncertain, or unknown.

## 8. Change classification and decision matrix

A5 classifies the semantic effect of a change independently across identity kinds. The following matrix is provisional guidance, not a universal automatic algorithm:

| Change | Default A5 interpretation |
|---|---|
| storage relocation / backend replacement | substrate-local identity changes; semantic/lineage preservation requires declared mapping |
| re-encoding / serialization change | representation changes; semantic content may be preserved under named equivalence |
| exact copy | usually a new Record/carrier; content may be same; provenance remains distinguishable |
| translation | new Record/expression; semantic-content equivalence is possible but must be declared/assessed |
| formatting or non-semantic typo correction | representation/Record version changes; content identity is domain-dependent, not assumed globally |
| semantic correction | usually a new content/position version with explicit lineage; represented occurrence need not change |
| reinterpretation | new Interpretation/position linked to the same underlying Record/Observation where applicable |
| Revision | identity effect must be classified explicitly; predecessor remains distinguishable unless authorized forgetting applies |
| Supersession | predecessor and successor remain distinct; replacement scope/effective time is explicit |
| restriction | availability/access changes; does not by itself change truth, content identity, or occurrence identity |
| logical erasure | disposition/availability change; does not imply global physical deletion or falsity |
| physical/cryptographic erasure | destroys or makes carriers inaccessible under a bounded proof scope; does not retroactively erase represented history |
| forgetting/loss | records an authorized or unavoidable reduction of availability/recoverability/continuity; does not mean the represented thing never existed |
| represented-world change | represented State may change while referent identity may or may not persist under the declared criterion |

When several identity kinds are relevant, the profile must report the vector of effects rather than collapse them into one `changed=true/false` flag.

## 9. Revision and Supersession

A semantic Revision requires, where material:

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

Revision may preserve one identity kind while creating a new version under another. Silent in-place replacement that makes the predecessor indistinguishable from never-existing history is not accountable Revision unless an explicit authorized forgetting/loss boundary applies.

Supersession means scoped replacement/preference, not deletion, falsity, universal invalidation, or physical erasure. A5 does not decide single-successor rules, cycle rules, self-supersession, or reducer referential topology; those remain outside this slice and Issue #74 / ADR-0024 remains untouched.

## 10. Restriction, erasure, and forgetting

A5 keeps these meanings separate:

```text
restriction
≠ logical erasure
≠ physical deletion
≠ cryptographic erasure
≠ semantic forgetting/loss
≠ falsity
```

Restriction changes availability/permission. Logical erasure records a semantic/disposition state in a declared profile. Physical deletion and crypto-erasure are execution/proof questions. Forgetting is a continuity/availability loss boundary and may occur on substrates with no rows or files at all.

A5 does not define the operational deletion lifecycle, key hierarchy, backup handling, provider deletion, or compliance semantics owned by Issue #16 and later lifecycle/profile work.

## 11. Relationship to existing contracts and the reference laboratory

The repository already contains accepted/versioned identity and Event contracts and a bounded clean implementation. A5 does not rewrite their history or evidence.

### Existing `nk-id/1.0`

`nk-id/1.0` uses a strict UTF-8/NFC canonical JSON subset, SHA-256 domain separation, `nkh1`/`nkc1`/`nkl1`, and an identity-bearing `asserted_at` field for the current reference contract. Those are valid versioned contract choices in their declared scope. They are **not established by A5 as the only possible physical realization of semantic identity**.

A5 therefore records a reconciliation requirement for later integrated review:

```text
A5 meaning-level identity/time model
        ↓
versioned encoding/profile mappings
        ↓
existing nk-id/1.0 as one current mapping
```

No ADR status changes here. Issue #14 remains open for semantic/profile separation, aliasing/migration, valid-time identity effects, hash agility, independent readers, and cross-encoding equivalence.

### Existing `nk-event/1.0` and P1–C5

`global_seq`, `stream_seq`, commit order, Event envelopes, reducer replay, and exact JSON/bytes remain useful reference-laboratory mechanisms. Their ordering is not universal occurrence or causal order. Issue #15 remains responsible for portable history commitment and broader Event/replay threat models.

### Existing deletion state machine

The current deletion/restriction state machine is a bounded profile realization. A5 imports only the semantic distinctions among restriction, logical erasure, physical deletion, crypto-erasure, and forgetting; it does not universalize the enum or operational workflow.

## 12. Failure and indeterminacy cases

A profile fails the A5 draft obligation for a declared mapping if it silently:

- uses a row ID, memory address, hash, byte equality, or object identity as every identity kind;
- merges two independent Claims because their text is equal;
- treats a copied Record as the same provenance-bearing occurrence without a declared rule;
- converts uncertain identity into `DISTINCT` or `SAME` for convenience;
- changes identifier/encoding during migration without preserving aliases/lineage or declaring loss;
- turns one timestamp into occurrence, Observation, assertion, Record, decision, valid, and write time simultaneously when those meanings differ;
- turns write/serialization order into causality;
- overwrites a revised position without visible lineage or authorized forgetting boundary;
- treats Supersession as falsity or physical deletion;
- treats restriction or forgetting as evidence that the represented entity never existed;
- claims exact replay or physical identity as the only valid continuity mechanism.

## 13. Contrasting substrate mappings

### Manual archival and review process

Paper records, signed provenance sheets, version labels, correction slips, effective-date registers, cross-references, and retention decisions can represent distinct Record/content/lineage identities and temporal relations without hashes, SQL, Events, or reducers.

### Adaptive analog or neuromorphic substrate

Continuity may be carried by changing physical dynamics, attractors, distributed traces, or observable transformations. Exact immutable IDs or timestamps may not exist. A companion procedure may be required to expose provenance, identity decisions, partial order, revision lineage, or accountable forgetting. A substrate that cannot expose those declared distinctions cannot claim the corresponding A5 mapping merely because it retains memory-like influence.

### Conventional digital Event-sourced laboratory

The current laboratory may realize some A5 relations through `nkh1`/`nkc1`/`nkl1`, timestamps, Event sequences, stored Claims, lineage references, reducer views, and deletion states. These are one named implementation family, not A5 itself.

## 14. Falsification criteria and open questions

A5 must be revised, split, or weakened if integrated review shows that:

- the proposed identity kinds cannot distinguish real cases without circular definitions;
- materially different substrates can preserve meaning but cannot express the required distinctions even through a functional equivalent;
- one identity kind collapses into another across all useful cases;
- the temporal model forces digital clock assumptions that are unnecessary for semantic preservation;
- the order model cannot represent legitimate concurrency/incomparability;
- migration with preserved declared meaning is incorrectly classified as identity loss solely because bytes change;
- forgetting cannot be represented without retaining content that policy requires unavailable;
- the model cannot represent uncertain/contested identity without forcing a false binary answer.

Open questions retained for later slices include domain-specific identity criteria, valid-time participation in Claim/content identity, identity of evolving Contexts/Sources/Authorities, branching lineage policy, conflict-resolution effects on identity, minimum portable history commitment, and cross-substrate equivalence thresholds.

## 15. Deferred responsibilities and completion boundary

A5 intentionally does not decide:

- **A6:** the complete knowledge lifecycle and state-transition vocabulary;
- **A7:** conflict taxonomy, resolution strategy, uncertainty algebra, or belief-revision algorithms;
- **A8:** conformance/equivalence thresholds and formal substrate-independence profile requirements;
- **A9:** final module-by-module classification of P1–C5;
- **A10:** integrated open-question and falsification registry;
- **Issue #14:** exact future encoding/hash migration contract details;
- **Issue #15:** append/idempotency/replay and portable Event/history commitment;
- **Issue #16:** physical/cryptographic deletion execution and retention mechanics;
- **Issue #74 / ADR-0024:** reducer-v2 referential/Supersession topology;
- **Issue #18:** license/publication;
- **Track H:** operator-controlled historical-source admission;
- runtime implementation, new Event vocabulary, new databases, LLM/vector adapters, maturity or production authorization.

First-draft completion test: the model can explain which identity relation is being asked, which temporal/order relation is being used, and whether a change preserves a relation, creates a version/entity, aliases/migrates, changes availability, or remains unresolved — without requiring one physical encoding.

A5 remains `DRAFTED / PROVISIONAL`. Independent review and integrated A1–A10 review remain required before Canon promotion or any reopening of runtime expansion.