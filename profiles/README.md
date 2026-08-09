# Native Kernel Implementation and Evidence Profiles

```yaml
document_role: PROFILE_STATUS
status_as_of: 2026-08-09
authoritative_machine_source: ../project-state.json
active_architecture_decision: ADR-0025
architecture_phase: ARCHITECTURE_REFOUNDATION_BLUEPRINT_FIRST
runtime_expansion_frozen: true
```

This directory contains machine-readable planning, implementation and evidence surfaces for replaceable profiles and bounded evaluation layers.

The current P1–C5 profiles are preserved as a **bounded reference laboratory**. They remain valid for their versioned contracts, fixtures and evidence, but they are not architectural authority and may not expand semantic/runtime scope before the ADR-0025 blueprint gate.

```text
profile or evidence manifest
≠ Architecture Canon
≠ completed A1–A10 blueprint
≠ complete runtime support
≠ evidence by itself
≠ production authorization
```

## Current profiles and evidence layers

| Surface | Decision | Implementation | Evidence | Assertion map |
|---|---|---|---|---|
| `native-kernel/postgresql-reference@0.4-p4` | `ACCEPTED / APPROVED` | `PARTIAL — P1–P4` | `C2 REPOSITORY_REPRODUCED` | `41 / 13 / 18 / 0` |
| `native-kernel/sqlite-embedded@0.5-p5` | `ACCEPTED / APPROVED` | `PARTIAL — P5` | `C2 REPOSITORY_REPRODUCED` | `41 / 13 / 18 / 0` |
| PostgreSQL↔SQLite comparison | `ADR-0019` | `PARTIAL — C3` | `REPOSITORY_REPRODUCED` | `45 / 10 / 17 / 0` |
| `native-kernel/c4-offline-shadow-v1` | `ADR-0020` | `PARTIAL — C4` | `REPOSITORY_REPRODUCED ON APPROVED DATASET` | `45 / 10 / 17 / 0` |
| `native-kernel/c5-bounded-rehearsal-v1` | `ADR-0021` | `PARTIAL — C5 BOUNDED SYNTHETIC OPERATIONAL REHEARSAL` | `REPOSITORY-RESIDENT EXACT ZIP BUNDLES` | `45 / 10 / 17 / 0` |

```text
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
support_state:              PARTIAL
production_authorized:      false
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

C4 and C5 are evidence/evaluation layers, not storage lineages. They do not create a new authoritative database or production profile.

## Current lineages

```text
clean/postgresql-reference/0.1
clean/sqlite-embedded/0.1
```

Both lineages remain independent from Historical Recovery Issue #1 and must never be represented as recovered `v0.1.2.1`.

## SQLite integrity boundary

Historical C5 matrices used SQLite `3.45.1`. ADR-0023 requires linked SQLite `3.51.3+` for the current WAL profile.

```text
historical SQLite 3.45.1 evidence
→ immutable and version-bound

