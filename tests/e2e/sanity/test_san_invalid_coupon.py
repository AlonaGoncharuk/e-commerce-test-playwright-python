from __future__ import annotations

import pytest

from framework.data.coupons import INVALID_COUPON
from framework.utils.url import extract_product_id_from_url


@pytest.mark.sanity
def test_invalid_coupon_shows_error(home, product, cart):
    home.open().wait_until_loaded()
    home.open_first_product()
    product.wait_until_loaded()
    product_id = extract_product_id_from_url(product.page.url)

    product.click_add_to_cart()
    product.header.go_cart()

    cart.assert_has_items()
    cart.item(product_id).assert_visible()

    cart.coupon.apply(INVALID_COUPON)
    cart.coupon.assert_error_contains("Invalid coupon")

