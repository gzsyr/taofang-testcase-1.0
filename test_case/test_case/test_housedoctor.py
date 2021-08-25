# -- by zsy
import allure

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 房博士页面的测试")
class TestHouseDoctor(TestBase):
    """
    房博士页面的所有用例
    """
    @allure.description("点击房博士页面搜索框")
    def test_goto_doctor_search(self):
        """
        点击房博士页面搜索框
        :return:
        """
        self.shouye.goto_doctor().goto_doctor_search().screenshot()

    @allure.description("点击房博士页面“电话咨询”")
    def test_goto_doctor_call(self):
        """
        点击房博士页面“电话咨询”
        :return:
        """
        self.shouye.goto_doctor().goto_doctor_call().screenshot()

    @allure.description("点击房博士页面“快速提问”")
    def test_goto_doctor_ask(self):
        """
        点击房博士页面“快速提问”
        :return:
        """
        self.shouye.goto_doctor().goto_doctor_ask().screenshot()

    @allure.description("点击房博士页面百科第一条")
    def test_goto_doctor_wiki_first(self):
        """
        点击房博士页面百科第一条
        :return:
        """
        self.shouye.goto_doctor().goto_doctor_wiki_first().screenshot()

    @allure.description("点击房博士页面百科更多")
    def test_goto_doctor_wiki_more(self):
        """
        点击房博士页面百科更多
        :return:
        """
        self.shouye.goto_doctor().goto_doctor_wiki_more().screenshot()

    @allure.description("点击房博士更多")
    def test_goto_doctor_more(self):
        """
        点击房博士更多
        :return:
        """
        self.shouye.goto_doctor().goto_doctor_more().screenshot()

    @allure.description("点击房博士第一个头像")
    def test_goto_doctor_photo_first(self):
        """
        点击房博士第一个头像
        :return:
        """
        self.shouye.goto_doctor().goto_doctor_photo_first().screenshot()

    @allure.description("点击房博士第一个咨询我")
    def test_goto_doctor_consult_first(self):
        """
        点击房博士第一个咨询我
        :return:
        """
        self.shouye.goto_doctor().goto_doctor_consult_first().screenshot()

    @allure.description("点击热门问答的更多")
    def test_goto_doctor_hot_more(self):
        """
        点击热门问答的更多
        :return:
        """
        self.shouye.goto_doctor().swipe_to_buttom(text='com.house365.newhouse:id/new_good').goto_doctor_hot_more().screenshot()

    @allure.description("点击热门第一个问题")
    def test_goto_doctor_question_first(self):
        """
        点击热门第一个问题
        :return:
        """
        self.shouye.goto_doctor().swipe_to_buttom(text='com.house365.newhouse:id/new_good').goto_doctor_question_first().screenshot()

    @allure.description("点击热门第一个标签")
    def test_goto_doctor_tag_first(self):
        """
        点击热门第一个标签
        :return:
        """
        self.shouye.goto_doctor().goto_doctor_tag_first().screenshot()
