from pages.web.base_page import BasePage

from typing import Self


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

    def go(self) -> Self:
        self.page.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.page.get_title()
