import time
from playwright.sync_api import Page
from pages.base_page import BasePage
from typing import Self


class PlaywrightPage(BasePage):

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        return self.page.locator(selector=selector).click()

    def input(self, selector: str, text):
        return self.page.locator(selector=selector).fill(text)

    @property
    def get_text(self, selector: str) -> str:
        return self.page.locator(selector=selector).inner_text()

    @property
    def get_text_content(self, selector: str) -> str:
        return self.page.locator(selector=selector).text_content()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector=selector).is_visible()

    def screenshot(self, filename: str) -> None:
        return self.page.screenshot(
            path=f"{self.screenshot_dir}{time.strftime(self.strftime, time.localtime())} {filename}.png"
        )

    def get_attribute(self, selector: str, attribute: str) -> str:
        return self.page.locator(selector=selector).get_attribute(attribute)

    def go(self) -> Self:
        self.page.goto(self.url)
        return self


if __name__ == "__main__":

    print()
