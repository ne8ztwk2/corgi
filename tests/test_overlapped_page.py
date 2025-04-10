from pages.overlapped_page import OverlappedPage


class TestOverlappedPage(OverlappedPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/overlapped")

    def test_fill_input(self):
        self.fill_input("Test Input")
        input_value = self.page.get_attribute("#overlappedInput", "value")
        assert input_value == "Test Input"

    def teardown_class(self):
        self.page.quit()
