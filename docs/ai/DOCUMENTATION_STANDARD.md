# 📚 Velantrim Documentation Standard v4

`overview != current state != machine state != evidence/history`

Native Kernel documentation presents **one project truth through four deliberately different layers**. The layers serve different readers and different authority needs; they are not four competing truths.

```text
                      🧬 ONE PROJECT TRUTH
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
     👤 HUMAN VIEW        🤖 AGENT VIEW        ⚙ MACHINE STATE
 README / OVERVIEW         docs/ai/**          JSON / YAML state
          │                    │                    │
          └────────────────────┴──────────┬─────────┘
                                          ▼
                                   📚 EVIDENCE / HISTORY
                              tests · ADRs · research · checkpoints
```

The four layers may summarize or constrain the same underlying project, but each has a different role.

## 1. Layer roles

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
- links outward to detailed current-state, machine, formal and evidence documents.

The root README should be a **3–7 minute orientation surface**, not a long-running status ledger. It may contain one compact comparison matrix when that matrix materially improves human comprehension, but the detailed caveats and source ledger belong in `docs/COMPARISONS*`. Volatile technical chronology belongs elsewhere.

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

An AI agent must not infer authorization from human-friendly presentation text when a machine/current-state surface exists.

### ⚙ Machine state

Primary surfaces:

- `project-state.json` — machine-readable repository state.
- `docs/ai/project_manifest.yaml` — documentation-routing manifest.
- validator- and contract-owned JSON/YAML records where applicable.

Machine surfaces should optimize for exact fields, schemas, status semantics and deterministic validation. Emojis and narrative are unnecessary here.

### 📚 Evidence / history

Primary surfaces include:

- `STATUS.md` and `ROADMAP.md` for current/historical human status context;
- `evidence/**`;
- `docs/research/**`;
- ADRs, test reports, evaluation artifacts and historical checkpoints.

Evidence/history surfaces preserve chronology, scoped claims and falsification records. They must not be promoted into architecture authority merely because they are detailed or recent.

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
3. update only the visual representations whose function changed;
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
- leave a dated external comparison undated after materially changing its claims.

Prefer collapsible historical or machine-detail sections when validators require text that would otherwise dominate the human landing page.

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
update only affected README visual summaries
      ↓
validate bilingual + AI-context + reconciliation
```

If `STATE_CHANGE`, update the current truth without redesigning the whole page.

If `EVIDENCE_ONLY`, preserve the high-level presentation unless the new evidence changes what the project can legitimately claim.

The goal is:

```text
                      one repository truth
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
     👤 understandable    🤖 deterministic    ⚙ machine-checkable
                              │
                              ▼
                       📚 evidence-preserving
```
