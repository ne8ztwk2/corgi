from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from playwright.sync_api import sync_playwright, Page
from pages.selenium_page import SeleniumPage
from pages.base_page import BasePage
from pages.playwrigh_page import PlaywrightPage
from pytest import Parser, FixtureRequest, fixture
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver


def pytest_addoption(parser: Parser):
    """在 pytest 中添加自定义命令行参数"""
    parser.addoption(
        "--driver",
        action="store",
        choices=["selenium", "playwright"],
        help="选择浏览器驱动: selenium, playwright",
    )
    parser.addoption(
        "--browser",
        action="store",
        choices=["chrome", "firefox"],
        help="选择浏览器: chrome, firefox",
    )


@fixture(scope="session")
def driver_type(request: FixtureRequest) -> str:
    """获取驱动类型参数"""
    return request.config.getoption("--driver")


@fixture(scope="session")
def browser_name(request: FixtureRequest) -> str:
    """获取浏览器类型参数"""
    return request.config.getoption("--browser").lower()


def create_selenium_driver(browser_name: str) -> WebDriver:
    """创建 Selenium 驱动"""
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        return webdriver.Chrome(service=ChromeService(), options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        return webdriver.Firefox(service=FirefoxService(), options=options)
    else:
        raise ValueError(f"Selenium 不支持这个浏览器: {browser_name}")


def create_playwright_driver(browser_name: str) -> Page:
    """创建 Playwright 驱动"""
    with sync_playwright() as p:
        if browser_name == "chrome":
            return p.chromium.launch(channel="chrome", headless=True).new_page()
        elif browser_name == "firefox":
            return p.firefox.launch(headless=True).new_page()
        else:
            raise ValueError(f"Playwright 不支持这个浏览器: {browser_name}")


@fixture(scope="class")
def basepage(driver_type, browser_name):
    """初始化浏览器驱动并返回对应的页面对象"""
    if driver_type == "selenium":
        driver = create_selenium_driver(browser_name)
        page = SeleniumPage(driver)
    elif driver_type == "playwright":
        pw_page = create_playwright_driver(browser_name)
        page = PlaywrightPage(pw_page)
    else:
        raise ValueError(f"不支持的驱动类型: {driver_type}")

    yield page

    if driver_type == "selenium":
        driver.quit()
    else:
        pw_page.close()
