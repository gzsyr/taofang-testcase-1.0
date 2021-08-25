#!/usr/bin/env python 
# -*- coding:utf-8 -*- by zzh

import allure

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 租房-独栋公寓列表页面的测试")
class TestSingleApartmentList(TestBase):
    """
    租房-独栋公寓列表页面
    """
    def goto_singleapartmentlist(self):
        return self.shouye.goto_func_entrance_zf().rent_house_function_entrance("独栋公寓")

    @allure.description("独栋公寓列表页-品牌，选择朗诗寓，确定")
    def test_click_singleapartmentlist_brand(self):
        step1 = self.goto_singleapartmentlist().click_singleapartmentlist_brand().\
            click_singleapartmentlist_filter("朗诗寓")
        step1.screenshot()
        step1.click_singleapartmentlist_confirm().screenshot()

    @allure.description("独栋公寓列表页-区域-玄武区-北京东路，确定")
    def test_click_singleapartmentlist_location(self):
        step1 = self.goto_singleapartmentlist().click_singleapartmentlist_location(). \
            click_singleapartmentlist_filter("玄武区").click_singleapartmentlist_filter("北京东路")
        step1.screenshot()
        step1.click_singleapartmentlist_confirm().screenshot()

    @allure.description("独栋公寓列表页-地铁-1号线-迈皋桥，确定")
    def test_click_singleapartmentlist_subway(self):
        step1 = self.goto_singleapartmentlist().click_singleapartmentlist_location(). \
            click_singleapartmentlist_filter("地铁").click_singleapartmentlist_filter("1号线").\
            click_singleapartmentlist_filter("迈皋桥站")
        step1.screenshot()
        step1.click_singleapartmentlist_confirm().screenshot()

    @allure.description("独栋公寓列表页-租金-1200-2000元")
    def test_click_singleapartmentlist_rent(self):
        self.goto_singleapartmentlist().click_singleapartmentlist_rent().\
            click_singleapartmentlist_filter("1200-2000元").screenshot()

    @allure.description("独栋公寓列表页-面积,选择20-50㎡")
    def test_click_singleapartmentlist_area(self):
        self.goto_singleapartmentlist().click_singleapartmentlist_area().\
            click_singleapartmentlist_filter("20-50㎡").screenshot()

    @allure.description("独栋公寓列表页,点击第一个房源")
    def test_click_singleapartmentlist_house(self):
        self.goto_singleapartmentlist().click_singleapartmentlist_house().screenshot()





