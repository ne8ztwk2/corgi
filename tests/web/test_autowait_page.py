from pages.autowait_page import AutowaitPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestAutowaitPage(AutowaitPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/autowait")

    def test_click_button(self):
        self.click_button()
        assert self.page.is_visible("#autoWaitMessage")

    def teardown_class(self):
        self.page.quit()


        
