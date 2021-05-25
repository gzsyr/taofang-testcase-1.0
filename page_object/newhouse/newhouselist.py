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

    def click_search_text(self):
        """
        点击列表项搜索框
        :return:
        """
        with allure.step("点击列表项搜索框"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_map(self):
        """
        点击列表项地图
        :return:
        """
        with allure.step("点击列表项地图"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_layout_one(self):
        """
        点击聚合入口1
        :return:
        """
        with allure.step("点击聚合入口1"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_layout_two(self):
        """
        点击聚合入口2
        :return:
        """
        with allure.step("点击聚合入口2"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_layout_three(self):
        """
        点击聚合入口3
        :return:
        """
        with allure.step("点击聚合入口3"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_layout_four(self):
        """
        点击聚合入口4
        :return:
        """
        with allure.step("点击聚合入口4"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_filter_price(self):
        """
        点击筛选项的“价格”
        :return:
        """
        with allure.step("点击筛选项的“价格”"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_filter_room(self):
        """
        点击筛选项的“户型”
        :return:
        """
        with allure.step("点击筛选项的“户型”"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_filter_screen(self):
        """
        点击筛选项的“筛选”
        :return:
        """
        with allure.step("点击筛选项的“筛选”"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_delete(self):
        """
        点击删除按钮
        :return:
        """
        with allure.step("点击删除按钮"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_empty(self):
        """
        点击删选清空按钮
        :return:
        """
        with allure.step("点击筛选清空按钮"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_definite(self):
        """
        点击删选确定按钮
        :return:
        """
        with allure.step("点击筛选确定按钮"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
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

        return self

    def click_price(self):
        """
        点击筛选项下方的“价格”
        :return:
        """
        with allure.step("点击筛选项下方的“价格”"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_opening_time(self):
        """
        点击筛选项下方的“开盘时间”
        :return:
        """
        with allure.step("点击筛选项下方的“开盘时间”"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
        self.tsleep(2)

        return self

    def click_attention_rate(self):
        """
        点击筛选项下方的“关注度”
        :return:
        """
        with allure.step("点击筛选项下方的“关注度”"):
            self.steps("../../page_object/newhouse/newhouselist.yaml")
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
            self.steps("../../page_object/newhouse/newhouselist.yaml", replace=True)
        self.tsleep(2)
        return self

