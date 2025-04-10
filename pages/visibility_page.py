from pages.base_page import BasePage


class VisibilityPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def check_element_visibility(self, selector):
        return self.page.is_visible(selector)
