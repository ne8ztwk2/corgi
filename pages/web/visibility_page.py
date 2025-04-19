from pages.base_page import BasePage
from typing import Self


class VisibilityPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/verifytext"
        self.hide_button_selector = "#hideButton"

    def check_element_visibility(self, selector): ...
    def click_hide_button(self):
        self.page.find(self.hide_button_selector).click()

    def go(self) -> Self:
        self.page.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.page.get_title()
