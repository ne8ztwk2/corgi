from pages.base_page import BasePage
from dynamicid_page import DynamicidPage
from classattr_page import ClassattrPage
from hiddenlayers_page import HiddenlayersPage
from loaddelay_page import LoaddelayPage
from pages.ajaxdata_page import AjaxdataPage
from clientsidedelay_page import ClientdelayPage
from click_page import ClickPage
from textinput_page import TextinputPage
from scrollbars_page import ScrollbarsPage
from dynamictable_page import DynamictablePage
from verifytext_page import VerifytextPage
from progressbar_page import ProgressbarPage
from visibility_page import VisibilityPage
from sampleapp_page import SampleappPage
from mouseover_page import MouseoverPage
from nbsp_page import NbspPage
from overlapped_page import OverlappedPage
from shadowdom_page import ShadowdomPage
from alerts_page import AlertsPage
from upload_page import UploadPage
from pages.animatedbutton_page import AnimatedbuttonPage
from disabledinput_page import DisabledinputPage
from autowait_page import AutowaitPage
from typing import Self


class IndexPage:
    def __init__(self, page: BasePage):
        self.page = page
        self.url = "https://www.uitestingplayground.com/"

        self.dynamicid_locator = 'a[href="/dynamicid"]'
        self.classattr_locator = 'a[href="/classattr"]'
        self.hiddenlayers_locator = 'a[href="/hiddenlayers"]'
        self.loaddelay_locator = 'a[href="/loaddelay"]'
        self.ajax_locator = 'a[href="/ajax"]'
        self.clientdelay_locator = 'a[href="/clientdelay"]'
        self.click_locator = 'a[href="/click"]'
        self.textinput_locator = 'a[href="/textinput"]'
        self.scrollbars_locator = 'a[href="/scrollbars"]'
        self.dynamictable_locator = 'a[href="/dynamictable"]'
        self.verifytext_locator = 'a[href="/verifytext"]'
        self.progressbar_locator = 'a[href="/progressbar"]'
        self.visibility_locator = 'a[href="/visibility"]'
        self.sampleapp_locator = 'a[href="/sampleapp"]'
        self.mouseover_locator = 'a[href="/mouseover"]'
        self.nbsp_locator = 'a[href="/nbsp"]'
        self.overlapped_locator = 'a[href="/overlapped"]'
        self.shadowdom_locator = 'a[href="/shadowdom"]'
        self.alerts_locator = 'a[href="/alerts"]'
        self.upload_locator = 'a[href="/upload"]'
        self.animation_locator = 'a[href="/animation"]'
        self.disabledinput_locator = 'a[href="/disabledinput"]'
        self.autowait_locator = 'a[href="/autowait"]'

    def link_dynamicid(self):
        self.page.find(self.dynamicid_locator).click()
        return DynamicidPage(self.page)

    def link_classattr(self):
        self.page.find(self.classattr_locator).click()
        return ClassattrPage(self.page)

    def link_hiddenlayers(self):
        self.page.find(self.hiddenlayers_locator).click()
        return HiddenlayersPage(self.page)

    def link_loaddelay(self):
        self.page.find(self.loaddelay_locator).click()
        return LoaddelayPage(self.page)

    def link_ajax(self):
        self.page.find(self.ajax_locator).click()
        return AjaxdataPage(self.page)

    def link_clientdelay(self):
        self.page.find(self.clientdelay_locator).click()
        return ClientdelayPage(self.page)

    def link_click(self):
        self.page.find(self.click_locator).click()
        return ClickPage(self.page)

    def link_textinput(self):
        self.page.find(self.textinput_locator).click()
        return TextinputPage(self.page)

    def link_scrollbars(self):
        self.page.find(self.scrollbars_locator).click()
        return ScrollbarsPage(self.page)

    def link_dynamictable(self):
        self.page.find(self.dynamictable_locator).click()
        return DynamictablePage(self.page)

    def link_verifytext(self):
        self.page.find(self.verifytext_locator).click()
        return VerifytextPage(self.page)

    def link_progressbar(self):
        self.page.find(self.progressbar_locator).click()
        return ProgressbarPage(self.page)

    def link_visibility(self):
        self.page.find(self.visibility_locator).click()
        return VisibilityPage(self.page)

    def link_sampleapp(self):
        self.page.find(self.sampleapp_locator).click()
        return SampleappPage(self.page)

    def link_mouseover(self):
        self.page.find(self.mouseover_locator).click()
        return MouseoverPage(self.page)

    def link_nbsp(self):
        self.page.find(self.nbsp_locator).click()
        return NbspPage(self.page)

    def link_overlapped(self):
        self.page.find(self.overlapped_locator).click()
        return OverlappedPage(self.page)

    def link_shadowdom(self):
        self.page.find(self.shadowdom_locator).click()
        return ShadowdomPage(self.page)

    def link_alerts(self):
        self.page.find(self.alerts_locator).click()
        return AlertsPage(self.page)

    def link_upload(self):
        self.page.find(self.upload_locator).click()
        return UploadPage(self.page)

    def link_animation(self):
        self.page.find(self.animation_locator).click()
        return AnimatedbuttonPage(self.page)

    def link_disabledinput(self):
        self.page.find(self.disabledinput_locator).click()
        return DisabledinputPage(self.page)

    def link_autowait(self):
        self.page.find(self.autowait_locator).click()
        return AutowaitPage(self.page)

    def go(self) -> Self:
        self.page.goto(self.url)
        return self
