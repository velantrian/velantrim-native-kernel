# 🗺️ Native Kernel Component and Evidence Map

## Current route

```text
Architecture Canon
→ accepted contracts
→ PostgreSQL and SQLite profiles
→ C2 single-profile reports
→ C3 cross-profile comparison
→ C4 offline shadow evidence
→ C5 bounded operational rehearsal
→ durable evidence archive + project-state snapshot
```

## Track map

```text
H historical recovery      docs/source-recovery/ + Issue #1
C clean implementation     native_kernel/ + profiles/ + tests/ + workflows
R long-horizon research    docs/research/ + proposed ADR/RFC work
```

## Main surfaces

| Surface | Role | Boundary |
|---|---|---|
| `project-state.json` | machine-readable repository/evidence snapshot | project state, not world truth |
| `contracts/project-state-v1.schema.json` | versioned state shape | no live remote mutation |
| `tools/ai_context/validate_project_state.py` | fail-closed state validator | checks declared snapshot and boundaries |
| `contracts/operational-plan-v1.json` | immutable 18-scenario C5 plan | synthetic ephemeral only |
| `native_kernel/operational_validation/` | report/Receipt validation core | evidence layer, not authority |
| `tools/operations/c5_rehearsal.py` | real profile rehearsal runner | no production/live data |
| `evidence/c5/2026-08-07/manifest.json` | two-checkpoint archive inventory | retained bytes, no proof expansion |
| `tools/evidence/verify_bundle.py` | archive/file integrity verifier | integrity, not truth/authenticity |
| `.github/workflows/c5-operational-rehearsal.yml` | four-environment C5 matrix | exact runs/artifacts only |
| `docs/research/POST_C5_RESEARCH_BACKLOG.md` | deferred/proposed ideas | no implementation or promotion |

## C5 scenario map

```text
SECURITY
├── authority denial ×2
└── stale writer fencing ×2

RELIABILITY
└── idempotent retry ×2

ROLLBACK
└── injected precommit fault ×2

RECOVERY
├── replay/projection ×2
└── quarantine import ×1

INCIDENT
├── corruption detection ×2
└── timeline containment ×1

PRIVACY
├── synthetic-only ×1
└── canary redaction ×1

RESILIENCE
└── bounded load ×2
```

## Ownership boundary

C5 owns bounded observation evidence. The evidence archive owns preservation of exact bytes. Project state owns a versioned repository-state snapshot. None owns production deployment, truth, cloud IAM, compliance, physical deletion, public APIs, candidate promotion or ecosystem authority.
