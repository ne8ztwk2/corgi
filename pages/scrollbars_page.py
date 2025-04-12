from pages.base_page import BasePage


class ScrollbarsPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/scrollbars"
        self.hidden_button_selector = "#hidingButton"

    def click_hidden_button(self):
        # can not found element
        # self.page.find(self.hidden_button_selector).scroll_into_view().click()
        ...
