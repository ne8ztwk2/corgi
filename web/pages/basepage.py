


class Basepage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        pass

    def click(self, locator: tuple):
        pass

    def send_keys(self, locator, text):
        pass

    def get_text(self, locator):
        pass

    def is_visible(self, locator):
        pass

    def take_screenshot(self, name: str = "enshot"):
        pass
