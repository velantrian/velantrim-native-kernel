# 🧾 Native Kernel AI Engineering Work Log

This is a concise chronology and hand-off surface.
Re-verify exact SHAs, PR state and current repository evidence before using an entry as present reality.

---

## 2026-08-06 — Exact contract and executable fixture proposal for Issues #14–#17

```text
Status:          DRAFT PR / PROPOSED / LOCAL VALIDATION PASS / NOTION SYNCED
PR:              #35
Base main:       c7610bc42fbc879c24e1a3a1408ebfaae1ac7340
Branch:          agent/contracts-14-17
Head at PR open: bd8cbdb70ebd0df21dc3ac5ed9f36e3b155f3c73
Scope:           architecture contracts + fixture-integrity support tooling
Runtime:         unchanged; no Native Kernel implementation added
Decisions:       ADR-0011…0014 PROPOSED; operator approval PENDING
Notion impact:   GITHUB_AND_NOTION → PROPOSAL SYNCED
Notion record:   Exact Contracts & Conformance Fixtures — PR #35
Issue #1 impact: NONE
```

The PR turns the remaining ADR-0010 architecture track into a reviewable package:

- `nk-id/1.0-proposed` — NFC UTF-8 compact sorted JSON subset, identity domains, collision/migration rules;
- `nk-event/1.0-proposed` — single-writer append/idempotency/order/replay boundary;
- `nk-deletion/1.0-proposed` — restriction, logical erase, physical deletion and crypto-erasure lifecycle;
- `nk-fixtures/1.0-proposed` — assertion registry, schemas, fixtures and external adapter protocol.

Artifacts:

- bilingual `docs/contracts/NORMATIVE_CONTRACTS_V1*`;
- ADR-0011 through ADR-0014;
- `contracts/registry.json` with 72 unique assertion IDs;
- schema bundle plus standalone evidence-report schema;
- identity/event/idempotency/deletion/epistemic fixture corpora;
- `tools/conformance/runner.py` and guide;
- `tests/test_conformance_runner.py`;
- proposed Python 3.11/3.12 fixture-integrity workflow.

Local authoring validation after manual hardening review:

```text
Focused unit tests:          8 PASS
Unique assertion IDs:        72
Assertion result coverage:   72 explicit statuses; no silent skip
Identity golden vectors:     2 matched
Identity invalid vectors:    4 rejected
Event chain scenarios:       2 validated
Idempotency scenarios:       2 validated
Deletion scenarios:          2 validated
NK-EPI-001…008:              positive + negative fixture for each
Reported runtime support:    UNSUPPORTED
Evidence level:              LOCALLY_TESTED
```

Manual review found and fixed three actionable gaps before merge:

1. stored `payload_hash` was not compared directly;
2. idempotency semantics lacked dedicated executable scenarios;
3. adapter reports did not require complete assertion coverage.

Hardening now rejects payload-hash tampering, incomplete assertion sets, duplicate assertion results and silent skips.

Evidence boundary:

```text
local fixture PASS
≠ operator acceptance
≠ repository-reproduced C2
≠ Kernel runtime
≠ C3 cross-profile equivalence
≠ production deletion or security evidence
```

No new event verb is accepted. Issue #1 remains separate. Titan, Mentaury and Crystal receive no inherited authority or runtime wiring.

GitHub↔Notion:

- deep Notion record created under Core Architecture;
- Hub block records Draft PR #35, base main and head at creation;
- public main remains unchanged;
- GitHub remains technically sufficient without Notion.

CI nuance:

The new workflow does not exist in the base branch, so no PR run appeared for it. The package may be merged while retaining `PROPOSED` decision status. A subsequent main-push run can establish repository evidence only for fixture-integrity tooling. Merge does not equal operator acceptance.

Remaining gates:

1. final diff/review-thread check;
2. publish/merge the proposal package with statuses unchanged;
3. inspect and record exact main-push workflow evidence;
4. obtain a separate explicit operator decision on ADR-0011…0014;
5. keep runtime adoption and independent-profile C3 as future work.

---

## 2026-08-06 — Foundational contract skeleton accepted and merged

```text
Status:          MERGED / ADR ACCEPTED / NOTION SYNCED
PR:              #28
PR head:         f67e2b632772cab068207177514f1f873f074e4b
Merge SHA:       2d42a1517ba87b39d2395aa5c22b966328615305
Decision:        ADR-0010 ACCEPTED / APPROVED
Runtime:         unchanged
```

Accepted the six-family ownership map `NK-SEM`, `NK-ID`, `NK-EVT`, `NK-AUT`, `NK-CFL`, `NK-EQV`. No schemas, runtime behaviour, C1–C5 evidence or portability were established.

---

## 2026-08-06 — AI context freshness guard

```text
Status:          MERGED / CI VERIFIED / NOTION SYNCED
PR:              #26
Merge SHA:       099ae235ff935948348f2101804eb53ac9eeae1a
Scope:           support tooling / CI / documentation governance
```

Added mandatory-file, selected-link, checkpoint existence/ancestry and status-boundary checks on Python 3.11/3.12. Six isolated tests and exact-head/main-push runs passed. The guard does not prove semantic freshness or Notion synchronization.

---

## 2026-08-06 — AI context and documentation-continuity governance

PR #24 → `d5989742f987b610b5a81bb59a14c0a11518aeea`. Introduced `AGENTS.md`, `docs/ai`, risk/work logs, audit playbook, PR documentation gate and GitHub↔Notion protocol. No runtime claim was added.

---

## 2026-08-06 — Ecosystem roles clarified

PR #23 → `18ee09c870f7416932de29a2b2f5de53202fcb2e`. Added role/navigation boundaries for Native Kernel, Mentaury, Titan and Crystal.

---

## 2026-08-06 — Storage profile documentation visualized

PR #22 → `fa8b2d9356486d6d78074e8bd6eb3b14ebfd2249`. Added bilingual architecture maps; no runtime implementation.

---

## 2026-08-06 — PostgreSQL/SQLite profile direction accepted

PR #21; PostgreSQL preferred full profile and SQLite optional embedded profile. Implementation remains `NOT_STARTED` and storage neutrality unproven.

---

## Continuing rule

Add an entry for significant work that changes project state/evidence, Canon/contracts, ADR/RFC, source recovery, profiles, integration boundaries, known risks or AI continuity. Include exact PR/SHA, scope, evidence, limitations, Notion state and next action.
