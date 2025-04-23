from pages.web.base_page import BasePage

from typing import Self


class DisabledinputPage:
    def __init__(self, basepage: BasePage):
        self.url = "https://www.uitestingplayground.com/disabledinput"
        self.basepage = basepage
        self.input_selector = "#inputField"
        self.min_need_time = 5.5

    def delay_input(self, time: float = None):
        self.basepage.wait_editable(self.input_selector, time or self.min_need_time)

    def input_text(self, text: str):
        self.basepage.find(self.input_selector).input(text)

    def open(self) -> Self:
        self.basepage.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.basepage.get_title()
