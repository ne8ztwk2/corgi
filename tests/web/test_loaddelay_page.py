from pages.loaddelay_page import LoaddelayPage
from selenium import webdriver
from pages.selenium_page import SeleniumPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestLoaddelayPage:

    def setup_class(self):
        driver = webdriver.Firefox()
        self.page = SeleniumPage(driver)
        self.page.goto("https://www.uitestingplayground.com/loaddelay")
        self.loaddelay_page = LoaddelayPage(self.page)

    def test_click_delayed_button(self):
        self.loaddelay_page.click_delayed_button()
        # 验证按钮点击后是否触发了预期行为，例如页面跳转或内容加载
        assert self.page.get_title() == "Load Delay"  # 示例：检查页面标题

    def teardown_class(self):
        self.page.quit()
