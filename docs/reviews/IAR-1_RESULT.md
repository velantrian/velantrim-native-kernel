# IAR-1 — Independent Architecture Review Result

**Process outcome:** `QUALIFYING_REVIEW_COMPLETE`  
**Protocol:** `nk-independent-architecture-review/1`  
**Result protocol:** `nk-independent-architecture-review-result/1`  
**Reviewed architecture commit:** `2dd51723e30d5f3c5e86268365bf4cf7639b5e9a`  
**Review surface:** PR #107  
**Reviewer identity:** `github-codex-review-agent`  
**Reviewer kind:** `AGENT`  
**Runtime:** `FROZEN`  
**BPV-1:** `BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION`

## Independence basis

The reviewer is a separate GitHub review agent. Repository-visible contributor/collaborator history contains only `velantrian`; the review agent did not author A1–A10 or `nk-integrated-blueprint-review/A1-A10-review-1`, received an immutable reviewed subject only after publication, and explicitly used the existing P1–C5 runtime as implementation-capture context rather than as an architectural oracle.

This satisfies the concrete-separation requirement of `nk-independent-architecture-review/1` for this review. It does **not** imply that a later BPV-1 implementation by the same current authorship lineage would itself be independently implemented.

## Review completeness

The review reports:

- mandatory packet read: **YES**;
- Q1–Q12 answered: **YES**;
- final finding register: **10 findings**;
- `BLOCKING`: **7** — `IAR-F01`, `IAR-F02`, `IAR-F03`, `IAR-F05`, `IAR-F07`, `IAR-F08`, `IAR-F09`;
- `MATERIAL`: **3** — `IAR-F04`, `IAR-F06`, `IAR-F10`;
- product runtime status: `FROZEN`;
- BPV-1 recommendation: remain blocked pending reconciliation.

The GitHub review comments are the source review evidence. `docs/reviews/IAR-1_RESULT.json` is the machine-readable transcription and guard surface.

## Q1–Q12 synthesis

### Q1 — Minimal kernel

The defensible minimum is smaller than the full A1–A10 taxonomy: preserve non-conflation of representation/Claim with reality/truth, scoped context and warrant, explicit uncertainty, accountable change/loss, and declared equivalence/capability. The complete A2 inventory, A3 transition catalogue and A6 lifecycle are not yet demonstrated architectural necessities.

### Q2 — Event-sourcing independence

Append-only Events and exact replay are not inherently necessary. However, current accountability/reconstruction obligations can force an Event-log equivalent unless state accountability, revision lineage and reconstruction are separated explicitly.

### Q3 — Bounded memory

Finite storage can preserve scoped current claims, uncertainty, summarized provenance, declared loss and bounded decision accounts. Exact reconstruction, permanent predecessor visibility, complete provenance and unlimited reopening of historical resolutions cannot survive arbitrary compaction without retention budgets or weakened obligations.

### Q4 — Identity

Stable bytes, hashes and global IDs are not universal requirements. The current draft still assumes stable distinguishable relata and continuity evidence more strongly than admitted; some identity kinds should remain analysis vocabulary rather than mandatory conformance inventory.

### Q5 — Time and ordering

No universal total order is required, but predecessor/successor lineage and from/to transitions imply a local consistent history. The minimum partial-order requirement must be explicit; the full eight-time inventory should not be treated as universally latent.

### Q6 — Epistemic separation

Source, Provenance and Authority can remain distinct as procedural roles without the current field layout. Evidence is relational and may be derived rather than separately stored. The portable obligation is non-conflation, not four mandatory first-class representations.

### Q7 — Conflict and uncertainty

Unresolved plurality and non-scalar uncertainty are viable. `Conflict ≠ Contradiction` remains under-operationalized unless each test preregisters proposition identity, logic, contextual/temporal alignment, assessment Authority and expected unresolved outcomes.

### Q8 — Deletion and forgetting

Restriction, logical erasure, physical erasure, cryptographic erasure and forgetting are distinguishable as claim types. Only restriction/logical disposition is generally internally observable. Physical/cryptographic erasure require threat-scoped external evidence; forgetting is an epistemic accessibility claim, not proof of global nonexistence.

### Q9 — Conformance

