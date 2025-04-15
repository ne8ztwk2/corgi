from pages.ajaxdata_page import AjaxdataPage


class TestAjaxPage(AjaxdataPage):

    def setup_class(self):
        self.goto("https://www.uitestingplayground.com/ajax")

    def test_ajax_response(self):
        self.click_trigger_button()
        self.wait_for_ajax_response()
        content = self.page.find("#content").get_text()
        assert content is not None

    def teardown_class(self):
        self.page.quit()
