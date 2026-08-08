# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-08
**Verified ADR-0023 runtime checkpoint:** `675aa4b398a2fc0181dc71d38904a2d33a09f5f8`
**Repository status:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

C5 closes none of the production, live-data, compliance, physical-deletion, provider-IAM, multi-region, historical-recovery or ecosystem-authority risks.

## P0 — Historical SQLite Event verification was incomplete

The 2026-08-07 SQLite verifier did not bind `contract`, `recorded_at`, nested `payload`, or the exact envelope key set to stored Event columns. A canonical re-hashed malformed envelope could therefore pass SQLite verification while PostgreSQL rejected several of the same mismatches.

Post-merge review found one residual type-confusion path: Python considers booleans equal to corresponding integers, so structural equality could accept a re-hashed envelope with `true` where the canonical payload stored `1`.

**State:** `FOLLOW-UP IMPLEMENTED IN CURRENT CHANGESET / PR AND CI PENDING / HISTORICAL EVIDENCE VERSION-BOUND`. The correction compares each committed Event field by canonical JSON bytes in SQLite and PostgreSQL. Exact repository CI remains required. Earlier evidence is not erased or retroactively repaired.

## P0 — Evidence bundle contract and verifier identity drift

The ADR-0023 manifest published `evidence_purpose` and `sqlite_integrity` under `nk-evidence-bundle/1`, but the v1 JSON Schema did not declare them. The repository verifier also accepted arbitrary positive P5/C3 and C4 associated run IDs.

**State:** `FOLLOW-UP IMPLEMENTED IN CURRENT CHANGESET / PR AND CI PENDING`. The v1 contract is extended compatibly for the optional revalidation fields, while the verifier binds both ADR-0023 checkpoint roles to exact commit and P5/C3/C4/C5 run identities. This verifies repository-declared identity; it is not an external signature or independent custody proof.

## P1 — SQLite builder workflow path trigger gap

A change limited to `tools/sqlite/build_safe_sqlite.sh` did not trigger P5/C3, C4 or C5 although all three workflows execute it.

**State:** `FOLLOW-UP IMPLEMENTED IN CURRENT CHANGESET / PR AND CI PENDING`. Both pull-request and `main` push filters now include `tools/sqlite/**` in every dependent workflow.

## P0 — Historical SQLite 3.45.1 is in the WAL-reset bug range

SQLite upstream documents a rare corruption race for WAL databases using multiple connections with concurrent write/checkpoint activity in versions 3.7.0 through 3.51.2. All retained C5 jobs used SQLite 3.45.1.

**State:** `MITIGATED IN CURRENT PROFILE / HISTORICAL EVIDENCE VERSION-BOUND`. The profile fails closed below linked SQLite 3.51.3, CI pins and hash-checks the official source archive, and declared/runtime mismatch is rejected. Both safe-runtime checkpoints are repository-captured. Known backports are not implicitly allowlisted; historical artifacts remain immutable and explicitly version-bound.

## P0 — Bounded rehearsal may be mistaken for production readiness

```text
ephemeral CI + synthetic data + 18 scenarios
≠ production deployment
≠ live user traffic
≠ sustained operations
```

**State:** `OPEN / PRIMARY C5 COMMUNICATION RISK`.

## P0 — C5 may be mistaken for assertion promotion

```text
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
assertion map: 45 / 10 / 17 / 0
NK-EPI: 0 / 8 SUPPORTED
```

Operational evidence does not turn partial or unsupported assertions into supported ones.

## P0 — Historical and clean lineages may be collapsed

```text
clean P1–P5 + C4 + C5
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 remains open and independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## P0 — Research may be mistaken for authorization

`docs/research/POST_C5_RESEARCH_BACKLOG.md` contains proposed work only. NK-EPI, admission, signed Receipts, erasure changes, cross-language profiles and ecosystem adapters require separate decisions and evidence.

## P0 — Synthetic privacy checks may be mistaken for privacy compliance

Canaries were absent from inspected artifacts. This does not prove real personal-data handling, data-subject rights, retention, breach response, provider logs or jurisdictional compliance.

## P0 — Logical export may be mistaken for disaster recovery

The backup preserves exact synthetic Event bytes for one instance and supports quarantined import/replay. It is not physical PostgreSQL backup, WAL restore, provider snapshot, point-in-time recovery, cross-region restore or restore-under-load proof.

## P0 — Physical deletion remains absent

No physical or cryptographic deletion is executed across databases, backups, logs, artifacts, providers or keys. All C5 Receipts deny this proof.

## P0 — Operational equivalence remains absent

PostgreSQL and SQLite pass the same bounded scenarios, but concurrency, durability, replication, failover, administration, filesystem and managed-provider behavior remain different.

## P1 — Durable evidence is repository-resident but not independent custody

Sixteen exact ZIPs across the historical and ADR-0023 identities are preserved and verified under `evidence/c5/`. This closes the immediate Actions-retention loss, but does not provide:

- independent third-party custody;
- signed timestamping;
- append-only external archive;
- reviewer quorum;
- disaster recovery for the Git repository itself.

## P1 — Threshold representativeness

The current p95 limit is 5000 ms and workload is 24 Events per profile. Passing it is not a capacity, scale, SLO or cost claim.

## P1 — Environment scope

Current preserved C5 evidence is Ubuntu 24.04, Python 3.11/3.12, PostgreSQL 16/18, historical runner SQLite 3.45.1 and current linked SQLite 3.51.3. Other OS, architecture, provider, filesystem and runtime combinations are untested.

SQLite 3.45.1 is an evidence-bound historical environment, not a recommended future minimum. ADR-0023 sets linked SQLite 3.51.3 as the WAL floor; the replacement exact evidence cycle is captured under a separate identity.

## P1 — Machine-readable state can drift

`project-state.json` reduces ambiguity but is still a snapshot. Live issue state, default branch and HEAD can change. Validators therefore preserve verification method, observed time and ancestor-check semantics rather than claiming self-updating truth.

## P1 — Plan governance

The C5 plan is repository-local and approved by ADR-0021. There is no signed registry, independent reviewer quorum, revocation system or external audit.

## Update rule

Always record exact plan identity, SHA, run, artifact bytes, limitations, verification method and next gate. Never convert one bounded PASS, retained archive or research note into production, truth, compliance, deletion or ecosystem-authority claims.
