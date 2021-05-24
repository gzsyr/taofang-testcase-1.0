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

