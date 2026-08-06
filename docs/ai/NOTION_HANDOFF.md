# 🔗 Native Kernel Notion Synchronization Hand-off Queue

This file preserves a complete public transfer package when an AI agent or contributor can work in GitHub but cannot access the Native Kernel Notion workspace.

A missing Notion connector is not a reason to abandon an audit, implementation or review.
GitHub must remain sufficient to understand technical state, verify evidence and continue the work.

## Access and synchronization states

| State | Meaning | Required action |
|---|---|---|
| `NOTION_AVAILABLE` | Actor can read/update intended record | Synchronize in the same work cycle |
| `HANDOFF_REQUIRED` | Actor lacks access | Complete GitHub and add structured item below |
| `SYNCED` | Connected actor verified evidence and updated Notion | Record safe reference and final evidence |
| `NOT_REQUIRED` | Correctly GitHub-only | State reason in PR |
| `BLOCKED_PRIVACY_OR_PERMISSION` | Real privacy/permission/target problem | Keep draft and escalate exact blocker |

A missing connector alone is `HANDOFF_REQUIRED`.

## GitHub completeness invariant

The following may never exist only in Notion:

- implemented behavior or changed technical contract;
- material audit/review finding;
- known engineering, security, privacy, epistemic or authority risk;
- exact PR/SHA/test/CI/benchmark/runtime evidence;
- durable decision;
- required next action or unresolved blocker.

## Connectorless actor procedure

1. Continue from GitHub.
2. Update affected technical documents and `docs/ai/` files.
3. Record exact base/head SHA, PR/issue, evidence, limitations and next actions.
4. Add a hand-off item for `GITHUB_AND_NOTION` work.
5. Set PR fields:
   - `Notion access: UNAVAILABLE`;
   - `Notion synchronization: HANDOFF_REQUIRED`;
   - `GitHub hand-off path: docs/ai/NOTION_HANDOFF.md#<anchor>`.
6. Never claim Notion was updated.

## Connected actor procedure

1. Verify the hand-off against current GitHub evidence.
2. Update the intended Notion record.
3. Preserve problem, decision, alternatives, boundaries, evidence, limitations and next actions.
4. Record safe Notion title/reference.
5. Mark item `SYNCED`.
6. Add final merge SHA and final evidence after merge.

## Privacy boundary

Native Kernel is public.
Do not copy private notes, personal information, secrets, private datasets or inaccessible private links into this file.
Use a safe page title or internal reference where necessary.

## Hand-off template

```markdown
## YYYY-MM-DD — Short title

- **Status:** `HANDOFF_REQUIRED` / `SYNCED` / `BLOCKED_PRIVACY_OR_PERMISSION`
- **Documentation impact:** `GITHUB_AND_NOTION`
- **Repository / PR / issue:**
- **Base SHA:**
- **Head SHA:**
- **Intended Notion record:** safe title or internal reference
- **Notion access for originating actor:** `UNAVAILABLE`

### Problem / opportunity
### Material findings
### Decision and rationale
### Rejected or deferred alternatives
### Canon, authority, safety, privacy and ecosystem boundaries
### GitHub files updated
### Evidence
### Known limitations
### Next actions

### Synchronization result
- Connected actor:
- Notion record:
- Status: `SYNCED`
- Final PR / merge SHA / CI:
```

## Queue

No pending hand-off items at the time this file was introduced.
