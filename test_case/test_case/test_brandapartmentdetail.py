#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import allure
import pytest

from test_case.base_test.test_base import TestBase

class TestBrandApartmentDetail(TestBase):

    def goto_brandapartmentdetail(self):
        return self.shouye.goto_func_entrance_zf().\
            rent_house_function_entrance("品牌公寓").click_brandapartmentlist_house()

    @allure.description("品牌公寓详情页，点击收藏")
    def test_click_brandapartment_detail_collection(self):
        self.goto_brandapartmentdetail().click_brandapartment_detail_collection().screenshot()

    @allure.description("品牌公寓详情页，点击分享")
    def test_click_brandapartment_detail_share(self):
        self.goto_brandapartmentdetail().click_brandapartment_detail_share().screenshot()

    @allure.description("品牌公寓详情页，点击房源图片")
    def test_click_brandapartment_detail_pic(self):
        self.goto_brandapartmentdetail().click_brandapartment_detail_pic().screenshot()

    @allure.description("品牌公寓详情页，点击租金旁边的im入口")
    def test_click_brandapartment_detail_price_im(self):
        self.goto_brandapartmentdetail().click_brandapartment_detail_price_im().screenshot()

    @allure.description("品牌公寓详情页，点击房源信息右侧的投诉举报")
    def test_click_brandapartment_detail_complaint(self):
        self.goto_brandapartmentdetail().click_brandapartment_detail_complaint().screenshot()

    @allure.description("品牌公寓详情页，点击地图")
    def test_click_brandapartment_detail_map(self):
        self.goto_brandapartmentdetail().fun_swipe("房源描述").click_brandapartment_detail_map().screenshot()

    @allure.description("品牌公寓详情页，点击房源描述-咨询详情")
    def test_click_brandapartment_detail_tv_im(self):
        self.goto_brandapartmentdetail().fun_swipe("公寓品牌").click_brandapartment_detail_tv_im().screenshot()

    @allure.description("品牌公寓详情页，点击租博士入口")
    def test_click_brandapartment_detail_zuboshi(self):
        self.goto_brandapartmentdetail().fun_swipe("公寓品牌").click_brandapartment_detail_zuboshi().screenshot()

    @allure.description("品牌公寓详情页，点击公寓品牌名称")
    def test_click_brandapartment_detail_brandname(self):
        self.goto_brandapartmentdetail().fun_swipe("buttom").click_brandapartment_detail_brandname().screenshot()

    @allure.description("品牌公寓详情页，点击悬浮-提问")
    def test_click_brandapartment_detail_arrow(self):
        self.goto_brandapartmentdetail().click_brandapartment_detail_arrow().screenshot()

    @allure.description("品牌公寓详情页，点击底部-联系电话")
    def test_click_brandapartment_detail_btn_call(self):
        self.goto_brandapartmentdetail().click_brandapartment_detail_btn_call().screenshot()


    @allure.description("品牌公寓详情页，点击底部-预约看房")
    def test_click_brandapartment_detail_btn_im(self):
        self.goto_brandapartmentdetail().click_brandapartment_detail_btn_im().screenshot()


