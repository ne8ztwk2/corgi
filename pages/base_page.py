from abc import ABC, abstractmethod
from typing import Literal, Any
from selenium.webdriver.remote.webelement import WebElement
from playwright.sync_api import Locator
from config import UI_MAX_WAIT_TIME, TIME_FORMAT, UI_SCREENSHOT_ABS_DIR


class BasePage(ABC):
    max_wait_time = UI_MAX_WAIT_TIME
    time_format = TIME_FORMAT
    screenshot_dir = UI_SCREENSHOT_ABS_DIR

    @abstractmethod
    def goto(self, url: str): ...

    @abstractmethod
    def click(self, selector: str): ...

    @abstractmethod
    def input(self, selector: str, text): ...

    @abstractmethod
    def get_text(self, selector: str) -> str | None: ...

    @abstractmethod
    def get_text_content(self, selector: str) -> str | None: ...

    @abstractmethod
    def is_visible(self, selector: str) -> bool: ...

    @abstractmethod
    def screenshot(self, filename: str): ...

    @abstractmethod
    def get_attribute(self, selector: str, attribute: str) -> str | None: ...

    @abstractmethod
    def get_title(self) -> str: ...

    @abstractmethod
    def get_url(self) -> str: ...

    @abstractmethod
    def close(self): ...

    @abstractmethod
    def quit(self): ...

    @abstractmethod
    def alert(self, action: Literal["accept", "dismiss"], text: str = None): ...

    @abstractmethod
    def get_alert_text(self) -> str: ...

    @abstractmethod
    def execute_script(self, script: str) -> Any: ...

    @abstractmethod
    def wait_visible(
        self, selector: str, max_wait_time: float = None
    ) -> WebElement | Locator: ...

    @abstractmethod
    def wait_enable(
        self, selector: str, max_wait_time: float = None
    ) -> WebElement | Locator: ...

    @abstractmethod
    def wait_editable(
        self, selector: str, max_wait_time: float = None
    ) -> WebElement | Locator: ...

    @abstractmethod
    def wait_clickable(
        self, selector: str, max_wait_time: float = None
    ) -> WebElement | Locator: ...

    @abstractmethod
    def wait_non_zreo_size(
        self, selector: str, max_wait_time: float = None
    ) -> WebElement | Locator: ...

    @abstractmethod
    def select_by_value(self, selector: str, value: str): ...

    @abstractmethod
    def select_by_index(self, selector: str, index: int): ...

    @abstractmethod
    def select_by_text(self, selector: str, text: str): ...


if __name__ == "__main__":
    print(BasePage.max_wait_time)
