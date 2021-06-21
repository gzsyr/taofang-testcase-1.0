import allure
import pytest

from test_case.base_test.test_base import TestBase


class TestMain(TestBase):
    """
    首页的用例
    """

    # 变更功能入口第一屏的用例方式，改成参数传递 by zsy
    @allure.description("点击功能入口")
    @pytest.mark.parametrize("func_entry", ["新房", "二手房", "租房", "商铺办公", "房源发布",
                                            "购房工具", "地图找房", "学校地图", "查房价", "找小区",
                                            "摇号查询", "看房团", "直播", "视频说房", "签到"])
    def test_click_func_entry(self, func_entry):
        self.shouye.goto_func_entrance_first(func_entry).screenshot()

    #功能入口的测试用例合并到test_click_func_entry  by zsy
    # @allure.description("点击功能入口“新房”tab，进入新房列表页面")
    # def test_click_newhouse(self):
    #     self.shouye.goto_func_entrance_newhouse().screenshot()
    #
    # @allure.description("点击功能入口“二手房”tab，进入二手房列表页面")
    # def test_click_sellhouse(self, cancel_adv):
    #     cancel_adv(self.app._driver)
    #     self.shouye.goto_func_entrance_esf().screenshot()

    @allure.description("下滑点击淘房头条更多")
    def test_goto_news_more(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("com.house365.newhouse:id/m_title").goto_news_more().screenshot()

    @allure.description("下滑点击淘房头条大新闻")
    def test_goto_news_live(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("com.house365.newhouse:id/m_title").goto_news_live().screenshot()

    @allure.description("点击功能入口“消息”tab，进入消息列表页面")
    def test_click_message(self):
        self.shouye.goto_message().screenshot()

    @allure.description("点击功能入口第二屏的“买房流程”")
    def test_click_trade_process(self):
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_trade_process().screenshot()

    @allure.description("点击功能入口第三屏的求租")
    def test_click_find_house(self):
        self.shouye.func_entrance_swipe_left("找小区").func_entrance_swipe_left("家居").goto_func_entrance_find_house().screenshot()

    # 合并到test_click_func_entry  by zsy
    # @allure.description("点击“购房工具”功能入口，进入购房工具箱页面")
    # def test_click_gfgj(self):
    #     self.shouye.goto_func_entrance_gfgj().screenshot()
    #
    # @allure.description("点击“地图找房”功能入口，进入地图找房页面")
    # def test_click_map(self):
    #     self.shouye.goto_func_entrance_map().screenshot()
    #
    # @allure.description("点击“学校地图”功能入口，进入学校地图页面")
    # def test_click_school_map(self):
    #     self.shouye.goto_func_entrance_school_map().screenshot()
    #
    # @allure.description("点击“查房价”功能入口，进入查房价首页")
    # def test_click_check_price(self):
    #     self.shouye.goto_func_entrance_check_price().screenshot()
    #
    # @allure.description("点击“找小区”功能入口，进入小区列表页面")
    # def test_click_find_community(self):
    #     self.shouye.goto_func_entrance_find_community().screenshot()
    #
    # @allure.description("点击“摇号查询”功能入口，进入淘房小程序")
    # def test_goto_func_entrance_lottery_query(self):
    #     self.shouye.goto_func_entrance_lottery_query().screenshot()
    #
    # @allure.description("点击“看房团”功能入口，进入看房团列表页面")
    # def test_click_group_house(self):
    #     self.shouye.goto_func_entrance_group_house().screenshot()
    #
    # @allure.description("点击“直播”功能入口，进入直播列表页面")
    # def test_click_live(self):
    #     self.shouye.goto_func_entrance_live().screenshot()
    #
    # @allure.description("点击“视频说房”功能入口，进入视频说房列表页面")
    # def test_click_video_house(self):
    #     self.shouye.goto_func_entrance_video_house().screenshot()
    #
    # @allure.description("点击“签到”功能入口，进入积分商城页面")
    # def test_click_online_shop(self):
    #     self.shouye.goto_func_entrance_online_shop().screenshot()
    #
    # @allure.description("点击“新房”tab，进入新房列表页面")
    # def test_click_func_newhouse(self):
    #     self.shouye.goto_func_entrance_newhouse().screenshot()

    @allure.description("点击城市")
    def test_click_city(self):
        self.shouye.goto_city().screenshot()

    @allure.description("点击首页搜索框")
    def test_click_search(self):
        self.shouye.goto_search().screenshot()

    @allure.description("点击首页扫一扫")
    def test_click_scan(self):
        self.shouye.goto_scan().screenshot()

    @allure.description("点击首页地图")
    def test_click_map(self):
        self.shouye.goto_map().screenshot()

    # 合并到test_click_func_entry  by zsy
    # @allure.description("点击首页二手房icon")
    # def test_click_func_sellhouse(self):
    #     self.shouye.goto_func_entrance_esf().screenshot()
    #
    # @allure.description("点击首页租房icon")
    # def test_click_func_rent(self):
    #     self.shouye.goto_func_entrance_zf().screenshot()
    #
    # @allure.description("点击首页商铺办公icon")
    # def test_click_func_spbg(self):
    #     self.shouye.goto_func_entrance_spbg().screenshot()
    #
    # @allure.description("点击首页发布房源icon")
    # def test_click_func_fbfy(self):
    #     self.shouye.goto_func_entrance_fyfb().screenshot()

    @allure.description("点击首页楼盘动态")
    def test_click_lpdt(self):
        self.shouye.goto_lpdt().screenshot()

    @allure.description("点击首页直卖楼盘")
    def test_click_zmlp(self):
        self.shouye.goto_zmlp().screenshot()

    @allure.description("点击首页近期开盘")
    def test_click_jqkp(self):
        self.shouye.goto_jqkp().screenshot()

    @allure.description("点击“房博士”功能入口，进入房博士首页")
    def test_click_doctor(self):
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_doctor().screenshot()

    @allure.description("点击“计算器”功能入口，进入贷款计算器页面")
    def test_click_calculator(self):
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_calculator().screenshot()

    @allure.description("点击“365直卖”功能入口，进入直卖房源列表页面")
    def test_click_zhimai_list(self):
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_zhimai_list().screenshot()

    @allure.description("点击“家居”功能入口，进入家居H5首页")
    def test_click_home_improvement(self):
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_home_improvement().screenshot()

    @allure.description("点击“求购”功能入口，进入我要买房页面")
    def test_click_want_buy(self):
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_want_buy().screenshot()

    @allure.description("点击“我要卖房”功能入口，进入发布房源页面")
    def test_click_publish_sell(self):
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_publish_sell().screenshot()

    @allure.description("点击“金融服务”功能入口，进入365小贷H5页面")
    def test_click_financial_service(self):
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_financial_service().screenshot()

    @allure.description("点击“VR看房”功能入口，进入VR看房列表页面")
    def test_click_VR_list(self):
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_VR_list().screenshot()

    @allure.description("点击“养老频道”功能入口，进入365养老小程序")
    def test_click_pension_channel(self):
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_pension_channel().screenshot()

    @allure.description("点击“我要出租”功能入口，进入发布租房页面")
    def test_click_publish_rent(self):
        self.shouye.func_entrance_swipe_left("找小区").func_entrance_swipe_left("家居").goto_func_entrance_publish_rent().screenshot()

    @allure.description("点击“房产资讯”功能入口，进入资讯列表页面")
    def test_click_news(self):
        self.shouye.func_entrance_swipe_left("找小区").func_entrance_swipe_left("家居").goto_func_entrance_news().screenshot()

    @allure.description("滑动到”马上找房“，点击找新房")
    def test_goto_find_newhouse_tab(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("马上找房").goto_find_newhouse_tab().screenshot()

    @allure.description("滑动到”马上找房“，点击找新房的马上找房")
    def test_goto_find_newhouse(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("马上找房").goto_find_newhouse().screenshot()

    @allure.description("滑动到”马上找房“，点击找二手房tab")
    def test_goto_find_second_tab(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("马上找房").goto_find_second_tab().screenshot()

    @allure.description("滑动到”马上找房“，点击找二手房的马上找房")
    def test_goto_find_second(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("马上找房").goto_find_second_tab().goto_find_second().screenshot()

    @allure.description("滑动到”马上找房“，点击找租房tab")
    def test_goto_find_rent_tab(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("马上找房").goto_find_rent_tab().screenshot()

    @allure.description("滑动到”马上找房“，点击找租房的马上找房")
    def test_goto_find_rent(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("马上找房").goto_find_rent_tab().goto_find_rent().screenshot()

    @allure.description("滑动到”马上找房“，点击我的房子tab")
    def test_goto_my_house_tab(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("马上找房").goto_my_house_tab().screenshot()

    @allure.description("滑动到”马上找房“，点击我的房子tab")
    def test_goto_my_house(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("马上找房").goto_my_house_tab().goto_my_house().screenshot()

    @allure.description("滑动到”马上找房“，点击帮你卖房tab")
    def test_goto_sell_house_tab(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("马上找房").goto_sell_house_tab().screenshot()

    @allure.description("滑动到”马上找房“，点击帮你卖房tab发布房源")
    def test_goto_release_house(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("马上找房").goto_sell_house_tab().goto_release_house().screenshot()

    @allure.description("滑动到”直播看房“，点击第一个直播")
    def test_goto_live_house(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("video_floor_title").goto_live_house().screenshot()

    @allure.description("滑动到”直播看房“，点击直播房源查看更多")
    def test_goto_live_house_more(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("video_floor_title").swipe_live_left().goto_live_house_more()

    @allure.description("滑动到”365房博士“，点击房价评估")
    def test_goto_price_evaluate(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("365房博士").goto_price_evaluate().screenshot()

    @allure.description("滑动到”365房博士“，点击南京二手房均价")
    def test_goto_second_price(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("365房博士").goto_second_price().screenshot()

    @allure.description("滑动到”365房博士“，点击房博士更多")
    def test_goto_doctor_more(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("咨询").goto_doctor_more().screenshot()

    @allure.description("滑动到”365房博士“，点击房博士头像")
    def test_goto_doctor_photo(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("咨询").goto_doctor_photo().screenshot()

    @allure.description("滑动到”365房博士“，点击房博士咨询按钮")
    def test_goto_doctor_consult(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("咨询").goto_doctor_consult().screenshot()

    @allure.description("滑动到”365房博士“，点击房博士问答数据")
    def test_goto_doctor_question(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("com.house365.newhouse:id/qa_tv").goto_doctor_question().screenshot()

    @allure.description("点击首页房博士tab")
    def test_click_doctor(self):
        self.shouye.goto_doctor().screenshot()

    @allure.description("点击首页发现tab")
    def test_click_find(self):
        self.shouye.goto_find().screenshot()

    @allure.description("点击首页我的tab")
    def test_click_my(self):
        self.shouye.goto_my().screenshot()

    @allure.description("滑动到”新房tab“，点击新房tab")
    def test_goto_newhouse_tab(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("tv_house_price_unit").goto_newhouse_tab().screenshot()

    @allure.description("滑动到”新房tab“，点击新房tab楼盘")
    def test_goto_newhouse_item(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("tv_house_price_unit").goto_tab_item().screenshot()

    @allure.description("滑动到”新房tab“，点击二手房tab")
    def test_goto_second_tab(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("tv_house_price_unit").goto_second_tab().screenshot()

    @allure.description("滑动到”新房tab“，点击二手房tab房源")
    def test_goto_second_item(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("tv_house_price_unit").goto_second_tab().goto_tab_item().screenshot()

    @allure.description("滑动到”新房tab“，点击租房tab")
    def test_goto_rent_tab(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("tv_house_price_unit").goto_rent_tab().screenshot()

    @allure.description("滑动到”新房tab“，点击租房tab数据")
    def test_goto_rent_item(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_swipe("tv_house_price_unit").goto_rent_tab().goto_tab_item().screenshot()

    @allure.description("切换城市")
    @pytest.mark.parametrize("letter, cityname", [("S", "苏州"), ("N", "南京")])
    def test_select_city(self, letter, cityname):
        self.shouye.goto_city().select_letter(letter).select_city(cityname).screenshot()
