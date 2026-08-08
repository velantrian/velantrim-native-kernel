# ADR-0023 SQLite integrity revalidation evidence

> **Protocol:** `nk-evidence-bundle/1`
> **Purpose:** `ADR_0023_SQLITE_INTEGRITY_REVALIDATION`
> **Status:** `CAPTURED_REPOSITORY_RESIDENT / BOUNDED EVIDENCE / NOT PRODUCTION PROOF`

This bundle preserves the exact GitHub Actions C5 ZIP bytes for two safe-runtime checkpoints:

1. PR #69 head `ab7a203ce7ed8ec46c341bc4da9063d56f023338`, C5 run `31251376574`;
2. merged main `675aa4b398a2fc0181dc71d38904a2d33a09f5f8`, C5 run `31251526982`.

Each checkpoint contains the Python 3.11/3.12 × PostgreSQL 16/18 matrix. Every archived C5 report records the actually linked SQLite 3.51.3 runtime, PASS, 18/18 scenarios, 18 Receipts, and the unchanged assertion map 45/10/17/0. The manifest also binds the exact P5/C3 and C4 workflow run IDs for both checkpoints.

## Verify

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json
python -m unittest discover -s tests -p 'test_evidence_bundle.py' -v
```

The 2026-08-07 SQLite 3.45.1 bundle remains unchanged. This new identity is additive and does not retroactively relabel or replace historical bytes.

## Explicit non-claims

```text
safe-runtime bounded rehearsal
≠ production readiness
≠ live-user-data validation
≠ compliance certification
≠ physical backup or physical deletion
≠ operational equivalence
≠ truth or external authenticity
≠ NK-EPI promotion
```
