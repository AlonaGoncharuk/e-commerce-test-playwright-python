from __future__ import annotations

from playwright.sync_api import Page, Locator, expect


class CartItemComponent:
    def __init__(self, page: Page, product_id: str):
        self.page = page
        self.product_id = product_id

    @property
    def root(self) -> Locator:
        return self.page.get_by_test_id(f"cart-item-{self.product_id}")

    @property
    def quantity(self) -> Locator:
        return self.page.get_by_test_id(f"cart-item-quantity-{self.product_id}")

    @property
    def increase(self) -> Locator:
        return self.page.get_by_test_id(f"increase-quantity-{self.product_id}")

    @property
    def decrease(self) -> Locator:
        return self.page.get_by_test_id(f"decrease-quantity-{self.product_id}")

    @property
    def remove(self) -> Locator:
        return self.page.get_by_test_id(f"remove-item-{self.product_id}")

    def assert_visible(self) -> None:
        expect(self.root).to_be_visible()

    def get_quantity(self) -> int:
        return int(self.quantity.inner_text().strip())

    def increase_qty(self, times: int = 1) -> None:
        for _ in range(times):
            self.increase.click()

    def decrease_qty(self, times: int = 1) -> None:
        for _ in range(times):
            self.decrease.click()

    def remove_item(self) -> None:
        self.remove.click()
        expect(self.root).to_be_hidden()
