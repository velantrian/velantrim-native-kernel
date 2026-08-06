# 🤖 AI context validation tools

These standard-library utilities validate the repository's AI orientation and continuity surfaces.

They are support/governance tooling only.

```text
AI-context guard PASS
≠ Native Kernel runtime PASS
≠ architecture correctness
≠ Notion synchronization proof
≠ authentic v0.1.2.1 recovery
```

## Validator

Run from the repository root:

```bash
python tools/ai_context/validate_context.py --repo .
```

The validator checks:

- mandatory AI-context and governance files exist;
- selected first-read Markdown files do not contain broken repository-relative links;
- relative links do not escape the repository;
- `docs/ai/CURRENT_STATE.md` contains an exact 40-character `Last verified public main` checkpoint;
- the checkpoint commit exists in Git history;
- the checkpoint is an ancestor of the commit under review;
- core status-boundary markers remain present.

An ancestor checkpoint is permitted deliberately. The context file is a last-verified checkpoint, not an automatically current database. The guard detects invalid or unrelated checkpoints; it does not decide whether every later change required a semantic status update.

## Tests

```bash
python -m unittest discover -s tests -p 'test_ai_context_validator.py' -v
```

The tests cover valid ancestor checkpoints, missing required files, broken links, repository-escape links, malformed checkpoint syntax, and unknown commits.

## CI boundary

`.github/workflows/ai-context.yml` runs read-only on relevant pull requests, pushes to `main`, and manual dispatches. It uses full Git history because ancestry cannot be checked from a one-commit shallow checkout.
