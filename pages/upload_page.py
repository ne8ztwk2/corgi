from pages.base_page import BasePage


class UploadPage:
    def __init__(self, page: BasePage):
        self.url = "https://www.uitestingplayground.com/upload"
        self.page = page
        self.file_upload_box_selector = ".document-uploader.upload-box"
        self.frame_selector = 'iframe[src="/static/upload.html"]'
        self.browse_btn_selector = ".browse-btn"

    def upload_file_for_grag(self, filepath): ...
    def upload_file_for_open_browse_files(self, filepath): ...

    #  can not impl
