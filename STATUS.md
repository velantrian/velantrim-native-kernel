# Current Status

> **Verified source checkpoint:** `3d56912260ea41b5b501b65477bff1642dfc2d58`
> **C5 implementation evidence checkpoint:** `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7`
> **Implementation publication:** Issue #64 `CLOSED / COMPLETED`, PR #65 merged, ADR-0021 accepted
> **Repository status:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

The checkpoint above is the verified repository state this document describes. A descendant documentation commit does not invalidate the evidence lineage and must not be confused with the artifact-producing SHA.

## 2026-08-08 integrity remediation candidate

```text
Branch:                 agent/sqlite-integrity-wal-safety
Decision:               ADR-0023 ACCEPTED / APPROVED
SQLite WAL minimum:     linked 3.51.3
Event Envelope:         exact field/value/hash verification implemented
Migration atomicity:    repaired
Configured busy timeout: preserved
Local focused tests:    PASS on linked SQLite 3.51.3
Repository matrices:    PENDING
New durable evidence:   PENDING / must be additive
```

The 2026-08-07 P5/C3/C4/C5 results on SQLite 3.45.1 remain exact historical evidence. Because 3.45.1 is inside SQLite's documented WAL-reset bug range and the prior SQLite verifier omitted committed fields, affected integrity/equivalence evidence is under review until safe-version reproduction. The arithmetic remains `45 / 10 / 17 / 0`; `NK-EPI` remains `0 / 8 SUPPORTED`; production remains unauthorized.

## Three independent tracks

| Track | Scope | Status |
|---|---|---|
| `H` — Historical Recovery | authentic `v0.1.2.1` and original 44-test suite | `BLOCKED / ACTIVE EVIDENCE-RECOVERY` |
| `C` — Clean Implementation | independently versioned P1–P5, C4 and C5 | `ACTIVE / PARTIAL` |
| `R` — Long-Horizon Research | proposed future contracts, profiles and experiments | `PROPOSED / BOUNDED` |

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
research proposal ≠ accepted contract ≠ runtime
```

Track H does not block Track C. Track R does not gain runtime or Canon status through documentation.

## Clean implementation phase

```text
P1: MERGED / REPOSITORY-TESTED
P2: MERGED / REPOSITORY-INTEGRATION-TESTED
P3: MERGED / REPOSITORY-INTEGRATION-TESTED
P4: MERGED / PARTIAL / POSTGRESQL C2
P5: MERGED / PARTIAL / SQLITE C2 + CROSS-PROFILE C3
C4: MERGED / PARTIAL / OFFLINE SHADOW EVIDENCE
C5: MERGED / PARTIAL / BOUNDED SYNTHETIC OPERATIONAL REHEARSAL
Production: NOT AUTHORIZED / NOT ESTABLISHED
```

C5 is a bounded operational evidence layer. It is not a new storage profile, production deployment, public service, compliance certification or ecosystem authority.

## Semantic and operational levels

```text
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
support_state:              PARTIAL
```

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
Offline C4 scope:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
C5 assertion map:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI-001…008:     0 SUPPORTED /  0 PARTIAL /  8 UNSUPPORTED / 0 FAILED
```

C5 does not promote semantic assertions. `NK-EPI-004 — unknown ≠ false` is a research candidate, not current runtime support.

## Operational plan

```text
plan_id:       native-kernel/c5-bounded-rehearsal-v1
protocol:      nk-operational-plan/1
sha256:        4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios:     18
deployment:    CI_EPHEMERAL_SYNTHETIC
```

Categories: `SECURITY · PRIVACY · RECOVERY · ROLLBACK · INCIDENT · RELIABILITY · RESILIENCE`.

## Exact C5 evidence lineage

### Implementation-main checkpoint

```text
Head:       296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
C5 run:     31204861404 — PASS
C4:         31204861534 — PASS
P5/C3:      31204861602 — PASS
P4:         31204861564 — PASS
AI context: 31204861416 — PASS
```

### Final documentation-main checkpoint

```text
Head:       3d56912260ea41b5b501b65477bff1642dfc2d58
C5 run:     31205512911 — PASS
C4:         31205512919 — PASS
P5/C3:      31205512874 — PASS
P4:         31205512957 — PASS
AI context: 31205512966 — PASS
```

C5 matrix at both checkpoints:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Every job passed C5 guards, exact P4/P5/C3/C4 prerequisites, all 18 scenarios, P1–C4 regressions, compileall and six-report artifact upload.

## Durable evidence capture

The exact eight ZIP archives from both C5 checkpoints are repository-resident:

```text
evidence/c5/2026-08-07/manifest.json
```

The bundle records:

- two checkpoint SHAs and workflow runs;
- eight original GitHub Actions ZIPs;
- GitHub and locally recomputed archive SHA-256 values;
- exact six-file inventories and file-level hashes;
- environment and bounded result metadata.

Verification:

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
```

The original GitHub Actions copies expire on 2026-09-06. The repository-resident bytes no longer depend on that retention window.

## Mandatory deployment boundary

```text
live_user_data: false
synthetic_data_only: true
production_traffic: false
network_api_exposed: false
authority_promotion: false
authoritative_external_side_effects: false
ecosystem_wiring: false
physical_deletion_claimed: false
compliance_certification_claimed: false
```

## Explicit non-claims

```text
C5 bounded rehearsal PASS
≠ production readiness
≠ live-user-traffic validation
≠ cloud IAM or multi-region HA proof
≠ exhaustive disaster recovery
≠ physical PostgreSQL backup
≠ physical or cryptographic deletion
≠ compliance certification
≠ operational equivalence
≠ truth or external authenticity
≠ authority promotion
≠ ecosystem wiring
≠ NK-EPI advancement
```

## Machine-readable state

`project-state.json` is the authoritative machine-readable project snapshot for repository state and evidence boundaries. It does not claim truth about the external world and does not replace exact code, tests, artifacts or GitHub live state.

## Next gate

1. reproduce P5/C3/C4/C5 on linked SQLite 3.51.3 at the exact remediation head;
2. preserve the new artifacts under a new evidence identity without changing the 2026-08-07 ZIPs;
3. re-adjudicate only affected integrity/equivalence assertions from executable evidence;
4. complete GitHub↔Notion synchronization for ADR-0023;
5. keep reducer referential rules and NK-EPI work in separately authorized contract-first slices.

Any production, live-traffic, physical-deletion, NK-EPI promotion or ecosystem-authority work requires separate explicit operator approval and evidence.
