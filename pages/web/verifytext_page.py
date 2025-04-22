from pages.web.base_page import BasePage
from typing import Self


class VerifytextPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/verifytext"
        self.text_selectors = ".badge-secondary"
        self.index = -1

    def verify_text(self) -> str:
        return self.page.find_all(self.text_selectors)[-1].get_text()

    def go(self) -> Self:
        self.page.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.page.get_title()
