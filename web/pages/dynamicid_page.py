from basepage import Basepage


class DynamicidPage:

    def __init__(self, page: Basepage):

        self.url = "https://www.uitestingplayground.com/dynamicid"
        self.page = page

        self.button_selector = ".btn.btn-primary"

    @property
    def get_button_id(self) -> str:
        print(self.page.text(self.button_selector))
        return self.page.get_attribute(self.button_selector, "id")

    @property
    def get_title(self) -> str:
        return self.page.get_title()
