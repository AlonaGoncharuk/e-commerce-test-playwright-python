from __future__ import annotations

import pytest

from framework.data.customer_info import DEFAULT_CUSTOMER
from framework.utils.url import extract_product_id_from_url


@pytest.mark.smoke
def test_purchase_happy_path(home, product, cart, checkout, confirmation):
    # 1) Home loads
    home.open().wait_until_loaded()
    home.header.assert_visible()

    # 2) Open first product details
    home.open_first_product()
    product.wait_until_loaded()

    # Capture product id from URL so we can reference cart item testids
    product_id = extract_product_id_from_url(product.page.url)

    # 3) Add to the cart and go to the cart
    product.click_add_to_cart()
    product.header.go_cart()

    # 4) Cart has items and proceed to checkout
    cart.assert_has_items()
    cart.item(product_id).assert_visible()
    cart.go_to_checkout()

    # 5) Checkout submit
    checkout.assert_on_page()
    checkout.fill_customer_info(
        full_name=DEFAULT_CUSTOMER.full_name,
        email=DEFAULT_CUSTOMER.email,
        address=DEFAULT_CUSTOMER.address,
        city=DEFAULT_CUSTOMER.city,
        country=DEFAULT_CUSTOMER.country,
    )
    checkout.select_credit_card()
    checkout.submit_order()

    # 6) Confirmation visible and order-id format is correct
    confirmation.assert_visible()
    confirmation.assert_order_id()
