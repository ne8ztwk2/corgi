from pages.upload_page import UploadPage


class TestUploadPage(UploadPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/upload")

    def test_upload_file(self):
        self.upload_file("/path/to/testfile.txt")
        uploaded_file_name = self.page.text("#uploadedFileName")
        assert uploaded_file_name == "testfile.txt"

    def teardown_class(self):
        self.page.quit()
