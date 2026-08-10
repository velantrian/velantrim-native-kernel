# A10 — Open Questions and Falsification

**State:** `DRAFTED / PROVISIONAL`  
**Model identity:** `nk-open-questions-falsification/A10-draft-1`  
**Architecture phase:** ADR-0025 / Issue #88  
**Previous slice:** `A9_REFERENCE_LABORATORY_BOUNDARY`  
**Next gate:** `INTEGRATED_A1_A10_REVIEW`  
**Runtime expansion:** `FROZEN`

## 1. Purpose

A10 closes the first drafting pass of the A1–A10 Architecture Re-foundation by making uncertainty explicit and by defining how important Native Kernel hypotheses can be weakened or refuted.

A10 is not a catalogue of promises. It is a **falsification boundary**.

```text
architectural hypothesis
+ declared scope
+ observable obligation
+ counterexample / falsifier
+ evidence quality
→ SUPPORTED_FOR_SCOPE | WEAKENED | REFUTED | INDETERMINATE | NOT_TESTED
```

A10 does not turn the blueprint into Canon. A1–A10 remain `DRAFTED / PROVISIONAL` until integrated review and a separate operator decision.

## 2. Evidence and authority boundary

A10 does not:

- modify `native_kernel/**`, contracts, profiles, fixtures, evidence bytes, or runtime behavior;
- authorize reducer-v2, new Event verbs, NK-EPI runtime, Temporal runtime, full Admission, deletion execution expansion, new databases, language ports, model adapters, cloud/network wiring, maturity promotion, or production authorization;
- decide Issue #18 license/publication terms;
- decide Issue #74 / ADR-0024;
- accept ADR-0003;
- admit Track H operator-controlled sources;
- change assertion arithmetic `45/10/17/0` or NK-EPI `0/0/8/0`;
- claim arbitrary future-substrate compatibility;
- treat absence of a falsifier as proof of truth.

## 3. Falsification vocabulary

### `SUPPORTED_FOR_SCOPE`
A declared test or body of evidence survived an explicit falsification attempt within a named scope. This is bounded support, not universal proof.

### `WEAKENED`
Evidence shows that the hypothesis needs narrower scope, stronger preconditions, or revised terminology, but does not yet establish full refutation.

### `REFUTED`
A reproducible counterexample violates a required semantic obligation under the scope in which the hypothesis claimed it would hold.

### `INDETERMINATE`
Available observations cannot distinguish preservation from failure with sufficient confidence or authority.

### `NOT_TESTED`
No qualifying falsification attempt exists. `NOT_TESTED ≠ SUPPORTED`.

These are A10 research outcomes; they do not replace the P4 assertion-map states or A8 preservation/conformance states.

## 4. Qualification rule for a falsification test

A meaningful falsification record should declare:

1. **Hypothesis** — what may be false.
2. **Scope** — where the claim is intended to hold.
3. **Preserved obligation** — which A1–A9 distinction/law/transition/lineage property matters.
4. **Observable** — what can actually be inspected.
5. **Counterexample condition** — what observation would weaken/refute the claim.
6. **Authority and provenance** — who/what produced the observation and under which method.
7. **Independence class** — same implementation lineage, independent language, independent team, independent custody, independent computation model, or other declared class.
8. **Loss declaration** — what cannot be observed or reconstructed.
9. **Outcome** — one A10 outcome, with rationale.
10. **Reproduction path** — enough information to repeat the attempt where possible.

A test that can only ever pass and has no declared counterexample is not an A10 falsification test.

## 5. Major hypotheses and falsifiers

