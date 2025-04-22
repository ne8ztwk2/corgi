from pages.web.base_page import BasePage
from typing import Self


class ShadowdomPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/shadowdom"

        self.shadow_host_selector = ".container > guid-generator"

        self.edit_field_selector = "#editField"
        self.button_copy_selector = "#buttonCopy"
        self.script = "return arguments[0].shadowRoot"
        self.button_generate_selector = "#buttonGenerate"

    def generate(self):
        shadow_host = self.page.find(self.shadow_host_selector)
        self.page.execute_script(self.script, shadow_host)
        self.page.find(self.button_generate_selector).click()

    def copy(self):
        self.page.find(self.button_copy_selector).click()

    def get_clipboard_content(self) -> str:
        return self.page.get_clipboard_content()

        """
        shadowHost = document.querySelector('.container > guid-generator');
        shadowRoot = shadowHost.shadowRoot;
        btn = shadowRoot.querySelector('#editField');
        btn.click();
        guid = shadowRoot.querySelector('#editField');
        console.log(guid.textContent);
        """

    def go(self) -> Self:
        self.page.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.page.get_title()
