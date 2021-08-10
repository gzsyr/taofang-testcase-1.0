#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import allure
from page_object.base_page.base_page import BasePage

class HouseTour(BasePage):
    """
    看房团页面
    """

    def click_housetour_rightbtn(self):
        """
        点击活动流程
        """
        with allure.step("点击活动流程"):
            self.steps("../../page_object/housetour/housetour.yaml")
        self.tsleep(1)
        return self

    def click_housetour_linebtn(self):
        """
        点击全部路线右侧的向下箭头
        """
        with allure.step("点击全部路线右侧的向下箭头"):
            self.steps("../../page_object/housetour/housetour.yaml")
        self.tsleep(1)
        return self

    def fun_line(self,text = None):
        self._params["line"] = text
        with allure.step("点击"+self._params["line"]):
            self.steps("../../page_object/housetour/housetour.yaml", replace=True)
        self.tsleep(1)
        return self

    def click_housetour_kft_title(self):
        """
        点击看房团专线，进入详情页
        """
        with allure.step("点击看房团专线，进入详情页"):
            self.steps("../../page_object/housetour/housetour.yaml")
        self.tsleep(1)
        return self

    def click_housetour_call(self):
        """
        点击电话咨询
        """
        with allure.step("点击电话咨询"):
            self.steps("../../page_object/housetour/housetour.yaml")
        self.tsleep(1)
        return self

    def click_housetour_sighup(self):
        """
        点击我要报名
        """
        with allure.step("点击我要报名"):
            self.steps("../../page_object/housetour/housetour.yaml")
        self.tsleep(1)
        return self

    def click_housetour_sign_req(self):
        """
        填写看房需求
        """
        with allure.step("填写看房需求"):
            self.steps("../../page_object/housetour/housetour.yaml")
        self.tsleep(1)
        return self






