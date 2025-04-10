from pages.ajaxdata_page import AjaxPage


class TestAjaxPage(AjaxPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/ajax")

    def test_ajax_response(self):
        self.click_trigger_button()
        self.wait_for_ajax_response()
        content = self.page.text("#content")
        assert content is not None

    def teardown_class(self):
        self.page.quit()
