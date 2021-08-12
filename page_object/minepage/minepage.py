import allure

from page_object.base_page.base_page import BasePage

class MinePage(BasePage):
    """
    我的页面
    """
    def click_personal_data(self):
        """
        点击个人资料
        :return:
        """
        with allure.step("我的页面点击个人资料"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def click_set_up(self):
        """
        点击设置按钮
        :return:
        """
        with allure.step("我的页面点击设置"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def click_minepage_message(self):
        """
        点击消息入口
        :return:
        """
        with allure.step("我的页面点击消息"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def click_house_money(self):
        """
        点击淘房币
        :return:
        """
        with allure.step("我的页面点击淘房币"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def click_invite_friends(self):
        """
        点击邀请好友
        :return:
        """
        with allure.step("我的页面点击邀请好友"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def click_minepage_release(self):
        """
        点击我的发布
        :return:
        """
        with allure.step("我的页面点击我的发布"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def click_minepage_collection(self):
        """
        点击收藏
        :return:
        """
        with allure.step("我的页面点击收藏"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def click_minepage_subscribe(self):
        """
        点击订阅
        :return:
        """
        with allure.step("我的页面点击订阅"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def click_minepage_footprint(self):
        """
        点击足迹
        :return:
        """
        with allure.step("我的页面点击足迹"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_my_house(self):
        """
        点击我的看房
        :return:
        """
        with allure.step("我的页面点击我的看房"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_more(self):
        """
        点击更多
        :return:
        """
        with allure.step("我的页面点击更多"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_my_comments(self):
        """
        点击我的点评
        :return:
        """
        with allure.step("我的页面点击我的点评"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_my_discount(self):
        """
        点击我的优惠
        :return:
        """
        with allure.step("我的页面点击我的优惠"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_my_question(self):
        """
        点击我的问答
        :return:
        """
        with allure.step("我的页面点击我的问答"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_my_bought_course(self):
        """
        点击已购课程
        :return:
        """
        with allure.step("我的页面点击已购课程"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_my_prize(self):
        """
        点击我的奖品
        :return:
        """
        with allure.step("我的页面点击我的奖品"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_loan_for(self):
        """
        点击贷款查询
        :return:
        """
        with allure.step("我的页面点击贷款查询"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_apartment_reservation(self):
        """
        点击公寓预约
        :return:
        """
        with allure.step("我的页面点击公寓预约"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_feedback(self):
        """
        点击意见反馈
        :return:
        """
        with allure.step("我的页面点击意见反馈"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_service_telephone(self):
        """
        点击客服电话
        :return:
        """
        with allure.step("我的页面点击客服电话"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_margin_management(self):
        """
        点击保证金管理
        :return:
        """
        with allure.step("我的页面点击保证金管理"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_find_room(self):
        """
        点击帮你找房
        :return:
        """
        with allure.step("我的页面点击帮你找房"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def minepage_my_roommate(self):
        """
        点击我的室友
        :return:
        """
        with allure.step("我的页面点击我的室友"):
            self.steps("../../page_object/minepage/minepage.yaml")

        return self

    def func_swipe(self, pos_text=None):
        """
        滑动到pos_text的位置，滑动
        :param pos_text: 1、写入页面存在的元素
                         2、如果写pos_text=buttom，则滑动到页面底部
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step("滑动到" + self._params["pos_text"]):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml", replace=True)
        self.tsleep(2)
        return self