# ADR-0004: Use rebuild-from-authoritative-history as the first conformance experiment

- **Decision status:** `PROPOSED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Date:** `2026-07-23`
- **Deciders:** `@velantrian`
- **Track:** `Evaluation`
- **Related:** `docs/FOUNDATIONAL_INTENT.md`, `docs/CONFORMANCE_MODEL.md`, `Issue #1`
- **Tags:** `replay, reconstruction, conformance, projections, receipt`

## Context 🧭

Native Kernel claims that authoritative history and semantic contracts should survive replacement or removal of disposable indexes and projections.

A large Titan integration or autonomous-agent experiment would introduce too many variables for the first proof. The initial experiment should test the smallest central architectural claim.

## Decision drivers 🎯

- test the architecture rather than the sophistication of one adapter;
- produce a result that is reproducible and easy to explain;
- preserve separation between Canon history and disposable projections;
- define semantic equivalence explicitly;
- avoid expanding Issue #1 with redesign.

## Considered options 🧪

### Option A — Start with a Titan Offline Shadow comparison

**Advantages**

- uses realistic workloads;
- compares richer behaviour.

**Disadvantages**

- introduces Titan-specific semantics;
- harder to isolate reconstruction defects;
- premature before public import and read-path stabilization.

### Option B — Start with charge-formula evaluation

**Advantages**

- tests an important experimental ranking mechanism.

**Disadvantages**

- charge is not the foundational architecture claim;
- results depend heavily on workload and current policy;
- does not prove history/projection separation.

### Option C — Rebuild semantic state after deleting disposable projections

**Advantages**

- directly tests the core history/reduction/projection boundary;
- small and deterministic;
- can later be repeated across storage profiles;
- produces clear failure cases and Receipts.

**Disadvantages**

- does not prove retrieval quality, scalability, or production safety;
- requires a documented semantic-equivalence rule.

## Decision ✅

**We propose to:**

Use the following experiment as the first architecture-conformance reference:

```text
1. Create a bounded set of Claims and Events.
2. Derive semantic state and disposable projections.
3. Record the expected semantic result.
4. Delete every disposable projection and index.
5. Rebuild solely from the declared authoritative history.
6. Compare the result under a documented equivalence rule.
7. Produce a Receipt describing source range, profile version, result, and limitations.
```

**We will not:**

- treat the experiment as proof of production readiness;
- require Titan or Crystal integration;
- make checkpointing part of the test unless separately scoped;
- require bit equality when semantic equality is the declared contract;
- insert this experiment into the exact Issue #1 import snapshot.

### One-line rationale

> To test the smallest central Native Kernel claim with minimal external variables, we propose rebuilding semantic state from authoritative history after removing disposable projections, accepting that this proves reconstruction only—not retrieval quality, security, or production readiness.

## Consequences 📌

### Positive

- creates an understandable first proof;
- establishes a reusable conformance fixture;
- exposes hidden projection authority;
- prepares later cross-profile testing.

### Negative / accepted trade-offs

- semantic equivalence must be carefully specified;
- a passing test does not validate broader cognition or retrieval;
- current repository evidence remains pending until runnable code is imported.

## Invariants 🔒

1. Deleting disposable projections must not delete authoritative history.
2. Rebuild must not silently omit unresolved conflicts.
3. Reconstructed identity, lineage, temporal state, and epistemic status must satisfy the declared equivalence rule.
4. The Receipt must state what was and was not demonstrated.
5. Failure must remain visible rather than being repaired by editing projections.

## Validation and evidence 🧪

| Evidence | Artifact / command | Current result | Required for next level |
|---|---|---|---|
| Documentation | this ADR + Conformance Model | proposed | operator acceptance |
| Repository test | future replay/rebuild command | not available | Issue #1 and scoped implementation |
| Cross-profile replay | future second adapter | not available | C3 conformance research |
| Offline Shadow | later Titan workload | not available | separate roadmap gate |

## Rollback / supersession

This ADR may be rejected or superseded if the imported prototype demonstrates that another smaller experiment tests the history/reduction boundary more accurately. The reasoning and evidence must remain visible.
