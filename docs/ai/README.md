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
8. affected Canon, contracts and ADRs
9. affected source, tests and workflows
10. relevant implementation/evidence records
11. [`DOCUMENTATION_SYNC_PROTOCOL.md`](DOCUMENTATION_SYNC_PROTOCOL.md)
12. current GitHub and Notion state

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

Live HEAD must be resolved through Git or GitHub. A descendant commit does not silently broaden an earlier evidence checkpoint.

## Current authorized sequence

```text
human-readable truth reconciliation
→ Issues #14–#17 and Notion reconciliation
→ license decision options
→ ADR-0024 decision options
→ NK-SAM and named equivalence profiles
→ Event/history commitment
→ only then reducer-v2 runtime
```

Executable NK-EPI, Temporal, full Admission, operational deletion, full independent implementation and ecosystem integration remain outside the current reconciliation slice.

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
5. implementation records, work log and PR/issue history;
6. Notion and historical chats.

## Automated guards

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json
python tools/ai_context/validate_project_state.py --repo .
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
- [`NOTION_HANDOFF.md`](NOTION_HANDOFF.md)
- [`AUDIT_PLAYBOOK.md`](AUDIT_PLAYBOOK.md)

Historical records preserve provenance; they do not override current state.