#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import allure
from page_object.base_page.base_page import BasePage

class PublishRentalPic(BasePage):

    def click_publishrentalpic_picadd(self):
        """
        图片或者视频-添加图片按钮
        """
        with allure.step("图片或者视频-添加图片按钮"):
            self.steps("../../page_object/renthouse/publishrentalpic.yaml")
        self.tsleep(1)
        return self

    def click_publishrentalpic_vedio(self):
        """
        图片或者视频-添加视频
        """
        with allure.step("图片或者视频-添加视频"):
            self.steps("../../page_object/renthouse/publishrentalpic.yaml")
        self.tsleep(1)
        return self

    def fun_para(self,text="None"):
        """
        填写参数
        """
        self._params["paramenter"] = text
        with allure.step("选择" + self._params["paramenter"]):
            self.steps("../../page_object/renthouse/publishrentalpic.yaml", replace=True)
        self.tsleep(1)
        return self

    def click_publishrentalpic_selected(self):
        """
        图片或者视频-添加图片
        """
        with allure.step("图片或者视频-添加图片"):
            self.steps("../../page_object/renthouse/publishrentalpic.yaml")
        self.tsleep(1)
        return self

    def click_publishrentalpic_hand(self):
        """
        图片或者视频-上传按钮
        """
        with allure.step("图片或者视频-上传按钮"):
            self.steps("../../page_object/renthouse/publishrentalpic.yaml")
        self.tsleep(1)
        return self

    def click_publishrentalpic_back(self):
        """
        图片或者视频-添加图片页左上角返回按钮
        """
        with allure.step("图片或者视频-添加图片页左上角返回按钮"):
            self.steps("../../page_object/renthouse/publishrentalpic.yaml")
        self.tsleep(1)
        return self

    def click_publishrentalpic_complete(self):
        """
        图片或者视频-完成按钮
        """
        with allure.step("图片或者视频-完成按钮"):
            self.steps("../../page_object/renthouse/publishrentalpic.yaml")
        self.tsleep(1)
        return self

    def click_publishrentalpic_noneed(self):
        """
        图片或者视频-不需要
        """
        with allure.step("图片或者视频-不需要"):
            self.steps("../../page_object/renthouse/publishrentalpic.yaml")
        self.tsleep(1)
        return self

    def click_publishrentalpic_upload(self):
        """
        图片或者视频-再传几张
        """
        with allure.step("图片或者视频-再传几张"):
            self.steps("../../page_object/renthouse/publishrentalpic.yaml")
        self.tsleep(1)
        return self





