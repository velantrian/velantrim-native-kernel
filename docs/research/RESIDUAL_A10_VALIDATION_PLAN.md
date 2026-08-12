# Residual A10 Validation Plan

**State:** `PLANNING_ONLY / EXECUTION_NOT_AUTHORIZED`  
**Protocol:** `nk-residual-a10-validation-plan/1`  
**Plan ID:** `RAVP-001-residual-a10-validation-plan-v1`  
**Source checkpoint:** `ec421410d6ea5df86adca3a962ad2c5ba699e297`  
**Operator decision:** ADR-0027 / `OD-POST-D8-001`  
**Decision merge:** `57993f39906ae7266011f6146c9a485d0587d2bf`  
**Architecture:** `STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL`  
**Runtime expansion:** `FROZEN`  
**Product runtime thaw:** `false`  
**Production:** `false`

**[English](./RESIDUAL_A10_VALIDATION_PLAN.md) · [Русский](./RESIDUAL_A10_VALIDATION_PLAN.ru.md)**

## 1. Purpose

This document turns the six D6 `NOT_TESTED` A10 hypotheses into a bounded research-planning program. It does **not** preregister, implement, execute, or adjudicate a new experiment.

The residual targets are exactly:

```text
A10-H03
A10-H06
A10-H08
A10-H09
A10-H10
A10-H11
```

The allowed A10 outcomes remain exactly:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

No other epistemic outcome is introduced by this plan.

The plan follows one governing principle:

```text
one research question
→ one bounded falsification family
→ separate preregistration
→ separate execution-admission decision
→ only then, if authorized, implementation and execution
```

A giant “BPV-2” that combines unrelated claims is therefore not the default design.

## 2. Authority boundary

ADR-0027 authorizes only `RESIDUAL_A10_VALIDATION_PLAN` in `RESEARCH_PLANNING_ONLY` scope.

This plan does **not** authorize:

- any residual experiment implementation or execution;
- product runtime integration or runtime thaw;
- Final Canon promotion;
- production authorization;
- reducer v2 or new Event verbs;
- NK-EPI runtime;
- Issue #18 license/publication decisions;
- Issue #74 / ADR-0024 decisions;
- Track H recovered-source admission;
- a new database, product implementation profile, or product hardware profile;
- a universal substrate-independence claim.

A later family preregistration must be a separate authority layer. A later execution admission must be another separate authority layer.

## 3. Correction to the handoff: H11 is not federation

The exact A10 hypothesis is:

> `A10-H11` — Laboratory mechanisms can remain reproducible without becoming Architecture Canon.

Composition/federation is a **separate** capability class recorded by D7-F08. BPV1-001 was single-node, so composed/federated conformance remains untested, but it is not the meaning of H11 and must not be silently substituted for it.

This correction matters because testing federation under the label H11 would produce evidence for the wrong research question.

## 4. Independence classes

Residual research must declare independence precisely rather than treating “different language” as a synonym for “different substrate.”

| Class | Meaning |
|---|---|
| `INDEPENDENT_LANGUAGE` | implementation language differs materially |
| `INDEPENDENT_IMPLEMENTATION_STRUCTURE` | implementation is not a thin translation/import of the same internal structure |
| `INDEPENDENT_TEAM` | implementation authorship is organizationally/personally independent for the declared scope |
| `INDEPENDENT_CUSTODY` | evidence/artifacts are not solely controlled by the subject implementation owner |
| `INDEPENDENT_STORAGE_MODEL` | persistence/memory mechanism differs materially, not merely SQL dialect/schema |
| `INDEPENDENT_COMPUTATION_MODEL` | execution/computation mechanism differs materially, not merely programming language |
| `INDEPENDENT_HARDWARE_FAMILY` | physical carrier/processor family differs materially for the tested claim |
| `INDEPENDENT_SEMANTIC_ORACLE` | adjudication is outside the subject and does not depend on private subject state |

These axes are independent dimensions. One experiment may qualify on some and not others.

## 5. Global fail-closed rules

Every future residual family must preserve these rules before it can become a qualifying preregistration:

1. The subject cannot emit an authoritative PASS for itself.
2. Implementation self-report is raw input at most, never semantic truth by itself.
3. Private implementation state cannot be mandatory oracle input.
4. Failure conditions must be frozen before adjudication data is seen.
5. Oracle logic and thresholds must be frozen before adjudication.
6. Post-hoc criteria changes cannot rescue a failed run under the same experiment identity.
7. `INDETERMINATE` is a legitimate result.
8. `NOT_TESTED` is a legitimate result.
9. Pilot/calibration data must be separated from adjudication data.
10. Raw fact capture must be separate from semantic qualification.
11. The qualifier must be separate from the subject.
12. Outcome vocabulary must remain the five A10 outcomes above.

