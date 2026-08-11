# ADR-0026: Independent challenge before bounded cross-lineage falsification

- **Decision status:** `ACCEPTED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `GOVERNANCE_PARTIAL`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-11`
- **Deciders:** `@velantrian`
- **Track:** `Architecture Validation`
- **Related:** `Issue #88`, `ADR-0025`, `A10`, `INTEGRATED_A1_A10_REVIEW`
- **Tags:** `independent-review, falsification, substrate-neutrality, runtime-freeze, post-blueprint`

> [!IMPORTANT]
> This decision authorizes a **validation phase**, not product-runtime expansion. Runtime remains frozen. It does not accept ADR-0024, choose Issue #18, admit Track H sources, promote A1–A10 to final Canon, or establish universal substrate independence.

## Context

ADR-0025 required the A1–A10 blueprint to be completed and integrated before any separate post-blueprint decision. A1–A10 drafting and the first integrated review are now `COMPLETE / PROVISIONAL`. The integrated review found no known blocking internal semantic contradiction after explicit reconciliation, but it explicitly did **not** establish independent architectural validation.

The existing P1–C5 Python/PostgreSQL/SQLite lineage remains useful, but it is a bounded reference laboratory with shared implementation ancestry. PostgreSQL↔SQLite C3 is real bounded cross-profile evidence, not independent-language, independent-computation-model, independent-team, or universal-substrate evidence.

The operator selected the post-blueprint direction that combines independent conceptual challenge with a later bounded cross-lineage falsification instrument while keeping product runtime frozen.

## Considered options

### Option A — Independent review only

Run an independent architecture review before any further work.

**Strength:** strongest immediate protection against self-confirming architecture.

**Limitation:** creates no executable cross-lineage evidence by itself.

### Option B — Bounded falsification experiment first

Start an alternative implementation experiment immediately.

**Strength:** produces practical pressure on the blueprint quickly.

**Rejected as first step because:** experiment design could accidentally encode the current authorship lineage's assumptions and become self-confirming.

### Option C — Provisional Canon plus restricted runtime thaw

Promote the integrated blueprint provisionally and reopen a narrow runtime scope.

**Rejected because:** current implementation pressure could recapture the provisional Canon before independent challenge or cross-lineage falsification.

### Option D — Independent challenge, reconciliation, then one bounded cross-lineage falsification experiment

**Selected.**

## Decision

Native Kernel enters a bounded **Post-Blueprint Validation** phase with this exact sequence:

```text
A1–A10 PROVISIONAL BLUEPRINT
→ INDEPENDENT_ARCHITECTURE_REVIEW
→ REVIEW_FINDING_RECONCILIATION
→ BPV-1 BOUNDED CROSS-LINEAGE FALSIFICATION
→ A10 OUTCOME CLASSIFICATION
→ INTEGRATED RE-REVIEW
→ SEPARATE OPERATOR CANON / RUNTIME DECISION
```

The next active content gate is:

```text
INDEPENDENT_ARCHITECTURE_REVIEW
```

`OPERATOR_POST_BLUEPRINT_DECISION` is therefore satisfied by this ADR, but it remains part of the historical blueprint gate record and is not retroactively treated as A11.

## Independent-review gate

The independent review protocol is defined in:

- `docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md`
- `docs/INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md`

Independent architectural validation is **not established merely by publishing the protocol**.

A qualifying review must have a reviewer identity and evidence trail that demonstrate the reviewer did not author A1–A10 or the integrated review and was tasked to search for counterexamples, hidden assumptions, unnecessary obligations, circularity, non-falsifiability, and implementation capture rather than to confirm the existing design.

The following do not satisfy the independent-review gate by themselves:

- the current integrated review;
- this ADR or the operator approval that created it;
- CI success;
- regression tests;
- Notion synchronization;
- Codex quota notices;
- a review performed by the same authorship/reasoning lineage without an explicit independence basis.

## BPV-1 admission rule

BPV-1 may begin only after:

1. a qualifying independent review is recorded;
2. all blocking/material findings are explicitly reconciled, rejected with rationale, or left open with a declared experiment dependency;
3. the experiment plan names the exact hypotheses and falsification conditions it will test;
4. the experiment remains isolated from product runtime.

BPV-1 is a **falsification instrument**, not a new implementation profile automatically admitted to the product or Canon.

The preferred experiment deliberately avoids relying on current implementation machinery as architectural authority, including where practical:

- no Python semantic core as oracle;
- no current reducer as oracle;
- no current Event envelope as required architecture;
- no current PostgreSQL/SQLite schemas as required architecture;
- no current ID prefixes or exact fixture bytes as semantic authority;
- no mandatory append-only Event log;
- no exact replay requirement unless independently justified by an obligation.

