# 🧪 P4 Assertion-Scoped Conformance Implementation Record

**Recorded:** 2026-08-07  
**Base before P4:** `4f8cb0a8b7d9ca678a8578cf005b118fd6dff150`  
**Implementation PR:** #56  
**Implementation merge:** `db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad`  
**Evidence lineage:** `clean/postgresql-reference/0.1`  
**Profile:** `native-kernel/postgresql-reference@0.4-p4`  
**Decision:** ADR-0018 `ACCEPTED / APPROVED`

## Final maturity

```text
P1 semantic core:          MERGED / REPOSITORY-TESTED
P2 PostgreSQL append:      MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections:     MERGED / REPOSITORY-INTEGRATION-TESTED
P4 conformance adapter:    MERGED / PARTIAL / C2 REPOSITORY-REPRODUCED
P5 / C3:                   NOT AUTHORIZED / NOT ESTABLISHED
support_state:             PARTIAL
C4/C5:                     NOT ESTABLISHED
```

P4 establishes a complete and traceable report for all 72 IDs. It does not claim that all assertions are supported.

## Assertion result map

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

C2 applies only to `SUPPORTED`. All `NK-EPI-001…008` remain `UNSUPPORTED` because their registry decision remains `PROPOSED`.

## Executable route

```text
registry + fixture pack
→ semantic/identity/authority/Receipt/reducer/deletion checks
→ PostgreSQL migration/fencing/append/replay/projection checks
→ one result for every assertion
→ passed-check traceability + limitations
→ nk-evidence-report/1
→ strict independent validation
→ per-matrix JSON artifact
```

## Check inventory

Profile-neutral:

```text
p4.registry.contracts
p4.identity.golden
p4.identity.invalid
p4.semantic.roles
p4.authority.policy
p4.receipts.boundaries
p4.reducer.determinism
p4.reducer.failures
p4.deletion.semantic
```

PostgreSQL:

```text
p4.postgresql.migrations
p4.postgresql.writer-fencing
p4.postgresql.append-idempotency
p4.postgresql.rollback-ordering
p4.postgresql.replay-projection
p4.postgresql.stale-head
p4.postgresql.corruption
```

Evidence:

```text
p4.environment.metadata
p4.report.traceability
```

Every supported/partial result names passed checks and limitations. Missing, duplicate, unknown, untraceable or failed evidence is rejected.

## Final PR-head evidence

```text
head 0e7adf71475d37d5c096718762cbc08086c5e465
P4 run 31177071487 — PASS
P3 run 31177072239 — PASS
P2 run 31177071499 — PASS
P1 run 31177071518 — PASS
Fixture run 31177071508 — PASS
AI-context run 31177071481 — PASS
```

Four final-head artifacts:

| Environment | Digest |
|---|---|
| Python 3.11 / PostgreSQL 16 | `sha256:7817ed79023d5654b6045c45f8c63adf591e6f9668830e542fbbae4f32551bac` |
| Python 3.11 / PostgreSQL 18 | `sha256:6cb23c44c4b0917288e1faaf1b494b9aafcfe3d1967d45e2e62905ee6f309d60` |
| Python 3.12 / PostgreSQL 16 | `sha256:e11b482ea58db5bd57561231305936ab528e31a02a1187c4c3a6cf3ce3de9017` |
| Python 3.12 / PostgreSQL 18 | `sha256:11359b684421dbdfc3e1cee3f572c457375fd82bf72427655e17d95184ca971d` |

One final-head artifact was opened and verified to contain:

```text
report_version: nk-evidence-report/1
profile_id: native-kernel/postgresql-reference
support_state: PARTIAL
kernel_runtime_conformance: C2
assertion_results: 72
checks: 18 / all PASS
41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
NK-EPI-001…008: UNSUPPORTED
```

## Exact main-push evidence

```text
main db6d65f69f7fc0c42861e5ab45869ec9c2f3d8ad
P4 push run 31177335611 — PASS
P3 push run 31177335146 — PASS
P2 push run 31177335749 — PASS
P1 push run 31177335898 — PASS
Fixture push run 31177335864 — PASS
AI-context push run 31177335964 — PASS
```

Main-bound artifacts:

| Environment | Digest |
|---|---|
| Python 3.11 / PostgreSQL 16 | `sha256:aad734cc2c1e5e76f8949c07d8a757a4b952788e35ba572148867bf0c221ea6c` |
| Python 3.11 / PostgreSQL 18 | `sha256:4057790b9abba3f7375b0ed6a56bc9dad58db47f093db66b4007c96322b458fd` |
| Python 3.12 / PostgreSQL 16 | `sha256:6021a26ff70734f5caa208a04bb50d6b7faf1ab91942d6378f4e0ca5b590dc65` |
| Python 3.12 / PostgreSQL 18 | `sha256:0661e2640f5d80898a4ba6e041f889d69179d07ad8ba8eab69d0e19caae166ae` |

Artifacts expire on 2026-09-06 unless retained elsewhere.

## Defect evidence

Initial P4 run `31175593261` failed after all unit/manifest/full C1 checks passed because standalone CLI execution lacked repository-root import bootstrap. The bootstrap was fixed without weakening checks, statuses, support counts or validation.

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

- assertion mapping can drift if guards/review are bypassed;
- top-level C2 can be misread as complete support;
- one PostgreSQL profile cannot prove storage neutrality;
- conflict modeling remains mostly unsupported;
- deletion execution, restore visibility and cross-project authority remain absent;
- environment metadata is credible only with external run/artifact traceability;
- artifact retention is finite;
- performance, failover, backup/restore and managed-provider behavior remain untested;
- Issue #18 licensing/publication terms remain unresolved.

## Next gate

P5/C3 requires a new explicit operator GO, a materially independent SQLite profile, declared equivalence classes and retained comparison evidence.
