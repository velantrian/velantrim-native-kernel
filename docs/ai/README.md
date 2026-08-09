# 🤖 Native Kernel AI Context Pack

This directory is the mandatory continuity surface for AI agents, auditors and maintainers.

## Required reading order

1. [`../../README.md`](../../README.md)
2. [`../../STATUS.md`](../../STATUS.md)
3. [`../../project-state.json`](../../project-state.json)
4. [`../../AGENTS.md`](../../AGENTS.md)
5. [`CURRENT_STATE.md`](CURRENT_STATE.md)
6. [`KNOWN_RISKS.md`](KNOWN_RISKS.md)
7. [`../../ROADMAP.md`](../../ROADMAP.md)
8. [`ISSUE_RECONCILIATION.md`](ISSUE_RECONCILIATION.md)
9. [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)
10. affected Canon, contracts and ADRs
11. affected source, tests and workflows
12. relevant implementation/evidence records
13. [`DOCUMENTATION_SYNC_PROTOCOL.md`](DOCUMENTATION_SYNC_PROTOCOL.md)
14. current GitHub and Notion state

Do not read every historical handoff before identifying the current task. Do not begin with random code search.

## Current boundary

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false
assertion map:              45 / 10 / 17 / 0
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

## Truth reconciliation

```text
PR #80 — machine-readable truth:          COMPLETE
PR #81 — human-readable truth:            COMPLETE
PR #82 — Issues/Notion repository record: COMPLETE
PR #83 — publication checkpoint:          MERGED / PENDING_OPERATOR PRESERVED
PR #86 — Notion synchronized descendant:  MERGED / VALIDATED / READ BACK
Issues #14–#17:                           RECONCILED / OPEN
```

Publication checkpoint: `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c` from PR #83. Manifest source and Notion synchronized descendant: `70acd0da61fee19131947aa56125833adb156ced` from PR #86. PR #86 exact head was `c3b8695bf3d7207ac4c6b19dcb5e9e2bda92f764`; all five exact-head and all five post-merge workflows passed with 18 successful jobs at each checkpoint and no failed, cancelled or skipped jobs.

The later Notion checkpoint does not rewrite or replace the publication checkpoint. A committed state file may reference only an already merged, synchronized and read-back ancestor; it never predicts its own future merge SHA.

## Truth surfaces

```text
CURRENT STATE
  ../../STATUS.md
  ../../project-state.json
  CURRENT_STATE.md

ACTIVE ROADMAP
  ../../ROADMAP.md

ACTIVE RISKS
  KNOWN_RISKS.md

RECONCILIATION RECORDS
  ISSUE_RECONCILIATION.md
  NOTION_HANDOFF.md

HISTORICAL RECORD
  implementation records
  accepted ADRs
  immutable evidence manifests
  Git history

PROPOSAL
  proposed ADRs
  research backlog
```

Historical chronology and proposals are not authoritative current state.

## Track boundary

```text
H historical recovery: BLOCKED / independent
C clean implementation: ACTIVE / PARTIAL
R long-horizon research: PROPOSED / bounded / no automatic promotion
```

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
research proposal ≠ accepted contract ≠ runtime
C2 ≠ C3 ≠ C4 ≠ C5
C5 bounded rehearsal ≠ production readiness
C5 operational validation ≠ assertion promotion
logical backup ≠ physical disaster recovery
```

## Checkpoint discipline

`project-state.json` uses `nk-project-state/2` and records separate runtime, integrity, evidence, publication and Notion synchronization checkpoints.

Live HEAD must be resolved through Git or GitHub. A descendant commit does not silently broaden an earlier evidence or publication checkpoint. A later post-merge Notion write can be newer than the repository-committed synchronization checkpoint until a subsequent non-self-referential manifest records the already completed sync.

## Current authorized sequence

```text
explicit license/publication operator selection
→ explicit ADR-0024 operator selection
→ NK-SAM and named equivalence profiles
→ Event/history commitment
→ only then reducer-v2 runtime
```

Current decision state:

```text
license/publication: PENDING_OPERATOR / selected_option: null
ADR-0024: PROPOSED / PENDING_OPERATOR / selected_option: null
reducer v1: IMMUTABLE
reducer-v2 runtime: NOT AUTHORIZED
```

Executable NK-EPI, Temporal, full Admission, operational deletion, full independent implementation and ecosystem integration remain outside the current slice.

## Evidence route

```text
C5 plan and ADR-0021
→ implementation and final checkpoints
→ repository-resident exact ZIPs
→ strict bundle manifests and verifier
→ ADR-0023 safe-version additive identity
```

Evidence roots:

```text
../../evidence/c5/2026-08-07/manifest.json
../../evidence/c5/2026-08-08-adr0023/manifest.json
```

These archives are version-bound. They are not production, compliance, independent-custody, complete-authenticity or physical-deletion proof.

## Source-of-truth order

1. exact code, tests, contracts and retained artifact bytes;
2. exact-SHA CI jobs/logs and GitHub live refs, issues and reviews;
3. `project-state.json`, `STATUS.md` and `CURRENT_STATE.md`;
4. accepted ADRs and versioned contracts;
5. implementation and reconciliation records, work log and PR/issue history;
6. Notion and historical chats.

## Automated guards

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_reconciliation.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
```

## Historical records

Read only when relevant:

- [`P4_IMPLEMENTATION_RECORD.md`](P4_IMPLEMENTATION_RECORD.md)
- [`P5_IMPLEMENTATION_RECORD.md`](P5_IMPLEMENTATION_RECORD.md)
- [`C4_IMPLEMENTATION_RECORD.md`](C4_IMPLEMENTATION_RECORD.md)
- [`C5_IMPLEMENTATION_RECORD.md`](C5_IMPLEMENTATION_RECORD.md)
- [`WORK_LOG.md`](WORK_LOG.md)
- [`AUDIT_PLAYBOOK.md`](AUDIT_PLAYBOOK.md)

Historical records preserve provenance; they do not override current state.
