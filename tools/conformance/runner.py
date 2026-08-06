from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import unicodedata
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

UTC_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._:/-]{0,127}$")

ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / "contracts" / "fixture-pack.json"
REGISTRY = ROOT / "contracts" / "registry.json"


class ContractError(ValueError):
    pass


def _normalize(value: Any, *, path: str = "$") -> Any:
    if value is None:
        raise ContractError(f"{path}: null is forbidden in canonical identity objects; omit optional fields")
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        raise ContractError(f"{path}: floating-point numbers are forbidden; use an integer or canonical decimal string")
    if isinstance(value, str):
        normalized = unicodedata.normalize("NFC", value)
        if normalized != value:
            raise ContractError(f"{path}: string is not NFC-normalized")
        return value
    if isinstance(value, list):
        return [_normalize(item, path=f"{path}[{index}]") for index, item in enumerate(value)]
    if isinstance(value, dict):
        normalized: dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise ContractError(f"{path}: object keys must be strings")
            nkey = unicodedata.normalize("NFC", key)
            if nkey != key:
                raise ContractError(f"{path}: key {key!r} is not NFC-normalized")
            if key in normalized:
                raise ContractError(f"{path}: duplicate key {key!r}")
            normalized[key] = _normalize(item, path=f"{path}.{key}")
        return normalized
    raise ContractError(f"{path}: unsupported value type {type(value).__name__}")


def canonical_json_bytes(value: Any) -> bytes:
    normalized = _normalize(value)
    return json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def domain_hash(domain: str, value: Any) -> str:
    if not ID_RE.fullmatch(domain):
        raise ContractError(f"invalid hash domain {domain!r}")
    return hashlib.sha256(domain.encode("ascii") + b"\x00" + canonical_json_bytes(value)).hexdigest()


def content_hash(content: dict[str, Any]) -> str:
    return "nkh1:" + domain_hash("nk-id-content-v1", content)


def claim_id(claim_identity: dict[str, Any]) -> str:
    return "nkc1:" + domain_hash("nk-id-claim-v1", claim_identity)


def lineage_id(lineage_seed: dict[str, Any]) -> str:
    return "nkl1:" + domain_hash("nk-id-lineage-v1", lineage_seed)


def payload_hash(payload: Any) -> str:
    return "nkp1:" + domain_hash("nk-event-payload-v1", payload)


def event_hash(envelope_without_hash: dict[str, Any]) -> str:
    return "nke1:" + domain_hash("nk-event-envelope-v1", envelope_without_hash)


@dataclass
class Check:
    check_id: str
    status: str
    detail: str


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_pack() -> dict[str, Any]:
    return load_json(PACK)


def validate_registry(checks: list[Check]) -> None:
    registry = load_json(REGISTRY)
    seen: set[str] = set()
    for family in registry["families"]:
        for assertion in family["assertions"]:
            assertion_id = assertion["assertion_id"]
            if assertion_id in seen:
                raise ContractError(f"duplicate assertion id {assertion_id}")
            seen.add(assertion_id)
    checks.append(Check("registry.unique_assertions", "PASS", f"{len(seen)} assertion IDs are unique"))


def validate_identity(checks: list[Check]) -> None:
    golden = load_pack()["identity_golden"]
    for vector in golden["vectors"]:
        actual = (
            content_hash(vector["content"]),
            claim_id(vector["claim_identity"]),
            lineage_id(vector["lineage_seed"]),
        )
        expected = vector["expected"]
        if actual != (expected["content_hash"], expected["claim_id"], expected["lineage_id"]):
            raise ContractError(f"identity vector {vector['vector_id']} mismatch")
    checks.append(Check("identity.golden", "PASS", f"{len(golden['vectors'])} golden vectors matched"))

    invalid = load_pack()["identity_invalid"]
    rejected = 0
    for vector in invalid["vectors"]:
        try:
            content_hash(vector["input"])
        except (ContractError, TypeError, ValueError):
            rejected += 1
        else:
            raise ContractError(f"invalid identity vector {vector['vector_id']} was accepted")
    checks.append(Check("identity.invalid", "PASS", f"{rejected} invalid vectors rejected"))


def _build_event(event: dict[str, Any]) -> dict[str, Any]:
    envelope = dict(event)
    envelope["payload_hash"] = payload_hash(envelope["payload"])
    without_hash = dict(envelope)
    without_hash.pop("event_hash", None)
    envelope["event_hash"] = event_hash(without_hash)
    return envelope


def validate_events(checks: list[Check]) -> None:
    corpus = load_pack()["event_scenarios"]
    for scenario in corpus["scenarios"]:
        previous = "GENESIS"
        expected_global = 1
        stream_seq: dict[str, int] = {}
        for event in scenario["events"]:
            if event["global_seq"] != expected_global:
                raise ContractError(f"{scenario['scenario_id']}: non-contiguous global_seq")
            expected_global += 1
            stream = event["stream_id"]
            expected_stream = stream_seq.get(stream, 0) + 1
            if event["stream_seq"] != expected_stream:
                raise ContractError(f"{scenario['scenario_id']}: invalid stream_seq for {stream}")
            stream_seq[stream] = expected_stream
            if event["prev_global_hash"] != previous:
                raise ContractError(f"{scenario['scenario_id']}: previous hash mismatch")
            built = _build_event(event)
            if built["event_hash"] != event["event_hash"]:
                raise ContractError(f"{scenario['scenario_id']}: event hash mismatch")
            previous = event["event_hash"]
        if scenario["expected_outcome"] not in {"ACCEPT", "REJECT", "RECOVER"}:
            raise ContractError(f"{scenario['scenario_id']}: unknown expected outcome")
    checks.append(Check("events.scenarios", "PASS", f"{len(corpus['scenarios'])} event scenarios validated"))


