from pages.base_page import BasePage

from typing import Self


class DisabledinputPage:
    def __init__(self, page: BasePage):
        self.url = "https://www.uitestingplayground.com/disabledinput"
        self.page = page
        self.input_selector = "#inputField"
        self.min_need_time = 5.5

    def check_input_disabled(self):
        return self.page.find(self.input_selector).get_attribute("disabled")

    def delay_input(self, time: float = None):
        self.page.find(self.input_selector).wait_editable(time or self.min_need_time)

    def input_text(self, text: str):
        self.page.find(self.input_selector).input(text)

    def go(self) -> Self:
        self.page.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.page.get_title()
