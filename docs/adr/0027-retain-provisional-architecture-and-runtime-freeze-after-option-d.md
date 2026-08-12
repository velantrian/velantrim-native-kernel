# ADR-0027: Retain provisional architecture and runtime freeze after Option D

- **Decision status:** `ACCEPTED`
- **Evidence level:** `REPOSITORY_REPRODUCED`
- **Implementation status:** `COMPLETE`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-12`
- **Deciders:** `@velantrian`
- **Track:** `Architecture Canon / Evaluation Boundary`
- **Related:** `Issue #88`, `ADR-0025`, `ADR-0026`, `PR #117`, `PR #118`, `PR #119`, `PR #120`
- **Tags:** `post-d8, canon-promotion, runtime-freeze, residual-validation, substrate-neutrality`

> [!IMPORTANT]
> This is the separate operator Canon/runtime decision required by ADR-0026. It does **not** promote A1–A10 to Final Canon and does **not** thaw product runtime. It authorizes only a new bounded research-planning gate for the six A10 hypotheses that remain `NOT_TESTED`.

## Context 🧭

ADR-0026 required this sequence before any later Canon/runtime decision:

```text
independent review
→ reconciliation
→ preregistered bounded cross-lineage falsification
→ A10 classification
→ integrated re-review
→ consolidated synchronization
→ separate operator Canon/runtime decision
```

That sequence is now complete through D8 and the post-D8 machine-truth checkpoint.

The strongest justified current architecture position is:

```text
STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL
```

D6 classified exactly six A10 hypotheses as `SUPPORTED_FOR_SCOPE` and six as `NOT_TESTED`:

```text
SUPPORTED_FOR_SCOPE:
  A10-H01 H02 H04 H05 H07 H12

NOT_TESTED:
  A10-H03 H06 H08 H09 H10 H11
```

D7 did not promote the architecture to Final Canon. D8 synchronized that provisional result. PR #120 then repaired current machine truth and restored fail-closed historical/current validator separation at `ad459cd5301756936a26cab0997ba6c77c58191b`.

The remaining evidence gaps include representation migration continuity, physical/cryptographic erasure, analog/neuromorphic/probabilistic or non-classical realization, independent storage/computation axes, governance separation not experimentally adjudicated by BPV1, independent implementation team/custody/computation model, and composition/federation.

## Inputs considered 🔍

```text
Repository evidence:
- IAR-1 QUALIFYING_REVIEW_COMPLETE
- IAR-1-R1 COMPLETE
- BPV1-001 frozen preregistration and qualified D5-R1 evidence
- D6 A10 classification: 6 SUPPORTED_FOR_SCOPE / 6 NOT_TESTED
- D7 integrated re-review: STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL
- D8 Notion synchronization: 7/7 read-back verified
- PR #120 post-D8 machine truth and validator repair

Operator interpretation:
- scoped support is meaningful but insufficient for Final Canon;
- six NOT_TESTED hypotheses are too large a residual evidence surface for runtime thaw;
- further validation should target named residual hypotheses rather than reopen product implementation pressure.
```

No model consensus, CI success, or operator approval is treated as empirical proof.

## Decision drivers 🎯

- epistemic honesty;
- substrate-neutrality without universal overclaim;
- resistance to implementation capture;
- preservation of falsifiability;
- explicit separation of Canon, evidence, implementation and approval;
- bounded research progress without product-runtime pressure.

## Considered options 🧪

### Option A — Promote A1–A10 to Final Canon and keep runtime frozen

Rejected for now. Six A10 hypotheses remain `NOT_TESTED`; Final Canon would overstate the evidence even if runtime stayed frozen.

### Option B — Promote a provisional Canon and thaw a restricted product runtime scope

Rejected. Runtime implementation pressure could recapture unresolved architecture boundaries before residual evidence exists.

### Option C — Keep architecture provisional but thaw maintenance-plus-semantic runtime work

Rejected. Maintenance already remains allowed under the existing freeze; semantic runtime expansion is not justified by the post-D8 evidence.

### Option D — Retain the validated-provisional architecture, keep runtime frozen, and authorize residual validation planning only

**Selected.**

## Decision ✅

**We will:**

