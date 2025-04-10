from pages.base_page import BasePage


class ProgressbarPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def start_progress(self):
        self.page.click("#startButton")

    def stop_progress(self):
        self.page.click("#stopButton")
