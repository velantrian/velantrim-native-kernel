# A9 — Reference Laboratory Boundary

**State:** `DRAFTED / PROVISIONAL`  
**Model identity:** `nk-reference-laboratory-boundary/A9-draft-1`  
**Architecture phase:** ADR-0025 / Issue #88  
**Previous slice:** `A8_SUBSTRATE_INDEPENDENCE_CONTRACT`  
**Next content slice:** `A10_OPEN_QUESTIONS_AND_FALSIFICATION`  
**Runtime expansion:** `FROZEN`

## 1. Purpose

A9 classifies the existing clean P1–C5 implementation lineage against A1–A8 without allowing the implementation to capture the architecture.

The current Python, PostgreSQL, SQLite, Event, reducer, Receipt, CI and evidence machinery is preserved as a bounded reference laboratory. A9 asks, for each mechanism:

1. what architecture-level obligation it usefully exercises;
2. what it demonstrates only for a declared profile and scope;
3. what remains partial or unsupported;
4. what is merely a profile-specific realization;
5. what can act as a falsification or regression instrument;
6. what must **not** be promoted into a universal Native Kernel requirement.

A9 does not delete, rewrite, weaken, or supersede accepted implementation contracts. It classifies their architectural role.

```text
existing mechanism
≠ architecture requirement

useful evidence
≠ proof of universal substrate portability

profile-specific realization
≠ architectural defect
```

## 2. Authority and evidence boundary

This document is architecture research/governance. It does not:

- modify `native_kernel/**` runtime semantics;
- modify accepted contracts or evidence bytes;
- authorize reducer-v2, new Event verbs, NK-EPI runtime, Temporal runtime, Admission lifecycle, deletion execution expansion, new databases, new language profiles, model adapters, network/cloud wiring, or production promotion;
- accept ADR-0003;
- decide Issue #74 / ADR-0024;
- decide Issue #18 license/publication terms;
- admit Track H operator-controlled sources;
- change assertion arithmetic `45/10/17/0` or NK-EPI `0/0/8/0`;
- claim P1–C5 is an independent implementation lineage in the strong cross-language/cross-hardware sense;
- claim PostgreSQL and SQLite operational equivalence.

## 3. Classification vocabulary

A9 uses six role labels. They classify a laboratory mechanism relative to A1–A8; they are not assertion-map states and do not replace A8 preservation states.

### `ARCHITECTURE_PRESERVING_EVIDENCE`

The mechanism provides bounded evidence that one or more architecture-level obligations can be realized without silently violating their meaning.

This label never means the mechanism itself is required by the architecture.

### `PROFILE_SPECIFIC_REALIZATION`

The mechanism is a concrete implementation choice that may remain valid for its profile but is replaceable in another conforming realization.

### `PARTIAL_ARCHITECTURE_COVERAGE`

The mechanism exercises part of an architecture obligation while leaving material distinctions, states, threat cases, environments, or authority questions unsupported.

### `FALSIFICATION_INSTRUMENT`

The mechanism/test/evidence can expose a contradiction, silent semantic collapse, replay divergence, identity drift, provenance loss, ordering error, or overclaim. Passing it is useful but does not prove the entire architecture.

### `LABORATORY_ONLY_CONSTRAINT`

The requirement is binding for the existing versioned laboratory lineage or evidence reproduction but is not established as substrate-neutral Canon.

### `NOT_ARCHITECTURE_EVIDENCE`

The mechanism may be operationally useful, but its existence alone does not support an architecture-level conformance claim.

## 4. Classification rule

A mechanism may carry more than one role. Classification is scoped by the architecture obligation under review.

Example:

```text
SHA-256 Event-chain verification
= ARCHITECTURE_PRESERVING_EVIDENCE
  for detectable recorded-history mutation within this laboratory

AND
= PROFILE_SPECIFIC_REALIZATION
  because SHA-256 and serialized hash chains are not universal Canon

AND
= FALSIFICATION_INSTRUMENT
  because a broken chain can expose integrity divergence
```

