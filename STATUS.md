# Current Status

```yaml
document_role: CURRENT_STATE
status_as_of: 2026-08-09
authoritative_machine_source: project-state.json (nk-project-state/2)
live_head_source: GitHub API or checked-out Git ref
machine_truth_reconciliation_merge: d9eee591de308a689ace940c2efe58c9e8a137f2
human_truth_reconciliation_merge: 07549a0cd952b4e06b61ef24d21b2dcdbc9f861d
runtime_checkpoint: 675aa4b398a2fc0181dc71d38904a2d33a09f5f8
runtime_integrity_checkpoint: a1cdc6d8f36d67f40f065641809bc6da463c10a4
evidence_producing_checkpoint: 296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
notion_synchronized_through: 07549a0cd952b4e06b61ef24d21b2dcdbc9f861d
```

> **Repository status:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`
>
> A checkpoint is not automatically the live branch head. Live `main` must be resolved from GitHub or the checked-out Git ref. A later documentation or metadata commit does not silently broaden the proof scope of an earlier runtime or evidence checkpoint.

## Current state

```text
clean_runtime_support:       PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

P1–P5, C4 and C5 are merged in the clean implementation lineage. C5 is a bounded synthetic operational rehearsal, not a production deployment, live-data validation, compliance certification or authority promotion.

## Checkpoint roles

| Role | Checkpoint | Meaning |
|---|---|---|
| Machine truth reconciliation | `d9eee591de308a689ace940c2efe58c9e8a137f2` | PR #80 introduced `nk-project-state/2`, non-self-referential checkpoints and registry↔state consistency checks. |
| Human truth reconciliation | `07549a0cd952b4e06b61ef24d21b2dcdbc9f861d` | PR #81 separated current truth from history and proposals across public and AI-facing documentation. |
| Runtime | `675aa4b398a2fc0181dc71d38904a2d33a09f5f8` | ADR-0023 safe SQLite/Event runtime checkpoint. |
| Runtime integrity follow-up | `a1cdc6d8f36d67f40f065641809bc6da463c10a4` | PR #72 closed the post-merge integrity review findings. |
| Evidence producing | `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7` | C5 implementation evidence lineage. |
| Notion synchronized through | `07549a0cd952b4e06b61ef24d21b2dcdbc9f861d` | Current dashboard, decision/evidence/risk ledgers, sync log and historical archive reflect PRs #80–#81 and reconciled Issues #14–#17. |

These identities are intentionally different. No committed file attempts to contain the SHA of its own commit.

## Truth-surface reconciliation

```text
Phase 0A — machine-readable truth:  COMPLETE / PR #80
Phase 0B — human-readable truth:    COMPLETE / PR #81
Phase 0C — issues and Notion:       COMPLETE / REPOSITORY RECORD IN PROGRESS
```

Issues #14–#17 remain open. Each now distinguishes original scope, completed work, evidence boundary, remaining scope, next acceptance gate and non-goals. Notion preserves old chronology as historical material while routing current retrieval through dedicated current-state pages.

## Three independent tracks

| Track | Scope | Current state |
|---|---|---|
| `H` — Historical Recovery | authentic `v0.1.2.1` and original 44-test suite | `BLOCKED / ACTIVE EVIDENCE-RECOVERY`; not found in accessible sources |
| `C` — Clean Implementation | P1–P5, C4 and C5 | `ACTIVE / PARTIAL` |
| `R` — Long-Horizon Research | proposed future contracts, profiles and experiments | `PROPOSED / BOUNDED / NO AUTOMATIC PROMOTION` |

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
research proposal ≠ accepted contract ≠ runtime
```

Track H does not block Track C. Track R cannot obtain Canon or runtime status through prose.

## Durable evidence

Repository-resident evidence remains immutable under its original identities:

```text
evidence/c5/2026-08-07/manifest.json
evidence/c5/2026-08-08-adr0023/manifest.json
```

The retained archives prove only their declared environments, inputs, runs and bounded outputs. They do not prove live-user safety, independent custody, complete authenticity, physical deletion, operational equivalence or production readiness.

## Current gaps and decisions

| Boundary | State | Next gate |
|---|---|---|
| License and publication terms — Issue #18 | `OPEN / OPERATOR DECISION REQUIRED` | Choose a publication regime before external collaboration or package publication. |
| Reducer referential semantics — Issue #74 / ADR-0024 | `PROPOSED / NOT STARTED` | Explicit operator decision before reducer-v2 runtime work. |
| Semantic abstract machine and equivalence profiles | `PROPOSED` | Define NK-SAM and named equivalence profiles before independent implementation claims. |
| Event/history commitment | `INCOMPLETE` | Separate portable semantic commitment from operational/profile receipts before reducer-v2 histories. |
| NK-EPI-001…008 | `8 UNSUPPORTED` | Contract-first executable slices; operations alone cannot promote them. |
| Temporal semantics | `NOT IMPLEMENTED AS A COMPLETE CONTRACT` | Decide identity impact and valid/recorded/write-order semantics separately. |
| Admission lifecycle | `NOT IMPLEMENTED AS A COMPLETE PIPELINE` | Define policy, authority, scope and decision records without truth overclaim. |
| Operational deletion | `NOT ESTABLISHED` | Inventory locations, execution methods and bounded Receipts. |
| Independent cross-language conformance | `NOT ESTABLISHED` | Independent encoder/parser/reducer and declared equivalence evidence. |
| Production authorization | `false` | Deployment-specific threat model, operations, evidence and explicit operator GO. |

## Next authorized gate

```text
license decision options
→ ADR-0024 operator decision package
→ NK-SAM and equivalence contracts
→ Event/history commitment contract
→ only then reducer-v2 runtime work
```

Do not begin Temporal, executable NK-EPI, full Admission, operational deletion, full Rust/Go implementation or ecosystem integration before those gates.

## Explicit non-claims

```text
C5 PASS
≠ production readiness
≠ live-user-traffic validation
≠ full substrate neutrality
≠ independent language equivalence
≠ complete Event authenticity
≠ physical or cryptographic deletion
≠ compliance certification
≠ authority or truth promotion
≠ NK-EPI advancement
≠ recovered v0.1.2.1
```

## Historical record

Earlier detailed status chronology remains inspectable in Git history and in the following version-bound records:

- [`docs/ai/C5_IMPLEMENTATION_RECORD.md`](docs/ai/C5_IMPLEMENTATION_RECORD.md)
- [`docs/adr/0023-harden-sqlite-wal-and-event-integrity.md`](docs/adr/0023-harden-sqlite-wal-and-event-integrity.md)
- [`evidence/c5/README.md`](evidence/c5/README.md)
- [historical `STATUS.md` at publication checkpoint `626f34e…`](https://github.com/velantrian/velantrim-native-kernel/blob/626f34e6328b455258f2dd5fcf2145ec4db64a60/STATUS.md)

Historical reports are evidence of their exact checkpoints. They are not the authoritative current-state surface.