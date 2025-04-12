from pages.base_page import BasePage


class HiddenlayersPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/hiddenlayers"
        self.hidden_button_selector = ".btn.btn-success"

    def click_hidden_button(self):
        self.page.find(self.click_hidden_button).click()
