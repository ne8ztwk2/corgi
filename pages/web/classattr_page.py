from pages.web.base_page import BasePage
from typing import Self


class ClassattrPage:
    def __init__(self, basepage: BasePage):
        self.basepage = basepage
        self.url = "https://www.uitestingplayground.com/classattr"
        self.blue_button_selector = ".btn-primary"
        self.alert_text = "Primary button pressed"

    def click_blue_button_and_get_text(self) -> str:
        self.basepage.find(self.blue_button_selector).click()
        return self.basepage.switch_to_alert().get_text()

    def open(self) -> Self:
        self.basepage.goto(self.url)
        return self

    def close(self):
        self.basepage.quit()

    @property
    def get_title(self) -> str:
        return self.basepage.get_title()
