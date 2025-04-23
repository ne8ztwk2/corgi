from pages.web.dynamicid_page import DynamicidPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestDynamicidPage:

    @pytest.fixture(autouse=True)
    def setup(self, basepage):
        self.page = DynamicidPage(basepage)
        self.page.open()
        yield

    def test_delay_input(self):
        text = "test input"
        self.page.click_button()
        self.page.delay_input(text, 5.5)
        self.page.get_value() == text
