from pages.hiddenlayers_page import HiddenlayersPage
from selenium import webdriver
from pages.selenium_page import SeleniumPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestHiddenlayersPage:

    def setup_class(self):
        driver = webdriver.Firefox()
        self.page = SeleniumPage(driver)
        self.page.goto("https://www.uitestingplayground.com/hiddenlayers")
        self.hiddenlayers_page = HiddenlayersPage(self.page)

    def test_click_hidden_button(self):
        self.hiddenlayers_page.click_hidden_button()
        # 验证按钮是否被点击，例如检查按钮是否被禁用或隐藏
        assert not self.page.is_enabled(".btn-primary")  # 示例：检查按钮是否被禁用

    def teardown_class(self):
        self.page.quit()
