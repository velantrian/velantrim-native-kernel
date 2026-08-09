# 🧾 Native Kernel AI Engineering Work Log

Re-verify exact SHAs, live issue state, runs and artifacts before treating an entry as current reality.

---

## 2026-08-09 — A2 Knowledge and Memory Ontology (second blueprint content slice)

```text
Issue:                      #88
Decision:                   ADR-0025
Base main:                  7b73015c07c46ba9490028768a587f768017f4b3
Classification:             Architecture Re-foundation blueprint content
Deliverable:                A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY
Runtime and contracts:      UNCHANGED
Assertion map / NK-EPI:     UNCHANGED
Production authorization:   UNCHANGED / false
```

Drafted the second Architecture Re-foundation content deliverable, `A2 — Knowledge and Memory Ontology`, as bilingual documents (`docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md` / `.ru.md`). The document defines a provisional technology- and substrate-neutral distinction set for Signal, Observation, Record, Proposition, Claim, Interpretation, Hypothesis, Belief, Knowledge, Memory, Evidence, Source, Provenance, Context, Relation, State, Change, Event, Conflict, Contradiction, Uncertainty, Revision, Supersession, Authority, and Receipt.

For every concept A2 records a working definition, non-definition, neighbouring distinctions, allowed relations, identity/lifecycle notes, minimum semantic obligations, unresolved questions, a falsification/counterexample, and provisional classification as `CANDIDATE_PRIMITIVE`, `DERIVED_CONCEPT`, or `OPEN_QUESTION`. It compares linear-pipeline, Event-centred, relation-first, and stratified-role organizations without accepting any one as final Canon. Event, State, and Memory remain open primitive questions.

A2 explicitly preserves:

```text
Observation ≠ Claim
Claim ≠ Truth
Evidence ≠ Source
Repetition ≠ Evidence
Belief ≠ Knowledge
Memory ≠ merely a stored Record
retrieval relevance ≠ epistemic validity
Conflict ≠ necessarily Contradiction
Unknown ≠ False
Event usage in P1–C5 ≠ Event as universal primitive
State ≠ necessarily reducer output
Knowledge ≠ LLM / embeddings / SQL / JSON / specific processor
```

Wired the pair into navigation and the bilingual parity registry, advanced `project-state.json` and the fail-closed architecture-freeze validator to exact completed deliverables `[A1, A2]` and next slice `A3_ABSTRACT_NATIVE_KERNEL_MACHINE`, extended AI continuity surfaces, and added dedicated ontology regression tests. A2 maps the current P1–C5 model as a bounded profile without changing any runtime class, reducer, Event vocabulary, storage profile, contract, fixture, evidence artifact, assertion, or maturity label.

This first draft remains `DRAFTED / PROVISIONAL` pending independent review and integrated review with A1 and A3–A10. It does not decide Issue #18, Issue #74/ADR-0024, or Track H source acceptance. Runtime expansion remains frozen.

## 2026-08-09 — A1 Kernel Purpose and Non-goals (first blueprint content slice)

```text
Issue:                      #88
Decision:                   ADR-0025
Base main:                  e578db8acd2d4f8a1f5600722cd7880e1c79f397
Classification:             Architecture Re-foundation blueprint content
Deliverable:                A1_KERNEL_PURPOSE_AND_NON_GOALS
Runtime and contracts:      UNCHANGED
Assertion map / NK-EPI:     UNCHANGED
Production authorization:   UNCHANGED / false
```

Drafted the first Architecture Re-foundation content deliverable, `A1 — Kernel Purpose and Non-goals`, as bilingual documents (`docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.md` / `.ru.md`). The document defines the problem Native Kernel studies, what `Kernel` means in this project, the candidate durable qualities a conforming implementation must preserve, what is explicitly outside the Kernel, and the boundary with Titan, Crystal, Mentaury, operating systems, databases, and model runtimes, satisfying the completion test recorded in `docs/ARCHITECTURE_REFOUNDATION.md`.

