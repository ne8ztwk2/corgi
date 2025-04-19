from pages.shadowdom_page import ShadowdomPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestShadowdomPage(ShadowdomPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/shadowdom")

    def test_interact_with_shadow_dom(self):
        self.interact_with_shadow_dom()
        assert self.page.is_visible("#shadowMessage")

    def teardown_class(self):
        self.page.quit()
