from pages.base_page import BasePage


class OverlappedPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def fill_input(self, text):
        self.page.fill("#overlappedInput", text)
