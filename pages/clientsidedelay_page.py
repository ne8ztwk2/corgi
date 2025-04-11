from pages.base_page import BasePage


class ClientdelayPage:
    def __init__(self, page: BasePage):
        self.url="https://www.uitestingplayground.com/clientdelay"
        self.page = page
        self.ajax_button_selector = "#ajaxButton"
        self.response_selector = ".bg-success"
        self.wait_response_need_time = 15.5

    def click_ajax_button(self):
        self.page.click(self.ajax_button_selector)

    def wait_response(self, time: float = None):
        self.page.wait_visible(
            self.response_selector, time or self.wait_response_need_time
        )
