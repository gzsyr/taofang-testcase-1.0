#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import allure
import pytest
from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 看房团页面的测试")
class Test_HouseTour(TestBase):

    def goto_kft(self):
        return self.shouye.goto_func_entrance_first("看房团")

    @allure.description("点击活动流程按钮")
    def test_click_housetour_rightbtn(self):
        self.goto_kft().click_housetour_rightbtn().screenshot()

    @allure.description("点击全部路线右侧的向下箭头")
    def test_click_housetour_linebtn(self):
        self.goto_kft().click_housetour_linebtn().screenshot()

    @allure.description("点击第一条具体线路")
    def test_click_housetour_line(self):
        self.goto_kft().click_housetour_linebtn().fun_line().screenshot()

    @allure.description("点击看房团路线，进入详情页")
    def test_click_housetour_kft_title(self):
        self.goto_kft().click_housetour_kft_title().screenshot()

    @allure.description("点击看房团路线-电话咨询按钮")
    def test_click_housetour_call(self):
        self.goto_kft().click_housetour_call().screenshot()

    @allure.description("点击看房团路线-我要报名按钮")
    def test_click_housetour_sighup(self):
        self.goto_kft().click_housetour_sighup().screenshot()

    @allure.description("点击底部-填写看房需求按钮")
    def test_click_housetour_sign_req(self):
        self.goto_kft().click_housetour_sign_req().screenshot()







