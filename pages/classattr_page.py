from pages.base_page import BasePage
from typing import Self


class ClassattrPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/classattr"
        self.blue_button_selector = ".btn-primary"
        self.alert_text = "Primary button pressed"

    def click_blue_button_and_get_text(self) -> str:
        self.page.click(self.blue_button_selector)
        return self.page.get_alert_text()

    def go(self) -> Self:
        self.page.goto(self.url)
        return self
