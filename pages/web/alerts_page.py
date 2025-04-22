from pages.web.base_page import BasePage, BaseAlert
from typing import Self


class AlertsPage:
    def __init__(self, basepage: BasePage):
        self.basepage = basepage
        self.url = "https://www.uitestingplayground.com/alerts"
        self.alert_button_selector = "#alertButton"
        self.confirm_button_selector = "#confirmButton"
        self.prompt_button_selector = "#promptButton"

    def trigger_alert(self):
        self.basepage.find(self.alert_button_selector).click()

    def open(self) -> Self:
        self.basepage.goto(self.url)
        return self

    def close(self):
        self.basepage.close()

    def trigger_confirm(self):
        self.basepage.find(self.confirm_button_selector).click()

    def trigger_prompt(self):
        self.basepage.find(self.prompt_button_selector).click()

    def _switch_to_alert(self) -> BaseAlert:
        return self.basepage.switch_to_alert()

    def accept_alert(self):
        alert = self._switch_to_alert()
        alert.accept()

    def dismiss_alert(self):
        alert = self._switch_to_alert()
        alert.dismiss()

    def send_keys_to_alert(self, text: str):
        alert = self._switch_to_alert()
        alert.send_keys(text)

    def get_alert_text(self) -> str:
        alert = self._switch_to_alert()
        return alert.get_text()

    @property
    def get_title(self) -> str:
        return self.basepage.get_title()
