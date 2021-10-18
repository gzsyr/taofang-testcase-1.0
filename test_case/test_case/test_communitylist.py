#!/usr/bin/env python 
# -*- coding:utf-8 -*- by zzh
import allure
import pytest

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 找小区列表页面的测试")
class Test_CommunityList(TestBase):
    """
    找小区列表页面
    """
    def goto_communitylist(self):
        return self.shouye.goto_func_entrance_first("找小区")

    @allure.description("点击搜索框")
    def test_click_community_search(self):
        self.goto_communitylist().click_community_search().screenshot()

    @allure.description("点击搜索框旁边的地图按钮")
    def test_click_community_map(self):
        self.goto_communitylist().click_community_map().screenshot()

    @allure.description("点击搜索框旁边的消息按钮")
    def test_click_community_msg(self):
        self.goto_communitylist().click_community_msg().screenshot()

    @allure.description("点击筛选-位置")
    def test_click_community_location(self):
        self.goto_communitylist().click_community_location().screenshot()

    @allure.description("点击位置-附近-5km")
    def test_click_community_location_near(self):
        self.goto_communitylist().click_community_location().fun_para("附近").fun_para("5km").screenshot()

    @allure.description("点击位置->区域-鼓楼区-福建路")
    def test_click_community_location_area(self):
        self.goto_communitylist().click_community_location().\
            fun_para("区域").fun_para("鼓楼区").fun_para("福建路").screenshot()

    @allure.description("点击均价->下级选项(1.5-2万元/㎡)")
    def test_click_community_price(self):
        self.goto_communitylist().click_community_price().fun_para("1.5-2万元/ m²").screenshot()

    @allure.description("点击均价->自定义")
    def test_click_community_customize(self):
        self.goto_communitylist().click_community_price().\
            click_community_lowest_price().click_community_highest_price().\
            click_community_confirm().screenshot()

    @allure.description("点击房龄-2-5年")
    def test_click_community_room_age(self):
        self.goto_communitylist().click_community_room_age().fun_para("2-5年").screenshot()

    @allure.description("点击更多->下级选项（品牌开发商），点击确定")
    def test_click_community_more(self):
        self.goto_communitylist().click_community_more().\
            fun_para("品牌开发商").click_community_confirm().screenshot()

    @allure.description("点击排序->下级选项（涨幅从低到高）")
    def test_click_community_sort(self):
        self.goto_communitylist().click_community_sort(). \
            fun_para("涨幅从低到高").screenshot()

    @allure.description("选择房龄->2-5年，点击清空按钮")
    def test_click_community_delete(self):
        self.goto_communitylist().click_community_room_age().\
            fun_para("2-5年").click_community_delete().screenshot()

    @allure.description("点击筛选项（有VR、地铁盘、大型社区、小区解读）")
    @pytest.mark.parametrize("text", ["有VR", "大型社区", "小区解读"])
    def test_click_community_filter(self, text):
        self.goto_communitylist().fun_para(text).screenshot()

    @allure.description("点击小区列表第一个小区")
    def test_goto_community_detail(self):
        self.goto_communitylist().go_community_detail().screenshot()
		
    @allure.description("点击小区旁边的im入口")
    def test_click_community_im(self):
        self.goto_communitylist().click_community_im().screenshot()
		
	
