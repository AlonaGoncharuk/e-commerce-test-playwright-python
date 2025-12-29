from __future__ import annotations

from playwright.sync_api import Page, Locator, expect


class ProductCardComponent:
    def __init__(self, page: Page, product_id: str):
        self.page = page
        self.product_id = product_id

    @property
    def root(self) -> Locator:
        return self.page.get_by_test_id(f"product-card-{self.product_id}")

    @property
    def add_to_cart(self) -> Locator:
        return self.page.get_by_test_id(f"add-to-cart-{self.product_id}")

    def assert_visible(self) -> None:
        expect(self.root).to_be_visible()

    def open_details(self) -> None:
        self.root.locator("a").first.click()

    def click_add_to_cart(self) -> None:
        self.add_to_cart.click()

    def assert_add_to_cart_button_visible(self) -> None:
        expect(self.add_to_cart).to_be_visible()
