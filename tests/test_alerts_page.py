from pages.alerts_page import AlertsPage


class TestAlertsPage(AlertsPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/alerts")

    def test_trigger_alert(self):
        self.trigger_alert()
        alert_text = self.page.driver.switch_to.alert.text
        assert "This is an alert" in alert_text
        self.page.driver.switch_to.alert.accept()

    def teardown_class(self):
        self.page.quit()
