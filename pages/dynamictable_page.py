from pages.base_page import BasePage


class DynamictablePage:
    def __init__(self, page: BasePage):
        self.url = "https://www.uitestingplayground.com/dynamictable"
        self.page = page
        self.titles_selector = 'span[role="columnheader"]'

    def get_chrome_cpu_data(self):
        elems = self.page.find_all(self.titles_selector)

        for i, h in enumerate(elems):
            ...
