from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from playwright.sync_api import sync_playwright, Page, Playwright, Browser
from pages.selenium_page import SeleniumPage
from pages.playwright_page import PlaywrightPage
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


def create_playwright_driver(
    browser_name: str, playwright_context: Playwright
) -> Browser:
    """创建 Playwright 驱动"""
    if browser_name == "chrome":
        return playwright_context.chromium.launch(channel="chrome", headless=True)
    elif browser_name == "firefox":
        return playwright_context.firefox.launch(headless=True)
    else:
        raise ValueError(f"Playwright 不支持这个浏览器: {browser_name}")


@fixture(scope="session")
def playwright_context():
    """创建 Playwright 上下文并在会话结束时关闭"""
    with sync_playwright() as p:
        yield p


@fixture(scope="class")
def basepage(driver_type, browser_name, playwright_context):
    """初始化浏览器驱动并返回对应的页面对象"""
    if driver_type == "selenium":
        driver = create_selenium_driver(browser_name)
        page = SeleniumPage(driver)
    elif driver_type == "playwright":
        browser = create_playwright_driver(browser_name, playwright_context)
        page = PlaywrightPage(browser.new_page())
    else:
        raise ValueError(f"不支持的驱动类型: {driver_type}")

    yield page

    if driver_type == "selenium":
        driver.quit()
    else:
        browser.close()
