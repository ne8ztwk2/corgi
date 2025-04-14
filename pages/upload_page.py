from pages.base_page import BasePage
from typing import Self

class UploadPage:
    def __init__(self, page: BasePage):
        self.url = "https://www.uitestingplayground.com/upload"
        self.page = page
        self.file_upload_box_selector = ".document-uploader.upload-box"
        self.frame_selector = 'iframe[src="/static/upload.html"]'
        self.browse_btn_selector = ".browse-btn"

    def upload_file_for_grag(self, filepath):
        # Unable to drag files from the local machine into the browser.
        ...

    def upload_file_for_open_browse_files(self, filepath):
        self.page.switch_to_frame(self.page.find(self.frame_selector)).find(
            self.browse_btn_selector
        ).click()
        #  File upload cannot be performed inside the Docker container.
        ...

    def go(self) -> Self:
        self.page.goto(self.url)
        return self
