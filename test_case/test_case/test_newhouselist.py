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

    @allure.description("列表页点击搜索框")
    def test_click_search_text(self):
        """
        列表页点击搜索框
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_search_text(). \
            screenshot()

    @allure.description("列表页点击地图")
    def test_click_map(self):
        """
        列表页点击搜索框
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_map(). \
            screenshot()

    @allure.description("列表页点击聚合入口1")
    def test_click_layout_one(self):
        """
        列表页点击聚合入口1
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_layout_one(). \
            screenshot()

    @allure.description("列表页点击聚合入口2")
    def test_click_layout_two(self):
        """
        列表页点击聚合入口2
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_layout_two(). \
            screenshot()

    @allure.description("列表页点击聚合入口3")
    def test_click_layout_three(self):
        """
        列表页点击聚合入口3
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_layout_three(). \
            screenshot()

    @allure.description("列表页点击聚合入口4")
    def test_click_layout_four(self):
        """
        列表页点击聚合入口4
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_layout_four(). \
            screenshot()

    @allure.description("点击筛选项：位置->附近")
    def test_click_position_nearby(self):
        """
        点击筛选项：位置-区域
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_position(). \
            click_filter_position_menu("附近"). \
            screenshot()

    @allure.description("点击筛选项：位置->地铁")
    def test_click_position_metro(self):
        """
        点击筛选项：位置-地铁
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_position(). \
            click_filter_position_menu("地铁"). \
            screenshot()

    @allure.description("点击筛选项：位置->地铁->一号线")
    def test_click_position_metro_oneline(self):
        """
        点击筛选项：位置-地铁
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_position(). \
            click_filter_position_menu("地铁"). \
            click_filter_position_menu("一号线"). \
            screenshot()

    @allure.description("点击筛选项：位置->板块")
    def test_click_position_plate(self):
        """
        点击筛选项：位置-板块
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_position(). \
            click_filter_position_menu("板块"). \
            screenshot()

    @allure.description("点击筛选项：位置->板块->城中")
    def test_click_position_plate_town_traders(self):
        """
        点击筛选项：位置-板块-城中
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_position(). \
            click_filter_position_menu("板块"). \
            click_filter_position_menu("城中"). \
            screenshot()

    @allure.description("点击筛选项：价格")
    def test_click_filter_price(self):
        """
        点击筛选项：价格
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_price(). \
            screenshot()

    @allure.description("点击筛选项：价格-10000元/m以下")
    def test_click_filter_price_onekilo(self):
        """
        点击筛选项：价格-10000元/m以下
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_price(). \
            click_filter_position_menu("10000元/㎡以下"). \
            screenshot()

    @allure.description("点击筛选项：户型")
    def test_click_filter_room(self):
        """
        点击筛选项：户型
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_room(). \
            screenshot()

    @allure.description("点击筛选项：户型-二室")
    def test_click_filter_room_bilocular(self):
        """
        点击筛选项：户型-二室
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_room(). \
            click_filter_position_menu("二室"). \
            screenshot()

    @allure.description("点击删除按钮")
    def test_click_delete(self):
        """
        点击删除按钮
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_delete(). \
            screenshot()

    @allure.description("点击筛选项：位置-附近-1km，价格-25000-30000元/m，户型-三室")
    def test_click_assemble(self):
        """
        点击筛选项：位置-附近-1km，价格-25000-30000元/m，户型-三室
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_position(). \
            click_filter_position_menu("附近"). \
            click_filter_position_menu("1km"). \
            click_filter_price(). \
            click_filter_position_menu("20000-25000元/㎡"). \
            click_filter_room(). \
            click_filter_position_menu("三室"). \
            screenshot()

    @allure.description("点击筛选项：位置-附近-1km，价格-25000-30000元/m，户型-三室,点击清空按钮")
    def test_click_grouping(self):
        """
        点击筛选项：位置-附近-1km，价格-25000-30000元/m，户型-三室，点击清空按钮
        :return:
        """
        self.shouye. \
            goto_func_entrance_newhouse(). \
            click_filter_position(). \
            click_filter_position_menu("附近"). \
            click_filter_position_menu("1km"). \
            click_filter_price(). \
            click_filter_position_menu("20000-25000元/㎡"). \
            click_filter_room(). \
            click_filter_position_menu("三室"). \
            click_delete(). \
            screenshot()

    @allure.description("点击筛选项：新房-筛选：筛选-品牌房企、住宅、60-80m、本月开盘、精装修")
    def test_click_filter_screen(self):
        """
        点击筛选项：新房-筛选：筛选-品牌房企、住宅、60-80m、本月开盘、精装修
        :return:
        """
        self.shouye.\
            goto_func_entrance_newhouse(). \
            click_filter_screen(). \
            click_filter_position_menu("品牌房企"). \
            click_filter_position_menu("住宅"). \
            func_swipe("成品交付"). \
            click_filter_position_menu("300㎡以上"). \
            click_filter_position_menu("本月开盘"). \
            click_filter_position_menu("精装修"). \
            screenshot()

    def test_click_filter_screen_definite(self):
        """
        点击筛选项：新房-筛选：筛选-品牌房企、住宅、60-80m、本月开盘、精装修、确定按钮
        :return:
        """
        self.shouye.\
            goto_func_entrance_newhouse(). \
            click_filter_screen(). \
            click_filter_position_menu("品牌房企"). \
            click_filter_position_menu("住宅"). \
            func_swipe("成品交付"). \
            click_filter_position_menu("300㎡以上"). \
            click_filter_position_menu("本月开盘"). \
            click_filter_position_menu("精装修"). \
            click_definite(). \
            screenshot()

    def test_click_filter_screen_empty(self):
        """
        点击筛选项：新房-筛选：筛选-品牌房企、住宅、60-80m、本月开盘、精装修、清空按钮
        :return:
        """
        self.shouye.\
            goto_func_entrance_newhouse(). \
            click_filter_screen(). \
            click_filter_position_menu("品牌房企"). \
            click_filter_position_menu("住宅"). \
            func_swipe("成品交付"). \
            click_filter_position_menu("300㎡以上"). \
            click_filter_position_menu("本月开盘"). \
            click_filter_position_menu("精装修"). \
            click_empty(). \
            screenshot()