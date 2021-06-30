import allure

from page_object.base_page.base_page import BasePage


class BrandApartmentList(BasePage):
    """
    品牌公寓页面
    """


    def click_brandapartmentlist_filter(self,text=None):
        """
        品牌公寓筛选项
        """
        self._params["filter"] = text
        with allure.step("点击筛选项"+ text):
            self.steps("../../page_object/renthouse/brandapartmentlist.yaml", replace=True)
        self.tsleep(1)
        return self

    def click_brandapartmentlist_type(self):
        """
        点击类型
        """
        with allure.step("点击类型"):
            self.steps("../../page_object/renthouse/brandapartmentlist.yaml")
        self.tsleep(1)
        return self

    def click_brandapartmentlist_location(self):
        """
        点击位置
        """
        with allure.step("点击位置"):
            self.steps("../../page_object/renthouse/brandapartmentlist.yaml")
        self.tsleep(1)
        return self

    def click_brandapartmentlist_price(self):
        """
        点击租金
        """
        with allure.step("点击租金"):
            self.steps("../../page_object/renthouse/brandapartmentlist.yaml")
        self.tsleep(1)
        return self


    def click_brandapartmentlist_selected(self):
        """
        点击筛选
        """
        with allure.step("点击筛选"):
            self.steps("../../page_object/renthouse/brandapartmentlist.yaml")
        self.tsleep(1)
        return self

    def click_brandapartmentlist_order(self):
        """
        点击排序
        """
        with allure.step("点击排序"):
            self.steps("../../page_object/renthouse/brandapartmentlist.yaml")
        self.tsleep(1)
        return self

    def click_brandapartmentlist_confirm(self):
        """
        点击确定
        """
        with allure.step("点击确定"):
            self.steps("../../page_object/renthouse/brandapartmentlist.yaml")
        self.tsleep(1)
        return self

    def click_brandapartmentlist_reset(self):
        """
        点击重置
        """
        with allure.step("点击重置"):
            self.steps("../../page_object/renthouse/brandapartmentlist.yaml")
        self.tsleep(1)
        return self

    def click_brandapartmentlist_house(self):
        """
        列表页第一个房源
        """
        with allure.step("列表页第一个房源"):
            self.steps("../../page_object/renthouse/brandapartmentlist.yaml")
        self.tsleep(1)
        return self

    def click_brandapartmentlist_search(self):
        """
        点击搜索框
        """
        with allure.step("点击搜索框"):
            self.steps("../../page_object/renthouse/brandapartmentlist.yaml")
        self.tsleep(1)
        return self



    def brandapartmentlist_swipe(self, pos_text=None):
        """
        滑动到pos_text的位置，滑动
        :param pos_text: 1、写入页面存在的元素
                         2、如果写pos_text=buttom，则滑动到页面底部
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step("滑动到" + self._params["pos_text"]):
            self.steps("../../page_object/renthouse/brandapartmentlist.yaml", replace=True)
        self.tsleep(1)
        return self






