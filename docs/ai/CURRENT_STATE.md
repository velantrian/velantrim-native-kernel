# 📍 Native Kernel Current State

```yaml
document_role: CURRENT_STATE
status_as_of: 2026-08-09
authoritative_machine_source: ../../project-state.json
machine_protocol: nk-project-state/2
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
live_head_source: GitHub API or checked-out Git ref
machine_truth_reconciliation_merge: d9eee591de308a689ace940c2efe58c9e8a137f2
human_truth_reconciliation_merge: 07549a0cd952b4e06b61ef24d21b2dcdbc9f861d
issues_notion_reconciliation_merge: cdf559a3a32decd538e4cab3dd7fb591fc6e9322
operator_decision_packages_merge: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
runtime_checkpoint: 675aa4b398a2fc0181dc71d38904a2d33a09f5f8
runtime_integrity_checkpoint: a1cdc6d8f36d67f40f065641809bc6da463c10a4
evidence_producing_checkpoint: 296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
notion_synchronized_through: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
```

> This page contains current repository truth only. Historical implementation and review chronology is linked under **Historical records** and remains available in Git history.

## Current boundary

```text
repository:                  RESEARCH
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

```text
C5 bounded rehearsal ≠ production readiness
C5 operations ≠ semantic assertion promotion
repository-resident evidence ≠ independent custody
logical ERASED ≠ physical deletion
public repository ≠ open-source license
```

## Reconciliation state

```text
0A machine-readable truth: COMPLETE / PR #80
0B human-readable truth:   COMPLETE / PR #81
0C Issues #14–#17:         RECONCILED / OPEN / PR #82 RECORD
0C Notion dashboard:       SYNCHRONIZED THROUGH PR #83
```

The Notion Hub routes current retrieval through Current State, Decision Ledger, Evidence Ledger, Active Risks, GitHub Sync Log and Historical Archive pages. Hub, Current State, Architecture, Roadmap, Decision Ledger, GitHub Sync Log and AI continuity were directly rechecked and reconciled through `main@10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c`.

Notion remains synchronized only through the recorded publication checkpoint. Any later descendant commit requires a new synchronization record before it can be represented as synchronized.

## Checkpoint model

The machine protocol does not attempt to store the SHA of its own commit.

```text
GitHub API / checked-out ref
        ↓ resolves live HEAD

project-state.json
        ↓ records verified checkpoint roles and expected relation to HEAD

runtime checkpoint
runtime-integrity checkpoint
evidence-producing checkpoint
publication checkpoint
Notion synchronization checkpoint
```

A descendant commit does not invalidate earlier evidence, but it also does not broaden that evidence.

## Three independent tracks

```text
H — Historical Recovery
  authentic v0.1.2.1 + original 44 tests
  BLOCKED / ACTIVE EVIDENCE-RECOVERY
  NOT_FOUND_IN_ACCESSIBLE_SOURCES
  does not block Track C

C — Clean Implementation
  P1–P5 + C4 + C5
  ACTIVE / PARTIAL

R — Long-Horizon Research
  PROPOSED / BOUNDED / NO AUTOMATIC PROMOTION
  no runtime or Canon status through prose
```

## Implemented and repository-evidenced boundary

```text
P1 semantic core:                    MERGED / REPOSITORY-TESTED
P2 PostgreSQL append:                MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay, projection and Receipts:  MERGED / REPOSITORY-INTEGRATION-TESTED
P4 PostgreSQL assertion profile:     MERGED / PARTIAL / C2
P5 SQLite and profile comparison:    MERGED / PARTIAL / C2 + C3
C4 offline shadow evaluation:        MERGED / PARTIAL
C5 bounded operational rehearsal:    MERGED / PARTIAL / SYNTHETIC
```

The current SQLite WAL floor is linked SQLite `3.51.3`. Historical SQLite `3.45.1` evidence remains immutable and version-bound.

## Current operator decisions

| Decision | State | Effect |
|---|---|---|
| Issue #18 — license/publication terms | `PENDING_OPERATOR / selected_option: null` | No license change; external contributions remain not accepted; package publication remains unauthorized. |
| Issue #74 / ADR-0024 — reducer referential semantics | `PROPOSED / PENDING_OPERATOR / selected_option: null` | Reducer v1 remains immutable; reducer-v2 runtime is not authorized. |

No AI agent may select the license or accept ADR-0024 on behalf of the operator.

## Verified PR #83 boundary

```text
exact head: 57c14742f705f96e33e929e7e206f14169d42fc0
merge:      10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
exact-head workflows: 5 PASS / 18 jobs success
post-merge workflows: 5 PASS / 18 jobs success
reviews: 0
unresolved review threads: 0
Codex: NOT AVAILABLE — quota notice, not review or approval
```

Passing CI proves the fail-closed decision packages and unchanged runtime/evidence guards. It does not choose a license, accept ADR-0024, prove reducer v2 or authorize production.

## Next authorized sequence

```text
1. obtain explicit license/publication operator selection
2. obtain explicit ADR-0024 operator selection
3. define NK-SAM and named equivalence profiles
4. define Event/history commitment boundaries
5. only then begin reducer-v2 runtime work
```

Out of scope until those gates are complete:

- executable NK-EPI;
- Temporal v0.1;
- full Admission lifecycle;
- operational deletion;
- full independent Rust/Go implementation;
- Titan, Crystal or Mentaury integration.

## Current known gaps

- reducer v1 does not enforce the proposed referential semantics for all LINK, UTILIZED, SUPERSEDED and ERASED cases;
- portable semantic Event commitment is not fully separated from operational/profile receipts;
- current C3 evidence compares PostgreSQL and SQLite profiles sharing a Python semantic lineage, not an independent language implementation;
- NK-EPI assertions have no executable support;
- temporal identity and interval semantics are incomplete;
- admission is not a complete replayable policy pipeline;
- physical/cryptographic deletion across actual locations is not established;
- production threat model, operations and authorization are absent.

## Machine-readable state

```text
project-state.json
contracts/project-state-v2.schema.json
contracts/registry.json
tools/ai_context/validate_project_state.py
```

`project-state.json` is authoritative for committed repository status metadata. GitHub remains authoritative for live refs, issues, PRs and Actions. Exact source, tests and evidence artifacts remain authoritative for their own technical claims.

## Reconciliation records

- [`ISSUE_RECONCILIATION.md`](ISSUE_RECONCILIATION.md)
- [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)

## Historical records

- [`C5_IMPLEMENTATION_RECORD.md`](C5_IMPLEMENTATION_RECORD.md)
- [`../adr/0023-harden-sqlite-wal-and-event-integrity.md`](../adr/0023-harden-sqlite-wal-and-event-integrity.md)
- [`../../evidence/c5/README.md`](../../evidence/c5/README.md)
- [previous current-state snapshot at `626f34e…`](https://github.com/velantrian/velantrim-native-kernel/blob/626f34e6328b455258f2dd5fcf2145ec4db64a60/docs/ai/CURRENT_STATE.md)

Historical records are version-bound evidence and chronology, not current-state authority.
