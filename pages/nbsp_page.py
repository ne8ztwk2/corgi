from pages.base_page import BasePage

from typing import Self


class NbspPage:
    def __init__(self, page: BasePage):
        self.url = "https://www.uitestingplayground.com/nbsp"
        self.page = page
        self.button_selector = ".btn.btn-primary"

    def click_nbsp_button(self):
        self.page.find(self.button_selector).click()

    def go(self) -> Self:
        self.page.goto(self.url)
        return self
