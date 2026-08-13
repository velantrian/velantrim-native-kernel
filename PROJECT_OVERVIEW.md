# 🧬 Velantrim Native Kernel — Project Overview

> **Human-first conceptual map.** This page explains what Native Kernel is trying to preserve and why the implementation is deliberately replaceable.

## 🎯 The central idea

Native Kernel is not defined by PostgreSQL, SQLite, Python, Rust, a graph database, vectors, an event log, or an LLM.

It is defined by the **semantic obligations that should survive when those technologies change**.

```text
technology may change
        ↓
representation may change
        ↓
storage may change
        ↓
compute may change
        ↓
but declared meaning must either survive
or the architecture must explicitly admit the loss/change
```

## 🌳 Conceptual structure

```text
🧬 Native Kernel
├── 🏛️ Meaning
│   ├── identity
│   ├── provenance
│   ├── time
│   ├── uncertainty
│   ├── conflict
│   └── accountable change / loss
├── 📐 Contracts
│   └── technology-neutral obligations
├── 🔌 Profiles
│   └── replaceable implementation mappings
├── 🧪 Laboratory
│   └── bounded executable realizations
├── 📊 Evidence
│   └── support / refutation / conformance
└── 🚦 Decisions
    └── architecture / Canon / runtime remain separate
```

## ⚖️ The distinctions that matter

| Distinction | Why it matters |
|---|---|
| `meaning ≠ implementation` | a database choice must not silently become architecture |
| `record ≠ truth` | storing something does not make it semantically true |
| `receipt ≠ correctness` | provenance proves an operation occurred, not that its conclusion is valid |
| `lab result ≠ universal proof` | one bounded experiment cannot prove every substrate |
| `architecture evidence ≠ runtime authority` | research success does not automatically authorize operation |
| `implementation change ≠ meaning change` | replaceable technology should not force semantic drift |

## 🧠 How to read the project

```text
README
  ↓
PROJECT_OVERVIEW       ← you are here
  ↓
STATUS / project-state ← what is true now?
  ↓
ARCHITECTURE docs      ← what owns the meaning?
  ↓
RESEARCH / EVIDENCE    ← what was actually tested?
  ↓
HISTORY                ← how did we get here?
```

## 🔬 Why the reference laboratory exists

The laboratory gives the architecture something concrete to challenge.

It can answer questions such as:

- can a declared invariant be implemented without relying on one storage engine?
- which architecture claims survive an independently derived realization?
- which assumptions fail under adversarial or cross-lineage testing?
- what evidence supports only a bounded scope rather than a universal claim?

The laboratory is therefore an **instrument for falsification and qualification**, not the definition of the Kernel itself.

## 🚦 Authority boundary

Native Kernel deliberately keeps these decisions separate:

```text
implemented
≠ tested
≠ supported for scope
≠ architecture promoted
≠ Final Canon
≠ runtime authorized
≠ production authorized
```

For the live values of those states, read **[STATUS.md](STATUS.md)** and **[project-state.json](project-state.json)** rather than inferring them from this stable overview.

## 📚 Next documents

- **Current state:** [STATUS.md](STATUS.md)
- **Machine state:** [project-state.json](project-state.json)
- **Architecture re-foundation:** [docs/ARCHITECTURE_REFOUNDATION.md](docs/ARCHITECTURE_REFOUNDATION.md)
- **Research material:** [docs/research/](docs/research/)
- **Quickstart:** [docs/QUICKSTART.md](docs/QUICKSTART.md)
- **AI entry:** [AGENTS.md](AGENTS.md) → [docs/ai/README.md](docs/ai/README.md)

> **One-sentence summary:** Native Kernel tries to preserve declared semantic meaning across replaceable technological substrates while forcing every claimed preservation, degradation, or promotion to remain explicit and evidence-bounded.