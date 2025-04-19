from pages.selenium_page import SeleniumBrowser
from pages.playwright_page import PlaywrightBrowser
from config import HEADLESS, BROWSER_NAME, DRIVER_TYPE
import pytest


@pytest.fixture(scope="class")
def browser():
    """初始化浏览器驱动并返回对应的页面对象"""
    if DRIVER_TYPE == "selenium":
        browser = SeleniumBrowser(browser_name=BROWSER_NAME, headless=HEADLESS)
    elif DRIVER_TYPE == "playwright":
        browser = PlaywrightBrowser(browser_name=BROWSER_NAME, headless=HEADLESS)
    else:
        raise ValueError(f"不支持的驱动类型: {DRIVER_TYPE}")

    page = browser.launch()

    yield page

    browser.close()
