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
