# 🤖 Native Kernel AI Context Pack

This directory is the mandatory continuity surface for AI agents, auditors and maintainers.

## Required reading order

1. [`../../README.md`](../../README.md)
2. [`../../STATUS.md`](../../STATUS.md)
3. [`../../AGENTS.md`](../../AGENTS.md)
4. [`CURRENT_STATE.md`](CURRENT_STATE.md)
5. [`C5_IMPLEMENTATION_RECORD.md`](C5_IMPLEMENTATION_RECORD.md)
6. [`C4_IMPLEMENTATION_RECORD.md`](C4_IMPLEMENTATION_RECORD.md)
7. [`P5_IMPLEMENTATION_RECORD.md`](P5_IMPLEMENTATION_RECORD.md)
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
```

```text
C2 ≠ C3 ≠ C4 ≠ C5
C5 bounded rehearsal ≠ production readiness
C5 synthetic data ≠ live user traffic
C5 operational validation ≠ assertion promotion
C5 logical backup ≠ physical disaster recovery
```

## C5 evidence route

```text
Issue #64 + ADR-0021
→ exact operational-plan-v1 bytes and SHA-256
→ exact C4 prerequisite report
→ 18 real profile scenarios
→ nk-operational-report/1
→ 18 nk-operational-receipt/1 records
→ nk-operational-backup/1
→ strict validators
→ exact-SHA six-report CI artifact
```

## Source-of-truth order

1. exact code, tests and plan bytes;
2. exact-SHA CI jobs/logs/artifacts;
3. `STATUS.md` and current-state checkpoint;
4. accepted ADRs/contracts;
5. work log and PR/issue records;
6. Notion and historical chats.

## Automated guard

```bash
python tools/ai_context/validate_context.py --repo .
```

The guard checks required C5 context files, links, checkpoint ancestry and mandatory C5 non-claim markers.
