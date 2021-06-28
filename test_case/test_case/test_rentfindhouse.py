import allure

from test_case.base_test.test_base import TestBase


class TestRentFindHouse(TestBase):
    """
    我要求租页面
    """
    def goto_rentfindhouse(self):
        """
        进入我要求租页面：大首页-租房-我要求租
        """
        return self.shouye.goto_func_entrance_zf().rent_house_function_entrance("我要求租")

    @allure.description("选择房屋类型：住宅")
    def test_select_type(self):
        """
        选择房屋类型：住宅
        """
        self.goto_rentfindhouse().select_rent_tiem("住宅").screenshot()

    @allure.description("弹出意向位置选择框")
    def test_show_location(self):
        """
        弹出意向位置选择框
        """
        self.goto_rentfindhouse().show_location().screenshot()

    @allure.description("选择意向位置：建邺区-南湖-确定")
    def test_select_location(self):
        """
        我要求租-意向位置：建邺区-南湖-确定
        """
        self.goto_rentfindhouse().show_location().select_rent_location("建邺区").select_rent_location("南湖").\
            click_rent_location_confirm().screenshot()

    @allure.description("选择租房类型（住宅）：合租单间")
    def test_select_mode(self):
        """
        我要求租-租房类型（住宅）:合租单间
        """
        self.goto_rentfindhouse().select_rent_tiem("合租单间").screenshot()

    @allure.description("选择租房预算（住宅）：1000-1500元")
    def test_select_price(self):
        """
        选择租房预算：1000-1500元
        """
        self.goto_rentfindhouse().select_rent_tiem("1000-1500元").screenshot()

    @allure.description("选择入住时间（住宅）：两周以内")
    def test_select_time(self):
        """
        选择入住时间（住宅）：两周以内
        """
        self.goto_rentfindhouse().select_rent_tiem("两周以内").screenshot()

    @allure.description("我要求租:住宅 雨花台铁心桥 合租单间 1000到1500元 两周以内入住-发布")
    def test_click_rent_findhouse(self):
        """
        我要求租:住宅 雨花台铁心桥 合租单间 1000到1500元 两周以内入住-发布
        """
        step1 = self.goto_rentfindhouse().select_rent_tiem("住宅").show_location().select_rent_location("雨花台区").\
            select_rent_location("铁心桥").click_rent_location_confirm().select_rent_tiem("合租单间").\
            select_rent_tiem("1000-1500元").select_rent_tiem("两周以内")
        step1.screenshot()
        step1.click_rent_findhouse().screenshot()
