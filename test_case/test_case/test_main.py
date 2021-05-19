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
        self.shouye.func_entrance_swape_left("找小区").goto_func_entrance_trade_process()
        # self.shouye.cancel_index_adv().func_entrance_swape_left().goto_func_entrance_trade_process()

    @allure.description("点击功能入口第三屏的求租")
    def test_click_find_house(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.shouye.func_entrance_swape_left("找小区").func_entrance_swape_left("家居").goto_func_entrance_find_house()

    # @allure.description("点击新房列表页面，列表项的第一个楼盘，进入详情页")
    # def test_goto_newhouse_detail(self):
    #     self.shouye.goto_newhouse().goto_newhouse_detail().screenshot()
    #
    # @allure.description("点击新房详情页面的“查看更多”，进入相册页面")
    # def test_goto_newhouse_detail(self):
    #     self.shouye.goto_newhouse().goto_newhouse_detail().goto_photo().screenshot()


