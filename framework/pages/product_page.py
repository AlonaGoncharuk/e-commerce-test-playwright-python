from __future__ import annotations

from playwright.sync_api import expect

from framework.pages.base_page import BasePage
from framework.components.header import HeaderComponent


class ProductPage(BasePage):
    @property
    def header(self) -> HeaderComponent:
        return HeaderComponent(self.page)

    @property
    def loading_spinner(self):
        return self.by_test_id("loading-spinner")

    @property
    def name(self):
        return self.by_test_id("product-detail-name")

    @property
    def add_to_cart(self):
        return self.by_test_id("add-to-cart-detail")

    def wait_until_loaded(self) -> ProductPage:
        if self.loading_spinner.is_visible():
            expect(self.loading_spinner).to_be_hidden()
        expect(self.name).to_be_visible()
        return self

    def click_add_to_cart(self) -> None:
        self.add_to_cart.click()
        expect(self.add_to_cart).to_be_hidden()