Wired the new document into the bilingual parity registry (`tools/docs/bilingual-pairs-v1.json`) and the AI-context required-path/link-scan inventories. Advanced the fail-closed architecture-freeze validator (`tools/ai_context/validate_architecture_freeze.py`) and `project-state.json` to record `A1` as the sole completed deliverable and `A2 — Knowledge and Memory Ontology` as the next content slice; the deliverable inventory, runtime freeze, and operator-review gate remain unchanged and fail closed.

This is a documentation and governance-tracking change only. It does not resume runtime, reducer, or profile work, does not change the assertion map, `NK-EPI`, `C4`/`C5` maturity, or production authorization, and does not decide Issue #18 or ADR-0024.

## 2026-08-08 — Bounded bilingual documentation parity validator

```text
Issue:                      #78
Base main:                  fc4559752ba8ed51907b0c0bc0a6a9952868c611
Classification:             Documentation integrity tooling
Translation scoring:        FORBIDDEN / NOT IMPLEMENTED
Runtime and contracts:      UNCHANGED
Assertion map / NK-EPI:     UNCHANGED
Production authorization:   UNCHANGED / false
```

Added an explicit `nk-bilingual-doc-parity/1` registry, dependency-free validator, failure-mode unit tests and AI-context workflow integration. The initial scope covers root and docs indexes, human Quickstart, glossary and storage/execution profiles.

The validator checks only configured file presence, language selectors, exact shared/language-specific obligations, single-H1 structure and optional heading-level outlines. It deliberately does not use file length, translation scores, semantic similarity models or automatic discovery of every `.ru.md` file. A PASS does not certify translation accuracy, completeness, legal equivalence, Canon or runtime evidence.

## 2026-08-08 — Human onboarding, glossary and bilingual profile parity

```text
Base main:                 da5d042d830508e46f36c7113197c87b8cef2f9c
Classification:            Documentation / onboarding / translation parity
Runtime and contracts:     UNCHANGED
Assertion map / NK-EPI:    UNCHANGED
Production authorization:  UNCHANGED / false
```

Prepared a bilingual human quickstart with exact semantic-core commands, the pinned SQLite 3.51.3 build path, PostgreSQL test setup, expected skip/fail-closed interpretation and evidence boundaries. Added a bilingual GitHub glossary that distinguishes Claim, Event, reducer state, epistemic state, projections, Receipts, evidence levels and governance status without describing proposed features as implemented.

The Russian storage/execution profile now restores the missing compute-versus-storage independence section and profile lineage fields. Root and documentation indexes expose the new human entry points. This is documentation-only work: no package publication, license choice, reducer v2, assertion promotion, evidence relabelling or maturity change is claimed.

## 2026-08-08 — Post-merge Codex integrity review follow-up in progress

```text
Reviewed main:            d8fe6c9f6e1233eb29ade630a85771e581c2813e
Source reviews:           PR #69 + PR #70 / 4 unresolved actionable threads
Classification:           Contract + Implementation Profile + Evidence + Governance
Candidate status:         PR #72 DRAFT / LOCAL FULL SUITE PASS / REPOSITORY CI PENDING
Assertion map / NK-EPI:   UNCHANGED
```

Reproduced and corrected in the candidate tree:

- JSON `true` versus `1` type confusion in stored Event envelope comparison;
- absent `tools/sqlite/**` pull/push triggers in P5/C3, C4 and C5;
- undeclared ADR-0023 fields in `evidence-bundle-v1.schema.json`;
- associated P5/C3 and C4 run IDs accepted as arbitrary positive integers.

Historical and ADR-0023 ZIPs remain byte-identical and keep their original evidence scope. Final PR/main runs and synchronization must be appended after merge; no maturity, production, assertion or NK-EPI promotion is authorized.

The tested implementation payload is remote commit `90c4a286dec2673c3768899cb67a55f854aa7b9c`, tree `bcd40890df6de12e0dbdd6371f4ba8b504325868`. Local validation: 172 PASS / 15 PostgreSQL-only SKIP on linked SQLite 3.51.3. Candidate state was prepended to the five canonical Notion pages before repository review.

