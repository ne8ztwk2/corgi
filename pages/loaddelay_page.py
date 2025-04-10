from pages.base_page import BasePage


class LoaddelayPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def click_delayed_button(self):
        self.page.wait_for_selector(".btn-primary")
        self.page.click(".btn-primary")
