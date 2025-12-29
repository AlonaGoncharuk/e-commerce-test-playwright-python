from __future__ import annotations

from playwright.sync_api import expect

from framework.pages.base_page import BasePage
from framework.components.header import HeaderComponent
from framework.components.product_filters import ProductFiltersComponent


class HomePage(BasePage):
    PATH = "/"

    @property
    def header(self) -> HeaderComponent:
        return HeaderComponent(self.page)

    @property
    def filters(self) -> ProductFiltersComponent:
        return ProductFiltersComponent(self.page)

    @property
    def title(self):
        return self.by_test_id("page-title")

    @property
    def products_grid(self):
        return self.by_test_id("products-grid")

    @property
    def loading_spinner(self):
        return self.by_test_id("loading-spinner")

    def open(self) -> HomePage:
        self.goto(self.PATH)
        return self

    def wait_until_loaded(self) -> HomePage:
        # Spinner exists while loading. After load, it's removed.
        if self.loading_spinner.is_visible():
            expect(self.loading_spinner).to_be_hidden()
        expect(self.title).to_be_visible()
        return self

    def open_first_product(self) -> None:
        expect(self.products_grid).to_be_visible()
        self.products_grid.locator("a").first.click()

    def assert_on_page(self) -> HomePage:
        expect(self.products_grid).to_be_visible()
        return self.wait_until_loaded()
