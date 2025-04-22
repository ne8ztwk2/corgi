from pages.web.classattr_page import ClassattrPage

import pytest


class TestClassattrPage:

    @pytest.fixture(autouse=True)
    def setup(self, basepage):
        self.page = ClassattrPage(basepage)
        self.page.open()
        yield
        self.page.close()

    def test_click_class_attr_button(self):

        assert self.page.click_blue_button_and_get_text() == "Primary button pressed"