A9 therefore rejects one-dimensional statements such as “Event sourcing is architecture” or “SQL is irrelevant.” The correct question is which semantic obligation a mechanism realizes, under what scope, with what declared limits.

## 5. P1 — Semantic core

Current P1 includes canonical identity helpers, Claim/domain objects, authority policy, deterministic in-memory reducer behavior, deletion/restriction state transitions and bounded Receipts.

### Architecture-preserving evidence

P1 provides bounded implementation evidence for:

- explicit semantic identity rather than backend-row identity;
- separation of authority decisions from mere data presence;
- explicit transition outcomes instead of silent mutation;
- explicit restriction/deletion semantic states;
- Receipt overclaim guards;
- deterministic behavior for a declared implementation contract.

These align with A1 purpose/non-goals, A2 semantic distinctions, A3 transition/accountability obligations, A4 non-conflation laws, A5 scoped identity, and parts of A6 lifecycle/disposition.

### Profile-specific realization

The following are not universal requirements merely because P1 uses them:

- Python objects/classes;
- Python 3.11–3.12;
- canonical JSON/byte encoding choices;
- current digest prefixes and provisional digests;
- one deterministic reducer function;
- current enum/state representations.

### Partial coverage

P1 does not establish durable provenance, independent storage, cross-profile equivalence, physical deletion, full temporal semantics, A7 conflict/uncertainty states, or NK-EPI support.

## 6. P2 — PostgreSQL append/idempotency profile

P2 adds PostgreSQL persistence, writer lease/epoch fencing, append/idempotency behavior, sequence allocation, payload commitment and hash-chain history.

### Architecture-preserving evidence

P2 is useful evidence that the laboratory can preserve:

- explicit recorded-change lineage;
- idempotent command handling within a named scope;
- distinguishable retry versus conflicting reuse;
- writer authority/fencing boundaries;
- ordered recorded history for the declared laboratory profile;
- detectable history-integrity violations under the laboratory commitment scheme.

### Profile-specific realization

The following remain replaceable implementation mechanisms:

- PostgreSQL;
- SQL tables, row locks and transaction primitives;
- Psycopg;
- one-owner epoch lease representation;
- global and stream integer sequences;
- numbered SQL migrations;
- SHA-256 migration ledger;
- `nkp1` / `nke1` byte commitments;
- stored canonical Event-envelope bytes.

A conforming future profile may preserve identity, causal/lineage relations, idempotency, authority and accountability without reproducing these physical forms.

### Laboratory-only constraints

Exact sequence allocation, current Event envelope and database transactional behavior remain binding for reproducing P2–C5 evidence. They are not automatically A1–A8 requirements.

## 7. P3 — Replay, projections and Receipts

P3 adds deterministic upcasting, replay, projection rebuild, publication guards and persisted replay/rebuild Receipts.

### Architecture-preserving evidence

P3 provides bounded evidence for:

- history-visible state reconstruction;
- explicit lineage from recorded history to derived state;
- derived-state disposability/rebuildability in this profile;
- rejection of stale publication against a declared history head;
- accountable reconstruction through bounded Receipts;
- separation of authoritative recorded history from disposable projections.

These are strong laboratory realizations of A3 reconstruction/accountability, A4 history/view laws, A5 lineage, and A6 revision/history obligations.

### Profile-specific realization

A1–A8 do not require:

- Event replay from byte zero as the only reconstruction method;
- persisted SQL projection tables;
- one upcaster registry structure;
- monotonic projection-generation integers;
- PostgreSQL `REPEATABLE READ`;
- exact Receipt JSON/bytes.

A non-event-sourced system may still conform if it preserves the required history, lineage, accountability and reconstruction-equivalent obligations and declares any loss.

## 8. P4 — Assertion-scoped conformance evidence

P4 creates complete 72-assertion reports and traceability for the PostgreSQL profile.

