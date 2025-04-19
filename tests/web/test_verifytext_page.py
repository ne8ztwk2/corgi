from pages.verifytext_page import VerifytextPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestVerifytextPage:

    def setup_class(self, basepage):
        self.page = VerifytextPage(basepage)

        self.page.go()

    def test_verify_text(self):
        assert self.verify_text("Welcome")
