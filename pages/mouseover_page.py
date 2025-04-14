from pages.base_page import BasePage

from typing import Self


class MouseoverPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/mouseover"
        self.move_to_click_me_selector = 'a[title="Click me"]'
        self.click_me_selector = "a[title='Active Link']"
        self.click_count_selctor = "#clickCount"
        self.link_button_selector = "a[title='Link Button']"
        self.move_to_link_button_selector = "a[title='Link Button']"
        self.click_button_count_selctor = "#clickButtonCount"

    def click_click_me(self):
        self.page.actions(self.move_to_click_me_selector).move()
        self.page.find(self.click_me_selector).click()

    def click_link_button(self):
        self.page.actions(self.move_to_click_me_selector).move()
        self.page.find(self.move_to_link_button_selector).click()

    def get_click_me_count(self) -> str:
        return self.page.find(self.click_count_selctor).get_text()

    def get_click_button_count(self) -> str:
        return self.page.find(self.click_button_count_selctor).get_text()

    def go(self) -> Self:
        self.page.goto(self.url)
        return self
