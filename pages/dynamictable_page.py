from pages.base_page import BasePage


class DynamictablePage:
    def __init__(self, page: BasePage):
        self.url = "https://www.uitestingplayground.com/dynamictable"
        self.page = page
        self.titles_selector = (
            "div[role=table] > div:nth-of-type(2)  span:not(:nth-child(1))"
        )
        self.rows_selector = (
            "div[role=table] > div:nth-of-type(3)  div span:first-child"
        )

        self.warning_text_selector = ".bg-warning"
        self.chrome_index = None
        self.cpu_index = None
        self.chrome_cpu_selector = None

    def get_chrome_cpu_data(self):

        for c, title in enumerate(self.page.find_all(self.titles_selector)):
            if title.get_text == "CPU":
                self.cpu_index = c + 2

        for r, name in enumerate(self.page.find_all(self.rows_selector)):
            if name.get_text() == "Chrome":
                self.chrome_index = r + 1

        self.chrome_cpu_selector = f"div[role=table] > div:nth-of-type(3) > div:nth-child({self.chrome_index})  span:nth-child({self.cpu_index})"

        self.page.find()

    def get_warning_text(self) -> str:
        return self.page.find(self.warning_text_selector).get_text()
