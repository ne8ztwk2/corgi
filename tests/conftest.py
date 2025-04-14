import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from playwright.sync_api import sync_playwright

from pages.selenium_page import SeleniumPage
from pages.playwrigh_page import PlaywrightPage


def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        action="store",
        default="selenium",
        choices=["selenium", "playwright"],
        help="Choose which driver to use: selenium or playwright",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome, firefox, edge, or webkit (playwright only)",
    )


@pytest.fixture(scope="session")
def driver_type(request):
    return request.config.getoption("--driver")


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser").lower()


@pytest.fixture
def basepage(driver_type, browser_name):
    if driver_type == "selenium":
        if browser_name == "chrome":
            driver = webdriver.Chrome(service=ChromeService())
        elif browser_name == "firefox":
            driver = webdriver.Firefox(service=FirefoxService())

        else:
            raise ValueError(f"Selenium does not support browser: {browser_name}")
        page = SeleniumPage(driver)
        yield page
        driver.quit()

    elif driver_type == "playwright":
        with sync_playwright() as p:
            if browser_name == "chrome":
                browser = p.chromium.launch(channel="chrome", headless=True)
            elif browser_name == "firefox":
                browser = p.firefox.launch(headless=True)

            else:
                raise ValueError(f"Playwright does not support browser: {browser_name}")
            pw_page = browser.new_page()
            page = PlaywrightPage(pw_page)
            yield page
            browser.close()

    else:
        raise ValueError(f"Unknown driver type: {driver_type}")
