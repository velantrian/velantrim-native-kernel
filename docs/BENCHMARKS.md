# Benchmark Methodology

## Purpose

Benchmarks in this repository are diagnostic tools, not production capacity claims. They are intended to reveal scaling shape and regressions in the deterministic research prototype.

## Prior local observations

The following measurements were previously observed on one local environment and are retained only as external baseline targets until the code and benchmark harness are imported into this repository.

### Selective query

```text
50 claims    0.000540 s
100          0.000961 s
200          0.001856 s
400          0.003753 s
800          0.011988 s
1600         0.029115 s
```

### Broad query

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

- deterministic synthetic corpus generation;
- selective and broad-query workloads;
- warm-up runs;
- multiple repetitions;
- median reporting;
- Python, OS, CPU, and commit metadata;
- explicit separation between snapshot construction and query timing.

## Benchmark rules

1. Record Python version, OS, CPU, and commit SHA.
2. Warm up before timed iterations.
3. Use multiple repetitions and report medians.
4. Keep corpus generation deterministic.
5. Separate selective and broad activation workloads.
6. Do not combine snapshot build and query timing without saying so.
7. Do not claim asymptotic complexity from a small number of points.
8. Treat regressions as investigation signals, not automatic architectural verdicts.
9. Do not present prototype numbers as Crystal or Titan production performance.
10. Mark all externally measured results as external until reproduced by repository CI or a reviewable artifact.