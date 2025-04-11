from pages.base_page import BasePage


class ClickPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/click"
        self.button_selector = "#badButton"
        self.button_success_selector = ".btn.btn-success"

    def click_button(self):
        self.page.click(self.button_selector)
        self.page.wait_visible(self.button_success_selector)
