from __future__ import annotations

from playwright.sync_api import Page, Locator, expect


class CouponInputComponent:
    def __init__(self, page: Page):
        self.page = page

    @property
    def input(self) -> Locator:
        return self.page.get_by_test_id("coupon-input")

    @property
    def apply_button(self) -> Locator:
        return self.page.get_by_test_id("apply-coupon")

    @property
    def error(self) -> Locator:
        return self.page.get_by_test_id("coupon-error")

    @property
    def applied_banner(self) -> Locator:
        return self.page.get_by_test_id("coupon-applied")

    @property
    def remove_coupon(self) -> Locator:
        return self.page.get_by_test_id("remove-coupon")

    def apply(self, code: str) -> None:
        self.input.fill(code)
        self.apply_button.click()

    def assert_applied(self) -> None:
        expect(self.applied_banner).to_be_visible()

    def remove(self) -> None:
        self.remove_coupon.click()

    def assert_error_contains(self, text: str) -> None:
        expect(self.error).to_be_visible()
        expect(self.error).to_contain_text(text)

    def assert_error_not_visible(self) -> None:
        expect(self.error).to_be_hidden()
