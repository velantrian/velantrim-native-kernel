<!-- H11_EXECUTION_ADMISSION_BLOCKED_CURRENT -->
# ⚠️ Native Kernel Known Risks and Required Proof

This file is an **active-risk register**. It does not preserve every historical risk checkpoint inline; historical findings remain in their original reviews, research records, `STATUS.md`, `ROADMAP.md`, work/reconciliation logs, evidence and Git history.

```yaml
document_role: ACTIVE_RISKS
status_as_of: 2026-08-15
authoritative_machine_source: ../../project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
selected_family: A10-H11
current_gate: A10_H11_EXECUTION_ADMISSION
admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
reviewer_reproducer: NOT_ESTABLISHED
h11_outcome: NOT_TESTED
runtime_expansion: FROZEN
production_authorized: false
```

## Risk-state vocabulary

```text
OPEN                 unresolved technical, governance or evidence risk
MITIGATED            bounded control exists; residual risk remains
CLOSED               exact finding corrected and repository-verified
HISTORICAL_BOUNDARY  retained evidence remains valid only for original version/scope
PROPOSED             research or decision work, not runtime protection
```

## 🔴 P0 — False independence / self-certification

**State:** `OPEN / CURRENT H11 BLOCKER`.

H11 requires a genuinely qualifying `INDEPENDENT_SEMANTIC_ORACLE`. The current qualification record for the existing Codex reviewer remains `NOT_ESTABLISHED` because shared custody/self-review and organizational-independence concerns remain material.

```text
CI success
≠ independent review
owner/self review
≠ independent review
LLM agreement / model change / same-agent relabeling
≠ independent review
Notion read-back
≠ independent review
```

PR #131 remains the external review surface. Do not merge it merely because the branch is mergeable or CI is green. A future qualifying reviewer/reproducer still requires a separate `A10_H11_EXECUTION_ADMISSION` reassessment before any execution.

## 🔴 P0 — Formal Authority misrouting / stale first-draft interpretation

**State:** `MITIGATION IN PROGRESS / MUST REMAIN FAIL-CLOSED`.

A1–A10 are preserved first-draft provenance, but IAR-1-R1 deliberately narrowed several first-draft structures. Any reading route that stops at A1–A10 can therefore overstate the current provisional architecture.

Required authority chain:

```text
ARCHITECTURE.md
→ A1–A10 first-draft provenance
→ Integrated A1–A10 Review
→ IAR-1
→ IAR-1-R1 reconciliation
→ later accepted ADR / operator decisions for their explicit scope
```

Where first-draft wording conflicts with IAR-1-R1, the reconciliation is the current provisional interpretation. Final Canon remains deferred.

## 🔴 P0 — Historical/current state confusion

**State:** `MITIGATION IN PROGRESS`.

Historical D5/D6/D7/D8, ADR-0027, RAVP, selection and preregistration records contain values that were once current. Requiring those literal values inside current-only AI surfaces creates a retrieval hazard even when a newer overlay exists.

Current-only surfaces must therefore carry current H11 state, while chronology remains in designated history/evidence surfaces.

```text
historical NEXT
≠ current next gate
historical NOT_STARTED
≠ current state
old Notion checkpoint
≠ live GitHub HEAD
```

## 🔴 P0 — Production / semantic overclaim

**State:** `OPEN`.

```text
repository status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production: false
```

C5, BPV1 and any scoped A10 support do not imply production readiness, universal architecture proof or arbitrary-substrate support.

## 🔴 P0 — Reference implementation may capture architecture authority

**State:** `MITIGATED / RESIDUAL OPEN`.

Controls already present:

- P1–C5 is `BOUNDED_REFERENCE_LABORATORY`;
- IAR-1-R1 demoted over-shaped taxonomies from universal minimum to reference structures;
- BPV1/H11 separate mechanism-level laboratory dependencies from meaning-level obligations;
- runtime remains frozen;
- Final Canon remains deferred.

Residual risk remains because the same repository and conventional digital machinery still dominate most evidence. Cross-language evidence is not independent computation-model proof.

## 🔴 P0 — Reducer referential semantics remain incomplete

**State:** `OPEN / ISSUE #74 / ADR-0024 PENDING / RUNTIME FROZEN`.

Reducer v1 historically permits referential cases that a stricter future policy may reject, including dangling/unknown references and insufficiently constrained supersession relations. This is a real contract gap.

Do **not** repair reducer v1 in place: that would reinterpret historical P1–C5 evidence. Any stricter semantics require the existing operator-controlled versioning/ADR path.

