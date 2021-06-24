import allure

from page_object.base_page.base_page import BasePage


class RentFindHouse(BasePage):
    """
    我要求租页面
    """
    def select_rent_tiem(self, text="住宅"):
        """
        选择我要求租选项
        :return:
        """
        self._params["rent_item"] = text
        with allure.step("选择我要求租选项"):
            self.steps("../../page_object/renthouse/rentfindhouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def show_location(self):
        """
        展开位置弹窗
        :return:
        """
        with allure.step("展开我要求租位置弹窗"):
            self.steps("../../page_object/renthouse/rentfindhouse.yaml")
        self.tsleep(2)
        return self

    def select_rent_location(self, text="鼓楼区"):
        """
        位置区属选择
        :return:
        """
        self._params["rent_location"] = text
        with allure.step("位置区属选择"):
            self.steps("../../page_object/renthouse/rentfindhouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_rent_location_reset(self):
        """
        意向位置，点击重置
        :return:
        """
        with allure.step("重置意向位置"):
            self.steps("../../page_object/renthouse/rentfindhouse.yaml")
        self.tsleep(2)
        return self

    def click_rent_location_confirm(self):
        """
        意向位置，点击确定
        :return:
        """
        with allure.step("确定意向位置"):
            self.steps("../../page_object/renthouse/rentfindhouse.yaml")
        self.tsleep(2)
        return self

    def click_rent_findhouse(self):
        """
        发布求租信息
        :return:
        """
        with allure.step("发布求租信息"):
            self.steps("../../page_object/renthouse/rentfindhouse.yaml")
        self.tsleep(2)
        return self
