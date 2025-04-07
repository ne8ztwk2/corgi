from playwright.sync_api import Page


class BookPage:

    def __init__(self, page: Page):
        ...

    def search(self, keyword: str):
        ...
