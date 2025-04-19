from pages.disabledinput_page import DisabledinputPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestDisabledinputPage(DisabledinputPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/disabledinput")

    def test_check_input_disabled(self):
        assert self.check_input_disabled()

    def teardown_class(self):
        self.page.quit()
