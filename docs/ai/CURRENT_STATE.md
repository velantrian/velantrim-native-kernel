# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-06  
**Last verified public `main`:** `1e721aeb5b116694a0dbb417c377aa9f92b6f8e5`  
**Latest proposal publication:** PR #41 / RFC-0002 — clean PostgreSQL reference profile planning  
**Repository status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`  
**Primary historical gate:** Issue #1 / authentic source recovery

> Re-check the actual branch, PR and final merge SHA before relying on this checkpoint.

```text
ACCEPTED CONTRACT ≠ IMPLEMENTED PROFILE
MERGED RFC PROPOSAL ≠ OPERATOR ACCEPTANCE
PROFILE PLAN ≠ RUNTIME GO
PLANNED ASSERTION ≠ SUPPORTED ASSERTION
LOCALLY_TESTED TOOLING ≠ REPOSITORY-REPRODUCED KERNEL
C2 ≠ C3
```

## Accepted exact contracts

```text
ADR-0011 / nk-id/1.0:       ACCEPTED / APPROVED
ADR-0012 / nk-event/1.0:    ACCEPTED / APPROVED
ADR-0013 / nk-deletion/1.0: ACCEPTED / APPROVED
ADR-0014 / nk-fixtures/1.0: ACCEPTED / APPROVED
```

Acceptance publication:

```text
PR #38 merge: ff88809fe7d7c79033a150140d20618e04aa1f9d
PR #39 merge: 350734c8ce8d8cbc742def7df9f3d5044a5953ab
Registry:     nk-contract-registry/1.1.0
```

`NK-EPI-001…008` and ADR-0008 remain proposed.

## RFC-0002 publication

```text
PR:                    #41
Issue:                 #40
Final PR head:         ab0e80b0833e96ef98ef4feec9e92b4153176083
Squash merge:          1e721aeb5b116694a0dbb417c377aa9f92b6f8e5
Changed files:         12
Profile ID:            native-kernel/postgresql-reference
Planning version:      nk-pg-profile/0.1-proposed
Evidence lineage:      clean/postgresql-reference/0.1
RFC status:            PROPOSED / DOCUMENTED_ONLY
Operator approval:     PENDING
Implementation:        NOT_STARTED
Kernel runtime:        ABSENT / UNSUPPORTED
```

Review record:

```text
Branch behind base:        0
Unresolved review threads: 0
Submitted reviews:         0
Actionable findings:       0
Codex review:              unavailable due external usage limit
```

RFC-0002 defines a future profile boundary:

```text
semantic core
→ authority port
→ append service
→ PostgreSQL authoritative-history adapter
→ reducer/upcaster registry
→ disposable projections
→ Receipt/evidence emitter
→ conformance adapter
```

It specifies one authoritative writer, transaction/idempotency behaviour, profile-local SQL boundaries, replay/rebuild, deletion inventory, migration, fault tests and C0→C5 gates. It does not select a permanent programming language, PostgreSQL major, SQL schema, driver, migration framework or writer-lease mechanism.

## Planning manifest

`profiles/postgresql-reference-v0/profile-manifest.json` maps all 72 registry assertions:

```text
64 accepted-family assertions: PLANNED
8 NK-EPI assertions:           DEFERRED_PROPOSED_FAMILY
runtime support:               72 × UNSUPPORTED
implementation evidence:       NONE
historical lineage:            null
Issue #1 relationship:         INDEPENDENT
```

Local planning-tool evidence:

```text
Profile-manifest tests: 5 PASS
Missing assertion:      rejected
Duplicate assertion:    rejected
False runtime support:  rejected
Historical lineage:     rejected
```

This validates the manifest guard, not a Kernel implementation.

## Existing conformance tooling evidence

Recorded package evidence remains:

- eight focused conformance-fixture tests pass locally;
- 72 unique registry assertions;
- identity, event, idempotency, deletion and epistemic fixture coverage;
- Kernel runtime conformance remains `UNSUPPORTED`.

## Workflow status

The conformance workflow now validates accepted fixtures and the proposed profile manifest on Python 3.11/3.12 and emits two machine-readable reports.

No run was created for PR #41 or merge `1e721aeb…`.

```text
workflow definition:            ACTIVE / MANUALLY DISPATCHABLE
repository run:                 NOT RECORDED
repository-reproduced evidence: NOT ESTABLISHED
```

This is not a PASS and not a test failure.

## Issue #1 separation

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
≠ declaration that historical source is globally lost
```

Issue #1 remains active and independent. Runtime implementation of the clean profile requires a separate operator GO.

## Runtime and ecosystem boundary

No PostgreSQL adapter, reducer, projection, deletion mechanism or Kernel package exists. No Titan, Mentaury or Crystal integration is authorized.

## Remaining decisions before runtime

1. operator acceptance, revision or rejection of RFC-0002/profile lineage;
2. separate runtime GO before P1;
3. language and package layout;
4. PostgreSQL/driver/migration version matrix;
5. writer lease/epoch mechanism;
6. neutral export encoding and initial reducer/projection set;
7. minimum deletion scope;
8. Issue #18 licensing/dependency/contribution terms;
9. whether clean-profile runtime may begin while Issue #1 remains active.

## Next gates

1. Merge the final PR #41 checkpoint and synchronize exact main to Notion.
2. Obtain explicit operator decision on RFC-0002.
3. Keep runtime implementation blocked until a separate GO.
4. Execute exact repository workflow evidence when available.
