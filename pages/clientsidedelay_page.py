from pages.base_page import BasePage


class ClientdelayPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.ajax_button_selector = "#ajaxButton"
        self.response_selector = ".bg-success"
        self.wait_response_time = 16

    def click_ajax_button(self):
        self.page.click(self.ajax_button_selector)

    def wait_response(self):
        self.page.wait_visible(self.response_selector, self.wait_response_time)
