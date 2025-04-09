from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from basepage import Basepage
import time


class BaseSeleniumPage(Basepage):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.max_wait_time = 8
        self.strftime = "%Y-%m-%d %H:%M:%S"

    def goto(self, url: str):
        self.driver.get(url)

    def click(self, selector: str):
        WebDriverWait(self.driver, self.max_wait_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()

    def input(self, selector: str, text: str):
        WebDriverWait(self.driver, self.max_wait_time).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, selector))).send_keys(text)

    def text(self, selector: str) -> str | None:
        return WebDriverWait(self.driver, self.max_wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))).text

    def text_content(self, selector: str) -> str | None:
        return WebDriverWait(self.driver, self.max_wait_time).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, selector))).get_attribute("textContent")

    def screenshot(self, filename: str):
        self.driver.save_screenshot(
            f"{self.screenshot_dir}{time.strftime(self.strftime, time.localtime())} {filename}.png"
        )

    def get_attribute(self, selector: str, attribute: str) -> str:
        return WebDriverWait(self.driver, self.max_wait_time).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, selector))).get_attribute(attribute)

    def is_visible(self, selector: str) -> bool:
        WebDriverWait(self.driver, self.max_wait_time).until(
            EC.visibility_of((By.CSS_SELECTOR, selector))).is_displayed()

    def get_title(self) -> str:
        return self.driver.title

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
