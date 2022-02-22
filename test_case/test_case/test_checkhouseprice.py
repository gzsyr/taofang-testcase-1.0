# -- by yfl
import allure

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 查房价页面的测试")
class TestCheckHousePrice(TestBase):
    """
    查房价首页测试用例
    """
    def goto_check_house_price(self):
        return self.shouye.func_entrance_swipe_left("签到").goto_func_entrance_check_price()

    @allure.description("点击搜索框")
    def test_click_search_house(self):
        self.goto_check_house_price().click_search_house().screenshot()

    @allure.description("快速评估输入小区：万科金色半山")
    def test_send_house(self):
        self.goto_check_house_price().select_house("万科金色半山").screenshot()

    @allure.description("快速评估输入面积：112")
    def test_send_price(self):
        self.goto_check_house_price().send_area("112").screenshot()

    @allure.description("输入小区和面积，快速评估房价")
    def test_quick_check_price(self):
        self.goto_check_house_price().quick_check_house_price().screenshot()

    @allure.description("查看附近房价")
    def test_check_neaby_price(self):
        self.goto_check_house_price().check_nearby_price().screenshot()

    @allure.description("点击查看房价地图")
    def test_goto_price_map(self):
        self.goto_check_house_price().click_house_price_map().screenshot()

    @allure.description("点击查看区属房价：鼓楼区")
    def test_check_district_price(self):
        self.goto_check_house_price().goto_district_house_price().screenshot()

    @allure.description("点击我的评估记录-更多")
    def test_more_record(self):
        self.goto_check_house_price().func_swipe().click_more_record().screenshot()

    @allure.description("点击我的评估记录-查看评估结果")
    def test_record_result(self):
        self.goto_check_house_price().func_swipe().view_record_result().screenshot()

    @allure.description("点击我的评估记录-查看小区详情")
    def test_view_record_house(self):
        self.goto_check_house_price().func_swipe().view_record_house().screenshot()

    @allure.description("点击我的评估记录-专家评估")
    def test_expert_evaluation(self):
        self.goto_check_house_price().func_swipe().view_record_expert_evaluation().screenshot()

    @allure.description("点击底部悬浮，跳转输入房屋信息页面")
    def test_goto_write_house_information(self):
        self.goto_check_house_price().goto_write_house_information().screenshot()
