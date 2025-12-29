from __future__ import annotations

def assert_order_id_format(order_id: str) -> None:
    assert order_id.startswith("ORD-"), f"Expected order id to start with 'ORD-', got: {order_id}"

def assert_order_id_length(order_id: str, expected_length: int) -> None:
    assert len(order_id) == expected_length, f"Expected order id length {expected_length}, got: {len(order_id)}"
