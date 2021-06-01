# 搜索总文件，包括首页进入的搜索、新房进入的搜索、二手房进入的搜索
import allure

from test_case.base_test.test_base import TestBase


class TestSearch(TestBase):
    """
    搜索相关测试用例
    """
    @allure.description("从搜索框进入搜索页面，输入关键词")
    def test_search_newhouse_keyword(self):
        """
        从搜索框进入搜索页面，输入关键词
        :return:
        """
        self.shouye.goto_search().action_search("万科").screenshot()

    @allure.description("从搜索框进入搜索页面，输入关键词“江山荟”")
    def test_search_newhouse_result(self):
        """
        从搜索框进入搜索页面，输入关键词
        :return:
        """
        self.shouye.goto_search().action_search("江山荟").select_search_result().screenshot()

    @allure.description("点击查看搜索类型")
    def test_search_show_type(self):
        """
        點擊搜索類型
        :return:
        """
        self.shouye.goto_search().show_business().screenshot()

    @allure.description("从搜索框进入搜索页面，点击“二手房”，输入关键词“瑞金新村”")
    def test_search_sellhouse_keyword(self):
        """
        从搜索框进入搜索页面，点击“二手房”，输入关键词“瑞金新村”
        :return:
        """
        self.shouye.goto_search().show_business().select_business("二手房").action_search("瑞金新村").screenshot()

    @allure.description("从搜索框进入搜索页面，点击“租房”，输入关键词“瑞金新村”")
    def test_search_rent_keyword(self):
        """
        从搜索框进入搜索页面，点击“租房”，输入关键词“瑞金新村”
        :return:
        """
        self.shouye.goto_search().show_business().select_business("租房").action_search("瑞金新村").screenshot()

    @allure.description("从搜索框进入搜索页面，点击“商铺”，输入关键词“瑞金新村”")
    def test_search_store_keyword(self):
        """
        从搜索框进入搜索页面，点击“商铺”，输入关键词“瑞金新村”
        :return:
        """
        self.shouye.goto_search().show_business().select_business("商铺").action_search("瑞金新村").screenshot()

    @allure.description("从搜索框进入搜索页面，点击“找小区”，输入关键词“尧化门街小区”")
    def test_search_community_keyword(self):
        """
        从搜索框进入搜索页面，点击“找小区”，输入关键词“尧化门街小区”
        :return:
        """
        self.shouye.goto_search().show_business().select_business("找小区").action_search("尧化门街小区").screenshot()

    @allure.description("从搜索框进入搜索页面，点击取消按钮，回到首页")
    def test_search_cancel(self):
        """
        从搜索框进入搜索页面，点击取消按钮，回到首页
        :return:
        """
        self.shouye.goto_search().click_cancel().screenshot()