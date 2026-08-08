# 🔐 C5 durable evidence archive

> **Protocol:** `nk-evidence-bundle/1`
> **Capture dates:** 2026-08-07 and 2026-08-08
> **Status:** `CAPTURED_REPOSITORY_RESIDENT / BOUNDED EVIDENCE / NOT PRODUCTION PROOF`

The original 2026-08-07 identity preserves the exact ZIP bytes produced by two C5 GitHub Actions checkpoints before the original 30-day retention expires:

1. implementation-main `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7`, run `31204861404`;
2. final documentation main `3d56912260ea41b5b501b65477bff1642dfc2d58`, run `31205512911`.

Each checkpoint contains four environment artifacts. Each artifact preserves six uploaded JSON files:

```text
postgresql-p4-report.json
sqlite-p5-report.json
c3-equivalence-report.json
c4-shadow-report.json
c5-operational-report.json
c5-quarantine-backup.json
```

## Verify

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json
python -m unittest discover -s tests -p 'test_evidence_bundle.py' -v
```

The verifier checks archive hashes, internal file inventories and hashes, source SHAs, workflow runs, environments, assertion counts and C5 boundaries.

## Preservation rules

- Files under `original/` are exact downloaded GitHub Actions ZIP archives.
- Do not rewrite, recompress or replace them under the same bundle identity.
- A changed archive requires a new bundle ID and manifest.
- The manifest records both the GitHub-provided digest and a locally recomputed SHA-256.
- Extracted reports are intentionally not duplicated in Git because the verifier reads them directly from preserved ZIP bytes.

The additive `2026-08-08-adr0023` identity preserves PR-head and final-main C5 archives from linked SQLite 3.51.3. It cross-binds the exact P5/C3, C4 and C5 workflow runs used for the integrity revalidation. It does not rewrite the 2026-08-07 identity.

Post-merge review tightened that cross-binding: the v1 JSON Schema now declares the optional ADR-0023 metadata, and the repository verifier binds each remediation role to its exact commit and P5/C3, C4 and C5 run IDs. This is a compatible contract/verifier correction; neither manifest nor any archived ZIP is rewritten. The retained runs predate the later JSON type-exact Event comparison and are not evidence of that follow-up implementation.

## Explicit non-claims

```text
retained artifact bytes
≠ production readiness
≠ live-user-data validation
≠ compliance certification
≠ physical backup or physical deletion
≠ operational equivalence
≠ truth or external authenticity
≠ NK-EPI promotion
```
