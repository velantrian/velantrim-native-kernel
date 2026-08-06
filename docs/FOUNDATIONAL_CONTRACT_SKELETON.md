# 🧬 Foundational Contract Skeleton

**[English](./FOUNDATIONAL_CONTRACT_SKELETON.md) · [Русский](./FOUNDATIONAL_CONTRACT_SKELETON.ru.md)**

- **Decision status:** `ACCEPTED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Operator approval:** `APPROVED`
- **Contract version:** `foundational-skeleton/1.0`
- **Track:** `Foundational Architecture / Abstract Contracts`
- **Scope:** technology-, storage-, model-, runtime-, hardware-, and worldview-neutral
- **Issue #1 impact:** `NONE`

> [!IMPORTANT]
> This document defines an accepted architectural skeleton, not a runnable machine. Acceptance establishes the contract boundary and stable assertion namespaces. It does not establish runtime behaviour, executable conformance, technology portability, or production evidence.

## 1. Purpose

Native Kernel needs a precise skeleton before it needs a complete runtime.

The skeleton must preserve meaning when implementations change and must prevent one overloaded object, database schema, model, event bus, or processor from silently becoming the architecture.

The accepted skeleton organizes the foundation into six contract families:

```text
🧩 Semantic roles
        ↓
🧬 Identity and canonical encoding
        ↓
📜 Event / observation / recorded change
        ↓
🛡️ Authority and admission
        ↓
⚔️ Conflict and explicit unknowns
        ↓
🔄 Conformance and semantic equivalence
```

The families are related but not interchangeable:

```text
semantic content
≠ source assertion
≠ observation
≠ evidence
≠ admission decision
≠ derived epistemic state
≠ implementation-specific row or object
```

## 2. Placement in Native Kernel architecture

```text
Architecture Canon
        ↓
Foundational Contract Skeleton
        ↓
Versioned normative contracts and fixtures
        ↓
Replaceable implementation profiles
        ↓
