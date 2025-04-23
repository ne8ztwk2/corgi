from pages.web.disabledinput_page import DisabledinputPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestDisabledinputPage:
    @pytest.fixture(autouse=True)
    def setup(self, basepage):
        self.page = DisabledinputPage(basepage)
        self.page.open()
        yield

    def test_check_input_disabled(self):
        assert self.check_input_disabled()

    def teardown_class(self):
        self.page.quit()
