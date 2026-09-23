# NK-HYGIENE-01 — branch inventory

Status: READ_ONLY_CLASSIFICATION · NO_DELETION_AUTHORITY

Observed baseline: main@7b938a76de9fd2778a4a08728be047ab7d4f960f

## Inventory

- 142 branches total during audit, including the active audit branch.
- 141 non-main refs.
- 162 pull requests inspected from repository history.
- 126 current branch tips exactly match merged PR heads.
- 3 additional refs are confirmed ancestors of current main.
- 4 refs exactly match closed-unmerged PR heads.
- 1 PR-associated ref has tip drift.
- 4 refs have no PR association in accessible history.
- 2 refs are frozen protected evidence lineages.
- 1 ref is the active audit branch.

## Boundary

No class in this inventory authorizes branch deletion.
Merged-PR and ancestor-of-main classifications still require a citation/provenance
check before any ref deletion. Commit ancestry is not treated as content-equivalence
for squash/rebase history.

The frozen preservation refs remain:

- archive/bootstrap-v0.1.2.1-docs-lineage
- bootstrap/research-kernel-v0.1.2.1

H11, runtime, Canon, reducer semantics, and production authorization are unchanged.

## Residual manual-review set

Closed-unmerged:
- agent/cognitive-os-relations (#149)
- agent/pr87-delayed-review-followups (#90)
- cursor/audit-2026-09-08-82b1 (#181)
- docs/readme-deep-explanation (#4)

PR-associated tip drift:
- docs/readme-visual-polish

No PR association:
- claude/audit-relationships-6866cw
- claude/documentation-analysis-owkx58
- claude/titan-native-kernel-audit-egbygd
- claude/velantrim-native-kernel-audit-18id3g

The following residual refs are confirmed ancestors of main but still await citation/provenance review:
- agent/bpv1-d6-status
- fix/operator-decision-ci-coverage
- repair/world-epistemic-boundaries
