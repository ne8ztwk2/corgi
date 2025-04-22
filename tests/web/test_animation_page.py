from pages.web.animatedbutton_page import AnimatedbuttonPage

import pytest


class TestAnimationPage:

    @pytest.fixture(autouse=True)
    def setup(self, basepage):
        self.page = AnimatedbuttonPage(basepage)
        self.page.open()
        yield
        self.page.close()

    def test_click_moving_target(self):
        text = self.page.click_animation_button_and_moving_target()
        assert text == "Moving Target clicked. It's class name is 'btn btn-primary'"
