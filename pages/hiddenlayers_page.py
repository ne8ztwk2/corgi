from pages.base_page import BasePage


class HiddenlayersPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def click_hidden_button(self):
        self.page.click(".btn-primary")
