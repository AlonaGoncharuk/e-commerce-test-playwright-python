from __future__ import annotations

from playwright.sync_api import expect

from framework.pages.base_page import BasePage


class NotFoundPage(BasePage):
    @property
    def root(self):
        return self.by_test_id("not-found-page")

    def assert_visible(self) -> None:
        expect(self.root).to_be_visible()

    def go_home(self) -> None:
        self.by_test_id("go-home").click()
