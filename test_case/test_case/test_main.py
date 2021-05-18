import allure
from test_case.base_test.test_base import TestBase


class TestMain(TestBase):
    """
    首页的用例
    """

    # shouye = App().start().main()

    @allure.description("点击“新房”tab，进入新房列表页面")
    def test_click_newhouse(self):
        self.shouye.goto_newhouse().screenshot()

    @allure.description("点击新房列表页面，列表项的第一个楼盘，进入详情页")
    def test_goto_newhouse_detail(self):
        self.shouye.goto_newhouse().goto_newhouse_detail().screenshot()

    @allure.description("点击新房详情页面的“查看更多”，进入相册页面")
    def test_goto_newhouse_detail(self):
        self.shouye.goto_newhouse().goto_newhouse_detail().goto_photo().screenshot()

