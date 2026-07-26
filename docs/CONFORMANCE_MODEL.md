# 🧪 Conformance Model

> **Status:** `PROPOSED DOCUMENTATION CONTRACT / NOT YET A CERTIFICATION PROGRAM`  
> **Purpose:** define how a present or future implementation can demonstrate that it follows Native Kernel architecture

## 1. Why conformance matters

Technology independence must be tested, not merely declared.

A system is not a Native Kernel implementation because it uses the same terminology. It should demonstrate that it preserves declared semantic contracts.

```text
same architectural contract
        ↓
implementation profile A
implementation profile B
        ↓
comparable semantic behaviour
```

> [!NOTE]
> Conformance concerns meaning and observable behaviour. It does not require identical source code, storage layout, programming language, or byte representation unless a specific contract declares byte equality.

## 2. Conformance levels

| Level | Meaning | Required evidence |
|---|---|---|
| **C0 — Described** | An implementation claims to follow a contract | architecture mapping only |
| **C1 — Locally exercised** | Core behaviour runs in one recorded controlled environment | local tests, commands, environment, and failure cases |
| **C2 — Repository reproduced** | A third party can reproduce specific declared behaviour from the repository | committed code, tests, environment, CI, and traceability |
| **C3 — Cross-profile equivalent** | Two different implementation profiles preserve a declared equivalence class | replay comparison, fixtures, and adapter evidence |
| **C4 — Shadow evaluated** | Behaviour is compared on recorded external workloads without becoming an authority | approved dataset, metrics, Receipts, failures, and report |
| **C5 — Operationally validated** | A bounded deployment has security, rollback, observability, privacy, and incident evidence | explicit operational review and evidence |

These levels do not replace decision status, project maturity, implementation status, or operator approval. They describe evidence for a particular contract, version, implementation profile, and equivalence definition.

Conformance is assertion-scoped. A profile may be C2 for deterministic replay and only C0 for deletion semantics.

## 3. Required contract families

A conforming implementation should explicitly map its behaviour to the following contract families.

### Identity

- Claims have stable semantic identity.
- Backend-generated row IDs are not the only source of identity.
- Lineage and version relationships remain inspectable.
- When byte-level identity is required, canonical encoding, Unicode normalization, hash domain/version, and migration rules are declared.

### History

- Changes are explicit.
- Authoritative history is not silently rewritten by projection updates.
- Replay boundaries are defined.
- Ordering, append atomicity, crash boundaries, and schema evolution are declared for the tested scope.

### Reduction

- Derived state can be reconstructed from declared authoritative history.
- Non-determinism is prohibited or explicitly bounded and receipted.
- Reducer/profile versions are identified.

### Projection

- Read models can be removed and rebuilt.
- Projection loss does not destroy authoritative history.
- Projection output does not silently become truth authority.

### Temporal meaning

- valid time, record/knowledge time, and write order are not silently collapsed;
- any implementation-specific approximation is documented and tested.

### Conflict

- candidate conflict is distinct from established conflict;
- detection is distinct from resolution;
- unresolved semantic conflict remains visible;
- directionality and lifecycle assumptions are declared.

### Admission

- admission decisions are explicit;
- the decision, policy version, evidence, and result can be receipted;
- no specific Crystal or Titan component is required by the abstract contract;
- implementation-profile names such as `GATE`, `TruthGate`, `Guardian`, `L3`, or an LLM filter do not become universal contract terms merely because one profile uses them.

### World and epistemic boundaries

A conforming profile should map the following documentation-level assertions:

| Assertion ID | Required meaning |
|---|---|
| `NK-EPI-001` | a representation is not silently treated as the represented reality |
| `NK-EPI-002` | an observation is not silently treated as a complete explanation |
| `NK-EPI-003` | transformation or assembly is not silently treated as proof of origin |
| `NK-EPI-004` | unknown or unanswered is not silently treated as false |
| `NK-EPI-005` | missing provenance remains explicit as a provenance gap |
| `NK-EPI-006` | a current observer, method, or profile limit is not silently universalized into impossibility |
| `NK-EPI-007` | worldview-sensitive claims retain explicit domain and scope |
| `NK-EPI-008` | observations, models, hypotheses, retrieval results, utility outcomes, and proposals are not silently promoted into admitted knowledge |

