# 新房详情页面
import allure

from test_case.base_test.test_base import TestBase


class TestNewHouseDetail(TestBase):
    """
    新房详情页用例，通过搜索的方式进入新房详情页
    """
    _house = "长江时代1516"

    def goto_housedetail(self):
        """
        进入新房详情页
        :return:
        """
        return self.shouye.goto_search().action_search(self._house).select_search_result()

    @allure.description("点击新房详情页图片")
    def test_click_newhouse_detail_picture(self):
        """
        点击图片
        :return:
        """
        self.goto_housedetail().click_newhouse_detail_picture().screenshot()

    @allure.description("点击新房详情页“查看更多”")
    def test_click_newhouse_detail_more(self):
        """
        点击相册的“查看更多”
        :return:
        """
        self.goto_housedetail().click_newhouse_detail_more().screenshot()

    @allure.description("新房详情页点击收藏按钮")
    def test_click_newhouse_detail_collection(self):
        """
        新房详情页点击收藏按钮”
        :return:
        """
        self.goto_housedetail().click_newhouse_detail_collection().screenshot()

    @allure.description("新房详情页点击分享按钮")
    def test_click_newhouse_detail_share(self):
        """
        新房详情页点击分享按钮”
        :return:
        """
        self.goto_housedetail().click_newhouse_detail_share().screenshot()

    @allure.description("新房详情页点击地址")
    def test_click_newhouse_detail_arrow(self):
        """
        新房详情页点击地址”
        :return:
        """
        self.goto_housedetail().click_newhouse_detail_arrow().screenshot()

    @allure.description("新房详情页点击悬浮提问")
    def test_click_newhouse_detail_questions(self):
        """
        新房详情页点击悬浮提问”
        :return:
        """
        self.goto_housedetail().click_newhouse_detail_questions().screenshot()

    @allure.description("新房详情页点击计算器")
    def test_click_newhouse_detail_calculator(self):
        """
        新房详情页点击计算器”
        :return:
        """
        self.goto_housedetail().click_newhouse_detail_calculator().screenshot()

    @allure.description("新房详情页拨打400电话")
    def test_click_newhouse_detail_400tel(self):
        """
        新房详情页拨打400电话
        :return:
        """
        self.goto_housedetail().func_swipe("开盘通知我").click_newhouse_detail_400tel().screenshot()

    @allure.description("新房详情页点击开盘通知我")
    def test_click_newhouse_detail_kptz(self):
        """
        新房详情页点击开盘通知我
        :return:
        """
        self.goto_housedetail().func_swipe("开盘通知我").click_newhouse_detail_kptz().screenshot()

    @allure.description("新房详情页点击降价通知我")
    def test_click_newhouse_detail_jjtz(self):
        """
        新房详情页点击降价通知我
        :return:
        """
        self.goto_housedetail().func_swipe("开盘通知我").click_newhouse_detail_jjtz().screenshot()

    @allure.description("新房详情页点击一键加群")
    def test_click_newhouse_detail_key_group(self):
        """
        新房详情页点击一键加群
        :return:
        """
        self.goto_housedetail().func_swipe("最新动态").click_newhouse_detail_key_group().screenshot()

    @allure.description("新房详情页点击复制微信号")
    def test_click_newhouse_detail_cope_wechat(self):
        """
        新房详情页点击复制微信号
        :return:
        """
        self.goto_housedetail().func_swipe("最新动态").click_newhouse_detail_cope_wechat().screenshot()

    @allure.description("新房详情页点击我要预约")
    def test_click_newhouse_detail_signup(self):
        """
        新房详情页点击我要预约
        :return:
        """
        self.goto_housedetail().func_swipe("最新动态").click_newhouse_detail_signup().screenshot()

    @allure.description("新房详情页点击最新动态")
    def test_click_newhouse_detail_developmen(self):
        """
        新房详情页点击最新动态
        :return:
        """
        self.goto_housedetail().func_swipe("最新动态").click_newhouse_detail_developmen().screenshot()

    @allure.description("新房详情页点击户型解析")
    def test_click_newhouse_detail_hxjiexi(self):
        """
        新房详情页点击户型解析
        :return:
        """
        self.goto_housedetail().func_swipe("最新动态").click_newhouse_detail_hxjiexi().screenshot()

    @allure.description("新房详情页点击楼盘详情")
    def test_click_newhouse_detail_house_detail(self):
        """
        新房详情页点击楼盘详情
        :return:
        """
        self.goto_housedetail().func_swipe("最新动态").click_newhouse_detail_house_detail().screenshot()

    @allure.description("新房详情页点击楼盘点评")
    def test_click_newhouse_detail_house_comment(self):
        """
        新房详情页点击楼盘点评
        :return:
        """
        self.goto_housedetail().func_swipe("最新动态").click_newhouse_detail_house_comment().screenshot()

    @allure.description("新房详情页点击一房一价")
    def test_click_newhouse_detail_yifangyijia(self):
        """
        新房详情页点击一房一价
        :return:
        """
        self.goto_housedetail().func_swipe("详细信息").click_newhouse_detail_yifangyijia().screenshot()