from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from collections.abc import Mapping, Sequence
from types import MappingProxyType
from typing import Any

from .errors import ContractViolation

_DOMAIN_RE = re.compile(r"^[a-z0-9][a-z0-9._:/-]{0,127}$")


def normalize_canonical(value: Any, *, path: str = "$") -> Any:
    """Validate and normalize the nk-id/1 canonical JSON subset.

    Inputs must already use NFC strings. Explicit null and floating-point values
    are forbidden. The returned value contains only JSON-compatible primitives.
    """
    if value is None:
        raise ContractViolation(
            f"{path}: null is forbidden in canonical identity objects; omit optional fields"
        )
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        raise ContractViolation(
            f"{path}: floating-point numbers are forbidden; use an integer or canonical decimal string"
        )
    if isinstance(value, str):
        normalized = unicodedata.normalize("NFC", value)
        if normalized != value:
            raise ContractViolation(f"{path}: string is not NFC-normalized")
        return value
    if isinstance(value, Mapping):
        normalized_object: dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise ContractViolation(f"{path}: object keys must be strings")
            normalized_key = unicodedata.normalize("NFC", key)
            if normalized_key != key:
                raise ContractViolation(f"{path}: key {key!r} is not NFC-normalized")
            if key in normalized_object:
                raise ContractViolation(f"{path}: duplicate key {key!r}")
            normalized_object[key] = normalize_canonical(item, path=f"{path}.{key}")
        return normalized_object
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [
            normalize_canonical(item, path=f"{path}[{index}]")
            for index, item in enumerate(value)
        ]
    raise ContractViolation(f"{path}: unsupported value type {type(value).__name__}")


def canonical_json_bytes(value: Any) -> bytes:
    normalized = normalize_canonical(value)
    return json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def domain_hash(domain: str, value: Any) -> str:
    if not _DOMAIN_RE.fullmatch(domain):
        raise ContractViolation(f"invalid hash domain {domain!r}")
    digest = hashlib.sha256(
        domain.encode("ascii") + b"\x00" + canonical_json_bytes(value)
    ).hexdigest()
    return digest


def content_hash(content: Mapping[str, Any]) -> str:
    return "nkh1:" + domain_hash("nk-id-content-v1", content)


def claim_id(claim_identity: Mapping[str, Any]) -> str:
    return "nkc1:" + domain_hash("nk-id-claim-v1", claim_identity)


def lineage_id(lineage_seed: Mapping[str, Any]) -> str:
    return "nkl1:" + domain_hash("nk-id-lineage-v1", lineage_seed)


def command_digest(command: Mapping[str, Any]) -> str:
    """Return the provisional P1 command digest.

    ``nkd0`` is a clean-profile implementation detail, not an accepted
    cross-profile identity contract.
    """
    return "nkd0:" + domain_hash("nk-p1-command-v0", command)


def state_digest(state: Mapping[str, Any]) -> str:
    """Return a deterministic P1 reducer-state digest.

    ``nks0`` is local evidence for reducer determinism, not a C2/C3 contract.
    """
    return "nks0:" + domain_hash("nk-p1-state-v0", state)


def freeze_json(value: Any) -> Any:
    normalized = normalize_canonical(value)
    if isinstance(normalized, dict):
        return MappingProxyType({key: freeze_json(item) for key, item in normalized.items()})
    if isinstance(normalized, list):
        return tuple(freeze_json(item) for item in normalized)
    return normalized


def thaw_json(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {key: thaw_json(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [thaw_json(item) for item in value]
    return value
