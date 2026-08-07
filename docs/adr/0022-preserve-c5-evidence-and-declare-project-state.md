# ADR-0022 — Preserve C5 evidence bytes and declare versioned project state

- **Decision status:** `ACCEPTED`
- **Evidence level:** `LOCALLY_VERIFIED / REPOSITORY_CI_PENDING`
- **Implementation status:** `IMPLEMENTED IN THIS CHANGE`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-07`
- **Decider:** `@velantrian`
- **Track:** `Clean Implementation Governance`
- **Related:** ADR-0007, ADR-0014, ADR-0015, ADR-0021, Issue #1, Issue #64

## Context

C5 produced exact GitHub Actions artifacts under a 30-day retention window. Digests were committed, but digests without retained bytes cannot preserve or independently re-inspect the original reports.

At the same time, current-state facts were distributed across `STATUS.md`, AI-context files, ROADMAP, Issues, CI and Notion. This caused external audits to disagree on basic facts such as whether runtime, tests, CI, PostgreSQL and Issue #64 existed.

The historical source-recovery path, clean implementation and future research were also represented through an older two-track roadmap that no longer reflected the accepted clean lineage.

## Decision

### 1. Preserve exact C5 bytes

Adopt `nk-evidence-bundle/1` for the bounded C5 archive.

Preserve exact original ZIP archives from:

```text
implementation-main:
  SHA 296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
  run 31204861404

final documentation main:
  SHA 3d56912260ea41b5b501b65477bff1642dfc2d58
  run 31205512911
```

The bundle must record archive hashes, internal file inventories, file hashes, source SHAs, workflow runs, environments, results and non-claims.

### 2. Declare machine-readable project state

Adopt `nk-project-state/1` as a versioned repository-state snapshot.

It records:

- verified ancestor checkpoint;
- implementation evidence checkpoint;
- maturity and assertion maps;
- Issue #1 and #64 observations with verification method/time;
- durable evidence location;
- production and epistemic non-claims;
- Notion synchronization state.

It does not replace code, tests, artifacts or live GitHub state.

### 3. Separate three tracks

```text
H — historical recovery
C — clean implementation
R — long-horizon research
```

Track H remains open and independent. Track C is active/partial. Track R remains proposed and cannot promote itself through documentation.

### 4. Keep future proposals in research

Post-C5 proposals such as NK-EPI-004, admission boundaries, erasure revisions, cross-language profiles, signed Receipts, licensing and ecosystem adapters belong in `docs/research/` until separately accepted and evidenced.

## Alternatives considered

### Keep hashes only

Rejected. A hash cannot reconstruct missing artifact bytes.

### Re-run C5 later instead of preserving old artifacts

Rejected. A future run is new evidence, not the original execution.

### Store only the final-main run

Rejected. The implementation-main run and final documentation-main replay are distinct evidence checkpoints.

### Make ROADMAP the sole state source

Rejected. ROADMAP mixes historical and future direction and is not machine-readable live state.

### Promote research ideas immediately

Rejected. This would violate the separation of proposal, decision, implementation and evidence.

## Consequences

### Positive

- exact C5 evidence survives Actions expiry;
- current state becomes machine-readable and fail-closed;
- historical, clean and research lineages become explicit;
- future auditors can distinguish bytes, metadata, evidence and proposals;
- research ideas are preserved without implementation overclaim.

### Costs

- eight small binary ZIPs enter repository history;
- state and evidence validators require maintenance;
- live GitHub/Notion facts still require freshness checks;
- future evidence bundles need explicit versioning and storage policy.

## Boundaries

```text
retained C5 bytes ≠ production evidence
project-state snapshot ≠ world truth
verified issue state ≠ permanent issue state
research backlog ≠ accepted contract or runtime
clean lineage ≠ recovered v0.1.2.1
```

## Verification

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/ai_context/validate_project_state.py --repo .
python -m unittest discover -s tests -p 'test_evidence_bundle.py' -v
python -m unittest discover -s tests -p 'test_project_state.py' -v
```

## Rollback and supersession

Do not delete the archived bytes merely because this mechanism is superseded. A successor may migrate them to independent immutable storage, but must preserve this manifest, original archive hashes and decision history.
