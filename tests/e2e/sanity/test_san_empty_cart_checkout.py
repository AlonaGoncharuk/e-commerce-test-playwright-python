from __future__ import annotations

import pytest


@pytest.mark.sanity
def test_checkout_empty_cart_message(cart, home):
    cart.open()
    cart.assert_empty_cart()
    cart.continue_shopping()
    home.assert_on_page()

