from pages.base_page import BasePage
from typing import Self


class DynamicidPage:

    def __init__(self, page: BasePage):

        self.url = "https://www.uitestingplayground.com/dynamicid"
        self.page = page

        self.button_selector = ".btn.btn-primary"

    @property
    def get_button_id(self) -> str:
        return self.page.find(self.button_selector).get_attribute("id")

    @property
    def get_title(self) -> str:
        return self.page.get_title()

    def go(self) -> Self:
        self.page.goto(self.url)
        return self
