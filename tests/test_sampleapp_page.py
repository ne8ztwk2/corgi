from pages.sampleapp_page import SampleappPage


class TestSampleappPage(SampleappPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/sampleapp")

    def test_login(self):
        self.login("testuser", "password")
        welcome_text = self.page.text("#loginstatus")
        assert "Welcome" in welcome_text

    def teardown_class(self):
        self.page.quit()
