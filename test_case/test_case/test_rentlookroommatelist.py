import allure

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 租房-找室友页面的测试")
class TestLookRoommateList(TestBase):
    """
    找室友用例
    """
    @allure.description("找室友列表点击我的找室友入口")
    def test_lookroom_mine(self):
        """
        找室友列表点击我的找室友入口
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_function_entrance("找室友").lookroom_mine().screenshot()

    @allure.description("找室友列表点击消息")
    def test_lookroom_news(self):
        """
        找室友列表点击消息
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_function_entrance("找室友").lookroom_news().screenshot()

    @allure.description("找室友列表点击收藏按钮")
    def test_click_lookroom_collection(self):
        """
        找室友列表点击收藏
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_function_entrance("找室友").click_lookroom_collection().screenshot()

    @allure.description("找室友列表点击在线聊按钮")
    def test_click_lookroom_online(self):
        """
        找室友列表点击在线聊
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_function_entrance("找室友").click_lookroom_online().screenshot()

    @allure.description("找室友列表点击第一条房源")
    def test_click_lookroom_fristroom(self):
        """
        找室友列表点击第一条房源
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_function_entrance("找室友").click_lookroom_fristroom().screenshot()

    @allure.description("找室友列表点击发布入口")
    def test_click_lookroom_release(self):
        """
        找室友列表点击发布入口
        :return:
        """
        self.shouye.goto_func_entrance_zf().rent_house_function_entrance("找室友").click_lookroom_release().screenshot()



