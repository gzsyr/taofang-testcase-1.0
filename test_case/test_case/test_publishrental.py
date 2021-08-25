#!/usr/bin/env python 
# -*- coding:utf-8 -*- by zzh

import allure

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 租房-发布出租页面的测试")
class Test_PublishRental(TestBase):
    """
    发布出租相关测试用例
    """
    def goto_rentindex(self):
        """
        进入租房发布页面
        """
        return self.shouye.goto_func_entrance_zf().rent_house_release_house()

    def goto_publishrental(self):
        """
        进入住宅发布页面
        """
        return self.goto_rentindex().click_publishrentindex_type()

    def goto_rentnext(self):
        """
        发布页面，点击下一页
        """
        return self.goto_publishrental().click_publishrental_next()



    @allure.description("进入出租发布页面，选择住宅")
    def test_click_publishrentindex_type(self):
        self.goto_rentindex().click_publishrentindex_type().screenshot()

    @allure.description("进入出租发布页面，点击发布规则")
    def test_click_publishrentindex_rules(self):
        self.goto_rentindex().click_publishrentindex_rules().screenshot()

    @allure.description("1.进入住宅出租发布页面，点击图片，进入添加图片页面；2、点击添加图片，选择相册选择，"
                        "3、选择第一张图片 ，上传，点击完成，点击弹框不需要，成功上传图片")
    def test_click_publishrental_upload(self):
        self.goto_publishrental().click_publishrental_upload().click_publishrentalpic_picadd().fun_para("相册选择").\
            click_publishrentalpic_selected().click_publishrentalpic_hand().\
            click_publishrentalpic_complete().click_publishrentalpic_noneed().screenshot()

    @allure.description("输入小区名称：测试正式小区2")
    def test_click_publishrental_blockname(self):
        self.goto_publishrental().click_publishrental_blockname().\
            send_publishrental_name_search("测试正式小区2").\
            select_publishrental_name_result().screenshot()

    @allure.description("点击户型")
    def test_click_publishrental_unittype(self):
        self.goto_publishrental().click_publishrental_unittype().screenshot()

    @allure.description("点击朝向")
    def test_click_publishrental_towards(self):
        self.goto_publishrental().click_publishrental_towards().screenshot()

    @allure.description("点击楼层")
    def test_click_publishrental_floor(self):
        self.goto_publishrental().click_publishrental_floor().screenshot()

    @allure.description("楼栋号")
    def test_click_publishrental_building_num(self):
        self.goto_publishrental().click_publishrental_building_num().screenshot()


    @allure.description("点击单元号")
    def test_click_publishrental_unit_num(self):
        self.goto_publishrental().click_publishrental_unit_num().screenshot()

    @allure.description("点击室号")
    def test_click_publishrental_room_num(self):
        self.goto_publishrental().click_publishrental_room_num().screenshot()

    @allure.description("输入面积：80")
    def test_click_publishrental_area(self):
        self.goto_publishrental().func_swipe("装修").\
            click_publishrental_area().fun_para("8").fun_para("0").\
            click_publishrental_confirm().screenshot()

    @allure.description("输入租金1000")
    def test_click_publishrental_rent(self):
        self.goto_publishrental().func_swipe("装修").click_publishrental_rent().\
            fun_para("季付").fun_para("1").fun_para("0").fun_para("0").fun_para("0").\
            click_publishrental_confirm().screenshot()

    @allure.description("点击租金包含费用，选择宽带费")
    def test_click_publishrental_rent_include(self):
        self.goto_publishrental().func_swipe("装修").click_publishrental_rent_include().fun_para("宽带费").\
            click_publishrental_confirm().screenshot()

    @allure.description("点击装修")
    def test_click_publishrental_decoratio(self):
        self.goto_publishrental().func_swipe("装修").click_publishrental_decoratio().\
            click_publishrental_confirm().screenshot()


    @allure.description("输入小区名，点击重置")
    def test_click_publishrental_reset(self):
        self.goto_publishrental().click_publishrental_blockname(). \
            send_publishrental_name_search("测试正式小区2"). \
            select_publishrental_name_result().click_publishrental_reset().screenshot()


    @allure.description("输入小区名称，户型、朝向、楼层，面积，租金，租金包含费用，装修，点击下一步")
    def test_click_publishrental_next(self):
        self.goto_publishrental().click_publishrental_reset().click_publishrental_blockname().\
            send_publishrental_name_search("测试正式小区2").\
            select_publishrental_name_result().click_publishrental_unittype().click_publishrental_confirm().\
            click_publishrental_confirm().click_publishrental_confirm().click_publishrental_confirm().\
            click_publishrental_confirm().func_swipe("装修").click_publishrental_area().fun_para("8").fun_para("0").\
            click_publishrental_confirm().click_publishrental_rent().\
            fun_para("季付").fun_para("1").fun_para("0").fun_para("0").fun_para("0").click_publishrental_confirm().\
            click_publishrental_rent_include().fun_para("宽带费").\
            click_publishrental_confirm().click_publishrental_decoratio().\
            click_publishrental_confirm().click_publishrental_next().screenshot()


    @allure.description("进入出租下一页，点击看房时间")
    def test_click_publishrentalnext_viewing_time(self):
        self.goto_rentnext().click_publishrentalnext_viewing_time().\
            click_publishrentalnext_confirm().screenshot()

    @allure.description("进入出租下一页，点击入住时间")
    def test_click_publishrentalnext_settlement_time(self):
        self.goto_rentnext().click_publishrentalnext_settlement_time(). \
            click_publishrentalnext_confirm().screenshot()

    @allure.description("进入出租下一页，点击房屋配置，选择冰箱，空调")
    def test_click_publishrentalnext_configuration(self):
        self.goto_rentnext().fun_nextpara("冰箱").fun_nextpara("空调").screenshot()

    @allure.description("进入出租下一页，房屋亮点，选择南北通透，交通便利")
    def test_click_publishrentalnext_feature(self):
        self.goto_rentnext().fun_nextpara("南北通透").fun_nextpara("交通便利").screenshot()

    @allure.description("1、进入出租发布下一页，出租要求“限女生”")
    def test_click_publishrentalnext_requestment(self):
        self.goto_rentnext().func_swipe("buttom").fun_nextpara("限女生").screenshot()

    @allure.description("1、进入出租发布下一页，滑动页面至底部，房屋描述：交通便利，环境优美")
    def test_send_publishrentalnext_description(self):
        self.goto_rentnext().func_swipe("buttom").\
            send_publishrentalnext_description("交通便利，环境优美").screenshot()

    @allure.description("进入出租发布下一页，滑动页面至底部，选择女士")
    def test_click_publishrentalnext_gender(self):
        self.goto_rentnext().func_swipe("buttom").fun_nextpara("女士").screenshot()

    @allure.description("进入出租发布下一页，滑动页面至底部，选择女士，输入姓名：张")
    def test_click_publishrentalnext_name(self):
        self.goto_rentnext().func_swipe("buttom").fun_nextpara("女士").send_publishrentalnext_name("张").screenshot()

    @allure.description("进入出租发布下一页，点击重置")
    def test_click_publishrentalnext_reset(self):
        self.goto_rentnext().click_publishrentalnext_reset().screenshot()

    @allure.description("1、进入出租发布下一页，选择看房时间、入驻时间2、选择房屋配置、房屋亮点、出租要求3、填写房屋描述，填写姓名，点击发布")
    def test_click_publishrentalnext_publish(self):
        step1 = self.goto_rentnext().click_publishrentalnext_viewing_time().click_publishrentalnext_confirm(). \
                click_publishrentalnext_confirm().click_publishrentalnext_confirm().fun_nextpara("冰箱").\
            fun_nextpara("南北通透").fun_nextpara("限女生").func_swipe("buttom").send_publishrentalnext_description("环境优美").\
            fun_nextpara("女士").send_publishrentalnext_name("张")
        step1.screenshot()
        # step1.click_publishrentalnext_publish().screenshot()




