1. retain `STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL` as the strongest current architecture position;
2. defer Final Canon promotion;
3. keep product runtime expansion `FROZEN`;
4. keep P1–C5 as `BOUNDED_REFERENCE_LABORATORY`;
5. open a new bounded gate named `RESIDUAL_A10_VALIDATION_PLAN`;
6. target exactly `A10-H03/H06/H08/H09/H10/H11` unless a later explicit decision changes that scope;
7. require preregistered observables, failure conditions, applicability, loss semantics and independence class before any new experiment execution;
8. preserve `NOT_TESTED`/`INDETERMINATE` when evidence is absent or non-qualifying.

**We will not:**

- promote A1–A10 to Final Canon at this checkpoint;
- authorize BPV-2 or another experiment execution merely by accepting this ADR;
- thaw product runtime;
- authorize reducer-v2, new Event verbs, NK-EPI runtime, a new database/profile/language as product authority, or production;
- decide Issue #18, Issue #74/ADR-0024, or Track H admission;
- claim arbitrary future-substrate portability.

### One-line rationale

> With Option D complete but half of the A10 hypothesis inventory still untested, Native Kernel retains the strongest evidence-backed provisional architecture and continues targeted research while refusing premature Canon or runtime promotion.

## Consequences 📌

### Positive

- avoids converting one bounded conventional-digital experiment into a universal architecture claim;
- preserves the gains from BPV1 without discarding useful provisional obligations;
- keeps product implementation pressure from defining the remaining architecture;
- makes the next research scope explicit and falsifiable.

### Negative / accepted trade-offs

- product semantic/runtime feature expansion remains paused;
- Final Canon remains unavailable;
- residual validation may require materially different experimental methods rather than one BPV-style subject;
- some residual hypotheses may remain indeterminate for a long time.

## Invariants 🔒

1. `SUPPORTED_FOR_SCOPE ≠ universal proof`.
2. `NOT_TESTED ≠ SUPPORTED`.
3. Final Canon remains not authorized until a later explicit operator decision.
4. Product runtime remains frozen until a later explicit operator decision.
5. Research experiments remain isolated from product runtime and cannot self-promote.
6. A new experiment with materially different normative scope requires a new preregistered identity.
7. Historical BPV1 plan/oracle/evidence bytes are not rewritten.
8. Independent team/custody/computation-model evidence remains `NOT_ESTABLISHED` unless separately demonstrated.
9. Issue #18, Issue #74/ADR-0024 and Track H remain independent operator decisions.
10. Production remains unauthorized.

## Architecture-layer placement

| Question | Answer |
|---|---|
| Architecture Canon changed? | `no Final Canon promotion; provisional position retained` |
| Abstract contract changed? | `no` |
| Implementation profile selected? | `no` |
| Runtime code exists? | `no new runtime authorized by this ADR` |
| Production evidence exists? | `no` |

## Validation and evidence 🧪

| Evidence | Artifact | Result |
|---|---|---|
| D6 classification | `docs/research/BPV1_D6_A10_CLASSIFICATION.json` | `6 SUPPORTED_FOR_SCOPE / 6 NOT_TESTED` |
| D7 re-review | `docs/research/BPV1_D7_INTEGRATED_REREVIEW.json` | `STILL_PROVISIONAL` |
| D8 sync | `docs/research/BPV1_D8_CONSOLIDATED_SYNC.json` | `7/7 READ_BACK_VERIFIED` |
| post-D8 machine truth | PR #120 / `ad459cd5301756936a26cab0997ba6c77c58191b` | merged / post-merge green |
| operator decision | `docs/research/POST_D8_OPERATOR_DECISION.json` | `ACCEPTED / APPROVED` |

## Failure cases 🚨

This decision is violated if any later change, without a new explicit operator decision:

- labels A1–A10 Final Canon;
- thaws product semantic/runtime expansion;
- converts any residual `NOT_TESTED` hypothesis to supported by inference alone;
- starts a residual experiment before its normative scope and failure rules are fixed;
- treats the current Python/Rust/SQL/Event lineages as the semantic oracle for the residual program.

## Rollback / supersession

A later ADR may promote, weaken, reject, or supersede this provisional position only if it preserves the D0–D8 evidence chain and states the new evidence/constraint that justifies the change. No silent runtime thaw or retroactive BPV1 rescoping is permitted.
