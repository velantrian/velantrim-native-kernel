# Memory Evaluation Specimens v0.1

```text
Status: PROPOSED RESEARCH / EVALUATION DEFINITIONS ONLY
Execution: NOT RUN
Architecture / Canon / runtime change: NONE
```

## Scope and attribution

These two bounded examples instantiate stress-profile directions already named in [Memory Evaluation Protocol v0](MEMORY_EVALUATION_PROTOCOL_V0.md), §10. They are test inputs and expected observations, not new semantic obligations, invariants, mechanisms, or evaluation results.

Attribution is limited to the OpenClaw/Mem0 example patterns supplied for this review. The examples do not assert anything about either project's current behavior, and neither project is an authority source for Native Kernel semantics.

## ME-TEMP-001 — valid time, occurrence interval, future and inexact date

### Fixed input

The fixture uses calendar dates and half-open intervals `[start, end)`. The evaluation anchor is `2026-10-01`.

```yaml
case_id: ME-TEMP-001
anchor_date: 2026-10-01
facts:
  - id: HOURS-PAST
    subject: office-hours
    value: "08:00"
    valid_from: 2026-08-01
    valid_until_exclusive: 2026-09-01
    recorded_at: 2026-08-01
  - id: HOURS-CURRENT
    subject: office-hours
    value: "09:00"
    valid_from: 2026-09-01
    valid_until_exclusive: 2026-10-15
    recorded_at: 2026-08-31
  - id: HOURS-FUTURE
    subject: office-hours
    value: "10:00"
    valid_from: 2026-10-15
    valid_until_exclusive: 2026-12-01
    recorded_at: 2026-09-28
  - id: EVENT-INSPECTION
    subject: inspection
    occurred_at: 2026-09-20
    recorded_at: 2026-09-30
  - id: DATE-INEXACT
    subject: maintenance-start
    known_window_start: 2026-11-01
    known_window_end_exclusive: 2026-12-01
    precision: month
    exact_day: unknown
```

### Queries and expected observations

| Query | Expected observation |
|---|---|
| What office hours are valid on the anchor date, `2026-10-01`? | Return `09:00` from `HOURS-CURRENT`, with its valid interval. |
| What office hours were valid on `2026-08-15`? | Return `08:00` from `HOURS-PAST`; do not replace it with the current value. |
| What event occurred during `[2026-09-15, 2026-09-25)`? | Return `EVENT-INSPECTION` because its occurrence date is `2026-09-20`, even though its record date is outside that interval. |
| What office hours are scheduled for `2026-11-01`? | Return `10:00` from `HOURS-FUTURE` as applicable to that future date; do not present it as valid on the anchor date. |
| On what exact day does maintenance start? | Report that the exact day is unknown and only the November 2026 window is known; do not invent a day or collapse the range to a point. |

The observations are local to this fixture. They exercise the protocol's existing temporal dimensions; they do not select a universal clock, temporal algebra, or valid-time model.

## ME-FORGET-001 — bounded forgetting, lineage gap and restoration probe

### Fixed input and declared scope

For this specimen only, the disposition target is source session `SESSION-A` and its **listed, known descendants**. The location inventory is complete for the named rows below but explicitly contains one cache candidate whose lineage is incomplete. This is a semantic-availability probe, not a physical- or cryptographic-erasure test.

```text
SESSION-A -> MEMORY-A -> INDEX-A -> CACHE-A
SESSION-B -> MEMORY-B -> INDEX-B -> CACHE-B     (unrelated positive control)
CACHE-UNKNOWN: candidate target cue present; source/derived-from link absent

Declared target scope: SESSION-A and its listed descendants.
Declared retained control: SESSION-B and its listed descendants.
```

Before disposition, the fixture query returns `MEMORY-A` for target A and `MEMORY-B` for the independent control. `CACHE-UNKNOWN` is recorded as a candidate surface with no verified lineage edge to `SESSION-A` or `MEMORY-A`.

### Probe and expected observations

Apply the fixture's `forget SESSION-A` request, then inspect the named source, derived-memory, index, and cache locations. Repeat target and positive-control queries after the declared restore/rebuild probe.

| Location / observation | Expected observation after disposition and restore/rebuild |
|---|---|
| `SESSION-A` | Absent or unavailable within the declared source location. |
| `MEMORY-A`, `INDEX-A`, `CACHE-A` | Absent or unavailable within their declared locations; the old known target chain is not returned after restore/rebuild. |
| `SESSION-B`, `MEMORY-B`, `INDEX-B`, `CACHE-B` | Remain available, and the positive-control query still returns `MEMORY-B`. |
| `CACHE-UNKNOWN` | Lineage remains `UNKNOWN` / `UNVERIFIED`; do not claim that it was deleted, retained as a descendant, or globally cleared without resolving the missing edge. |
| Scope-level conclusion | The known chain may be assessed only over the verified locations. Overall completeness remains `UNKNOWN` while `CACHE-UNKNOWN` is unresolved; absence from the known chain is not a global erasure claim. |

The no-resurrection observation is bounded to the known target identities and listed, verified locations: those identities must not be restored or returned by the post-disposition probe. The unresolved cache candidate remains an explicit epistemic gap, not evidence of either deletion or resurrection. No deletion mechanism, storage topology, or product runtime behavior is prescribed.

## Existing-scope mapping

- `ME-TEMP-001` supplies concrete inputs for the protocol's existing temporal stress-profile direction and the existing temporal distinctions; it does not add a temporal law.
- `ME-FORGET-001` supplies a concrete source/derived/index/cache probe for existing forgetting, lineage, deletion-durability, and resurrection-resistance evaluation directions; it does not claim H06 execution or add an erasure guarantee.

Neither specimen is registered as executable conformance evidence, changes a registry or status, or authorizes runtime expansion, H11 work, Canon promotion, or production claims.
