#!/usr/bin/env python 
# -*- coding:utf-8 -*- by zzh

import allure
import pytest

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 写字楼详情页面的测试")
class TestOfficeBuildingDetail(TestBase):
    """
    写字楼详情页
    """
    def goto_officebuildingdetail(self):
        return self.shouye.goto_func_entrance_zf().rent_house_function_entrance("写字楼").\
            func_swipe("推荐写字楼").goto_office_recommenddetail()


    @allure.description("点击分享")
    def test_click_officebuilding_detail_share(self):
        self.goto_officebuildingdetail().click_officebuilding_detail_share().screenshot()

    @allure.description("点击收藏")
    def test_click_officebuilding_detail_collect(self):
        self.goto_officebuildingdetail().click_officebuilding_detail_collect().screenshot()

    @allure.description("点击右上角消息入口")
    def test_click_officebuilding_detail_msg(self):
        self.goto_officebuildingdetail().click_officebuilding_detail_msg().screenshot()

    @allure.description("点击房源图片")
    def test_click_officebuilding_detail_pic(self):
        self.goto_officebuildingdetail().click_officebuilding_detail_pic().screenshot()

    @allure.description("点击小地图按钮")
    def test_click_officebuilding_detail_location(self):
        self.goto_officebuildingdetail().click_officebuilding_detail_location().screenshot()

    @allure.description("点击价格旁边的im消息入口")
    def test_click_officebuilding_detail_price_im(self):
        self.goto_officebuildingdetail().click_officebuilding_detail_price_im().screenshot()

    @allure.description("点击房源概况-预约看房")
    def test_click_officebuilding_detail_info_im(self):
        self.goto_officebuildingdetail().click_officebuilding_detail_info_im().screenshot()

    @allure.description("点击房源描述-电话")
    def test_click_officebuilding_detail_iv_call(self):
        self.goto_officebuildingdetail().officebuilding_swipe("展开").\
            click_officebuilding_detail_iv_call().screenshot()

    @allure.description("点击房源描述-im入口")
    def test_click_officebuilding_detail_iv_im(self):
        self.goto_officebuildingdetail().officebuilding_swipe("展开").\
            click_officebuilding_detail_iv_im().screenshot()

    @allure.description("点击房源描述-展开")
    def test_click_officebuilding_detail_tv_more(self):
        self.goto_officebuildingdetail().officebuilding_swipe("展开"). \
            click_officebuilding_detail_tv_more().screenshot()

    @allure.description("点击房源描述-大地图")
    def test_click_officebuilding_detail_map(self):
        self.goto_officebuildingdetail().officebuilding_swipe("我要举报"). \
            click_officebuilding_detail_map().screenshot()

    @allure.description("点击房源描述-地铁，咨询详情按钮")
    def test_click_officebuilding_detail_tv_im(self):
        self.goto_officebuildingdetail().officebuilding_swipe("我要举报"). \
            click_officebuilding_detail_tv_im().screenshot()

    @allure.description("点击房源描述-地铁，共x条路线")
    def test_click_officebuilding_detail_tv_control(self):
        self.goto_officebuildingdetail().officebuilding_swipe("我要举报"). \
            click_officebuilding_detail_tv_control().screenshot()

    @allure.description("点击举报")
    def test_click_officebuilding_detail_complaint(self):
        self.goto_officebuildingdetail().officebuilding_swipe("附近写字楼"). \
            click_officebuilding_detail_complaint().screenshot()

    @allure.description("点击附近写字楼-查看全部")
    def test_click_officebuilding_detail_list_more(self):
        self.goto_officebuildingdetail().officebuilding_swipe("附近写字楼"). \
            click_officebuilding_detail_list_more().screenshot()

    @allure.description("点击附近写字楼-第一个楼盘")
    def test_click_officebuilding_detail_list_house(self):
        self.goto_officebuildingdetail().officebuilding_swipe("附近写字楼"). \
            click_officebuilding_detail_list_house().screenshot()

    @allure.description("点击悬浮-提问")
    def test_click_officebuilding_detail_arrow(self):
        self.goto_officebuildingdetail().click_officebuilding_detail_arrow().screenshot()

    @allure.description("点击底部-经济人信息")
    def test_click_officebuilding_detail_btn_person(self):
        self.goto_officebuildingdetail().click_officebuilding_detail_btn_person().screenshot()

    @allure.description("点击底部-电话咨询")
    def test_click_officebuilding_detail_btn_call(self):
        self.goto_officebuildingdetail().click_officebuilding_detail_btn_call().screenshot()

    @allure.description("点击底部-在线咨询")
    def test_click_officebuilding_detail_btn_im(self):
        self.goto_officebuildingdetail().click_officebuilding_detail_btn_im().screenshot()

























