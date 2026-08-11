# 🔒 BPV-1 Execution Admission — Candidate Package

**[English](./BPV1_EXECUTION_ADMISSION.md) · [Русский](./BPV1_EXECUTION_ADMISSION.ru.md)**

> **Protocol:** `nk-bpv1-execution-admission/1`  
> **Admission ID:** `BPV1-001-execution-admission-v1`  
> **Scenario:** `BPV1-001-cross-lineage-bounded-accountability-v1`  
> **State:** `CANDIDATE_PACKAGE / EXECUTION_NOT_ADMITTED`

This package translates the already-authoritative preregistration into an executable **oracle boundary before any Rust subject implementation exists**. It does not execute BPV-1 and does not thaw product runtime.

## Frozen plan binding

```text
plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
plan SHA-256: 15c830ed195762d571cf675900303dfbfb29bf01a5cde2aac814388319585a91
plan path: docs/research/BPV1_PREREGISTRATION.json
```

The admission validator must recompute the exact SHA-256 and verify that the authoritative plan merge is an ancestor. A semantically similar edited plan is not the same admitted plan.

## External oracle package

```text
fixture protocol: nk-bpv1-fixtures/1
observation protocol: nk-bpv1-observations/1
evaluation protocol: nk-bpv1-evaluation/1
oracle authority: BPV1-ORACLE-001
fixture spec: experiments/bpv1/BPV1-001/admission/fixtures.json
evaluator: tools/bpv1/evaluate.py
```

The fixture file contains exactly the 12 preregistered fixture families. The evaluator consumes implementation-neutral observations; it does not inspect Rust structs, current Python domain classes, SQL schemas, Event envelopes, reducers, Receipts, or current ID prefixes.

A mandatory predicate failure yields `REFUTED`; a missing mandatory observable yields `INDETERMINATE`; no observed fixtures yields `NOT_TESTED`; complete mandatory success yields `SUPPORTED_FOR_SCOPE`. Final A10 hypothesis classification remains a later stage and is not automatic Canon promotion.

## Evaluator self-test before subject

`tests/test_bpv1_execution_admission.py` must demonstrate, before subject source exists:

- a synthetic conforming observation bundle → `SUPPORTED_FOR_SCOPE`;
- a semantic hard failure → `REFUTED`;
- a missing mandatory observable → `INDETERMINATE`;
- no fixture observations → `NOT_TESTED`;
- a wrong plan digest is rejected;
- exceeding bounded-state limits is `REFUTED`;
- reuse of current Native Kernel/Event/reducer/Receipt/SQL semantics as the subject boundary is `REFUTED` or rejected by scope validation.

These are oracle self-tests, not BPV-1 evidence.

## Rust toolchain and source boundary

```text
Rust channel: 1.97.1
language role: EXPERIMENTAL_INSTRUMENT_NOT_CANON
subject root: experiments/bpv1/BPV1-001/subject
independent team: NOT_ESTABLISHED
independent custody: NOT_ESTABLISHED
independent computation model: NOT_ESTABLISHED / CONVENTIONAL_DIGITAL
```

`experiments/bpv1/BPV1-001/rust-toolchain.toml` pins the toolchain. The subject root must be absent from this admission package. Future subject work is isolated under that root and may not register a product runtime/profile or modify `native_kernel/**`, `contracts/**`, `profiles/**`, current C5 evidence, migrations, or ADR semantics.

## Static no-product-integration audit

`tools/bpv1/audit_scope.py` audits the admission diff from current pre-admission main `20484a151bc7011509579353c2cf78845e3c33f9`. Admission packaging may touch only the declared admission docs/oracle/tooling/tests/workflow paths. Subject source is forbidden in this package.

## Two-phase admission rule

This package cannot admit itself.

```text
#112 package merge
= fixtures/oracle/toolchain/source boundary READY
≠ execution admitted

separate post-merge state checkpoint
= binds #112 merge + exact/post-merge CI + scope audit
= may admit BPV1-001 subject implementation/execution only
≠ product runtime thaw
```

Until that separate checkpoint is authoritative:

```text
BPV-1 execution: BLOCKED_PENDING_EXECUTION_ADMISSION
runtime expansion: FROZEN
product runtime thaw: NO
production: false
```

## Non-authorization

Neither this candidate package nor its future bounded admission decides Issue #18, accepts Issue #74/ADR-0024, authorizes reducer-v2, creates new Event verbs, enables NK-EPI runtime, admits Track H sources, promotes A1–A10 to Final Canon, authorizes production, or proves universal substrate independence.