A test that cannot fail is not an A10 falsification test.

## 6. Family H03 — representation migration continuity

### Hypothesis

`A10-H03`: scoped identity and lineage continuity can survive representation migration.

### Why BPV1 did not test it

BPV1-001 created a materially different realization, but it did not execute a source→target migration and adjudicate identity/continuation relations across that migration.

### Testable question

Can a materially different target representation preserve declared semantic identity and lineage while substrate-local identity changes, without making source bytes, hashes, row IDs, or physical carrier identity the semantic criterion?

### Required independence

Minimum planning target:

```text
INDEPENDENT_IMPLEMENTATION_STRUCTURE
INDEPENDENT_STORAGE_MODEL
INDEPENDENT_SEMANTIC_ORACLE
```

Independent language/team/custody would strengthen the evidence but are not silently assumed.

### Core observables

- pre/post typed identity relation vectors;
- `MIGRATED_FROM` / `CONTINUATION_OF` lineage;
- Context, Provenance and Authority preservation;
- declared substrate-local identity change;
- declared loss vector;
- raw transformation facts separated from adjudication.

### Equivalence predicate

The migrated target preserves every materially required semantic identity/lineage relation for the preregistered cases even though local IDs, bytes, layout, storage representation or operation sequence differ.

### Allowed losses

Source serialization, local address/row/object identity, non-semantic layout/indexing details and other explicitly non-material metadata may be lost.

### Failure / hard refutation

Failure includes silent Provenance/Authority loss, inability to distinguish required identity relations, or inferring semantic continuity only from copied physical identifiers.

A hard refutation exists if a migration preserves all declared meaning-level content, yet required identity/continuation cannot be justified without making source-format physical identity itself universal architecture.

### Oracle boundary

A frozen implementation-neutral migration oracle sees externally exposed identity/provenance/lineage observations and declared loss. It does not read private target internals.

## 7. Family H06 — forgetting, disposal and erasure epistemics

### Hypothesis

`A10-H06`: forgetting/disposal can be represented without claiming impossible knowledge of physical substrate state.

### Why BPV1 did not test it

Physical and cryptographic erasure were explicitly outside BPV1 applicability. Logical compaction/loss witnesses are not evidence of physical residue destruction or key destruction.

### Three separate evidence lanes

H06 must not be one ambiguous “delete” test.

| Lane | What it may establish | Mandatory boundary |
|---|---|---|
| `LOGICAL_FORGETTING` | semantic/logical unavailability for scope | physical/crypto state remains `INDETERMINATE` unless separately observed |
| `CRYPTOGRAPHIC_ERASURE` | bounded crypto-erasure under declared key/custody/recoverability assumptions | subject self-report alone is non-qualifying |
| `PHYSICAL_ERASURE` | bounded sanitization/physical erasure under an independently inspectable recovery/residue boundary | opaque residue remains `INDETERMINATE` |

### Testable question

Can the architecture keep restriction, logical disposal, semantic forgetting/loss, cryptographic erasure, physical erasure and unknown physical residue distinct while never making a stronger claim than the evidence permits?

### Observables

- semantic recovery/query result after forgetting;
- a non-content-bearing disposition/accountability witness;
- independent key custody/sanitization evidence for crypto-erasure claims;
- independent sanitization/residue validation for physical-erasure claims;
- declared adversarial recovery effort boundary;
- explicit claim-strength classification.

### Failure / hard refutation

Failure includes promoting logical inaccessibility to physical erasure, accepting a self-authored PASS, collapsing forgetting into “never existed,” or retaining prohibited recoverable material solely to prove absence.

Hard refutation occurs if the semantic distinction among logical forgetting, cryptographic erasure, physical erasure and unknown residue cannot be preserved without either retaining the prohibited material or issuing an unjustifiably strong claim.

### External research role

NIST SP 800-88 Rev. 2 is a threat/validation design reference for media sanitization and cryptographic erase. It is **not** Native Kernel authority and cannot supply an H06 outcome by citation alone.

## 8. Family H08 — non-address-based dynamical continuity

### Hypothesis

`A10-H08`: a non-address-based substrate could preserve semantic identity/history through relational or dynamical continuity rather than stable byte addresses.

### Why BPV1 did not test it

BPV1 remained conventional digital computation. No analog or neuromorphic physical realization was adjudicated.

### Qualification tiers

```text
SIMULATION_OR_EMULATION
  → method rehearsal only
  → cannot support H08

PHYSICAL_NON_ADDRESS_REALIZATION
  → eligible for H08 only if every other gate qualifies

HYBRID_PROFILE
  → eligible only for its declared hybrid scope
  → companion mechanism cannot secretly hold the complete authoritative semantic state
```

### Testable question

