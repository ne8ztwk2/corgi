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
        self.type_selector = "#element-type"

    def choose_element_type(self, type: str):
        self.page.find(self.type_selector).select_by_value(type)

    def select_visible(self):
        self.page.find(self.visible_checkbox_selector).click()

    def select_enabled(self):
        self.page.find(self.enable_checkbox_selector).click()

    def select_editable(self):
        self.page.find(self.editable_checkbox_selector).click()

    def select_ontop(self):
        self.page.find(self.ontop_checkbox_selector).click()

    def select_nonzero(self):
        self.page.find(self.nonzero_checkbox_selector).click()

    def click_apply_button3(self):
        self.page.find(self.applyButton3_selector).click()

    def click_apply_button5(self):
        self.page.find(self.applyButton5_selector).click()

    def click_apply_button10(self):
        self.page.find(self.applyButton10_selector).click()

    def choose_target_item(self, value: str):
        self.page.find(self.target_selector, value).select_by_value(value)
