# 📚 Velantrim Documentation Standard v5

`formal architecture != human presentation != agent instructions != machine state != evidence/history`

Native Kernel maintains **one project truth through an explicit authority core plus several deliberately different representations and evidence surfaces**. These layers serve different readers and authority needs; they are not competing truths.

```text
                         🧬 ONE PROJECT TRUTH
                                  │
                                  ▼
                     🏛 FORMAL AUTHORITY CORE
              meaning · invariants · contracts · decisions
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
         👤 HUMAN VIEW       🤖 AGENT VIEW       ⚙ MACHINE STATE
       README / OVERVIEW      docs/ai/**         JSON / YAML state

      🔬 EVIDENCE / HISTORY ── supports / challenges ──▶ 🏛 AUTHORITY CORE
      tests · research · reviews · falsification · checkpoints
```

The direction matters:

- the **Formal Authority Core** owns declared project meaning, invariants and accepted architecture-level decisions;
- Human, Agent and Machine surfaces present or constrain that truth for different consumers;
- Evidence/history can support, weaken, refute or trigger reassessment of authority claims, but **does not auto-promote itself into authority**.

## 1. Layer roles

### 🏛 Formal Architecture / Authority Core

Primary surfaces include:

- `ARCHITECTURE.md` — top-level formal architecture entrypoint;
- the owning A1–A10 architecture documents under `docs/`;
- accepted ADRs / operator decisions where the repository explicitly designates them as architecture authority;
- formal contracts and invariants whose owning documents are named by the architecture/current-state surfaces.

The Authority Core answers:

> **What is the system declared to mean, preserve, distinguish, forbid or require?**

It should optimize for:

- stable semantic definitions;
- explicit invariants and ownership boundaries;
- technology-neutral contracts where the architecture claims neutrality;
- explicit status of provisional vs accepted vs deferred claims;
- precise links to evidence without turning evidence machinery into Canon;
- explicit decision authority for changes to architecture meaning.

The Authority Core is **not** a presentation layer and is **not** the same thing as current runtime state. A formal architecture contract may remain stable while a gate, experiment, implementation or runtime authorization changes.

### 👤 Human view

Primary surfaces:

- `README.md` — English human-first landing page.
- `README.ru.md` — Russian human-first landing page.
- `PROJECT_OVERVIEW.md` — stable deep human explanation.
- `PROJECT_OVERVIEW.ru.md` — stable deep human explanation in Russian.
- `docs/COMPARISONS.md` / `docs/COMPARISONS.ru.md` — dated, source-backed external comparison surfaces.

Human surfaces should optimize for:

- comprehension before chronology;
- explanation before SHA inventories;
- visual forms only when each answers a distinct question;
- explicit limitations rather than marketing overclaim;
- links outward to formal architecture, current-state, machine and evidence documents.

The root README should be a **3–7 minute orientation surface**, not a long-running status ledger. It may contain one compact comparison matrix when that matrix materially improves human comprehension, but the detailed caveats and source ledger belong in `docs/COMPARISONS*`. Volatile technical chronology belongs elsewhere.

Human presentation may summarize formal architecture, but **does not create or modify architecture authority by itself**.

### 🤖 Agent view

Primary surfaces:

- `docs/ai/README.md` — mandatory AI/agent entrypoint and reading order.
- `AGENTS.md` — operating constraints and authority boundaries.
- `docs/ai/CURRENT_STATE.md` — layered current-state context.
- affected contracts, ADRs, research records and evidence — task-specific authoritative inputs.

Agent surfaces should optimize for:

- deterministic reading order;
- exact vocabulary;
- explicit authority and prohibition boundaries;
- checkpoint identities and evidence bindings;
- minimal decorative prose;
- explicit `never infer` boundaries where ambiguity is dangerous.

An AI agent must not infer architecture authority or runtime authorization from human-friendly presentation text. When meaning is in question, follow the named Formal Authority Core. When volatile state is in question, follow current-state/machine authority.

### ⚙ Machine state

Primary surfaces:

- `project-state.json` — machine-readable repository state.
- `docs/ai/project_manifest.yaml` — documentation-routing manifest.
- validator- and contract-owned JSON/YAML records where applicable.

Machine surfaces should optimize for exact fields, schemas, status semantics and deterministic validation. Emojis and narrative are unnecessary here.

