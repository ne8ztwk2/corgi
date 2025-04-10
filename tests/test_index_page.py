from pages.index_page import IndexPage


class TestIndexPage(IndexPage):

    def setup_class(self):

        self.page.goto(self.index_url)

    def teardown_class(self):
        self.page.quit()

    def test_link_to_dymicicd(self):
        title = self.link_dynamicid().get_title
        assert title == "Dynamic ID"

    def test_link_to_classattr(self):
        title = self.link_classattr().get_title
        assert title == "Class Attribute"

    def test_link_to_hiddenlayers(self):
        title = self.link_hiddenlayers().get_title
        assert title == "Hidden Layers"

    def test_link_to_loaddelay(self):
        title = self.link_loaddelay().get_title
        assert title == "Load Delay"

    def test_link_to_ajax(self):
        title = self.link_ajax().get_title
        assert title == "AJAX Data"

    def test_link_to_clientdelay(self):
        title = self.link_clientdelay().get_title
        assert title == "Client Delay"

    def test_link_to_click(self):
        title = self.link_click().get_title
        assert title == "Click"

    def test_link_to_textinput(self):
        title = self.link_textinput().get_title
        assert title == "Text Input"

    def test_link_to_scrollbars(self):
        title = self.link_scrollbars().get_title
        assert title == "Scrollbars"

    def test_link_to_dynamictable(self):
        title = self.link_dynamictable().get_title
        assert title == "Dynamic Table"

    def test_link_to_verifytext(self):
        title = self.link_verifytext().get_title
        assert title == "Verify Text"

    def test_link_to_progressbar(self):
        title = self.link_progressbar().get_title
        assert title == "Progress Bar"

    def test_link_to_visibility(self):
        title = self.link_visibility().get_title
        assert title == "Visibility"

    def test_link_to_sampleapp(self):
        title = self.link_sampleapp().get_title
        assert title == "Sample App"

    def test_link_to_mouseover(self):
        title = self.link_mouseover().get_title
        assert title == "Mouse Over"

    def test_link_to_nbsp(self):
        title = self.link_nbsp().get_title
        assert title == "NBSP"

    def test_link_to_overlapped(self):
        title = self.link_overlapped().get_title
        assert title == "Overlapped"

    def test_link_to_shadowdom(self):
        title = self.link_shadowdom().get_title
        assert title == "Shadow DOM"

    def test_link_to_alerts(self):
        title = self.link_alerts().get_title
        assert title == "Alerts"

    def test_link_to_upload(self):
        title = self.link_upload().get_title
        assert title == "File Upload"

    def test_link_to_animation(self):
        title = self.link_animation().get_title
        assert title == "Animation"

    def test_link_to_disabledinput(self):
        title = self.link_disabledinput().get_title
        assert title == "Disabled Input"

    def test_link_to_autowait(self):
        title = self.link_autowait().get_title
        assert title == "Auto Wait"
