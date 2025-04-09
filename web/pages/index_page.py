from basepage import Basepage
from dynamicid_page import DynamicidPage


class IndexPage:

    def __init__(self, page: Basepage):

        self.page = page

        self.index_url = "https://www.uitestingplayground.com/"

        ...

    def link_dynamicid(self):
        self.page.click('a[href="/dynamicid"]')
        return DynamicidPage(self.page)

    def link_classattr(self):
        self.page.click()
        ...

    def link_hiddenlayers(self):
        ...

    def link_loaddelay(self):
        ...

    def link_ajax(self):
        ...

    def link_clientdelay(self):
        ...

    def link_click(self):
        ...

    def link_textinput(self):
        ...

    def link_scrollbars(self):
        ...

    def link_dynamictable(self):
        ...

    def link_verifytext(self):
        ...

    def link_progressbar(self):
        ...

    def link_visibility(self):
        ...

    def link_sampleapp(self):
        ...

    def link_mouseover(self):
        ...

    def link_nbsp(self):
        ...

    def link_overlapped(self):
        ...

    def link_shadowdom(self):
        ...

    def link_alerts(self):
        ...

    def link_upload(self):
        ...

    def link_animation(self):
        ...

    def link_disabledinput(self):
        ...

    def link_autowait(self):
        ...


if __name__ == "__main__":

    # from playwright.sync_api import sync_playwright

    # p = IndexPage()
    # p.link_book().search("python")

    # 初始化 Playwright
    # with sync_playwright() as playwright:
    #     # 启动浏览器（例如 Chromium）
    #     browser = playwright.chromium.launch(
    #         headless=False)  # headless=False 表示显示浏览器窗口
    #     # 创建新页面
    #     page = browser.new_page()

    #     # 传入 Page 对象实例化 IndexPage
    #     p = IndexPage(page)
    #     p.link_book().search("python")

    #     # 关闭浏览器（可选）
    #     browser.close()

    ...
    from selenium import webdriver
    import basepage_selenium
    driver = webdriver.Firefox()

    sp = basepage_selenium.BaseSeleniumPage(driver)
    sp.goto("https://www.uitestingplayground.com/")
    p = IndexPage(sp)
    lkt = p.link_dynamicid()

    print(lkt.get_title)
    print(lkt.get_button_id)

    driver.quit()
