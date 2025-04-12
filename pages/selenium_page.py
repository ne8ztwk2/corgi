from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage, BaseElement, BaseActions
import time
from typing import Literal, Self, Any
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains

# class SeleniumPage(BasePage):

#     def __init__(self, driver: WebDriver):
#         self.driver = driver
#         self.max_wait_time = 8
#         self.strftime = "%Y-%m-%d %H:%M:%S"

#     def goto(self, url: str):
#         self.driver.get(url)

#     def click(self, selector: str):
#         self.wait_clickable(selector).click()

#     def click2(self, web_element: WebElement):
#         web_element.click()

#     def input(self, selector: str, text: str):
#         self.wait_editable(selector).send_keys(text)

#     def get_text(self, selector: str) -> str | None:
#         return self.find(selector).text

#     def get_text_content(self, selector: str) -> str | None:
#         return self.find(selector).get_attribute("textContent")

#     def screenshot(self, filename: str):
#         self.driver.save_screenshot(
#             f"{self.screenshot_dir}{time.strftime(self.strftime, time.localtime())} {filename}.png"
#         )

#     def get_attribute(self, selector: str, attribute: str) -> str | None:
#         self.find(selector).get_attribute(attribute)

#     def is_visible(self, selector: str) -> bool:
#         return self.find(selector).is_displayed()

#     def get_title(self) -> str:
#         return self.driver.title

#     def get_url(self) -> str:
#         return self.driver.current_url

#     def close(self):
#         self.driver.close()

#     def quit(self):
#         self.driver.quit()

#     def get_alert_text(self) -> str:
#         return Alert(self.driver).text

#     def execute_script(self, script: str):
#         self.driver.execute_script(script)

#     def alert(self, action: Literal["accept", "dismiss"], text: str = None):
#         if text is not None:
#             Alert(self.driver).send_keys(text)

#         if action == "accept":
#             Alert(self.driver).accept()
#         else:
#             Alert(self.driver).dismiss()

#     def wait_visible(self, selector: str, max_wait_time: float = None) -> WebElement:
#         return WebDriverWait(self.driver, max_wait_time or self.max_wait_time).until(
#             EC.visibility_of((By.CSS_SELECTOR, selector))
#         )

#     def wait_enable(self, selector: str, max_wait_time: float = None) -> WebElement:
#         return WebDriverWait(self.driver, max_wait_time or self.max_wait_time).until(
#             self.__element_is_enable(selector)
#         )

#     def wait_editable(self, selector: str, max_wait_time: float = None) -> WebElement:
#         return WebDriverWait(self.driver, max_wait_time or self.max_wait_time).until(
#             self.__element_is_editable(selector)
#         )

#     def __element_is_editable(self, selector: str) -> bool:
#         def _predicate() -> bool:
#             try:
#                 element: WebElement = self.find(selector)
#                 return (
#                     element.is_displayed()
#                     and element.is_enabled()
#                     and element.get_attribute("readonly") is None
#                 )
#             except:
#                 return False

#         return _predicate

#     def __element_is_enable(self, selector: str) -> bool:
#         def _predicate() -> bool:
#             try:
#                 element: WebElement = self.find(selector)
#                 return element.is_enabled()
#             except:
#                 return False

#         return _predicate

#     def wait_clickable(self, selector: str, max_wait_time: float = None) -> WebElement:
#         return WebDriverWait(self.driver, max_wait_time or self.max_wait_time).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
#         )

#     def wait_non_zreo_size(
#         self, selector: str, max_wait_time: float = None
#     ) -> WebElement:
#         return WebDriverWait(self.driver, max_wait_time or self.max_wait_time).until(
#             self.__element_is_non_zreo_size(selector)
#         )

#     def __element_is_non_zreo_size(self, selector: str) -> bool:
#         def _predicate() -> bool:
#             try:
#                 element_size: WebElement = self.find(selector).size
#                 return element_size["width"] > 0 and element_size["height"] > 0
#             except:
#                 return False

#         return _predicate

#     def select_by_value(self, selector: str, value: str):
#         Select(self.find(selector)).select_by_value(value)

#     def select_by_index(self, selector: str, index: int):
#         Select(self.find(selector)).select_by_index(index)

#     def select_by_text(self, selector: str, text: str):
#         Select(self.find(selector)).select_by_visible_text(text)

#     def find(self, selector: str) -> WebElement:
#         return self.driver.find_element(selector)

#     def find_all(self, selector: str) -> list[WebElement]:
#         return self.driver.find_elements(selector)


class SeleniumElement(BaseElement):

    def __init__(self, element: WebElement, actions: ActionChains):
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
        self.element.get_attribute(attribute)

    def is_visible(self) -> bool:
        return self.element.is_displayed()

    def wait_visible(self, timeout: float = None) -> WebElement:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of(self.element)
        )

    def wait_enable(self, timeout: float = None) -> WebElement:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            self.element.is_enabled()
        )

    def wait_editable(self, timeout: float = None) -> WebElement:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            self.self.element.is_displayed()
            and self.element.is_enabled()
            and self.element.get_attribute("readonly") is None
        )

    def wait_clickable(self, timeout: float = None) -> WebElement:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(self.element)
        )

    def wait_non_zreo_size(self, timeout: float = None) -> WebElement:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            self.element_size["width"] > 0 and self.element_size["height"] > 0
        )

    def select_by_value(self, value: str):
        Select(self.element).select_by_value(value)

    def select_by_index(self, index: int):
        Select(self.element).select_by_index(index)

    def select_by_text(self, text: str):
        Select(self.element).select_by_visible_text(text)

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

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.strftime = "%Y-%m-%d %H:%M:%S"

    def goto(self, url: str):
        self.driver.get(url)

    def screenshot(self, filename: str):
        self.driver.save_screenshot(
            f"{self.screenshot_dir}{time.strftime(self.strftime, time.localtime())} {filename}.png"
        )

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

    def find(self, selector: str) -> SeleniumElement:
        return SeleniumElement(self.driver.find_element(By.CSS_SELECTOR, selector))

    def find_all(self, selector: str) -> list[SeleniumElement]:
        return [SeleniumElement(self.driver.find_element(By.CSS_SELECTOR, selector))]

    def actions(self, selector: str) -> SeleniumElement:
        return SeleniumElement(self.driver.find_element(By.CSS_SELECTOR, selector))
