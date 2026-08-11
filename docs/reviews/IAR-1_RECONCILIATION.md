# IAR-1 — Architecture Finding Reconciliation

**Reconciliation identity:** `IAR-1-R1`  
**Protocol:** `nk-independent-architecture-review-reconciliation/1`  
**Input review:** `IAR-1 / QUALIFYING_REVIEW_COMPLETE`  
**Architecture status after reconciliation:** `PROVISIONAL_RECONCILED`  
**Runtime:** `FROZEN`  
**Next gate after authoritative merge:** `BPV1_PLAN_AND_PREREGISTRATION`  
**BPV-1 execution:** `NOT AUTHORIZED`

## 1. Purpose

IAR-1 found that several attractive A1–A10 structures were still stronger than the project had evidence to justify. This reconciliation does not defend those structures. It deliberately **shrinks and separates** the provisional architecture so that a later BPV-1 can falsify it without merely reproducing the current Python/Event/reducer lineage.

A1–A10 remain preserved as first-draft provenance. Where this record conflicts with their wording, this reconciliation is the current provisional interpretation until a later integrated re-review or operator Canon decision.

## 2. Smaller minimum Kernel

The minimum candidate architecture is now limited to these problem-level obligations:

1. representation and Claim are not silently equated with represented reality or truth;
2. scope, Context, warrant/provenance and Authority assumptions are explicit where materially relevant;
3. `Unknown`, uncertainty and unsupported states remain representable without coercion to `False`;
4. change, revision, supersession, retention and loss are accountable for the declared scope;
5. equivalence, capability, degradation and loss claims are made against preregistered observables and failure conditions.

The following remain useful **reference taxonomies**, but are no longer treated as the universal minimum shape of a Native Kernel:

- the complete A2 ontology inventory;
- A3 `K → K′`, the fixed transition-family catalogue and common outcome vocabulary;
- A5's seven identity kinds and eight temporal dimensions as one mandatory inventory;
- A6's nine lifecycle positions;
- Receipt-shaped accountability;
- Event-log-shaped history;
- exact reconstruction or exact replay.

A future realization may use snapshots, witnesses, procedural accounts, bounded summaries, or another state/change model if it preserves the preregistered obligations for its declared scope.

## 3. Preregistered conformance oracle

Before BPV-1 implementation begins, its plan must freeze a `PRE_REGISTERED_CONFORMANCE_SCENARIO` containing at least:

```text
scenario_id
purpose_scope
mandatory_obligations
applicability_rules
mandatory_observables
equivalence_predicates
allowed_declared_losses
failure_thresholds
hard_refutation_observations
grounding_mode
threat_model
oracle_authority
```

Rules:

- the implementation under test does not decide its own mandatory obligations after execution;
- `NOT_APPLICABLE` requires a preregistered rationale;
- changing mandatory obligations, applicability, equivalence predicates or failure thresholds after execution **invalidates the run for the claimed scope**;
- a redesigned scope requires a new experiment identity; the previous outcome remains recorded;
- full conformance requires preservation of every mandatory obligation for that scenario, not merely matching final outputs.

This resolves the self-confirming scope/oracle problem in `IAR-F01` and `IAR-F07`.

## 4. Accountability without universal Event sourcing or exact reconstruction

Accountability and reconstructability are now separate capability classes.

### Candidate required classes

`CURRENT_ACCOUNTABILITY` — the current scoped position and its material warrant/loss state remain inspectable.  
`DECLARED_RETENTION_SCOPE` — the realization declares what historical detail is retained and for how long/by what budget.  
`LOSS_WITNESS` — when detail is compacted, forgotten or unavailable outside that retention scope, the loss boundary is explicit enough to prevent silent overwrite being misrepresented as preserved history.

### Optional capabilities unless a scenario preregisters them

- `EXACT_RECONSTRUCTION`;
- permanent predecessor visibility;
- exact replay;
- complete provenance retention forever;
- unbounded reopening of every historical resolution.

Compaction outside a declared retention scope may be conformant. Silent overwrite **inside** the retained accountability scope is not.

This resolves `IAR-F03` and removes the hidden Event-log-equivalent pressure identified by `IAR-F02`.

## 5. Identity, time and order

A5's taxonomies remain analytical vocabulary. A scenario must declare which identity relations and temporal/order dimensions are materially required.

A realization is not required to expose all seven identity kinds or all eight temporal dimensions merely to be considered a Kernel. If a required distinction cannot be represented, the result is `PARTIAL`, `LOSSY`, `UNSUPPORTED`, or `INDETERMINATE` for that scope rather than automatic global non-conformance.

No global total order is introduced. When lineage is required, the minimum is only the local partial ordering needed to make the declared predecessor/successor or causal claim meaningful.

This resolves `IAR-F04`.

## 6. Epistemic roles and conflict semantics

The portable requirement is **non-conflation of semantic roles**, not mandatory storage fields.

- Source, Provenance and Authority may be represented procedurally, relationally or by external witness;
- Evidence may be derived rather than stored as a first-class object;
- a realization must not silently collapse these roles when the scenario declares them material.

Every conflict/contradiction scenario must preregister:

```text
proposition_identity_predicate
logic_or_conflict_relation
context_alignment_rule
temporal_alignment_rule
assessment_authority
allowed_unresolved_outcomes
```

