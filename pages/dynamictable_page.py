from pages.base_page import BasePage


class DynamictablePage:
    def __init__(self, page: BasePage):
        self.url = "https://www.uitestingplayground.com/dynamictable"
        self.page = page

    def get_chrome_cpu_data(self):
        ...
