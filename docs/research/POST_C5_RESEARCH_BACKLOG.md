# 🔬 Post-C5 research backlog

> **Status:** `RESEARCH / PROPOSED / NOT IMPLEMENTED / NO MATURITY PROMOTION`
> **Current runtime boundary:** `C4`
> **Current operational boundary:** `C5_BOUNDED_REHEARSAL`
> **Current NK-EPI support:** `0 / 8`

This document keeps useful post-audit ideas in the research surface. Nothing here changes Architecture Canon, runtime behavior, assertion support, production authorization or ecosystem authority.

## R1 — First executable epistemic vertical slice

Candidate: `NK-EPI-004 — unknown or unanswered is not silently treated as false`.

Research questions:

- what normative state vocabulary is sufficient;
- how `UNKNOWN`, `CONFLICTED`, `REJECTED`, `RESTRICTED` and admitted state remain distinct;
- how provenance gaps survive append, replay, projection rebuild and Receipt generation;
- how PostgreSQL and SQLite expose the same bounded semantics;
- what positive, negative and invalid fixtures are required.

Promotion requires a separate accepted decision, implementation PR, cross-profile evidence and assertion-map update. Existing fixture descriptions alone are not runtime support.

## R2 — Epistemic admission boundary

Research the explicit separation:

```text
Event accepted into history
≠
Claim admitted as knowledge
```

Candidate stages include structural validation, identity, provenance, authority, evidence evaluation and admission. Names such as `TruthGate`, `Guardian` or model filters remain profile terms, not Canon.

## R3 — Evidence-bearing erasure state machine

Research a bounded chain such as:

```text
ERASURE_REQUESTED
→ ERASURE_AUTHORIZED
→ ERASURE_IN_PROGRESS
→ PHYSICALLY_ERASED_BOUNDED
→ ERASURE_VERIFIED
```

The existing accepted deletion contract remains authoritative. This research must not rename current states or claim physical execution without a separate contract migration, location scope, executor identity and evidence.

## R4 — Independent cross-language reader/profile

A small independent implementation may later cover canonical JSON, NFC, identity hashes, event/Receipt decoding and golden/invalid vectors. Rust, Go, Java, TypeScript or another runtime may be evaluated as replaceable profiles. No language becomes Canon.

## R5 — Signed Receipts

Signatures may attest that a key signed exact bytes. They do not prove truth, completeness, deletion, safety or production readiness. Research must first define canonical Receipt bytes, signer authority, rotation, revocation, delegation and threat model.

## R6 — License and contribution governance

Issue #18 remains independent. Research must decide publication goals, commercial use, patent grant, permissive versus copyleft terms, documentation licensing, DCO/CLA and AI-assisted contribution provenance before selecting a license.

## R7 — Controlled ecosystem adapters

Titan, Crystal and Mentaury may later use mock, read-only or shadow adapters. Automatic authority, shared Canon, truth promotion and production wiring remain prohibited without separate evidence and operator approval.

## Promotion discipline

```text
research note
→ explicit contract
→ reproducible code and tests
→ failure cases
→ evidence record
→ decision/ADR
→ operator approval
→ bounded implementation
```
