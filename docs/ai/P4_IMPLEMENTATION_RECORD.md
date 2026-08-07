# 🧪 P4 Assertion-Scoped Conformance Implementation Record

**Recorded:** 2026-08-07  
**Base public `main`:** `4f8cb0a8b7d9ca678a8578cf005b118fd6dff150`  
**Canonical issue:** #55  
**Pull request:** #56  
**Evidence lineage:** `clean/postgresql-reference/0.1`  
**Profile:** `native-kernel/postgresql-reference@0.4-p4`  
**Decision:** ADR-0018 `ACCEPTED / APPROVED`

## Maturity

```text
P1 semantic core:          MERGED / REPOSITORY-TESTED
P2 PostgreSQL append:      MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections:     MERGED / REPOSITORY-INTEGRATION-TESTED
P4 conformance adapter:    PARTIAL / C2 REPOSITORY-REPRODUCED ON PREVIOUS HEAD
P5 / C3:                   NOT AUTHORIZED / NOT ESTABLISHED
support_state:              PARTIAL
C4/C5:                     NOT ESTABLISHED
```

P4 does not claim that every registered assertion is supported. It establishes an executable, complete and traceable report for all 72 IDs.

## Assertion result map

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

The top-level `C2` label applies only to assertion results marked `SUPPORTED` in the exact report. `PARTIAL` and `UNSUPPORTED` remain outside the supported conformance set.

All `NK-EPI-001…008` results remain `UNSUPPORTED` because the registry decision status remains `PROPOSED`.

## Executable route

```text
contracts/registry.json + fixture-pack.json
→ semantic and identity checks
→ authority and Receipt checks
→ reducer and deletion-semantic checks
→ real PostgreSQL migration/fencing/append checks
→ real replay/projection/stale-head/corruption checks
→ 72 assertion results
→ assertion-to-check traceability validation
→ nk-evidence-report/1
→ independent runner validation
→ retained per-matrix JSON artifact
```

## P4 checks

Semantic/profile-neutral checks:

- `p4.registry.contracts`;
- `p4.identity.golden`;
- `p4.identity.invalid`;
- `p4.semantic.roles`;
- `p4.authority.policy`;
- `p4.receipts.boundaries`;
- `p4.reducer.determinism`;
- `p4.reducer.failures`;
- `p4.deletion.semantic`.

PostgreSQL profile checks:

- `p4.postgresql.migrations`;
- `p4.postgresql.writer-fencing`;
- `p4.postgresql.append-idempotency`;
- `p4.postgresql.rollback-ordering`;
- `p4.postgresql.replay-projection`;
- `p4.postgresql.stale-head`;
- `p4.postgresql.corruption`.

Evidence checks:

- `p4.environment.metadata`;
- `p4.report.traceability`.

Every `SUPPORTED` and `PARTIAL` result names one or more passed checks and explicit limitations. Missing, duplicate, unknown, untraceable or failed evidence is rejected.

## Initial repository C2 evidence

Executable head:

```text
93710131fffdea7d9a586cc05e7f258c07fae707
```

Workflow run:

```text
P4 assertion conformance 31175767586 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
```

Each matrix job passed:

- 5 P4 assertion-mapping/traceability tests;
- 5 P4 manifest/anti-overclaim tests;
- 1 full PostgreSQL C1 report integration test;
- generation and strict validation of a C2 report;
- P1 semantic and manifest regressions;
- P2 unit, PostgreSQL and manifest regressions;
- P3 semantic, PostgreSQL and manifest regressions;
- compileall.

Four artifacts were retained for 30 days:

| Artifact | Digest |
|---|---|
| `p4-evidence-py3.11-pg16` | `sha256:63e609a009b0fa05ddd31c0d659fe6d03a0afce1006bbe7d6216059f3affbad3` |
| `p4-evidence-py3.11-pg18` | `sha256:6f5f2a4202e73d909e015a193be7a3990ab92208e40ef5cd320048c00cfe0707` |
| `p4-evidence-py3.12-pg16` | `sha256:60cba98b4b27932d348c43110ee820ef9f73eac84f5a7abfdf3c004aec8639d8` |
| `p4-evidence-py3.12-pg18` | `sha256:ead4ad348acbc0e3c2c08923e5fdd6fbe825927f32936bb6f2351f61e184f65f` |

The initial failure run `31175593261` is retained as negative evidence: all P4 C1 checks passed, but the standalone adapter could not import the repository package. The CLI bootstrap was corrected without lowering runtime or report requirements.

## Evidence boundary

```text
P4 C2 for 41 SUPPORTED assertions
≠ support for all 72 assertions
≠ C3 cross-profile equivalence
≠ accepted NK-EPI
≠ truth or external authenticity
≠ physical/cryptographic deletion
≠ C4/C5
≠ production readiness
```

## Remaining risks

- static assertion mapping can drift from implementation if guards are bypassed;
- top-level C2 can be misread as complete profile support despite `support_state: PARTIAL`;
- one PostgreSQL profile cannot prove storage neutrality;
- conflict modeling remains mostly unsupported;
- deletion execution, restore visibility and cross-project authority remain absent;
- C2 metadata is credible only when tied to an actual repository run/artifact;
- artifact retention is finite;
- performance, failover, backup/restore and managed-provider behavior remain untested;
- Issue #18 licensing/publication terms remain unresolved.

## Finalization gate

1. update public and AI documentation to P4 reality;
2. repeat P4/P1/P2/P3/fixture/AI checks on one exact final PR head;
3. inspect full diff, comments and review threads;
4. merge only with P5/C3/deletion/production scope absent;
5. synchronize final PR/merge/run evidence to Notion;
6. require separate operator GO before P5/C3.
