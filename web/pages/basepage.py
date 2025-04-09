from abc import ABC, abstractmethod

from config import UI_MAX_WAIT_TIME, TIME_FORMAT, UI_SCREENSHOT_ABS_DIR


class Basepage(ABC):
    max_wait_time = UI_MAX_WAIT_TIME
    time_format = TIME_FORMAT
    screenshot_dir = UI_SCREENSHOT_ABS_DIR

    @abstractmethod
    def goto(self, url: str):
        pass

    @abstractmethod
    def click(self, selector: str):
        pass

    @abstractmethod
    def input(self, selector: str, text):
        pass

    @abstractmethod
    def text(self, selector: str) -> str | None:
        pass

    @abstractmethod
    def text_content(self, selector: str) -> str | None:
        pass

    @abstractmethod
    def is_visible(self, selector: str) -> bool:
        pass

    @abstractmethod
    def screenshot(self, filename: str):
        pass

    @abstractmethod
    def get_attribute(self, selector: str, attribute: str) -> str:
        pass

    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def quit(self):
        pass


if __name__ == "__main__":
    print(Basepage.max_wait_time)
