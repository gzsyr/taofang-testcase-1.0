import allure

from page_object.base_page.base_page import BasePage


class HouseDoctorMain(BasePage):
    """
    房博士模块的首页
    """
    def goto_doctor_search(self):
        """
        点击搜索按钮
        :return:
        """
        with allure.step("房博士页面，点击“搜索”"):
            self.steps("../../page_object/housedoctor/housedoctormain.yaml")

        return self

    def goto_doctor_call(self):
        """
        点击“电话咨询”
        :return:
        """
        with allure.step("房博士页面，点击“电话咨询”"):
            self.steps("../../page_object/housedoctor/housedoctormain.yaml")

        return self

    def goto_doctor_ask(self):
        """
        点击“快速提问”
        :return:
        """
        with allure.step("房博士页面，点击“快速提问”"):
            self.steps("../../page_object/housedoctor/housedoctormain.yaml")

        return self

    def goto_doctor_wiki_first(self):
        """
        点击购房百科第一条
        :return:
        """
        with allure.step("房博士页面，点击购房百科第一条"):
            self.steps("../../page_object/housedoctor/housedoctormain.yaml")

        return self

    def goto_doctor_wiki_more(self):
        """
        点击购房百科“更多”
        :return:
        """
        with allure.step("房博士页面，点击购房百科“更多”"):
            self.steps("../../page_object/housedoctor/housedoctormain.yaml")

        return self

    def goto_doctor_more(self):
        """
        点击房博士“更多”
        :return:
        """
        with allure.step("房博士页面，点击房博士“更多”"):
            self.steps("../../page_object/housedoctor/housedoctormain.yaml")

        return self

    def goto_doctor_photo_first(self):
        """
        点击第一个房博士头像
        :return:
        """
        with allure.step("房博士页面，点击第一个房博士头像"):
            self.steps("../../page_object/housedoctor/housedoctormain.yaml")

        return self

    def goto_doctor_consult_first(self):
        """
        点击第一个房博士的“咨询我”
        :return:
        """
        with allure.step("房博士页面，点击第一个房博士的“咨询我”"):
            self.steps("../../page_object/housedoctor/housedoctormain.yaml")

        return self

    def goto_doctor_hot_more(self):
        """
        点击热门问答的“更多”
        :return:
        """
        with allure.step("房博士页面，点击热门问答的“更多”"):
            self.steps("../../page_object/housedoctor/housedoctormain.yaml")

        return self

    def goto_doctor_question_first(self):
        """
        点击热门问答的第一条
        :return:
        """
        with allure.step("房博士页面，点击热门问答的第一条"):
            self.steps("../../page_object/housedoctor/housedoctormain.yaml")

        return self

    def goto_doctor_tag_first(self):
        """
        点击热门问答的第一个标签
        :return:
        """
        with allure.step("房博士页面，点击热门问答的第一个标签"):
            self.steps("../../page_object/housedoctor/housedoctormain.yaml")

        return self