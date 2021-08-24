import allure

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 租房列表页面的测试")
class TestRentHouseList(TestBase):
    """
    租房房源列表的所有用例
    """
    def goto_renthouselist(self):
        """
        进入房源列表页
        :return:
        """
        return self.shouye.goto_func_entrance_zf().rent_house_function_entrance("整租")

    def empty_filter_more(self):
        return self.goto_renthouselist().click_filter_more().click_empty()

    @allure.description("点击搜索框")
    def test_click_search_text(self):
        """
        点击搜索框
        """
        self.goto_renthouselist().click_renthouse_search().screenshot()

    @allure.description("租房列表页筛选：区域-鼓楼区-江东")
    def test_click_position_region(self):
        """
        租房列表页筛选：区域-鼓楼区-江东
        """
        self.goto_renthouselist().click_filter_position().click_filter_position_menu("区域").\
            click_filter_position_menu("鼓楼区").click_filter_position_menu("江东").click_definite().screenshot()

    @allure.description("租房列表页筛选：地铁-2号线-元通站")
    def test_click_position_metro(self):
        """
        租房列表页筛选：地铁-2号线-元通站
        """
        self.goto_renthouselist().click_filter_position().click_filter_position_menu("地铁"). \
            click_filter_position_menu("2号线").click_filter_position_menu("元通站").click_definite().screenshot()

    @allure.description("租房列表页筛选：租金1500-2000元")
    def test_click_filter_price(self):
        """
        租房列表页筛选：租金1500-2000元
        """
        self.goto_renthouselist().click_filter_price().click_filter_position_menu("1500-2000元").screenshot()

    @allure.description("租房列表页筛选：户型 一室")
    def test_click_filter_room(self):
        """
        租房列表页筛选：户型 一室
        """
        self.goto_renthouselist().click_filter_room().click_filter_position_menu("一室").screenshot()

    @allure.description("租房列表页筛选：更多筛选出租方式-合租")
    def test_click_filter_mode(self):
        """
        租房列表页筛选：更多筛选出租方式-合租
        """
        self.empty_filter_more().click_filter_position_menu("合租").click_definite().screenshot()

    @allure.description("租房列表页筛选：更多筛选来源-中介")
    def test_click_filter_source(self):
        """
        租房列表页筛选：更多筛选来源-中介
        """
        self.empty_filter_more().click_filter_position_menu("中介").click_definite().screenshot()

    @allure.description("租房列表页筛选：更多筛选物业类型-住宅")
    def test_click_filter_type(self):
        """
        租房列表页筛选：更多筛选物业类型-住宅
        """
        self.empty_filter_more().click_filter_position_menu("住宅").click_definite().screenshot()

    @allure.description("租房列表页筛选：更多筛选装修-精装")
    def test_click_filter_renovation(self):
        """
        租房列表页筛选：更多筛选装修-精装
        """
        self.empty_filter_more().click_filter_position_menu("精装").click_definite().screenshot()

    @allure.description("租房列表页筛选：更多筛选房源特色-视频房源")
    def test_click_filter_characteristic(self):
        """
        租房列表页筛选：更多筛选房源特色-视频房源
        """
        self.empty_filter_more().click_filter_position_menu("视频房源").click_definite().screenshot()

    @allure.description("租房列表页筛选：更多筛选 整租/中介/住宅/精装/严选")
    def test_click_filter_more(self):
        """
        租房列表页筛选：更多筛选 整租/中介/住宅/精装/严选
        """
        self.empty_filter_more().click_filter_position_menu("整租").click_filter_position_menu("中介").\
            click_filter_position_menu("住宅").click_filter_position_menu("精装").click_filter_position_menu("严选").\
            click_definite().screenshot()

    @allure.description("租房列表页排序：不限")
    def test_click_sort(self):
        """
        租房列表页排序：不限
        排序选项入参待研究
        """
        self.goto_renthouselist().click_filter_sort().click_ok().screenshot()

    @allure.description("进入整租、中介、住宅筛选的第一个房源")
    def test_goto_renthouse_detail(self):
        """
        进入整租、中介、住宅筛选的第一个房源
        """
        self.empty_filter_more().click_filter_position_menu("整租").click_filter_position_menu("中介").\
            click_filter_position_menu("住宅").click_definite().goto_renthouse_detail().screenshot()
