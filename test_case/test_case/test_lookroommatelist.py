import allure

from test_case.base_test.test_base import TestBase

class TestLookRoommateList(TestBase):
    """
    新房列表页面的所有用例
    """
    @allure.description("找室友列表点击我的找室友入口")
    def test_lookroom_mine(self):
        """
        找室友列表点击我的找室友入口
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_function_entrance("找室友").lookroom_mine().screenshot()

    @allure.description("找室友列表点击消息")
    def test_lookroom_news(self):
        """
        找室友列表点击消息
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_function_entrance("找室友").lookroom_news().screenshot()

    @allure.description("找室友列表点击消息")
    def test_click_filter_position_region(self):
        """
        找室友列表点击全南京-区域-鼓楼区-确定按钮
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_function_entrance("找室友"). \
            click_filter_position(). \
            click_filter_position_menu("区域"). \
            click_filter_position_menu("鼓楼区").\
            screenshot()

