from pages.mouseover_page import MouseoverPage


class TestMouseoverPage(MouseoverPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/mouseover")

    def test_hover(self):
        self.hover_over_element("#mouseoverButton")
        assert self.page.is_visible("#mouseoverMessage")

    def teardown_class(self):
        self.page.quit()
