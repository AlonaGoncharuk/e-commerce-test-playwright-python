from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Settings:

    base_url: str = "https://alonas-testing-store.lovable.app"
    default_timeout_ms: int = 10_000
