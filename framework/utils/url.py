from __future__ import annotations

def extract_product_id_from_url(url: str) -> str:
    # expects .../product/<id>
    parts = url.split("/")
    if "product" not in parts:
        raise ValueError(f"URL does not contain '/product/': {url}")
    idx = parts.index("product")
    if idx + 1 >= len(parts) or not parts[idx + 1]:
        raise ValueError(f"Cannot extract product id from: {url}")
    return parts[idx + 1]
