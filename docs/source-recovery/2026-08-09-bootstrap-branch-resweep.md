# Source Recovery Resweep — 2026-08-09

> **Search ID:** `NK-SRC-RECOVERY-20260809-004`  
> **Result:** `NOT_FOUND_IN_ACCESSIBLE_SOURCES`  
> **Target:** reported external `v0.1.2.1`, original 44-test suite, benchmark harness, and environment metadata  
> **Live main at sweep start:** `1fd1d49e643f253bc1de26bda63d0b56584f8ebe`  
> **Decision impact:** Issue #1 remains blocked  
> **Global-loss claim:** not made

## 1. Reason for this resweep

The earlier accessible-source sweep did not separately record the retained branch:

```text
bootstrap/research-kernel-v0.1.2.1
```

Because the branch name resembles the reported historical checkpoint, it required an explicit lineage and tree inspection before it could be rejected as a source-bearing candidate.

## 2. Branch identity

```yaml
branch: bootstrap/research-kernel-v0.1.2.1
head: d64855afc4b34bcfb0ed8f1c3766925d287b07c6
head_date: 2026-07-22T19:57:12Z
head_message: "docs: standardize evidence grip terminology"
protected: false
associated_pr: 2
pr_title: "docs: bootstrap Native Kernel research repository"
pr_merge: 8377f6c03a9ad5f99bc9aea18aa810ccba0b50f4
```

PR #2 explicitly described the branch as a documentation-first bootstrap and stated that it added no runnable kernel code. It was merged on 2026-07-22, while the head branch remained retained.

## 3. Head-tree inventory

The complete recursive tree at `d64855afc4b34bcfb0ed8f1c3766925d287b07c6` contains only:

```text
.gitignore
ARCHITECTURE.md
CONTRIBUTING.md
README.md
ROADMAP.md
SECURITY.md
STATUS.md
docs/BENCHMARKS.md
docs/INTEGRATION_BOUNDARIES.md
prototype/README.md
```

It contains no:

```text
kernel.py
Python package source
test files
benchmark harness
dependency lock
environment export
source archive
CI workflow for the historical suite
```

## 4. Full reachable lineage inspection

The branch is a single-parent chain of 14 commits including the repository initial commit:

```text
636781fb  Initial commit
92bf1309  docs: establish Native Kernel research overview
8e6b009f  docs: define exact repository status boundary
c95ab689  docs: add Native Kernel architecture and invariants
41c75de3  docs: add staged Native Kernel roadmap
a3d24f31  docs: add benchmark methodology and evidence boundary
59caf04e  docs: define Titan and Crystal integration boundaries
e029cff4  docs: add research-stage security policy
e3f32544  docs: add contribution and status discipline
5d5f496e  docs: add controlled prototype import plan
b3e942db  docs: align repository maturity terminology
da5d019d  docs: standardize documented-only status
c85d3da5  docs: align prototype import status terminology
d64855af  docs: standardize evidence grip terminology
```

Every commit diff was inspected. The chain begins with `.gitignore` and a two-line `README.md`; later commits add or edit only documentation. No commit adds, deletes, renames, or modifies a source file, test file, benchmark executable, environment file, or archive.

The branch therefore does not contain a deleted historical runtime hidden in an earlier reachable tree.

## 5. Evidence inside the branch

The branch documentation itself preserves the opposite boundary:

- `STATUS.md` says the previously tested Python prototype and 44-test suite were not merged into the repository;
- `ROADMAP.md` lists `kernel.py`, the original suite, environment metadata, CI, and benchmark script as future import artifacts;
- `prototype/README.md` is an import checklist and says those artifacts were verified outside the repository;
- `docs/BENCHMARKS.md` labels timing values as prior local observations pending source and harness import.

These are historical references, not recovered bytes.

## 6. Additional GitHub checks

The connected GitHub surface was also checked for:

```text
branches matching: v0.1.2.1, prototype, source, recovery
code: v0.1.2.1, lexical_proxy_ablation, conclusion_frozen, _canonical_neighbors
commits: v0.1.2.1, lexical_proxy_ablation, conclusion_frozen, _canonical_neighbors
tags
releases
```

Results:

- the only branch matching `v0.1.2.1` was the docs-only bootstrap branch inspected above;
- `prototype` returned no other branch;
- `source` and `recovery` returned only later source-recovery tooling branches;
- distinctive code identifiers resolved only to derived documentation;
- commit search returned documentation or unrelated neighboring-project matches, not the historical source;
- the repository has no tags and no releases.

## 7. Notion resweep

Connected Notion workspace search was repeated for:

```text
v0.1.2.1
lexical_proxy_ablation
conclusion_frozen
_canonical_neighbors
```

The results again resolved to the Native Kernel historical status, roadmap, architecture, and hub pages. The full `Prototype Status v0.1.2.1 & Benchmarks` page explicitly classifies the checkpoint as an external report whose source is not located and contains no source attachment or original test inventory.

No byte-level candidate was surfaced.

## 8. Candidate and false-positive classification

```yaml
candidate_artifacts: []
false_positive:
  ref: bootstrap/research-kernel-v0.1.2.1
  classification: MERGED_DOCS_BOOTSTRAP_BRANCH
  source_bearing: false
  reason: >-
    Complete head tree and all reachable commit diffs contain documentation only.
    PR #2 explicitly preserved the runtime as an external, future import.
```

No artifact was available to hash, quarantine, manifest, or execute.

## 9. Conclusion

Supported conclusion:

```text
The retained bootstrap/research-kernel-v0.1.2.1 branch is not the
historical prototype and contains no recoverable source or original tests.
The authentic v0.1.2.1 source remains not found in the connected surfaces
checked on 2026-08-09.
```

Unsupported conclusion:

```text
The source is globally and permanently lost.
```

Operator-controlled local devices, IDE history, local Git reflogs/stashes, backups, private archives, disconnected cloud folders, email attachments, removable media, and inaccessible repositories remain outside this sweep.

## 10. Next gate

Issue #1 remains open. Stage 1 remains blocked until either:

1. a byte-level candidate is preserved and classified `UNVERIFIED_CANDIDATE`, then accepted by an explicit operator provenance decision; or
2. the operator declares all relevant local surfaces checked and records the checkpoint as `LOST / NON-REPRODUCIBLE EXTERNAL CHECKPOINT`.

A reconstructed or clean implementation must use a separate version and evidence lineage and must not inherit the reported `v0.1.2.1` result.
