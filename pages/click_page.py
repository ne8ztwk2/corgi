from pages.base_page import BasePage
from typing import Self


class ClickPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/click"
        self.button_selector = "#badButton"
        self.button_success_selector = ".btn.btn-success"

    def click_button(self):
        self.page.click(self.button_selector)
        self.page.wait_visible(self.button_success_selector)

    def go(self) -> Self:
        self.page.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.page.get_title()
