# 🔐 C5 durable evidence archive

> **Protocol:** `nk-evidence-bundle/1`
> **Capture date:** 2026-08-07
> **Status:** `CAPTURED_REPOSITORY_RESIDENT / BOUNDED EVIDENCE / NOT PRODUCTION PROOF`

This directory preserves the exact ZIP bytes produced by two C5 GitHub Actions checkpoints before the original 30-day retention expires:

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
python -m unittest discover -s tests -p 'test_evidence_bundle.py' -v
```

The verifier checks archive hashes, internal file inventories and hashes, source SHAs, workflow runs, environments, assertion counts and C5 boundaries.

## Preservation rules

- Files under `original/` are exact downloaded GitHub Actions ZIP archives.
- Do not rewrite, recompress or replace them under the same bundle identity.
- A changed archive requires a new bundle ID and manifest.
- The manifest records both the GitHub-provided digest and a locally recomputed SHA-256.
- Extracted reports are intentionally not duplicated in Git because the verifier reads them directly from preserved ZIP bytes.

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
