# Agent Memory Atlas donor reconciliation — 2026-09-28

**Status:** `EXTERNAL DONOR · RESEARCH INPUT · NON-CANONICAL · NOT RUNTIME AUTHORITY · NARROW RECONCILIATION NOTE`

Source: https://neoneye.github.io/agent-memory-atlas/

## Purpose

Record the narrow residual questions raised by Agent Memory Atlas **after** checking existing Velantrim coverage, without treating an external survey/pattern catalog as architecture authority.

This is **not** the first Agent Memory Atlas intake into Velantrim, and it is **not** a new multi-principle package.

```text
NEW ATLAS RECONCILIATION != FIRST ATLAS INTAKE INTO VELANTRIM
THIS NOTE RECORDS ONLY RESIDUAL QUESTIONS BEYOND EXISTING COVERAGE.
```

## Existing Velantrim coverage / prior Atlas-related / pre-existing overlapping coverage

| Surface | Existing coverage relevant to this donor |
|---|---|
| Native Kernel — [`docs/research/MEMORY_EVALUATION_PROTOCOL_V0.md`](MEMORY_EVALUATION_PROTOCOL_V0.md) | §10 conflict, correction/supersession, deletion durability and resurrection resistance, valid-time vs knowledge/record-time profiles; §12 positive obligations vs negative invariants, including the always-abstain caveat; §4 abstention count where meaningful; §14 already lists "Agent Memory Atlas-style correction/deletion/governance evaluation" as an evidence inspiration. |
| 💠 Crystal — `docs/research/MEMORY_EVAL_ADVERSARIAL_PROFILE_V0.md`, [PR #462](https://github.com/velantrian/velantrim-exocortex-crystal/pull/462) (merged) | §3 correction/supersession durability; §4 deletion durability / resurrection resistance, including re-ingest of the original source, derived surfaces, and "newly observed equivalent claim != resurrection of erased record identity/provenance"; §6 positive obligations vs negative invariants and the always-empty/always-abstain trap; §8 names Agent Memory Atlas as an external, non-normative source. |
| 🕸 Graphiti Fractal Lab — `docs/AGENT_MEMORY_EVALUATION_PROFILE.md` (main); FM-13 → FM-16 Honest Empty line on branch `experiment/falkordblite-deterministic-memory` (`docs/research/FM16_CLOSURE_AND_INDEPENDENT_REVIEW_2026-09-11.md`, `RESEARCH_STATUS.md`) | Retrieval relevance / no-relevant-memory qualification; forbidden-hit rate and abstention rate (profile §10); required negative invariants and positive obligations (profile §9). Current status: `FM-16 Honest Empty = NOT_ESTABLISHED`. |

## Already covered in Native Kernel — temporal semantics

The distinction between valid time, observation/knowledge time, record time and write order **pre-exists** in Native Kernel. Agent Memory Atlas provides external convergence only, not a new donor delta.

```text
VALID TIME != OBSERVATION / KNOWLEDGE TIME != RECORD TIME != WRITE ORDER
AGENT MEMORY ATLAS = EXTERNAL CONVERGENCE ONLY
```

Existing Native references:

- [`docs/FOUNDATIONAL_CONTRACT_SKELETON.md`](../FOUNDATIONAL_CONTRACT_SKELETON.md) — `NK-EVT-002` (observation time, record time, valid time and write order are not silently collapsed); `NK-CFL-003` (write order alone does not determine semantic correctness);
- [`docs/FOUNDATIONAL_INTENT.md`](../FOUNDATIONAL_INTENT.md) — "Temporal meaning" row (valid time, record time and write order should not collapse into one timestamp);
- [`docs/adr/0006-causal-links-are-relations.md`](../adr/0006-causal-links-are-relations.md) — temporal validity, system knowledge time and technical write order remain distinct;
- [`docs/contracts/NORMATIVE_CONTRACTS_V1.md`](../contracts/NORMATIVE_CONTRACTS_V1.md) — valid time, observation time and record time remain separate fields when applicable;
- A4/A5 semantic material ([`docs/A4_SEMANTIC_LAWS_AND_INVARIANTS.md`](../A4_SEMANTIC_LAWS_AND_INVARIANTS.md), [`docs/A5_IDENTITY_TIME_AND_CHANGE.md`](../A5_IDENTITY_TIME_AND_CHANGE.md)) where applicable.

## Source-fidelity note

Agent Memory Atlas's rejected-value mechanism is narrower than general semantic matching: a rejected value is keyed under a declared identity/normalization policy (for example scope + subject + predicate + normalized value).

```text
DECLARED NORMALIZED VALUE MATCH != ARBITRARY SEMANTIC PARAPHRASE MATCH
```

The source does not establish general semantic-equivalence blocking. Paraphrase matching, if ever considered, is an **OPEN POLICY / SEPARATE TEST QUESTION** and is not assumed here.

## Residual candidates

### Candidate A — rejected/corrected disposition vs new-record-ID reassertion (main narrow residual)

A later automated write may create a new record ID carrying the same value under a declared normalization/identity rule, bypassing a disposition attached only to the old record ID.

**Research question:** Can rejection/correction disposition be preserved across fresh re-extraction under a new record identity without requiring a specific tombstone mechanism?

- Semantic paraphrase equivalence is **NOT** assumed; the matching rule must be declared/preregistered by the owner.
- Legitimate independent re-observation under a policy that permits reactivation/new evidence must remain distinguishable from reassertion of the old disposition (compare Crystal profile §4).
- Owner split: Crystal / admission runtime = policy implementation; SVL = falsification; Native Kernel = semantic identity question only.
- Status: `NOT RUN · NOT PREREGISTERED · NO NEW EXPERIMENT ID · NOT ARCHITECTURE`.

**Crystal read-only inspection (2026-09-28, `velantrim-exocortex-crystal` main `726b85e`):** Crystal has exact normalized ingestion identity (`core/ingest_identity.py`: NFC, trim, whitespace collapse, casefold — explicitly "not semantic or near-duplicate matching"); `store_fact` preserves the persisted epistemic state on conflict (`core/memory.py`); the normalized compatibility index resolves only `Validated` targets (`core/normalized_ingest_index.py`); explicit caller-supplied fact IDs bypass the normalized index (`tests/test_dedup.py::test_explicit_custom_fact_id_does_not_use_normalized_legacy_index`); immune memory blocks by normalized pattern only for explicitly recorded threats (`core/immune.py`, `tests/test_immune.py`). No test was found that rejects/collapses/deprecates a value and then asserts that a fresh extraction producing a **different** record ID with a value matching under the declared normalization rule does not regain current applicability. Result: `OPEN TEST GAP` — not claimed solved, not claimed failing, no runtime change.

### Candidate B — correction survives regeneration (refinement only)

Anchored to existing Native concepts: derived views, lineage, staleness and correction/revision — in particular [A4-L23](../A4_SEMANTIC_LAWS_AND_INVARIANTS.md) ("Derived views do not rewrite history or become universal State"; profiles must disclose derivation inputs, method and staleness) and the open derived-state boundary question [A10-Q13](../A10_OPEN_QUESTIONS_AND_FALSIFICATION.md).

**Refinement question:** Given existing derived-state/staleness obligations, is an additional test needed to establish that correction survives regeneration of non-replay derived artifacts?

This is a test refinement, **not** a new invariant. Actual caches/indexes/summaries belong to their runtime owners; falsification belongs to SVL (Return Arc / E10).

## Routed out of Native Kernel semantic candidates

### Retrieval abstention — routing note

Retrieval abstention is a retrieval-owner / evaluation question. Existing Velantrim work includes Graphiti FM-16 Honest Empty (status `NOT_ESTABLISHED`) and Crystal / memory-evaluation profiles (Crystal profile §6; Native protocol §4, §12).

It is **not** a Native Kernel semantic candidate and no new state name is minted here; when no candidate clears scope, applicability or evidence constraints, the retrieval owner decides how an empty or abstaining result is represented.

### Negative retrieval assertion — evaluation method

```text
NEGATIVE RETRIEVAL ASSERTION = EVALUATION METHOD
METHOD != ARCHITECTURE
```

Route to: Native [Memory Evaluation Protocol §12](MEMORY_EVALUATION_PROTOCOL_V0.md#12-positive-obligations-and-negative-invariants); Crystal adversarial profile §6; Graphiti `docs/AGENT_MEMORY_EVALUATION_PROFILE.md` (§9–§10); SVL as a cross-cutting assertion form. Always pair with a positive control so an always-empty system cannot pass.

## Authority boundary

```text
EXTERNAL PATTERN != NATIVE KERNEL INVARIANT
DONOR CONVERGENCE != VALIDATION
RESEARCH QUESTION != IMPLEMENTATION AUTHORIZATION
```

Any promotion requires an owner-local uncovered failure, a bounded test, and the normal evidence/governance process.

## Current Native Kernel reconciliation status

```text
CURRENT RECONCILIATION: NO_NEW_INVARIANT
NO_RUNTIME_CHANGE
NO_CANON_CHANGE
NO_IMPLEMENTATION_AUTHORIZATION
```
