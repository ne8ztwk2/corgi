from pages.clientdelay_page import ClientdelayPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestClientdelayPage(ClientdelayPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/clientdelay")

    def test_client_delay(self):
        self.click_trigger_button()
        self.wait_for_client_response()
        content = self.page.text("#content")
        assert content is not None

    def teardown_class(self):
        self.page.quit()