| ID | Provisional hypothesis | What would weaken or refute it | Current status |
|---|---|---|---|
| `A10-H01` | Core semantic distinctions can be specified independently of one representation/storage technology. | A required A1–A7 distinction cannot be expressed on a materially different realization without collapsing meaning that the architecture requires. | `NOT_TESTED` across independent computation models |
| `A10-H02` | Explicit history/accountability does not require Event sourcing specifically. | Every viable non-event-sourced mapping necessarily loses required change lineage/accountability or must recreate an equivalent Event log in substance. | `NOT_TESTED` |
| `A10-H03` | Scoped identity/lineage continuity can survive representation migration. | A migration preserving declared semantics still cannot establish required identity/continuation relations without relying on source-format physical identity. | `PARTIALLY_SUPPORTED` only by current same-lineage mappings; not a universal claim |
| `A10-H04` | Unknown, uncertainty and unresolved plurality can be preserved without one universal confidence scalar. | A required decision/accountability scenario cannot be represented without silently forcing uncertainty into a scalar or binary truth state. | `NOT_TESTED` across independent models |
| `A10-H05` | Revision/supersession can preserve prior epistemic lineage without silent overwrite. | A conforming bounded-memory realization cannot retain required accountability without unbounded retention of superseded state. | `NOT_TESTED` |
| `A10-H06` | Forgetting/disposal can be represented without claiming impossible knowledge of physical substrate state. | The architecture cannot distinguish logical disposal, inaccessible state and actual physical/cryptographic erasure without retaining forbidden proof material. | `OPEN / INDETERMINATE` |
| `A10-H07` | Independent-language implementations provide stronger portability evidence than PostgreSQL↔SQLite in one Python lineage. | Independent-language implementations agree only because they share hidden representation assumptions, or diverge on A1–A8 obligations despite matching fixtures. | `NOT_TESTED`; stronger evidence class, not sufficient proof |
| `A10-H08` | A non-address-based substrate could preserve semantic identity/history through relational or dynamical continuity rather than stable byte addresses. | Analog/neuromorphic mapping cannot expose enough stable lineage, Context, Authority or accountability to satisfy the required obligations. | `NOT_TESTED` |
| `A10-H09` | Probabilistic substrates can be assessed using bounded statistical conformance without redefining uncertainty as failure. | Required semantic distinctions cannot be separated from observational noise or tests become non-falsifiable because any divergence is excused as probability. | `NOT_TESTED` |
| `A10-H10` | Storage and computation mechanisms can vary independently within declared semantic constraints. | Changing one axis necessarily changes a semantic law/identity relation/authority rule that was claimed substrate-neutral. | `PARTIALLY_SUPPORTED` for storage profiles only |
| `A10-H11` | Laboratory mechanisms can remain reproducible without becoming Architecture Canon. | Maintaining accepted evidence reproducibility requires architecture documents to mandate profile-specific bytes/SQL/Python mechanisms as universal obligations. | `SUPPORTED_FOR_SCOPE` as governance discipline; not a substrate proof |
| `A10-H12` | Conformance can be scoped and loss-aware rather than binary universal compatibility. | Real mappings cannot state partial/lossy/indeterminate preservation without making comparison meaningless or non-actionable. | `NOT_TESTED` broadly |

`PARTIALLY_SUPPORTED` above is descriptive prose for current research context, not a new machine-readable assertion state.

## 6. Open-question registry

### `A10-Q01` — Minimum explicit change history
What is the minimum structure that preserves accountability when a realization is not event-sourced?

A candidate answer must distinguish at least: what changed, relevant identity/lineage, Context, Authority where applicable, and enough temporal/causal relation to avoid silent overwrite.

### `A10-Q02` — Reconstruction without exact replay
If exact replay is impossible, what counts as reconstruction-equivalent evidence? Possible candidates include certified snapshots plus lineage proofs, reversible state transitions, independently checkable derivations, or bounded audit witnesses. No candidate is Canon yet.

### `A10-Q03` — Identity on lossy substrates
How much lineage can be lost before `CONTINUATION_OF` or `SAME` under a declared identity relation becomes unjustified?

### `A10-Q04` — Independent-language evidence threshold
Is one independent-language implementation enough to strengthen an A8 claim? A10 answer: **stronger than same-language profile comparison, but not sufficient by itself**. Independence of team, representation assumptions, computation model and custody may matter separately.

