import allure

from page_object.base_page.base_page import BasePage
from page_object.renthouse.renthousedetail import RentHouseDetail


class RentHouseList(BasePage):
    """
    租房房源列表页面
    """
    def click_renthouse_search(self):
        """
        点击租房房源列表搜索框
        :return:
        """
        with allure.step("点击租房房源列表页搜索框"):
            self.steps("../../page_object/renthouse/renthouselist.yaml")
        self.tsleep(2)
        return self

    def click_filter_position_menu(self, text='不限'):
        """
        :param text: 传入的需要点击的位置参数
                     默认不限
        :return:
        """
        self._params["filter_postion"] = text
        with allure.step("点击租房房源列表页筛选项：" + text):
            self.steps("../../page_object/renthouse/renthouselist.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_filter_position(self):
        """
        点击租房房源列表位置筛选项-全南京
        :return:
        """
        with allure.step("点击租房房源列表页位置筛选项：全南京"):
            self.steps("../../page_object/renthouse/renthouselist.yaml")
        self.tsleep(2)
        return self

    def click_filter_price(self):
        """
        点击租房房源列表租金筛选
        :return:
        """
        with allure.step("点击租房房源列表页租金筛选"):
            self.steps("../../page_object/renthouse/renthouselist.yaml")
        self.tsleep(2)
        return self

    def click_filter_room(self):
        """
        点击租房房源列表户型筛选
        :return:
        """
        with allure.step("点击租房房源列表页户型筛选"):
            self.steps("../../page_object/renthouse/renthouselist.yaml")
        self.tsleep(2)
        return self

    def click_filter_more(self):
        """
        点击租房房源列表更多筛选
        :return:
        """
        with allure.step("点击租房房源列表页更多筛选"):
            self.steps("../../page_object/renthouse/renthouselist.yaml")
        self.tsleep(2)
        return self

    def click_empty(self):
        """
        点击租房房源列表筛选项清空
        :return:
        """
        with allure.step("点击租房房源列表页筛选项清空"):
            self.steps("../../page_object/renthouse/renthouselist.yaml")
        self.tsleep(2)
        return self

    def click_definite(self):
        """
        点击租房房源列表筛选确定
        :return:
        """
        with allure.step("点击租房房源列表页筛选项确定"):
            self.steps("../../page_object/renthouse/renthouselist.yaml")
        self.tsleep(2)
        return self

    def click_filter_sort(self):
        """
        点击租房房源列表排序
        :return:
        """
        with allure.step("点击租房房源列表页排序"):
            self.steps("../../page_object/renthouse/renthouselist.yaml")
        self.tsleep(2)
        return self

    def click_cancel(self):
        """
        点击租房房源列表排序取消按钮
        :return:
        """
        with allure.step("点击租房房源列表页排序取消按钮"):
            self.steps("../../page_object/renthouse/renthouselist.yaml")
        self.tsleep(2)
        return self

    def click_ok(self):
        """
        点击租房房源列表排序确定按钮
        :return:
        """
        with allure.step("点击租房房源列表页排序确定按钮"):
            self.steps("../../page_object/renthouse/renthouselist.yaml")
        self.tsleep(2)
        return self

    def goto_renthouse_detail(self):
        """
        进入租房详情页
        :return:
        """
        with allure.step("进入租房详情页"):
            self.steps("../../page_object/renthouse/renthouselist.yaml")
        self.tsleep(2)
        return RentHouseDetail(self._driver)
