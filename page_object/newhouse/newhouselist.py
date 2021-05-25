import allure

from page_object.base_page.base_page import BasePage
from page_object.newhouse.newhousedetail import NewHouseDetail


class NewHouseList(BasePage):

    """
    新房列表页面，相关元素
    """

    def goto_newhouse_detail(self):
        """
        点击列表项第一个楼盘，进入详情页面
        :return:
        """
        with allure.step("点击列表项第一个楼盘，进入详情页面"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return NewHouseDetail(self._driver)

    def click_filter_position(self):
        """
        点击筛选项的“位置”
        :return:
        """
        with allure.step("点击筛选项的“位置”"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_filter_position_menu(self, text="不限"):
        """
        点击筛选项“位置”的菜单
        :param text: 传入的需要点击的位置参数
                     默认不限
        :return:
        """
        self._params["filter_postion"] = text
        with allure.step("点击筛选项的“位置”的" + text):
            self.steps("../../page_object/newhouse/newhouselist.yaml", replace=True)
        self.tsleep(2)

        return self

    def click_final_priorities(self):
        """
        点击筛选项下方的“综合排序”
        :return:
        """
        with allure.step("点击筛选项下方的“综合排序”"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

    def click_price(self):
        """
        点击筛选项下方的“价格”
        :return:
        """
        with allure.step("点击筛选项下方的“价格”"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

    def click_opening_time(self):
        """
        点击筛选项下方的“开盘时间”
        :return:
        """
        with allure.step("点击筛选项下方的“开盘时间”"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

    def click_attention_rate(self):
        """
        点击筛选项下方的“关注度”
        :return:
        """
        with allure.step("点击筛选项下方的“关注度”"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

