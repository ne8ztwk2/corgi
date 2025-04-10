from pages.base_page import BasePage


class AlertsPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/alerts"
        self.alert_button_selector = "#alertButton"
        self.confirm_button_selector = "#confirmButton"
        self.prompt_button_selector = "#promptButton"

    def trigger_alert(self):
        self.page.click("#alertButton")
