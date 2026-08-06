# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-06  
**Last verified public `main`:** `1e721aeb5b116694a0dbb417c377aa9f92b6f8e5`  
**Published proposal:** PR #41 / RFC-0002 / Issue #40

Accepted contracts, passing tooling and a detailed profile plan do not close runtime, security, privacy, licensing or portability risks.

## P0 — Authentic source recovery remains unresolved

**State:** `OPEN`

The reported `v0.1.2.1` source and original 44-test suite are absent. Connected-source search found no authentic candidate; operator-controlled devices and archives remain outside connector evidence.

Required proof: authentic bytes, lineage, hashes, original tests and explicit Issue #1 operator gate.

## P0 — Clean profile may be mistaken for recovered history

**State:** `OPEN`, narrowed by published RFC-0002 guardrails

RFC-0002 uses `clean/postgresql-reference/0.1` and forbids historical lineage, use of the `v0.1.2.1` identity, replacement of the original 44-test evidence and closure of Issue #1 through clean implementation work.

The planning validator rejects a non-null historical lineage and any permission to claim recovery.

Required control: every future runtime package, migration, test report and release repeats the clean-lineage boundary.

## P0 — Planning manifest may be mistaken for runtime support

**State:** `OPEN`, narrowed by machine-readable enforcement

```text
PLANNED
≠ SUPPORTED
≠ LOCALLY_TESTED runtime
≠ C2
```

All 72 assertion rows currently state `runtime_support: UNSUPPORTED` and `evidence_state: NONE`. The validator rejects missing/duplicate assertions, false support claims, historical lineage and silent `NK-EPI` promotion.

## P0 — Support tooling may be mistaken for Kernel runtime

**State:** `OPEN`

```text
accepted assertion
≠ assertion implemented by a Kernel profile
fixture reader supported
≠ durable event store
≠ replay/deletion implementation
≠ C2/C3 Kernel conformance
```

Required control: built-in reports retain `kernel_runtime_conformance: UNSUPPORTED` until a real profile demonstrates scoped behaviour.

## P0 — Published RFC may be mistaken for runtime authorization

**State:** `OPEN`

PR #41 merged RFC-0002 as `PROPOSED / DOCUMENTED_ONLY`. Operator approval remains pending and implementation is not started.

```text
merged RFC proposal
≠ accepted profile plan
≠ runtime GO
≠ implementation evidence
```

## P1 — GitHub Actions execution remains unrecorded

**State:** `OPEN`, validation surface expanded

The conformance workflow includes both fixture and profile-manifest tests/reports on Python 3.11/3.12. No run was created for PR #41 or merge `1e721aeb…`.

Required proof: exact workflow run ID, head SHA, jobs, conclusions and artifacts for both reports.

## P1 — Profile implementation language and dependency policy undecided

**State:** `OPEN`

RFC-0002 deliberately does not select a permanent language, package layout, PostgreSQL driver or migration framework.

Issue #18 leaves repository publication/contribution licensing unresolved. Dependency selection, package publication and outside contributions must not begin under assumed license permissions.

Required decisions before runtime: language/runtime, dependency/package policy, PostgreSQL matrix, driver/migrations, license compatibility and contribution terms.

## P1 — Single-writer boundary may be weakened by PostgreSQL concurrency

**State:** `OPEN`

PostgreSQL concurrency is not a multi-writer safety proof. RFC-0002 requires one authoritative writer per Kernel instance.

Required proof: explicit writer lease/epoch, mismatch rejection, transaction/fault tests and incident fencing.

## P1 — SQL schema may become accidental Canon

**State:** `OPEN`

Tables, columns, surrogate keys, indexes and SQL transaction syntax remain profile details. Semantic IDs and accepted contracts must survive schema/backend replacement.

Required proof: neutral export, replay, migration Receipt and future independent SQLite comparison.

## P1 — Deletion planning is insufficient for sensitive data

**State:** `OPEN`

RFC-0002 inventories payloads, commands, projections, evidence, logs, backups, replicas and migrations but implements none of the deletion mechanisms.

Required proof: profile location matrix, key hierarchy if used, retry/partial-failure tests, backup/restore evidence and security/legal review.

## P1 — GitHub ↔ Notion drift

**State:** `OPEN`, narrowed by dedicated RFC page

RFC status, PR/head/merge SHA, operator decision, runtime GO and evidence must remain synchronized. GitHub remains authoritative.

## P1 — Accepted contracts remain unimplemented

**State:** `OPEN`

ADR-0011–0014 define accepted identity, event/replay, deletion and fixture contracts. RFC-0002 maps them, but no profile implements them.

## P1 — Registry/profile plan can hide proposed NK-EPI status

**State:** `OPEN`

`NK-EPI-001…008` remains proposed. The profile manifest defers all eight assertions with no implementation phase.

Required control: planning or fixture presence must not be described as architecture acceptance or runtime enforcement.

## P1 — Storage neutrality unproven

**State:** `OPEN`

A PostgreSQL plan is not storage-neutrality evidence. C3 requires an independently developed second profile and declared equivalence.

## P1 — Cross-project authority leakage

**State:** `OPEN`

RFC-0002 does not authorize Titan, Mentaury or Crystal integration, shared storage, identity or inherited authority.

## P1 — Future-substrate claims can become hype

**State:** `OPEN`

Neutrality remains a versioned architecture target, not demonstrated portability or superiority.

## Update rule

Record state, exact evidence/SHA, remaining uncertainty, owner and next action. Never close a risk through prose, merge, operator approval alone, planning coverage or support-tool success.