### Architecture-preserving evidence

P4 is primarily a **measurement and falsification instrument**. It demonstrates a disciplined ability to:

- enumerate supported, partial and unsupported claims;
- bind a support claim to checks and environment metadata;
- prevent unsupported assertions from being silently promoted;
- distinguish repository reproduction from stronger conformance levels.

This supports A4 anti-overclaim laws, A8 explicit degradation and architecture-accountability requirements.

### Boundary

P4’s assertion registry is not itself the architecture ontology. A1–A8 remain the meaning-level authority for the blueprint. Existing assertion IDs continue to describe the current laboratory evidence surface and are not retroactively rewritten by A9.

## 9. P5 — SQLite profile and C3 comparison

P5 adds an independently implemented SQLite storage profile inside the same Python lineage, history import and a cross-profile comparator.

### Architecture-preserving evidence

P5/C3 is important because it demonstrates that some declared semantic/behavioral obligations can survive a storage-profile change:

- PostgreSQL and SQLite can produce equivalent declared semantic outcomes for supported comparison scenarios;
- SQL dialect, schema layout, locking strategy and server topology may differ while selected meaning-level results remain stable;
- profile-local identifiers/timestamps may differ without necessarily breaking semantic equivalence;
- cross-profile comparison can expose semantic drift.

This is genuine architecture-preserving evidence for **replaceable storage-profile realization within a narrow shared-language lineage**.

### Critical limitation

P5 does **not** establish strong substrate independence because PostgreSQL and SQLite profiles share major implementation assumptions:

- Python language/runtime;
- conventional digital memory and CPU execution;
- shared semantic-core/reducer model;
- shared current Event vocabulary and canonical encodings;
- closely related test harnesses and repository custody.

Therefore:

```text
PostgreSQL ↔ SQLite C3
= useful cross-profile evidence
≠ independent-language equivalence
≠ independent-computation-model equivalence
≠ arbitrary-substrate portability proof
```

### A9 reinterpretation of exact-byte equivalence

P5 currently contains BYTE/STRUCTURAL/SEMANTIC/BEHAVIOURAL comparison classes. Exact bytes remain valid where a versioned laboratory contract explicitly requires them, especially imported authoritative-history verification.

A9 does not generalize that rule across substrates. A8 is controlling at architecture level: different bytes may still preserve meaning, while equal bytes do not prove semantic equivalence.

## 10. C4 — Offline shadow evaluation

C4 evaluates the already-supported C3 assertion surface against an approved synthetic offline workload with no authoritative writes or side effects.

### Architecture-preserving role

C4 is predominantly a **falsification and bounded behavioral-evidence instrument**. It can expose:

- divergence under scenario execution;
- accidental authority promotion;
- hidden side effects;
- evidence/reporting inconsistencies;
- supported-assertion regressions.

### Boundary

C4 is not live production shadowing, not external authority, not proof of correct decisions, not privacy/compliance evidence, and not an architecture requirement that every future substrate must implement a “shadow evaluator.”

## 11. C5 — Bounded operational rehearsal

C5 runs synthetic, ephemeral scenarios covering security, privacy, recovery, rollback, incident, reliability and resilience categories and preserves repository-resident evidence bundles.

### Architecture-preserving role

C5 provides bounded evidence that the laboratory can preserve declared behavior and evidence boundaries across controlled operational scenarios. Its durable evidence bundles are useful for reproducibility and later falsification.

### Boundary

C5 does not establish:

- production readiness;
- live-user-data safety;
- cloud/IAM correctness;
- high availability;
- physical deletion;
- compliance;
- ecosystem authority;
- independent custody;
- universal runtime or substrate conformance.

Synthetic operational rehearsal is therefore **laboratory evidence**, not architecture authority.

## 12. Mechanism classification matrix

