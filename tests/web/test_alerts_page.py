from pages.web.alerts_page import AlertsPage
import pytest


class TestAlertsPage(AlertsPage):

    @pytest.fixture(autouse=True)
    def setup(self, basepage):
        self.page = AlertsPage(basepage)
        self.page.open()
        yield
        self.page.close()

    def test_trigger_alert_text(self):
        self.trigger_alert()
        alert_text = self.page.get_alert_text()
        assert "Today is a working day\nOr less likely a holiday." == alert_text

    def test_trigger_alert_accept(self):
        self.page.trigger_alert()
        self.page.accept_alert()

    def test_trigger_confirm_dismiss(self):
        self.page.trigger_confirm()
        self.page.dismiss_alert()
        assert "No" == self.page.get_alert_text()
        self.page.accept_alert()

    def test_trigger_confirm_accept(self):
        self.page.trigger_confirm()
        self.page.accept_alert()
        assert "Yes" == self.page.get_alert_text()
        self.page.accept_alert()

    def test_trigger_prompt(self):
        self.page.trigger_prompt()
        self.page.accept_alert()
        assert "User value: cats" == self.get_alert_text()

    @pytest.mark.parametrize("input", ["cats", "dogs"])
    def test_trigger_prompt_send_keys(self, input):
        self.page.trigger_prompt()
        self.page.send_keys_to_alert(input)
        self.page.accept_alert()
        assert f"User value: {input}" == self.get_alert_text()

    def test_trigger_prompt_send_keys_dismiss(self):
        self.page.trigger_prompt()
        self.page.dismiss_alert()
        assert "User value: no answer" == self.get_alert_text()
        self.page.accept_alert()
