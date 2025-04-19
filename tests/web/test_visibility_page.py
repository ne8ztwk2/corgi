from pages.visibility_page import VisibilityPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestVisibilityPage:

    def setup(self, basepage):
        self.page = VisibilityPage(basepage)
        self.page.go()

    def test_element_visibility(self):
        assert self.check_element_visibility("#hideButton")
