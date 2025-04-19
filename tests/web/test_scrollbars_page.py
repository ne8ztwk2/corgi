from pages.scrollbars_page import ScrollbarsPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestScrollbarsPage(ScrollbarsPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/scrollbars")

    def test_click_hidden_button(self):
        self.click_hidden_button()
        assert self.page.is_visible("#hidingButton")

    def teardown_class(self):
        self.page.quit()
