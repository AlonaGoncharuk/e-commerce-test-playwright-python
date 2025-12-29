from __future__ import annotations

def money_to_float(text: str) -> float:
    """Convert '$1,234.56' -> 1234.56 (best effort)."""
    clean = text.strip().replace("$", "").replace(",", "")
    return float(clean)

def float_to_money(value: float) -> str:
    """Convert 1234.56 -> '$1,234.56' (best effort)."""
    return f"${value:,.2f}"
