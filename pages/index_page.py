from pages.base_page import BasePage
from dynamicid_page import DynamicidPage
from classattr_page import ClassattrPage
from hiddenlayers_page import HiddenlayersPage
from loaddelay_page import LoaddelayPage
from pages.ajaxdata_page import AjaxPage
from clientdelay_page import ClientdelayPage
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
from pages.animatedbutton_page import AnimationPage
from disabledinput_page import DisabledinputPage
from autowait_page import AutowaitPage


class IndexPage:

    def __init__(self, page: BasePage):
        self.page = page
        self.index_url = "https://www.uitestingplayground.com/"

    def link_dynamicid(self):
        self.page.click('a[href="/dynamicid"]')
        return DynamicidPage(self.page)

    def link_classattr(self):
        self.page.click('a[href="/classattr"]')
        return ClassattrPage(self.page)

    def link_hiddenlayers(self):
        self.page.click('a[href="/hiddenlayers"]')
        return HiddenlayersPage(self.page)

    def link_loaddelay(self):
        self.page.click('a[href="/loaddelay"]')
        return LoaddelayPage(self.page)

    def link_ajax(self):
        self.page.click('a[href="/ajax"]')
        return AjaxPage(self.page)

    def link_clientdelay(self):
        self.page.click('a[href="/clientdelay"]')
        return ClientdelayPage(self.page)

    def link_click(self):
        self.page.click('a[href="/click"]')
        return ClickPage(self.page)

    def link_textinput(self):
        self.page.click('a[href="/textinput"]')
        return TextinputPage(self.page)

    def link_scrollbars(self):
        self.page.click('a[href="/scrollbars"]')
        return ScrollbarsPage(self.page)

    def link_dynamictable(self):
        self.page.click('a[href="/dynamictable"]')
        return DynamictablePage(self.page)

    def link_verifytext(self):
        self.page.click('a[href="/verifytext"]')
        return VerifytextPage(self.page)

    def link_progressbar(self):
        self.page.click('a[href="/progressbar"]')
        return ProgressbarPage(self.page)

    def link_visibility(self):
        self.page.click('a[href="/visibility"]')
        return VisibilityPage(self.page)

    def link_sampleapp(self):
        self.page.click('a[href="/sampleapp"]')
        return SampleappPage(self.page)

    def link_mouseover(self):
        self.page.click('a[href="/mouseover"]')
        return MouseoverPage(self.page)

    def link_nbsp(self):
        self.page.click('a[href="/nbsp"]')
        return NbspPage(self.page)

    def link_overlapped(self):
        self.page.click('a[href="/overlapped"]')
        return OverlappedPage(self.page)

    def link_shadowdom(self):
        self.page.click('a[href="/shadowdom"]')
        return ShadowdomPage(self.page)

    def link_alerts(self):
        self.page.click('a[href="/alerts"]')
        return AlertsPage(self.page)

    def link_upload(self):
        self.page.click('a[href="/upload"]')
        return UploadPage(self.page)

    def link_animation(self):
        self.page.click('a[href="/animation"]')
        return AnimationPage(self.page)

    def link_disabledinput(self):
        self.page.click('a[href="/disabledinput"]')
        return DisabledinputPage(self.page)

    def link_autowait(self):
        self.page.click('a[href="/autowait"]')
        return AutowaitPage(self.page)


if __name__ == "__main__":
    from selenium import webdriver
    import pages.selenium_page as selenium_page

    driver = webdriver.Firefox()

    sp = selenium_page.SeleniumPage(driver)
    sp.goto("https://www.uitestingplayground.com/")
    p = IndexPage(sp)
    lkt = p.link_dynamicid()

    print(lkt.get_title)
    print(lkt.get_button_id)

    driver.quit()
