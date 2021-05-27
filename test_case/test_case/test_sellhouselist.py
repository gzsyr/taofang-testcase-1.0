import allure
from test_case.base_test.test_base import TestBase


class TestSellHouseList(TestBase):
    """
    二手房列表页面的所有用例
    """

    @allure.description("点击搜素框")
    def test_click_search_text(self):
        """
        点击列表搜素框
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_search_text().screenshot()

    @allure.description("点击地图")
    def test_click_map(self):
        """
        点击列表地图
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_map().screenshot()

    @allure.description("点击消息")
    def test_click_msg(self):
        """
        点击列表消息
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_msg().screenshot()

    @allure.description("点击列表功能入口-找小区")
    def test_click_neighborhood(self):
        """
        点击列表功能入口-找小区
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_neighborhood().screenshot()

    @allure.description("点击二手房列表页第一个房源")
    def test_goto_sellhouse_detail(self):
        """
        点击二手房列表页第一个房源进入详情页
        """
        self.shouye.goto_func_entrance_esf().goto_sellhouse_detail().screenshot()

    @allure.description("点击二手房列表标签筛选——写字楼")
    def test_click_office_buildings(self):
        """
        点击二手房列表标签筛选——写字楼
        """
        self.shouye.goto_func_entrance_esf().click_office_buildings().screenshot()

    @allure.description("点击二手房列表标签筛选——个人")
    def test_click_personal(self):
        """
        点击二手房列表标签筛选——个人
        """
        self.shouye.goto_func_entrance_esf().click_personal().screenshot()

    @allure.description("点击二手房列表标签筛选——中介")
    def test_click_mediation(self):
        """
        点击二手房列表标签筛选——中介
        """
        self.shouye.goto_func_entrance_esf().click_mediation().screenshot()

    @allure.description("点击二手房列表标签筛选——VR带看")
    def test_click_vr_see(self):
        """
        点击二手房列表标签筛选——VR带看
        """
        self.shouye.goto_func_entrance_esf().click_vr_see().screenshot()

    @allure.description("点击二手房列表标签筛选——南北通透")
    def test_click_north(self):
        """
        点击二手房列表标签筛选——南北通透
        """
        self.shouye.goto_func_entrance_esf().click_north().screenshot()

    @allure.description("点击二手房列表筛选-房型-二室/三室")
    def test_click_filter_room_menu(self):
        """
        点击二手房列表筛选-房型-二室/三室
        """
        self.shouye.\
            goto_func_entrance_esf().\
            click_filter_room(). \
            click_filter_position_menu("二室").\
            click_filter_position_menu("三室").\
            click_filter_confirm().\
            screenshot()

    @allure.description("二手房-筛选：排序-总价从低到高")
    def test_click_filter_sort(self):
        """
        二手房-筛选：排序-总价从低到高
        """
        self.shouye.\
            goto_func_entrance_esf().\
            click_filter_sort(). \
            click_filter_position_menu("总价从低到高").\
            screenshot()

    @allure.description("点击列表功能入口-个人房源")
    def test_click_personal_housing(self):
        """
        点击列表功能入口-个人房源
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_personal_housing().screenshot()

    @allure.description("点击列表功能入口-学校地图")
    def test_click_school_map(self):
        """
        点击列表功能入口-学校地图
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_school_map().screenshot()

    @allure.description("点击列表功能入口-查房价")
    def test_click_check_prices(self):
        """
        点击列表功能入口-查房价
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_check_prices().screenshot()

    @allure.description("点击列表功能入口-我要买房")
    def test_click_buy_house(self):
        """
        点击列表功能入口-我要买房
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_buy_house().screenshot()

    @allure.description("点击列表-帮你找房icon")
    def test_click_find_room(self):
        """
        点击列表-帮你找房icon
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_find_room().screenshot()

    @allure.description("点击列表-快速卖房ICON")
    def test_click_fast_selling(self):
        """
        点击列表-快速卖房ICON
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_fast_selling().screenshot()

    @allure.description("点击列表-买房咨询师ICON")
    def test_click_consultant(self):
        """
        点击列表-买房咨询师ICON
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_consultant().screenshot()

    @allure.description("点击列表-楼市头条")
    def test_click_headlines(self):
        """
        点击列表-楼市头条
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_headlines().screenshot()

    @allure.description("点击筛选项：位置-附近-1km")
    def test_click_screening_location_kilo(self):
        """
        点击筛选项：位置-附近-1km
        :return:
        """
        self.shouye. \
            goto_func_entrance_esf(). \
            click_screening_location(). \
            click_filter_position_menu("附近"). \
            click_filter_position_menu("1km"). \
            screenshot()

    @allure.description("点击筛选项：位置-附近")
    def test_click_screening_location_near(self):
        """
        点击筛选项：位置-附近
        :return:
        """
        self.shouye. \
            goto_func_entrance_esf(). \
            click_screening_location(). \
            click_filter_position_menu("附近"). \
            screenshot()

    @allure.description("点击筛选项：位置-附近")
    def test_click_screening_location_area(self):
        """
        点击筛选项：位置-区域
        :return:
        """
        self.shouye. \
            goto_func_entrance_esf(). \
            click_screening_location(). \
            click_filter_position_menu("区域"). \
            click_filter_position_menu("建邺区"). \
            screenshot()



    @allure.description("二手房-筛选：总价-200-250万")
    def test_click_filter_price(self):
        """
        二手房-筛选：总价-200-250万
        """
        self.shouye.\
            goto_func_entrance_esf().click_empty().\
            click_filter_price().\
            click_filter_position_menu("200-250万").\
            screenshot()

    @allure.description("二手房-筛选：总价-自定义，150-280万，确定")
    def test_click_filter_price_customize(self):
        """
        二手房-筛选：总价-自定义，150-280万，确定
        """
        self.shouye.goto_func_entrance_esf().\
            click_empty().click_filter_price().\
            click_filter_lowest_price("150").\
            click_filter_highest_price("280").\
            click_filter_confirm().\
            screenshot()


    @allure.description("1、二手房-筛选：位置-附近-1km 2、点击清空按钮")
    def test_click_empty(self):
        """
        1、二手房-筛选：位置-附近-1km
        2、点击清空按钮
        """
        self.shouye. \
            goto_func_entrance_esf().click_empty(). \
            click_screening_location(). \
            click_filter_position_menu("附近"). \
            click_filter_position_menu("1km").screenshot().\
            click_empty().screenshot()


    @allure.description("二手房-筛选：更多-个人、住宅、80-100m、简装、1995年后、2-5层、南、无个税、VR看房、产权房，确定")
    def test_click_filter_more(self):
        """
        二手房-筛选：更多-个人、住宅、80-100m、简装、1995年后、2-5层、南、无个税、VR看房、产权房，确定
        """
        self.shouye.goto_func_entrance_esf().click_empty().click_filter_more().\
            click_filter_position_menu("个人").click_filter_position_menu("住宅").\
            click_filter_position_menu("80-100㎡").click_filter_position_menu("简装").screenshot().\
            swipe_to_buttom("使用权房").screenshot(). \
            click_filter_position_menu("1995年后").click_filter_position_menu("2-5层"). \
            click_filter_position_menu("南").click_filter_position_menu("无个税"). \
            click_filter_position_menu("VR看房").click_filter_position_menu("产权房").screenshot().\
            click_filter_confirm().screenshot()











