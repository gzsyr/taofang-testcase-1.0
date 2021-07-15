#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#发布租房首页
import allure
from page_object.base_page.base_page import BasePage
from page_object.renthouse.publishrental import PublishRental


class PublishRentalIndex(BasePage):
    """
    发布出租首页，目前仅住宅
    """

    def click_publishrentindex_type(self,text="住宅"):
        """
        租房发布页面，选择类型
        """
        self._params["tv_type"] = text
        with allure.step("选择" + self._params["tv_type"]):
            self.steps("../../page_object/renthouse/publishrentalindex.yaml", replace=True)
        self.tsleep(1)
        if "找室友" == self._params["tv_type"]:
            return self   #后期有找室友发布页面这边再改成找室友发布页面
        else:
            return PublishRental(self._driver)

    def click_publishrentindex_authentication(self):
        """
        立即认证
        """
        with allure.step("立即认证"):
            self.steps("../../page_object/renthouse/publishrentalindex.yaml")
        self.tsleep(1)
        return self

    def click_publishrentindex_rules(self):
        """
        点击发布规则
        """
        with allure.step("点击发布规则"):
            self.steps("../../page_object/renthouse/publishrentalindex.yaml")
        self.tsleep(1)
        return self

    def click_publishrentindex_know(self):
        """
        点击发布规则-“我知道了”按钮
        """
        with allure.step("点击发布规则-“我知道了”按钮"):
            self.steps("../../page_object/renthouse/publishrentalindex.yaml")
        self.tsleep(1)
        return self

    def click_publishrentindex_agreement(self):
        """
        发布页面，点击我已阅读并同意勾选框
        """
        with allure.step("发布页面，点击我已阅读并同意勾选框"):
            self.steps("../../page_object/renthouse/publishrentalindex.yaml")
        self.tsleep(1)
        return self

    def click_publishrentindex_publish(self):
        """
        发布页面，点击立即发布
        """
        with allure.step("发布页面，点击立即发布"):
            self.steps("../../page_object/renthouse/publishrentalindex.yaml")
        self.tsleep(1)
        return self


