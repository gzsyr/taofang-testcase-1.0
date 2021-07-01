#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import allure

from page_object.base_page.base_page import BasePage

class BrandApartmentDetail(BasePage):

    def fun_swipe(self, pos_text=None):
        """
        滑动到pos_text的位置，滑动
        :param pos_text: 1、写入页面存在的元素
                         2、如果写pos_text=buttom，则滑动到页面底部
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step("滑动到" + self._params["pos_text"]):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml", replace=True)
        self.tsleep(1)
        return self

    def click_brandapartment_detail_collection(self):
        """
        点击收藏
        """
        with allure.step("点击收藏"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_brandapartment_detail_share(self):
        """
        点击分享
        """
        with allure.step("点击分享"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_brandapartment_detail_pic(self):
        """
        点击房源图片
        """
        with allure.step("点击房源图片"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_brandapartment_detail_price_im(self):
        """
        点击租金傍边的im入口
        """
        with allure.step("点击租金傍边的im入口"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_brandapartment_detail_complaint(self):
        """
        点击投诉举报
        """
        with allure.step("点击投诉举报"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_brandapartment_detail_map(self):
        """
        点击地图
        """
        with allure.step("点击地图"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_brandapartment_detail_tv_im(self):
        """
        点击房源描述-咨询详情
        """
        with allure.step("点击房源描述-咨询详情"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_brandapartment_detail_zuboshi(self):
        """
        点击找不到合适的房源？365租房顾问帮你忙！
        """
        with allure.step("点击找不到合适的房源？365租房顾问帮你忙！"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_brandapartment_detail_brandname(self):
        """
        点击品牌公寓
        """
        with allure.step("点击品牌公寓"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_brandapartment_detail_arrow(self):
        """
        悬浮提问
        """
        with allure.step("点击悬浮提问"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_brandapartment_detail_btn_call(self):
        """
        点击联系电话
        """
        with allure.step("点击联系电话"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

    def click_brandapartment_detail_btn_im(self):
        """
        点击预约看房
        """
        with allure.step("点击预约看房"):
            self.steps("../../page_object/renthouse/brandapartmentdetail.yaml")
        self.tsleep(1)
        return self

