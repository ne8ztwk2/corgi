from pages.base_page import BasePage


class ShadowdomPage:
    def __init__(self, page: BasePage):
        super().__init__(page)

    def interact_with_shadow_dom(self):
        shadow_root = self.page.get_shadow_root("#shadowHost")
        shadow_root.click("#shadowButton")
