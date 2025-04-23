from pages.web.base_page import BasePage


class DynamicidPage:

    def __init__(self, basepage: BasePage):

        self.url = "https://www.uitestingplayground.com/dynamicid"
        self.basepage = basepage

        self.button_selector = ".btn.btn-primary"
        self.delay = 3.5

    def click_button(self):
        self.basepage.find(self.button_selector).click()

    def delay_input(self, text: str, time: float = None):
        self.basepage.wait_editable(self.button_selector, time or self.delay).input(
            text
        )

    def get_value(self) -> str:
        return self.basepage.find(self.button_selector).get_attribute("value")

    @property
    def get_title(self) -> str:
        return self.basepage.get_title()

    def open(self):
        self.basepage.goto(self.url)