`Conflict` remains a broader tension category. `Contradiction` is always logic/scope dependent. A failed case cannot be rescued after execution by relabeling it as a context mismatch or different Authority decision unless that distinction was preregistered.

This resolves `IAR-F05`.

## 7. Deletion, erasure and forgetting

The architecture now distinguishes three evidence layers:

1. **logical disposition claim** — restriction/logical erasure inside the semantic system;
2. **substrate-condition claim** — physical or cryptographic erasure under a declared observation boundary/threat model;
3. **epistemic accessibility claim** — forgetting/loss relative to accessible sources and retained evidence.

Physical or cryptographic erasure cannot be upgraded from a self-assertion alone. It requires threat-scoped evidence whose verification Authority is declared separately from the unverified claim. If sufficient external evidence is unavailable, the correct outcome is `INDETERMINATE`, not stronger erasure.

Forgetting never proves global nonexistence.

This resolves `IAR-F06`.

## 8. Architecture-level threat model

Substrate neutrality does not remove adversaries. Before a claim of accountable provenance/history/conformance can be tested, the scenario must declare:

### Protected meanings

- provenance/Authority basis actually relied upon;
- history/accountability claims;
- loss declarations;
- conformance evidence.

### Adversarial cases to consider where relevant

- forged Source/provenance/Authority;
- history fork;
- truncation;
- rollback;
- equivocation between observers;
- withheld counterevidence;
- unavailable witness;
- colluding witness;
- compromised conformance certifier.

The architecture does **not** require one cryptographic mechanism. It requires explicit trust assumptions and explicit failure/uncertainty semantics. A realization that cannot establish authenticity under its declared threat model must say so rather than silently claiming strong accountability.

BPV-1 planning must include negative fixtures for the relevant adversarial cases.

This resolves `IAR-F08`.

## 9. Finite grounding of Context, Provenance and Authority

Every evaluation that follows Context/Provenance/Authority chains must declare one finite grounding mode:

- `EXTERNALLY_ATTESTED_ROOT`;
- `EXPLICIT_ASSUMED_ROOT`;
- `BOUNDED_RECURSIVE_CLOSURE`;
- `DECLARED_CYCLE`;
- `TERMINAL_UNKNOWN_OR_GAP`.

A chain may not claim stronger support merely by recurring indefinitely. Cycles, assumptions and terminal gaps are part of the meaning and must remain inspectable.

Different grounding assumptions are a material conformance difference and cannot be hidden by having the same final answer.

This resolves `IAR-F09`.

## 10. Composition is a separate capability class

Base substrate-independence claims are narrowed to **scoped, non-composed realizations**.

Local conformance does not imply federation/composition conformance. A future composed test must separately declare semantics for:

- overlapping Contexts;
- identity disagreement;
- provenance union/loss;
- Authority conflict;
- concurrency;
- partial failure;
- whether plurality remains separate or is projected into a common scope.

No centralized coordinator is implied by the base architecture.

This resolves `IAR-F10` without pretending distributed composition has already been solved.

## 11. Hard refutation observations for BPV-1

The following must be copied unchanged or made stricter in the BPV-1 preregistration:

1. a non-event realization preserves the minimal purpose but cannot expose the A3/A6 catalogues → **weaken the catalogues; do not reject the realization for that reason**;
2. bounded compaction preserves declared current semantics plus a loss witness but cannot reconstruct superseded detail → **weaken universal reconstructability/history**;
3. profiles match final outputs while materially differing in provenance, uncertainty or Authority → **full semantic equivalence is refuted for that scope**;
4. an opaque substrate cannot provide independent physical-erasure evidence → **physical erasure remains `INDETERMINATE` for that scope**;
5. any post-execution change to mandatory obligations, applicability, equivalence predicates or failure thresholds → **the old run cannot be rescued; create a new experiment identity**.

## 12. Finding dispositions

| Finding | Final D3 status | Architecture effect |
|---|---|---|
| IAR-F01 | RESOLVED | external preregistered conformance oracle |
| IAR-F02 | RESOLVED | A3/A6 structures demoted from universal minimum to reference taxonomy |
| IAR-F03 | RESOLVED | bounded accountability separated from exact reconstructability |
| IAR-F04 | RESOLVED | identity/time inventories become scenario-required dimensions, not universal latent inventory |
| IAR-F05 | RESOLVED | epistemic/conflict tests receive preregistered operational boundaries |
| IAR-F06 | RESOLVED | erasure claim type separated from external substrate evidence |
| IAR-F07 | RESOLVED | hard refutations + no post-hoc rescue rule |
| IAR-F08 | RESOLVED | architecture-level trust/threat boundary added |
| IAR-F09 | RESOLVED | finite grounding modes added |
| IAR-F10 | RESOLVED | base claim narrowed; composition becomes separate capability class |

`docs/reviews/IAR-1_RECONCILIATION.json` is the machine-readable disposition record.

## 13. Gate state after reconciliation

```text
IAR-1: QUALIFYING_REVIEW_COMPLETE
IAR-1-R1: COMPLETE
open BLOCKING findings: 0
open MATERIAL findings: 0
A1-A10: DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY
BPV-1 plan: NEXT
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
runtime_expansion: FROZEN
product_runtime_thaw: NO
production_authorized: false
```

This reconciliation **does not** prove the refined architecture is correct. It only makes the next falsification experiment capable of failing for reasons defined before implementation.
