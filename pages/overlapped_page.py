from pages.base_page import BasePage

from typing import Self


class OverlappedPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/overlapped"

        self.name_input_selector = "#name"
        self.id_input_selector = "#id"
        self.subject_input_selector = "#subject"

    def input_id(self, text: str):
        self.page.execute_script(
            f"arguments[{self.page.find(self.id_input_selector)}].scrollIntoView(true);"
        )
        self.page.find(self.id_input_selector).input(text)

    def input_name(self, text: str):
        self.page.execute_script(
            f"arguments[{self.page.find(self.name_input_selector)}].scrollIntoView(true);"
        )
        self.page.find(self.name_input_selector).input(text)

    def input_subject(self, text: str):
        self.page.execute_script(
            f"arguments[{self.page.find(self.subject_input_selector)}].scrollIntoView(true);"
        )
        self.page.find(self.subject_input_selector).input(text)

    def go(self) -> Self:
        self.page.goto(self.url)
        return self
