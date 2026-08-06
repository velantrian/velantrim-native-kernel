from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .errors import AuthorityDenied
from .models import Command, EventType


@dataclass(frozen=True, slots=True)
class AuthorityGrant:
    authority_ref: str
    actor_ref: str
    policy_ref: str
    authority_kind: str
    allowed_event_types: tuple[EventType, ...]
    stream_prefixes: tuple[str, ...] = ("",)

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


class StaticAuthorityPolicy:
    """Deterministic, explicit, deny-by-default authority adapter for P1 tests."""

    def __init__(self, grants: Iterable[AuthorityGrant]) -> None:
        self._grants = tuple(grants)

    def decide(self, command: Command) -> AuthorityDecision:
        for grant in self._grants:
            if grant.permits(command):
                return AuthorityDecision(
                    allowed=True,
                    authority_kind=grant.authority_kind,
                    scope=f"stream:{command.stream_id}",
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
            scope=f"stream:{command.stream_id}",
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
