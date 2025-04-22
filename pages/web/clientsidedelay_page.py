from pages.web.base_page import BasePage
from typing import Self


class ClientdelayPage:
    def __init__(self, page: BasePage):
        self.url = "https://www.uitestingplayground.com/clientdelay"
        self.page = page
        self.ajax_button_selector = "#ajaxButton"
        self.response_selector = ".bg-success"
        self.wait_response_need_time = 15.5

    def click_ajax_button(self):
        self.page.find(self.ajax_button_selector).click()

    def wait_response(self, time: float = None):
        self.page.find(self.response_selector).wait_visible(
            time or self.wait_response_need_time
        )

    def go(self) -> Self:
        self.page.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.page.get_title()
