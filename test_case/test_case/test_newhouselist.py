import allure

from test_case.base_test.test_base import TestBase


class TestNewHouseList(TestBase):
    """
    新房列表页面的所有用例
    """

    @allure.description("点击筛选项：位置->区域")
    def test_click_position_region(self):
        """
        点击筛选项：位置-区域
        :return:
        """
        self.shouye.\
            goto_func_entrance_newhouse().\
            click_filter_position().\
            click_filter_position_menu("区域").\
            screenshot()

    @allure.description("点击筛选项：位置->区域->建邺区")
    def test_click_position_region_area(self):
        """
        点击筛选项：位置->区域->建邺区
        :return:
        """
        self.shouye.\
            goto_func_entrance_newhouse().\
            click_filter_position().\
            click_filter_position_menu("区域").\
            click_filter_position_menu("建邺区").\
            screenshot()

    @allure.description("点击筛选项：位置->附近->1km")
    def test_click_position_region_area(self):
        """
        点击筛选项：位置->区域->建邺区
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_position(). \
            click_filter_position_menu("附近"). \
            click_filter_position_menu("1km"). \
            screenshot()

    @allure.description("点击筛选项：位置->地铁->1号线->迈皋桥站")
    def test_click_position_region_area(self):
        """
        点击筛选项：位置->地铁->1号线->迈皋桥站
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_position(). \
            click_filter_position_menu("地铁"). \
            click_filter_position_menu("一号线"). \
            click_filter_position_menu("迈皋桥站").\
            screenshot()