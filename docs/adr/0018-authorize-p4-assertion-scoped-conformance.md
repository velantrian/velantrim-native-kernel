# ADR-0018: Authorize P4 assertion-scoped conformance and repository evidence

- **Decision status:** `ACCEPTED`
- **Evidence level:** `NOT_RECORDED` pending exact repository matrix
- **Implementation status:** `PARTIAL — P4 CODE UNDER REVIEW`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-07`
- **Decider:** `@velantrian`
- **Track:** `Implementation Profile / Conformance`
- **Related:** Issue #55, PR #56, RFC-0002, ADR-0014…0017

## Context

P1–P3 provide a bounded semantic core, PostgreSQL append/idempotency, persisted replay, disposable projections and operational Receipts. Their tests establish specific behavior, but the profile still lacks one complete assertion-scoped report connecting the 72 stable registry IDs to executable checks and explicit limitations.

The operator separately authorized P4 on 2026-08-07. This authorization is authority to implement and evaluate P4; it is not itself conformance evidence.

## Decision

Implement a PostgreSQL reference-profile adapter for `nk-evidence-report/1` that:

```text
registry 1.1.0
→ execute P1 semantic checks
→ execute P2 PostgreSQL append/fencing checks
→ execute P3 replay/projection/Receipt checks
→ emit every assertion ID exactly once
→ attach passed check IDs and limitations
→ validate the report independently
→ retain exact repository artifacts
```

Every registered assertion is emitted as exactly one of:

- `SUPPORTED` — the declared P4 check set directly reproduces the bounded assertion behavior;
- `PARTIAL` — a meaningful part is reproduced, but an explicit semantic or operational gap remains;
- `UNSUPPORTED` — no sufficient executable P4 support exists or the assertion remains proposed;
- `FAILED` — a claimed check was executed and failed.

Assertions may not be omitted or promoted through prose.

## Initial support mapping

The P4 implementation declares this conservative map:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

The count is a profile-specific implementation claim and is guarded by tests and manifest validation. It is not a change to the accepted contract registry.

All eight `NK-EPI-001…008` results remain `UNSUPPORTED` because their registry decision status is `PROPOSED`. Fixture presence and P4 execution do not accept ADR-0008.

## C1 and C2 boundary

Conformance levels remain assertion-scoped:

- local execution with recorded commands and failures may emit `C1 / LOCALLY_TESTED`;
- exact repository matrix execution with committed implementation, environment, CI traceability and retained artifacts may emit `C2 / REPOSITORY_REPRODUCED`;
- top-level `support_state` remains `PARTIAL` while any assertions are partial or unsupported.

`C2` applies only to assertion results marked `SUPPORTED` in the exact report. It does not convert `PARTIAL` or `UNSUPPORTED` results into support.

```text
P4 C2 for supported assertions
≠ complete profile support
≠ C3 cross-profile equivalence
≠ production validation
```

## Required traceability

Each `SUPPORTED` or `PARTIAL` result must:

1. reference at least one check ID;
2. reference only checks present in the same report;
3. reference only checks that passed;
4. contain non-empty limitations.

Every result, including `UNSUPPORTED`, must contain a limitation or reason. Adapter failure aborts report generation; it must not silently downgrade a failed required check into an unsupported result.

## Executable check boundary

P4 directly exercises bounded checks for:

- registry identity and decision statuses;
- canonical identity golden/invalid vectors;
- semantic roles, explicit scope and source-bound Claim identity;
- explicit deny-by-default authority;
- admission/deletion Receipt overclaim rejection;
- deterministic reduction, sequence and schema failures;
- semantic deletion/restriction transitions;
- PostgreSQL migration idempotency;
- writer lease/epoch fencing;
- append/idempotency/conflict behavior;
- transaction rollback and contiguous ordering;
- persisted replay and deterministic projection rebuild;
- stale-head rejection;
- stored canonical corruption detection.

These checks do not create missing conflict, restore, deletion-worker, cross-project or cross-profile behavior.

## Repository evidence gate

P4 repository C2 requires:

```text
Python 3.11 / PostgreSQL 16
Python 3.11 / PostgreSQL 18
Python 3.12 / PostgreSQL 16
Python 3.12 / PostgreSQL 18
```

Every matrix job must:

- generate a C2 evidence report with exact commit/run/environment metadata;
- pass strict report validation;
- retain the JSON report as an artifact;
- pass P1, P2 and P3 regressions;
- compile the implementation and tooling.

A workflow definition is not evidence. C2 may be recorded only after exact run IDs, head SHA, successful jobs and artifacts exist.

## Explicit non-goals

- no P5 SQLite profile;
- no C3 cross-profile equivalence;
- no physical or cryptographic deletion execution;
- no truth, signature, notarization or external-authenticity certification;
- no C4/C5 or production claim;
- no network API;
- no Titan, Mentaury or Crystal runtime wiring;
- no `v0.1.2.1` recovery claim;
- no ADR-0008 or `NK-EPI` promotion;
- no package publication decision under Issue #18.

## Consequences

Positive:

- assertion support becomes machine-readable and reviewable;
- unsupported areas remain visible rather than implied away;
- exact checks and limitations can be audited per assertion;
- repository artifacts permit third-party reproduction of supported assertions.

Costs and risks:

- static assertion mappings can drift from implementation unless guarded;
- top-level C2 can be misread as complete support without the `PARTIAL` boundary;
- one PostgreSQL profile cannot establish storage neutrality or C3;
- operational and security properties remain outside current evidence.

## Next gate

P5 and C3 require a separate operator GO and a materially independent profile with declared equivalence and comparison evidence.
