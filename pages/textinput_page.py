from pages.base_page import BasePage


class TextinputPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def enter_text(self, text):
        self.page.fill("#newButtonName", text)

    def click_update_button(self):
        self.page.click("#updatingButton")
