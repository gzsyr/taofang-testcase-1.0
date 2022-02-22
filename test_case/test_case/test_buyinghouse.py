# -- by zsy
import allure

from page_object.base_page.app import App
from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 我要买房页面的测试")
class TestBuyingHouse(TestBase):
    """
    我要买房页面测试用例
    """
    def setup_method(self):
        self.shouye = self.app.openapp().main().func_entrance_swipe_left("签到").func_entrance_swipe_left("查房价").goto_func_entrance_want_buy()
        if self.shouye.delete_in_page():  # 这个页面有“删除”，则先执行删除-是-开始生成
            print("该页面存在删除文字")
            self.shouye.show_buying_house_page()
            print("回到“我要买房”选项页面")
        print("我要买房：setup_method")

    def teardown_method(self):
        self.app.closeapp()
        print("我要买房：teardown_method")

    @allure.description("选择房屋类型，单选“别墅”")
    def test_select_house_type(self):
        """
        选择房屋类型，单选
        :return:
        """
        # self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_want_buy().\
        #     select_house_type(house_item="房屋类型", house_type="别墅").screenshot()
        self.shouye.select_house_type(house_item="房屋类型", house_type="别墅").screenshot()

    @allure.description("拖动预算进度条")
    def test_swipe_budget(self):
        """
        拖动预算进度条
        :return:
        """
        self.shouye.swipe_house_budget()

    @allure.description("点击展示出意向位置的菜单")
    def test_show_location(self):
        """
        展示意向位置
        :return:
        """
        # self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_want_buy().
        self.shouye.show_location().screenshot()

    @allure.description("选择意向位置“雨花台区-能仁里”")
    def test_select_area_confirm(self):
        """
        选择意向位置“雨花台区-能仁里”
        :return:
        """
        self.shouye.\
            show_location().\
            select_house_type(house_item="位置类型", house_type="城区").\
            select_house_type(house_item="区域", house_type="雨花台区").\
            select_house_type(house_item="板块", house_type="能仁里").\
            select_house_location_confirm().screenshot()

    @allure.description("选择意向位置“地铁-10号线-文德路站”")
    def test_select_metro_confirm(self):
        """
        选择意向位置“地铁-10号线-文德路站”
        :return:
        """
        self.shouye.\
            show_location().\
            select_house_type(house_item="位置类型", house_type="地铁").\
            select_house_type(house_item="地铁", house_type="10号线").\
            select_house_type(house_item="站点", house_type="文德路站").\
            select_house_location_confirm().screenshot()

    @allure.description("选择意向位置“学校-雨花台区-西善桥中心小学”")
    def test_select_school_confirm(self):
        """
        选择意向位置“学校-雨花台区-西善桥中心小学”
        :return:
        """
        self.shouye.\
            show_location().\
            select_house_type(house_item="位置类型", house_type="学校").\
            select_house_type(house_item="区域", house_type="雨花台区").\
            select_house_type(house_item="学校", house_type="西善桥中心小学").\
            select_house_location_confirm().screenshot()

    @allure.description("点击心仪户型-五室以上")
    def test_select_house_style(self):
        """
        点击心仪户型-五室以上
        :return:
        """
        self.shouye.\
            select_house_type(house_item="心仪户型", house_type="五室以上").screenshot()

    @allure.description("点击购房目的-投资、结婚")
    def test_select_purpose(self):
        """
        点击购房目的-投资、结婚
        :return:
        """
        self.shouye.\
            swipe_to_buttom().\
            select_house_type(house_item="购房目的", house_type="投资"). \
            select_house_type(house_item="购房目的", house_type="结婚"). \
            screenshot()

    @allure.description("点击面积-200㎡以上")
    def test_select_size(self):
        """
        点击面积-200㎡以上
        :return:
        """
        self.shouye.\
            swipe_to_buttom().\
            select_house_type(house_item="面积", house_type="200㎡以上").screenshot()

    @allure.description("点击“选填更多需求”")
    def test_goto_more_requirement(self):
        """

        :return:
        """
        self.shouye.\
            swipe_to_buttom().\
            goto_house_more_requirement().screenshot()

    @allure.description("点击 住宅、五室-立即找房 ")
    def test_goto_find_house(self):
        """
        点击住宅、五室-立即找房
        :return:
        """
        self.shouye.\
            select_house_type(house_item="房屋类型", house_type="住宅").\
            swipe_to_buttom().\
            select_house_type(house_item="心仪户型", house_type="五室").\
            click_find_house_button().screenshot()
