from pages.web.base_page import BasePage
from typing import Self


class ClientdelayPage:
    def __init__(self, basepage: BasePage):
        self.url = "https://www.uitestingplayground.com/clientdelay"
        self.basepage = basepage
        self.ajax_button_selector = "#ajaxButton"
        self.response_selector = ".bg-success"
        self.wait_response_need_time = 15.5

    def click_ajax_button(self):
        self.basepage.find(self.ajax_button_selector).click()

    def wait_response(self, time: float = None):
        self.basepage.wait_visible(
            self.response_selector, time or self.wait_response_need_time
        )

    def open(self) -> Self:
        self.basepage.goto(self.url)
        return self

    def close(self) -> Self:
        self.basepage.close()
        return self

    def get_response(self) -> str:
        return self.basepage.find(self.response_selector).get_text()

    @property
    def get_title(self) -> str:
        return self.basepage.get_title()
