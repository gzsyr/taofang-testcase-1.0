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

    @allure.description("点击列表功能入口-个人房源")
    def test_click_personal_housing(self):
        """
        点击列表功能入口-个人房源
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_personal_housing().screenshot()

    @allure.description("点击列表功能入口-学校地图")
    def test_click_school_map(self):
        """
        点击列表功能入口-学校地图
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_school_map().screenshot()

    @allure.description("点击列表功能入口-查房价")
    def test_click_check_prices(self):
        """
        点击列表功能入口-查房价
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_check_prices().screenshot()

    @allure.description("点击列表功能入口-我要买房")
    def test_click_buy_house(self):
        """
        点击列表功能入口-我要买房
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_buy_house().screenshot()

    @allure.description("点击列表-帮你找房icon")
    def test_click_find_room(self):
        """
        点击列表-帮你找房icon
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_find_room().screenshot()

    @allure.description("点击列表-快速卖房ICON")
    def test_click_fast_selling(self):
        """
        点击列表-快速卖房ICON
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_fast_selling().screenshot()

    @allure.description("点击列表-买房咨询师ICON")
    def test_click_consultant(self):
        """
        点击列表-买房咨询师ICON
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_consultant().screenshot()

    @allure.description("点击列表-楼市头条")
    def test_click_headlines(self):
        """
        点击列表-楼市头条
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_headlines().screenshot()

    @allure.description("点击筛选项：位置-附近-1km")
    def test_click_screening_location_kilo(self):
        """
        点击筛选项：位置-附近-1km
        :return:
        """
        self.shouye. \
            goto_func_entrance_esf(). \
            click_screening_location(). \
            click_filter_position_menu("附近"). \
            click_filter_position_menu("1km"). \
            screenshot()

    @allure.description("点击筛选项：位置-附近")
    def test_click_screening_location_near(self):
        """
        点击筛选项：位置-附近
        :return:
        """
        self.shouye. \
            goto_func_entrance_esf(). \
            click_empty(). \
            click_screening_location(). \
            click_filter_position_menu("附近"). \
            screenshot()

