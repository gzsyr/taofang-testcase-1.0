import allure
import pytest
from test_case.base_test.test_base import TestBase

class TestRentHouse(TestBase):

    """
    租房首页用例
    """

    @allure.description("租房首页点击搜索入口")
    def test_rent_house_search(self):
        """
        租房首页点击搜索入口
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_search().screenshot()

    @allure.description("租房首页点击地图找房")
    def test_map_find_room(self):
        """
        租房首页点击地图找房
        :return:
        """
        self.shouye.goto_func_entrance_zf().map_find_room().screenshot()

    @allure.description("租房首页点击通勤找房")
    def test_commuting_find_room(self):
        """
        租房首页点击通勤找房
        :return:
        """
        self.shouye.goto_func_entrance_zf().commuting_find_room().screenshot()

    @allure.description("租房首页点击消息")
    def test_rent_house_news(self):
        """
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_news().screenshot()

    @allure.description("租房首页点击功能入口")
    @pytest.mark.parametrize("func_entry", ["整租", "合租", "找室友", "个人房源", "品牌公寓",
                                            "商铺", "写字楼", "独栋公寓", "月租", "我要求租"])
    def test_rent_house_function_entrance(self, func_entry):
        self.shouye.goto_func_entrance_zf().rent_house_function_entrance(func_entry).screenshot()

    @allure.description("租房首页点击功能入口")
    @pytest.mark.parametrize("pos_text, func_entry", [("品牌公寓", "厂房"), ("品牌公寓", "车位")])
    def test_rent_house_function_entrance(self, pos_text, func_entry):
        self.shouye.goto_func_entrance_zf().func_entrance_swipe_left(pos_text).rent_house_function_entrance(func_entry).screenshot()

    @allure.description("租房首页点击附近tab")
    def test_rent_house_nearby(self):
        """
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_nearby().screenshot()

    @allure.description("租房首页点击公寓tab")
    def test_rent_house_apartment(self):
        """
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_apartment().screenshot()

    @allure.description("租房首页点击严选tab")
    def test_rent_house_strict_selection(self):
        """
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_strict_selection().screenshot()

    @allure.description("租房首页点击写字楼tab")
    def test_rent_house_office(self):
        """
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_office().screenshot()

    @allure.description("租房首页点击我的")
    def test_rent_house_mine(self):
        """
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_mine().screenshot()

    @allure.description("租房首页点击发布房源")
    def test_rent_house_release_house(self):
        """
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_release_house().screenshot()

    @allure.description("租房首页点击租房顾问")
    def test_rent_house_rent_consultant(self):
        """
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_rent_consultant().screenshot()
