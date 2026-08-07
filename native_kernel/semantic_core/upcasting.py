from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from typing import Any

from .canonical import freeze_json, thaw_json
from .errors import ContractViolation, UnsupportedVersion

UpcastTransform = Callable[[Mapping[str, Any]], Mapping[str, Any]]


def _version(name: str, value: object) -> str:
    if not isinstance(value, str) or not value:
        raise ContractViolation(f"{name} must be a non-empty string")
    return value


@dataclass(frozen=True, slots=True)
class UpcastStep:
    source_version: str
    target_version: str
    transform: UpcastTransform

    def __post_init__(self) -> None:
        _version("source_version", self.source_version)
        _version("target_version", self.target_version)
        if self.source_version == self.target_version:
            raise ContractViolation("an upcast step must advance to a different version")
        if not callable(self.transform):
            raise ContractViolation("transform must be callable")


@dataclass(frozen=True, slots=True)
class UpcastResult:
    source_version: str
    target_version: str
    applied_steps: tuple[tuple[str, str], ...]
    payload: Mapping[str, Any]

    def __post_init__(self) -> None:
        _version("source_version", self.source_version)
        _version("target_version", self.target_version)
        object.__setattr__(self, "payload", freeze_json(self.payload))


class UpcasterRegistry:
    """Deterministic one-successor schema upcaster registry.

    This is a standard-library semantic helper. It does not define which schema
    versions are accepted by a storage profile; callers provide the target.
    """

    def __init__(self, *, target_version: str, steps: Iterable[UpcastStep] = ()) -> None:
        self.target_version = _version("target_version", target_version)
        indexed: dict[str, UpcastStep] = {}
        for step in steps:
            if not isinstance(step, UpcastStep):
                raise ContractViolation("steps must contain UpcastStep values")
            if step.source_version in indexed:
                raise ContractViolation(
                    f"multiple upcast successors declared for {step.source_version}"
                )
            indexed[step.source_version] = step
        self._steps = indexed
        self._validate_graph()

    def _validate_graph(self) -> None:
        for source in self._steps:
            seen: set[str] = set()
            version = source
            while version != self.target_version and version in self._steps:
                if version in seen:
                    raise ContractViolation(f"cyclic upcaster path at {version}")
                seen.add(version)
                version = self._steps[version].target_version
            if version in seen:
                raise ContractViolation(f"cyclic upcaster path at {version}")

    def upcast(self, source_version: str, payload: Mapping[str, Any]) -> UpcastResult:
        source = _version("source_version", source_version)
        if not isinstance(payload, Mapping):
            raise ContractViolation("payload must be a mapping")
        current_payload = freeze_json(payload)
        current_version = source
        applied: list[tuple[str, str]] = []
        seen: set[str] = set()

        while current_version != self.target_version:
            if current_version in seen:
                raise UnsupportedVersion(f"cyclic upcaster path at {current_version}")
            seen.add(current_version)
            step = self._steps.get(current_version)
            if step is None:
                raise UnsupportedVersion(
                    f"no upcaster path from schema {source} to {self.target_version}"
                )
            transformed = step.transform(freeze_json(thaw_json(current_payload)))
            if not isinstance(transformed, Mapping):
                raise ContractViolation(
                    f"upcaster {step.source_version}->{step.target_version} must return a mapping"
                )
            current_payload = freeze_json(transformed)
            current_version = step.target_version
            applied.append((step.source_version, step.target_version))

        return UpcastResult(
            source_version=source,
            target_version=self.target_version,
            applied_steps=tuple(applied),
            payload=current_payload,
        )


def identity_upcaster_registry(target_version: str = "1") -> UpcasterRegistry:
    return UpcasterRegistry(target_version=target_version)
