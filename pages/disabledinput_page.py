from pages.base_page import BasePage


class DisabledinputPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.input_selector = "#inputField"
        self.min_need_time = 5.5

    def check_input_disabled(self):
        return self.page.get_attribute(self.input_selector, "disabled")

    def delay_input(self, time: float = None):
        self.page.wait_editable(self.input_selector, time or self.min_need_time)

    def input_text(self, text: str):
        self.page.input(self.input_selector, text)