Machine state answers:

> **What exact state, gate, authorization, binding or routing value is currently asserted in machine-readable form?**

Machine state can encode the current status of architecture work, but a field value does not silently redefine the meaning of a formal architecture contract unless the owning authority process says it does.

### 🔬 Evidence / history

Primary surfaces include:

- `STATUS.md` and `ROADMAP.md` for current/historical human status context;
- `evidence/**`;
- `docs/research/**`;
- tests, review artifacts, evaluation reports, reproductions, falsification records and historical checkpoints;
- ADR/review history when it is evidence for a decision rather than the accepted decision authority itself.

Evidence/history surfaces preserve chronology, scoped claims and falsification records. They can justify reassessment, but they must not be promoted into architecture authority merely because they are detailed, recent or green.

The evidence layer answers:

> **Why do we have reason to support, weaken, refute, defer or revisit a claim?**

## 2. Authority rule

Presentation never creates authority, and evidence never auto-promotes itself into authority.

```text
🔬 evidence / falsification
          │
          │ supports · weakens · refutes · triggers reassessment
          ▼
🏛 formal architecture / accepted decisions
          │
          ├── summarized for humans
          ├── constrained for agents
          └── represented as exact current state where applicable
```

Use the owning layer for the question being asked:

| Question | Owning layer |
|---|---|
| What does the architecture mean or require? | 🏛 Formal Authority Core |
| How should a person understand it? | 👤 Human view |
| How must an AI read/work with it? | 🤖 Agent view |
| What is the exact current gate/state/binding? | ⚙ Machine/current-state surfaces |
| What evidence supports or challenges the claim? | 🔬 Evidence/history |

For volatile state:

- live GitHub ref resolves current repository head;
- `project-state.json` owns machine-readable project state;
- `STATUS.md` owns the primary human status summary;
- `docs/ai/README.md` owns AI reading order;
- evidence/contract records own their scoped observations and results.

For stable architecture meaning:

- `ARCHITECTURE.md` and its named owning architecture documents are the formal entrypoint;
- accepted ADRs/operator decisions own only the scope explicitly assigned to them;
- README/Overview diagrams are explanatory projections and must follow, not override, formal architecture.

## 3. Update classes

### `STRUCTURAL_CHANGE`

Use when the conceptual system changes: new architecture layer, changed ontology, new authority boundary, changed relationship between Canon/lab/evidence, or another modification that changes how the project should be understood.

Required action:

1. update the **owning Formal Authority Core** first;
2. review both root READMEs;
3. review both Project Overviews;
4. update only the visual representations whose function changed;
5. update `docs/ai/README.md` only if machine reading order or authority changes;
6. update current-state/machine routing surfaces when their representation of the changed architecture is affected;
7. preserve bilingual parity;
8. preserve evidence/history rather than rewriting it to match the new conclusion.

A structural change is incomplete if formal architecture changed but Human/Agent/Machine projections still describe the old model.

### `STATE_CHANGE`

Use when a gate, authorization, selected family, result, runtime state or other current status changes without changing the conceptual architecture.

Required action:

1. update authoritative current-state/machine surfaces;
2. refresh the small current-boundary block in root READMEs if its meaning changed;
3. do **not** rewrite stable formal architecture or explanatory diagrams merely because a PR number, SHA or gate value changed;
4. synchronize Notion when the existing governance rules require a semantic state sync.

### `EVIDENCE_ONLY`

Use when a PR, test run, evidence bundle, review comment or checkpoint adds support without changing architecture meaning or current semantic state.

Required action:

- update evidence/history/status surfaces as appropriate;
- avoid visual churn in README/Overview;
- do not manufacture a new architecture claim;
- do not edit the Formal Authority Core unless the evidence actually causes a governed architecture reassessment.

## 4. Visual grammar

Use visual forms deliberately. Each should answer a different question:

- **Mindmap** → which major concepts exist and how they relate. Keep it compact enough for mobile reading.
- **ASCII flow** → transformation / authority / information flow.
- **Tree** → what exists and how it is grouped.
- **Mermaid diagram** → architecture or process topology.
- **Table** → comparison, boundary, status or may/must-not distinctions.
- **Commentary callout** → why a distinction matters.

Do not keep two large visualizations in the root README if they communicate essentially the same information. Move deeper or alternative representations to the Overview instead.

