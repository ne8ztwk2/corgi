from pages.base_page import BasePage
from typing import Self


class AjaxdataPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/ajax"
        self.ajax_button_selector = "#ajaxButton"
        self.ajax_response_selector = ".bg-success"

    def click_button(self):
        self.page.find(self.ajax_button_selector).click()

    def wait_for_ajax_response(self):
        self.page.find(self.ajax_response_selector).wait_visible()

    def go(self) -> Self:
        self.page.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.page.get_title()
