# 🔄 Code ↔ Documentation ↔ Notion Sync Protocol

This protocol makes documentation continuity part of the definition of done for Native Kernel.
A change is incomplete when code, contracts, current-state documentation, decision history, evidence and next actions describe different realities.

## 1. Roles of each surface

| Surface | Role | Authority |
|---|---|---|
| GitHub code and committed tests | Executable truth in their declared scope | Highest for implemented behavior |
| `STATUS.md` and current-state docs | Public implementation/evidence boundary | Must match verified repository state |
| Architecture, contracts and accepted ADRs | Durable semantic and governance decisions | Normative only in their declared status |
| Pull request | Proposed change, evidence and review discussion | Proposal until merged |
| `docs/ai/WORK_LOG.md` | Concise engineering chronology and hand-off | Operational history, not runtime proof |
| `docs/ai/NOTION_HANDOFF.md` | Connectorless synchronization queue | Transfer evidence, not implementation proof |
| Notion Native Kernel hub | Deeper rationale, roadmap, alternatives and cross-project history | Strategy/history; never overrides GitHub runtime evidence |

Notion may explain why a capability was proposed or changed.
It must not claim `implemented`, `tested`, `wired`, `enabled` or `observed` without exact GitHub evidence.

## 2. GitHub completeness invariant

An AI without Notion access must still be able to understand the project, audit it, verify evidence and continue work from GitHub alone.

The following may never exist only in Notion or chat:

- implemented behavior or a changed technical contract;
- a material audit or review finding;
- a known engineering, security, privacy, epistemic or authority risk;
- exact PR, SHA, test, CI, benchmark or runtime evidence required for review;
- a durable architectural decision;
- an unresolved blocker or required next action.

GitHub and Notion do not need sentence-for-sentence duplication.
GitHub carries the complete public technical and audit package; Notion carries deeper rationale, rejected alternatives, roadmap and historical evolution.
Both must preserve the same decision-bearing facts, status, evidence, limitations and next actions.

## 3. Documentation impact classes

Every PR selects one class.

### `NONE`

Use only when behavior, contracts, architecture, risks, source-recovery state, user guidance and project intent are unchanged.
The PR must state why no documentation update is needed.

### `GITHUB_ONLY`

Use when the public technical record changes but no deeper project decision or roadmap context is introduced.
Examples: typo correction, broken link, clarified command, narrow risk correction or formatting with unchanged meaning.

### `GITHUB_AND_NOTION`

Required when a change affects:

- Architecture Canon, contracts, profiles, authority, safety, privacy or epistemic boundaries;
- source-recovery state, provenance, Issue #1 or executable evidence;
- a new technology, module, capability, integration direction or implementation profile;
- runtime wiring, activation posture, deployment model or operational workflow;
- a durable decision with alternatives or trade-offs;
- roadmap, project meaning or cross-project boundaries;
- a material audit that changes priorities or accepted risk.

## 4. Notion access states

| State | Meaning | Required action |
|---|---|---|
| `NOTION_AVAILABLE` | Actor can access the intended record | Update GitHub and Notion in the same work cycle |
| `HANDOFF_REQUIRED` | Actor lacks access | Complete GitHub and add a structured hand-off item |
| `SYNCED` | Connected actor verified evidence and updated Notion | Record safe reference and final evidence |
| `NOT_REQUIRED` | Correctly GitHub-only | State the reason in the PR |
| `BLOCKED_PRIVACY_OR_PERMISSION` | Real privacy, permission or target ambiguity prevents safe sync | Keep draft and escalate exact blocker |

A missing connector alone is `HANDOFF_REQUIRED`, not a privacy blocker.

## 5. Mandatory workflow

### Before editing

1. Read `AGENTS.md`, this context pack, `STATUS.md`, relevant ADRs and affected artifacts.
2. Establish exact base SHA and distinguish `main`, open PR, external checkpoint, proposal and implemented scope.
3. Read the related Notion record for `GITHUB_AND_NOTION` when available.
4. When unavailable, continue from GitHub and plan a hand-off.

### During work

1. Record material findings, assumptions, decisions, alternatives and rejected paths.
2. Keep status language exact.
3. Update public GitHub technical documents in the same branch.
4. Do not leave important conclusions only in chat or private scratchpads.
5. Preserve English/Russian semantic parity for paired documents.

### Before review

Update as applicable:

- `STATUS.md` and `CURRENT_STATE.md`;
- `KNOWN_RISKS.md`;
- `COMPONENT_MAP.md`;
- `WORK_LOG.md`;
- ADR/RFC;
- security, conformance, profile, integration, roadmap and user-facing documents;
- Notion record or `NOTION_HANDOFF.md`.

Complete the PR synchronization block and confirm GitHub is sufficient without Notion.

### After merge

For `GITHUB_AND_NOTION`, record:

- final PR and merge SHA;
- final tests/CI/evidence;
- deviations from the initial plan;
- remaining limitations and next actions;
- final synchronization status.

## 6. Required deep Notion record

A substantial record should contain:

1. Problem or opportunity
2. Intended function
3. Decision and rationale
4. Alternatives rejected or deferred
5. Implementation or audit summary
6. Canon, authority, safety, privacy and cross-project boundaries
7. Evidence: PR, issue, SHA, tests, CI and measurements
8. Reality status: documented / proposed / accepted / implemented / tested / wired / enabled / observed
9. Known limitations
10. Difference from the initial plan
11. Next actions

## 7. Public/private boundary

The repository is public.
Do not copy private workspace notes, personal information, secrets, private datasets or inaccessible private links into GitHub.
Privacy does not justify omitting the public contract, evidence, limitations or next actions.

## 8. Completion rule

```text
material change
+ focused validation and exact evidence
+ complete public GitHub technical/audit record
+ direct Notion synchronization or structured hand-off
+ final PR/SHA/status/limitations
= change complete
```

A checked box without corresponding content is not synchronization.
An accepted ADR is not implementation evidence.
A merged change with stale public documentation is not finished.