## 2026-08-08 — SQLite integrity and WAL safety remediation completed

```text
PR:                     #69 SQUASH-MERGED
Runtime main:           675aa4b398a2fc0181dc71d38904a2d33a09f5f8
Decision:               ADR-0023 ACCEPTED / APPROVED
Repository evidence:    PR-HEAD + FINAL-MAIN PASS / ADDITIVE BUNDLE CAPTURED
Assertion map / NK-EPI: UNCHANGED
```

Completed:

- strict SQLite Event Envelope equality for contract, time, nested payload and exact fields;
- exact field-set parity in the PostgreSQL stored Event verifier;
- stored JSON failures normalized to `StoredEventCorrupt`;
- fail-closed linked SQLite 3.51.3 WAL minimum;
- pinned official SQLite source archive with SHA-256 verification in P5/C3/C4/C5 CI;
- evidence metadata must match the actually linked SQLite version;
- atomic migration execution without `executescript()` implicit commit;
- `timeout_seconds` now controls `PRAGMA busy_timeout`;
- regression tests for previously accepted malformed envelopes and failure paths.

Repository P5/C3, C4 and C5 matrices passed at PR head `ab7a203c…` and final main `675aa4b3…`. Eight exact new C5 archives are preserved under `evidence/c5/2026-08-08-adr0023/`; the 2026-08-07 bytes remain unchanged. Re-adjudication preserved 45/10/17/0 and NK-EPI 0/8. Reducer dangling/self/cycle semantics remain a separate contract-first slice because current accepted fixtures do not define the proposed rejection rule.

Evidence publication PR #70 final head `c9d3944627b40619002428d2a37b8621b2cbfe3b` squash-merged as `f13e0c8a948789d8d4e93e95fd95b61324478528`. Exact evidence payload commit `65d3375dbb5506540ba6d2d41e5508ea9c5dabc5` has tree `da5dfd59dbdcc75e930898a8a79ddd67fa7aec68`. All post-merge checks passed, and the five canonical Notion surfaces contain the final publication record.

## 2026-08-07 — C5 evidence preserved; state surfaces reconciled

```text
Verified source checkpoint: 3d56912260ea41b5b501b65477bff1642dfc2d58
Implementation checkpoint:  296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
Issue #64:                 CLOSED / COMPLETED
Status:                    C5 PARTIAL / NOT PRODUCTION-READY
```

Completed:

- downloaded and preserved four implementation-main C5 ZIPs;
- downloaded and preserved four final-main C5 ZIPs;
- verified all eight archive SHA-256 values against GitHub digests;
- recorded exact six-file inventories and file-level hashes;
- added `nk-evidence-bundle/1` manifest and strict verifier;
- added `nk-project-state/1` snapshot and validator;
- separated historical recovery, clean implementation and long-horizon research;
- corrected stale Issue #64 and checkpoint language;
- moved post-C5 proposals into a research-only backlog;
- preserved `NK-EPI 0/8` and all production/non-authority boundaries.

```text
retained bytes
≠ broader evidence than the producing runs
project-state snapshot
≠ self-updating remote truth
research backlog
≠ implementation authorization
```

Remaining:

- repository CI and review for this reconciliation;
- Notion synchronization in the same work cycle;
- separate authorization for any NK-EPI implementation.

---

## 2026-08-07 — C5 bounded operational rehearsal implemented

```text
Issue / PR / ADR: #64 / #65 / ADR-0021
Base main:        d1dd4986a8496cd9ca3e353d33ca422038c65d40
Implementation:   296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
Final checkpoint: 3d56912260ea41b5b501b65477bff1642dfc2d58
```

Implemented an immutable 18-scenario plan, operational report/Receipt/backup protocols, PostgreSQL/SQLite rehearsal, rollback, replay, quarantine restore, corruption/incident checks, privacy canaries, bounded load, strict validators and four-environment evidence.

---

## Previous milestones

```text
C4 / PR #62 + checkpoint #63
P5/C3 / PR #59 + checkpoint #60
P4 / PR #56
P3 / PR #50
P2 / PR #47
P1 / PR #44
```
