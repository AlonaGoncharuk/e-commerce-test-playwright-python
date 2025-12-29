from __future__ import annotations

from playwright.sync_api import expect

from framework.pages.base_page import BasePage
from framework.components.header import HeaderComponent
from framework.assertions.order_assertions import assert_order_id_format
from framework.utils.money import money_to_float


class OrderConfirmationPage(BasePage):
    @property
    def header(self) -> HeaderComponent:
        return HeaderComponent(self.page)

    @property
    def root(self):
        return self.by_test_id("order-confirmation")

    @property
    def order_id(self):
        return self.by_test_id("order-id")

    @property
    def order_total(self):
        return self.by_test_id("order-total")

    def assert_visible(self) -> None:
        expect(self.root).to_be_visible()

    def get_order_id(self) -> str:
        return self.order_id.inner_text().strip()

    def assert_order_id(self) -> None:
        assert_order_id_format(self.get_order_id())

    def get_total_value(self) -> float:
        return money_to_float(self.order_total.inner_text())