| Laboratory mechanism | A1–A8 obligation exercised | A9 role | Architectural requirement? |
|---|---|---|---|
| Explicit Claim/semantic identity | scoped identity and semantic distinction | `ARCHITECTURE_PRESERVING_EVIDENCE` + `PARTIAL_ARCHITECTURE_COVERAGE` | meaning obligation yes; current ID encoding no |
| Python domain objects | representation of ontology/transition concepts | `PROFILE_SPECIFIC_REALIZATION` | no |
| Current Event vocabulary | explicit change/history in P1–C5 | `LABORATORY_ONLY_CONSTRAINT` + `PROFILE_SPECIFIC_REALIZATION` | exact verbs/envelope no |
| Deterministic reducer v1 | reproducible declared transition result | `ARCHITECTURE_PRESERVING_EVIDENCE` + `LABORATORY_ONLY_CONSTRAINT` | exact reducer no |
| PostgreSQL append store | durable recorded history and authority fencing | `PROFILE_SPECIFIC_REALIZATION` | no |
| SQLite embedded store | alternate storage realization | `PROFILE_SPECIFIC_REALIZATION` | no |
| PostgreSQL↔SQLite comparator | semantic drift detection | `FALSIFICATION_INSTRUMENT` + `ARCHITECTURE_PRESERVING_EVIDENCE` | comparator implementation no |
| Hash chain | bounded recorded-history integrity detection | `PROFILE_SPECIFIC_REALIZATION` + `FALSIFICATION_INSTRUMENT` | SHA/hash chain no |
| Global/stream sequence | deterministic laboratory ordering | `LABORATORY_ONLY_CONSTRAINT` | global integer order no |
| Replay from Events | laboratory reconstruction and lineage | `ARCHITECTURE_PRESERVING_EVIDENCE` + `PROFILE_SPECIFIC_REALIZATION` | Event replay specifically no |
| Rebuildable projections | separation of authoritative/derived state | `ARCHITECTURE_PRESERVING_EVIDENCE` | separation obligation yes; SQL projection mechanism no |
| Receipts | bounded accountability | `ARCHITECTURE_PRESERVING_EVIDENCE` | accountability yes; current Receipt encoding no |
| P4 assertion reports | explicit support/degradation accounting | `FALSIFICATION_INSTRUMENT` | exact registry/report schema no |
| C4 shadow workload | side-effect/authority/regression probing | `FALSIFICATION_INSTRUMENT` | no |
| C5 rehearsal | controlled operational falsification/evidence | `FALSIFICATION_INSTRUMENT` + `PARTIAL_ARCHITECTURE_COVERAGE` | no |
| GitHub Actions matrices | reproducibility in declared environments | `FALSIFICATION_INSTRUMENT` | no |
| Repository-resident evidence ZIPs | preservation of exact historical evidence bytes | `LABORATORY_ONLY_CONSTRAINT` | no |

## 13. A1–A8 coverage summary

### A1 — purpose and non-goals

The laboratory demonstrates that a meaning/provenance/history-oriented kernel can be implemented with current technologies. It does not demonstrate hardware or computational-substrate neutrality.

### A2 — ontology

Several A2 concepts have current representations, but laboratory object models do not cover the full A2 ontology and may collapse distinctions not required by existing runtime contracts. Absence of a runtime field is not evidence that an A2 concept is unnecessary.

### A3 — abstract machine

P1–P5 exercise many transition/accountability patterns, but current command/Event/reducer structure is one mapping only. A3 transition families are not required to map one-to-one to Event verbs.

### A4 — semantic laws

The laboratory contains useful anti-overclaim, identity, history, provenance and derived-view guards. It does not executable-test all 28 A4 laws across independent substrates.

### A5 — identity, time and change

Current canonical IDs, sequences and timestamps provide partial mappings. The laboratory does not fully implement A5’s typed identity relations or all temporal dimensions. Write order cannot be used as a substitute for occurrence/causal/semantic precedence.

### A6 — lifecycle

