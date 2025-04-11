from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time
from typing import Literal, Self, Any
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


class SeleniumPage(BasePage):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.max_wait_time = 8
        self.strftime = "%Y-%m-%d %H:%M:%S"

    def goto(self, url: str):
        self.driver.get(url)

    def click(self, selector: str):
        self.wait_clickable(selector).click()

    def input(self, selector: str, text: str):
        self.wait_editable(selector).send_keys(text)

    def get_text(self, selector: str) -> str | None:
        return self.driver.find_element(By.CSS_SELECTOR, selector).text

    def get_text_content(self, selector: str) -> str | None:
        return self.driver.find_element(By.CSS_SELECTOR, selector).get_attribute(
            "textContent"
        )

    def screenshot(self, filename: str):
        self.driver.save_screenshot(
            f"{self.screenshot_dir}{time.strftime(self.strftime, time.localtime())} {filename}.png"
        )

    def get_attribute(self, selector: str, attribute: str) -> str | None:
        self.driver.find_element(By.CSS_SELECTOR, selector).get_attribute(attribute)

    def is_visible(self, selector: str) -> bool:
        return self.driver.find_element(By.CSS_SELECTOR, selector).is_displayed()

    def get_title(self) -> str:
        return self.driver.title

    def get_url(self) -> str:
        return self.driver.current_url

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def get_alert_text(self) -> str:
        return Alert(self.driver).text

    def execute_script(self, script: str):
        self.driver.execute_script(script)

    def alert(self, action: Literal["accept", "dismiss"], text: str = None):
        if text is not None:
            Alert(self.driver).send_keys(text)

        if action == "accept":
            Alert(self.driver).accept()
        else:
            Alert(self.driver).dismiss()

    def wait_visible(self, selector: str, max_wait_time: float = None) -> WebElement:
        return WebDriverWait(self.driver, max_wait_time or self.max_wait_time).until(
            EC.visibility_of((By.CSS_SELECTOR, selector))
        )

    def wait_enable(self, selector: str, max_wait_time: float = None) -> WebElement:
        return WebDriverWait(self.driver, max_wait_time or self.max_wait_time).until(
            self.__element_is_enable(By.CSS_SELECTOR, selector)
        )

    def wait_editable(self, selector: str, max_wait_time: float = None) -> WebElement:
        return WebDriverWait(self.driver, max_wait_time or self.max_wait_time).until(
            self.__element_is_editable(By.CSS_SELECTOR, selector)
        )

    def __element_is_editable(self, selector: str) -> bool:
        def _predicate(driver) -> bool:
            try:
                element: WebElement = driver.find_element(By.CSS_SELECTOR, selector)
                return (
                    element.is_displayed()
                    and element.is_enabled()
                    and element.get_attribute("readonly") is None
                )
            except:
                return False

        return _predicate

    def __element_is_enable(self, selector: str) -> bool:
        def _predicate(driver) -> bool:
            try:
                element: WebElement = driver.find_element(By.CSS_SELECTOR, selector)
                return element.is_enabled()
            except:
                return False

        return _predicate

    def wait_clickable(self, selector: str, max_wait_time: float = None) -> WebElement:
        return WebDriverWait(self.driver, max_wait_time or self.max_wait_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )

    def wait_non_zreo_size(
        self, selector: str, max_wait_time: float = None
    ) -> WebElement:
        return WebDriverWait(self.driver, max_wait_time or self.max_wait_time).until(
            self.__element_is_non_zreo_size(selector)
        )

    def __element_is_non_zreo_size(self, selector: str) -> bool:
        def _predicate(driver) -> bool:
            try:
                element_size: WebElement = driver.find_element(
                    By.CSS_SELECTOR, selector
                ).size
                return element_size["width"] > 0 and element_size["height"] > 0
            except:
                return False

        return _predicate

    def select_by_value(self, selector: str, value: str):
        Select(self.driver.find_element(By.CSS_SELECTOR, selector)).select_by_value(
            value
        )

    def select_by_index(self, selector: str, index: int):
        Select(self.driver.find_element(By.CSS_SELECTOR, selector)).select_by_index(
            index
        )

    def select_by_text(self, selector: str, text: str):
        Select(
            self.driver.find_element(By.CSS_SELECTOR, selector)
        ).select_by_visible_text(text)
