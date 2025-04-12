from pages.base_page import BasePage


class ProgressbarPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/progressbar"
        self.start_button_selector = "#startButton"
        self.stop_button_selector = "#stopButton"
        self.progress_bar_selector = "#progressBar"
        self.result_attribute = "aria-valuenow"

    def start_progress(self):
        self.page.click("#startButton")

    def stop_progress(self):
        self.page.click("#stopButton")

    def get_result(self) -> str:
        return self.page.find(self.progress_bar_selector).get_attribute(
            self.result_attribute
        )
