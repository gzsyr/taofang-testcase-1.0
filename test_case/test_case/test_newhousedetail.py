# 新房详情页面 -- by hzc
import allure

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 新房详情页面的测试")
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

    @allure.description("新房详情页点击楼盘动态右侧箭头")
    def test_click_newhouse_detail_dynamic_arrow(self):
        """
        新房详情页点击楼盘动态右侧箭头
        :return:
        """
        self.goto_housedetail().func_swipe("详细信息").click_newhouse_detail_dynamic_arrow().screenshot()

    @allure.description("新房详情页点击楼盘动态内容")
    def test_click_newhouse_detail_desc_short(self):
        """
        新房详情页点击楼盘动态内容
        :return:
        """
        self.goto_housedetail().func_swipe("详细信息").click_newhouse_detail_desc_short().screenshot()

    @allure.description("新房详情页点击楼盘动态内容下拉箭头")
    def test_click_newhouse_detail_more_ico(self):
        """
        新房详情页点击楼盘动态内容下拉箭头
        :return:
        """
        self.goto_housedetail().func_swipe("详细信息").click_newhouse_detail_more_ico().screenshot()

    @allure.description("新房详情页点击详细信息的“纠错”")
    def test_click_newhouse_detail_error_correction(self):
        """
        新房详情页点击详细信息的“纠错”
        :return:
        """
        self.goto_housedetail().func_swipe("主力户型").click_newhouse_detail_error_correction().screenshot()

    @allure.description("新房详情页点击详细信息的下拉箭头")
    def test_click_newhouse_detail_xxnr_more_ico(self):
        """
        新房详情页点击详细信息的下拉箭头
        :return:
        """
        self.goto_housedetail().func_swipe("主力户型").click_newhouse_detail_xxnr_more_ico().screenshot()

    @allure.description("新房详情页点击位置及周边右侧箭头")
    def test_click_newhouse_detail_wzzb_address(self):
        """
        新房详情页点击位置及周边右侧箭头
        :return:
        """
        self.goto_housedetail().func_swipe("咨询楼盘配套及区域规划").click_newhouse_detail_wzzb_address().screenshot()

    @allure.description("新房详情页点击位置及周边下拉箭头")
    def test_click_newhouse_detail_wzzb_more_ico(self):
        """
        新房详情页点击位置及周边下拉箭头
        :return:
        """
        self.goto_housedetail().func_swipe("咨询楼盘配套及区域规划").click_newhouse_detail_wzzb_more_ico().screenshot()

    @allure.description("新房详情页点击位置及周边“咨询楼盘配套及区域规划”")
    def test_click_newhouse_detail_tv_plan(self):
        """
        新房详情页点击位置及周边“咨询楼盘配套及区域规划”
        :return:
        """
        self.goto_housedetail().func_swipe("咨询楼盘配套及区域规划").click_newhouse_detail_tv_plan().screenshot()

    @allure.description("新房详情页点击位置及周边的地图")
    def test_click_newhouse_detail_map_image(self):
        """
        新房详情页点击位置及周边的地图
        :return:
        """
        self.goto_housedetail().func_swipe("咨询楼盘配套及区域规划").click_newhouse_detail_map_image().screenshot()

    @allure.description("新房详情页点击楼盘点评右侧箭头")
    def test_click_newhouse_detail_imageview(self):
        """
        新房详情页点击楼盘点评右侧箭头
        :return:
        """
        self.goto_housedetail().func_swipe("com.house365.newhouse:id/room_ratingbar").click_newhouse_detail_imageview().screenshot()

    @allure.description("新房详情页点击楼盘点评“点评赚淘房币，立即点评”")
    def test_click_newhouse_detail_bt_comment(self):
        """
        新房详情页点击 楼盘点评“点评赚淘房币，立即点评”
        :return:
        """
        self.goto_housedetail().func_swipe("我要提问").click_newhouse_detail_bt_comment().screenshot()

    @allure.description("新房详情页点击房博士解读右侧“更多”")
    def test_click_newhouse_detail_fbs_right_arrow(self):
        """
        新房详情页点击房博士解读右侧“更多”
        :return:
        """
        self.goto_housedetail().func_swipe("我要提问").click_newhouse_detail_fbs_right_arrow().screenshot()

    @allure.description("新房详情页点击房博士房博士内容项")
    def test_click_newhouse_detail_tv_title_ask(self):
        """
        新房详情页点击房博士房博士内容项
        :return:
        """
        self.goto_housedetail().func_swipe("我要提问").click_newhouse_detail_tv_title_ask().screenshot()

    @allure.description("新房详情页点击房博士“我要提问”")
    def test_click_newhouse_detail_bt_ask(self):
        """
        新房详情页点击房博士“我要提问”
        :return:
        """
        self.goto_housedetail().func_swipe("我要提问").click_newhouse_detail_bt_ask().screenshot()

    @allure.description("新房详情页点击申请优惠")
    def test_click_newhouse_detail_tfh_discount(self):
        """
        新房详情页点击申请优惠
        :return:
        """
        self.goto_housedetail().click_newhouse_detail_tfh_discount().screenshot()

    @allure.description("新房详情页点击我要看房")
    def test_click_newhouse_detail_look_house(self):
        """
        新房详情页点击我要看房
        :return:
        """
        self.goto_housedetail().click_newhouse_detail_look_house().screenshot()

    @allure.description("新房详情页点击在线咨询")
    def test_click_newhouse_detail_online_chat_tfh(self):
        """
        新房详情页点击在线咨询
        :return:
        """
        self.goto_housedetail().click_newhouse_detail_online_chat_tfh().screenshot()

    @allure.description("新房详情页点击拨打电话")
    def test_click_newhouse_detail_call_tfh(self):
        """
        新房详情页点击拨打电话
        :return:
        """
        self.goto_housedetail().click_newhouse_detail_call_tfh().screenshot()