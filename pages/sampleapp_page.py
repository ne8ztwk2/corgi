from pages.base_page import BasePage


class SampleappPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("#login")