Emojis are **visual grammar for humans**, not authority. Suggested stable meanings include:

- 🧠 concept / knowledge
- 🏛 formal architecture / authority core
- 🛡 authority / safety boundary
- 🧪 experiment / laboratory
- ✅ implemented or established for the stated scope
- 🟡 research / incomplete / conditional
- ❌ unavailable / not authorized when the text says so
- 📜 historical
- 🤖 agent / AI
- 👤 human
- ⚙ machine state
- 🔬 evidence / falsification

The text must remain understandable if emoji rendering is removed.

## 5. External comparison rule

The root README may contain **one compact, source-safe comparison matrix** when it helps a human understand architectural positioning. The matrix should normally keep systems in columns and criteria in rows so that each criterion can be scanned across approaches. The detailed explanation belongs in:

- `docs/COMPARISONS.md`
- `docs/COMPARISONS.ru.md`

Every substantive external comparison must:

1. carry a **Last source check** date in the detailed comparison document;
2. cite primary or canonical sources;
3. distinguish a source-backed positive claim from an absence claim;
4. prefer conditional / scoped wording over unsupported statements such as “system X cannot do Y”;
5. distinguish **design target** from **proven universal property** — especially for Native Kernel’s substrate/model/storage independence;
6. avoid superiority language unless supported by an explicit, reproducible evaluation with matching scope;
7. correct attractive but false simplifications when primary sources contradict them;
8. be re-checked when an external project changes materially.

Examples of comparison hygiene:

- if a project explicitly claims model-agnostic operation, do not label it “low resilience to LLM replacement” without narrower evidence;
- if a graph system supports incremental updates, do not claim restart necessarily requires a complete rebuild;
- if a persisted retrieval index survives process restart, do not describe plain RAG as losing that index merely because conversational state is out of scope;
- if event sourcing uses projections/materialized views/snapshots, do not imply every recovery path must replay the complete history from genesis;
- do not write that Native Kernel “preserves everything”; write that declared obligations are intended to survive a **conforming** replacement, with loss/change made explicit, and keep evidence scope visible.

Prefer:

> “These systems solve different layers of the problem.”

Avoid:

> “Native Kernel is better than X.”

A comparison document is a human orientation aid. It does not create Native Kernel evidence, architecture authority or current-state truth.

## 6. Anti-drift rules

Do not:

- duplicate a volatile live SHA into multiple human explanation pages without a validator-backed reason;
- copy an aggregate experiment result onto hypotheses that were not adjudicated;
- present a bounded laboratory mechanism as universal Canon;
- convert CI success, owner review, bot review or local identity into independent evidence;
- turn historical `NEXT` markers into current instructions;
- remove historical validator bindings merely to make a page shorter;
- keep a stale human visual summary after a real structural architecture change;
- leave a dated external comparison undated after materially changing its claims;
- let README wording override the owning formal architecture;
- let machine-state convenience fields silently redefine architecture meaning;
- treat a passing experiment, review or evidence bundle as an accepted architecture decision without the owning gate.

Prefer collapsible historical or machine-detail sections when validators require text that would otherwise dominate the human landing page.

## 7. Maintenance contract for AI agents

Before writing documentation, classify the change as `STRUCTURAL_CHANGE`, `STATE_CHANGE`, or `EVIDENCE_ONLY`.

If `STRUCTURAL_CHANGE`:

```text
🏛 formal authority changed
      ↓
update owning architecture / accepted decision surface
      ↓
update affected machine/current-state representation
      ↓
update Agent view if reading order or constraints changed
      ↓
update Human Overview
      ↓
update only affected README visual summaries
      ↓
validate bilingual + AI-context + reconciliation
```

If `STATE_CHANGE`, update current truth without redesigning stable formal architecture.

If `EVIDENCE_ONLY`, preserve high-level presentation and authority unless the new evidence triggers a separate governed reassessment.

The target model is:

```text
                           one repository truth
                                  │
                                  ▼
                         🏛 formal authority
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
         👤 understandable    🤖 deterministic    ⚙ machine-checkable

       🔬 evidence-preserving ── supports / challenges ──▶ 🏛 authority
```

The objective is not maximal documentation volume. It is **clear ownership of meaning, state, instructions, presentation and evidence without drift between them**.