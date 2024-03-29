# -- by hzc
import allure
import pytest

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 二手房列表页面的测试")
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

    # 以下直接数据驱动标签筛选 by yfl
    @allure.description("点击二手房列表第一行功能入口")
    @pytest.mark.parametrize("func_entry", ["找小区", "学校地图", "查房价", "我要卖方", "我要买房"])
    def test_click_func_entry(self, func_entry):
        """
        点击二手房列表功能入口
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_func_entry(func_entry).screenshot()
    #
    # @allure.description("点击列表功能入口-找小区")
    # def test_click_neighborhood(self):
    #     """
    #     点击列表功能入口-找小区
    #     :return:
    #     """
    #     self.shouye.goto_func_entrance_esf().click_neighborhood().screenshot()

    @allure.description("点击二手房列表页第一个房源")
    def test_goto_sellhouse_detail(self):
        """
        点击二手房列表页第一个房源进入详情页
        """
        self.shouye.goto_func_entrance_esf().goto_sellhouse_detail().screenshot()

    # 以下直接数据驱动标签筛选 by zsy
    @allure.description("点击二手房列表标签筛选")
    @pytest.mark.parametrize("tips", ["VR看房", "放心看", "个人", "写字楼"])
    def test_tips_filter(self, tips):
        """
        数据驱动测试用例执行二手房列表的标签筛选
        :param tips:
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_tips_filter(tips).screenshot()

    # 由上一个用例代替以下用例 by zsy
    # @allure.description("点击二手房列表标签筛选——写字楼")
    # def test_click_office_buildings(self):
    #     """
    #     点击二手房列表标签筛选——写字楼
    #     """
    #     self.shouye.goto_func_entrance_esf().click_office_buildings().screenshot()
    #
    # @allure.description("点击二手房列表标签筛选——个人")
    # def test_click_personal(self):
    #     """
    #     点击二手房列表标签筛选——个人
    #     """
    #     self.shouye.goto_func_entrance_esf().click_personal().screenshot()
    #
    # @allure.description("点击二手房列表标签筛选——中介")
    # def test_click_mediation(self):
    #     """
    #     点击二手房列表标签筛选——中介
    #     """
    #     self.shouye.goto_func_entrance_esf().click_mediation().screenshot()
    #
    # @allure.description("点击二手房列表标签筛选——VR带看")
    # def test_click_vr_see(self):
    #     """
    #     点击二手房列表标签筛选——VR带看
    #     """
    #     self.shouye.goto_func_entrance_esf().click_vr_see().screenshot()
    #
    # @allure.description("点击二手房列表标签筛选——南北通透")
    # def test_click_north(self):
    #     """
    #     点击二手房列表标签筛选——南北通透
    #     """
    #     self.shouye.goto_func_entrance_esf().click_north().screenshot()

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

        # 以下直接数据驱动标签筛选 by yfl
    @allure.description("点击二手房列表第二行功能入口")
    @pytest.mark.parametrize("func_entry", ["个人房源", "写字楼", "商铺", "别墅", "楼市头条"])
    def test_click_func_entry_second(self, func_entry):
        """
        点击二手房列表功能入口
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_func_entry(func_entry).screenshot()

    # @allure.description("点击列表功能入口-个人房源")
    # def test_click_personal_housing(self):
    #     """
    #     点击列表功能入口-个人房源
    #     :return:
    #     """
    #     self.shouye.goto_func_entrance_esf().click_personal_housing().screenshot()
    #
    # @allure.description("点击列表功能入口-学校地图")
    # def test_click_school_map(self):
    #     """
    #     点击列表功能入口-学校地图
    #     :return:
    #     """
    #     self.shouye.goto_func_entrance_esf().click_school_map().screenshot()
    #
    # @allure.description("点击列表功能入口-查房价")
    # def test_click_check_prices(self):
    #     """
    #     点击列表功能入口-查房价
    #     :return:
    #     """
    #     self.shouye.goto_func_entrance_esf().click_check_prices().screenshot()
    #
    # @allure.description("点击列表功能入口-我要买房")
    # def test_click_buy_house(self):
    #     """
    #     点击列表功能入口-我要买房
    #     :return:
    #     """
    #     self.shouye.goto_func_entrance_esf().click_buy_house().screenshot()

    # @allure.description("点击列表-帮你找房icon")
    # def test_click_find_room(self):
    #     """
    #     点击列表-帮你找房icon
    #     :return:
    #     """
    #     self.shouye.goto_func_entrance_esf().click_find_room().screenshot()
    #
    # @allure.description("点击列表-快速卖房ICON")
    # def test_click_fast_selling(self):
    #     """
    #     点击列表-快速卖房ICON
    #     :return:
    #     """
    #     self.shouye.goto_func_entrance_esf().click_fast_selling().screenshot()
    #
    # @allure.description("点击列表-买房咨询师ICON")
    # def test_click_consultant(self):
    #     """
    #     点击列表-买房咨询师ICON
    #     :return:
    #     """
    #     self.shouye.goto_func_entrance_esf().click_consultant().screenshot()
    #
    # @allure.description("点击列表-楼市头条")
    # def test_click_headlines(self):
    #     """
    #     点击列表-楼市头条
    #     :return:
    #     """
    #     self.shouye.goto_func_entrance_esf().click_headlines().screenshot()

    @allure.description("点击列表-房源H5推荐")
    def test_click_recom_house(self):
        """
        点击列表-房源推荐
        :return:
        """
        self.shouye.goto_func_entrance_esf().click_recom_house().screenshot()

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

    @allure.description("点击二手房-筛选：位置-区域-建邺区")
    def test_click_screening_location_area(self):
        """
        点击筛选项：位置-区域-建邺区
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
            goto_func_entrance_esf().\
            click_filter_price().\
            click_filter_position_menu("200-250万").\
            screenshot()

    @allure.description("二手房-筛选：总价-自定义，150-280万，确定")
    def test_click_filter_price_customize(self):
        """
        二手房-筛选：总价-自定义，150-280万，确定
        """
        step = self.shouye.goto_func_entrance_esf().\
            click_filter_price().\
            click_filter_lowest_price("150").\
            click_filter_highest_price("280")
        step.screenshot()
        step.click_filter_confirm().screenshot()

    @allure.description("二手房-筛选：更多-个人、住宅、80-100m、简装、1995年后、2-5层、南、无个税、VR看房、产权房，确定")
    def test_click_filter_more(self):
        """
        二手房-筛选：更多-个人、住宅、80-100m、简装、1995年后、2-5层、南、无个税、VR看房、产权房，确定
        """
        step1 = self.shouye.goto_func_entrance_esf().click_filter_more().\
            click_filter_position_menu("个人").click_filter_position_menu("住宅").\
            click_filter_position_menu("80-100㎡").click_filter_position_menu("简装")
        step1.screenshot()
        step2 = step1.swipe_to_buttom("朝向")
        step2.screenshot()
        step3 = step2.click_filter_position_menu("1995年后").click_filter_position_menu("2-5层"). \
            click_filter_position_menu("南")
        step3.screenshot()
        step4 = step3.swipe_to_buttom("使用权房").click_filter_position_menu("无个税"). \
            click_filter_position_menu("VR看房").click_filter_position_menu("产权房")
        step4.screenshot()
        step4.click_filter_confirm().screenshot()

    @allure.description("点击二手房-筛选：位置-地铁-1号线-迈皋桥站")
    def test_click_screening_location_station(self):
        """
        点击二手房-筛选：位置-地铁-1号线-迈皋桥站
        """
        self.shouye. \
            goto_func_entrance_esf().click_empty(). \
            click_screening_location().\
            click_filter_position_menu("地铁").\
            click_filter_position_menu("1号线"). \
            click_filter_position_menu("迈皋桥站").\
            screenshot()

    @allure.description("点击二手房-筛选：位置-学校-鼓楼区-拉萨路小学")
    def test_click_screening_location_school(self):
        """
        点击二手房-筛选：位置-学校-鼓楼区-拉萨路小学
        """
        self.shouye.\
            goto_func_entrance_esf().click_empty().\
            click_screening_location().\
            click_filter_position_menu("学校").\
            click_filter_position_menu("鼓楼区").\
            click_filter_position_menu("拉萨路小学").\
            screenshot()

    # 直接點擊清空按鈕
    @allure.description("点击清空按钮")
    def test_click_empty(self):
        """
        1、点击清空按钮
        """
        step = self.shouye. \
            goto_func_entrance_esf().click_empty().screenshot()
