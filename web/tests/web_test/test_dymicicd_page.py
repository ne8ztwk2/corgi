from web.pages.dynamicid_page import DynamicidPage


class TestDynamicidPage(DynamicidPage):

    def test_get_dynamicid(self):
        _id = self.get_button_id()
        assert not _id == ""
