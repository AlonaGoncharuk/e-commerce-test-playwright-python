from __future__ import annotations

import pytest

from framework.config import Settings
from framework.pages.home_page import HomePage
from framework.pages.product_page import ProductPage
from framework.pages.cart_page import CartPage
from framework.pages.checkout_page import CheckoutPage
from framework.pages.confirmation_page import OrderConfirmationPage
from framework.pages.not_found_page import NotFoundPage


@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings()


@pytest.fixture(autouse=True)
def isolate_storage(page):
    # Run before any page loads in the context
    page.add_init_script("() => { localStorage.clear(); sessionStorage.clear(); }")


@pytest.fixture
def home(page, settings: Settings) -> HomePage:
    return HomePage(page, settings)


@pytest.fixture
def product(page, settings: Settings) -> ProductPage:
    return ProductPage(page, settings)


@pytest.fixture
def cart(page, settings: Settings) -> CartPage:
    return CartPage(page, settings)


@pytest.fixture
def checkout(page, settings: Settings) -> CheckoutPage:
    return CheckoutPage(page, settings)


@pytest.fixture
def confirmation(page, settings: Settings) -> OrderConfirmationPage:
    return OrderConfirmationPage(page, settings)


@pytest.fixture
def not_found(page, settings: Settings) -> NotFoundPage:
    return NotFoundPage(page, settings)
