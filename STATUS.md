# Current Status

> **Verified ADR-0023 runtime checkpoint:** `675aa4b398a2fc0181dc71d38904a2d33a09f5f8`
> **C5 implementation evidence checkpoint:** `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7`
> **Implementation publication:** PR #69 squash-merged, ADR-0023 accepted; Issue #64 remains `CLOSED / COMPLETED`
> **Repository status:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`
> **Post-merge Codex review follow-up:** `PR #72 DRAFT / REPOSITORY CI PENDING`

The checkpoint above is the verified repository state this document describes. A descendant documentation commit does not invalidate the evidence lineage and must not be confused with the artifact-producing SHA.

## 2026-08-08 post-merge review follow-up

Four unresolved Codex review findings against PRs #69 and #70 were reproduced on `main@d8fe6c9f6e1233eb29ade630a85771e581c2813e`:

```text
Python bool/int equality bypass:      CONFIRMED
SQLite builder workflow trigger gap: CONFIRMED
evidence-bundle-v1 schema drift:      CONFIRMED
associated run-ID identity gap:       CONFIRMED
```

Draft PR [#72](https://github.com/velantrian/velantrim-native-kernel/pull/72) adds type-exact canonical Event field comparison in both profiles, `tools/sqlite/**` triggers in P5/C3/C4/C5, a backward-compatible `nk-evidence-bundle/1` schema extension and role-bound exact ADR-0023 run identities. Its tested implementation payload is commit `90c4a286dec2673c3768899cb67a55f854aa7b9c`, tree `bcd40890df6de12e0dbdd6371f4ba8b504325868`. Local validation and candidate Notion synchronization are complete. Repository CI and final merge evidence remain pending; the retained ADR-0023 ZIPs are not rewritten or described as evidence of this later fix.

## 2026-08-08 integrity remediation

```text
PR:                     #69 SQUASH-MERGED
Decision:               ADR-0023 ACCEPTED / APPROVED
SQLite WAL minimum:     linked 3.51.3
Event Envelope:         exact field/value/hash verification merged
Migration atomicity:    repaired
Configured busy timeout: preserved
PR-head P5/C3/C4/C5:    PASS / runs 31251376567, 31251376572, 31251376574
Final-main P5/C3/C4/C5: PASS / runs 31251526992, 31251526965, 31251526982
New durable evidence:   evidence/c5/2026-08-08-adr0023/manifest.json
```

The 2026-08-07 P5/C3/C4/C5 results on SQLite 3.45.1 remain exact historical evidence under their original identity. Revalidation on the actually linked SQLite 3.51.3 completed at PR-head and final-main checkpoints; the new eight ZIPs are additive. Re-adjudication preserved `45 / 10 / 17 / 0`; `NK-EPI` remains `0 / 8 SUPPORTED`; production remains unauthorized.

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

### ADR-0023 safe-runtime checkpoints

```text
PR #69 head ab7a203ce7ed8ec46c341bc4da9063d56f023338
  P5/C3 31251376567 — PASS
  C4     31251376572 — PASS
  C5     31251376574 — PASS

Merged main 675aa4b398a2fc0181dc71d38904a2d33a09f5f8
  P5/C3 31251526992 — PASS
  C4     31251526965 — PASS
  C5     31251526982 — PASS
```

Both matrices used Python 3.11/3.12 × PostgreSQL 16/18 × linked SQLite 3.51.3. Every C5 job recorded 18/18 scenarios, 18 Receipts, zero canary leaks, zero recovery failures and zero uncontained incidents.

## Durable evidence capture

Both additive eight-archive identities are repository-resident:

```text
evidence/c5/2026-08-07/manifest.json
evidence/c5/2026-08-08-adr0023/manifest.json
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
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json
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

1. complete PR review and exact P5/C3/C4/C5 CI for the post-merge Codex findings;
2. define reducer referential rules (dangling, self and cycle semantics) in a separate contract-first decision before changing runtime behavior;
3. keep NK-EPI-004 in its own separately authorized executable slice;
4. continue Track H source recovery independently;
5. continue operational hardening without promoting maturity through operations alone.

Any production, live-traffic, physical-deletion, NK-EPI promotion or ecosystem-authority work requires separate explicit operator approval and evidence.