Current admission, supersession, restriction, erasure and accounting mechanisms exercise some lifecycle positions. They do not implement A6 as a complete required runtime state machine, nor should they: A6 is a meaning-level model.

### A7 — conflict, uncertainty and revision

Current runtime has only partial conflict/revision representation and does not implement A7’s full tension/assessment/resolution taxonomy or typed uncertainty model. Missing A7 runtime support remains explicit and must not be inferred from generic contradiction links or reducer behavior.

### A8 — substrate independence

P5 provides limited storage-profile evidence. The laboratory does not establish full A8 conformance across independent languages, hardware, memory models, analog/neuromorphic systems, quantum systems, or unknown future substrates.

## 14. Failure and overclaim cases

The following interpretations are non-conforming to A9:

1. “PostgreSQL is primary, therefore SQL is Canon.”
2. “SQLite matches PostgreSQL, therefore substrate independence is proved.”
3. “Exact Event bytes match, therefore semantic equivalence is proved.”
4. “Different Event bytes exist, therefore semantic equivalence is impossible.”
5. “The reducer reconstructs state, therefore every future substrate needs a reducer.”
6. “The Event log preserves history, therefore every future substrate must be event-sourced.”
7. “C5 passes synthetic security scenarios, therefore production security is established.”
8. “A concept has no P1–C5 field, therefore it is not part of the architecture.”
9. “A laboratory mechanism is profile-specific, therefore it should be deleted.”
10. “Operator approval of P1–C5 is independent evidence for architecture truth.”
11. “Repository-resident evidence is independent custody.”
12. “Current assertion arithmetic grades the A1–A8 blueprint as a whole.”

## 15. Preservation rule for the existing laboratory

A9 does not require code removal merely because a mechanism is profile-specific.

```text
profile-specific
→ label correctly
→ preserve reproducibility
→ keep evidence lineage
→ prevent silent Canon promotion
≠ delete or rewrite automatically
```

Accepted laboratory contracts remain binding inside their declared versioned scope until separately changed through the decision process.

## 16. Relationship to pending decisions

- Issue #18 remains operator-controlled; A9 makes no license/publication choice.
- Issue #74 / ADR-0024 remains `PROPOSED / PENDING_OPERATOR`; reducer v1 remains immutable and reducer-v2 remains unauthorized.
- ADR-0003 remains `PROPOSED / NOT_STARTED`.
- Track H source admission remains operator-controlled.
- Issue #14/#15/#16/#17 retain their existing implementation/evidence scopes.

A9 classification does not prejudge any of these decisions.

## 17. Open questions deliberately deferred to A10

A9 identifies but does not settle:

- the minimum non-event-sourced equivalent of explicit change history;
- minimum accountability when exact replay is impossible;
- how much lineage continuity is required across lossy or probabilistic substrates;
- whether independent-language implementation is sufficient evidence for stronger substrate-independence claims;
- what analog/neuromorphic realization would count as a persistent identity/history equivalent;
- how forgetting can be demonstrated when the substrate cannot expose exact retained bytes;
- how conformance should be falsified when observations are inherently probabilistic;
- whether some current accepted contracts should later be recast as profile contracts rather than architecture contracts.

These belong to `A10_OPEN_QUESTIONS_AND_FALSIFICATION` and integrated A1–A10 review.

## 18. First-draft completion test

A9 bounded drafting is complete when a reviewer can take a P1–C5 mechanism and determine:

1. which A1–A8 obligation it exercises;
2. whether it is architecture-preserving evidence, profile-specific, partial, a falsification instrument, a laboratory-only constraint, or not architecture evidence;
3. what the current evidence actually demonstrates;
4. what it does **not** demonstrate;
5. whether replacing the mechanism would necessarily change Native Kernel meaning.

For this draft, that test is satisfied for the principal P1–C5 mechanisms listed above.

Final acceptance remains pending independent review, A10, integrated A1–A10 reconciliation, and a separate operator decision before any runtime thaw.
