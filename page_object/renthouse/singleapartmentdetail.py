#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import allure

from page_object.base_page.base_page import BasePage

class SingleApartmentDetail(BasePage):
    """
    独栋公寓详情页
    """
    def fun_swipe(self, pos_text=None):
        """
        滑动到pos_text的位置，滑动
        :param pos_text: 1、写入页面存在的元素
                         2、如果写pos_text=buttom，则滑动到页面底部
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step("滑动到" + self._params["pos_text"]):
            self.steps("../../page_object/renthouse/singleapartmentdetail.yaml", replace=True)
        self.tsleep(1)
        return self

    def click_singleapartment_detail_pic(self):
        """
        点击房源图片
        """
        with allure.step("点击房源图片"):
            self.steps("../../page_object/renthouse/singleapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_singleapartment_detail_house(self):
        """
        点击在租房型-第一个房型
        """
        with allure.step("点击在租房型-第一个房型"):
            self.steps("../../page_object/renthouse/singleapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_singleapartment_detail_full_house(self):
        """
        点击公寓-查看全部
        """
        with allure.step("点击公寓-查看全部"):
            self.steps("../../page_object/renthouse/singleapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_singleapartment_detail_location(self):
        """
        点击公寓位置右侧的“>”
        """
        with allure.step("点击公寓位置右侧的“>”"):
            self.steps("../../page_object/renthouse/singleapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_singleapartment_detail_map(self):
        """
        点击地图
        """
        with allure.step("点击地图"):
            self.steps("../../page_object/renthouse/singleapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_singleapartment_detail_contact(self):
        """
        点击联系公寓
        """
        with allure.step("点击联系公寓"):
            self.steps("../../page_object/renthouse/singleapartmentdetail.yaml")
        self.tsleep(1)
        return self


