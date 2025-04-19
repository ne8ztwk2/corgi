from pages.animatedbutton_page import AnimatedbuttonPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestAnimationPage:

    def setup(self, basepage):
        self.page = AnimatedbuttonPage(basepage)
        self.page.goto("https://www.uitestingplayground.com/animation")

    def test_wait_for_animation(self):
        self.wait_for_animation()
        assert self.page.is_visible("#animatedElement")

    def teardown_class(self):
        self.page.quit()
