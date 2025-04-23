from pages.web.clientsidedelay_page import ClientdelayPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestClientdelayPage:

    @pytest.fixture(autouse=True)
    def setup(self, basepage):
        self.page = ClientdelayPage(basepage)
        self.page.open()
        yield
        self.page.close()

    def test_client_delay_wait_success(self):
        self.page.click_ajax_button()
        self.page.wait_response(15.5)
        content = self.page.get_response()
        assert content == "Data calculated on the client side."

    @pytest.mark.xfail(strict=True)
    def test_client_delay_wait_false(self):
        self.page.click_ajax_button()
        self.page.wait_response(10)
        self.page.get_response()
