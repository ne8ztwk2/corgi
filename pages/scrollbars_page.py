from pages.base_page import BasePage


class ScrollbarsPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def click_hidden_button(self):
        self.page.scroll_into_view("#hidingButton")
        self.page.click("#hidingButton")