Reproducible evidence
```

This document does not replace [`ARCHITECTURE.md`](../ARCHITECTURE.md), [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md), or the world/epistemic boundary proposal. It supplies a stable map that those documents, future schemas, fixtures, and profiles can reference.

## 3. Shared contract envelope

Every foundational contract family SHOULD be able to declare or translate the following meaning where applicable:

| Field of meaning | Required question |
|---|---|
| **Contract identity** | Which contract family, assertion, and version apply? |
| **Semantic scope** | Which domain, subject, jurisdiction, tenant, project, or worldview frame is being described? |
| **Actor / source** | Who or what produced, observed, asserted, transformed, admitted, or resolved it? |
| **Provenance** | Which sources, methods, transformations, and gaps are known? |
| **Temporal meaning** | When was it valid, observed, recorded, admitted, revised, or restricted? |
| **Authority** | Which authority was exercised, over what scope, under which policy? |
| **Lineage** | Which prior or related records does this continue, revise, qualify, or supersede? |
| **Evidence / basis** | Which evidence candidates or decision bases were considered? |
| **Receipt boundary** | What can the resulting Receipt prove, and what remains unproven? |
| **Profile/version** | Which implementation and contract versions produced the representation? |

This is a semantic envelope, not a frozen JSON schema. A profile may represent the fields differently only if it preserves the declared meaning and conformance mapping.

---

# 4. Contract family I — Semantic Object Model 🧩

**Family ID:** `NK-SEM`

## 4.1 Problem

The current architecture uses `Claim` as the durable semantic record. Without sharper role distinctions, one object can be mistaken simultaneously for content, an assertion, an observation, evidence, a hypothesis, and admitted knowledge.

## 4.2 Contract rule

`Claim` remains the durable root record unless a later ADR proves that a new root primitive is necessary. A Claim MUST preserve or translate the semantic role of the represented content.

Conceptual roles include:

| Role | Meaning | Must not silently become |
|---|---|---|
| **Proposition** | semantic content within declared scope | a source-bound assertion or truth |
| **Assertion** | an actor/source presents a proposition | verified observation or admitted knowledge |
| **Observation** | a signal, testimony, trace, or result was received | complete explanation |
| **Measurement** | a value produced by a declared method, frame, scale, and uncertainty model | context-free fact |
| **Interpretation** | meaning assigned under assumptions | observation itself |
| **Hypothesis** | testable or inspectable explanatory candidate | established explanation |
| **Question** | an explicit unresolved information need | false proposition |
| **Evidence reference** | artifact or trace relevant to an evaluation | automatic proof or authority |

These roles MAY be expressed through `claim_kind`, typed relations, a profile mapping, or another versioned contract. They are not a mandatory enum in this contract.

## 4.3 Contract assertions

| Assertion ID | Required meaning |
|---|---|
| `NK-SEM-001` | semantic content is distinguishable from a source-bound assertion |
| `NK-SEM-002` | observation and measurement preserve method and provenance meaning |
| `NK-SEM-003` | interpretation and hypothesis remain distinguishable from observation |
| `NK-SEM-004` | evidence relevance does not automatically establish truth |
| `NK-SEM-005` | a question or unknown is not silently encoded as false |
| `NK-SEM-006` | admission state is not inferred only from semantic role or storage presence |
| `NK-SEM-007` | Claim scope and domain remain explicit when they affect interpretation |
| `NK-SEM-008` | role translation across profiles is declared and testable |

## 4.4 Anti-Canon

This family does not require:

- a universal ontology;
- one frozen list of all possible Claim kinds;
- an LLM classifier;
- a graph database;
- a mandatory separate `Proposition`, `Observation`, or `Evidence` table;
- a new event verb;
- a claim that the current vocabulary is complete.

---

# 5. Contract family II — Identity and Canonical Encoding 🧬

**Family ID:** `NK-ID`

## 5.1 Required identity layers

A profile MUST distinguish or explicitly map:

```text
content identity
≠ Claim identity
≠ lineage identity
≠ event identity
≠ storage identity
```

| Identity | Responsibility |
|---|---|
| **Content identity** | identifies canonical semantic content under a declared content contract |
| **Claim identity** | identifies the durable Claim record, including the identity-bearing scope declared by the contract |
| **Lineage identity** | groups an explicit continuity/revision family without equating every version |
| **Event identity** | identifies one recorded transition or append attempt/result |
| **Storage identity** | local row, object, shard, address, or backend key; never sufficient as semantic identity |

## 5.2 Contract assertions

| Assertion ID | Required meaning |
|---|---|
| `NK-ID-001` | backend-generated IDs are not the only semantic identity source |
| `NK-ID-002` | identity-bearing fields are declared per contract version |
| `NK-ID-003` | canonical encoding rules are deterministic within their declared version |
| `NK-ID-004` | Unicode, number, timestamp, null, ordering, omission, and ambiguity rules are explicit |
| `NK-ID-005` | hashes use declared algorithms, domains, and version separation |
| `NK-ID-006` | collisions cannot silently overwrite or merge distinct records |
| `NK-ID-007` | identity migration and aliasing preserve inspectable lineage |
| `NK-ID-008` | independent profiles can evaluate the same golden and invalid vectors |

The exact canonical bytes, normalization policy, hash agility, and migration rules remain owned by [Issue #14](https://github.com/velantrian/velantrim-native-kernel/issues/14). This skeleton establishes the separation, not the final encoding algorithm.

## 5.3 Anti-Canon

Identity MUST NOT depend permanently on:

- a PostgreSQL sequence;
- a SQLite rowid;
- Python object identity;
- one JSON library's undocumented serialization;
- one model provider's embedding;
- one processor's native memory layout.

---

# 6. Contract family III — Event, Observation, and Recorded Change 📜

**Family ID:** `NK-EVT`

## 6.1 Four distinct layers

Native Kernel MUST preserve the distinction between:

```text
🌍 represented-world occurrence
👁️ observation or measurement of that occurrence
💾 recording by a system
⚖️ admission or authority decision about the record
```

These are semantic layers. They are not additions to the accepted research event vocabulary.

## 6.2 Command-to-history boundary

A future implementation contract must make the following path explicit:

```text
command intent
→ validation
→ authorization / admission eligibility
→ durable idempotency decision
→ atomic append result
→ declared ordering
→ reducer input
→ derived state / projection
→ Receipt
```

## 6.3 Contract assertions

| Assertion ID | Required meaning |
|---|---|
| `NK-EVT-001` | a represented-world occurrence is not equated with the system record about it |
| `NK-EVT-002` | observation time, record time, valid time, and write order are not silently collapsed |
| `NK-EVT-003` | commands and recorded events remain distinguishable |
| `NK-EVT-004` | duplicate command semantics and idempotency scope are declared |
| `NK-EVT-005` | append acknowledgement states what durability and atomicity were achieved |
| `NK-EVT-006` | ordering rules are deterministic in the declared writer model |
| `NK-EVT-007` | reducer and schema versions are bound to replay evidence |
| `NK-EVT-008` | projection failure cannot silently rewrite authoritative history |
| `NK-EVT-009` | correction, supersession, restriction, and erasure remain explicit transitions |
| `NK-EVT-010` | tamper, truncation, reordering, and fork limits are declared under a threat model |

The detailed append, idempotency, ordering, crash, and replay contract remains owned by [Issue #15](https://github.com/velantrian/velantrim-native-kernel/issues/15).

## 6.4 Current vocabulary boundary

The current documented research vocabulary remains:

```text
ADMIT · LINK · UTILIZED · SUPERSEDED · ERASED
```

Terms such as `OBSERVED`, `CONFLICT_OPENED`, or `POLICY_CHANGED` are not accepted event verbs through this document. New verbs require a separate decision and compatibility analysis.

---

# 7. Contract family IV — Authority and Admission 🛡️

**Family ID:** `NK-AUT`

## 7.1 Problem

A system may record many things without granting every actor, model, source, retrieval result, or linked project the right to change admitted epistemic state.

## 7.2 Authority Envelope

Every authoritative transition SHOULD identify or translate an **Authority Envelope** containing the following meaning where applicable:

```text
actor / system reference
role or authority kind
authority domain and scope
policy reference and version
decision reference
basis / evidence references
delegation chain
temporal validity or expiry
constraints and known limits
```

This is not a mandatory storage schema. It is the minimum semantic explanation for why a transition was permitted.

## 7.3 Authority kinds

A profile MAY distinguish authority such as:

- observation authority;
- source/assertion authority;
- operational append authority;
- admission authority;
- epistemic promotion authority;
- conflict-resolution authority;
- deletion/restriction authority;
- architecture/governance authority.

These authorities MUST NOT be inherited implicitly from one another.

## 7.4 Contract assertions

| Assertion ID | Required meaning |
|---|---|
| `NK-AUT-001` | storage presence does not imply admission |
| `NK-AUT-002` | retrieval, ranking, utility, confidence, repetition, or model output does not imply authority |
| `NK-AUT-003` | authority kind, scope, policy, and actor remain inspectable |
| `NK-AUT-004` | delegation is explicit and cannot silently expand scope |
| `NK-AUT-005` | operator approval remains separate from empirical evidence |
| `NK-AUT-006` | cross-project data does not inherit authority through shared terminology or links |
| `NK-AUT-007` | deletion/restriction decisions identify authorization and proof limits |
| `NK-AUT-008` | an admission Receipt records the decision boundary without claiming truth beyond evidence |

## 7.5 Ecosystem boundary

- Titan cognition or tool output is an input, not automatic admission.
- Crystal evidence or TruthGate semantics do not become a mandatory Kernel component.
- Mentaury identity/continuity authority is not inherited by Kernel events.
- Kernel history does not become universal truth authority for the ecosystem.

---

# 8. Contract family V — Conflict and Explicit Unknowns ⚔️

**Family ID:** `NK-CFL`

## 8.1 Conflict classes

A profile MUST distinguish relevant classes rather than collapsing all disagreement into one flag:

```text
duplicate delivery
write-version race
divergent history
semantic contradiction
temporal mismatch
scope mismatch
provenance conflict
measurement disagreement
policy conflict
epistemic disagreement
projection drift
```

## 8.2 Conflict Set pattern

A future Conflict Set contract SHOULD be able to preserve:

- involved Claims, Events, histories, policies, or projections;
- conflict class and detection basis;
- candidate versus established status;
- directionality and scope;
- provenance and temporal context;
- unresolved questions and missing evidence;
- reviewer/authority decisions;
- resolution, deferral, reopening, and supersession history;
- Receipts and known limits.

A Conflict Set is a semantic pattern, not a mandatory root entity or event vocabulary in this document.

## 8.3 Unknown discipline

```text
unknown
≠ false
≠ unsupported certainty
≠ conflict resolution
≠ permission to invent provenance
```

The correct state MAY remain unresolved when evidence is insufficient or scopes differ.

## 8.4 Contract assertions

| Assertion ID | Required meaning |
|---|---|
| `NK-CFL-001` | candidate conflict is distinguishable from established conflict |
| `NK-CFL-002` | detection is distinguishable from resolution |
| `NK-CFL-003` | write order alone does not determine semantic correctness |
| `NK-CFL-004` | incompatible Claims may remain visible without a forced winner |
| `NK-CFL-005` | temporal, scope, provenance, and policy mismatches remain inspectable |
| `NK-CFL-006` | unknown and missing evidence remain explicit |
| `NK-CFL-007` | resolution identifies authority, policy, basis, scope, and history |
| `NK-CFL-008` | profile translation cannot silently discard unresolved conflict |

This family extends the structure around ADR-0003 without accepting a specific OCC, CRDT, LWW, multi-writer, or human-review implementation.

---

# 9. Contract family VI — Conformance and Semantic Equivalence 🔄

**Family ID:** `NK-EQV`

## 9.1 Contract registry

Every mature contract assertion SHOULD be traceable through a registry:

| Registry field | Meaning |
|---|---|
| `contract_family` | e.g. `NK-ID` |
| `contract_version` | version of the normative contract |
| `assertion_id` | stable assertion identifier |
| `required_semantics` | meaning that must be preserved |
| `equivalence_class` | byte, structural, semantic, or behavioural |
| `fixture_ids` | valid, invalid, replay, conflict, temporal, epistemic, or deletion vectors |
| `profile_mapping` | runtime/schema symbols that implement or translate the assertion |
| `evidence_record` | exact commit, command, environment, result, and limits |
| `support_state` | supported, unsupported, partial, or failed; never silently skipped |

## 9.2 Contract assertions

| Assertion ID | Required meaning |
|---|---|
| `NK-EQV-001` | every conformance claim names a contract and assertion version |
| `NK-EQV-002` | equivalence is defined rather than used as an undefined marketing term |
| `NK-EQV-003` | allowed and forbidden differences are explicit |
| `NK-EQV-004` | unsupported assertions remain visible |
| `NK-EQV-005` | fixture and evidence records identify exact repository/profile versions |
| `NK-EQV-006` | projection destroy/rebuild evidence is distinct from identity or deletion evidence |
| `NK-EQV-007` | two materially different profiles are required before cross-profile C3 claims |
| `NK-EQV-008` | a Receipt states its proof boundary and known omissions |

## 9.3 Equivalence layers

```text
byte equality
    ⊂ structural comparison
        ⊂ semantic comparison
            ⊂ bounded behavioural comparison
