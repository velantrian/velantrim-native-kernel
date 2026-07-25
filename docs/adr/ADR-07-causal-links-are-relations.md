# ADR-07: Causal Semantics in Native Kernel

- **Status:** `Vision / Deferred (v0.1.4+)`
- **Date:** 2026-07-25
- **Deciders:** @velantrian
- **Related:** Issue #1, ADR-0005, ROADMAP.md

> **Causal is a relation, not a knowledge type.**

## Context

Native Kernel already has a topological edge `LINK` with `relation = "CAUSES"` (weight 0.7).  
However, there is no explicit causal model (evidence, mechanism, temporal lag).

Proposals to introduce `knowledge_type: CAUSAL_LINK` or to overload `parents` violate core invariants by mixing three separate axes:

- `knowledge_type` → decay policy (INVARIANT / VARIANT / PRACTICAL)
- `epistemic_state` → degree of belief
- `LINK.relation` → graph topology

## Decision

Causality will be implemented **only** through typed links and structural payload data, without mutating base node metadata.

| Layer | Implementation |
|-------|----------------|
| Base topology | `LINK.relation = "CAUSES"` (already exists) |
| Evidence base | Field `evidence: non-empty` required for canonical causal assertions |
| Complex semantics (optional) | Claim with `content_struct = { kind: "causal_assertion", cause_id, effect_id, polarity }` |
| Dynamics (PULL / Grip) | Directed causal hop — only after directed links (v0.1.4+) |

### Forbidden

- Changing `knowledge_type` to represent causality
- Overloading `parents` (reserved for lineage)
- Introducing `CausalContextBuilder` into the kernel before v0.1.4+

### Dependencies

- v0.1.2.2 — ReadIndex (`out_links` / `in_links`)
- v0.1.4 — directed links + bi-temporal

## Consequences

- Charge, PULL and Conflict Set continue to treat causal assertions as ordinary Claims
- The three axes (decay, belief, topology) remain clean
- Implementation is deferred until the core is stable

## Rationale

Introducing causality as a new knowledge type or through `parents` would collapse distinct semantic axes and create long-term maintenance debt.  
Keeping causality as a typed relation preserves architectural hygiene and allows a proper causal read-model to be added later without rewriting the foundation.

## Status

Accepted as vision. Will be revisited after v0.1.4.