The assertions are defined by [`WORLD_AND_EPISTEMIC_BOUNDARIES.md`](./WORLD_AND_EPISTEMIC_BOUNDARIES.md) and proposed through [`ADR-0008`](./adr/0008-epistemic-boundaries-are-representation-disciplines.md).

An implementation may use different schemas and vocabulary, but it must demonstrate the declared semantic equivalence rather than merely repeat these labels.

### Retrieval and selection

- relevance is not treated as truth;
- exclusions, conflicts, uncertainty, and limits can be exposed;
- selection behaviour is reproducible within its declared profile;
- a Receipt does not imply task sufficiency.

### Audit

- important state transitions and context selections can produce accountable Receipts;
- a Receipt explains processing but does not prove truth or task sufficiency;
- Receipt schema and source-range semantics are declared.

### Deletion and restriction

- append-only history does not nullify legal deletion or restriction requirements;
- payloads, projections, indexes, embeddings, exports, Receipts, Shadow datasets, and backups are included in the declared scope;
- crypto-erasure or tombstone behaviour must state what remains observable.

## 4. Executable conformance artifacts

Prose is necessary but insufficient. A conformance claim should eventually be backed by reviewable artifacts.

Recommended artifact set:

```text
contracts/
├── schemas/                 # normative event, Claim, Receipt, and export schemas
├── golden/                  # valid histories and expected semantic outputs
├── invalid/                 # malformed or forbidden event corpora
├── canonical/               # canonical encoding and identity vectors
├── replay/                  # reducer and projection rebuild vectors
├── conflict/                # candidate/canonical conflict fixtures
├── temporal/                # valid-time and record-time fixtures
├── epistemic/               # NK-EPI positive and negative fixtures
├── deletion/                # restriction and erasure expectations
└── evidence/                # machine-readable conformance records
```

A cross-profile runner should consume the same fixtures and report allowed and forbidden differences under a declared equivalence class.

### Proposed epistemic fixture families

Future fixtures for `NK-EPI-001` through `NK-EPI-008` should include at least:

- a model output that resembles an observation but lacks observation provenance;
- a transformation result incorrectly presented as proof of ultimate origin;
- missing evidence incorrectly collapsed to a negative result;
- an unknown provenance segment incorrectly filled by an assumption;
- a profile limitation incorrectly promoted to universal impossibility;
- a worldview Claim presented without domain or scope;
- a retrieval result silently promoted into admitted knowledge;
- a valid profile that preserves the gap, scope, and admission decision explicitly.

These fixtures are proposed only. No executable pack currently exists.

## 5. Reference conformance experiment

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
Compare declared equivalence
        ↓
