from pages.animatedbutton_page import AnimationPage


class TestAnimationPage(AnimationPage):

    def setup_class(self):
        self.page.goto("https://www.uitestingplayground.com/animation")

    def test_wait_for_animation(self):
        self.wait_for_animation()
        assert self.page.is_visible("#animatedElement")

    def teardown_class(self):
        self.page.quit()
