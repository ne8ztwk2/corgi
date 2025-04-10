from pages.nbsp_page import NbspPage


class TestNbspPage(NbspPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/nbsp")

    def test_click_nbsp_button(self):
        self.click_nbsp_button()
        assert self.page.is_visible("#buttonClickedMessage")

    def teardown_class(self):
        self.page.quit()
