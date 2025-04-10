from pages.base_page import BasePage


class DynamictablePage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def get_table_data(self):
        return self.page.get_text("#table")