Representation-independent conformance is possible only if an external scenario-to-obligation matrix, mandatory observables, applicability rules and failure thresholds are fixed before implementation. Profile-local post-hoc scope selection is too permissive.

### Q10 — Reference-laboratory capture

The strongest recapture risks are not merely Python/SQL. They include A3 command/outcome algebra, transition records, reducer-like reconstruction boundaries, Receipt-shaped accountability, current lineage models, exact fixtures, canonical IDs and deterministic reference outputs.

### Q11 — Independent realization

A genuine cross-lineage realization must independently derive its state/change model, identifiers, history/storage strategy, result vocabulary, fixtures and semantic oracle from problem-level obligations. Reusing A3/A6 structures while changing language is only a port.

### Q12 — Refutation conditions

At minimum, preregister these non-negotiable observations:

1. if a non-event realization preserves the minimal purpose but cannot expose A3/A6 catalogues, weaken those catalogues rather than rejecting the realization;
2. if bounded compaction preserves current semantics and a loss witness but cannot reconstruct superseded detail, weaken universal reconstructability/history;
3. if profiles match final outputs while materially differing in provenance, uncertainty or Authority, refute full semantic equivalence for that scope;
4. if an opaque substrate cannot provide independent physical-erasure evidence, keep physical erasure `INDETERMINATE` for that scope.

## Finding register

| ID | Severity | Status | Disposition | BPV-1 | Core issue |
|---|---|---|---|---|---|
| IAR-F01 | BLOCKING | OPEN | CLARIFY | BLOCKS | conformance oracle/scope can be changed post hoc |
| IAR-F02 | BLOCKING | OPEN | SPLIT | BLOCKS | A3/A6 may encode current laboratory shape as architecture |
| IAR-F03 | BLOCKING | OPEN | SPLIT | BLOCKS | bounded-memory accountability lacks retention/sufficient-summary boundary |
| IAR-F04 | MATERIAL | OPEN | SPLIT | SHOULD_INFORM | identity/time taxonomies may be stronger than necessary |
| IAR-F05 | BLOCKING | OPEN | CLARIFY | BLOCKS | epistemic/conflict distinctions are insufficiently operationalized |
| IAR-F06 | MATERIAL | OPEN | SPLIT | SHOULD_INFORM | erasure assertions and independently verified substrate conditions are conflated |
| IAR-F07 | BLOCKING | OPEN | TEST | BLOCKS | BPV-1 refutations are not hard enough against post-hoc rescoping |
| IAR-F08 | BLOCKING | OPEN | SPLIT | BLOCKS | architecture-level threat model is absent |
| IAR-F09 | BLOCKING | OPEN | CLARIFY | BLOCKS | Context/Provenance/Authority grounding can recurse indefinitely |
| IAR-F10 | MATERIAL | OPEN | TEST | SHOULD_INFORM | composition of independently evolving scoped kernels is undefined |

A GitHub review thread may later be marked resolved after this finding is durably captured or reconciled, but that UI state must **not** be interpreted as semantic `status: RESOLVED`. The machine result remains authoritative for finding status until a D3 reconciliation record changes it.

## Stable-candidate claims after challenge

The review considers these reasonable **candidate** obligations, not Final Canon:

- representation ≠ represented reality;
- Claim ≠ truth;
- Unknown ≠ False;
- Context, Provenance and Authority are scoped;
- implementation/write order ≠ causal or semantic precedence;
- Revision, Supersession and erasure are non-equivalent;
- loss and conformance must be explicit.

## Claims that must remain provisional

- complete A2 ontology;
- A3 transition/outcome machine;
- A4 law package as one mandatory set;
- A5 identity/time taxonomy;
- A6 lifecycle graph;
- universal reconstruction/history;
- full A8 conformance/equivalence;
- independently verifiable erasure;
- broad substrate independence.

## Gate result

```text
independent_review_status: QUALIFYING_REVIEW_COMPLETE
finding_reconciliation: REQUIRED
open_blocking_findings: 7
BPV-1: BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION
runtime_expansion: FROZEN
product_runtime_thaw: NO
A1-A10: DRAFTED / PROVISIONAL
production_authorized: false
```

D3 must reconcile every `BLOCKING` finding with an explicit architecture-level record before BPV-1 design may begin. A recommended disposition is not itself a resolution.
