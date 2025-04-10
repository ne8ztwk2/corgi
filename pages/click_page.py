from pages.base_page import BasePage


class ClickPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def click_button(self):
        self.page.click("#badButton")
