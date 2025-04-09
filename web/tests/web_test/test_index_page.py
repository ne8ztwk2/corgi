from web.pages.index_page import IndexPage


class TestIndexPage():

    def setup_class(self):
        self.index_page = IndexPage()
        self.index_page.goto(self.index_page.index_url)

    def test_link_to_dymicicd(self):
        title = self.index_page.link_dynamicid().get_title
        assert title == "Dynamic ID"
