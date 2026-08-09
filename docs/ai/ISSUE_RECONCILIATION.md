# 📋 Foundational Issue Reconciliation Record

```yaml
document_role: ISSUE_RECONCILIATION
status_as_of: 2026-08-09
verified_repository_checkpoint: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
original_issue_reconciliation_checkpoint: 07549a0cd952b4e06b61ef24d21b2dcdbc9f861d
issue_state_source: GitHub API
result: RECONCILED / ALL ISSUES REMAIN OPEN
```

This record captures the bounded reconciliation of foundational Issues #14–#17 after machine-readable PR #80 and human-readable PR #81. PR #82 preserved the repository record, and the issue states/comments were directly rechecked during the PR #83 publication/Notion reconciliation. The remaining scope below is unchanged.

## Verification boundary

The original reconciliation workflows passed on `main@07549a0cd952b4e06b61ef24d21b2dcdbc9f861d`:

| Workflow | Run | Result |
|---|---:|---|
| Conformance fixture integrity | `31310849909` | `PASS` |
| AI context integrity | `31310849870` | `PASS` |
| P4 assertion conformance | `31310849875` | `PASS` |
| P5 SQLite and C3 equivalence | `31310849858` | `PASS` |
| C4 offline shadow evaluation | `31310849869` | `PASS` |
| C5 bounded operational rehearsal | `31310849864` | `PASS` |

PR #83 exact head `57c14742f705f96e33e929e7e206f14169d42fc0` and merge `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c` were also validated by AI-context, P4, P5/C3, C4 and C5 workflows. Issues #14–#17 remained open when directly rechecked. This follow-up does not broaden the original issue evidence boundary.

These runs verify their exact repository checkpoints and existing bounded profiles. They do not prove that every remaining item in the issues is implemented.

## Issue #14 — Canonical identity

**State:** `OPEN`  
**Reconciliation comment:** `5231286665`

### Already completed

- deterministic canonical JSON subset;
- Unicode NFC and UTF-8 reference encoding;
- explicit omission, float and null rules;
- domain-separated SHA-256 identifiers;
- distinct content, Claim, lineage and storage identities;
- Python implementation and golden/invalid vectors;
- bounded PostgreSQL/SQLite use and evidence.

### Remaining

- independent cross-language vectors;
- semantic identity separated from reference encoding;
- hash agility and collision response;
- alias and migration semantics;
- valid-time identity decision;
- declared equivalence across different physical encodings.

### Next gate

Define NK-SAM and named equivalence profiles before stronger neutrality claims.

## Issue #15 — Append, idempotency, ordering and replay

**State:** `OPEN`  
**Reconciliation comment:** `5231287409`

### Already completed

- single-writer baseline;
- lease and fencing epoch;
- global and stream sequence;
- transactional append;
- command digest and idempotency checks;
- stale-writer rejection;
- deterministic replay binding;
- PostgreSQL/SQLite rebuild paths;
- exact stored-Event checks and bounded hash chain.

### Remaining

- portable semantic Event/history commitment;
- committed-field classification;
- history-head, truncation, fork and rollback model;
- reducer/schema/identity/encoding substitution failures;
- independent implementation verification;
- any future multi-writer contract.

### Next gate

Accept an Event/history commitment contract before reducer-v2 histories.

## Issue #16 — Deletion and restriction

**State:** `OPEN`  
**Reconciliation comment:** `5231288045`

### Already completed

- explicit logical erase/restriction state machine;
- distinction from physical deletion and crypto-erasure;
- partial completion, retry and retention-hold states;
- bounded Receipts and global-erasure overclaim guards;
- restore-before-visibility contract requirement.

### Remaining

- execution and verification across payloads, projections, indexes, caches, exports, backups, replicas, logs, dumps and external providers;
- per-location retry, retention and restore policies;
- privacy versus immutable audit/evidence retention;
- bounded inability Receipts.

### Next gate

Create a location inventory and operational execution contract before physical or cryptographic deletion claims.

## Issue #17 — Conformance fixtures

**State:** `OPEN`  
**Reconciliation comment:** `5231288737`

### Already completed

- versioned registry, schemas and manifests;
- golden and invalid vectors;
- P1–P5 runners and reports;
- PostgreSQL/SQLite C2 and C3;
- C4 and C5 bounded evidence;
- repository-resident evidence verification;
- current assertion map `45 / 10 / 17 / 0`.

### Remaining

- executable NK-EPI fixtures;
- Temporal and richer conflict fixtures;
- reducer-v2 negative fixtures after ADR-0024 approval;
- Event/history mutation/fork/truncation/rollback fixtures;
- independent language runner;
- remaining unsupported and partial assertions;
- named equivalence and stable failure-location comparison.

### Next gate

Retain Issue #17 as the umbrella conformance backlog and version each new semantic slice independently.

## Shared non-goals

This reconciliation does not:

- close Issues #14–#17;
- promote any assertion;
- alter reducer v1;
- rewrite fixture outputs or evidence archives;
- prove full substrate neutrality;
- authorize production;
- implement NK-EPI, Temporal, Admission or operational deletion.

## Update rule

When one of these issues changes, record:

1. exact accepted contract or decision;
2. exact runtime and fixture version;
3. exact SHA and workflow runs;
4. evidence identity and proof boundary;
5. remaining scope;
6. whether the issue remains open or is ready for an explicit closure decision.