Produce reconstruction Receipt
```

Minimum assertions:

1. replay reconstructs the declared state;
2. removing projections does not remove Canon history;
3. rebuilt lineage and temporal meaning remain equivalent;
4. conflicts are not silently lost;
5. the Receipt identifies source range, reducer/profile version, result, and known limits;
6. invalid events fail in declared ways;
7. the evidence record names the exact fixture and implementation commit.

The first replay experiment does not by itself prove the eight `NK-EPI` assertions. Each assertion requires its own traceable fixture and expected semantic result.

## 6. Semantic equivalence

Different substrates may represent the same meaning differently.

A conformance test must declare its equivalence class.

| Equivalence class | Example |
|---|---|
| **Byte equality** | deterministic canonical serialization in the same declared profile/version |
| **Structural equality** | same Claims, Events, links, and statuses despite allowed non-semantic field ordering |
| **Semantic equality** | equivalent identity, lineage, temporal meaning, conflict visibility, epistemic boundaries, and policy result |
| **Behavioural equality** | same accepted commands and observable results under a bounded workload |

> [!IMPORTANT]
> “Equivalent” must never remain an undefined marketing word. Every test must state what differences are allowed and why they do not change meaning.

## 7. Contract-to-test traceability

A conformance claim must point from prose to executable evidence.

| Contract assertion | Fixture/test ID | Runtime symbol/path | Equivalence class | Result | Known limit |
|---|---|---|---|---|---|
| Claims are immutable semantic records | `<id>` | `<path>` | semantic | pass/fail | `<limit>` |
| Replay reconstructs declared state | `<id>` | `<path>` | structural | pass/fail | `<limit>` |
| Candidate conflict is not canonical conflict | `<id>` | `<path>` | behavioural | pass/fail | `<limit>` |
| Relevance is not truth evidence | `<id>` | `<path>` | behavioural | pass/fail | `<limit>` |
| `NK-EPI-001` representation is not reality | `<id>` | `<path>` | semantic | pass/fail | `<limit>` |
| `NK-EPI-003` transformation is not origin | `<id>` | `<path>` | semantic | pass/fail | `<limit>` |
| `NK-EPI-005` provenance gap is preserved | `<id>` | `<path>` | structural/semantic | pass/fail | `<limit>` |
| `NK-EPI-008` no silent semantic promotion | `<id>` | `<path>` | behavioural | pass/fail | `<limit>` |

Missing mappings remain explicit gaps. A line-by-line prose review is not a substitute for traceability.

## 8. Evidence record

Each conformance claim should point to:

```yaml
contract_id: <stable-id>
contract_version: <version>
assertion_id: <stable-id>
implementation_profile: <profile>
repository_commit: <sha>
source_snapshot_sha256: <sha256-or-not-applicable>
runtime_environment: <identity>
test_command: <command>
test_artifacts:
  - <path-or-artifact>
fixture_ids:
  - <id>
known_failures:
  - <value>
equivalence_definition: <class-and-rules>
evidence_level: DOCUMENTED | EXTERNALLY_OBSERVED | LOCALLY_TESTED | REPOSITORY_REPRODUCED | SHADOW_EVALUATED | OPERATIONALLY_VALIDATED
operator_approval: NOT_REQUESTED | PENDING | APPROVED | WITHDRAWN
```

AI-generated reviews, architectural discussions, and external model consensus may be listed as inputs. They are not conformance evidence by themselves.

## 9. Non-conformance examples

```text
❌ Projection rows are edited and treated as history.
❌ A graph edge silently promotes a Claim to truth.
❌ Replacing SQLite requires changing Claim identity.
❌ An LLM response becomes Canon without an explicit admission decision.
❌ A conflict disappears because the newest timestamp wins.
❌ A README claim has no reproducible code or test artifact.
❌ A replacement suite has 44 tests but is presented as the lost original suite.
❌ Operator approval is presented as empirical proof.
❌ A GitHub-hosted timing is presented as historical hardware-equivalent performance without comparability evidence.
❌ A model or simulation is presented as the represented reality without declared equivalence limits.
❌ Successful transformation or assembly is presented as proof of ultimate origin.
❌ Missing evidence is presented as a negative result.
❌ A provenance gap is filled by an unmarked assumption or worldview statement.
❌ A current implementation limitation is presented as universal impossibility.
❌ A metaphysical, religious, anti-religious, cultural, or ethical Claim is presented as unmarked empirical fact.
```

## 10. Relationship to Issue #1

Issue #1 is currently blocked by authentic source recovery.

```text
Stage 0.5
recover authentic v0.1.2.1 source and original suite
        ↓
Stage 1
sealed exact import
→ preserved test inventory
→ historical reproduction environment
→ compatibility CI
→ contract-to-test traceability
```

Issue #1 is not expected to prove full technology independence or the proposed `NK-EPI` assertion family.

A successful import may establish C2 evidence only for the specific assertions demonstrated by the authentic imported profile. It does not establish C3 cross-profile equivalence, C4 Shadow value, C5 operational validation, production readiness, universal substrate portability, or compliance with `NK-EPI-001` through `NK-EPI-008` unless dedicated fixtures prove them.

See [`ISSUE_1_IMPORT_SPEC.md`](./ISSUE_1_IMPORT_SPEC.md) and [`ISSUE_1_IMPORT_SPEC.ru.md`](./ISSUE_1_IMPORT_SPEC.ru.md).
