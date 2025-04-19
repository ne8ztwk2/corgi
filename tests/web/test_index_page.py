from pages.index_page import IndexPage
import pytest


@pytest.mark.usefixtures("basepage")
class TestIndexPage:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        self.page = IndexPage(browser)
        self.page.go()
        self.base_url = "https://www.uitestingplayground.com"

    @pytest.mark.parametrize(
        "selector",
        "expected_title",
        "expected_url",
        [
            ('a[href="/dynamicid"]', "Dynamic ID", "/dynamicid"),
            ('a[href="/classattr"]', "Class Attribute", "/classattr"),
            ('a[href="/hiddenlayers"]', "Hidden Layers", "/hiddenlayers"),
            ('a[href="/loaddelay"]', "Load Delays", "/loaddelay"),
            ('a[href="/ajax"]', "AJAX Data", "/ajax"),
            ('a[href="/clientdelay"]', "Client Side Delay", "/clientdelay"),
            ('a[href="/click"]', "Click", "/click"),
            ('a[href="/textinput"]', "Text Input", "/textinput"),
            ('a[href="/scrollbars"]', "Scrollbars", "/scrollbars"),
            ('a[href="/dynamictable"]', "Dynamic Table", "/dynamictable"),
            ('a[href="/verifytext"]', "Verify Text", "/verifytext"),
            ('a[href="/progressbar"]', "Progress Bar", "/progressbar"),
            ('a[href="/visibility"]', "Visibility", "/visibility"),
            ('a[href="/sampleapp"]', "Sample App", "/sampleapp"),
            ('a[href="/mouseover"]', "Mouse Over", "/mouseover"),
            ('a[href="/nbsp"]', "Non-Breaking Space", "/nbsp"),
            ('a[href="/overlapped"]', "Overlapped Element", "/overlapped"),
            ('a[href="/shadowdom"]', "Shadow DOM", "/shadowdom"),
            ('a[href="/alerts"]', "Alerts", "/alerts"),
            ('a[href="/upload"]', "File Upload", "/upload"),
            ('a[href="/animation"]', "Animation", "/animation"),
            ('a[href="/disabledinput"]', "Disabled Input", "/disabledinput"),
            ('a[href="/autowait"]', "Auto Wait", "/autowait"),
        ],
    )
    def test_link(self, selector, expected_title, expected_url):
        self.page.link_to(selector)
        title = self.page.get_title()
        url = self.page.get_url()

        assert title == expected_title
        assert url == f"{self.base_url}{expected_url}"
