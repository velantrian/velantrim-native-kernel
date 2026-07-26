# Benchmark Methodology

## Purpose

Benchmarks in this repository are diagnostic tools, not production capacity claims. They are intended to reveal scaling shape and regressions in the deterministic research prototype.

## Benchmark identity and lineage

Every published measurement set must have a stable `benchmark_id`. Results with different IDs are separate workloads unless a comparison artifact proves otherwise.

| Benchmark ID | Workload | Evidence state | Source snapshot | Environment metadata |
|---|---|---|---|---|
| `NK-BM-V0121-SELECTIVE-001` | selective activation query | `EXTERNALLY_OBSERVED` | reported local `v0.1.2.1` | incomplete |
| `NK-BM-V0121-BROAD-001` | broad activation query | `EXTERNALLY_OBSERVED` | reported local `v0.1.2.1` | incomplete |
| `NK-BM-LEGACY-INDEXED-001` | earlier indexed read-path table preserved in Notion | `EXTERNALLY_OBSERVED` | local prototype lineage not fully identified | incomplete |

These benchmark IDs identify records; they do not upgrade their evidence level. The three workloads must not be numerically compared as if they were repetitions of one benchmark. In particular, the legacy Notion value at 800 claims, the selective value at 800 claims, and the broad value at 800 claims come from different declared workloads.

## Prior local observations

The following measurements were previously observed on one local environment and are retained only as external baseline targets until the code and benchmark harness are imported into this repository.

### `NK-BM-V0121-SELECTIVE-001` — Selective query

```text
50 claims    0.000540 s
100          0.000961 s
200          0.001856 s
400          0.003753 s
800          0.011988 s
1600         0.029115 s
```

### `NK-BM-V0121-BROAD-001` — Broad query

```text
50 claims    0.000777 s
100          0.001550 s
200          0.004160 s
400          0.016250 s
800          0.046970 s
```

These numbers are environment-specific and must not be quoted as stable product performance.

## Interpretation

The selective workload benefited substantially from an event index and cached charge calculations introduced in the `v0.1.2.1` research snapshot.

The broad workload remained superlinear. Profiling previously identified repeated neighbour discovery and conclusion checks as significant contributors. Greedy ablation also rebuilt candidate text repeatedly.

The honest statement is therefore:

```text
Typical read paths were substantially faster than the pre-index prototype.
The complete broad-query selection path was not yet linear.
```

## Reproduction gate

Before these results become repository evidence, a dedicated benchmark script must be merged with:

- stable benchmark IDs emitted in every result;
- deterministic synthetic corpus generation;
- selective and broad-query workloads;
- warm-up runs;
- multiple repetitions;
- median and p95 reporting;
- Python, OS, CPU, commit SHA, source-snapshot hash, seed, and timestamp metadata;
- explicit separation between snapshot construction and query timing.

## Benchmark rules

1. Record benchmark ID, Python version, OS, CPU, commit SHA, source-snapshot hash, seed, and timestamp.
2. Warm up before timed iterations.
3. Use multiple repetitions and report medians.
4. Keep corpus generation deterministic.
5. Separate selective and broad activation workloads.
6. Do not combine snapshot build and query timing without saying so.
7. Do not claim asymptotic complexity from a small number of points.
8. Treat regressions as investigation signals, not automatic architectural verdicts.
9. Do not present prototype numbers as Crystal or Titan production performance.
10. Mark all externally measured results as external until reproduced by repository CI or a reviewable artifact.
