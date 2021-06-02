import allure

from page_object.base_page.base_page import BasePage


class BuyingHouse(BasePage):
    """
    我要买房页面
    """
    def delete_in_page(self):
        """
        判断“删除”文字是否在当前页面
        注：如果用查找元素的方法，不存在的话，就会用例失败
        :return:
        """
        return self.inPageSource(text="删除")

    def show_buying_house_page(self):
        """
        条件：当前页面是“专属房卡”页面
        目的：删除该页面，需要重新生成
        步骤：1、点击“删除”
             2、点击“是”
             3、点击“开始生成”
        :return:
        """
        self.steps("../../page_object/sellhouse/buyinghouse.yaml")

    def select_house_type(self, house_item="房屋", house_type="住宅"):
        """
        选择 房屋类型
        :param:  house_item: 选择项，用户步骤中展示
                 house_type: 房屋类型，默认为“住宅”
        :return:
        """
        self._params["house_type"] = house_type
        with allure.step("选择”" + house_item + "“的内容：" + house_type):
            self.steps("../../page_object/sellhouse/buyinghouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def swipe_house_budget(self, house_type="住宅"):
        """
        选择 预算
        :param: house_type: 房屋类型，默认为“住宅”
        :return:
        """
        # with allure.step("选择预算"):
        #     self.steps("../../page_object/sellhouse/buyinghouse.yaml", replace=True)
        # self.tsleep(2)
        # return self
        pass

    def show_location(self):
        """
        点击意向位置，弹出选择项
        :return:
        """
        with allure.step("点击意向位置"):
            self.steps("../../page_object/sellhouse/buyinghouse.yaml")

        self.tsleep(2)
        return self

    def select_house_location(self, house_location="不限"):
        """
        选择意向位置的内容
        :param: house_location: 默认“不限”
        :return:
        """
        with allure.step("选择意向位置：" + house_location):
            self.steps("../../page_object/sellhouse/buyinghouse.yaml", replace=True)

        self.tsleep(2)
        return self

    def select_house_location_confirm(self):
        """
        选择意向位置弹框的“确定”
        :return:
        """
        with allure.step("选择意向位置："):
            self.steps("../../page_object/sellhouse/buyinghouse.yaml")

        self.tsleep(2)
        return self

    def goto_house_more_requirement(self):
        """
        点击“选填更多需求”
        :return:
        """
        with allure.step("点击“选填更多需求”"):
            self.steps("../../page_object/sellhouse/buyinghouse.yaml")

        self.tsleep(2)
        return self

    def click_find_house_button(self):
        """
        点击“立即找房”
        :return:
        """
        with allure.step("点击“选填更多需求”"):
            self.steps("../../page_object/sellhouse/buyinghouse.yaml")

        self.tsleep(2)
        return self

