from pages.web.base_page import BasePage

from typing import Self


class SampleappPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/sampleapp"
        self.username_input_selector = "[name=UserName]"
        self.password_input_selector = "[type=password]"
        self.login_button_selector = "#login"
        self.logout_button_selector = "#login"
        self.loginstatus_selector = "#loginstatus"

    def login(self, username, password):
        self.page.find(self.username_input_selector).input(username)
        self.page.find(self.password_input_selector).input(password)
        self.page.click("#login")

    def get_loginstatus(self) -> str:
        return self.page.find(self.loginstatus_selector).get_text()

    def logout(self):
        return self.page.find(self.logout_button_selector).click()

    def go(self) -> Self:
        self.page.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.page.get_title()