```

The nesting is conceptual, not automatic. A semantic comparison may intentionally allow different bytes, and behavioural equality does not prove identical internal representation.

This family maps directly to [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) and [Issue #17](https://github.com/velantrian/velantrim-native-kernel/issues/17).

---

# 10. Cross-cutting dimensions

The six families share five dimensions that MUST remain explicit where relevant.

## 10.1 Provenance

Provenance includes sources, actors, methods, transformations, policy/profile versions, known gaps, and contested accounts. Missing provenance remains a gap rather than invented continuity.

## 10.2 Time

Profiles SHOULD preserve or translate the relevant axes:

- represented-world or valid time;
- observation/measurement time;
- source publication time;
- record/ingestion time;
- admission/decision time;
- revision/supersession time;
- retention/restriction/erasure time;
- deterministic write order.

Not every profile must materialize every axis, but omission and approximation must be declared.

## 10.3 Scope

A meaning or authority statement may depend on domain, subject, jurisdiction, project, tenant, worldview frame, observer, method, or temporal interval. Scope MUST NOT be silently widened.

## 10.4 Receipt

A Receipt is an accountable processing record. It may show inputs, decisions, exclusions, conflicts, source range, profile versions, and limits. It does not by itself prove truth, completeness, authenticity, deletion, or task sufficiency.

## 10.5 Deletion and restriction

Logical `ERASED` state is not complete deletion evidence. Physical deletion, restriction, retention, backup expiry, downstream propagation, crypto-erasure, and residual metadata remain a separate technology-neutral contract owned by [Issue #16](https://github.com/velantrian/velantrim-native-kernel/issues/16).

---

# 11. End-to-end skeleton

```text
Source / actor / sensor / model / document
                │
                ▼
