#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import allure
from page_object.base_page.base_page import BasePage
from page_object.community.communitydetail import CommunityDetail


class CommunityList(BasePage):
    """
    找小区列表
    """

    def click_community_search(self):
        """
        点击小区搜索框
        """
        with allure.step("点击小区搜索框"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def click_community_map(self):
        """
        点击小区搜索框旁的地图按钮
        """
        with allure.step("点击小区搜索框旁的地图按钮"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def click_community_msg(self):
        """
        点击小区搜索框旁的消息按钮
        """
        with allure.step("点击小区搜索框旁的消息按钮"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def click_community_location(self):
        """
        点击筛选项-位置
        """
        with allure.step("点击筛选项-位置"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def click_community_price(self):
        """
        点击筛选项-均价
        """
        with allure.step("点击筛选项-均价"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def click_community_room_age(self):
        """
        点击筛选项-房龄
        """
        with allure.step("点击筛选项-房龄"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def click_community_more(self):
        """
        点击筛选项-更多
        """
        with allure.step("点击筛选项-更多"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def click_community_sort(self):
        """
        点击筛选项-排序
        """
        with allure.step("点击筛选项-排序"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def click_community_delete(self):
        """
        点击清空按钮
        """
        with allure.step("点击清空按钮"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def go_community_detail(self):
        """
        点击小区列表第一个小区
        """
        with allure.step("点击小区列表第一个小区"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return CommunityDetail(self._driver)

    def click_community_im(self):
        """
        点击小区列表第一个小区旁的im入口
        """
        with allure.step("点击小区列表第一个小区旁的im入口"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def fun_para(self,text = None):
        """
        点击输入的参数
        """
        self._params["para"] =text
        with allure.step("点击" + self._params["para"] ):
            self.steps("../../page_object/community/communitylist.yaml", replace=True)
        self.tsleep(1)
        return self

    def click_community_lowest_price(self):
        """
        筛选-均价-自定义：最低价
        """
        with allure.step("筛选-均价-自定义：最低价，输入：10000"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def click_community_highest_price(self):
        """
        筛选-均价-自定义：最高价
        """
        with allure.step("筛选-均价-自定义：最高价，输入：50000"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self

    def click_community_confirm(self):
        """
        点击确定按钮
        """
        with allure.step("点击确定按钮"):
            self.steps("../../page_object/community/communitylist.yaml")
        self.tsleep(1)
        return self



