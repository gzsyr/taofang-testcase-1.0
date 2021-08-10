#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import allure
from page_object.base_page.base_page import BasePage

class CommunityDetail(BasePage):
    """
    小区详情页
    """
    def click_community_detail_share(self):
        """
        点击分享
        """
        with allure.step("点击分享"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_fav(self):
        """
        点击收藏
        """
        with allure.step("点击收藏"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_msg(self):
        """
        点击消息入口
        """
        with allure.step("点击消息入口"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self



    def click_community_detail_img(self):
        """
        点击小区图片
        """
        with allure.step("点击小区图片"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_name(self):
        """
        点击小区名
        """
        with allure.step("点击小区名"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self


    def click_community_detail_smap(self):
        """
        点击小区名旁边的地图按钮
        """
        with allure.step("点击小区名旁边的地图按钮"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self


    def click_community_detail_mortgage(self):
        """
        点击贷款计算器
        """
        with allure.step("点击贷款计算器"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self


    def click_community_detail_sell(self):
        """
        点击在售房源
        """
        with allure.step("点击在售房源"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self



    def click_community_detail_rent(self):
        """
        点击在租房源
        """
        with allure.step("点击在租房源"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_evaluate(self):
        """
        点击我是业主-去估价
        """
        with allure.step("点击我是业主-去估价"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_wechat(self):
        """
        点击复制微信号
        """
        with allure.step("点击复制微信号"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_qq(self):
        """
        点击复制qq号
        """
        with allure.step("点击复制qq号"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_base_more(self):
        """
        点击基础信息-查看更多
        """
        with allure.step("点击基础信息-查看更多"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_bmap(self):
        """
        点击周边配套-地图
        """
        with allure.step("点击周边配套-地图"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_layout(self):
        """
        点击小区户型第一个户型
        """
        with allure.step("点击小区户型第一个户型"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_layout_more(self):
        """
        点击小区户型-查看更多
        """
        with allure.step("点击小区户型-查看更多"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_block_more(self):
        """
        点击小区解读-查看更多
        """
        with allure.step("点击小区解读-查看更多"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_block_ask(self):
        """
        点击小区解读-在线咨询
        """
        with allure.step("点击小区解读-在线咨询"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_iv_im(self):
        """
        点击小区专家-im
        """
        with allure.step("点击小区专家-im"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_iv_call(self):
        """
        点击小区专家-电话
        """
        with allure.step("点击小区专家-电话"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_blockexpert(self):
        """
        点击小区专家第一个小区专家
        """
        with allure.step("点击小区专家第一个小区专家"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_sell_house(self):
        """
        点击在售房源第一个房源
        """
        with allure.step("点击在售房源第一个房源"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_sell_more(self):
        """
        点击在售房源-同小区在售房源
        """
        with allure.step("点击在售房源-同小区在售房源"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_near_block(self):
        """
        点击周边小区-第一个小区
        """
        with allure.step("点击周边小区-第一个小区"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_find_house(self):
        """
        点击马上找房入口
        """
        with allure.step("点击马上找房入口"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_broker(self):
        """
        点击底部经纪人信息
        """
        with allure.step("点击底部经纪人信息"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_tv_ask(self):
        """
        点击底部在线咨询按钮
        """
        with allure.step("点击底部在线咨询按钮"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def click_community_detail_tv_call(self):
        """
        点击底部拨打电话按钮
        """
        with allure.step("点击底部拨打电话按钮"):
            self.steps("../../page_object/community/communitydetail.yaml")
        self.tsleep(1)
        return self

    def fun_para(self,text=None):
        self._params["para"] = text
        with allure.step("点击"+self._params["para"]):
            self.steps("../../page_object/community/communitydetail.yaml", replace=True)
        self.tsleep(1)
        return self

    def fun_swipe(self,pos_text=None):
        self._params["pos_text"] = pos_text
        with allure.step("滑动到" + self._params["pos_text"]):
            self.steps("../../page_object/community/communitydetail.yaml", replace=True)
        self.tsleep(1)
        return self
