from pages.web.base_page import BasePage
from typing import Self


class AnimatedbuttonPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/animation"
        self.opstatus_selector = "#opstatus"
        self.opststus_expected = (
            "Moving Target clicked. It's class name is 'btn btn-primary spin'"
        )
        self.animation_button_selector = "#animationButton"
        self.moving_target_selector = "#movingTarget"
        self.script = "document.getElementById('movingTarget').style.animation='none';"

    def click_animation_button_and_moving_target(self) -> str:
        """
        点击animationButton按钮,然后点击movingTarget按钮
        函数返回opstatus的文本
        """
        self.page.execute_script()
        self.page.find(self.animation_button_selector).click()
        self.page.find(self.moving_target_selector).click()
        return self.page.find(self.opstatus_selector).get_text()

    def go(self) -> Self:
        self.page.goto(self.url)
        return self

    @property
    def get_title(self) -> str:
        return self.page.get_title()
