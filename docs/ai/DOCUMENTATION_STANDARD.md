# 📚 Velantrim Documentation Standard v2

`overview != current state != evidence != history`

This standard defines how Native Kernel documentation must serve **two different readers** without creating two different truths.

## 1. Audience split

### 👤 Human landing surfaces

- `README.md` — English human-first landing page.
- `README.ru.md` — Russian human-first landing page.
- `PROJECT_OVERVIEW.md` — stable deep human explanation.
- `PROJECT_OVERVIEW.ru.md` — stable deep human explanation in Russian.

Human surfaces should optimize for:

- comprehension before chronology;
- explanation before SHA inventories;
- diagrams, trees, mindmaps, tables and examples where they clarify;
- explicit limitations rather than marketing overclaim;
- links outward to detailed current-state and formal documents.

The root README must **not** become a long-running status ledger. Volatile technical chronology belongs in `STATUS.md`, `ROADMAP.md`, research/evidence records, and machine-state surfaces.

### 🤖 Machine / agent surfaces

- `docs/ai/README.md` — mandatory AI/agent entrypoint and reading order.
- `AGENTS.md` — operating constraints and authority boundaries.
- `project-state.json` — machine-readable repository state.
- `docs/ai/CURRENT_STATE.md` — layered current-state context.
- affected contracts, ADRs, research records and evidence — task-specific authoritative inputs.

Machine surfaces should optimize for:

- deterministic reading order;
- exact vocabulary;
- explicit authority and prohibition boundaries;
- machine-readable state;
- checkpoint identities and evidence bindings;
- minimal decorative prose.

An AI agent must not infer authorization from human-friendly presentation text when a machine/current-state surface exists.

## 2. Authority rule

Presentation never creates authority.

```text
human explanation
        │
        ├── may summarize
        ├── may visualize
        └── may link
             │
             ▼
current-state / machine / evidence surfaces
             │
             └── own the authoritative technical claim
```

For volatile state:

- live GitHub ref resolves current repository head;
- `project-state.json` owns machine-readable project state;
- `STATUS.md` owns the primary human status summary;
- `docs/ai/README.md` owns AI reading order;
- evidence/contract records own their scoped claims.

## 3. Update classes

### `STRUCTURAL_CHANGE`

Use when the conceptual system changes: new architecture layer, changed ontology, new authority boundary, changed relationship between Canon/lab/evidence, or another modification that changes how the project should be understood.

Required action:

1. review both root READMEs;
2. review both Project Overviews;
3. update relevant mindmap/tree/ASCII/diagram/table representations;
4. update `docs/ai/README.md` only if machine reading order or authority changes;
5. update formal architecture/current-state surfaces that actually own the new truth;
6. preserve bilingual parity.

A structural change must not leave the human visual model describing an obsolete architecture.

### `STATE_CHANGE`

Use when a gate, authorization, selected family, result, runtime state or other current status changes without changing the conceptual architecture.

Required action:

1. update authoritative current-state/machine surfaces;
2. refresh the small current-boundary block in root READMEs if its meaning changed;
3. do **not** rewrite stable explanatory diagrams merely because a PR number or SHA changed;
4. synchronize Notion only when the existing governance rules require a semantic state sync.

### `EVIDENCE_ONLY`

Use when a PR, test run, evidence bundle, review comment or checkpoint adds support without changing the architecture or current semantic state.

Required action:

- update evidence/history/status surfaces as appropriate;
- avoid visual churn in README/Overview;
- do not manufacture a new architecture claim.

## 4. Visual roles

Use visual forms deliberately:

- **Mindmap** → relationships between concepts.
- **ASCII flow** → transformation / authority / information flow.
- **Tree** → what exists and how it is grouped.
- **Mermaid diagram** → architecture or process topology.
- **Table** → comparison, boundary, status or may/must-not distinctions.
- **Commentary callout** → why a distinction matters.

Emojis are presentation metadata for humans. They must never carry a semantic distinction that is absent from the text.

## 5. Comparison rule

Human documentation may compare Native Kernel with other systems, but comparisons must be scoped to **declared goals and architecture roles**, not unsupported superiority claims.

Prefer:

> “These systems solve different layers of the problem.”

Avoid:

> “Native Kernel is better than X.”

If a comparison depends on an external project's current behavior, verify it against the project's primary documentation before updating the table.

## 6. Anti-drift rules

Do not:

- duplicate a volatile live SHA into multiple human explanation pages without a validator-backed reason;
- copy an aggregate experiment result onto hypotheses that were not adjudicated;
- present a bounded laboratory mechanism as universal Canon;
- convert CI success, owner review, bot review or local identity into independent evidence;
- turn historical `NEXT` markers into current instructions;
- remove historical validator bindings merely to make a page shorter;
- keep a stale human visual summary after a real structural architecture change.

Prefer collapsible historical sections when a validator requires old role/checkpoint text that would otherwise dominate the landing page.

## 7. Maintenance contract for AI agents

Before writing documentation, classify the change as `STRUCTURAL_CHANGE`, `STATE_CHANGE`, or `EVIDENCE_ONLY`.

If `STRUCTURAL_CHANGE`:

```text
formal truth changed
      ↓
update authoritative architecture/current-state source
      ↓
update machine reading surface if needed
      ↓
update Human Overview
      ↓
update README visual summary
      ↓
validate bilingual + AI-context + reconciliation
```

If `STATE_CHANGE`, update the current truth without redesigning the whole page.

If `EVIDENCE_ONLY`, preserve the high-level presentation unless the new evidence changes what the project can legitimately claim.

The goal is:

```text
one repository truth
      │
      ├── 👤 human interface: understandable
      └── 🤖 machine interface: precise
```
