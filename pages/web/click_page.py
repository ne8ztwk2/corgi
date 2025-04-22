from pages.web.base_page import BasePage
from typing import Self


class ClickPage:
    def __init__(self, basepage: BasePage):
        self.basepage = basepage
        self.url = "https://www.uitestingplayground.com/click"
        self.button_selector = "#badButton"
        self.button_success_selector = ".btn.btn-success"

    def click_button(self):
        self.basepage.find(self.button_selector).click()
        self.basepage.wait_visible(self.button_success_selector)

    def open(self) -> Self:
        self.basepage.goto(self.url)
        return self

    def get_button_class(self) -> str:
        return self.basepage.find(self.button_success_selector).get_attribute("class")

    def close(self):
        self.basepage.close()

    @property
    def get_title(self) -> str:
        return self.basepage.get_title()
