# Substrate-Neutral Ecosystem Bridge

**Status:** Orientation only.  
**Authority:** This note does not replace A1–A10, A8, current project state, or any accepted architecture decision.

Native Kernel already defines the deeper substrate-neutral conformance contract. This note records only its ecosystem-facing implication:

> Velantrim architecture is preserved by keeping required semantic distinctions and obligations intact across implementation replacement, not by preserving any specific technology.

```text
TECHNOLOGY != ARCHITECTURE
SAME OUTPUT != SAME SEMANTIC CONFORMANCE
IMPLEMENTATION REPLACEMENT != PERMISSION TO COLLAPSE DISTINCTIONS
```

For Native Kernel, the authoritative technical detail remains in the Architecture Re-foundation documents, especially:

- `A2_CORE_ONTOLOGY_AND_VOCABULARY.md`
- `A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md`
- `A4_SEMANTIC_LAWS_AND_INVARIANTS.md`
- `A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md`

The ecosystem-level bridge should therefore remain thin: Crystal, Titan, Soul, Continuum, and Mentaury-Kernel may each expose technology-neutral projections of their own domains, while Native Kernel remains the primary home for substrate-neutral semantic obligations and conformance reasoning.
