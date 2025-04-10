from pages.base_page import BasePage


class ClientdelayPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def click_trigger_button(self):
        self.page.click("#ajaxButton")

    def wait_for_client_response(self):
        self.page.wait_for_selector("#content")
