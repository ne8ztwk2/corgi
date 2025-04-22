from pages.web.autowait_page import AutowaitPage

import pytest


class TestAutowaitPage:

    @pytest.fixture(autouse=True)
    def setup(self, basepage):
        self.page = AutowaitPage(basepage)
        self.page.open()
        yield
        self.page.close()

    def test_click_button(self):
        self.click_button()

    def teardown_class(self):
        self.page.quit()
