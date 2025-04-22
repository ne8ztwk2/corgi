from pages.web.ajaxdata_page import AjaxdataPage
import pytest


class TestAjaxPage:

    @pytest.fixture(autouse=True)
    def setup(self, basepage):
        self.page = AjaxdataPage(basepage)
        self.page.open()
        yield
        self.page.close()

    @pytest.mark.parametrize("expected_content", ["Data loaded with AJAX get request."])
    def test_ajax_response(self, expected_content):
        self.page.click_button()
        self.page.wait_for_ajax_response()
        content = self.page.get_content()
        assert content == expected_content
