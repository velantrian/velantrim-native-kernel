# H11 evidence-contract hardening against PR #131 findings

**Status:** bounded validation-machinery candidate; no H11 execution authorized  
**Source review:** PR #131 · review `4923945680` · reviewed head `61f02f7eb3f6c3903fa5662358690457bba4fb9e`  
**Immutable review subject:** `e36b7f45410d74b8a65406bff6fdd6d070fa96b0`  
**Frozen plan:** `H11-001-c5-lab-canon-separation-v1`  
**Frozen plan SHA-256:** `60da649e675b79b3e70bf8a61cf03cb4d57bb989f4934b65ab8d50c925b19914`

## Boundary

This change hardens schemas and validators only. The frozen preregistration bytes,
hypothesis, leakage classes, support threshold, hard refutation, experiment identity and
outcome vocabulary remain unchanged. No dependency graph is constructed for the real
experiment; no real observation is produced; no reviewer is qualified; no leakage count
is calculated; and no semantic adjudication occurs.

```text
validation machinery hardening
≠ H11 execution
≠ H11 evidence
≠ reviewer qualification
≠ execution admission
≠ H11 outcome
```

If a future remediation requires changing the frozen H11 hypothesis, rubric, threshold or
hard-refutation semantics, this candidate is insufficient: work must stop and proceed
through explicit versioning and re-preregistration. It must not edit the frozen plan
post-hoc.

The existing `/1` protocol identifiers remain in place deliberately. No real H11 graph,
observation or adjudication artifact has been admitted under those protocols, and these
changes encode constraints already required by the frozen rubric rather than introduce a
new hypothesis or outcome meaning. If an admitted external consumer or evidence artifact
is later found to depend on the permissive shape, the protocol must be versioned instead
of being treated as backward compatible.

## Reconciliation of the six P1 findings

| Finding | Fail-closed control | Regression evidence |
|---|---|---|
| Claimed mechanism coverage without graph evidence | Every covered mechanism needs exactly one `PROFILE_MECHANISM` node, a Git-anchored repository source, at least one connected dependency edge and an existing `DEPENDENCY_EDGE` raw observation whose structured `{edge_id, from, to, edge_class}` binding matches that exact edge. | Missing node, missing edge, missing raw reference, generic observation and mismatched edge-binding fixtures are rejected. |
| Self-reviewed qualification | `QUALIFIED` requires established identity, non-authorship, `INDEPENDENT_FOR_DECLARED_SCOPE`, zero conflicts, structured organizational-separation and independent-custody bases, plus Git-anchored evidence. | `SAME_CUSTODY` + `SELF_REVIEW` and CI/validator substitute bases are rejected. |
| Weak support invariant | `SUPPORTED_FOR_SCOPE` conditionally requires qualified independence, zero mandatory-profile leakage, zero unjustified Canon dependency, exact positive verification of the frozen eight-artifact bundle and no raw/graph/adjudication gaps. The validator independently recounts hard-failure edges and the distinct profile mechanisms they implicate. | Support with unqualified independence, an unjustified edge, absent/failed bundle verification or any declared gap is rejected. |
| Arbitrary/collapsed artifact references | Raw, graph and qualification inputs are typed `{path, sha256, artifact_type, git_commit}` references. The commit must be an ancestor of the adjudicated `HEAD`; both the declared Git object and `HEAD` path must preserve the digest; inputs must be mutually distinct and cannot point at the adjudication itself. | Untracked input, collapsed paths, moved/deleted Git objects and digest mismatch are rejected. |
| Non-repository observations in adjudication | Every consumed raw observation must be `repository_visible=true` and its source must resolve to bytes preserved in the adjudicated Git tree. | A non-visible or untracked observation is rejected. |
| Semantic self-report in raw evidence | Raw observations require producer identity, authority class, observation type, provenance, an observation-kind-specific neutral fact token and a closed typed `structured_value`. Free-form fact/notes channels are not accepted. | Verdict injection, ordinary-language semantic paraphrases, unknown structured fields and missing producer identity are rejected. |

## PR #134 second-round review hardening

A substantive Codex review of PR #134 at `7bb05b5a42acfb7ab37b3f20a3936959e27ed64c`
found seven additional P1 bypasses. The review is captured in
`H11_PR134_CODEX_REVIEW_RECONCILIATION.json`. It remains technical review only and does
not qualify Codex as the H11 reviewer/reproducer.

