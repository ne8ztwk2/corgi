from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.web.base_page import BasePage, BaseElement, BaseBrowser
import time
from typing import Literal, Self, Any
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from playwright.sync_api import sync_playwright, Page, Playwright, Browser
from pages.web.selenium_page import SeleniumPage
from pages.web.playwright_page import PlaywrightPage
from pages.web.base_page import BaseBrowser
from pytest import Parser, FixtureRequest, fixture
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumElement(BaseElement):

    def __init__(self, element: WebElement, actions: ActionChains = None):
        self.element = element
        self.timeout = 8
        self.actions = actions

    def click(self):
        self.element.click()

    def input(self, text: str):
        self.element.send_keys(text)

    def get_text(self) -> str | None:
        return self.element.text

    def get_text_content(self) -> str | None:
        return self.element.get_attribute("textContent")

    def get_attribute(self, attribute: str) -> str | None:
        return self.element.get_attribute(attribute)

    def is_visible(self) -> bool:
        return self.element.is_displayed()

    def wait_visible(self, timeout: float = None) -> Self:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of(self.element)
        )

    def wait_enable(self, timeout: float = None) -> Self:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            self.element.is_enabled()
        )

    def wait_editable(self, timeout: float = None) -> Self:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            self.element.is_displayed()
            and self.element.is_enabled()
            and self.element.get_attribute("readonly") is None
        )

    def wait_clickable(self, timeout: float = None) -> Self:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(self.element)
        )

    def wait_non_zero_size(self, timeout: float = None) -> Self:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            self.element_size["width"] > 0 and self.element_size["height"] > 0
        )

    def select_by_value(self, value: str):
        Select(self.element).select_by_value(value)

    def select_by_index(self, index: int):
        Select(self.element).select_by_index(index)

    def select_by_text(self, text: str):
        Select(self.element).select_by_visible_text(text)

    def scroll_into_view(self) -> Self:
        self.element.location_once_scrolled_into_view
        return self

    # actions

    def move(self):
        self.actions.move_to_element(self.element).perform()

    def drag_to(self, target: WebElement):
        self.actions.drag_and_drop(self.element, target).perform()

    def double_click(self):
        self.actions.double_click(self.element).perform()

    def right_click(self):
        self.actions.context_click(self.element).perform()

    def click_hold(self):
        self.actions.click_and_hold(self.element).perform()


class SeleniumPage(BasePage):

    def __init__(self, page: WebDriver):
        self.page = page
        self.strftime = "%Y-%m-%d %H:%M:%S"

    def goto(self, url: str):
        self.page.get(url)

    def screenshot(self, filename: str):
        self.page.save_screenshot(
            f"{self.screenshot_dir}{time.strftime(self.strftime, time.localtime())} {filename}.png"
        )

    def get_title(self) -> str:
        return self.page.title

    def get_url(self) -> str:
        return self.page.current_url

    def close(self):
        self.page.close()

    def quit(self):
        self.page.quit()

    def get_alert_text(self) -> str:
        return Alert(self.page).text

    def execute_script(self, script: Any, *args: Any) -> Any:
        return self.page.execute_script(script, *args)

    def alert(self, action: Literal["accept", "dismiss"], text: str = None):
        if text is not None:
            Alert(self.page).send_keys(text)

        if action == "accept":
            Alert(self.page).accept()
        else:
            Alert(self.page).dismiss()

    def find(self, selector: str) -> SeleniumElement:
        return SeleniumElement(self.page.find_element(By.CSS_SELECTOR, selector))

    def find_all(self, selector: str) -> list[SeleniumElement]:
        return [
            SeleniumElement(element)
            for element in self.page.find_elements(By.CSS_SELECTOR, selector)
        ]

    def actions(self, selector: str) -> SeleniumElement:
        return SeleniumElement(
            self.page.find_element(By.CSS_SELECTOR, selector),
            ActionChains(self.page),
        )

    @staticmethod
    def get_clipboard_content() -> str:
        return pyperclip.paste()

    def switch_to_frame(self, webelement: WebElement) -> Self:
        self.page.switch_to.frame(webelement)
        return self

    def switch_to_window(self, name: str) -> Self:
        self.page.switch_to.window(name)
        return self


class SeleniumBrowser(BaseBrowser):

    def __init__(self, browser_name: Literal["firefox", "chrome"], headless: bool):
        self.browser: WebDriver = None

        self.browser_name = browser_name
        self.headless = headless

    def launch(self) -> SeleniumPage:
        if self.browser_name == "chrome":
            options = ChromeOptions()
            if self.headless:
                options.add_argument("--headless")
            self.browser = webdriver.Chrome(service=ChromeService(), options=options)
        elif self.browser_name == "firefox":
            options = FirefoxOptions()
            if self.headless:
                options.add_argument("--headless")
            self.browser = webdriver.Firefox(service=FirefoxService(), options=options)
            return self
        else:
            raise ValueError(f"Selenium 不支持这个浏览器: {self.browser_name}")

        return SeleniumPage(self.browser)

    def new_page(self) -> SeleniumPage:
        self.browser.execute_script("window.open('');")
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return SeleniumPage(self.browser)

    def close(self):
        self.browser.quit()
