# 🧪 Conformance Model

> **Status:** `PROPOSED DOCUMENTATION CONTRACT / NOT YET A CERTIFICATION PROGRAM`  
> **Purpose:** define how a present or future implementation can demonstrate that it follows Native Kernel architecture

## 1. Why conformance matters

Technology independence must be tested, not merely declared.

A system is not a Native Kernel implementation because it uses the same terminology. It should demonstrate that it preserves the required semantic contracts.

```text
same architectural contract
        ↓
implementation profile A
implementation profile B
        ↓
comparable semantic behaviour
```

> [!NOTE]
> Conformance concerns meaning and observable behaviour. It does not require identical source code, storage layout, programming language, or byte representation.

---

## 2. Conformance levels

| Level | Meaning | Required evidence |
|---|---|---|
| **C0 — Described** | The implementation claims to follow a contract | architecture mapping only |
| **C1 — Locally exercised** | Core behaviour runs in one controlled environment | local tests and failure cases |
| **C2 — Repository reproduced** | A third party can reproduce the declared behaviour from the repository | committed code, tests, environment, CI |
| **C3 — Cross-profile equivalent** | Two different implementation profiles preserve a declared semantic equivalence | replay comparison and adapter evidence |
| **C4 — Shadow evaluated** | Behaviour is compared on recorded external workloads without becoming an authority | Shadow report and Receipts |
| **C5 — Operationally validated** | A bounded deployment has security, rollback, observability, and incident evidence | explicit production review |

These levels do not replace project maturity labels. They describe implementation evidence for a particular contract and version.

---

## 3. Required contract families

A conforming implementation should explicitly map its behaviour to the following contract families.

### Identity

- Claims have stable semantic identity.
- Backend-generated row IDs are not the only source of identity.
- Lineage and version relationships remain inspectable.

### History

- Changes are explicit.
- Authoritative history is not silently rewritten by projection updates.
- Replay boundaries are defined.

### Reduction

- Derived state can be reconstructed from the declared authoritative history.
- Non-determinism is prohibited or explicitly bounded and receipted.

### Projection

- Read models can be removed and rebuilt.
- Projection loss does not destroy authoritative history.
- Projection output does not silently become truth authority.

### Temporal meaning

- valid time, record/knowledge time, and write order are not silently collapsed;
- any implementation-specific approximation is documented.

### Conflict

- candidate conflict is distinct from established conflict;
- detection is distinct from resolution;
- unresolved semantic conflict remains visible.

### Admission

- admission decisions are explicit;
- the decision, policy version, evidence, and result can be receipted;
- no specific Crystal or Titan component is required by the abstract contract.

### Retrieval and selection

- relevance is not treated as truth;
- exclusions, conflicts, uncertainty, and limits can be exposed;
- selection behaviour is reproducible within its declared profile.

### Audit

- important state transitions and context selections can produce accountable Receipts;
- a Receipt explains processing but does not prove task sufficiency.

---

## 4. Reference conformance experiment

The first reference experiment should be small and technology-neutral.

```text
Authoritative history
        ↓
Reference implementation profile
        ↓
Derived semantic state
        ↓
Delete all disposable projections
        ↓
Rebuild
        ↓
Compare semantic equivalence
        ↓
Produce reconstruction Receipt
```

Minimum assertions:

1. replay reconstructs the declared state;
2. removing projections does not remove Canon history;
3. rebuilt lineage and temporal meaning remain equivalent;
4. conflicts are not silently lost;
5. the Receipt identifies the source range, reducer/profile version, result, and known limits.

---

## 5. Semantic equivalence

Different substrates may represent the same meaning differently.

A conformance test must therefore declare its equivalence class.

| Equivalence class | Example |
|---|---|
| **Byte equality** | deterministic serialization in the same profile |
| **Structural equality** | same Claims, Events, links, and statuses despite different ordering of non-semantic fields |
| **Semantic equality** | equivalent identity, lineage, temporal meaning, conflict visibility, and policy result |
| **Behavioural equality** | same accepted commands and observable results under a bounded workload |

> [!IMPORTANT]
> “Equivalent” must never remain an undefined marketing word. Every test must state what differences are allowed.

---

## 6. Evidence record

Each conformance claim should point to:

```text
contract_version
implementation_profile
repository_commit
runtime_environment
test_command
test_artifacts
known_failures
equivalence_definition
operator_decision
```

AI-generated reviews, architectural discussions, and external model consensus may be listed as inputs. They are not conformance evidence by themselves.

---

## 7. Non-conformance examples

```text
❌ Projection rows are edited and treated as history.
❌ A graph edge silently promotes a Claim to truth.
❌ Replacing SQLite requires changing Claim identity.
❌ An LLM response becomes Canon without an explicit admission decision.
❌ A conflict disappears because the newest timestamp wins.
❌ A README claim has no reproducible code or test artifact.
```

---

## 8. Relationship to Issue #1

Issue #1 is not expected to prove full technology independence.

Its purpose is narrower:

```text
exact v0.1.2.1 import
→ exact 44-test suite
→ reproducible environment
→ CI
→ parity review
```

That work may establish early repository-reproduced evidence for the imported profile. Cross-profile conformance requires later, separately scoped experiments.
