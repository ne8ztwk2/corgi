from playwright.sync_api import Page
from book_page import BookPage


class IndexPage:

    def __init__(self, page: Page):

        self.page = page

        self.index_url = "https://www.douban.com"

        self.book_link = "https://book.douban.com"
        self.movie_link = "https://movie.douban.com"
        self.music_link = "https://music.douban.com"
        self.location_link = "https://www.douban.com/location/"
        self.group_link = "https://www.douban.com/group/"
        self.reading_link = "https://read.douban.com/"
        self.fm_link = "https://fm.douban.com/"
        self.time_link = "https://time.douban.com/"
        self.market_link = "https://market.douban.com"

        self.link_book_locator = self.page.locator(".lnk-book")
        ...

    def link_book(self) -> BookPage:
        self.page.goto(self.index_url)
        print(self.link_book_locator.get_attribute("href"))
        self.link_book_locator.click()
        return BookPage(self.page)

        ...

    def link_movie(self):
        ...

    def link_music(self):
        ...

    def link_group(self):
        ...

    def link_reading(self):
        ...

    def link_fm(self):
        ...

    def link_time(self):
        ...

    def link_market(self):
        ...

    def link_location(self):
        ...

    def search(self):
        ...

    def download_with_qrcode(self):
        ...

    def download(self):
        ...

    def login_with_qrcode(self):
        ...

    def login(self, username, password):
        ...

    def login_with_wechat(self):
        ...

    def login_with_weibo(self):
        ...

    def link_agreement(self):
        ...


if __name__ == "__main__":

    from playwright.sync_api import sync_playwright

    # p = IndexPage()
    # p.link_book().search("python")

    # 初始化 Playwright
    with sync_playwright() as playwright:
        # 启动浏览器（例如 Chromium）
        browser = playwright.chromium.launch(
            headless=False)  # headless=False 表示显示浏览器窗口
        # 创建新页面
        page = browser.new_page()

        # 传入 Page 对象实例化 IndexPage
        p = IndexPage(page)
        p.link_book().search("python")

        # 关闭浏览器（可选）
        browser.close()
