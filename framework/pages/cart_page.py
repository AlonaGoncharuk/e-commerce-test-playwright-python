from __future__ import annotations

from playwright.sync_api import expect

from framework.pages.base_page import BasePage
from framework.components.header import HeaderComponent
from framework.components.coupon_input import CouponInputComponent
from framework.components.cart_item import CartItemComponent
from framework.pages.home_page import HomePage
from framework.utils.money import money_to_float


class CartPage(BasePage):
    PATH = "/cart"

    @property
    def header(self) -> HeaderComponent:
        return HeaderComponent(self.page)

    @property
    def coupon(self) -> CouponInputComponent:
        return CouponInputComponent(self.page)

    def item(self, product_id: str) -> CartItemComponent:
        return CartItemComponent(self.page, product_id)

    @property
    def empty_cart(self):
        return self.by_test_id("empty-cart")

    @property
    def cart_items_container(self):
        return self.by_test_id("cart-items")

    @property
    def proceed_to_checkout(self):
        return self.by_test_id("proceed-to-checkout")

    @property
    def subtotal(self):
        return self.by_test_id("subtotal")

    @property
    def discount_amount(self):
        return self.by_test_id("discount-amount")

    @property
    def total(self):
        return self.by_test_id("cart-total")

    @property
    def continue_shopping_btn(self):
        return self.by_test_id("continue-shopping")

    def open(self) -> CartPage:
        self.goto(self.PATH)
        return self

    def assert_has_items(self) -> CartPage:
        expect(self.cart_items_container).to_be_visible()
        return self

    def go_to_checkout(self) -> None:
        self.proceed_to_checkout.click()

    def get_subtotal_value(self) -> float:
        return money_to_float(self.subtotal.inner_text())

    def get_total_value(self) -> float:
        return money_to_float(self.total.inner_text())

    def assert_empty_cart(self) -> CartPage:
        expect(self.empty_cart).to_be_visible()
        return self

    def continue_shopping(self) -> HomePage:
        self.continue_shopping_btn.click()
        return HomePage(self.page, self.settings)
