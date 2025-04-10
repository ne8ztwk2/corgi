from pages.base_page import BasePage


class AutowaitPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/autowait"
        self.visible_checkbox_selector = "#visible"
        self.enable_checkbox_selector = "#enabled"
        self.editable_checkbox_selector = "#editable"
        self.ontop_checkbox_selector = "#ontop"
        self.nonzero_checkbox_selector = "#nonzero"
        self.applyButton3_selector = "#applyButton3"
        self.applyButton5_selector = "#applyButton5"
        self.applyButton10_selector = "#applyButton10"
        self.target_selector = "#target"

    def choose_element_type(self, type: str):
        self.page.select("#selectType", type)

    def select_visible(self):
        self.page.click(self.visible_checkbox_selector)

    def select_enabled(self):
        self.page.click(self.enable_checkbox_selector)

    def select_editable(self):
        self.page.click(self.editable_checkbox_selector)

    def select_ontop(self):
        self.page.click(self.ontop_checkbox_selector)

    def select_nonzero(self):
        self.page.click(self.nonzero_checkbox_selector)

    def click_apply_button3(self):
        self.page.click(self.applyButton3_selector)

    def click_apply_button5(self):
        self.page.click(self.applyButton5_selector)

    def click_apply_button10(self):
        self.page.click(self.applyButton10_selector)

    def choose_target_item(self, item: str):
        self.page.select(self.target_selector, item)
