from pages.base_page import BasePage


class DisabledinputPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.input_selector = "#inputField"

    def check_input_disabled(self):
        return self.page.is_disabled("#inputField")

    def delay_input(self, time: int):
        self.page.wait_editable(self.input_selector, time)
