#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import allure

from test_case.base_test.test_base import TestBase

class TestBrandApartmentList(TestBase):

    def goto_brandapartmentlist(self):
        return self.shouye.goto_func_entrance_zf().rent_house_function_entrance("品牌公寓")

    @allure.description("点击品牌公寓列表页搜索框")
    def test_click_brandapartmentlist_search(self):
        self.goto_brandapartmentlist().click_brandapartmentlist_search().screenshot()

    @allure.description("点击品牌公寓列表页,类型-整租")
    def test_test_click_brandapartmentlist_type(self):
        self.goto_brandapartmentlist().click_brandapartmentlist_type().\
            click_brandapartmentlist_filter("整租").click_brandapartmentlist_confirm().screenshot()

    @allure.description("品牌公寓列表页-区域-玄武区-北京东路，点击确定")
    def test_click_brandapartmentlist_location(self):
        step1 = self.goto_brandapartmentlist().click_brandapartmentlist_location().\
            click_brandapartmentlist_filter("玄武区").click_brandapartmentlist_filter("北京东路")
        step1.screenshot()
        step1.click_brandapartmentlist_confirm().screenshot()

    @allure.description("品牌公寓列表页-地铁-1号线-迈皋桥，点击确定")
    def test_click_brandapartmentlist_subway(self):
        step1 = self.goto_brandapartmentlist().\
            click_brandapartmentlist_location().\
            click_brandapartmentlist_filter("地铁").\
            click_brandapartmentlist_filter("1号线").\
            click_brandapartmentlist_filter("迈皋桥站")
        step1.screenshot()
        step1.click_brandapartmentlist_confirm().screenshot()

    @allure.description("品牌公寓列表页-租金-1200-2000元，点击确定")
    def test_click_brandapartmentlist_price(self):
        step1 = self.goto_brandapartmentlist(). \
            click_brandapartmentlist_price().click_brandapartmentlist_filter("1200-2000元")
        step1.screenshot()
        step1.click_brandapartmentlist_confirm().screenshot()

    @allure.description("品牌公寓列表页-筛选-一室/20-50㎡/朝南/空调/家电齐全，点击确定")
    def test_click_brandapartmentlist_selectd(self):
        step1 = self.goto_brandapartmentlist(). \
            click_brandapartmentlist_selected().click_brandapartmentlist_filter("一室").click_brandapartmentlist_filter("20-50㎡").\
            click_brandapartmentlist_filter("朝南").click_brandapartmentlist_filter("空调")
        step1.screenshot()
        step2 = step1.brandapartmentlist_swipe("家电齐全")
        step2.screenshot()
        step3 = step2.click_brandapartmentlist_filter("近地铁")
        step3.screenshot()
        step3.click_brandapartmentlist_confirm().screenshot()

    @allure.description("品牌公寓列表页，排序 ，价格从低到高")
    def test_click_brandapartmentlist_order(self):
        self.goto_brandapartmentlist().click_brandapartmentlist_order().\
            click_brandapartmentlist_filter("价格从低到高").screenshot()

    @allure.description("品牌公寓列表页,点击第一个房源")
    def test_click_brandapartmentlist_house(self):
        self.goto_brandapartmentlist().click_brandapartmentlist_house().screenshot()













