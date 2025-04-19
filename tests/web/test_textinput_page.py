from pages.textinput_page import TextinputPage
import pytest


@pytest.mark.usefixtures("basepage")

class TestTextinputPage(TextinputPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/textinput")

    def test_text_input(self):
        self.enter_text("New Button Name")
        self.click_update_button()
        button_text = self.page.text("#updatingButton")
        assert button_text == "New Button Name"

    def teardown_class(self):
        self.page.quit()
