from pages.base_page import BasePage


class LoaddelayPage:
    def __init__(self, page: BasePage):
        self.url = "https://www.uitestingplayground.com/loaddelay"
        self.page = page
        self.button_selector = "btn.btn-primary"

    def click_delayed_button(self):
        self.page.find(self.button_selector).wait_clickable().click()
