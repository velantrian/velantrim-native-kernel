# CI reproducibility boundary

Status: MAINTENANCE_GUARD · NON_CANONICAL · NO_AUTHORITY_PROMOTION

This maintenance surface narrows avoidable CI drift without changing runtime,
Canon, H11 admission, reducer semantics, or production authorization.

## Enforced now

- GitHub Actions references in repository workflows use full 40-character commit SHAs.
- Human-readable action release labels remain comments only.
- Workflow runners use the explicit `ubuntu-24.04` label instead of `ubuntu-latest`.
- PostgreSQL CI installs the declared driver without first upgrading pip.
- The PostgreSQL CI driver is version-pinned.
- `tools/ci/check_ci_reproducibility.py` fails closed on mutable action refs,
  `ubuntu-latest`, and workflow-level pip self-upgrade.

## Explicitly not proven

This does **not** make CI hermetic. It does not pin the underlying GitHub-hosted
runner image digest, apt/package-index state, PostgreSQL service image digest,
Python distribution artifact, transitive wheel hashes, DNS/network responses, or
GitHub service behavior.

Therefore:

CI green != environment identity.
CI green != H11 qualification.
CI green != runtime authorization.
CI green != Canon authorization.
CI green != production authorization.

## Next bounded hardening

A later maintenance change may add hash-locked Python artifacts and record
container/runner dependency identities. That requires its own evidence pass and
must not be described as semantic or authority progress.
