from __future__ import annotations

from playwright.sync_api import Page, Locator, expect


class ProductFiltersComponent:
    def __init__(self, page: Page):
        self.page = page

    @property
    def root(self) -> Locator:
        return self.page.get_by_test_id("product-filters")

    @property
    def search_input(self) -> Locator:
        return self.page.get_by_test_id("search-input")

    @property
    def category_select(self) -> Locator:
        return self.page.get_by_test_id("category-select")

    @property
    def sort_select(self) -> Locator:
        return self.page.get_by_test_id("sort-select")

    def assert_visible(self) -> None:
        expect(self.root).to_be_visible()

    def set_search(self, text: str) -> None:
        self.search_input.fill(text)

    def select_sort(self, sort_option: str) -> None:
        self.sort_select.click()
        self.page.get_by_test_id(f"sort-option-{sort_option}").click()
