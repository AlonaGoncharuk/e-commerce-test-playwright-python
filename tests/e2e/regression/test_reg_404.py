from __future__ import annotations

import pytest


@pytest.mark.regression
def test_invalid_route_shows_not_found(page, settings, not_found):
    page.goto(f"{settings.base_url}/some-route-that-does-not-exist")
    not_found.assert_visible()