🧩 Semantic role is declared
   proposition / assertion / observation / hypothesis / question / evidence reference
                │
                ▼
🧬 Identity contract derives or validates identity
   content / Claim / lineage / event / storage distinction
                │
                ▼
📜 Recording contract appends an explicit change
   command / idempotency / ordering / schema / replay boundary
                │
                ▼
🛡️ Authority contract evaluates permitted transition
   actor / scope / policy / delegation / basis
                │
                ▼
⚔️ Reducer preserves state, conflict, and unknowns
   no silent winner / no invented provenance / no false certainty
                │
                ▼
🧾 Receipt records process and proof limits
                │
                ▼
🔄 Conformance registry maps meaning to fixtures and evidence
```

# 12. Anti-Canon

This contract does not make any of the following permanent architecture:

- Python, Rust, SQL, PostgreSQL, SQLite, files, graphs, vectors, FTS, LLMs, CPUs, GPUs, or future substrates;
- one class hierarchy or database schema;
- one universal ontology;
- one model of multi-writer consistency;
- one truth-scoring formula;
- one human or AI authority implementation;
- one fixed event vocabulary beyond current accepted records;
- one deletion mechanism;
- one definition of consciousness, life, reality, or ultimate origin.

# 13. Relationship to existing governance

| Area | Owning record |
|---|---|
| Canon vs implementation profiles | ADR-0001 |
| Conflict remains explicit | ADR-0003 |
| Rebuild-first conformance | ADR-0004 |
| Causal relations placement | ADR-0006 |
| Approval vs evidence | ADR-0007 |
| World and epistemic boundaries | ADR-0008 + `NK-EPI-001…008` |
| Storage profiles | ADR-0009 |
| This six-family skeleton | ADR-0010 — `ACCEPTED` |
| Canonical identity details | Issue #14 |
| Append/replay details | Issue #15 |
| Deletion/restriction details | Issue #16 |
| Executable conformance | Issue #17 |

Issue #1 remains unchanged. This document must not be represented as recovered `v0.1.2.1` design or evidence.

# 14. Next gates

1. Preserve ADR-0010 acceptance and the `foundational-skeleton/1.0` aliases in future revisions.
2. Keep this document bilingual and semantically aligned.
3. Define the exact identity contract and vectors under Issue #14.
4. Define the command/event integrity contract under Issue #15.
5. Define deletion and restriction semantics under Issue #16.
6. Create versioned fixture schemas and registry records under Issue #17.
7. Require separate ADRs when a detail changes Canon, event vocabulary, authority, identity-bearing fields, or equivalence guarantees.
8. Do not claim implementation, testing, wiring, activation, observation, or portability until exact repository evidence exists.