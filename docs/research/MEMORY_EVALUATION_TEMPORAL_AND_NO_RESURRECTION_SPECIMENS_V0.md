# Memory Evaluation: Temporal and Logical No-Resurrection Specimens v0

**Status:** `RESEARCH / NON-CANONICAL / NOT RUNTIME AUTHORITY`

**A10-H06:** `OPEN / INDETERMINATE` (unchanged)

These are synthetic, documentation-only specimen specifications: `specimen specification != executed evidence`. Their expected adjudication labels are not observations, runtime conformance, or promotion of an invariant. They use existing A5/A6 and restore-rule semantics; no new API or deletion concept is proposed.

## Temporal/as-of specimen

The fixture uses the A5 distinction among [VALID_TIME and RECORD_TIME](../A5_IDENTITY_TIME_AND_CHANGE.md#6-temporal-dimensions). Its half-open interval notation is local to this fixture, not a universal profile rule. The fields and filters below describe a specimen, not a runtime schema or API.

```yaml
entity: synthetic:account-017
interval_convention: "[from, to) for this fixture only"
records:
  - id: fact-active-1
    kind: FACT
    status: ACTIVE
    valid_time: [2026-01-01, 2026-03-01)
    record_time: 2026-01-02T09:00:00Z
  - id: correction-suspended-1
    kind: FACT_CORRECTION
    status: SUSPENDED
    valid_time: [2026-02-01, 2026-02-20)
    record_time: 2026-03-01T09:00:00Z
    lineage: "scoped correction of fact-active-1 for this interval only"
  - id: plan-archived-1
    kind: PLAN
    status: ARCHIVED
    effective_from: 2026-06-01
    record_time: 2026-02-10T09:00:00Z
```

The three predicates are separate. `record_time <= cutoff` selects what was retained by the record-time cutoff; `valid_time contains date` selects the represented valid-time position. Exact timestamps make the record cutoffs explicit for this fixture.

| Query | Predicate and cutoff | Expected result |
|---|---|---|
| (a) What was known then? | `record_time <= 2026-02-15T23:59:59Z` and `valid_time contains 2026-02-15` | `ACTIVE`; the late correction is not yet in the selected record set. |
| (b) What is now known about that past date? | `record_time <= 2026-03-02T23:59:59Z` and `valid_time contains 2026-02-15` | `SUSPENDED`; the scoped late correction is now included. |
| (c) What valid-time position is represented for an earlier date? | `record_time <= 2026-03-02T23:59:59Z` and `valid_time contains 2026-01-15` | `ACTIVE`. This is the fixture's latest represented position for that date, not a claim of truth beyond its records. |

The `ARCHIVED` entry remains a `PLAN`, not a fact. With the latest record cutoff above, a factual-status query for valid date `2026-06-01` returns `UNKNOWN`; a separate plan query may report `ARCHIVED` as planned. The fixture does not infer that the plan occurred.

**Oracle.** `PASS` means the three results remain distinct as specified, the plan remains a plan, and factual status on the future date is `UNKNOWN`. `FAIL` means the record cutoff and retrospective/valid-time results collapse together, or the plan is returned as an established fact. `UNKNOWN` means a cutoff, interval, lineage, or fact-versus-plan distinction cannot be resolved, or the fixture is not executed. These are expected adjudication semantics only.

## H06 logical no-resurrection specimen

This specimen reuses the existing [A6 `LOGICALLY_ERASED` meaning](../A6_KNOWLEDGE_LIFECYCLE.md#7-disposition-and-closure-kinds) and the existing [restore rule](../contracts/NORMATIVE_CONTRACTS_V1.md#restore-rule). It proposes neither a new deletion state nor a semantic invariant. Only the following synthetic surfaces are in scope:

1. **Authoritative state/history:** the source claim, its derived-item lineage, and the existing logical disposition record; inspection of a disposed Record remains subject to Authority.
2. **One ordinary retrieval/projection cache:** the only indexed/queryable surface checked by this specimen.
3. **One synthetic derived view:** `LC-01`, a `LessonCandidate` derived from the source claim; no other generated view is checked.
4. **One pre-disposition archive:** a synthetic snapshot containing the source claim and `LC-01`, included only under the existing contract's backup/restore scope.

The synthetic source claim is `CLM-01: sample-entity preferred_format = concise`. `LC-01` is the single derived LessonCandidate carrying that preference. Positive control `CTRL-01: sample-entity locale = en` is unrelated, not disposed, and kept outside the pre-disposition archive so it remains queryable throughout this fixture. These are invented fixture values, not user data.

**Path and expected observations:** create the source, LessonCandidate, control, and pre-disposition archive; apply the existing logical disposition to the source and derived target; run an ordinary query; replay/rebuild the enumerated projection from authoritative history; restore the old archive into quarantine; check ordinary-query visibility during quarantine; apply the latest disposition under the existing restore rule; then repeat the ordinary query after the restore rule permits visibility. At the disposition, replay/rebuild, quarantine, and post-restore query checkpoints, `CLM-01` and `LC-01` must not be returned as ordinary accessible knowledge; `CTRL-01` remains available. The restore check is expressly before general visibility, not a test of privileged Authority inspection.

**Oracle.** `PASS` is available only for the enumerated logical surfaces when the source and derived targets remain ordinarily unavailable, the control remains available, and restore applies the latest disposition before restored data becomes ordinarily queryable. `FAIL` means source/derived content resurfaces, the control is lost, or the result claims coverage beyond the enumerated surfaces. `UNKNOWN` applies if any enumerated surface or Oracle is unobservable, or the specified path is not executed. The label definitions are expected test adjudication semantics, not executed observations.

This specimen does not establish physical deletion or cryptographic erasure; those remain `UNKNOWN / INDETERMINATE`. It makes no global-coverage claim for unlisted indexes, caches, exports, providers, backups, replicas, logs, or other surfaces. No runtime, model run, tests, CI, or benchmarks were executed to write this specification; it asserts no runtime conformance and does not change H06 status.
