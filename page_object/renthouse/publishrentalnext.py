#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import allure
from page_object.base_page.base_page import BasePage

class PublishRentalNext(BasePage):
    """
    租房发布第二页
    """

    def fun_nextpara(self, text="None"):
        """
        填写参数
        """
        self._params["parameter"] = text
        with allure.step("选择" + self._params["parameter"]):
            self.steps("../../page_object/renthouse/publishrentalnext.yaml", replace=True)
        self.tsleep(1)
        return self


    def click_publishrentalnext_viewing_time(self):
        """
        点击看房时间
        """
        with allure.step("点击看房时间"):
            self.steps("../../page_object/renthouse/publishrentalnext.yaml")
        self.tsleep(1)
        return self

    def click_publishrentalnext_settlement_time(self):
        """
        点击入驻时间
        """
        with allure.step("点击入驻时间 "):
            self.steps("../../page_object/renthouse/publishrentalnext.yaml")
        self.tsleep(1)
        return self

    def click_publishrentalnext_title(self,text = None):
        """
        点击房源标题
        """
        self._params["title"] = text
        with allure.step("点击房源标题 " + self._params["title"] ):
            self.steps("../../page_object/renthouse/publishrentalnext.yaml", replace=True)
        self.tsleep(1)
        return self

    def send_publishrentalnext_description(self,text = None):
        """
        输入房源描述
        """
        self._params["description"] = text
        with allure.step("输入房源描述" + self._params["description"] ):
            self.steps("../../page_object/renthouse/publishrentalnext.yaml", replace=True)
        self.tsleep(1)
        return self

    def send_publishrentalnext_name(self,text = None):
        """
        姓名输入
        """
        self._params["name"] = text
        with allure.step("姓名输入" + self._params["name"]):
            self.steps("../../page_object/renthouse/publishrentalnext.yaml", replace=True)
        self.tsleep(1)
        return self

    def click_publishrentalnext_phone(self):
        """
        点击手机号
        """
        with allure.step("点击手机号 "):
            self.steps("../../page_object/renthouse/publishrentalnext.yaml")
        self.tsleep(1)
        return self

    def click_publishrentalnext_reset(self):
        """
        重置按钮
        """
        with allure.step("点击重置按钮"):
            self.steps("../../page_object/renthouse/publishrentalnext.yaml")
        self.tsleep(1)
        return self

    def click_publishrentalnext_publish(self):
        """
        点击确认发布
        """
        with allure.step("点击确认发布 "):
            self.steps("../../page_object/renthouse/publishrentalnext.yaml")
        self.tsleep(1)
        return self


    def click_publishrentalnext_confirm(self):
        """
        点击确定按钮
        """
        with allure.step("点击确定按钮"):
            self.steps("../../page_object/renthouse/publishrentalnext.yaml")
        self.tsleep(1)
        return self

    def func_swipe(self, pos_text=None):
        """
        滑动到pos_text的位置，滑动
        :param pos_text: 1、写入页面存在的元素
                         2、如果写pos_text=buttom，则滑动到页面底部
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step("滑动到" + self._params["pos_text"]):
            self.steps("../../page_object/renthouse/publishrentalnext.yaml", replace=True)
        self.tsleep(1)
        return self
