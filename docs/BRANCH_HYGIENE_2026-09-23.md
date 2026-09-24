# NK-HYGIENE-01 — branch inventory

Status: READ_ONLY_CLASSIFICATION · NO_DELETION_AUTHORITY

Observed baseline: main@7b938a76de9fd2778a4a08728be047ab7d4f960f

## Inventory

- 142 branches total during audit, including the active audit branch.
- 141 non-main refs.
- 162 pull requests inspected from repository history.
- 126 current branch tips exactly match merged PR heads.
- 3 additional refs are confirmed ancestors of current main.
- 9 refs carry a unique unmerged delta and must be preserved.
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

## Preserve: unique unmerged delta

- agent/cognitive-os-relations — 1 unique commit; ECOSYSTEM_RELATIONS.md.
- agent/pr87-delayed-review-followups — 3 unique commits; reconciliation validator/tests/known-risks.
- claude/audit-relationships-6866cw — 3 unique commits; ecosystem integration docs + ADR.
- claude/documentation-analysis-owkx58 — 1 unique documentation-audit commit.
- claude/titan-native-kernel-audit-egbygd — 1 unique 925-line audit commit.
- claude/velantrim-native-kernel-audit-18id3g — 1 unique validation/state/test delta.
- cursor/audit-2026-09-08-82b1 — 1 unique historical audit commit.
- docs/readme-deep-explanation — 1 unique substantial README delta.
- docs/readme-visual-polish — 3 unique commits; README + Copilot-instructions delta.

## Pending deletion-evidence pass

The 126 exact merged-PR heads and 3 confirmed ancestors of main are **not**
declared safe to delete here.

A default-branch citation pass found 12 surviving refs referenced through the
frozen evidence-anchor migration surfaces. Each of those 12 already has a
DURABLE_MAIN_CHECKPOINT_RECORDED record, but the migration policy explicitly
requires a separate owner action before branch deletion.

For the other 117 candidates, exact ref-name code search on the default branch
returned no match. This is bounded search evidence, not proof of global absence.
They still require final provenance review and explicit deletion authority.


## Semantic review follow-up — 2026-09-24

The nine `KEEP_UNMERGED_UNIQUE_DELTA` refs were reviewed against current main.
None should be merged wholesale.

Their bounded dispositions are recorded in
`evidence/branch-semantic-disposition-v1.json`:

- stale code / validator drafts that are superseded by stronger main remediation;
- historical audit snapshots that remain provenance, not current truth;
- closed research proposals that must not be silently promoted;
- one documentation-audit branch whose still-live findings were revalidated and
  selectively remediated rather than importing the stale audit snapshot.

This semantic review still does **not** authorize branch deletion.
