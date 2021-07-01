#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#写字楼详情页

import allure

from page_object.base_page.base_page import BasePage

class OfficeBuildingDetail(BasePage):
    """
    写字楼详情页
    """

    def officebuilding_swipe(self, pos_text=None):
        """
        滑动到pos_text的位置，滑动
        :param pos_text: 1、写入页面存在的元素
                         2、如果写pos_text=buttom，则滑动到页面底部
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step("滑动到" + self._params["pos_text"]):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml", replace=True)
        self.tsleep(1)
        return self

    def click_officebuilding_detail_share(self):
        """
        点击分享
        """
        with allure.step("点击分享"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_collect(self):
        """
        点击收藏
        """
        with allure.step("点击收藏"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_msg(self):
        """
        点击消息
        """
        with allure.step("点击消息"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_pic(self):
        """
        点击图片
        """
        with allure.step("点击图片"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_price_im(self):
        """
        点击租金旁的im咨询入口
        """
        with allure.step("点击租金旁的im咨询入口"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_location(self):
        """
        小地图按钮
        """
        with allure.step("点击小地图按钮"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_info_im(self):
        """
        房源概况-预约看房
        """
        with allure.step("点击房源概况-预约看房"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_iv_call(self):
        """
        房源描述-电话
        """
        with allure.step("点击房源描述-电话"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_iv_im(self):
        """
        点击房源描述-im咨询
        """
        with allure.step("点击房源描述-im咨询"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_tv_more(self):
        """
        房源描述-展开
        """
        with allure.step("点击房源描述-展开"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_go_detail(self):
        """
        所属楼盘-查看详情
        """
        with allure.step("点击所属楼盘-查看详情"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_map(self):
        """
        大地图
        """
        with allure.step("点击大地图"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_tv_im(self):
        """
        地铁-咨询详情
        """
        with allure.step("点击地铁-咨询详情"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_tv_control(self):
        """
        地铁-共X条路线
        """
        with allure.step("点击地铁-共X条路线"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_complaint(self):
        """
        点击举报
        """
        with allure.step("点击举报"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_list_more(self):
        """
        点击附近写字楼-查看全部
        """
        with allure.step("点击附近写字楼-查看全部"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_list_house(self):
        """
        点击附近写字楼-第一个楼盘
        """
        with allure.step("点击附近写字楼-第一个楼盘"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_arrow(self):
        """
        点击悬浮-提问
        """
        with allure.step("点击悬浮-提问"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_btn_call(self):
        """
       点击底部-电话咨询
        """
        with allure.step("点击底部-电话咨询"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_btn_im(self):
        """
        点击底部-在线咨询
        """
        with allure.step("点击底部-在线咨询"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self

    def click_officebuilding_detail_btn_person(self):
        """
        点击底部经纪人信息
        """
        with allure.step("点击底部经纪人信息"):
            self.steps("../../page_object/renthouse/officebuildingdetail.yaml")
        self.tsleep(1)
        return self


