A different programming language and non-event-sourced realization are strong candidates for reducing shared-lineage bias, but neither language choice nor any specific storage model is promoted into Canon by this ADR.

## Validation targets

Candidate obligations to challenge include, at minimum:

- representation ≠ represented reality;
- Claim ≠ truth;
- Source / Evidence / Provenance / Authority remain distinct and scoped;
- Unknown ≠ False;
- semantic identity ≠ storage/byte identity;
- identity is typed/scoped rather than one universal ID;
- write order ≠ occurrence/causal/semantic precedence;
- Revision ≠ overwrite;
- Supersession ≠ deletion or falsity;
- Conflict ≠ necessarily Contradiction;
- Detection ≠ Resolution;
- uncertainty need not be one scalar;
- lifecycle is not a mandatory linear pipeline;
- logical / physical / cryptographic erasure / forgetting remain distinct;
- conformance and loss are explicitly scoped;
- Event sourcing, SQL, Python, JSON, SHA-256 and exact replay are not universal Canon unless falsification forces a stronger obligation.

These are **candidate stable obligations**, not final Canon.

## Runtime and authority boundary

The following remain exact:

```text
runtime_expansion: FROZEN
product_runtime_thaw: NO
semantic_runtime_expansion_authorized: false
reducer_v2: NOT_AUTHORIZED
new_event_verbs: NOT_AUTHORIZED
nk_epi_runtime: NOT_AUTHORIZED
new_database_profile: NOT_AUTHORIZED
production_authorized: false
P1-C5: BOUNDED_REFERENCE_LABORATORY
automatic_canon_promotion: NO
automatic_runtime_promotion: NO
```

This ADR does not decide:

- Issue #18 license/publication terms;
- Issue #74 / ADR-0024 outcome;
- Track H source admission;
- reducer-v2 semantics or implementation;
- a production or maturity promotion;
- universal support for analog, neuromorphic, probabilistic, quantum, or arbitrary future substrates.

## Evidence and outcome discipline

BPV-1 results must use the A10 outcome vocabulary exactly:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

`NOT_TESTED ≠ SUPPORTED`.

A failed experiment is a valid and potentially valuable result. If preserving an obligation requires recreating a supposedly non-essential mechanism, the relevant architecture claim must be weakened, refuted, or left indeterminate for the tested scope rather than hidden by redesigning the experiment after the fact.

## Consequences

### Positive

- attacks implementation capture before any runtime thaw;
- separates conceptual independence from executable cross-lineage evidence;
- gives A10 a real path from hypotheses to scoped outcomes;
- allows the architecture to become smaller and stronger when unsupported assumptions fail;
- preserves the current laboratory and historical evidence without making them architectural authority.

### Negative / accepted trade-offs

- runtime feature work remains paused;
- a genuine independent reviewer may not be immediately available;
- review may reopen parts of A1–A10 already considered coherent internally;
- BPV-1 may weaken or refute attractive architecture claims;
- cross-lineage work is intentionally slower than adding features to the current Python lineage.

## Invariants

1. Runtime remains frozen through independent review and BPV-1 unless a later explicit operator decision says otherwise.
2. A1–A10 remains provisional until a later operator Canon decision.
3. P1–C5 remains a bounded reference laboratory.
4. Independent review cannot be self-certified by the same authorship lineage.
5. BPV-1 is admitted only as a falsification instrument.
6. No experiment outcome automatically promotes Canon, runtime, maturity, or production status.
7. Loss, partial preservation, unsupported mappings and indeterminate results must remain visible.
8. Historical contracts, reducer-v1 histories and evidence identities are not rewritten.
9. Issue #18, Issue #74/ADR-0024 and Track H authority remain separate.
10. Universal substrate-independence claims remain forbidden without substantially broader named evidence.

## Exit criteria

This validation phase does not end merely because BPV-1 executes. A later operator decision requires:

- independent review record and independence basis;
- reconciliation record for its findings;
- exact BPV-1 plan identity;
- reproducible BPV-1 artifacts/results;
- A10 outcome classification;
- integrated re-review across affected A1–A10 obligations;
- explicit list of still-provisional obligations and absent evidence;
- a separate operator decision on Canon promotion and any exact runtime scope, if any, to reopen.

## Rollback / supersession

A later ADR may supersede this phase only by preserving the evidence/history created under it and explicitly stating whether independent review or BPV-1 was completed, blocked, weakened, or abandoned. No silent runtime thaw is permitted.