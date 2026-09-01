# EITI-Derived Invariant Candidates

Status: **RESEARCH · SUBSTRATE-NEUTRAL CANDIDATES ONLY**  
Recorded: 2026-08-21

EITI contains concrete implementations of lexical association, ranking/salience, temporal decay/accessibility and local adaptive learning. Native Kernel must not import those algorithms as Canon merely because they work in one client. What may belong here are only durable semantic invariants exposed by testing those mechanisms.

## Candidate invariants

```text
association != evidence
retrieval relevance != evidence quality
salience != epistemic confidence
decay/accessibility != epistemic revision
repetition != independent corroboration
model output != Canon
proposal != authorization
integration != authority transfer
```

### Association

A frequently co-activated or strongly weighted relationship may describe retrieval utility or learned association. It does not by itself establish semantic relation, causality, evidence independence or truth.

### Accessibility / decay

A memory becoming harder to retrieve does not mean its evidence was retracted, contradicted or invalidated. Forgetting/decay is an accessibility policy unless an owning epistemic process separately changes status.

### Multiple numerical signals

Association strength, salience, freshness, novelty, retrieval relevance and epistemic confidence are distinct dimensions. Authority, provenance, evidence status and ownership are constraints/gates rather than interchangeable scalar weights.

**Research formulation:** truth must not collapse into a generic weight.

### Adaptive learning

An observation that improves retrieval or routing does not grant permission to mutate an authoritative target. The target owner retains admission authority.

## Promotion test

Before any statement moves from research into Native Kernel Canon, verify that it is:
1. technology- and project-neutral;
2. meaningful across multiple implementations, not EITI-specific terminology;
3. compatible with existing authority/evidence semantics;
4. falsifiable through counterexamples/conformance tests;
5. free of accidental runtime or ownership assumptions.

EITI remains an empirical motivation source, not Native Kernel implementation truth.
