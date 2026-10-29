"""Synthetic positive/negative controls for a reference-export probe, not H11."""

import copy
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from native_kernel.semantic_core.reducer import SemanticState
from tools.lab import state_transfer_probe as probe


class TransferProbeTests(unittest.TestCase):
    def setUp(self):
        self.source = SemanticState(
            last_global_seq=6, stream_offsets=(("stream", 6),),
            admitted_claim_ids=("c1", "c2"), links=(("c1", "related", "c2"),),
            utilization_counts=(("c1", 2),), superseded_by=(("c1", "c2"),),
            erased_claim_ids=("c1",),
        ).as_contract_object()

    def test_equal_state_passes_and_inputs_remain_unchanged(self):
        target = copy.deepcopy(self.source)
        original = copy.deepcopy(self.source)
        self.assertEqual(probe.compare_objects(self.source, target)["status"], "PASS")
        self.assertEqual(self.source, original)
        self.assertEqual(target, original)

    def test_each_lost_state_dimension_fails_with_only_field_name(self):
        for field in ("stream_offsets", "admitted_claim_ids", "links", "utilization_counts",
                      "superseded_by", "erased_claim_ids"):
            with self.subTest(field=field):
                target = copy.deepcopy(self.source)
                target[field] = []
                result = probe.compare_objects(self.source, target)
                self.assertEqual(result["status"], "FAIL")
                self.assertEqual(result["changed_fields"], [field])

    def test_unknown_missing_and_invalid_contract_fields_are_blocked(self):
        cases = [{**self.source, "secret-extra-field": "secret-value"},
                 {**self.source, "contract": "unsupported"},
                 {k: v for k, v in self.source.items() if k != "erased_claim_ids"}]
        for target in cases:
            with self.subTest(target=target):
                result = probe.compare_objects(self.source, target)
                self.assertEqual(result["status"], "BLOCKED")
                self.assertNotIn("secret", json.dumps(result))
        self.assertEqual(probe.compare_objects({}, self.source)["reason"], "invalid_source")

    def test_file_parser_rejects_duplicate_keys_nonfinite_and_invalid_utf8(self):
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory)/"source.json", Path(directory)/"target.json"
            source.write_text(json.dumps(self.source))
            for invalid in (b'{"x":1,"x":2}', b'{"x":NaN}', b'\xff', b'{broken',
                            b'[' * 1600 + b'0' + b']' * 1600):
                target.write_bytes(invalid)
                self.assertEqual(probe.compare_files(source, target)["status"], "BLOCKED")

    def test_size_limit_and_unreadable_input_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory)/"source.json", Path(directory)/"target.json"
            source.write_bytes(b' ' * (probe.MAX_EXPORT_BYTES + 1))
            self.assertEqual(probe.compare_files(source, target)["reason"], "unreadable_source")
            source.write_text(json.dumps(self.source))
            self.assertEqual(probe.compare_files(source, target)["reason"], "unreadable_target")

    def test_cli_reports_pass_fail_blocked_without_writing_exports(self):
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory)/"source.json", Path(directory)/"target.json"
            source.write_text(json.dumps(self.source))
            for expected, value in ((0, self.source), (1, {**self.source, "erased_claim_ids": []}),
                                    (2, {})):
                target.write_text(json.dumps(value))
                before = source.read_bytes(), target.read_bytes()
                with redirect_stdout(io.StringIO()) as output:
                    code = probe.main([str(source), str(target)])
                self.assertEqual(code, expected)
                self.assertIn(json.loads(output.getvalue())["status"], ("PASS", "FAIL", "BLOCKED"))
                self.assertEqual((source.read_bytes(), target.read_bytes()), before)


if __name__ == "__main__":
    unittest.main()
