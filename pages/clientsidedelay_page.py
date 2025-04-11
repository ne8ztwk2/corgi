from pages.base_page import BasePage


class ClientdelayPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.ajax_button_selector = "#ajaxButton"

    def click_trigger_button(self):
        self.page.click(self.ajax_button_selector)

    def wait_for_client_response(self):
        self.page.wait_for_selector("#content")
