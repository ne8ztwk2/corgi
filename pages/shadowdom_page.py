from pages.base_page import BasePage


class ShadowdomPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/shadowdom"

        self.generator_selector = ".container > guid-generator"

        self.edit_field_selector = "#editField"
        self.button_copy_selector = "#buttonCopy"
        self.script = "return arguments[0].shadowRoot"

    def generate(self):
        shadow_host = self.page.find(self.generator_selector)
        self.page.execute_script(self.script)
        """
        shadowHost = document.querySelector('.container > guid-generator');
        shadowRoot = shadowHost.shadowRoot;
        btn = shadowRoot.querySelector('#editField');
        btn.click();
        guid = shadowRoot.querySelector('#editField');
        console.log(guid.textContent);
        """
