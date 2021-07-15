#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#租房发布的第一页
import allure
from page_object.base_page.base_page import BasePage
from page_object.renthouse.publishrentalnext import PublishRentalNext
from page_object.renthouse.publishrentalpic import PublishRentalPic
from page_object.sellhouse.publishhouse import PublishHouse


class PublishRental(BasePage):

    def fun_para(self, text="None"):
        """
        填写参数
        """
        self._params["parameter"] = text
        with allure.step("选择" + self._params["parameter"]):
            self.steps("../../page_object/renthouse/publishrental.yaml", replace=True)
        self.tsleep(1)
        return self


    def click_publishrental_upload(self):
        """
        点击图片或视频
        """
        with allure.step("点击图片或视频 "):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return PublishRentalPic(self._driver)

    def click_publishrental_blockname(self):
        """
        点击小区名称输入框
        """
        with allure.step("点击小区名称输入框"):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def send_publishrental_name_search(self, keyword="测试正式小区2"):
        """
        执行搜索
        :param keyword: 输入搜索关键词，默认“测试正式小区2”
        :return:
        """
        self._params["house_name"] = keyword
        with allure.step("输入搜索关键词: " + self._params["house_name"]):
            self.steps("../../page_object/renthouse/publishrental.yaml", replace=True)

        # self.adbshell('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
        # self.tsleep(1)
        # self._driver.press_keycode('66')  # os.system("adb shell input keyevent 66")
        # self.adbshell('adb shell ime set io.appium.settings/.UnicodeIME')
        # self.tsleep(1)
        return self

    def select_publishrental_name_result(self):
        """
        选择小区搜索结果
        :return:
        """
        with allure.step("选择小区搜索结果"):
            self.steps("../../page_object/renthouse/publishrental.yaml", replace=True)
        self.tsleep(1)
        return self

    def click_publishrental_unittype(self):
        """
        点击户型输入框
        """
        with allure.step("点击户型输入框"):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_towards(self):
        """
        点击朝向输入框
        """
        with allure.step("点击朝向输入框"):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_floor(self):
        """
        点击楼层输入框
        """
        with allure.step("点击楼层输入框 "):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_building_num(self):
        """
        点击楼栋号输入框
        """
        with allure.step("点击楼栋号输入框"):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_unit_num(self):
        """
        点击单元号输入框
        """
        with allure.step("点击单元号输入框"):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_room_num(self):
        """
        点击室号输入框
        """
        with allure.step("点击室号输入框,输入"):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_area(self):
        """
        点击面积
        """
        with allure.step("点击面积"):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_rent(self):
        """
        点击租金
        """
        with allure.step("点击租金"):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_rent_include(self):
        """
        点击租金包含费用
        """
        with allure.step("点击租金包含费用"):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self


    def click_publishrental_decoratio(self):
        """
        点击装修
        """
        with allure.step("点击装修 "):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_gender(self):
        """
        点击合租-租客性别
        """
        with allure.step("点击合租-租客性别"):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_confirm(self):
        """
        点击确定按钮
        """
        with allure.step("点击确定按钮 "):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_reset(self):
        """
        点击重置
        """
        with allure.step("点击重置 "):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return self

    def click_publishrental_next(self):
        """
        点击下一步
        """
        with allure.step("点击下一步"):
            self.steps("../../page_object/renthouse/publishrental.yaml")
        self.tsleep(1)
        return PublishRentalNext(self._driver)


    def func_swipe(self, pos_text=None):
        """
        滑动到pos_text的位置，滑动
        :param pos_text: 1、写入页面存在的元素
                         2、如果写pos_text=buttom，则滑动到页面底部
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step("滑动到" + self._params["pos_text"]):
            self.steps("../../page_object/renthouse/publishrental.yaml", replace=True)
        self.tsleep(1)
        return self








