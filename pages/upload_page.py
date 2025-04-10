from pages.base_page import BasePage


class UploadPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def upload_file(self, file_path):
        self.page.set_input_files("#fileInput", file_path)
