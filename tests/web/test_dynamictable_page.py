from pages.dynamictable_page import DynamictablePage

import pytest


@pytest.mark.usefixtures("basepage")
class TestDynamictablePage(DynamictablePage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/dynamictable")

    def test_table_data(self):
        table_data = self.get_table_data()
        assert table_data is not None

    def teardown_class(self):
        self.page.quit()
