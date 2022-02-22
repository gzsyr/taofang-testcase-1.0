#!/usr/bin/env python 
# -*- coding:utf-8 -*- by zzh

import allure
import pytest

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 找小区详情页面的测试")
class TestCommunityDetail(TestBase):
    """
    小区详情页
    """
    def goto_community_detail(self):
        return self.shouye.func_entrance_swipe_left("签到").func_entrance_swipe_left("查房价").goto_func_entrance_first("找小区").go_community_detail()

    @allure.description("点击分享")
    def test_click_community_detail_share(self):
        self.goto_community_detail().click_community_detail_share().screenshot()

    @allure.description("点击收藏")
    def test_click_community_detail_fav(self):
        self.goto_community_detail().click_community_detail_fav().screenshot()

    @allure.description("点击消息入口")
    def test_click_community_detail_msg(self):
        self.goto_community_detail().click_community_detail_msg().screenshot()

    @allure.description("点击小区名")
    def test_click_community_detail_name(self):
        self.goto_community_detail().click_community_detail_name().screenshot()

    @allure.description("点击小区名旁边的地图入口")
    def test_click_community_detail_smap(self):
        self.goto_community_detail().click_community_detail_smap().screenshot()

    @allure.description("点击房贷计算器")
    def test_click_community_detail_mortgage(self):
        self.goto_community_detail().click_community_detail_mortgage().screenshot()

    @allure.description("点击在售房源入口")
    def test_click_community_detail_sell(self):
        self.goto_community_detail().click_community_detail_sell().screenshot()

    @allure.description("点击在租房源入口")
    def test_click_community_detail_rent(self):
        self.goto_community_detail().click_community_detail_rent().screenshot()

    @allure.description("点击我是业主-去估价按钮")
    def test_click_community_detail_evaluate(self):
        self.goto_community_detail().click_community_detail_evaluate().screenshot()

    @allure.description("点击复制微信号")
    def test_click_community_detail_wechat(self):
        self.goto_community_detail().click_community_detail_wechat().screenshot()

    @allure.description("点击复制qq号")
    def test_click_community_detail_qq(self):
        self.goto_community_detail().click_community_detail_qq().screenshot()

    @allure.description("点击基础信息-查看更多")
    def test_click_community_detail_base_more(self):
        self.goto_community_detail().fun_swipe("周边配套").click_community_detail_base_more().screenshot()

    @allure.description("点击周边配套-地图")
    def test_click_community_detail_bmap(self):
        self.goto_community_detail().fun_swipe("小区户型").click_community_detail_bmap().screenshot()

    @allure.description("点击小区户型-第一个户型")
    def test_click_community_detail_layout(self):
        self.goto_community_detail().fun_swipe("小区户型").click_community_detail_layout().screenshot()

    @allure.description("点击小区户型-查看更多")
    def test_click_community_detail_layout_more(self):
        self.goto_community_detail().fun_swipe("小区户型").click_community_detail_layout_more().screenshot()

    @allure.description("点击小区解读-查看更多")
    def test_click_community_detail_block_more(self):
        self.goto_community_detail().fun_swipe("周边配套").fun_para("小区解读").\
            click_community_detail_block_more().screenshot()

    @allure.description("点击小区解读-在线咨询")
    def test_click_community_detail_block_ask(self):
        self.goto_community_detail().fun_swipe("周边配套").fun_para("小区解读"). \
            click_community_detail_block_ask().screenshot()

    @allure.description("点击小区专家第一个-im消息入口")
    def test_click_community_detail_iv_im(self):
        self.goto_community_detail().fun_swipe("周边配套").fun_para("小区解读").\
            click_community_detail_iv_im().screenshot()

    @allure.description("点击小区专家第一个-电话按钮")
    def test_click_community_detail_iv_call(self):
        self.goto_community_detail().fun_swipe("周边配套").fun_para("小区解读").\
            click_community_detail_iv_call().screenshot()

    @allure.description("点击小区专家-第一个小区专家")
    def test_click_community_detail_blockexpert(self):
        self.goto_community_detail().fun_swipe("周边配套").fun_para("小区解读"). \
            click_community_detail_blockexpert().screenshot()

    @allure.description("点击在售房源-第一个房源")
    def test_click_community_detail_sell_house(self):
        self.goto_community_detail().fun_swipe("周边配套").fun_para("租售情况"). \
            click_community_detail_sell_house().screenshot()

    @allure.description("点击在售房源底部‘同小区在售房源’按钮")
    def test_click_community_detail_sell_more(self):
        self.goto_community_detail().fun_swipe("周边配套").fun_para("租售情况"). \
            click_community_detail_sell_more().screenshot()

    @allure.description("点击周边小区-第一个小区")
    def test_click_community_detail_near_block(self):
        self.goto_community_detail().fun_swipe("周边配套").fun_para("相关推荐"). \
            click_community_detail_near_block().screenshot()

    # 改版周边小区底部无“马上找房”入口
    # @allure.description("点击周边小区底部‘马上找房’")
    # def test_click_community_detail_find_house(self):
    #     self.goto_community_detail().fun_swipe("基础信息").fun_para("相关推荐"). \
    #         click_community_detail_find_house().screenshot()

    @allure.description("点击底部经纪人信息")
    def test_click_community_detail_broker(self):
        self.goto_community_detail().click_community_detail_broker().screenshot()

    @allure.description("点击底部‘在线咨询’")
    def test_click_community_detail_tv_ask(self):
        self.goto_community_detail().click_community_detail_tv_ask().screenshot()

    @allure.description("点击底部‘拨打电话’")
    def test_click_community_detail_tv_call(self):
        self.goto_community_detail().click_community_detail_tv_call().screenshot()
