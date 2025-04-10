from pages.click_page import ClickPage


class TestClickPage(ClickPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/click")

    def test_click_button(self):
        self.click_button()
        button_class = self.page.get_attribute("#badButton", "class")
        assert "btn-success" in button_class

    def teardown_class(self):
        self.page.quit()