Can a physical non-address-based dynamical realization preserve scoped identity, lineage and accountability when exact microstate, stable row/byte/neuron address and exact deterministic replay are unavailable?

### Required independence

```text
INDEPENDENT_COMPUTATION_MODEL
INDEPENDENT_HARDWARE_FAMILY
INDEPENDENT_IMPLEMENTATION_STRUCTURE
INDEPENDENT_SEMANTIC_ORACLE
```

### Anti-shadow rule

A conventional companion is allowed only as an explicit bounded part of a hybrid profile. If the companion stores the complete authoritative semantic state and history, while the analog/neuromorphic component is merely a calculator or decorative accelerator, the run does not establish H08.

### Allowed losses

Exact microstate, exact neuron/synapse/device identity, exact replay path, non-semantic physical coordinates and exact timing/weight values outside declared semantic scope may be lost.

### Failure / hard refutation

Failure includes hidden stable-address identity, a full digital shadow, promotion of simulation to hardware evidence, or semantic observability that depends on private internal state.

A hard refutation requires a qualifying physical non-address-based realization that cannot preserve required semantic identity/lineage/accountability even after exact microstate and physical-address identity are explicitly removed from the requirements.

## 9. Family H09 — probabilistic conformance

### Hypothesis

`A10-H09`: probabilistic substrates can be assessed with bounded statistical conformance without redefining uncertainty as failure.

### Why BPV1 did not test it

There was no probabilistic substrate and no preregistered repeated-trial statistical protocol.

### Qualification tiers

```text
SOFTWARE_STOCHASTIC_REHEARSAL
  → may qualify the statistical method only
  → cannot support a physical/probabilistic-substrate claim

MATERIALLY_PROBABILISTIC_REALIZATION
  → eligible only after semantic + statistical preregistration
```

### Two-layer oracle

H09 must separate:

1. **hard semantic invariants** — zero-tolerance forbidden outcomes for their declared scope;
2. **distributional obligations** — explicitly statistical properties with preregistered trial count/stopping rule, error/equivalence bounds and sufficient power.

Insufficient power yields `INDETERMINATE`, not support.

### Failure / hard refutation

Failure includes post-hoc thresholds, optional stopping, discarded adverse trials, treating every semantic divergence as “noise,” or reporting insufficient-power data as support.

Hard refutation occurs if an adequately powered preregistered protocol cannot distinguish required semantics from stochastic divergence strongly enough to keep the claim falsifiable, or a hard invariant is reproducibly violated inside the claimed scope.

### External research role

Physical p-bit/stochastic hardware literature is a candidate-realization reference only. Its existence shows that a materially stochastic realization class is not purely imaginary; it does not constitute Native Kernel evidence.

## 10. Family H10 — orthogonal storage/computation variation

### Hypothesis

`A10-H10`: storage and computation mechanisms can vary independently within declared semantic constraints.

### Why BPV1 did not test it

BPV1 varied language, history model and representation together. Those changes cannot isolate storage independence from computation independence.

### Minimum design

A qualifying family should use at least a 2×2 mechanism matrix:

```text
           Storage S1   Storage S2
Compute C1     C1/S1        C1/S2
Compute C2     C2/S1        C2/S2
```

`C1` and `C2` must differ in computation mechanism, not only language. `S1` and `S2` must differ in storage model, not merely SQL dialect or schema layout.

### Testable question

Can the storage axis change while computation is held materially fixed, and can computation change while storage is held materially fixed, without changing a required semantic law, identity relation, Authority rule or accountability property?

### Failure / hard refutation

Failure includes thin wrappers around one shared mechanism, semantic logic hidden inside a storage adapter, an oracle coupled to one cell, or uncontrolled simultaneous axis changes.

A hard refutation exists when an isolated storage or computation change necessarily alters a required meaning-level obligation rather than merely implementation mechanics or declared loss.

## 11. Family H11 — laboratory/Canon separation

### Hypothesis

`A10-H11`: laboratory mechanisms can remain reproducible without becoming Architecture Canon.

### Why BPV1 did not test it

H11 was not preregistered as a BPV1 falsification target. The current `BOUNDED_REFERENCE_LABORATORY` governance boundary is informative repository evidence, not BPV1 adjudication of H11.

### Dual-layer challenge

A future H11 family should deliberately maintain two independent layers:

```text
Historical laboratory reproduction layer
  → may require exact Python / SQL / JSON / SHA / Event / reducer / versioned bytes
  → exactness is allowed because the historical profile is being reproduced

Architecture conformance layer
  → must remain meaning-level
  → must not make those exact mechanisms universal requirements merely because the laboratory needs them
```

### Testable question

Can accepted laboratory evidence remain exactly reproducible under its own versioned profile manifest while the Architecture and its conformance/falsification rules remain mechanism-neutral?

