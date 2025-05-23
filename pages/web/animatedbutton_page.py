from pages.web.base_page import BasePage
from typing import Self


class AnimatedbuttonPage:
    def __init__(self, basepage: BasePage):
        self.basepage = basepage
        self.url = "https://www.uitestingplayground.com/animation"
        self.opstatus_selector = "#opstatus"
        self.opststus_expected = (
            "Moving Target clicked. It's class name is 'btn btn-primary spin'"
        )
        self.animation_button_selector = "#animationButton"
        self.moving_target_selector = ".btn.btn-primary:not(.spin)"
        self.script = "document.getElementById('movingTarget').style.animation='none';"

    def click_animation_button_and_moving_target(self) -> str:
        """
        点击animationButton按钮,然后点击movingTarget按钮
        函数返回opstatus的文本
        """
        self.basepage.execute_script()

        self.basepage.wait_visible(self.animation_button_selector, 10).click()
        self.basepage.find(self.moving_target_selector).click()
        return self.basepage.find(self.opstatus_selector).get_text()

    def open(self) -> Self:
        self.basepage.goto(self.url)
        return self

    def close(self):
        self.basepage.close()

    def get_title(self) -> str:
        return self.basepage.get_title()
