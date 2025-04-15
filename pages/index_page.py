from pages.base_page import BasePage

from typing import Self


class IndexPage:
    def __init__(self, base_page: BasePage):
        self.base_page = base_page
        self.url = "https://www.uitestingplayground.com/"

        self.dynamicid_selector = 'a[href="/dynamicid"]'
        self.classattr_selector = 'a[href="/classattr"]'
        self.hiddenlayers_selector = 'a[href="/hiddenlayers"]'
        self.loaddelay_selector = 'a[href="/loaddelay"]'
        self.ajax_selector = 'a[href="/ajax"]'
        self.clientdelay_selector = 'a[href="/clientdelay"]'
        self.click_selector = 'a[href="/click"]'
        self.textinput_selector = 'a[href="/textinput"]'
        self.scrollbars_selector = 'a[href="/scrollbars"]'
        self.dynamictable_selector = 'a[href="/dynamictable"]'
        self.verifytext_selector = 'a[href="/verifytext"]'
        self.progressbar_selector = 'a[href="/progressbar"]'
        self.visibility_selector = 'a[href="/visibility"]'
        self.sampleapp_selector = 'a[href="/sampleapp"]'
        self.mouseover_selector = 'a[href="/mouseover"]'
        self.nbsp_selector = 'a[href="/nbsp"]'
        self.overlapped_selector = 'a[href="/overlapped"]'
        self.shadowdom_selector = 'a[href="/shadowdom"]'
        self.alerts_selector = 'a[href="/alerts"]'
        self.upload_selector = 'a[href="/upload"]'
        self.animation_selector = 'a[href="/animation"]'
        self.disabledinput_selector = 'a[href="/disabledinput"]'
        self.autowait_selector = 'a[href="/autowait"]'

    def link_to(self, selector) -> Self:
        self.base_page.find(selector).click()
        return self

    def go(self) -> Self:
        self.base_page.goto(self.url)
        return self

    def get_title(self) -> str:
        return self.base_page.get_title()

    def get_url(self) -> str:
        return self.base_page.get_url()
