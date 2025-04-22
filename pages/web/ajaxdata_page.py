from pages.web.base_page import BasePage
from typing import Self


class AjaxdataPage:
    def __init__(self, basepage: BasePage):
        self.basepage = basepage
        self.url = "https://www.uitestingplayground.com/ajax"
        self.ajax_button_selector = "#ajaxButton"
        self.ajax_response_selector = ".bg-success"

    def click_button(self):
        self.basepage.find(self.ajax_button_selector).click()

    def wait_for_ajax_response(self):
        self.basepage.find(self.ajax_response_selector).wait_visible(max_wait_time=16)

    def open(self) -> Self:
        self.basepage.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.basepage.get_title()

    def close(self):
        self.basepage.close()

    def get_content(self) -> str:
        return self.basepage.find(self.ajax_response_selector).get_text()
