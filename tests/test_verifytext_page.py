from pages.verifytext_page import VerifytextPage


class TestVerifytextPage(VerifytextPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/verifytext")

    def test_verify_text(self):
        assert self.verify_text("Welcome")

    def teardown_class(self):
        self.page.quit()
