# 🤖 Native Kernel AI Context Pack

This directory is the mandatory continuity surface for AI agents, auditors and maintainers.

## Required reading order

1. [`../../README.md`](../../README.md)
2. [`../../STATUS.md`](../../STATUS.md)
3. [`../../project-state.json`](../../project-state.json)
4. [`../../AGENTS.md`](../../AGENTS.md)
5. [`CURRENT_STATE.md`](CURRENT_STATE.md)
6. [`C5_IMPLEMENTATION_RECORD.md`](C5_IMPLEMENTATION_RECORD.md)
7. [`../../evidence/c5/README.md`](../../evidence/c5/README.md)
8. [`COMPONENT_MAP.md`](COMPONENT_MAP.md)
9. [`KNOWN_RISKS.md`](KNOWN_RISKS.md)
10. [`WORK_LOG.md`](WORK_LOG.md)
11. [`DOCUMENTATION_SYNC_PROTOCOL.md`](DOCUMENTATION_SYNC_PROTOCOL.md)
12. [`AUDIT_PLAYBOOK.md`](AUDIT_PLAYBOOK.md)

## Current boundary

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
support_state: PARTIAL
assertion map: 45 / 10 / 17 / 0
NK-EPI: 0 / 8 SUPPORTED
```

## Track boundary

```text
H historical recovery: BLOCKED / independent
C clean implementation: ACTIVE / PARTIAL
R long-horizon research: PROPOSED / bounded
```

```text
historical recovery ≠ clean implementation
research proposal ≠ runtime
C2 ≠ C3 ≠ C4 ≠ C5
C5 bounded rehearsal ≠ production readiness
C5 operational validation ≠ assertion promotion
C5 logical backup ≠ physical disaster recovery
```

## C5 evidence route

```text
Issue #64 CLOSED / PR #65 merged / ADR-0021
→ immutable plan
→ implementation-main run 31204861404
→ final-main run 31205512911
→ eight exact repository-resident ZIPs
→ archive and file-level manifest
→ strict bundle verifier
```

## Source-of-truth order

1. exact code, tests, contracts and retained artifact bytes;
2. exact-SHA CI jobs/logs and GitHub live issue state;
3. `project-state.json`, `STATUS.md` and current-state checkpoint;
4. accepted ADRs/contracts;
5. work log and PR/issue records;
6. Notion and historical chats.

## Automated guards

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_context.py --repo .
```
