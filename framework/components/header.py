from __future__ import annotations

from playwright.sync_api import Page, Locator, expect


class HeaderComponent:
    def __init__(self, page: Page):
        self.page = page

    @property
    def logo(self) -> Locator:
        return self.page.get_by_test_id("logo")

    @property
    def nav_home(self) -> Locator:
        return self.page.get_by_test_id("nav-home")

    @property
    def nav_cart(self) -> Locator:
        return self.page.get_by_test_id("nav-cart")

    @property
    def cart_count(self) -> Locator:
        return self.page.get_by_test_id("cart-count")

    def assert_visible(self) -> None:
        expect(self.logo).to_be_visible()
        expect(self.nav_home).to_be_visible()
        expect(self.nav_cart).to_be_visible()

    def go_home(self) -> None:
        self.nav_home.click()

    def go_cart(self) -> None:
        self.nav_cart.click()

    def assert_cart_count(self, expected_count: int) -> None:
        actual_count = self.get_cart_count()
        assert actual_count == expected_count, f"Expected cart count {expected_count}, got {actual_count}"

    def get_cart_count(self) -> int:
        if self.cart_count.is_visible():
            return int(self.cart_count.inner_text().strip())
        return 0
