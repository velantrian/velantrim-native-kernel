# Roadmap

Velantrim Native Kernel now maintains three independent tracks. They may progress at different speeds, but their statuses and evidence must never be collapsed.

```text
H — Historical Recovery
authentic v0.1.2.1 → original 44 tests → controlled import, if recovered

C — Clean Implementation
accepted contracts → P1–P5 → C3 → C4 → C5 → future bounded evidence

R — Long-Horizon Research
hypothesis → explicit contract → experiments → evidence → decision → possible implementation
```

## Track H — Historical Recovery

**Status:** `BLOCKED / ACTIVE EVIDENCE-RECOVERY / INDEPENDENT`

Purpose: identify the authentic source archive or original location for the externally reported `v0.1.2.1` checkpoint and original 44-test suite.

Current facts:

- authentic source bytes and original tests are not found in accessible sources;
- operator-controlled devices, backups and inaccessible archives remain outside the completed sweep;
- `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`;
- no clean implementation artifact may be relabelled as recovered history.

Allowed:

- search and document locations;
- preserve candidates read-only;
- hash and verify exact bytes;
- record an operator provenance decision when sufficient evidence exists.

Prohibited:

- approximation labelled `v0.1.2.1`;
- new tests labelled as the original 44;
- inherited historical claims without provenance.

Possible outcomes:

```text
authentic source recovered
→ controlled historical import under separate evidence

declared exhaustive search + operator decision
→ LOST / NON-REPRODUCIBLE EXTERNAL CHECKPOINT

neither condition met
→ remain NOT_FOUND_IN_ACCESSIBLE_SOURCES
```

Track H does not block Track C.

## Track C — Clean Implementation

**Status:** `ACTIVE / PARTIAL / NOT PRODUCTION-READY`

The clean lineage was accepted by ADR-0015 and is independent of historical recovery.

```text
P1 semantic core                         MERGED / REPOSITORY-TESTED
P2 PostgreSQL append                     MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay / projections / Receipts       MERGED / REPOSITORY-INTEGRATION-TESTED
P4 PostgreSQL assertion conformance      MERGED / PARTIAL / C2
P5 SQLite + cross-profile comparison     MERGED / PARTIAL / C2 + C3
C4 offline shadow evaluation             MERGED / PARTIAL
C5 bounded operational rehearsal         MERGED / PARTIAL
```

Current evidence:

```text
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
assertion map: 45 / 10 / 17 / 0
NK-EPI: 0 / 8 SUPPORTED
```

### C5 preservation checkpoint

Exact implementation-main and final-main ZIP artifacts are retained under `evidence/c5/2026-08-07/`.

### Next clean-lineage work

Potential work must be separately scoped:

1. first executable NK-EPI vertical slice;
2. admission-boundary evidence;
3. SQLite/runtime hardening;
4. evidence automation for future runs;
5. deletion evidence without physical-erasure overclaim;
6. independent cross-language conformance reader.

Operational work may continue, but it cannot alone raise semantic conformance or authorize C6.

## Track R — Long-Horizon Research

**Status:** `PROPOSED / BOUNDED / NO AUTOMATIC PROMOTION`

Track R contains ideas that are useful to preserve but are not yet accepted runtime commitments. Current backlog: [`docs/research/POST_C5_RESEARCH_BACKLOG.md`](docs/research/POST_C5_RESEARCH_BACKLOG.md).

Research areas include:

- `NK-EPI-004 — unknown ≠ false`;
- explicit epistemic admission boundary;
- evidence-bearing erasure states;
- independent language/runtime profiles;
- signed Receipts;
- licensing and contribution governance;
- controlled Titan/Crystal/Mentaury adapters;
- neuromorphic, photonic, analog, probabilistic and other future substrates;
- bounded bio-inspired and Curiosity research.

Hard boundaries:

- research vocabulary does not become Canon automatically;
- graph, relevance, salience, utility, repetition and model output are not truth;
- Rust, Python, SQL, LLMs, vectors and hardware remain profile choices;
- no research note authorizes runtime, production or ecosystem wiring;
- every promotion follows the rule below.

## Promotion rule

```text
research hypothesis
→ explicit contract
→ reproducible code and tests
→ failure cases
→ exact evidence
→ decision record
→ bounded implementation proposal
→ threat model / deletion / rollback where applicable
→ operator approval
```

## C6 gate

C6 is not authorized. It may be discussed only after:

- durable C5 evidence remains verifiable;
- GitHub and Notion current-state surfaces agree;
- `project-state.json` is validated in CI;
- at least one NK-EPI assertion has executable support;
- admission and overclaim boundaries are tested;
- operational environment risks are explicitly addressed;
- a separate ADR and operator GO exist.
