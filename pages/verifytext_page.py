from pages.base_page import BasePage


class VerifytextPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def verify_text(self, expected_text):
        actual_text = self.page.get_text("body")
        return expected_text in actual_text