def validate_deletion(checks: list[Check]) -> None:
    corpus = load_pack()["deletion_scenarios"]
    allowed = {
        "ACTIVE": {"RESTRICTED", "ERASE_REQUESTED", "RETENTION_HOLD"},
        "RESTRICTED": {"ACTIVE", "ERASE_REQUESTED", "RETENTION_HOLD"},
        "ERASE_REQUESTED": {"ERASURE_IN_PROGRESS", "RETENTION_HOLD", "FAILED_RETRYABLE"},
        "ERASURE_IN_PROGRESS": {"PARTIALLY_ERASED", "CRYPTO_ERASED", "PHYSICALLY_ERASED", "FAILED_RETRYABLE"},
        "PARTIALLY_ERASED": {"ERASURE_IN_PROGRESS", "FAILED_RETRYABLE", "PHYSICALLY_ERASED", "CRYPTO_ERASED"},
        "FAILED_RETRYABLE": {"ERASURE_IN_PROGRESS", "RETENTION_HOLD"},
        "RETENTION_HOLD": {"RESTRICTED", "ERASE_REQUESTED"},
        "CRYPTO_ERASED": set(),
        "PHYSICALLY_ERASED": set(),
    }
    for scenario in corpus["scenarios"]:
        state = scenario["initial_state"]
        for transition in scenario["transitions"]:
            target = transition["to"]
            if target not in allowed.get(state, set()):
                raise ContractError(f"{scenario['scenario_id']}: forbidden {state}->{target}")
            state = target
        if state != scenario["expected_final_state"]:
            raise ContractError(f"{scenario['scenario_id']}: final state mismatch")
        if scenario["receipt"]["claims_complete_global_erasure"]:
            raise ContractError(f"{scenario['scenario_id']}: Receipt exceeds proof boundary")
    checks.append(Check("deletion.scenarios", "PASS", f"{len(corpus['scenarios'])} deletion scenarios validated"))


def validate_epistemic(checks: list[Check]) -> None:
    corpus = load_pack()["epistemic_scenarios"]
    expected_ids = {f"NK-EPI-{index:03d}" for index in range(1, 9)}
    seen: set[str] = set()
    polarities: dict[str, set[str]] = {}
    for scenario in corpus["scenarios"]:
        assertion_id = scenario["assertion_id"]
        seen.add(assertion_id)
        polarities.setdefault(assertion_id, set()).add(scenario["polarity"])
        if scenario["expected_result"] not in {"ACCEPT", "REJECT"}:
            raise ContractError(f"{scenario['scenario_id']}: invalid expected result")
    if seen != expected_ids:
        raise ContractError(f"epistemic assertion coverage mismatch: {sorted(expected_ids - seen)} missing")
    for assertion_id in expected_ids:
        if polarities[assertion_id] != {"positive", "negative"}:
            raise ContractError(f"{assertion_id}: requires positive and negative fixtures")
    checks.append(Check("epistemic.coverage", "PASS", "NK-EPI-001..008 each have positive and negative fixtures"))


def run_adapter(command: list[str], output: Path) -> None:
    completed = subprocess.run(command + [str(PACK)], cwd=ROOT, check=False, text=True, capture_output=True)
    if completed.returncode != 0:
        raise SystemExit(completed.stderr or completed.stdout or f"adapter exited {completed.returncode}")
    try:
        report = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"adapter did not emit JSON: {exc}") from exc
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate_pack(output: Path | None) -> int:
    checks: list[Check] = []
    try:
        validate_registry(checks)
        validate_identity(checks)
        validate_events(checks)
        validate_deletion(checks)
        validate_epistemic(checks)
    except (ContractError, KeyError, OSError, json.JSONDecodeError) as exc:
        checks.append(Check("fixture-pack", "FAIL", str(exc)))

    passed = all(check.status == "PASS" for check in checks)
    report = {
        "report_version": "nk-evidence-report/1",
        "profile_id": "fixture-integrity/python-stdlib-v1",
        "support_state": "SUPPORTED" if passed else "FAILED",
        "kernel_runtime_conformance": "UNSUPPORTED",
        "evidence_level": "LOCALLY_TESTED",
        "checks": [asdict(check) for check in checks],
        "limitations": [
            "Validates contract fixtures and deterministic reference algorithms only.",
            "Does not implement Native Kernel runtime semantics.",
            "Does not establish C2 until committed CI evidence exists.",
            "Does not establish C3 without two materially independent profiles.",
        ],
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if output:
        output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if passed else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Native Kernel contract fixtures or invoke a profile adapter")
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate")
    validate.add_argument("--output", type=Path)
    adapter = subparsers.add_parser("adapter")
    adapter.add_argument("--output", type=Path, required=True)
    adapter.add_argument("adapter_command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.command == "validate":
        return validate_pack(args.output)
    if not args.adapter_command:
        parser.error("adapter command is required")
    adapter_command = args.adapter_command[1:] if args.adapter_command[0] == "--" else args.adapter_command
    run_adapter(adapter_command, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
