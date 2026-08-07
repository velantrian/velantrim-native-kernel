# C5 operational tooling

Run the bounded rehearsal after producing an exact C4 prerequisite report:

```bash
python tools/operations/c5_rehearsal.py \
  contracts/operational-plan-v1.json \
  artifacts/c4-shadow-report.json \
  --output artifacts/c5-operational-report.json \
  --backup-output artifacts/c5-quarantine-backup.json

python tools/operations/validate_c5_report.py \
  artifacts/c5-operational-report.json \
  --plan contracts/operational-plan-v1.json \
  --c4-report artifacts/c4-shadow-report.json \
  --backup artifacts/c5-quarantine-backup.json
```

Repository evidence additionally requires exact commit/run/Python/PostgreSQL/SQLite/runner metadata and all four matrix jobs.

The logical backup is synthetic application-level recovery evidence, not physical backup or provider DR proof.