### Failure / hard refutation

Failure includes Architecture documents or validators that mandate Python, SQL, JSON, SHA-256, Event, reducer, exact replay, UUID, current clocks or equivalent profile mechanisms solely because historical lab evidence depends on them.

Hard refutation occurs if a necessary architecture obligation cannot remain reproducible/testable unless a profile-specific lab mechanism is promoted into universal Architecture **only because** historical evidence reproduction requires it.

### Independence target

The minimum critical axis is `INDEPENDENT_SEMANTIC_ORACLE`; independent reviewer/reproducer, team or custody strengthens the result substantially because same-author boundary review is vulnerable to circular reasoning.

## 12. Recommended order

The recommended order is deliberately not the numerical H03→H11 order:

| Order | Family | Why first/next |
|---|---|---|
| 1 | H11 | protects every later family from profile→Canon leakage; lowest experiment burden |
| 2 | H03 | directly tests representation migration using conventional-digital resources without claiming new substrate support |
| 3 | H10 | establishes what “independent computation model” really means before hardware claims |
| 4 | H06 | logical lane is tractable; crypto/physical lanes demand stronger custody/observability |
| 5 | H09 | statistical protocol should be qualified before costly probabilistic-substrate adjudication |
| 6 | H08 | strongest specialized hardware/anti-shadow requirement; should come after oracle discipline is mature |

Order is a planning recommendation, not execution authorization.

## 13. Evidence package expected from any future family

A future preregistered family should define at minimum:

```text
hypothesis + scope
frozen semantic obligation inventory
independence-axis qualification
candidate realization identity
raw observables
external qualifier
frozen semantic oracle
failure / hard-refutation rules
allowed losses
threat/trust model
complete reproduction path
A10 outcome
```

Evidence must make it possible to fail the hypothesis. A polished demonstration without a credible negative path is non-qualifying.

## 14. External research references

These references inform candidate experiment design only. They are not architectural authority and do not change any A10 outcome.

- NIST SP 800-88 Rev. 2, *Guidelines for Media Sanitization* (2025) — H06 sanitization, cryptographic-erasure and validation/trust-boundary design reference.
- Singh et al., *Nature Communications* 15, 2685 (2024), DOI `10.1038/s41467-024-46645-6` — example of physical stochastic p-bit hardware relevant to H09 candidate realization research.
- Cotteret et al., arXiv:`2405.01305` (2024) — distributed representations in neuromorphic hardware, relevant to H08 candidate realization research.

A citation can motivate a test class. It cannot produce `SUPPORTED_FOR_SCOPE` for Native Kernel.

## 15. Non-target: composition/federation

D7-F08 remains important:

```text
BPV1 single-node local/scoped conformance
≠ composition/federation conformance
```

However, this is not H11. Composition/federation should receive its own future architecture/research gate if the operator authorizes it. This residual plan neither tests nor admits it.

## 16. Non-target: quantum/non-classical computation

A10-Q16 remains open. This plan does not invent a quantum family merely to make the roadmap look comprehensive.

A quantum/non-classical mapping would require its own research question about identity, observation history and accountability under measurement/state-change semantics. It remains `NOT_TESTED` and outside this plan.

## 17. Completion criteria for this planning gate

`RESIDUAL_A10_VALIDATION_PLAN` is complete only when reviewers can verify that:

1. all six D6 `NOT_TESTED` hypotheses are represented exactly;
2. H11 is not confused with federation;
3. each hypothesis has its own bounded falsification family;
4. each family declares the requested semantic obligations, question, independence, realization class, observables, equivalence predicate, allowed loss, failure, hard refutation, grounding, trust model, oracle, reproduction path and expected evidence;
5. H06 separates logical, cryptographic and physical claims;
6. H08 cannot gain substrate support from simulation/emulation;
7. H09 cannot gain substrate support from stochastic software rehearsal alone;
8. H10 cannot count a language change as a computation-model change;
9. H11 protects exact lab reproduction without universalizing lab machinery;
10. no family authorizes implementation or execution;
11. runtime remains frozen;
12. Final Canon and production remain unauthorized.

## 18. Next gate after this plan

If this plan becomes authoritative through merge and post-merge validation, the next bounded gate is:

```text
SEPARATE_FAMILY_PREREGISTRATION_SELECTION
```

That gate still does **not** authorize residual experiment execution.

A selected family would require its own preregistration PR and, after that, a separate execution-admission decision. Until those gates exist and explicitly authorize execution:

```text
residual experiment implementation: NOT AUTHORIZED
residual experiment execution:      NOT AUTHORIZED
product runtime integration:         NOT AUTHORIZED
runtime expansion:                   FROZEN
Final Canon:                         DEFERRED
production:                          false
```
