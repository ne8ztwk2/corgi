from pages.classattr_page import ClassattrPage
from selenium import webdriver
from pages.selenium_page import SeleniumPage

import pytest


@pytest.mark.usefixtures("basepage")
class TestClassattrPage:

    def setup_class(self):
        driver = webdriver.Firefox()
        self.page = SeleniumPage(driver)
        self.page.goto("https://www.uitestingplayground.com/classattr")
        self.classattr_page = ClassattrPage(self.page)

    def test_click_class_attr_button(self):
        self.classattr_page.click_class_attr_button()
        # 验证点击后是否触发了预期行为，例如弹窗或页面变化
        assert self.page.is_alert_present()  # 示例：检查是否有弹窗
        self.page.accept_alert()  # 关闭弹窗

    def teardown_class(self):
        self.page.quit()
