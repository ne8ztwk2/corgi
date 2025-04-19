from pages.mouseover_page import MouseoverPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestMouseoverPage:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        self.page = MouseoverPage(browser)
        self.page.go("https://www.uitestingplayground.com/mouseover")
        yield
        self.page.base_page.quit()

    @pytest.mark.parametrize("times", [1, 10])
    def test_click_me(self, times: int):
        self.page.click_click_me(times)
        click_me_count = self.page.get_click_me_count()
        assert click_me_count == str(times)

    @pytest.mark.parametrize("times", [1, 10])
    def test_click_link_button(self, times: int):
        self.page.click_link_button(times)
        click_link_button_count = self.page.get_click_button_count()
        assert click_link_button_count == str(times)
