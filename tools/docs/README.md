# Bounded bilingual documentation parity tooling

`validate_bilingual_parity.py` checks explicitly configured English/Russian documentation obligations.

```bash
python tools/docs/validate_bilingual_parity.py --repo .
```

Configuration:

```text
tools/docs/bilingual-pairs-v1.json
protocol: nk-bilingual-doc-parity/1
```

## What it checks

For each declared pair, configuration may require:

- both UTF-8 files to exist inside the repository;
- exact language-selector link literals in both files;
- exact shared status, contract or non-claim literals in both files;
- language-specific obligation literals;
- exactly one level-1 heading;
- equal sequences of Markdown heading levels for selected synchronized pairs.

Headings inside backtick or tilde fenced code blocks are ignored.

## What it does not prove

```text
PASS
≠ accurate translation
≠ complete preservation of meaning
≠ legal equivalence
≠ identical prose or document length
≠ requirement that every document be bilingual
≠ Architecture Canon, runtime or maturity evidence
```

The registry is intentionally explicit. Adding a pair or obligation changes the validation scope and must be reviewed like any other policy-bearing tooling change.

Legacy pairs may use bounded marker checks without heading-outline equality until their structures have been independently reconciled. The validator never computes a translation score or length ratio.
