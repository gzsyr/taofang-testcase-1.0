import allure
from test_case.base_test.test_base import TestBase


class TestSellHouseList(TestBase):
    """
    二手房列表页面的所有用例
    """

    @allure.description("点击搜素框")
    def test_click_search_text(self):
        """
        点击列表搜素框
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_search_text().screenshot()

    @allure.description("点击地图")
    def test_click_map(self):
        """
        点击列表地图
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_map().screenshot()

    @allure.description("点击消息")
    def test_click_msg(self):
        """
        点击列表消息
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_msg().screenshot()

    @allure.description("点击列表功能入口-找小区")
    def test_click_neighborhood(self):
        """
        点击列表功能入口-找小区
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_neighborhood().screenshot()