from web.pages.index_page import IndexPage


class TestIndexPage(IndexPage):

    def setup_class(self):

        self.page.goto(self.index_url)

    def test_link_to_dymicicd(self):
        title = self.link_dynamicid().get_title
        assert title == "Dynamic ID"

    def teardown_class(self):
        self.page.quit()
