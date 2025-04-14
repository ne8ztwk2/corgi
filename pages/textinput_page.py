from pages.base_page import BasePage
from typing import Self


class TextinputPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/textinput"
        self.input_selector = "#newButtonName"
        self.button_selector = "#updatingButton"

    def input_text(self, text):
        self.page.find(self.input_selector).input(text)

    def click_update_button(self):
        self.page.find(self.button_selector).click()

    def get_butten_text(self) -> str:
        return self.page.find(self.button_selector).get_attribute("value")

    def go(self) -> Self:
        self.page.goto(self.url)
        return self