current linked SQLite 3.51.3 profile
→ fail-closed floor
→ separate safe-version evidence identity
```

Safe-version evidence is retained under:

```text
evidence/c5/2026-08-08-adr0023/manifest.json
```

Historical evidence is not rewritten as if it had been produced by the safer runtime.

## Manifest roles

### PostgreSQL

- [`postgresql-reference-v0/profile-manifest.json`](./postgresql-reference-v0/profile-manifest.json) — initial proposal snapshot;
- [`postgresql-reference-v0/p1-manifest.json`](./postgresql-reference-v0/p1-manifest.json) — P1 semantic core;
- [`postgresql-reference-v0/p2-manifest.json`](./postgresql-reference-v0/p2-manifest.json) — P2 append and idempotency;
- [`postgresql-reference-v0/p3-manifest.json`](./postgresql-reference-v0/p3-manifest.json) — P3 replay, projection and Receipts;
- [`postgresql-reference-v0/p4-manifest.json`](./postgresql-reference-v0/p4-manifest.json) — PostgreSQL C2 assertion map.

### SQLite and C3

- [`sqlite-embedded-v0/p5-manifest.json`](./sqlite-embedded-v0/p5-manifest.json) — SQLite C2, C3 comparison, equivalence classes, artifacts and boundaries.

### C4

- [`shadow-evaluation-v0/c4-manifest.json`](./shadow-evaluation-v0/c4-manifest.json) — dataset identity, C3 prerequisite, C4 scope, artifacts and non-claims;
- [`shadow-evaluation-v0/README.md`](./shadow-evaluation-v0/README.md) — human-readable C4 guide.

### C5

- [`operational-validation-v0/c5-manifest.json`](./operational-validation-v0/c5-manifest.json) — bounded operational plan, prerequisites, scenario classes and non-claims;
- [`../evidence/c5/README.md`](../evidence/c5/README.md) — repository-resident exact ZIP identities.

## Package ownership

[`../native_kernel/postgresql_profile/`](../native_kernel/postgresql_profile/) owns PostgreSQL-specific append, replay, projection, Receipt and P4 report behavior.

[`../native_kernel/sqlite_profile/`](../native_kernel/sqlite_profile/) independently owns stdlib `sqlite3` persistence, transactions, fencing, replay, projections, Receipts, exact-history import and SQLite C2/C3 behavior.

[`../native_kernel/shadow_evaluation/`](../native_kernel/shadow_evaluation/) owns authority-free comparison of approved recorded observations.

[`../native_kernel/operational_validation/`](../native_kernel/operational_validation/) owns bounded synthetic operational scenarios and Receipts. It does not own production deployment, external authority or live data.

Shared contracts and fixtures do not make implementations fully independent. PostgreSQL and SQLite still share a Python semantic lineage.

## Phase boundary

```text
P0: COMPLETE
P1: MERGED
P2: MERGED
P3: MERGED
P4: MERGED / PARTIAL / C2
P5: MERGED / PARTIAL / C2 + C3
C4: MERGED / PARTIAL / OFFLINE SHADOW EVIDENCE
C5: MERGED / PARTIAL / BOUNDED SYNTHETIC OPERATIONAL REHEARSAL
Production: NOT AUTHORIZED / NOT ESTABLISHED
```

## Proof boundaries

```text
C2 profile evidence
≠ cross-profile equivalence

C3 semantic/behavioural comparison
≠ operational equivalence
≠ independent language implementation

C4 offline shadow evidence
≠ live shadow deployment
≠ authority promotion

C5 bounded synthetic rehearsal
≠ production readiness
≠ compliance
≠ physical backup or deletion
≠ ecosystem wiring
```

## Next gate

Profile runtime expansion is frozen under ADR-0025. The authoritative sequence is:

```text
A1 Purpose and Non-goals
→ A2 Knowledge and Memory Ontology
→ A3 Abstract Native Kernel Machine
→ A4 Semantic Laws and Invariants
→ A5 Identity / Time / Change
→ A6 Knowledge Lifecycle
→ A7 Conflict / Uncertainty / Revision
→ A8 Substrate-independence Contract
→ A9 Reference Laboratory Boundary
→ A10 Open Questions / Falsification
→ integrated blueprint review
→ separate operator decision reopening runtime work
```

Only after that gate may downstream profile work be reconsidered:

```text
reconcile contract families
→ define NK-SAM and named equivalence profiles
→ define portable Event/history commitment
→ obtain the relevant license/publication and ADR-0024 decisions where required
→ only then authorize a new profile or reducer-v2 runtime slice
```

Completing an older profile checklist does not bypass ADR-0025. Integrity, security, reproducibility, provenance, evidence-preservation, validator and historical-recovery fixes remain allowed without semantic/runtime promotion.

## Read next

- [`../STATUS.md`](../STATUS.md)
- [`../ROADMAP.md`](../ROADMAP.md)
- [`../project-state.json`](../project-state.json)
- [`../docs/ARCHITECTURE_REFOUNDATION.md`](../docs/ARCHITECTURE_REFOUNDATION.md)
- [`../docs/adr/0025-blueprint-before-runtime-expansion.md`](../docs/adr/0025-blueprint-before-runtime-expansion.md)
- [`../docs/CONFORMANCE_MODEL.md`](../docs/CONFORMANCE_MODEL.md)
- [`../docs/ai/CURRENT_STATE.md`](../docs/ai/CURRENT_STATE.md)
- [`../docs/ai/KNOWN_RISKS.md`](../docs/ai/KNOWN_RISKS.md)
- [`../evidence/c5/README.md`](../evidence/c5/README.md)

The previous profile-status snapshot remains available in Git history at publication checkpoint `626f34e…`.