| PR #134 finding | Bounded remediation candidate |
|---|---|
| Supplied records were not validated against their schemas | The graph, raw, reviewer and adjudication objects are now evaluated against their complete bound schemas before cross-record checks; schema-forbidden fields fail closed. |
| Worktree files could masquerade as repository-visible evidence | Every evidence reference now includes a full `git_commit`; the validator resolves bytes from Git, checks ancestry to `HEAD`, and verifies unchanged preservation at `HEAD`. |
| A hard Architecture→profile requirement could be mislabeled benign | `ARCHITECTURE_OBLIGATION → PROFILE_MECHANISM` with `ARCHITECTURE_REQUIRES` is structurally forced to `UNJUSTIFIED_CANON_DEPENDENCY`; a benign label is rejected. |
| Semantic paraphrases bypassed the token blacklist | Raw facts are closed neutral tokens and structured values are observation-kind-specific closed objects; arbitrary prose is no longer an evidence channel. |
| CI and validators could substitute for reviewer independence | A qualified record needs structured `ORGANIZATIONAL_SEPARATION` and `INDEPENDENT_EVIDENCE_CUSTODY` evidence; frozen non-qualifying substitutes are rejected. |
| Scoped support could omit laboratory verification or declare gaps | Support requires exactly one successful exact-bundle observation for the frozen subject, at least eight verified artifacts, and empty missing/gap inventories. |
| Conditional schema rules were checked only as text | A dependency-free schema-subset evaluator exercises valid and adversarial instances. Conditions made unreachable with `not: {}` fail validation. |

## PR #134 third-round review hardening

Codex reviewed the next candidate at
`1e179d31ed2a7618319ca20dd930a7d562d5fae8` and opened seven P1 threads plus one P2.
The review is captured in `H11_PR134_CODEX_REREVIEW_RECONCILIATION.json`. It remains a
technical hardening review and has no H11 reviewer-qualification effect.

| Re-review finding | Bounded remediation candidate |
|---|---|
| Graph completeness could remain vacuous | The graph must contain exactly one node for each frozen `H11-O01`–`H11-O04` obligation, at least one node of every frozen class, all twelve distinct profile nodes, no self-loops and no disconnected nodes. Historical, Architecture and profile sources are frozen-snapshot-bound. |
| Generic bytes could pose as independence evidence | Qualified bases now reference closed structured attestations bound to experiment, plan digest, reviewer, issuer, issuer role, basis type, authorship, custody, conflicts, private-state exclusion and repository visibility. The two mandatory bases require distinct non-self issuers and exactly enumerated distinct artifacts. |
| Bundle success trusted self-report | Scoped support requires `TOOL_OUTPUT` from `AUTOMATED_VALIDATOR`, bound to the frozen manifest. The admission validator runs the repository `verify_bundle.py`, requires success and derives the exact eight-artifact count rather than trusting the observation. |
| Hard failure could be downgraded | `UNJUSTIFIED_CANON_DEPENDENCY > 0` and `REFUTED` are a bidirectional invariant in both schema and validator. |
| Subject could author adjudication while citing an unrelated reviewer | Semantic records now carry adjudicator identity, role and `QUALIFYING_INDEPENDENT_REVIEWER` authority; identity and role must exactly match the qualified reviewer record. |
| Historical sources could be rewritten before citation | Architecture, laboratory and profile references must predate or equal immutable review subject `e36b7f...`, exist there with identical bytes, and remain unchanged through adjudicated `HEAD`. |
| Python equality could equate `true` with `1` | Referenced records are schema-validated after load and compared recursively with exact JSON type identity; schema `const`/`enum` evaluation uses the same strict comparator. |
| String patterns were ignored | The dependency-free schema evaluator applies regex patterns to string instances and fails closed on invalid patterns. |

Seventy-four local H11 tests cover the blocked admission package and all three review
rounds. Bounded implementation head `9dbab33ff3a8ecfe9383ce861f9bb6168521a6d4`
passed all six repository workflows; all 15 PR #134 threads were reconciled with evidence,
and the seven existing Notion pages were read back 7/7. This documentation-reconciliation
descendant still requires its own exact-head workflows and fresh final review before any
protected merge. None of that evidence qualifies an H11 reviewer or changes admission.

The synthetic acceptance fixture in `tests/test_h11_execution_admission.py` proves only
that the validation machinery can accept a structurally complete fabricated test bundle.
It is created in a temporary directory, is not H11 evidence, and cannot affect repository
admission or project state.

## Reviewer reconciliation

The substantive Codex review is now captured in
`H11_PR131_CODEX_REVIEW_RECONCILIATION.json` with all six thread URLs and the reviewer's
own disclosure. The reviewer identity is known, but qualification remains
`NOT_ESTABLISHED`: shared Codex custody and organizational/self-review separation were not
established. Recording a useful non-qualifying review is not the same as upgrading it.

## State preserved

```text
current gate:                  A10_H11_EXECUTION_ADMISSION
admission:                     BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
qualifying reviewer:           NOT_ESTABLISHED
H11:                           NOT_TESTED
implementation authorized:     false
execution authorized:          false
dependency graph authorized:   false
semantic adjudication:         false
runtime expansion:             FROZEN
Final Canon:                   DEFERRED / NOT_AUTHORIZED
production:                    false
Issue #88:                     OPEN
```

After this hardening is independently reviewed, CI-validated and merged, a genuinely
independent H11 reviewer/reproducer is still required. Reviewer qualification must then be
recorded and execution admission must be reassessed separately. Neither merge nor green CI
can make admission pass by itself.
