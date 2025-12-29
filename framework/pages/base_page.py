from __future__ import annotations

from playwright.sync_api import Page, Locator, expect

from framework.config import Settings


class BasePage:

    def __init__(self, page: Page, settings: Settings):
        self.page = page
        self.settings = settings
        self.page.set_default_timeout(settings.default_timeout_ms)

    def goto(self, path: str, *, wait_until: str = "domcontentloaded") -> None:
        if not path.startswith("/"):
            path = f"/{path}"
        base = self.settings.base_url.rstrip("/")
        self.page.goto(f"{base}{path}", wait_until=wait_until)

    def by_test_id(self, test_id: str) -> Locator:
        return self.page.get_by_test_id(test_id)

    def wait_for_network_idle(self) -> None:
        self.page.wait_for_load_state("networkidle")

    def assert_url_contains(self, fragment: str) -> None:
        assert fragment in self.page.url, f"Expected URL to contain '{fragment}', got '{self.page.url}'"

    def assert_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible()
