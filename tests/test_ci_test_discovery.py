"""Reproducible tests for the bounded CI test-declaration coverage guard."""
from __future__ import annotations

import tempfile
import textwrap
import unittest
from pathlib import Path

from tools.ci.check_test_discovery import (
    TEST_FILE_PATTERN,
    audit_test_discovery,
    github_glob_match,
    list_test_modules,
    parse_pull_request_paths,
    parse_unittest_invocations,
)

ROOT = Path(__file__).resolve().parents[1]


def _write_repo(root: Path, *, tests: list[str], workflow: str) -> None:
    tests_dir = root / "tests"
    tests_dir.mkdir()
    for name in tests:
        (tests_dir / name).write_text("import unittest\n", encoding="utf-8")
    workflows = root / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "ci.yml").write_text(textwrap.dedent(workflow).lstrip() + "\n", encoding="utf-8")


class GitHubGlobTests(unittest.TestCase):
    def test_exact_and_star_and_recursive(self) -> None:
        self.assertTrue(github_glob_match("tests/test_a2_ontology.py", "tests/test_a2_ontology.py"))
        self.assertTrue(github_glob_match("tests/test_p3_semantic.py", "tests/test_p3_*.py"))
        self.assertTrue(github_glob_match("tests/test_foo.py", "tests/**"))
        self.assertFalse(github_glob_match("tests/test_foo.py", "docs/**"))


class WorkflowParserTests(unittest.TestCase):
    def test_unrestricted_pull_request_has_no_path_list(self) -> None:
        text = textwrap.dedent("""
            on:
              pull_request:
              push:
                branches: [main]
            jobs:
              x:
                runs-on: ubuntu-24.04
        """).lstrip()
        self.assertIsNone(parse_pull_request_paths(text))

    def test_explicit_paths_and_unittest_patterns(self) -> None:
        text = textwrap.dedent("""
            on:
              pull_request:
                paths:
                  - "tests/test_alpha.py"
            jobs:
              x:
                steps:
                  - run: python -m unittest discover -s tests -p 'test_alpha.py' -v
                  - run: python -m unittest tests.test_branch_preservation -v
        """).lstrip()
        self.assertEqual(parse_pull_request_paths(text), ("tests/test_alpha.py",))
        patterns, modules, default_discover = parse_unittest_invocations(text)
        self.assertEqual(patterns, ("test_alpha.py",))
        self.assertEqual(modules, ("tests.test_branch_preservation",))
        self.assertFalse(default_discover)

    def test_comment_only_unittest_text_is_not_counted_as_invocation(self) -> None:
        text = textwrap.dedent("""
            jobs:
              x:
                steps:
                  - run: |
                      # python -m unittest discover -s tests -p 'test_alpha.py' -v
                      echo no-test-execution-here
        """).lstrip()
        patterns, modules, default_discover = parse_unittest_invocations(text)
        self.assertEqual(patterns, ())
        self.assertEqual(modules, ())
        self.assertFalse(default_discover)


class DiscoveryAuditFixtureTests(unittest.TestCase):
    def test_covered_module_reports_no_gaps(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _write_repo(root, tests=["test_alpha.py"], workflow="""
                on:
                  pull_request:
                    paths:
                      - "tests/test_alpha.py"
                jobs:
                  x:
                    steps:
                      - run: python -m unittest discover -s tests -p 'test_alpha.py' -v
            """)
            self.assertEqual(audit_test_discovery(root), [])

    def test_module_without_supported_invocation_is_a_gap(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _write_repo(root, tests=["test_alpha.py", "test_beta.py"], workflow="""
                on:
                  pull_request:
                    paths:
                      - "tests/**"
                jobs:
                  x:
                    steps:
                      - run: python -m unittest discover -s tests -p 'test_alpha.py' -v
            """)
            gaps = audit_test_discovery(root)
            self.assertEqual([gap.test_path for gap in gaps], ["tests/test_beta.py"])

    def test_default_discover_plus_tests_glob_covers_all_modules(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _write_repo(root, tests=["test_alpha.py", "testfoo.py"], workflow="""
                on:
                  pull_request:
                    paths:
                      - "tests/**"
                jobs:
                  x:
                    steps:
                      - run: python -m unittest discover -s tests -v
            """)
            self.assertEqual(audit_test_discovery(root), [])


class LiveRepositoryDiscoveryTests(unittest.TestCase):
    def test_current_modules_are_declared_and_path_triggered_within_supported_syntax(self) -> None:
        modules = list_test_modules(ROOT)
        self.assertTrue(modules)
        self.assertEqual(TEST_FILE_PATTERN, "test*.py")
        self.assertEqual(audit_test_discovery(ROOT), [])


if __name__ == "__main__":
    unittest.main()