## 🔴 P0 — Physical / cryptographic erasure is not established

**State:** `OPEN`.

Logical restriction/`ERASED` in the semantic system does not prove physical deletion, cryptographic erasure or global forgetting.

The reconciled architecture distinguishes:

1. logical disposition claim;
2. substrate-condition claim under a threat/observation boundary;
3. epistemic accessibility / forgetting-loss claim.

Do not upgrade one layer into another without the required evidence and Authority boundary.

## 🔴 P0 — License and contribution rights are unresolved

**State:** `OPEN / ISSUE #18 / OPERATOR DECISION REQUIRED`.

```text
public repository
≠ open-source license
```

No AI agent may choose the license, contribution regime, patent/trademark terms or recovered-source rights on behalf of the operator.

## 🔴 P0 — Historical and clean lineages may be collapsed

**State:** `OPEN / GOVERNANCE BOUNDARY`.

```text
clean P1–P5 + C4 + C5
≠ recovered v0.1.2.1
≠ original 44-test evidence
NOT_FOUND_IN_ACCESSIBLE_SOURCES
≠ GLOBALLY_LOST
```

Issue #1 remains independent and Track H source admission remains operator-controlled.

## 🟠 P1 — H11 qualification evidence must be operationally bindable

**State:** `OPEN / PRE-EXECUTION OPERATIONAL RISK`.

The fail-closed qualification contract correctly prevents repository-local self-certification. When a genuine external reviewer/reproducer appears, the repository must be able to bind the externally authenticated review identity/evidence into the existing qualification record without weakening the frozen criteria.

This is not permission to invent a substitute reviewer or a new gate. It is a requirement that the existing PR #131 → qualification record → admission reassessment path remain executable.

## 🟠 P1 — Independent implementation/substrate evidence remains limited

**State:** `PARTIAL`.

BPV1 provides bounded cross-language evidence, but:

```text
independent team: NOT_ESTABLISHED
independent custody: NOT_ESTABLISHED
independent computation model: NOT_ESTABLISHED / CONVENTIONAL_DIGITAL
```

PostgreSQL↔SQLite is bounded storage/profile evidence inside the same Python semantic lineage. Neither result proves arbitrary future-substrate support.

## 🟠 P1 — Composition/federation remains a separate capability class

**State:** `OPEN / OUTSIDE CURRENT H11 SCOPE`.

```text
local scoped conformance
≠ composition/federation conformance
A10-H11
≠ composition/federation
```

Do not import composition authority from Titan, Crystal, Mentaury or another project into Native Kernel.

## 🟠 P1 — Evidence/checkpoint identity can be misread after squash merges

**State:** `MITIGATED / RESIDUAL PROCESS RISK`.

PR #138 repaired one post-squash evidence anchor. The general distinction remains important:

```text
pre-merge candidate identity: exact PR head
post-merge authoritative repository identity: main-reachable merge/commit + verified bytes/digest
```

A PR-head SHA must not be silently treated as the durable main-reachable evidence anchor after a squash merge.

## 🟠 P1 — Notion projection can drift or duplicate volatile state

**State:** `OPEN / DOCUMENTATION PROCESS RISK`.

Notion is a human/navigation projection, not a stronger authority than GitHub. Different pages have different roles; copying the same live SHA/gate block into every page creates synchronization churn and another source of stale truth.

Use role-specific updates and read-back. The GitHub Sync Log owns detailed synchronization chronology; Current State owns current state; Core Architecture owns architecture meaning; Roadmap owns active order/gates; Active Risks owns risks; AI Context owns continuation/routing.

## 🟡 P2 — Local SQLite environment may be unable to execute P5 safely

**State:** `EXPECTED ENVIRONMENT LIMITATION / NOT A REASON TO LOWER THE SAFETY FLOOR`.

The SQLite profile intentionally fails closed below the evidenced WAL-safe floor. CI builds the pinned safe SQLite version. A local environment with an older linked SQLite may therefore be `NOT_EXECUTED` for affected P5 tests rather than a Kernel regression.

Do not weaken the WAL safety floor merely to make an unsafe local environment green.

## Required non-claims

```text
bounded evidence ≠ universal proof
cross-language ≠ independent computation model
repository-visible ≠ independent custody
logical ERASED ≠ physical deletion
physical deletion ≠ global forgetting
Final Canon deferred ≠ architecture absent
runtime frozen ≠ research stopped
Notion synchronized ≠ H11 qualified
CI green ≠ independent validation
```
