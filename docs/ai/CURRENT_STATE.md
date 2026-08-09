# 📍 Native Kernel Current State

```yaml
document_role: CURRENT_STATE
status_as_of: 2026-08-09
authoritative_machine_source: ../../project-state.json
machine_protocol: nk-project-state/2
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
live_head_source: GitHub API or checked-out Git ref
machine_truth_reconciliation_merge: d9eee591de308a689ace940c2efe58c9e8a137f2
runtime_checkpoint: 675aa4b398a2fc0181dc71d38904a2d33a09f5f8
runtime_integrity_checkpoint: a1cdc6d8f36d67f40f065641809bc6da463c10a4
evidence_producing_checkpoint: 296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
notion_synchronized_through: 626f34e6328b455258f2dd5fcf2145ec4db64a60
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

## Checkpoint model

The current machine protocol does not attempt to store the SHA of its own commit.

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
| Issue #18 — license/publication terms | `OPEN` | External collaboration and package publication remain blocked by an unresolved rights regime. |
| Issue #74 / ADR-0024 — reducer referential semantics | `PROPOSED / APPROVAL PENDING` | Reducer v1 remains immutable; reducer-v2 runtime work is not authorized yet. |

No AI agent may select the license or accept ADR-0024 on behalf of the operator.

## Next authorized sequence

```text
1. complete human-readable truth reconciliation
2. reconcile Issues #14–#17 and Notion current-state pages
3. prepare license options for operator decision
4. prepare ADR-0024 final decision options
5. define NK-SAM and named equivalence profiles
6. define Event/history commitment boundaries
7. only then begin reducer-v2 runtime work
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
- production threat model, operations and authorization are absent;
- Notion remains synchronized only through the recorded publication checkpoint until the dedicated reconciliation step completes.

## Machine-readable state

```text
project-state.json
contracts/project-state-v2.schema.json
contracts/registry.json
tools/ai_context/validate_project_state.py
```

`project-state.json` is authoritative for committed repository status metadata. GitHub remains authoritative for live refs, issues, PRs and Actions. Exact source, tests and evidence artifacts remain authoritative for their own technical claims.

## Historical records

- [`C5_IMPLEMENTATION_RECORD.md`](C5_IMPLEMENTATION_RECORD.md)
- [`../adr/0023-harden-sqlite-wal-and-event-integrity.md`](../adr/0023-harden-sqlite-wal-and-event-integrity.md)
- [`../../evidence/c5/README.md`](../../evidence/c5/README.md)
- [previous current-state snapshot at `626f34e…`](https://github.com/velantrian/velantrim-native-kernel/blob/626f34e6328b455258f2dd5fcf2145ec4db64a60/docs/ai/CURRENT_STATE.md)

Historical records are version-bound evidence and chronology, not current-state authority.