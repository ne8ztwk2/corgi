from pages.ajaxdata_page import AjaxdataPage


class TestAjaxPage:

    def setup(self, basepage):
        self.page = AjaxdataPage(basepage)
        self.page.go()

    def test_ajax_response(self):
        self.click_trigger_button()
        self.wait_for_ajax_response()
        content = self.page.find("#content").get_text()
        assert content is not None
