from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .errors import AuthorityDenied, ContractViolation
from .models import Command, EventType


def _nonempty(name: str, value: object) -> str:
    if not isinstance(value, str) or not value:
        raise ContractViolation(f"{name} must be a non-empty string")
    return value


def _nonempty_strings(name: str, values: tuple[str, ...]) -> None:
    if not values or any(not isinstance(value, str) or not value for value in values):
        raise ContractViolation(f"{name} must contain non-empty strings")


@dataclass(frozen=True, slots=True)
class AuthorityGrant:
    authority_ref: str
    actor_ref: str
    policy_ref: str
    authority_kind: str
    allowed_event_types: tuple[EventType, ...]
    stream_prefixes: tuple[str, ...] = ("stream:",)

    def __post_init__(self) -> None:
        _nonempty("authority_ref", self.authority_ref)
        _nonempty("actor_ref", self.actor_ref)
        _nonempty("policy_ref", self.policy_ref)
        _nonempty("authority_kind", self.authority_kind)
        if not self.allowed_event_types or any(
            not isinstance(event_type, EventType) for event_type in self.allowed_event_types
        ):
            raise ContractViolation("allowed_event_types must contain EventType values")
        _nonempty_strings("stream_prefixes", self.stream_prefixes)

    def permits(self, command: Command) -> bool:
        return (
            command.authority_ref == self.authority_ref
            and command.actor_ref == self.actor_ref
            and command.event_type in self.allowed_event_types
            and any(command.stream_id.startswith(prefix) for prefix in self.stream_prefixes)
        )


@dataclass(frozen=True, slots=True)
class AuthorityDecision:
    allowed: bool
    authority_kind: str
    scope: str
    policy_ref: str
    actor_ref: str
    authority_ref: str
    basis: tuple[str, ...]
    limitations: tuple[str, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.allowed, bool):
            raise ContractViolation("allowed must be boolean")
        for name in (
            "authority_kind",
            "scope",
            "policy_ref",
            "actor_ref",
            "authority_ref",
        ):
            _nonempty(name, getattr(self, name))
        _nonempty_strings("basis", self.basis)
        _nonempty_strings("limitations", self.limitations)


class StaticAuthorityPolicy:
    """Deterministic, explicit, deny-by-default authority adapter for P1 tests."""

    def __init__(self, grants: Iterable[AuthorityGrant]) -> None:
        self._grants = tuple(grants)
        if any(not isinstance(grant, AuthorityGrant) for grant in self._grants):
            raise ContractViolation("grants must contain AuthorityGrant values")

    def decide(self, command: Command) -> AuthorityDecision:
        if not isinstance(command, Command):
            raise ContractViolation("command must be a Command")
        for grant in self._grants:
            if grant.permits(command):
                return AuthorityDecision(
                    allowed=True,
                    authority_kind=grant.authority_kind,
                    scope=command.stream_id,
                    policy_ref=grant.policy_ref,
                    actor_ref=command.actor_ref,
                    authority_ref=command.authority_ref,
                    basis=("explicit-static-grant",),
                    limitations=(
                        "P1 deterministic local policy only.",
                        "Decision does not establish truth or storage durability.",
                    ),
                )
        return AuthorityDecision(
            allowed=False,
            authority_kind="none",
            scope=command.stream_id,
            policy_ref="policy:deny-by-default",
            actor_ref=command.actor_ref,
            authority_ref=command.authority_ref,
            basis=("no-matching-explicit-grant",),
            limitations=("Storage presence, retrieval rank and model output are not authority.",),
        )

    def require(self, command: Command) -> AuthorityDecision:
        decision = self.decide(command)
        if not decision.allowed:
            raise AuthorityDenied(
                f"command {command.command_id} denied for {command.actor_ref}/{command.authority_ref}"
            )
        return decision
