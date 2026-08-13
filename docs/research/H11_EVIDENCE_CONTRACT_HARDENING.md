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
| Claimed mechanism coverage without graph evidence | Every covered mechanism needs exactly one `PROFILE_MECHANISM` node, a content-addressed repository source, at least one connected dependency edge and an existing `DEPENDENCY_EDGE` raw observation whose structured `{edge_id, from, to}` binding matches that exact edge. | Missing node, missing edge, missing raw reference, generic observation and mismatched edge-binding fixtures are rejected. |
| Self-reviewed qualification | `QUALIFIED` requires established identity, non-authorship, `INDEPENDENT_FOR_DECLARED_SCOPE`, zero conflicts, repository-visible basis and existing content-addressed evidence. | `SAME_CUSTODY` + `SELF_REVIEW` is rejected. |
| Weak support invariant | `SUPPORTED_FOR_SCOPE` conditionally requires qualified independence, zero mandatory-profile leakage and zero unjustified Canon dependency. The validator independently recounts hard-failure edges and the distinct profile mechanisms they implicate. | Support with unqualified independence or an unjustified edge is rejected. |
| Arbitrary/collapsed artifact references | Raw, graph and qualification inputs are typed `{path, sha256, artifact_type}` references, must exist in-repository, match bytes, be mutually distinct and cannot point at the adjudication itself. | Collapsed paths and digest mismatch are rejected. |
| Non-repository observations in adjudication | Every consumed raw observation must be `repository_visible=true` and its source must resolve to content-addressed repository bytes. | A non-visible observation is rejected. |
| Semantic self-report in raw evidence | Raw observations require producer identity, authority class, observation type and provenance. Verdict keys/tokens in `fact` or `structured_value` are rejected before adjudication. | Text and structured verdict injection plus missing producer identity are rejected. |

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
