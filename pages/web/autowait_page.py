from pages.web.base_page import BasePage
from typing import Self


class AutowaitPage:
    def __init__(self, basepage: BasePage):
        self.basepage = basepage
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
        self.basepage.find(self.type_selector).select_by_value(type)

    def select_visible(self):
        self.basepage.find(self.visible_checkbox_selector).click()

    def select_enabled(self):
        self.basepage.find(self.enable_checkbox_selector).click()

    def select_editable(self):
        self.basepage.find(self.editable_checkbox_selector).click()

    def select_ontop(self):
        self.basepage.find(self.ontop_checkbox_selector).click()

    def select_nonzero(self):
        self.basepage.find(self.nonzero_checkbox_selector).click()

    def click_apply_button3(self):
        self.basepage.find(self.applyButton3_selector).click()

    def click_apply_button5(self):
        self.basepage.find(self.applyButton5_selector).click()

    def click_apply_button10(self):
        self.basepage.find(self.applyButton10_selector).click()

    def choose_target_item(self, value: str):
        self.basepage.find(self.target_selector).select_by_value(value)

    def go(self) -> Self:
        self.basepage.goto(self.url)
        return self

    def get_title(self) -> str:
        return self.basepage.get_title()

    def close(self):
        self.basepage.close()

    def open(self) -> Self:
        self.basepage.goto(self.url)
        return self
