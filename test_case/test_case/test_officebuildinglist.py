import allure
import pytest

from test_case.base_test.test_base import TestBase


class TestOfficeBuildingList(TestBase):
    """
    写字楼页面
    """
    def goto_officebuildinglist(self):
        """
        进入租房写字楼列表页
        :return:
        """
        return self.shouye.goto_func_entrance_zf().rent_house_function_entrance("写字楼")

    @allure.description("点击搜索框")
    def test_click_search_text(self):
        """
        点击搜索框
        """
        self.goto_officebuildinglist().click_officehouse_search().screenshot()

    @allure.description("点击IM,进入消息列表页")
    def test_click_message(self):
        """
        点击IM,进入消息列表页
        """
        self.goto_officebuildinglist().goto_message().screenshot()

    @allure.description("点击功能入口")
    @pytest.mark.parametrize("func_entry", ["租写字楼", "办公楼盘", "联合办公", "发布房源", "帮你找房"])
    def test_goto_func_entrance(self, func_entry):
        """
        点击功能入口："租写字楼", "办公楼盘", "联合办公", "发布房源", "帮你找房"
        """
        self.goto_officebuildinglist().goto_func_entrance(func_entry).screenshot()

    @allure.description("点击大家都在搜第一个")
    def test_goto_office_position(self):
        """
        点击大家都在搜第一个
        """
        self.goto_officebuildinglist().goto_office_position().screenshot()

    @allure.description("点击热门楼盘-查看全部")
    def test_goto_office_hotlist(self):
        """
        热门楼盘-查看全部
        """
        self.goto_officebuildinglist().goto_office_hotlist().screenshot()

    @allure.description("点击热门楼盘，第一个楼盘")
    def test_goto_office_hotdetail(self):
        """
        点击热门楼盘，第一个楼盘
        """
        self.goto_officebuildinglist().func_swipe("推荐写字楼").goto_office_hotdetail().screenshot()

    @allure.description("点击推荐楼写字楼 第一个")
    def test_goto_office_recommenddetail(self):
        """
        点击推荐楼写字楼 第一个
        """
        self.goto_officebuildinglist().func_swipe("tv_location").goto_office_recommenddetail().screenshot()
