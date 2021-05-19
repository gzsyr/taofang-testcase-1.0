import allure
from test_case.base_test.test_base import TestBase


class TestMain(TestBase):
    """
    首页的用例
    """

    # shouye = App().start().main()

    #功能入口的测试用例
    @allure.description("点击功能入口“新房”tab，进入新房列表页面")
    def test_click_newhouse(self):
        self.shouye.goto_func_entrance_newhouse().screenshot()

    @allure.description("点击功能入口“二手房”tab，进入二手房列表页面")
    def test_click_newhouse(self):
        self.shouye.goto_func_entrance_esf().back().goto_func_entrance_newhouse().back()

    @allure.description("点击功能入口第二屏的“买房流程”")
    def test_click_trade_process(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_trade_process()
        # self.shouye.cancel_index_adv().func_entrance_swape_left().goto_func_entrance_trade_process()

    @allure.description("点击功能入口第三屏的求租")
    def test_click_find_house(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").func_entrance_swipe_left("家居").goto_func_entrance_find_house()

    # @allure.description("点击新房列表页面，列表项的第一个楼盘，进入详情页")
    # def test_goto_newhouse_detail(self):
    #     self.shouye.goto_newhouse().goto_newhouse_detail().screenshot()
    #
    # @allure.description("点击新房详情页面的“查看更多”，进入相册页面")
    # def test_goto_newhouse_detail(self):
    #     self.shouye.goto_newhouse().goto_newhouse_detail().goto_photo().screenshot()

    @allure.description("点击“购房工具”功能入口，进入购房工具箱页面")
    def test_click_gfgj(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.goto_func_entrance_gfgj().screenshot()

    @allure.description("点击“地图找房”功能入口，进入地图找房页面")
    def test_click_map(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.goto_func_entrance_map().screenshot()

    @allure.description("点击“学校地图”功能入口，进入学校地图页面")
    def test_click_school_map(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.goto_func_entrance_school_map().screenshot()

    @allure.description("点击“查房价”功能入口，进入查房价首页")
    def test_click_check_price(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.goto_func_entrance_check_price().screenshot()

    @allure.description("点击“找小区”功能入口，进入小区列表页面")
    def test_click_find_community(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.goto_func_entrance_find_community().screenshot()

    @allure.description("点击“摇号查询”功能入口，进入淘房小程序")
    def test_click_find_community(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.goto_func_entrance_lottery_query().screenshot()

    @allure.description("点击“看房团”功能入口，进入看房团列表页面")
    def test_click_group_house(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.goto_func_entrance_group_house().screenshot()

    @allure.description("点击“直播”功能入口，进入直播列表页面")
    def test_click_live(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.goto_func_entrance_live().screenshot()

    @allure.description("点击“视频说房”功能入口，进入视频说房列表页面")
    def test_click_video_house(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.goto_func_entrance_video_house().screenshot()

    @allure.description("点击“签到”功能入口，进入积分商城页面")
    def test_click_online_shop(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.goto_func_entrance_online_shop().screenshot()


    @allure.description("点击“房博士”功能入口，进入房博士首页")
    def test_click_doctor(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_doctor().screenshot()

    @allure.description("点击“计算器”功能入口，进入贷款计算器页面")
    def test_click_calculator(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_calculator().screenshot()

    @allure.description("点击“365直卖”功能入口，进入直卖房源列表页面")
    def test_click_zhimai_list(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_zhimai_list().screenshot()

    @allure.description("点击“家居”功能入口，进入家居H5首页")
    def test_click_home_improvement(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_home_improvement().screenshot()

    @allure.description("点击“求购”功能入口，进入我要买房页面")
    def test_click_want_buy(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_want_buy().screenshot()

    @allure.description("点击“我要卖房”功能入口，进入发布房源页面")
    def test_click_publish_sell(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_publish_sell().screenshot()

    @allure.description("点击“金融服务”功能入口，进入365小贷H5页面")
    def test_click_financial_service(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_financial_service().screenshot()

    @allure.description("点击“VR看房”功能入口，进入VR看房列表页面")
    def test_click_VR_list(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_VR_list().screenshot()

    @allure.description("点击“养老频道”功能入口，进入365养老小程序")
    def test_click_pension_channel(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_pension_channel().screenshot()


    @allure.description("点击“我要出租”功能入口，进入发布租房页面")
    def test_click_publish_rent(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").func_entrance_swipe_left("家居").goto_func_entrance_publish_rent().screenshot()


    @allure.description("点击“房产资讯”功能入口，进入资讯列表页面")
    def test_click_news(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swipe_left("找小区").func_entrance_swipe_left("家居").goto_func_entrance_news().screenshot()