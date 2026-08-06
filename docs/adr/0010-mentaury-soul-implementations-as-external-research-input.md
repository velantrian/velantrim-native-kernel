# ADR-0010: Mentaury Soul's implemented P0 mechanisms as external research input

- **Decision status:** `PROPOSED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Date:** `2026-08-06`
- **Deciders:** `pending operator decision`
- **Track:** `Evaluation`
- **Related:** `docs/VELANTRIM_ECOSYSTEM.md`, `docs/INTEGRATION_BOUNDARIES.md`, `ADR-0002`, `ADR-0004`, `ADR-0006`, external repository `velantrim-mentaury-soul` (`docs/P0_010_ATOMIC_SAME_STREAM_REDACTION.md`, `docs/P0_013_R1_DETERMINISTIC_REPLAY.md`, `docs/P0_015_EVIDENCE_GATE.md`)
- **Tags:** `cross-project, evaluation, replay, redaction, evidence-gate, relations`

> [!NOTE]
> This ADR exists so that citing a sibling project's working code never quietly turns into evidence for this repository's own architecture, and so that a real prior-art signal is not discarded just because it lives in another repository.

## Context 🧭

Native Kernel is drafting abstract contracts — deterministic replay/checkpoint equivalence (`ADR-0002`), rebuild-from-authoritative-history conformance (`ADR-0004`), and typed directed relations (`ADR-0006`) — without yet having a working reference implementation of its own; the Issue #1 conformance experiment has not started.

A cross-repository audit (recorded in `docs/VELANTRIM_ECOSYSTEM.md`, "Possible future complementarity" section) found that a sibling, independently developed Velantrim project, `velantrim-mentaury-soul`, has already implemented and tested narrower but structurally adjacent mechanisms:

- deterministic replay equivalence (`P0-013`: `state_hash(full replay) == state_hash(verified snapshot + tail replay)`);
- governed, same-stream, byte-for-byte-immutable-row redaction (`P0-010`);
- a deterministic evidence-gated belief-status transition (`P0-015`).

These are external, out-of-repository artifacts belonging to an independent research track. They do not prove Native Kernel's own architecture and must not be imported as code.

- **Problem:** how to benefit from a working, tested, adjacent implementation without treating it as evidence for Native Kernel's own contracts, without importing code, and without creating an implied runtime dependency between the two repositories.
- **Constraints:** preserve `INTEGRATION_BOUNDARIES.md` ("no package transfer of the complete research kernel into Crystal, Titan or Mentaury is implied or approved"); preserve honest evidence levels; preserve Native Kernel's independence.
- **Non-goals:** import Mentaury Soul source code, schemas, or tests; treat Mentaury Soul's passing tests as Native Kernel test evidence; create a package or runtime dependency; expand Issue #1 import scope.
- **Current implementation boundary:** public `main` contains documentation only for `ADR-0002`, `ADR-0004`, and `ADR-0006`; no replay, redaction, or relation runtime exists in this repository.
- **Source-derived facts:** `velantrim-mentaury-soul` is a separate repository under separate authority; its tests validate its own narrower domain, not Native Kernel's substrate-neutral claims.
- **Open uncertainty:** which specific ideas, if any, will be adopted, and in what re-specified form.

## Inputs considered 🔍

```text
Repository evidence:
- ADR-0002, ADR-0004, ADR-0006 remain PROPOSED / NOT_STARTED
- no committed replay, redaction, or relation implementation exists here

External research:
- velantrim-mentaury-soul, docs/P0_010_ATOMIC_SAME_STREAM_REDACTION.md
- velantrim-mentaury-soul, docs/P0_013_R1_DETERMINISTIC_REPLAY.md
- velantrim-mentaury-soul, docs/P0_015_EVIDENCE_GATE.md

AI-generated inputs:
- this ADR and the VELANTRIM_ECOSYSTEM.md complementarity note were drafted
  by an AI audit session comparing both repositories' documentation

