# -- by hzc
import allure

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 我的页面的测试")
class TestMinePage(TestBase):
    """
    我的页面测试用例
    """
    @allure.description("点击个人资料")
    def test_click_personal_data(self):
        """
        点击我的页面个人资料
        :return:
        """
        self.shouye.goto_my().click_personal_data().screenshot()

    @allure.description("点击设置")
    def test_click_set_up(self):
        """
        点击我的页面设置
        :return:
        """
        self.shouye.goto_my().click_set_up().screenshot()

    @allure.description("点击消息")
    def test_click_minepage_message(self):
        """
        点击我的页面消息
        :return:
        """
        self.shouye.goto_my().click_minepage_message().screenshot()

    @allure.description("点击淘房币")
    def test_click_house_money(self):
        """
        点击淘房币
        :return:
        """
        self.shouye.goto_my().click_house_money().screenshot()

    @allure.description("点击邀请好友")
    def test_click_invite_friends(self):
        """
        点击邀请好友
        :return:
        """
        self.shouye.goto_my().click_invite_friends().screenshot()

    @allure.description("点击我的发布")
    def test_click_minepage_release(self):
        """
        点击我的发布
        :return:
        """
        self.shouye.goto_my().click_minepage_release().screenshot()

    @allure.description("点击收藏")
    def test_click_minepage_collection(self):
        """
        点击收藏
        :return:
        """
        self.shouye.goto_my().click_minepage_collection().screenshot()

    @allure.description("点击订阅")
    def test_click_minepage_subscribe(self):
        """
        点击订阅
        :return:
        """
        self.shouye.goto_my().click_minepage_subscribe().screenshot()

    @allure.description("点击足迹")
    def test_click_minepage_footprint(self):
        """
        点击足迹
        :return:
        """
        self.shouye.goto_my().click_minepage_footprint().screenshot()

    @allure.description("点击我的看房")
    def test_minepage_my_house(self):
        """
        点击我的看房
        :return:
        """
        self.shouye.goto_my().minepage_my_house().screenshot()

    @allure.description("点击更多")
    def test_minepage_more(self):
        """
        点击购房百科更多
        :return:
        """
        self.shouye.goto_my().func_swipe("购房百科").minepage_more().screenshot()

    @allure.description("点击我的点评")
    def test_minepage_my_comments(self):
        """
        点击我的点评
        :return:
        """
        self.shouye.goto_my().minepage_my_comments().screenshot()

    @allure.description("点击我的优惠")
    def test_minepage_my_discount(self):
        """
        点击我的优惠
        :return:
        """
        self.shouye.goto_my().minepage_my_discount().screenshot()

    @allure.description("点击我的问答")
    def test_minepage_my_question(self):
        """
        点击我的问答
        :return:
        """
        self.shouye.goto_my().minepage_my_question().screenshot()

    @allure.description("点击已购课程")
    def test_minepage_my_bought_course(self):
        """
        点击已购课程
        :return:
        """
        self.shouye.goto_my().minepage_my_bought_course().screenshot()

    @allure.description("点击我的奖品")
    def test_minepage_my_prize(self):
        """
        点击我的奖品
        :return:
        """
        self.shouye.goto_my().minepage_my_prize().screenshot()

    @allure.description("点击贷款查询")
    def test_minepage_loan_for(self):
        """
        点击贷款查询
        :return:
        """
        self.shouye.goto_my().minepage_loan_for().screenshot()

    @allure.description("点击公寓预约")
    def test_minepage_apartment_reservation(self):
        """
        点击公寓预约
        :return:
        """
        self.shouye.goto_my().minepage_apartment_reservation().screenshot()

    @allure.description("点击意见反馈")
    def test_minepage_feedback(self):
        """
        点击意见反馈
        :return:
        """
        self.shouye.goto_my().minepage_feedback().screenshot()

    @allure.description("点击客服电话")
    def test_minepage_service_telephone(self):
        """
        点击客服电话
        :return:
        """
        self.shouye.goto_my().minepage_service_telephone().screenshot()

    @allure.description("点击保证金管理")
    def test_minepage_margin_management(self):
        """
        点击保证金管理
        :return:
        """
        self.shouye.goto_my().minepage_margin_management().screenshot()

    @allure.description("点击帮你找房")
    def test_minepage_find_room(self):
        """
        点击帮你找房
        :return:
        """
        self.shouye.goto_my().minepage_find_room().screenshot()

    @allure.description("点击我的室友")
    def test_minepage_my_roommate(self):
        """
        点击我的室友
        :return:
        """
        self.shouye.goto_my().minepage_my_roommate().screenshot()