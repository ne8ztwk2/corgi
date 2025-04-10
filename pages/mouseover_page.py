from pages.base_page import BasePage


class MouseoverPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def hover_over_element(self, selector):
        self.page.hover(selector)
