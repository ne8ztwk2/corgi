from pages.base_page import BasePage


class NbspPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def click_nbsp_button(self):
        self.page.click("button[title='My Button']")
