from pages.base_page import BasePage


class VisibilityPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/verifytext"
        self.hide_button_selector = "#hideButton"

    def check_element_visibility(self, selector): ...
    def click_hide_button(self):
        self.page.find(self.hide_button_selector).click()