Operator interpretation:
- pending
```

AI-generated inputs and an external project's own tests are design inputs, not Native Kernel implementation evidence.

## Decision drivers 🎯

- semantic durability;
- deterministic replay;
- epistemic honesty about evidence levels;
- portability;
- testability;
- avoiding premature coupling between independent projects;
- avoiding silent promotion of an external artifact into internal evidence.

## Considered options 🧪

### Option A — Ignore Mentaury Soul entirely

**Advantages**

- zero cross-project risk or confusion.

**Disadvantages**

- discards a working, tested, adjacent reference;
- slower discovery of gaps in Native Kernel's own abstract contracts.

### Option B — Import or vendor Mentaury Soul's implementation as a starting point

**Advantages**

- fast bootstrap for Native Kernel's own replay/redaction code.

**Disadvantages**

- contradicts `INTEGRATION_BOUNDARIES.md`;
- collapses two independent research tracks into one;
- hides which invariants Native Kernel has actually proven itself.

### Option C — Read-only, cited research input

**Description**

Treat Mentaury Soul's implementation as `DOCUMENTED`/`EXTERNALLY_OBSERVED` input when drafting or revising `ADR-0002`, `ADR-0004`, `ADR-0006`, and any future Native Kernel redaction or evidence-gate ADR, with explicit citation, and no code import.

**Advantages**

- benefits from prior art without importing it;
- keeps evidence levels honest;
- keeps both projects independent.

**Disadvantages**

- still requires Native Kernel to independently define, implement, and test any adopted idea.

## Decision ✅

**We will:**

- treat `velantrim-mentaury-soul`'s `P0-010`, `P0-013`, and `P0-015` as `DOCUMENTED`/`EXTERNALLY_OBSERVED` research input for `ADR-0002`, `ADR-0004`, `ADR-0006`, and any future Native Kernel redaction or evidence-gate ADR;
- cite the specific Mentaury Soul document (and commit/PR, where relevant) whenever an idea from it is adopted or discussed;
- require Native Kernel to independently define, implement, and test any adopted contract inside this repository before claiming `REPOSITORY_REPRODUCED` evidence for it.

**We will not:**

- import Mentaury Soul source code, schemas, or tests into this repository;
- treat Mentaury Soul's passing tests as Native Kernel test evidence;
- create a package, API, or runtime dependency on `velantrim-mentaury-soul`;
- claim that Mentaury Soul implements or validates Native Kernel's architecture;
- expand Issue #1 import scope through this ADR;
- authorize any runtime integration; the boundaries in `INTEGRATION_BOUNDARIES.md` remain in force unchanged.

### One-line rationale

> In the context of designing replay, redaction, and relation contracts before a working reference implementation exists, facing the risk of either discarding useful prior art or improperly importing it, we selected read-only, explicitly cited research input to sharpen contract design while keeping evidence levels and project independence intact.

## Consequences 📌

### Positive

- sharper contract drafts informed by a tested, adjacent implementation;
- an explicit, auditable citation trail instead of an implicit or undocumented influence;
- no new dependency, package, or runtime coupling.

### Negative / accepted trade-offs

- still requires full independent implementation and testing inside this repository;
- citations must be kept current as Mentaury Soul's own code evolves;
- a careless reader could conflate "cited" with "validated" if this ADR is skipped.

### Neutral

- Architecture Canon is unchanged;
- no previously accepted contract is changed by this ADR.

## Invariants 🔒

1. Citing Mentaury Soul's implementation does not by itself raise Native Kernel's evidence level above `DOCUMENTED`/`EXTERNALLY_OBSERVED` for the cited idea.
2. No Native Kernel contract may be marked `REPOSITORY_REPRODUCED` based on Mentaury Soul's own tests.
3. No source code, schema, or dependency is imported from `velantrim-mentaury-soul` through this ADR.
4. Any adopted idea must be re-specified as a Native Kernel abstract contract before implementation, not copied verbatim.
5. This ADR does not authorize runtime integration; `INTEGRATION_BOUNDARIES.md` boundaries remain in force.

## Architecture-layer placement

| Question | Answer |
|---|---|
| Architecture Canon changed? | `no` |
| Abstract contract changed? | `no` (this ADR governs citation practice, not a contract) |
| Implementation profile selected? | `no` |
| Runtime code exists? | `no` |
| Production evidence exists? | `no` |

## Implementation notes 🔧

- affected paths: documentation only (this ADR, `docs/adr/README.md` index, `docs/INTEGRATION_BOUNDARIES.md` cross-link);
- schema/events: none;
- feature flags: none;
- migration/upcast: none;
- compatibility: none;
- rollback: revert this ADR file and index entry; no runtime effect to unwind;
- Titan/Crystal boundary: unaffected; Mentaury Soul boundary: read-only citation only, per `INTEGRATION_BOUNDARIES.md` → "Native Kernel and Mentaury Soul".

## Validation and evidence 🧪

| Evidence | Artifact / command | Result | Required for next level |
|---|---|---|---|
| Documentation | this ADR + `VELANTRIM_ECOSYSTEM.md` complementarity note | proposed | operator acceptance |
| Repository test | none applicable | not applicable | this ADR governs citation practice, not runtime |
| Cited external artifact | `velantrim-mentaury-soul` P0-010 / P0-013 / P0-015 | `EXTERNALLY_OBSERVED` | independent Native Kernel reproduction, if adopted |

## Failure cases 🚨

- a future PR imports Mentaury Soul code or schemas directly;
- a future PR or ADR claims Mentaury Soul's tests as proof of a Native Kernel contract;
- a reader treats the "possible future complementarity" language in `VELANTRIM_ECOSYSTEM.md` as an already-approved integration;
- a citation is left in place after Mentaury Soul's own implementation changes underneath it.

## Rollback / supersession

This ADR may be rejected or superseded if citing an independent, separately governed project is judged to create confusion between project boundaries even in read-only citation form. No runtime effect exists to roll back, since none is created by this ADR.

## Consistency checklist 🔱

- [x] Event history remains authoritative about recorded changes.
- [x] History is not equated with truth.
- [x] Projection/cache is not promoted to Canon.
- [x] Relevance/utility is not equated with truth.
- [x] Candidate conflict is not described as resolved conflict.
- [x] Current technology is not silently promoted to permanent architecture.
- [x] Titan and Crystal boundaries remain explicit.
- [x] Issue #1 import scope is not silently expanded.
- [x] Decision status, evidence level, and implementation status remain separate.

## References 📚

- [`VELANTRIM_ECOSYSTEM.md`](../VELANTRIM_ECOSYSTEM.md)
- [`INTEGRATION_BOUNDARIES.md`](../INTEGRATION_BOUNDARIES.md)
- [`ADR-0002`](./0002-state-checkpoints-are-disposable.md)
- [`ADR-0004`](./0004-rebuild-from-authoritative-history.md)
- [`ADR-0006`](./0006-causal-links-are-relations.md)
- External: `velantrim-mentaury-soul` — `docs/P0_010_ATOMIC_SAME_STREAM_REDACTION.md`, `docs/P0_013_R1_DETERMINISTIC_REPLAY.md`, `docs/P0_015_EVIDENCE_GATE.md`

A citation alone is not proof that a Mentaury Soul mechanism applies to or validates Native Kernel.
