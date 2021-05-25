import allure

from page_object.newhouse.newhousedetail import NewHouseDetail
from test_case.base_test.test_base import TestBase


class TestNewHouseList(TestBase):
    """
    新房列表页面的所有用例
    """

    @allure.description("点击第一个楼盘")
    def test_goto_newhouse_detail(self):
        """
        点击列表项第一个楼盘，进入详情页面
        :return:
        """
        self.shouye.goto_func_entrance_newhouse().goto_newhouse_detail().screenshot()

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
    def test_click_position_region_km(self):
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
    def test_click_position_region_metro(self):
        """
        点击筛选项：位置->地铁->1号线->迈皋桥站
        :return:
        """
        a = self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_position(). \
            click_filter_position_menu("地铁"). \
            click_filter_position_menu("一号线"). \
            click_filter_position_menu("迈皋桥站")
        a.screenshot()
        a.click_filter_position().screenshot()

    @allure.description("点击筛选项下方的“综合排序”")
    def test_final_priorities(self):
        """
        点击筛选项下方的“综合排序”
        :return:
        """
        self.shouye.goto_func_entrance_newhouse().click_final_priorities().screenshot()

    @allure.description("点击筛选项下方的“价格”")
    def test_click_price(self):
        """
        点击筛选项下方的“价格”
        :return:
        """
        self.shouye.goto_func_entrance_newhouse().click_price().screenshot()

    @allure.description("点击筛选项下方的“开盘时间”")
    def test_click_open_time(self):
        """
        点击筛选项下方的“开盘时间”
        :return:
        """
        self.shouye.goto_func_entrance_newhouse().click_opening_time().screenshot()

    @allure.description("点击筛选项下方的“关注度”")
    def test_click_attention_rate(self):
        """
        点击筛选项下方的“关注度”
        :return:
        """
        self.shouye.goto_func_entrance_newhouse().click_attention_rate().screenshot()