from pages.progressbar_page import ProgressbarPage


class TestProgressbarPage(ProgressbarPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/progressbar")

    def test_progress_bar(self):
        self.start_progress()
        self.stop_progress()
        progress_value = self.page.get_attribute("#progressBar", "aria-valuenow")
        assert progress_value is not None

    def teardown_class(self):
        self.page.quit()
