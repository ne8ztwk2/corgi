from pages.dynamicid_page import DynamicidPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestDynamicidPage(DynamicidPage):

    def setup_class(self):

        self.page.goto(self.url)

    def test_get_dynamicid(self):
        _id = self.get_button_id()
        assert _id is not None

    def teardown_class(self):
        self.page.quit()