### `A10-Q05` — Analog persistence
What observable makes an analog state a persistent memory/identity carrier when exact bytes and stable addresses do not exist?

### `A10-Q06` — Neuromorphic continuity
Can distributed synaptic/dynamical patterns provide lineage and revision accountability without requiring exact neuron-to-record identity?

### `A10-Q07` — Probabilistic conformance
What statistical test, confidence protocol and repeated-trial boundary is strong enough to falsify a preservation claim without converting model confidence into Evidence or truth?

### `A10-Q08` — Forgetting proof
How can a realization demonstrate that information is no longer semantically recoverable without retaining the very content or secret whose absence must be shown?

### `A10-Q09` — Physical deletion observability
When a substrate cannot expose its physical residue, which claims must remain `INDETERMINATE` rather than being promoted from logical deletion to physical erasure?

### `A10-Q10` — Bounded memory versus auditability
What information must survive compaction/forgetting so accountability remains meaningful? Unbounded history retention is not assumed to be universally possible or desirable.

### `A10-Q11` — Causal order without global sequence
What is the minimum causal/lineage relation required when no total global order exists?

### `A10-Q12` — Authority on decentralized substrates
How is Authority represented when there is no single writer, database transaction, process owner or global lock?

### `A10-Q13` — Derived-state boundary
How can a substrate distinguish authoritative retained meaning from disposable/derived views when it does not expose database-like storage layers?

### `A10-Q14` — Semantic equivalence observables
Which observable obligations are sufficient for `FULL_CONFORMANCE_FOR_SCOPE`, and which apparently equal outputs can still hide provenance/uncertainty/authority loss?

### `A10-Q15` — Contract reclassification
Which accepted current contracts are architecture contracts, which are profile contracts, and which contain mixed layers that should later be split without rewriting historical evidence?

### `A10-Q16` — Quantum or non-classical computation
No current blueprint evidence establishes a useful Native Kernel mapping to quantum computation. What would count as persistent identity, observation history, and reproducible accountability when measurement alters state? This remains an open research question, not a roadmap promise.

### `A10-Q17` — Self-modifying realization
How can a realization change its own mechanisms while preserving the semantic contract, lineage of change and authority for the change itself?

### `A10-Q18` — Evidence independence
What minimum combination of independent implementation, reviewer, custody and environment is required before a claim may be described as independently validated?

## 7. Falsifiers for recurring overclaims

The following observations must weaken or refute the corresponding overclaim rather than be explained away:

1. **Universal portability overclaim:** an independent realization cannot preserve a required distinction → universal wording must be withdrawn or scoped.
2. **Semantic equivalence overclaim:** outputs match but provenance/Authority/uncertainty differs materially → full semantic equivalence fails.
3. **Identity overclaim:** IDs match but lineage/referent relation diverges → identifier equality is insufficient.
4. **History overclaim:** final state matches but required revision/supersession history is unrecoverable → history/accountability conformance fails.
5. **Deletion overclaim:** logical inaccessibility is observed but physical residue cannot be checked → physical erasure remains indeterminate.
6. **Conflict-resolution overclaim:** one implementation chooses a winner where the architecture permits unresolved plurality → the implementation is not evidence for a universal winner rule.
7. **Determinism overclaim:** repeatability exists only because one deterministic runtime is shared → substrate-independent determinism is not established.
8. **Production overclaim:** synthetic C5 scenarios pass → production safety/readiness is still not established.
9. **Independent-evidence overclaim:** two profiles share core language, team, harness and custody → the evidence is not an independent lineage in the strong sense.
10. **Future-substrate overclaim:** no mapping/test exists → compatibility remains `NOT_TESTED`, not presumed.

## 8. Contrasting substrate thought experiments

These are falsification aids, not implementation commitments.

### 8.1 Eventless state-transition archive

Assume a system stores certified state snapshots plus typed change witnesses but no canonical Event log. A2–A8 obligations should be tested against whether change lineage, Authority, Context, revision and reconstruction remain inspectable. If not, H02 weakens.

