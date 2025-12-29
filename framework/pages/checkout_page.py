from __future__ import annotations

from playwright.sync_api import expect

from framework.pages.base_page import BasePage
from framework.components.header import HeaderComponent
from framework.utils.money import money_to_float


class CheckoutPage(BasePage):
    PATH = "/checkout"

    @property
    def header(self) -> HeaderComponent:
        return HeaderComponent(self.page)

    @property
    def title(self):
        return self.by_test_id("checkout-title")

    @property
    def empty_cart_checkout(self):
        return self.by_test_id("empty-cart-checkout")

    @property
    def input_fullname(self):
        return self.by_test_id("input-fullname")

    @property
    def input_email(self):
        return self.by_test_id("input-email")

    @property
    def input_address(self):
        return self.by_test_id("input-address")

    @property
    def input_city(self):
        return self.by_test_id("input-city")

    @property
    def input_country(self):
        return self.by_test_id("input-country")

    @property
    def payment_credit_card(self):
        return self.by_test_id("payment-credit-card")

    @property
    def place_order(self):
        return self.by_test_id("place-order-button")

    @property
    def checkout_total(self):
        return self.by_test_id("checkout-total")

    @property
    def checkout_error(self):
        return self.by_test_id("checkout-error")

    def open(self) -> CheckoutPage:
        self.goto(self.PATH)
        return self

    def assert_on_page(self) -> CheckoutPage:
        expect(self.title).to_be_visible()
        return self

    def assert_empty_cart(self) -> CheckoutPage:
        expect(self.empty_cart_checkout).to_be_visible()
        return self

    def assert_checkout_button_disabled(self) -> CheckoutPage:
        expect(self.place_order).to_be_disabled()
        return self

    def fill_customer_info(self, full_name: str, email: str, address: str, city: str, country: str) -> None:
        self.input_fullname.fill(full_name)
        self.input_email.fill(email)
        self.input_address.fill(address)
        self.input_city.fill(city)
        self.input_country.fill(country)

    def select_credit_card(self) -> None:
        self.payment_credit_card.click()

    def submit_order(self) -> None:
        self.place_order.click()

    def get_total_value(self) -> float:
        return money_to_float(self.checkout_total.inner_text())

    def assert_checkout_error_contains(self, text: str) -> None:
        expect(self.checkout_error).to_be_visible()
        expect(self.checkout_error).to_contain_text(text)
