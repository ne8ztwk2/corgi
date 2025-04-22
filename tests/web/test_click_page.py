from pages.web.click_page import ClickPage

import pytest


class TestClickPage:

    @pytest.fixture(autouse=True)
    def setup(self, basepage):
        self.page = ClickPage(basepage)
        self.page.open()
        yield
        self.page.close()

    def test_click_button(self):
        self.click_button()
        button_class = self.page.get_button_class()
        assert "btn-success" in button_class
