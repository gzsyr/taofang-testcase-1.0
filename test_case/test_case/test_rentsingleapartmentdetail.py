#!/usr/bin/env python 
# -*- coding:utf-8 -*- by zzh
import allure
import pytest

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 租房-独栋公寓详情页面的测试")
class TestSingleApartmentDetail(TestBase):
    """
    独栋公寓详情页
    """
    def goto_singleapartmentdetail(self):
        return self.shouye.goto_func_entrance_zf().\
            rent_house_function_entrance("独栋公寓").click_singleapartmentlist_house()

    @allure.description("独栋公寓详情页，点击房源图片")
    def test_click_singleapartment_detail_pic(self):
        self.goto_singleapartmentdetail().click_singleapartment_detail_pic().screenshot()

    @allure.description("独栋公寓详情页，点击在租房型第一个房型")
    def test_click_singleapartment_detail_house(self):
        self.goto_singleapartmentdetail().click_singleapartment_detail_house().screenshot()

    @allure.description("独栋公寓详情页,点击公寓品牌右侧“查看全部”")
    def test_click_singleapartment_detail_full_house(self):
        self.goto_singleapartmentdetail().fun_swipe("buttom").\
            click_singleapartment_detail_full_house().screenshot()

    @allure.description("独栋公寓详情页,点击公寓位置-地图")
    def test_click_singleapartment_detail_map(self):
        self.goto_singleapartmentdetail().fun_swipe("buttom").\
            click_singleapartment_detail_map().screenshot()

    @allure.description("独栋公寓详情页,点击“联系公寓”按钮")
    def test_click_singleapartment_detail_contact(self):
        self.goto_singleapartmentdetail().click_singleapartment_detail_contact().screenshot()


