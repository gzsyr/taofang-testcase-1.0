import allure

from page_object.base_page.base_page import BasePage

class LookRoommateList(BasePage):
    """
    找室友页面相关元素
    """
    def lookroom_mine(self):
        """
        点击找室友列表我的找室友入口
        :return:
        """
        with allure.step("找室友列表点击我的找室友入口"):
            self.steps("../../page_object/renthouse/lookroommatelist.yaml")
            self.tsleep(2)

            return self

    def lookroom_news(self):
        """
        点击找室友列表消息入口
        :return:
        """
        with allure.step("找室友列表消息入口"):
            self.steps("../../page_object/renthouse/lookroommatelist.yaml")
            self.tsleep(2)

            return self

    def click_filter_position(self):
        """
        点击筛选项的“全南京”
        :return:
        """
        with allure.step("点击筛选项的“全南京”"):
            self.steps("../../page_object/renthouse/lookroommatelist.yaml")
        self.tsleep(2)

    def click_filter_position_menu(self, text="不限"):
        """
        点击筛选项“全南京”的菜单
        :param text: 传入的需要点击的参数
                     默认不限
        :return:
        """
        self._params["filter_postion"] = text
        with allure.step("点击筛选项的“全南京”的" + text):
            self.steps("../../page_object/renthouse/lookroommatelist.yaml", replace=True)
        self.tsleep(2)

        return self
