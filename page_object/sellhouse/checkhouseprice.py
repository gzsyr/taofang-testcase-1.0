import allure

from page_object.base_page.base_page import BasePage


class CheckHousePrice(BasePage):
    """
    查房价首页
    """
    def click_search_house(self):
        """
        点击搜索框
        :return:
        """
        with allure.step("点击输入小区名称查房价搜索框"):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml")
        self.tsleep(2)
        return self

    def select_house(self, house_name='雨花客厅'):
        """
        输入小区
        :return:
        """
        self._params["house_name"] = house_name
        with allure.step("快速评估，输入小区名" + house_name):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml", replace=True)
        self.tsleep(2)
        return self

    def send_area(self, area='89'):
        """
        输入面积
        :return:
        """
        self._params["area"] = area
        with allure.step("快速评估，输入面积" + area):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml", replace=True)
        self.tsleep(2)
        return self

    def quick_check_house_price(self, house_name="雨花客厅", area='89'):
        """
        快速评估房价
        :return:
        """
        self._params["house_name"] = house_name
        self._params["area"] = area
        with allure.step("输入房屋信息，快速评估房价：小区名称=" + house_name + "，面积=" + area):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml", replace=True)
        self.tsleep(2)
        return self

    def check_nearby_price(self):
        """
        查看附近房价
        :return:
        """
        with allure.step("查看附近房价"):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml")
        self.tsleep(2)
        return self

    def click_house_price_map(self):
        """
        查看房价地图
        :return:
        """
        with allure.step("查看房价地图"):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml")
        self.tsleep(2)
        return self

    def goto_district_house_price(self, position="鼓楼区"):
        """
        点击区属房价
        :return:
        """
        self._params["position"] = position
        with allure.step("查看区属房价:" + position):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_more_record(self):
        """
        查看更多评估记录
        :return:
        """
        with allure.step("查看历史评估记录"):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml")
        self.tsleep(2)
        return self

    def view_record_result(self):
        """
        查看我的评估记录-评估结果
        :return:
        """
        with allure.step("查看我的评估记录的结果"):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml")
        self.tsleep(2)
        return self

    def view_record_house(self):
        """
        查看我的评估记录-小区详情
        :return:
        """
        with allure.step("查看我的评估记录的小区详情"):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml")
        self.tsleep(2)
        return self

    def view_record_expert_evaluation(self):
        """
        查看我的评估记录-专家评估
        :return:
        """
        with allure.step("查看我的评估记录的专家评估"):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml")
        self.tsleep(2)
        return self

    def goto_write_house_information(self):
        """
        点击底部的输入房屋信息按钮，进入填写页
        :return:
        """
        with allure.step("点击底部的输入房屋信息按钮，进入填写页"):
            self.steps("../../page_object/sellhouse/checkhouseprice.yaml")
        self.tsleep(2)
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
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml", replace=True)
        self.tsleep(2)
        return self

