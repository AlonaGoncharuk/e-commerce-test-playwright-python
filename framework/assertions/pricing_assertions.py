from __future__ import annotations

def assert_discount_applied(subtotal: float, discount: float, total: float, *, rate: float = 0.10) -> None:
    expected_discount = round(subtotal * rate, 2)
    assert round(discount, 2) == expected_discount, f"Expected discount {expected_discount}, got {discount}"
    assert round(total, 2) == round(subtotal - expected_discount, 2), f"Total mismatch: {total} != {subtotal - expected_discount}"

def assert_discount_rate(rate: float, expected_rate: float) -> None:
    assert round(rate, 2) == expected_rate, f"Expected discount rate {expected_rate}, got {rate}"
