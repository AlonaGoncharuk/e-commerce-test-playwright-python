from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class CustomerInfo:
    full_name: str
    email: str
    address: str
    city: str
    country: str


DEFAULT_CUSTOMER = CustomerInfo(
    full_name="Automation Tester",
    email="auto.tester@example.com",
    address="1 Automation Street",
    city="Tel Aviv",
    country="Israel",
)
