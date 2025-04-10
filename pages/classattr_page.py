from pages.base_page import BasePage


class ClassattrPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/classattr"
        self.blue_button_selector = ".btn-primary"

    def click_blue_button(self):
        self.page.click(self.blue_button_selector)
