from pages.visibility_page import VisibilityPage


class TestVisibilityPage(VisibilityPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/visibility")

    def test_element_visibility(self):
        assert self.check_element_visibility("#hideButton")

    def teardown_class(self):
        self.page.quit()