### 8.2 Distributed neuromorphic memory

Assume meaning is carried by distributed changing patterns, with no stable row or byte address. Test whether referent/semantic identity, lineage, uncertainty and revision can be expressed without pretending one neuron/synapse equals one Record. Failure would weaken H08.

### 8.3 Lossy bounded-memory agent

Assume old details are compacted or forgotten. Test whether the system can preserve required accountability and uncertainty about lost material without fabricating exact history. Failure would weaken H05/H06/H10.

### 8.4 Probabilistic realization

Assume repeated execution can produce a distribution of valid outputs rather than one deterministic byte sequence. Test whether conformance can be scoped to invariant semantic obligations and whether real divergence remains falsifiable. If every failure can be dismissed as noise, H09 is non-qualifying.

### 8.5 Independent-language digital profile

Assume a second implementation is produced without importing Python domain classes or serializer code. Matching current fixtures would be stronger evidence than P5/C3, but hidden shared ontology/fixture assumptions still need explicit accounting. It cannot by itself establish arbitrary-substrate portability.

## 9. Stop conditions

Architecture work must stop and re-open earlier assumptions when any of the following occurs:

- an A4 semantic law cannot be stated consistently with A1–A3 purpose/ontology/machine;
- A5 identity/time rules make A6 lifecycle or A7 revision accountability impossible without contradiction;
- A8 conformance requires physical sameness that A1/A2 explicitly reject;
- A9 classification shows that a supposedly architectural requirement has no meaning-level justification beyond current implementation convenience;
- an A10 falsifier reproducibly refutes a hypothesis inside its claimed scope;
- two blueprint documents use the same term with materially incompatible meanings;
- a proposed conformance test has no possible failure condition;
- runtime work is needed merely to make the architecture claim look true.

Stop means: record the contradiction, narrow or revise the hypothesis explicitly, preserve history, and perform review. It does not mean silently edit prior claims away.

## 10. Relationship to current P1–C5 evidence

Current laboratory evidence is useful primarily for regression and bounded falsification:

- P1–P3 can falsify some identity/history/accountability assumptions inside the current profile;
- P4 can expose assertion overclaim;
- P5/C3 can expose storage-profile semantic drift;
- C4 can expose side effects/authority drift under offline scenarios;
- C5 can expose bounded operational regressions.

None of these supplies strong evidence for H01–H10 across independent computation models.

## 11. Relationship to pending decisions

A10 does not prejudge:

- Issue #18 license/publication;
- Issue #74 / ADR-0024 reducer-v2 topology;
- ADR-0003 runtime conflict semantics;
- Track H source admission;
- future language/storage/hardware profiles.

The open-question registry may inform later decisions, but it does not authorize them.

## 12. First-draft completion test

A10 drafting is complete when a reviewer can:

1. identify the major architecture hypotheses that remain unproved;
2. identify at least one meaningful falsifier or weakening condition for each major hypothesis;
3. distinguish `NOT_TESTED` and `INDETERMINATE` from support;
4. locate the minimum-history, identity, forgetting, probabilistic-conformance, independent-evidence and non-classical-substrate questions;
5. see explicit stop conditions for returning to earlier A1–A9 assumptions;
6. confirm that no A10 statement authorizes runtime expansion or operator-reserved decisions.

For this draft, that test is satisfied as a **first drafting pass**. It does not establish that any open hypothesis is true.

## 13. Post-A10 gate

With A10 drafted, the document inventory becomes:

```text
A1–A10: DRAFTED / PROVISIONAL
next gate: INTEGRATED_A1_A10_REVIEW
runtime expansion: FROZEN
reference laboratory: BOUNDED
production authorization: false
```

The integrated review must reconcile terminology, contradictions, duplicate concepts, cross-document dependencies, current contract mappings and falsification coverage across A1–A10. Only after that review may the operator separately decide whether any next architecture or runtime phase is authorized.
