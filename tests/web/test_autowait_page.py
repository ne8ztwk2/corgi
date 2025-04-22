from pages.web.autowait_page import AutowaitPage

import pytest


class TestAutowaitPage:

    @pytest.fixture(autouse=True)
    def setup(self, basepage):
        self.page = AutowaitPage(basepage)
        self.page.open()
        yield
        self.page.close()

    def test_wait_button_visible(self):
        self.page.choose_element_type("button")
        self.page.select_visible()
        self.page.click_apply_button3()
        self.page.wait_target_visible(4)
        self.page.click_target()
        assert self.page.get_opstatus() == "Target clicked."
