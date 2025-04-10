from pages.base_page import BasePage


class DisabledinputPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def check_input_disabled(self):
        return self.page.is_disabled("#inputField")
