import time
from playwright.sync_api import Page, Browser, Playwright, BrowserType
from pages.base_page import BasePage, BaseBrowser, BaseElement
from typing import Self
from playwright.sync_api import sync_playwright
from config import BROWSER_NAME, HEADLESS
from typing import Literal


class PlaywrightPage(BasePage):

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        return self.page.locator(selector=selector).click()

    def input(self, selector: str, text):
        return self.page.locator(selector=selector).fill(text)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector=selector).inner_text()

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

    def go(self):
        self.page.goto(self.url)

    def close(self):
        self.page.close()


class PlaywrightBrowser(BaseBrowser):
    def __init__(self, browser_name: Literal["firefox", "chromium"], headless: bool):
        self.driver: Playwright = None
        self.browser: Browser = None

        self.browser_name = browser_name
        self.headless = headless

    def launch(self) -> PlaywrightPage:
        self.driver = sync_playwright().start()

        if self.browser_name == "chrome":
            self.browser = self.driver.chromium.launch(headless=self.headless)

        elif self.browser_name == "firefox":
            self.browser = self.driver.firefox.launch(headless=self.headless)

        else:
            raise ValueError(f"Playwright 不支持这个浏览器: {BROWSER_NAME}")

        return self.new_page()

    def new_page(self) -> PlaywrightPage:
        return PlaywrightPage(self.browser.new_page())

    def close(self):
        self.browser.close()


if __name__ == "__main__":

    print()
