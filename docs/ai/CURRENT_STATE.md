# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-06  
**Last verified public `main`:** `350734c8ce8d8cbc742def7df9f3d5044a5953ab`  
**Accepted exact-contract checkpoint:** PR #38 + PR #39  
**Active proposal:** Draft PR #41 / RFC-0002 — clean PostgreSQL reference profile planning  
**Repository status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`  
**Primary historical gate:** Issue #1 / authentic source recovery

> Re-check the actual branch, PR and final merge SHA before relying on this checkpoint.

```text
ACCEPTED ≠ IMPLEMENTED
PROPOSED PROFILE ≠ RUNTIME GO
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

## Active RFC-0002 proposal

```text
PR:                    #41
Issue:                 #40
Branch:                agent/postgresql-reference-profile-rfc
Head at PR open:       0c05f38dfc4f760a05d3deb0d15a7dd281c3065f
Profile ID:            native-kernel/postgresql-reference
Planning version:      nk-pg-profile/0.1-proposed
Evidence lineage:      clean/postgresql-reference/0.1
RFC status:            PROPOSED / DOCUMENTED_ONLY
Operator approval:     PENDING
Implementation:        NOT_STARTED
Kernel runtime:        ABSENT / UNSUPPORTED
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

It specifies one authoritative writer, transaction/idempotency behaviour, profile-local SQL boundaries, replay/rebuild, deletion inventory, migration, fault tests and C0→C3 gates. It does not select a permanent programming language, PostgreSQL major, schema, or writer-lease mechanism.

## Proposed planning manifest

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

## Existing fixture tooling evidence

Recorded package evidence remains:

- eight focused conformance-fixture tests pass locally;
- 72 unique registry assertions;
- identity, event, idempotency, deletion and epistemic fixture coverage;
- Kernel runtime conformance remains `UNSUPPORTED`.

## Workflow status

The conformance workflow is expanded in PR #41 to validate:

- accepted contract fixtures;
- proposed profile-manifest integrity;
- Python 3.11/3.12;
- machine-readable conformance and planning reports.

No exact repository run is claimed before one exists.

## Issue #1 separation

```text
clean/postgresql-reference/0.1
≠ recovered v0.1.2.1
≠ original 44-test evidence
≠ declaration that historical source is globally lost
```

Issue #1 remains active and independent. Runtime implementation of the clean profile requires a separate operator GO.

## Runtime and ecosystem boundary

No PostgreSQL adapter, reducer, projection, deletion mechanism or Kernel package exists in this proposal. No Titan, Mentaury or Crystal integration is authorized.

## Next gates

1. Review and merge PR #41 as `PROPOSED`, not accepted runtime work.
2. Synchronize the RFC rationale and exact SHA to Notion.
3. Obtain explicit operator acceptance of RFC-0002 and clean lineage.
4. Obtain a separate GO before P1 semantic-core code.
5. Manually execute repository workflow evidence when available.
